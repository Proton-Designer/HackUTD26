import asyncio

from detection.eval import run_eval as R


def test_live_guard_pauses_until_idle(monkeypatch):
    seq = iter([2, 1, 0])
    class Resp:
        def __init__(self, n): self.n = n
        def json(self): return {"active_stt_sockets": self.n}
    class Client:
        def __init__(self, *a, **k): pass
        async def __aenter__(self): return self
        async def __aexit__(self, *a): return False
        async def get(self, url): return Resp(next(seq))
    import httpx
    monkeypatch.setattr(httpx, "AsyncClient", Client)
    sleeps = []
    async def fake_sleep(s): sleeps.append(s)
    monkeypatch.setattr(R.asyncio, "sleep", fake_sleep)
    monkeypatch.setattr(R, "_idle", {"t": 0.0})
    monkeypatch.delenv("EVAL_NO_LIVE_GUARD", raising=False)
    asyncio.run(R.wait_live_idle())
    assert len(sleeps) == 2  # paused twice (2 then 1 sockets), proceeded at 0


def test_live_guard_unreachable_means_idle(monkeypatch):
    monkeypatch.setattr(R, "_idle", {"t": 0.0})
    monkeypatch.setattr(R, "LIVE_HEALTH", "http://127.0.0.1:9/healthz")
    monkeypatch.delenv("EVAL_NO_LIVE_GUARD", raising=False)
    asyncio.run(R.wait_live_idle())
