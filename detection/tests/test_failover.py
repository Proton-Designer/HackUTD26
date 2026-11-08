import asyncio
import pytest
from detection import detect as D

TXT = "please read me the six digit code we texted you"
LOCAL_RAW = {"s": 0.7, "asks": [], "scam_type": "unknown", "stage": "ask", "impersonates": "unknown",
             "addresses_ai_system": False, "why_chips": ["x"]}


@pytest.fixture(autouse=True)
def clean(monkeypatch):
    D._CACHE.clear(); D._local.update(ok=False, t=-1e9); D.FAILOVERS["n"] = 0
    monkeypatch.delenv("DEMO_MODE", raising=False); monkeypatch.delenv("P2_FAILOVER", raising=False)


def run(coro): return asyncio.run(coro)


def patch(monkeypatch, cloud, local, reachable=True):
    async def es(text, md, engine):
        return await (cloud if engine == "cloud" else local)()
    async def reach(): return reachable
    monkeypatch.setattr(D, "_engine_score", es); monkeypatch.setattr(D, "_local_reachable", reach)


async def boom(): raise RuntimeError("cloud 429")
async def ok_local(): return LOCAL_RAW
async def down(): raise ConnectionError("x")


def test_cloud_error_uses_local(monkeypatch):
    patch(monkeypatch, boom, ok_local)
    out = run(D.detect("c", "hello there", {}, "cloud"))
    assert out["engine"] == "local" and D.FAILOVERS["n"] == 1


def test_local_also_down_rules_only(monkeypatch):
    patch(monkeypatch, boom, down)
    out = run(D.detect("c", TXT, {}, "cloud"))
    assert out["engine"] == "cloud" and out["s"] >= 0.82 and "otp" in out["asks"]


def test_local_unreachable_skips_failover(monkeypatch):
    calls = []
    async def loc(): calls.append(1); return LOCAL_RAW
    patch(monkeypatch, boom, loc, reachable=False)
    out = run(D.detect("c", TXT, {}, "cloud"))
    assert not calls and out["engine"] == "cloud"


def test_disabled_by_env(monkeypatch):
    monkeypatch.setenv("P2_FAILOVER", "0")
    patch(monkeypatch, boom, ok_local)
    assert run(D.detect("c", "hello there", {}, "cloud"))["engine"] == "cloud"


def test_budget_exhausted_goes_local(monkeypatch):
    monkeypatch.setattr(D, "_bucket", {"tokens": 0.0, "t": 1e18})
    monkeypatch.setattr(D, "MAX_BUCKET_WAIT_S", 0.05)
    async def reach(): return True
    monkeypatch.setattr(D, "_local_reachable", reach)
    async def fake_local(text, md): return LOCAL_RAW
    import sys, types
    mod = types.ModuleType("detection.engines.local"); mod.score = fake_local
    monkeypatch.setitem(sys.modules, "detection.engines.local", mod)
    import detection.engines as pkg; monkeypatch.setattr(pkg, "local", mod, raising=False)
    out = run(D.detect("c", "hello there", {}, "cloud"))
    assert out["engine"] == "local"


def test_local_not_gated_by_cloud_bucket(monkeypatch):
    monkeypatch.setattr(D, "_bucket", {"tokens": 0.0, "t": 1e18})
    assert run(D._acquire("local")) is True


def test_slow_cloud_leaves_budget_for_local(monkeypatch):
    async def slow(): await asyncio.sleep(10)
    monkeypatch.setattr(D, "FAILOVER_CLOUD_S", 0.2)
    patch(monkeypatch, slow, ok_local)
    assert run(D.detect("c", "hello there", {}, "cloud"))["engine"] == "local"


def test_concurrent_calls_share_one_probe(monkeypatch):
    calls = {"n": 0}
    import httpx
    class FakeResp: status_code = 200
    class FakeClient:
        def __init__(self, *a, **k): pass
        async def __aenter__(self): return self
        async def __aexit__(self, *a): return False
        async def get(self, url):
            calls["n"] += 1; await asyncio.sleep(0.1); return FakeResp()
    monkeypatch.setattr(httpx, "AsyncClient", FakeClient)
    D._local.update(ok=False, t=-1e9)
    async def many(): return await asyncio.gather(*[D._local_reachable() for _ in range(6)])
    assert all(run(many())) and calls["n"] == 1


def test_probe_capped(monkeypatch):
    import httpx, time
    class FakeClient:
        def __init__(self, *a, **k): pass
        async def __aenter__(self): return self
        async def __aexit__(self, *a): return False
        async def get(self, url): await asyncio.sleep(5)
    monkeypatch.setattr(httpx, "AsyncClient", FakeClient)
    D._local.update(ok=False, t=-1e9)
    t = time.monotonic()
    assert run(D._local_reachable()) is False and time.monotonic() - t < 1.0


def test_timeout_cloud_still_alerts_via_local(monkeypatch):
    async def hang(): await asyncio.sleep(30)
    monkeypatch.setattr(D, "FAILOVER_CLOUD_S", 0.3)
    patch(monkeypatch, hang, ok_local)
    import time; t = time.monotonic()
    assert run(D.detect("c", "hello there", {}, "cloud"))["engine"] == "local"
    assert time.monotonic() - t < D.OVERALL_TIMEOUT_S


# ---- reverse failover (TASK-041): engine=local primary, cloud second ----
@pytest.fixture
def rev(monkeypatch):
    monkeypatch.setenv("NVIDIA_API_KEY", "test-not-a-key")
    D.FAILOVERS["reverse"] = 0
    D.BREAKER.reset()
    CLOUD_RAW = dict(LOCAL_RAW, s=0.9)
    async def ok_cloud(): return CLOUD_RAW
    return ok_cloud


def test_local_error_uses_cloud(monkeypatch, rev):
    patch(monkeypatch, rev, down)
    out = run(D.detect("c", "hello there", {}, "local"))
    assert out["engine"] == "cloud" and out["s"] >= 0.9 and D.FAILOVERS["reverse"] == 1


def test_local_timeout_uses_cloud(monkeypatch, rev):
    async def slow(): await asyncio.sleep(5); return LOCAL_RAW
    monkeypatch.setattr(D, "LOCAL_FIRST_S", 0.2)
    patch(monkeypatch, rev, slow)
    out = run(D.detect("c", "hello there", {}, "local"))
    assert out["engine"] == "cloud" and D.FAILOVERS["reverse"] == 1


def test_local_probe_down_skips_local(monkeypatch, rev):
    calls = []
    async def loc(): calls.append(1); return LOCAL_RAW
    patch(monkeypatch, rev, loc, reachable=False)
    out = run(D.detect("c", "hello there", {}, "local"))
    assert not calls and out["engine"] == "cloud"


def test_local_ok_no_cloud_call(monkeypatch, rev):
    calls = []
    async def cl(): calls.append(1); return LOCAL_RAW
    patch(monkeypatch, cl, ok_local)
    out = run(D.detect("c", "hello there", {}, "local"))
    assert not calls and out["engine"] == "local"


def test_both_down_rules_floor(monkeypatch, rev):
    patch(monkeypatch, boom, down)
    out = run(D.detect("c", TXT, {}, "local"))
    assert out["s"] >= 0.82 and "otp" in out["asks"] and D.detect.__name__


def test_reverse_disabled_or_no_key_or_breaker_open(monkeypatch, rev):
    calls = []
    async def cl(): calls.append(1); return LOCAL_RAW
    patch(monkeypatch, cl, down)
    monkeypatch.setenv("P2_FAILOVER", "0")
    run(D.detect("c", "hello there", {}, "local")); assert not calls
    monkeypatch.delenv("P2_FAILOVER"); monkeypatch.delenv("NVIDIA_API_KEY")
    run(D.detect("c", "hello there", {}, "local")); assert not calls
    monkeypatch.setenv("NVIDIA_API_KEY", "x")
    monkeypatch.setattr(D.BREAKER, "state", "open"); monkeypatch.setattr(D.BREAKER, "allow", lambda: False)
    monkeypatch.setattr(D.BREAKER, "enabled", staticmethod(lambda: True))
    run(D.detect("c", "hello there", {}, "local")); assert not calls
