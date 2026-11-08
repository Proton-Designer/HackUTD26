import base64, json
import numpy as np
from fastapi.testclient import TestClient
from detection import stt, stream, app as appmod

def mulaw_enc(x):  # reference encoder (independent of the decoder table)
    x = int(np.clip(x, -32635, 32635)); sign = 0x80 if x < 0 else 0; x = abs(x) + 0x84
    e = 7
    while e > 0 and not (x & (1 << (e + 7))): e -= 1
    return ~(sign | (e << 4) | ((x >> (e + 3)) & 0x0F)) & 0xFF

def test_mulaw_roundtrip():
    xs = [0, 100, -100, 1000, -5000, 12000, -30000]
    dec = stt.mulaw_decode(bytes(mulaw_enc(v) for v in xs))
    for v, d in zip(xs, dec):
        assert abs(int(d) - v) <= max(40, abs(v) * 0.04), (v, d)

def media(pcm_bytes, track="inbound"):
    return json.dumps({"event": "media", "media": {"track": track, "payload": base64.b64encode(pcm_bytes).decode()}})

def test_parse_frame_track_filter_and_garbage():
    assert stream.parse_frame(media(b"\xff" * 160))[0] == "media"
    assert stream.parse_frame(media(b"\xff" * 160, "outbound")) == ("media_other_track", None)
    for bad in ["", "not json", "[]", "null", '{"event":"media"}', '{"event":"media","media":{"payload":"!!!"}}', "123"]:
        ev, a = stream.parse_frame(bad)
        assert a is None or ev == "media"
    assert stream.parse_frame('{"event":"stop"}') == ("stop", None)

def tone(sec, amp=6000):
    t = np.arange(int(8000 * sec)); return (amp * np.sin(2 * np.pi * 300 * t / 8000)).astype(np.int16)

def test_segmenter_endpoints_two_utterances():
    s = Seg = stream.Segmenter()
    sil = np.zeros(8000, np.int16)
    out = s.feed(np.concatenate([sil, tone(1.0), sil, tone(0.8), sil]))
    assert len(out) == 2 and 0.9 < len(out[0]) / 8000 < 1.8

def test_segmenter_ignores_blips_and_silence():
    s = stream.Segmenter()
    assert s.feed(np.concatenate([np.zeros(8000, np.int16), tone(0.08), np.zeros(8000, np.int16)])) == []

class FakeSTT(stt.STT):
    name = "fake"
    async def transcribe(self, pcm): return "hello gift cards"

def test_ws_end_to_end_fail_open_and_on_final(monkeypatch):
    emitted, finals = [], []
    async def fake_emit(t, c, d): emitted.append((t, c, d)); return True
    async def fake_final(c, u): finals.append((c, u))
    monkeypatch.setattr(stream.hub, "emit", fake_emit); monkeypatch.setattr(stream, "on_final", fake_final)
    stt.set_stt(FakeSTT()); monkeypatch.setattr(stream, "PARTIALS", False)
    pcm = np.concatenate([np.zeros(4000, np.int16), tone(1.0), np.zeros(8000, np.int16)])
    mu = bytes(mulaw_enc(v) for v in pcm)
    c = TestClient(appmod.app)
    with c.websocket_connect("/stt/c1") as ws:
        ws.send_text("garbage"); ws.send_text(json.dumps({"event": "connected"}))
        ws.send_text(media(b"\xff\x00")); ws.send_text('{"event":"media","media":{"payload":"@@"}}')
        for i in range(0, len(mu), 160):
            ws.send_text(media(mu[i:i+160]))
        for i in range(0, len(mu), 160):   # outbound track (Maria) must be dropped
            ws.send_text(media(mu[i:i+160], "outbound"))
        ws.send_text(json.dumps({"event": "stop"}))
    assert [e[0] for e in emitted] == ["transcript.caller"]
    assert emitted[0][2] == {"utterance_id": "c1-u1", "text": "hello gift cards", "is_final": True}
    assert finals and finals[0][0] == "c1"

def test_on_final_exception_does_not_break(monkeypatch):
    async def fake_emit(*a): return True
    async def boom(c, u): raise RuntimeError("x")
    monkeypatch.setattr(stream.hub, "emit", fake_emit); monkeypatch.setattr(stream, "on_final", boom)
    stt.set_stt(FakeSTT())
    import asyncio
    asyncio.run(stream.handle_utterance("c", "c-u1", tone(0.5)))

def test_healthz():
    assert TestClient(appmod.app).get("/healthz").json()["ok"] is True

def test_ws_emits_partials_then_final(monkeypatch):
    emitted = []
    async def fake_emit(t, c, d): emitted.append(d); return True
    async def fake_final(c, u): pass
    monkeypatch.setattr(stream.hub, "emit", fake_emit); monkeypatch.setattr(stream, "on_final", fake_final)
    monkeypatch.setattr(stream, "PARTIAL_EVERY_S", 0.0)
    stt.set_stt(FakeSTT())
    mu = bytes(mulaw_enc(v) for v in np.concatenate([tone(1.5), np.zeros(8000, np.int16)]))
    with TestClient(appmod.app).websocket_connect("/stt/c2") as ws:
        for i in range(0, len(mu), 160):
            ws.send_text(media(mu[i:i+160]))
        ws.send_text(json.dumps({"event": "stop"}))
    assert emitted[-1]["is_final"] is True
    parts = [e for e in emitted if not e["is_final"]]
    assert all(p["utterance_id"] == emitted[-1]["utterance_id"] for p in parts)
    assert emitted.index(emitted[-1]) == len(emitted) - 1   # no partial after the final
