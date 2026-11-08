#!/usr/bin/env python3
"""Automated SIMULATED scam-caller test call (synthetic voice, synthetic script cards). Account-agnostic.

  voip/.venv/bin/python voip/test_call.py --script irs|bank|crypto|benign            # DRY RUN (default): builds audio, prints the curl (key redacted)
  voip/.venv/bin/python voip/test_call.py --script irs --live                 # serves audio via local http.server + cloudflared quick tunnel, then POST /v2/calls

How it works: macOS `say` voices the script card (data/script-cards.md: numbered lines + payment step) -> ffmpeg -> 8 kHz mono mp3,
served from a spare local port (default 8799, never the hub's :8000) through a cloudflared quick tunnel; Telnyx dials
POST /v2/calls {connection_id=TELNYX_CALL_CONTROL_APP_ID, from=to=TELNYX_SCAM_LINE, audio_url, time_limit_secs}. The call goes into the
scam line, i.e. the hub's webhook, like a judge calling in. Needs outbound termination on the Telnyx account (the trial account blocks it).
Env (from .env: `set -a; . ./.env; set +a`): TELNYX_API_KEY, TELNYX_CALL_CONTROL_APP_ID, TELNYX_SCAM_LINE. Never prints the key."""
import argparse, json, os, pathlib, re, shutil, subprocess, sys, tempfile, threading, time, urllib.error, urllib.request
import http.server, functools

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = ROOT / "data" / "script-cards.md"
CARD_NO = {"irs": 1, "bank": 2, "crypto": 3}
# benign: synthetic legitimate call (no urgency, no money, no secrecy) so P2 risk stays low -> restore test (LIVE_TEST_PLAN restore check)
BENIGN = [
    "Hi, this is the front desk at Lakeside Family Dental calling to confirm your cleaning appointment this Thursday at two thirty.",
    "There is nothing you need to do. If the time does not work, just call the office during business hours and we will find another slot.",
    "We also have a reminder that your next visit is covered by your usual plan, so there is no change to your costs.",
    "Thanks so much, and we will see you Thursday. Have a lovely evening.",
]
VOICE = {"irs": "Daniel", "bank": "Samantha", "crypto": "Alex", "benign": "Samantha"}   # macOS built-in voices; falls back to the default voice
PAUSE_S = 2.5   # silence between lines so the live guard / "Maria" has room to respond


def card_text(script):
    if script == "benign": return list(BENIGN)
    """Spoken lines of one card: the numbered lines, then the payment step (says the callback/site/wallet as written)."""
    md = CARDS.read_text()
    m = re.search(rf"^# Card {CARD_NO[script]}:.*?(?=^# Card |\Z)", md, re.S | re.M)
    if not m: sys.exit(f"card {CARD_NO[script]} not found in {CARDS}")
    sec = m.group(0)
    lines = [re.sub(r"\s+", " ", x).strip() for x in re.findall(r'^\d+\.\s+\*\*"(.*?)"\*\*', sec, re.M)]
    pay = re.search(r'### Payment step.*?\*\*"(.*?)"\*\*', sec, re.S)
    if pay: lines.append(re.sub(r"\s+", " ", pay.group(1)).strip())
    if not lines: sys.exit("no lines parsed from card")
    return [l.replace("1-888-555-0123", "1, 8 8 8, 5 5 5, 0 1 2 3") for l in lines]


def make_audio(script, outdir):
    """say per line -> concat with silence -> 8 kHz mono mp3. Returns the mp3 path."""
    for tool in ("say", "ffmpeg"):
        if not shutil.which(tool): sys.exit(f"{tool} not found (macOS + ffmpeg required)")
    outdir = pathlib.Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    parts = []
    for i, line in enumerate(card_text(script)):
        a = outdir / f"l{i}.aiff"
        r = subprocess.run(["say", "-v", VOICE[script], "-o", str(a), line], capture_output=True)
        if r.returncode:   # voice missing: default voice
            subprocess.run(["say", "-o", str(a), line], check=True)
        parts.append(a)
    inputs, filt = [], []
    for i, a in enumerate(parts):
        inputs += ["-i", str(a)]
        filt.append(f"[{i}:a]aresample=8000,aformat=channel_layouts=mono,apad=pad_dur={PAUSE_S}[a{i}]")
    cat = "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[o]"
    mp3 = outdir / f"{script}.mp3"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt) + ";" + cat, "-map", "[o]",
                    "-ar", "8000", "-ac", "1", "-b:a", "32k", str(mp3)], check=True)
    return mp3


def duration_s(mp3):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)], capture_output=True, text=True).stdout
        return float(out.strip())
    except Exception:
        return 60.0


def body_for(audio_url, line, limit):
    return {"connection_id": os.environ.get("TELNYX_CALL_CONTROL_APP_ID", "<TELNYX_CALL_CONTROL_APP_ID>"), "to": line, "from": line,
            "audio_url": audio_url, "time_limit_secs": limit}


def print_curl(body):
    print("curl -sS -X POST https://api.telnyx.com/v2/calls \\\n  -H 'Authorization: Bearer ***REDACTED***' -H 'Content-Type: application/json' \\\n  -d '" + json.dumps(body) + "'")


def start_tunnel(port, timeout=25):
    p = subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--url", f"http://127.0.0.1:{port}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    url, t0 = None, time.time()
    def pump():
        nonlocal url
        for l in p.stdout:
            m = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", l)
            if m and not url: url = m.group(0)
    threading.Thread(target=pump, daemon=True).start()
    while not url and time.time() - t0 < timeout and p.poll() is None: time.sleep(0.3)
    if not url: p.terminate(); sys.exit("cloudflared gave no tunnel URL")
    return p, url


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--script", choices=list(CARD_NO) + ["benign"], required=True)
    ap.add_argument("--live", action="store_true", help="really place the call (default is a dry run)")
    ap.add_argument("--dry-run", action="store_true", help="explicit dry run (the default)")
    ap.add_argument("--port", type=int, default=8799, help="spare local port for the audio server (never 8000)")
    ap.add_argument("--time-limit", type=int, default=0, help="time_limit_secs (default: audio length + 15)")
    ap.add_argument("--keep", action="store_true", help="keep generated audio")
    ap.add_argument("--wav-out", help="only write the script audio as an 8 kHz mono 16-bit WAV to this path (e.g. logs/sim_scam.wav) and exit; no call")
    a = ap.parse_args()
    if a.port == 8000: sys.exit("refusing port 8000 (the hub)")
    if a.wav_out:
        w = tempfile.mkdtemp(prefix="bf_wav_"); mp3 = make_audio(a.script, w)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "8000", "-ac", "1", "-c:a", "pcm_s16le", a.wav_out], check=True)
        shutil.rmtree(w, ignore_errors=True); print(f"wrote {a.wav_out} ({duration_s(a.wav_out):.0f} s, script={a.script}, synthetic voice)"); return
    live = a.live and not a.dry_run
    work = tempfile.mkdtemp(prefix=f"bf_testcall_{a.script}_")
    mp3 = make_audio(a.script, work); dur = duration_s(mp3); limit = a.time_limit or int(dur) + 15
    line = os.environ.get("TELNYX_SCAM_LINE", "<TELNYX_SCAM_LINE>")
    print(f"script={a.script} voice={VOICE[a.script]} audio={mp3} ({dur:.0f}s, 8 kHz mono mp3) time_limit_secs={limit}")
    if not live:
        print("DRY RUN (add --live to place the call). The request that would be sent:"); print_curl(body_for(f"https://<tunnel>.trycloudflare.com/{a.script}.mp3", line, limit))
        if not a.keep: shutil.rmtree(work, ignore_errors=True)
        return
    for k in ("TELNYX_API_KEY", "TELNYX_CALL_CONTROL_APP_ID", "TELNYX_SCAM_LINE"):
        if not os.environ.get(k): sys.exit(f"{k} not set (run: set -a; . ./.env; set +a)")
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=work)
    handler.log_message = lambda *x, **k: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", a.port), handler); threading.Thread(target=srv.serve_forever, daemon=True).start()
    tun, base = start_tunnel(a.port)
    try:
        url = f"{base}/{a.script}.mp3"
        for _ in range(20):   # best-effort local reachability check; a fresh quick-tunnel name can fail on THIS machine's DNS cache while Telnyx resolves it fine
            try:
                if urllib.request.urlopen(url, timeout=4).status == 200: print("tunnel serves the audio"); break
            except Exception: time.sleep(1)
        else: print("WARNING: could not fetch the audio through the tunnel from here (local DNS?); dialing anyway, Telnyx resolves it itself")
        body = body_for(url, line, limit)
        req = urllib.request.Request("https://api.telnyx.com/v2/calls", json.dumps(body).encode(), {"Authorization": "Bearer " + os.environ["TELNYX_API_KEY"], "Content-Type": "application/json"})
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=15).read()); d = r.get("data", {})
            print("DIALED:", {k: d.get(k) for k in ("call_control_id", "call_session_id", "call_leg_id", "is_alive")})
        except urllib.error.HTTPError as e:   # e.g. 403/422 'Account is disabled D17' on the trial account
            print("DIAL FAILED:", e.code, e.read().decode()[:400]); sys.exit(2)
        print(f"holding audio server up {limit}s; Ctrl-C to stop early"); time.sleep(limit)
    except KeyboardInterrupt:
        pass
    finally:
        tun.terminate(); srv.shutdown()
        if not a.keep: shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
