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


def test_stop_on_fallback_cancels_the_run(monkeypatch, tmp_path):
    import pytest
    monkeypatch.setenv("EVAL_STOP_ON_FALLBACK", "1")
    monkeypatch.setenv("EVAL_NO_LIVE_GUARD", "1")
    monkeypatch.setattr(R, "CACHE_DIR", tmp_path)
    calls = []
    async def scorer(engine, cid, text):
        calls.append(cid)
        return {"s": 0.0, "asks": [], "fallback": True}
    row = lambda i: {"id": f"r{i}", "split": "dev", "label": "scam", "scam_type": "t", "expected_asks": [], "expected_alert": True,
                     "caller_lines": ["a", "b"]}
    monkeypatch.setattr(R, "MAX_RPM", {"cloud": 6000})   # as in a real cloud run: one row at a time
    with pytest.raises(R.EvalStop):
        asyncio.run(R.run_engine("cloud", [row(i) for i in range(5)], scorer=scorer))
    assert len(calls) == 1          # stopped at the first failure, no further windows were attempted
