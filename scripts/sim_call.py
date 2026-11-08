#!/usr/bin/env python3
"""Telnyx call simulator (TASK-012): drive the hub/voip like Telnyx would, no phone number needed. SIMULATED caller only.
  scripts/sim_call.py --from +15555550123 [--to +15555550100] [--attestation A|B|C|none] [--wav f.wav] [--tone] [--fast]
                      [--hub http://127.0.0.1:8000] [--webhook-path /telnyx/webhook] [--media-token T] [--dry-run]
Sends webhooks (call.initiated, call.answered, streaming.started, call.hangup) then the media WS (connected, start, media, stop).
Webhook/WS shapes follow Telnyx docs; shaken_stir_* location in the payload is UNVERIFIED (see voip/API_EVIDENCE.md).
Media WS auth: voip's spike requires ?t=<token> that only appears in its answer command's stream_url. Under SIM_MODE voip should
return it as {"stream_url": ...} in the webhook response; else pass --media-token. If voip isn't mounted: prints plan, exit 0."""
import argparse, asyncio, base64, json, math, sys, time, uuid, wave, urllib.request, urllib.error
from datetime import datetime, timezone

def lin2ulaw(s):
    s = max(-32635, min(32635, s)); sign = 0x80 if s < 0 else 0
    s = abs(s) + 132; e = s.bit_length() - 8; m = (s >> (e + 3)) & 0x0F
    return ~(sign | (e << 4) | m) & 0xFF

def pcmu_from_wav(path):
    with wave.open(path, "rb") as w:
        if (w.getframerate(), w.getnchannels(), w.getsampwidth()) != (8000, 1, 2):
            sys.exit("WAV must be 8 kHz mono 16-bit PCM (scripts/make_scam_wav.sh makes one)")
        raw = w.readframes(w.getnframes())
    return bytes(lin2ulaw(int.from_bytes(raw[i:i + 2], "little", signed=True)) for i in range(0, len(raw) - 1, 2))

def pcmu_tone(hz=440, secs=3.0):
    return bytes(lin2ulaw(int(6000 * math.sin(2 * math.pi * hz * i / 8000))) for i in range(int(8000 * secs)))

def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def webhook(event_type, p):
    return {"data": {"event_type": event_type, "id": str(uuid.uuid4()), "occurred_at": now(), "record_type": "event", "payload": p},
            "meta": {"attempt": 1, "delivered_to": "simulator"}}

def post(url, body):
    req = urllib.request.Request(url, json.dumps(body).encode(), {"content-type": "application/json", "x-sim-call": "1", "x-hub-token": __import__("os").environ.get("HUB_TOKEN", "")})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            raw = r.read().decode() or "{}"
            try: return r.status, json.loads(raw)
            except ValueError: return r.status, {}
    except urllib.error.HTTPError as e:
        return e.code, {}
    except Exception as e:
        return None, {"error": str(e)}

async def listen(hub_ws, sid, seen, ready):
    import websockets
    try:
        async with websockets.connect(f"{hub_ws}/events?call_id={sid}") as ws:
            ready.set()
            async for m in ws:
                ev = json.loads(m); seen.append(ev); print(f"  hub event: {ev['type']} {json.dumps(ev['data'])[:90]}")
    except Exception:
        ready.set()

async def main():
    a = argparse.ArgumentParser()
    a.add_argument("--from", dest="frm", required=True); a.add_argument("--to", default="+15555550100")
    a.add_argument("--attestation", default="none", choices=["A", "B", "C", "none"])
    a.add_argument("--script", choices=["irs", "bank", "crypto", "benign"], help="voice a synthetic card with macOS say + ffmpeg (voip/test_call.py), real-time paced")
    a.add_argument("--wav"); a.add_argument("--tone", action="store_true"); a.add_argument("--fast", action="store_true")
    a.add_argument("--hub", default="http://127.0.0.1:8000"); a.add_argument("--webhook-path", default="/telnyx/webhook")
    a.add_argument("--media-token", default=""); a.add_argument("--dry-run", action="store_true")
    a = a.parse_args()
    sid = str(uuid.uuid4()); ccid = "v3:sim_" + uuid.uuid4().hex[:24]; leg = str(uuid.uuid4())
    hub_ws = a.hub.replace("http", "ws", 1); hook = a.hub + a.webhook_path
    base = {"call_control_id": ccid, "call_session_id": sid, "call_leg_id": leg, "from": a.frm, "to": a.to, "connection_id": "sim", "client_state": None}
    init = dict(base, direction="incoming", state="parked", start_time=now())
    if a.attestation != "none":
        init["shaken_stir_attestation"] = a.attestation; init["shaken_stir_validated"] = True  # location UNVERIFIED
    steps = [("call.initiated", init), ("call.answered", dict(base, direction="incoming", state="answered")),
             ("streaming.started", dict(base, stream_type="websocket")), ("call.hangup", dict(base, direction="incoming", state="hangup", hangup_cause="normal_clearing", hangup_source="caller"))]
    print(f"SIMULATED call {sid}: {a.frm} -> {a.to} attestation={a.attestation}")
    if a.dry_run:
        for et, p in steps: print(f"would POST {hook}: {et}")
        print(f"would connect {hub_ws}/media/{sid} and stream PCMU 8 kHz 20 ms frames (connected,start,media...,stop)"); return 0
    seen, ready = [], asyncio.Event()
    lt = asyncio.create_task(listen(hub_ws, sid, seen, ready)); await asyncio.wait_for(ready.wait(), 3)
    st, resp = post(hook, webhook(*steps[0]))
    if st is None or st == 404:
        print(f"voip not mounted / hub down ({st} {resp.get('error', '')}); nothing sent beyond this probe. Exit 0.")
        for et, p in steps: print(f"would POST {hook}: {et}")
        lt.cancel(); return 0
    print(f"POST call.initiated -> {st}")
    await asyncio.sleep(1.5)  # let routing/answer happen
    dec = next((e["data"].get("decision") for e in seen if e["type"] == "call.routed"), None)
    if dec == "BLOCKED_BACKFIRE":
        print("REJECTED before ring (BLOCKED_BACKFIRE): no media sent"); post(hook, webhook(*steps[3]))
        await asyncio.sleep(0.5); lt.cancel(); return 0
    print("POST call.answered ->", post(hook, webhook(*steps[1]))[0])
    print("POST streaming.started ->", post(hook, webhook(*steps[2]))[0])
    su = resp.get("stream_url")
    if su:   # the hub may hand back its PUBLIC ws base (PUBLIC_WS/tunnel); sim media must come straight to the local hub (loopback-only), keep path+token
        from urllib.parse import urlsplit
        u = urlsplit(su); su = f"{hub_ws}{u.path}" + (f"?{u.query}" if u.query else "")
    url = su or f"{hub_ws}/media/{sid}" + (f"?t={a.media_token}" if a.media_token else "")
    if a.script and not a.wav:
        import pathlib, subprocess, tempfile
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "voip"))
        import test_call as tc
        d = tempfile.mkdtemp(prefix="bf_sim_"); mp3 = tc.make_audio(a.script, d); a.wav = str(pathlib.Path(d) / "s.wav")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "8000", "-ac", "1", "-c:a", "pcm_s16le", a.wav], check=True)
    if not a.wav and not a.tone:   # default: the SAME file the hub serves at GET /demo/caller.wav (env DEMO_CALLER_WAV, else $LOGDIR/sim_scam.wav)
        import os, pathlib
        root = pathlib.Path(__file__).resolve().parent.parent
        w = pathlib.Path(os.environ.get("DEMO_CALLER_WAV") or (pathlib.Path(os.environ.get("LOGDIR") or "logs") / "sim_scam.wav"))
        w = w if w.is_absolute() else root / w
        if w.is_file(): a.wav = str(w); print(f"caller audio: {w} (same file as GET /demo/caller.wav)")
        else: print(f"no caller WAV at {w} (run scripts/make_scam_wav.sh or set DEMO_CALLER_WAV); using a 3 s tone")
    audio = pcmu_from_wav(a.wav) if a.wav else pcmu_tone()
    frames = [audio[i:i + 160] for i in range(0, len(audio), 160)]
    import websockets
    sent = 0
    try:
        async with websockets.connect(url) as ws:
            sj = lambda o: ws.send(json.dumps(o))
            back = {"media": 0}
            async def rx():
                try:
                    async for m in ws:
                        try: back["media"] += 1 if json.loads(m).get("event") == "media" else 0
                        except Exception: pass
                except Exception: pass
            rxt = asyncio.create_task(rx())
            await sj({"event": "connected", "protocol": "Call", "version": "1.0.0"})
            await sj({"event": "start", "sequence_number": "1", "stream_id": "sim-stream",
                      "start": {"call_control_id": ccid, "call_session_id": sid, "stream_id": "sim-stream", "tracks": ["inbound"],
                                "media_format": {"encoding": "audio/x-mulaw", "sample_rate": 8000, "channels": 1}}})
            for i, f in enumerate(frames):
                await sj({"event": "media", "sequence_number": str(i + 2), "stream_id": "sim-stream",
                          "media": {"track": "inbound", "chunk": str(i + 1), "timestamp": str(i * 20), "payload": base64.b64encode(f).decode()}})
                sent += 1
                if not a.fast: await asyncio.sleep(0.02)
            await sj({"event": "stop", "sequence_number": str(len(frames) + 2), "stream_id": "sim-stream", "stop": {"call_control_id": ccid}})
            await asyncio.sleep(0.5); rxt.cancel()
            print(f"frames returned to the caller (decoy/echo audio): {back['media']}")
    except Exception as e:
        print(f"media WS failed ({type(e).__name__}: {str(e)[:80]}); pass --media-token if voip needs ?t=")
    print(f"sent {sent} media frames ({sent * 20 / 1000:.1f}s of SIMULATED caller audio)")
    print("POST call.hangup ->", post(hook, webhook(*steps[3]))[0])
    await asyncio.sleep(1); lt.cancel()
    print("hub events seen:", sorted({e["type"] for e in seen}))
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
