#!/usr/bin/env python
"""Per-call timeline from the P2 log (rehearsal tool). Read-only; never prints keys; transcript text is cut to 60 chars.
Usage: call_report.py [logfile] [--call ID-or-prefix] [--last N]     (default logs/p2.log, last 3 calls)
Needs timestamped lines (app.py logging format); older untimestamped lines still parse but show '--' for time."""
import argparse, re, sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TS = re.compile(r"^(\d\d):(\d\d):(\d\d)\.(\d{3}) (\w+) (\S+) (.*)$")
OLD = re.compile(r"^(INFO|WARNING|ERROR):(p2\.\w+):(.*)$")
CID = r"([0-9A-Za-z_-]+?)"
PATS = [
    ("start", re.compile(r"stt ws (\S+) first frame")),
    ("close", re.compile(r"stt ws (\S+) closed: frames=(\{.*?\}) utterances=(\d+)")),
    ("final", re.compile(r"stt final (\S+)-u(\d+): ([\d.]+)s after endpoint: '(.*)'")),
    ("risk", re.compile(r"risk\.update call=(\S+) s=([\d.]+) band=(\S+) engine=(\S+) src=(\S+) asks=(\S+)")),
    ("alert", re.compile(r"alert\.fired call=(\S+) level=(\S+) src=(\S+) s=([\d.]+)")),
    ("cont", re.compile(r"user\.action continue seen call=(\S+)")),
    ("restore", re.compile(r"handoff\.restored seen call=(\S+)")),
    ("droplate", re.compile(r"drop late final: .* call=(\S+)")),
    ("dropstale", re.compile(r"drop stale result: .* call=(\S+)")),
    ("failover", re.compile(r"detect (\S+) failover: cloud (\S+) -> local")),
    ("failfail", re.compile(r"detect (\S+) failover to local failed: (\S+)")),
    ("rules", re.compile(r"detect (\S+) engine=(\S+) fell back to rules: (\S+)(?: status=(\d+))?")),
    ("demo", re.compile(r"(demo cache (?:fuzzy )?hit.*)")),
]

def secs(m): return int(m[0]) * 3600 + int(m[1]) * 60 + int(m[2]) + int(m[3]) / 1000

def parse(lines):
    calls, last = OrderedDict(), None
    day = 0.0; prev = None
    for ln in lines:
        ln = ln.rstrip("\n"); t = None; msg = None
        m = TS.match(ln)
        if m:
            t = secs(m.groups()[:4]); msg = m.group(7)
            if prev is not None and t < prev - 3600: day += 86400      # crossed midnight
            prev = t; t += day
        else:
            m = OLD.match(ln)
            if m: msg = m.group(3)
        if not msg: continue
        for kind, rx in PATS:
            mm = rx.search(msg)
            if not mm: continue
            g = mm.groups()
            cid = last if kind == "demo" else g[0]
            if cid is None: break
            c = calls.setdefault(cid, {"ev": [], "t0": t})
            if c["t0"] is None: c["t0"] = t
            c["ev"].append((t, kind, g if kind != "demo" else g))
            last = cid
            break
    return calls

def rel(t, t0): return "  --  " if t is None or t0 is None else f"{t - t0:+6.1f}"

def report(cid, c):
    t0, out = c["t0"], []
    n_alert = n_fo = n_429 = n_http = 0; first_alert = None; s_final = None; nfin = 0
    out.append(f"=== call {cid}")
    for t, k, g in c["ev"]:
        r = rel(t, t0)
        if k == "start": out.append(f"{r}s  ws open")
        elif k == "close": out.append(f"{r}s  ws closed frames={g[1]} utterances={g[2]}")
        elif k == "final": nfin += 1; out.append(f"{r}s  final u{g[1]}  {g[2]}s after endpoint  {g[3][:60]!r}")
        elif k == "risk": s_final = float(g[1]); out.append(f"{r}s  risk s={g[1]} band={g[2]} engine={g[3]} src={g[4]} asks={g[5]}")
        elif k == "alert":
            n_alert += 1; first_alert = first_alert if first_alert is not None else (t - t0 if t is not None and t0 is not None else -1)
            out.append(f"{r}s  ALERT {g[1]} ({'fast path (rules)' if g[2].startswith('fast') else 'LLM'}, src={g[2]}) s={g[3]}")
        elif k == "cont": out.append(f"{r}s  user Continue (window cleared)")
        elif k == "restore": out.append(f"{r}s  handoff restored")
        elif k == "droplate": out.append(f"{r}s  dropped late final (audio ended before Continue)")
        elif k == "dropstale": out.append(f"{r}s  dropped stale result (Continue mid-flight)")
        elif k == "failover": n_fo += 1; out.append(f"{r}s  FAILOVER cloud ({g[1]}) -> local")
        elif k == "failfail": out.append(f"{r}s  failover to local failed: {g[1]}")
        elif k == "rules":
            if g[3] == "429": n_429 += 1
            elif g[2] == "HTTPStatusError" and not g[3]: n_http += 1
            out.append(f"{r}s  engine {g[1]} fell back to rules: {g[2]}{' status=' + g[3] if g[3] else ''}")
        elif k == "demo": out.append(f"{r}s  {g[0]}   (attributed to the most recent call)")
    fa = "none" if first_alert is None else ("?" if first_alert < 0 else f"+{first_alert:.1f}s")
    out.append(f"SUMMARY {cid}: first alert {fa} · final s {'-' if s_final is None else f'{s_final:.2f}'} · alerts {n_alert} · failovers {n_fo} · 429s {n_429}"
               + (f" (+{n_http} HTTP errors with unknown status, older log format)" if n_http else "") + f" · finals {nfin}")
    return "\n".join(out)

def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("log", nargs="?", default=str(ROOT / "logs/p2.log"))
    ap.add_argument("--call"); ap.add_argument("--last", type=int, default=3)
    a = ap.parse_args(argv)
    try:
        with open(a.log, errors="replace") as f: calls = parse(f)
    except OSError as e:
        print(f"cannot read {a.log}: {e.strerror}", file=sys.stderr); return 2
    sel = [k for k in calls if a.call and k.startswith(a.call)] if a.call else list(calls)[-a.last:]
    if not sel: print("no matching calls"); return 1
    print("\n\n".join(report(k, calls[k]) for k in sel)); return 0

if __name__ == "__main__":
    sys.exit(main())
