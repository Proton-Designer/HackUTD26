"""Test client: stream a WAV to WS /stt/{call_id} as Telnyx frames at real time; print transcripts + latency.
Transcripts are read from the hub WS /events (need hub running) OR, with --local, the service log. Usage:
  python detection/scripts/stream_wav.py [wav] [--url ws://localhost:8100] [--call c_test]"""
import argparse, asyncio, base64, json, time, wave
import numpy as np, websockets

def mulaw_encode(pcm):
    x = np.clip(pcm.astype(np.int32), -32635, 32635); s = (x < 0); x = np.abs(x) + 0x84
    e = np.clip(np.floor(np.log2(np.maximum(x, 1))).astype(int) - 7, 0, 7)
    m = (x >> (e + 3)) & 0x0F
    return (~(((s.astype(int) << 7) | (e << 4) | m)) & 0xFF).astype(np.uint8).tobytes()

async def main(a):
    w = wave.open(a.wav); assert w.getframerate() == 8000 and w.getnchannels() == 1
    pcm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")
    async with websockets.connect(f"{a.url}/stt/{a.call}") as ws:
        await ws.send(json.dumps({"event": "connected"}))
        await ws.send(json.dumps({"event": "start", "start": {"media_format": {"encoding": "PCMU"}}}))
        t0 = time.time()
        for i in range(0, len(pcm) - 159, 160):
            await ws.send(json.dumps({"event": "media", "media": {"track": "inbound", "payload": base64.b64encode(mulaw_encode(pcm[i:i+160])).decode()}}))
            await asyncio.sleep(max(0, t0 + (i + 160) / 8000 - time.time()))
        print(f"sent {len(pcm)/8000:.1f}s of audio; stop")
        await ws.send(json.dumps({"event": "stop"}))
        try:
            await asyncio.wait_for(ws.wait_closed(), 20)
        except Exception:
            pass
if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("wav", nargs="?", default="detection/testdata/scam_call_synth.wav")
    p.add_argument("--url", default="ws://localhost:8100"); p.add_argument("--call", default="c_test")
    asyncio.run(main(p.parse_args()))
