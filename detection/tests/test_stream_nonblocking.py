"""TASK-047: a slow detect() must not hold up STT of the next utterance (on_final runs as a background task)."""
import asyncio, time
from detection import alert, stream, stt
from detection.tests.test_alert import R


class FakeSTT:
    def __init__(self, texts): self.texts = list(texts)
    async def transcribe(self, pcm): return self.texts.pop(0)


def test_slow_detect_does_not_block_finals(monkeypatch):
    emitted, det_calls, flight, peak = [], [], [0], [0]
    async def emit(typ, cid, d): emitted.append((time.monotonic(), typ, d))
    async def det(cid, text, meta, engine):
        det_calls.append(text); flight[0] += 1; peak[0] = max(peak[0], flight[0])
        await asyncio.sleep(1.0)            # stands in for a 2-5 s local llama call
        flight[0] -= 1; return R(0.4)
    m = alert.AlertMachine(emit=emit, detect=det, clock=time.time, engine="local")
    monkeypatch.setattr(stream.hub, "emit", emit); monkeypatch.setattr(stream, "on_final", m.on_final)
    monkeypatch.setattr(stt, "_stt", FakeSTT(["first line", "second line", "third line"]))
    async def go():
        t0 = time.monotonic()
        for i in range(3):
            await stream.handle_utterance("c1", f"u{i}", None, None)
            await asyncio.sleep(0.5)
        finals = [t for t, typ, d in emitted if typ == "transcript.caller"]
        assert len(finals) == 3 and max(finals) - t0 < 1.4, [round(x - t0, 2) for x in finals]   # not serialised behind 1 s detects
        await stream.drain(10)
        for _ in range(60):
            if not m.calls["c1"].busy: break
            await asyncio.sleep(0.1)
    asyncio.run(go())
    assert peak[0] == 1                                          # one detect in flight per call
    assert "third line" in det_calls[-1] and "first line" in det_calls[-1]   # newest window scored last
    risks = [d["s"] for t, typ, d in emitted if typ == "risk.update"]
    assert risks and risks[-1] == 0.4


def test_riva_has_its_own_pool():
    p = stt._riva_pool()
    assert p is stt._riva_pool() and p._thread_name_prefix == "riva"
