import base64, json, os
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


class _Prim(stt.STT):
    name = "prim"
    def __init__(self): self.calls, self.down = 0, True
    async def transcribe(self, pcm):
        self.calls += 1
        if self.down: raise RuntimeError("riva down")
        return "from riva"


class _Wh(stt.STT):
    name = "whisper"
    async def transcribe(self, pcm): return "from whisper"


def test_fallback_uses_whisper_then_bypasses_riva_then_recovers():
    import asyncio, numpy as np
    pcm = np.zeros(800, dtype=np.int16)
    p, now = _Prim(), [1000.0]
    f = stt.FallbackSTT(p, preload=False, whisper_factory=_Wh)
    f._time = lambda: now[0]
    run = lambda: asyncio.run(f.transcribe(pcm))
    assert run() == "from whisper" and run() == "from whisper" and p.calls == 2 and f.bypassing   # 2 fails -> bypass
    assert run() == "from whisper" and p.calls == 2                                               # positive control: Riva NOT called while bypassed
    now[0] += 31; p.down = False
    assert run() == "from riva" and f.fails == 0 and not f.bypassing                              # re-probed and recovered


def test_fallback_preloads_whisper_in_background():
    import time
    f = stt.FallbackSTT(_Prim(), preload=True, whisper_factory=_Wh)
    for _ in range(50):
        if f._fb: break
        time.sleep(0.05)
    assert f._fb is not None


def _wav(name):
    import wave, numpy as np
    w = wave.open(os.path.join(os.path.dirname(__file__), "..", "testdata", "acc", name)); return np.frombuffer(w.readframes(w.getnframes()), dtype="<i2")


def _utts(x, noise_rms=30.0, db=0.0, seed=1):
    import numpy as np
    rng = np.random.default_rng(seed)
    y = x.astype(np.float64) * 10 ** (db / 20) + rng.normal(0, noise_rms, len(x))
    y = np.clip(y, -32768, 32767).astype(np.int16)
    seg, out = stream.Segmenter(), []
    for i in range(0, len(y), 160 * 5): out += seg.feed(y[i:i + 800])
    return out + seg.flush(), seg


def test_quiet_line_speech_still_endpointed():
    x = _wav("askfirst.wav")
    for db, nz in ((0, 30.0), (-20, 30.0), (-25, 8.0)):     # -25 dB = speech median rms ~120 over a quiet comfort-noise floor
        u, _ = _utts(x, db=db, noise_rms=nz)
        assert len(u) >= 1, db
    # positive control: the OLD detector (floor 300, noise*3.5) misses -25 dB speech, so this test can fail
    try:
        stream.VAD_FLOOR, stream.VAD_REL = 300.0, 3.5
        u_old, _ = _utts(x, db=-25, noise_rms=8.0)
    finally:
        stream.VAD_FLOOR, stream.VAD_REL = 60.0, 2.5
    assert len(u_old) == 0


def test_pure_noise_makes_no_utterances():
    import numpy as np
    for rms in (10.0, 30.0, 60.0):
        u, seg = _utts(np.zeros(8000 * 20, dtype=np.int16), noise_rms=rms)
        assert u == [], rms


def test_long_noisy_intro_does_not_raise_threshold_past_cap():
    import numpy as np
    seg = stream.Segmenter()
    seg.feed((np.random.default_rng(2).normal(0, 2000, 8000 * 20)).astype(np.int16))   # 20 s of very loud noise
    assert seg.thr() <= stream.NOISE_CAP * stream.VAD_REL + 1


def test_alaw_l16_and_16k_decode():
    import numpy as np
    assert stt.alaw_decode(bytes([0xD5]))[0] == 8 and stt.alaw_decode(bytes([0x55]))[0] == -8
    assert stt.alaw_decode(bytes([0xAA]))[0] > 20000                                 # max positive
    x = np.array([1000, -1000, 300], dtype=">i2").tobytes()
    assert list(stt.decode_media(x, "L16", 8000)) == [1000, -1000, 300]
    assert len(stt.decode_media(np.zeros(320, dtype=">i2").tobytes(), "L16", 16000)) == 160
    assert stt.decode_media(bytes([0xFF]), "PCMU", 8000)[0] == 0
