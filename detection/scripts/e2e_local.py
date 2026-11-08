"""Full local loop: hub (:8190, temp DB) + P2 service (:8191) -> stream synthetic WAV to /stt -> watch hub WS /events for
transcript.caller -> risk.update -> alert.fired -> POST /user/action continue -> service log shows it. Prints ask->alert latency."""
import asyncio, json, os, subprocess, sys, tempfile, time, wave
from pathlib import Path
import httpx, numpy as np, websockets
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from detection import stream
HUB, P2, CALL = 8190, 8191, "c_e2e"
# call.incoming is hub-only (RESERVED), so the test hub publishes it in-process so /user/action accepts the call_id
HUB_BOOT = f"""
import uvicorn
from server.main import app
from server import bus
bus.publish('call.incoming', '{CALL}', {{'from': '+15555550123', 'to': '+15555550100', 'attestation': 'none', 'scam_id_score': 0.5}})
uvicorn.run(app, port={HUB}, log_level='warning')
"""

def ask_end_seconds(wav):
    """Seconds into the WAV where the 3rd utterance's speech ends (the gift-card ask), via the same VAD as the service."""
    w = wave.open(wav); pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    seg, closed, ends = stream.Segmenter(), 0, []
    for i in range(0, len(pcm) - 159, 160):
        n = len(seg.feed(pcm[i:i + 160]))
        if n: ends.append((i + 160) / 8000 - seg.end_frames * 0.02)
    return ends[2]

async def main():
    wav = str(ROOT / "detection/testdata/scam_call_synth.wav")
    tmp = tempfile.mkdtemp(); env = {k: v for k, v in os.environ.items() if k not in ("PIPELINE_TOKEN", "HUB_TOKEN")}
    env.update(HUB_DB=f"{tmp}/hub.db", HUB_URL=f"http://localhost:{HUB}", P2_ENGINE=os.environ.get("P2_ENGINE", "cloud"))
    py = str(ROOT / ".venv/bin/python")
    logf = open(f"{tmp}/p2.log", "w")
    procs = [subprocess.Popen([py, "-c", HUB_BOOT], cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL),
             subprocess.Popen([py, "-m", "uvicorn", "detection.app:app", "--port", str(P2)], cwd=ROOT, env=env, stdout=logf, stderr=subprocess.STDOUT)]
    ok = False
    try:
        async with httpx.AsyncClient() as h:
            for _ in range(40):
                try:
                    if (await h.get(f"http://localhost:{HUB}/healthz")).status_code == 200 and (await h.get(f"http://localhost:{P2}/healthz")).status_code == 200: break
                except Exception: pass
                await asyncio.sleep(0.25)
            else: raise SystemExit("FAIL: services did not start")
            await asyncio.sleep(1.5)                      # let P2 subscribe to hub WS
            events = []
            async def listen():
                async with websockets.connect(f"ws://localhost:{HUB}/events") as ws:
                    async for m in ws:
                        e = json.loads(m); e["_t"] = time.time(); events.append(e)
            lt = asyncio.create_task(listen()); await asyncio.sleep(0.5)
            t0 = time.time()
            sp = await asyncio.create_subprocess_exec(py, str(ROOT / "detection/scripts/stream_wav.py"), wav, "--url", f"ws://localhost:{P2}", "--call", CALL, cwd=ROOT, env=env)
            await sp.wait(); await asyncio.sleep(3)
            r = await h.post(f"http://localhost:{HUB}/user/action", json={"call_id": CALL, "action": "continue"})
            await asyncio.sleep(1.0); lt.cancel()
        kinds = [e["type"] for e in events if e["call_id"] == CALL]
        print("events seen:", {k: kinds.count(k) for k in dict.fromkeys(kinds)})
        alert = next((e for e in events if e["type"] == "alert.fired"), None)
        need = ["transcript.caller", "risk.update", "alert.fired", "user.action"]
        missing = [k for k in need if k not in kinds]
        saw = "user.action continue seen" in open(f"{tmp}/p2.log").read()
        print("user.action POST:", r.status_code, "| service saw continue:", saw)
        if alert:
            ask = t0 + ask_end_seconds(wav)       # end of the 3rd line, the gift-card ask
            gc = next((e for e in events if e["type"] == "risk.update" and "gift_card" in e["data"]["asks"]), None)
            if gc: print(f"ask(end of speech)->first risk.update with gift_card: {gc['_t'] - ask:+.2f} s (s={gc['data']['s']})")
            print(f"alert.fired level={alert['data']['level']} chips={alert['data']['why_chips']}")
            print(f"ask(end of speech)->FIRST alert.fired (may be earlier: IRS claim alone already scores high): {alert['_t'] - ask:+.2f} s (negative = fired before the ask finished)")
        ok = not missing and saw and alert is not None
        print("PASS" if ok else f"FAIL missing={missing} saw={saw}")
    finally:
        for p in procs: p.terminate()
    sys.exit(0 if ok else 1)
asyncio.run(main())
