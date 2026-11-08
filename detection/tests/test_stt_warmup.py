import asyncio
from detection import app as A, stt

def test_warmup_failure_is_swallowed(monkeypatch, caplog):
    def boom(): raise RuntimeError("no riva")
    monkeypatch.setattr(A, "_warm_stt", boom)
    asyncio.run(A.warmup_stt())                      # must not raise
    assert any("stt warmup failed" in r.getMessage() for r in caplog.records)

def test_warmup_disabled_skips(monkeypatch):
    called = []
    monkeypatch.setattr(A, "_warm_stt", lambda: called.append(1))
    monkeypatch.setenv("P2_STT_WARMUP", "0")
    asyncio.run(A.warmup_stt()); assert not called
    monkeypatch.setenv("P2_STT_WARMUP", "1")
    asyncio.run(A.warmup_stt()); assert called == [1]

def test_lifespan_starts_even_when_warmup_fails(monkeypatch):
    monkeypatch.setattr(A, "_warm_stt", lambda: (_ for _ in ()).throw(RuntimeError("x")))
    monkeypatch.setenv("P2_NO_HUB_WS", "1")
    async def go():
        async with A._lifespan(A.app):
            await asyncio.sleep(0.05)
    asyncio.run(go())
