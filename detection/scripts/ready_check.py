#!/usr/bin/env python3
"""TASK-050: one-command readiness check for the freeze and judging. READ-ONLY (one /detect control pair, nothing is changed or killed).
  bash detection/scripts/ready_check.sh [--live URL] [--tunnel URL] [--tests] [--no-detect]
Each check prints PASS/FAIL/WARN/SKIP with a one-line fix hint. Never prints .env values or env values (only key presence / booleans)."""
import argparse, json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path
TAG_RE = re.compile(r"^p2-known-good-")

# ---------- pure parts (unit-tested) ----------
def check_health(h):
    """healthz dict -> [(name, state, detail, hint)]. state in PASS/FAIL/WARN."""
    out = []
    def add(n, ok, d, hint, warn=False): out.append((n, "PASS" if ok else ("WARN" if warn else "FAIL"), d, "" if ok else hint))
    e, st, br = h.get("engines") or {}, h.get("stt") or {}, h.get("cloud_breaker") or {}
    add("healthz ok", h.get("ok") is True, f"ok={h.get('ok')}", "restart p2svc (Ctrl-C twice in its window, rerun run.sh)")
    add("engines.primary == local", e.get("primary") == "local", f"primary={e.get('primary')}", "start P2 with P2_ENGINE=local (DEMO_DAY step 2)")
    add("llama reachable (local_reachable)", e.get("local_reachable") is True, f"local_reachable={e.get('local_reachable')} probe_ms={e.get('local_probe_ms')}", "start llama: detection/engines/run_local_llm.sh in backfire-p2-eng:llama")
    add("cloud breaker closed", br.get("state") == "closed", f"state={br.get('state')} retry_in_s={br.get('retry_in_s')}", "NVIDIA key throttled; local is primary so OK for the demo, wait for the half-open probe", warn=True)
    add("STT primary not bypassed", st.get("primary_bypassed") is False, f"backend={st.get('backend')} bypassed={st.get('primary_bypassed')} failures={st.get('primary_failures')}", "Riva failing: Whisper fallback is in use (slower); check NVIDIA key/network", warn=True)
    add("whisper fallback loaded", st.get("whisper_fallback_loaded") is True, f"loaded={st.get('whisper_fallback_loaded')}", "warmup runs ~10-15 s after start (P2_STT_WARMUP=1); if it stays unloaded, restart p2svc and check the log for 'stt warmup failed'", warn=True)
    n = h.get("active_stt_sockets")
    add("no active STT sockets", n == 0, f"active_stt_sockets={n}", "a call is in progress: do not run anything heavy; re-check after it ends", warn=True)
    return out

def tunnel_matches(local, tunnel):
    """Tunnel healthz must show the same wiring as local."""
    keys = [("ok",), ("engine",), ("engines", "primary")]
    def g(d, k):
        for x in k: d = (d or {}).get(x) if isinstance(d, dict) else None
        return d
    diff = [".".join(k) for k in keys if g(local, k) != g(tunnel, k)]
    return not diff, ("same ok/engine/primary" if not diff else "differs in " + ",".join(diff))

def env_flag(environ_bytes, key="P2_DUMP_AUDIO"):
    """/proc/<pid>/environ bytes -> ('on'|'off'|'unset'). Reads ONLY the named key; never returns other values."""
    for kv in environ_bytes.split(b"\0"):
        if kv.startswith(key.encode() + b"="):
            return "on" if kv.split(b"=", 1)[1].decode(errors="ignore").strip() == "1" else "off"
    return "unset"

def tag_status(head, tag_map):
    """head sha, {tag: sha} -> (ok, detail)."""
    hit = sorted(t for t, s in tag_map.items() if s == head and TAG_RE.match(t))
    if hit: return True, f"HEAD {head[:7]} == {hit[-1]}"
    latest = sorted((t for t in tag_map if TAG_RE.match(t)))
    return False, f"HEAD {head[:7]} matches no p2-known-good tag (latest tag {latest[-1] if latest else 'none'})"

def stale_code(proc_start_ts, last_detection_commit_ts):
    """True when detection/ code was committed after the process started (the live process runs older code than HEAD)."""
    return last_detection_commit_ts > proc_start_ts + 1

def controls(pos, neg):
    """/detect results -> [(name, ok, detail)]; positive must be critical, negative low."""
    return [("positive control (gift card + secrecy) -> critical", isinstance(pos, dict) and pos.get("band") == "critical", f"band={pos.get('band') if isinstance(pos, dict) else None} s={pos.get('s') if isinstance(pos, dict) else None}"),
            ("negative control (benign) -> low", isinstance(neg, dict) and neg.get("band") == "low", f"band={neg.get('band') if isinstance(neg, dict) else None} s={neg.get('s') if isinstance(neg, dict) else None}")]

# ---------- I/O parts ----------
def jget(url, timeout=5):
    with urllib.request.urlopen(url, timeout=timeout) as r: return json.loads(r.read().decode())

def listener_pid(port):
    try:
        o = subprocess.run(["ss", "-ltnp"], capture_output=True, text=True, timeout=5).stdout
        for l in o.splitlines():
            if re.search(rf":{port}\s", l):
                m = re.search(r"pid=(\d+)", l)
                if m: return int(m.group(1))
    except Exception: pass
    return None

def env_token(root):
    f = Path(root) / ".env"
    try:
        for l in f.read_text().splitlines():
            if l.startswith("PIPELINE_TOKEN="): return l.split("=", 1)[1].strip().strip("'\"")
    except Exception: pass
    return os.environ.get("PIPELINE_TOKEN", "")

def post_detect(base, text, token):
    h = {"content-type": "application/json"}
    if token: h["x-pipeline-token"] = token
    req = urllib.request.Request(base + "/detect", json.dumps({"call_id": "ready-check", "window_text": text, "engine": "local"}).encode(), h)
    with urllib.request.urlopen(req, timeout=15) as r: return json.loads(r.read().decode())

def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=300).stdout.strip()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--live", default="http://127.0.0.1:8100"); ap.add_argument("--tunnel"); ap.add_argument("--tests", action="store_true"); ap.add_argument("--no-detect", action="store_true")
    a = ap.parse_args(); live = a.live.rstrip("/")
    rows = []
    def add(n, st, d="", hint=""): rows.append((n, st, d, hint))
    port = int(re.search(r":(\d+)$", live).group(1)) if re.search(r":(\d+)$", live) else 8100
    try: h = jget(live + "/healthz")
    except Exception as e:
        add("healthz reachable", "FAIL", type(e).__name__, "P2 is down: restart p2svc (bash detection/scripts/run.sh); the watchdog should do this within ~60 s"); h = None
    if h:
        rows += check_health(h)
        if a.tunnel:
            try:
                t = jget(a.tunnel.rstrip("/") + "/healthz"); ok, d = tunnel_matches(h, t); add("tunnel healthz matches live", "PASS" if ok else "FAIL", d, "" if ok else "tunnel points at a different/stale service: restart bash detection/scripts/tunnel.sh and give P1 the new URL")
            except Exception as e: add("tunnel healthz matches live", "FAIL", type(e).__name__, "tunnel down: bash detection/scripts/tunnel.sh, then tell P1 the new URL")
    pid = listener_pid(port); root = None
    if pid is None: add("live process found", "WARN", f"no listener pid on :{port} visible", "run this check as the same user that runs P2")
    else:
        try:
            root = os.readlink(f"/proc/{pid}/cwd")
            fl = env_flag(Path(f"/proc/{pid}/environ").read_bytes())
            add("P2_DUMP_AUDIO off in live process", "PASS" if fl != "on" else "FAIL", f"P2_DUMP_AUDIO={fl}", "restart p2svc without P2_DUMP_AUDIO=1 (caller audio must not be kept on stage)")
            ad = Path(root) / "logs/audio"; n = len(list(ad.glob("*"))) if ad.exists() else 0
            add("logs/audio empty", "PASS" if n == 0 else "FAIL", f"{n} files in {ad}", "rm -f logs/audio/*.wav (in the live checkout)")
        except Exception as e: add("live process env/cwd", "WARN", type(e).__name__, "cannot read /proc for the live pid (different user?)")
    if root:
        try:
            head = sh(["git", "rev-parse", "HEAD"], root); tags = {}
            for l in sh(["git", "tag", "--list", "p2-known-good-*", "--format=%(refname:short) %(objectname) %(*objectname)"], root).splitlines():
                p = l.split(); tags[p[0]] = (p[2] if len(p) > 2 else p[1])
            ok, d = tag_status(head, tags); add("live HEAD is a p2-known-good tag", "PASS" if ok else "FAIL", d, "" if ok else "deploy only a tagged commit: git checkout p2-known-good-<latest>, restart p2svc (or tag this HEAD after the lead accepts it)")
            dirty = sh(["git", "status", "--porcelain", "--", "detection"], root)
            add("detection/ clean in live checkout", "PASS" if not dirty else "FAIL", "clean" if not dirty else f"{len(dirty.splitlines())} changed paths", "commit or discard local edits in detection/ before judging")
            st = float(sh(["bash", "-c", f"date -d \"$(ps -o lstart= -p {pid})\" +%s"], root) or 0); lc = float(sh(["git", "log", "-1", "--format=%ct", "--", ":(glob)detection/*.py"], root) or 0)
            add("live process newer than last detection/*.py commit", "PASS" if not stale_code(st, lc) else "FAIL", f"process started {time.strftime('%H:%M:%S', time.localtime(st))}, last runtime commit {time.strftime('%H:%M:%S', time.localtime(lc))}", "live runs older code than HEAD: restart p2svc (not during a judge visit)")
        except Exception as e: add("git checks", "WARN", type(e).__name__, "run from the live checkout")
        if a.tests:
            try:
                r = subprocess.run([".venv/bin/python", "-m", "pytest", "-q", "detection"], cwd=root, capture_output=True, text=True, timeout=600)
                add("pytest detection", "PASS" if r.returncode == 0 else "FAIL", (r.stdout.strip().splitlines() or [""])[-1], "" if r.returncode == 0 else "fix before the freeze")
            except Exception as e: add("pytest detection", "WARN", type(e).__name__, "")
    try:
        lu = os.environ.get("LOCAL_LLM_URL") or f"http://{subprocess.run(['ip', 'route'], capture_output=True, text=True).stdout.split('default via ')[1].split()[0]}:8101"
        d = jget(lu.rstrip("/") + "/v1/models", 3); add("llama /v1/models answers", "PASS" if d.get("models") or d.get("data") else "FAIL", lu, "start llama (detection/engines/run_local_llm.sh)")
    except Exception as e: add("llama /v1/models answers", "FAIL", type(e).__name__, "start llama (detection/engines/run_local_llm.sh in backfire-p2-eng:llama); set LOCAL_LLM_URL if it is not the WSL gateway")
    wd = subprocess.run(["bash", "-c", "ps -eo args | grep -c '[w]atchdog.sh'"], capture_output=True, text=True).stdout.strip()
    add("watchdog process alive", "PASS" if wd not in ("", "0") else "FAIL", f"{wd} watchdog.sh process(es)", "bash detection/scripts/watchdog.sh in its own tmux window")
    if a.no_detect or not h: add("detect controls", "SKIP", "skipped" if a.no_detect else "healthz down", "")
    elif h.get("active_stt_sockets", 0) != 0: add("detect controls", "SKIP", "a call is active (shared llama): not sending controls", "re-run after the call")
    else:
        tok = env_token(root or ".")
        try:
            pos = post_detect(live, "Go buy gift cards at the store and read me the numbers on the back, and do not tell anyone about this.", tok)
            neg = post_detect(live, "Hi, just checking you are still coming to the picnic on Saturday, the weather looks nice.", tok)
            for n, ok, d in controls(pos, neg): add(n, "PASS" if ok else "FAIL", d, "" if ok else "detector not scoring as expected: check engines/healthz, then eval/RESULTS.md")
        except Exception as e: add("detect controls", "FAIL", type(e).__name__ + " (bad token / service down?)", "check PIPELINE_TOKEN in .env matches the running process; healthz first")
    w = max(len(r[0]) for r in rows)
    for n, st, d, hint in rows: print(f"{st:4} {n:{w}}  {d}" + (f"\n     -> {hint}" if hint and st not in ("PASS", "SKIP") else ""))
    fails = [r for r in rows if r[1] == "FAIL"]
    print(f"\nREADY" if not fails else f"\nNOT READY: {len(fails)} FAIL ({sum(r[1]=='WARN' for r in rows)} warn)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
