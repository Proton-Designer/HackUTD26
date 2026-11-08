"""Acts like P1's relay (server/relay.py) against WS /decoy/{call_id}: streams caller sentences as Telnyx PCMU frames in
real time with pauses, records the decoy's audio (decoy_heard.wav). Usage:
  .venv-hub/bin/python decoy/tests/relay_sim.py ws://127.0.0.1:8300 out_dir seg0.wav seg1.wav ...  [--gap 9]"""
import asyncio, base64, json, sys, time, uuid, wave
import numpy as np, websockets
sys.path.insert(0, "."); from decoy.voice import to_pcmu_frames
from detection.stt import mulaw_decode

async def main(url, out, wavs, gap):
    cid = "sim-" + uuid.uuid4().hex[:8]; heard = []; got = {"media": 0, "clear": 0}
    async with websockets.connect(f"{url}/decoy/{cid}", max_size=None) as ws:
        await ws.send(json.dumps({"event": "connected", "protocol": "Call", "version": "1.0.0"}))
        await ws.send(json.dumps({"event": "start", "stream_id": "s1", "start": {"stream_id": "s1", "custom_parameters": {"call_id": cid},
                                  "media_format": {"encoding": "audio/x-mulaw", "sample_rate": 8000, "channels": 1}}}))
        async def rx():
            async for raw in ws:
                m = json.loads(raw); e = m.get("event")
                if e in got: got[e] += 1
                if e == "media": heard.append(base64.b64decode(m["media"]["payload"]))
                if e == "clear": print(time.strftime("%X"), "<- clear (barge-in)", flush=True)
        rt = asyncio.create_task(rx())
        silence = b"\xff" * 160
        async def send_frames(frames):
            t = time.monotonic()
            for i, f in enumerate(frames):
                await ws.send(json.dumps({"event": "media", "media": {"track": "inbound", "payload": base64.b64encode(f).decode()}}))
                d = t + (i + 1) * 0.02 - time.monotonic()
                if d > 0: await asyncio.sleep(d)
        await send_frames([silence] * int(4 / 0.02))     # let the opener play
        for w in wavs:
            wv = wave.open(w); pcm = wv.readframes(wv.getnframes())
            print(time.strftime("%X"), "-> caller says", w.split("/")[-1], flush=True)
            await send_frames(to_pcmu_frames(pcm, wv.getframerate()) + [silence] * int(gap / 0.02))
        await ws.send(json.dumps({"event": "stop"}))
        await asyncio.sleep(1); rt.cancel()
    pcm = mulaw_decode(b"".join(heard))
    with wave.open(f"{out}/decoy_heard.wav", "wb") as o: o.setnchannels(1); o.setsampwidth(2); o.setframerate(8000); o.writeframes(pcm.astype("<i2").tobytes())
    print("decoy audio received: %.1f s in %d frames; clears=%d; call_id=%s" % (len(pcm) / 8000, got["media"], got["clear"], cid))

args = [a for a in sys.argv[1:] if not a.startswith("--")]
gap = float(sys.argv[sys.argv.index("--gap") + 1]) if "--gap" in sys.argv else 9.0
if "--gap" in sys.argv: args.remove(sys.argv[sys.argv.index("--gap") + 1])
asyncio.run(main(args[0], args[1], args[2:], gap))
