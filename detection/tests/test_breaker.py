"""TASK-026 cloud circuit breaker. Mocked engines and clock; no network."""
import asyncio
import httpx
import pytest
from detection import detect as D
from detection.engines import cloud, local

IRS = "This is the IRS. Pay with gift cards now or you will be arrested."


class Clock:
    t = 1000.0
    def __call__(self): return self.t


@pytest.fixture
def env(monkeypatch):
    clk = Clock()
    D.BREAKER.reset(); D.BREAKER.clock = clk
    D._CACHE.clear()
    monkeypatch.delenv("DEMO_MODE", raising=False)
    monkeypatch.delenv("P2_BREAKER", raising=False)
    monkeypatch.setenv("P2_CLOUD_RPM", "100000")
    D._bucket["tokens"] = None
    calls = {"cloud": 0, "local": 0, "cloud_mode": "429"}

    async def cloud_score(text, meta):
        calls["cloud"] += 1
        m = calls["cloud_mode"]
        if m == "ok":
            return {"s": 0.7, "asks": []}
        if m == "429":
            raise httpx.HTTPStatusError("429", request=httpx.Request("POST", "http://x"), response=httpx.Response(429))
        if m == "500":
            raise httpx.HTTPStatusError("500", request=httpx.Request("POST", "http://x"), response=httpx.Response(503))
        if m == "400":
            raise httpx.HTTPStatusError("400", request=httpx.Request("POST", "http://x"), response=httpx.Response(400))
        if m == "hang":
            await asyncio.sleep(30)

    async def local_score(text, meta):
        calls["local"] += 1
        return {"s": 0.6, "asks": []}

    async def reach(): return True
    monkeypatch.setattr(cloud, "score", cloud_score)
    monkeypatch.setattr(local, "score", local_score)
    monkeypatch.setattr(D, "_local_reachable", reach)
    yield clk, calls
    D.BREAKER.reset(); D.BREAKER.clock = __import__("time").monotonic


def run(text=IRS, call="c1", engine="cloud"):
    D._CACHE.clear()   # distinct windows are the norm live; force a miss
    return asyncio.run(D.detect(call, text, {}, engine))


def test_opens_after_3_failures_then_skips_cloud(env):
    clk, calls = env
    for i in range(3):
        out = run()
        assert out["engine"] == "local"            # failover still serves
    assert D.BREAKER.info()["state"] == "open"
    n = calls["cloud"]
    out = run()
    assert calls["cloud"] == n and out["engine"] == "local"   # cloud not touched while open


def test_failures_outside_30s_do_not_open(env):
    clk, calls = env
    run(); clk.t += 31; run(); clk.t += 31; run()
    assert D.BREAKER.info()["state"] == "closed"


def test_non_health_errors_do_not_count(env):
    clk, calls = env
    calls["cloud_mode"] = "400"
    for _ in range(5):
        run()
    assert D.BREAKER.info()["state"] == "closed"


def test_5xx_counts(env):
    clk, calls = env
    calls["cloud_mode"] = "500"
    for _ in range(3):
        run()
    assert D.BREAKER.info()["state"] == "open"


def test_half_open_probe_success_closes(env):
    clk, calls = env
    for _ in range(3):
        run()
    clk.t += 61
    calls["cloud_mode"] = "ok"
    out = run()
    assert out["engine"] == "cloud" and D.BREAKER.info()["state"] == "closed"


def test_half_open_failure_reopens_with_backoff_cap(env):
    clk, calls = env
    for _ in range(3):
        run()
    waits = []
    for _ in range(5):
        clk.t += D.BREAKER.backoff + 1
        run()                                         # probe fails (429)
        assert D.BREAKER.info()["state"] == "open"
        waits.append(D.BREAKER.backoff)
    assert waits == [120, 240, 300, 300, 300]


def test_only_one_probe_in_half_open(env):
    clk, calls = env
    for _ in range(3):
        run()
    clk.t += 61
    assert D.BREAKER.allow() is True       # the probe
    assert D.BREAKER.allow() is False      # everyone else waits
    assert D.BREAKER.info()["state"] == "half_open"


def test_open_and_local_down_goes_rules_only_fast(env, monkeypatch):
    clk, calls = env
    for _ in range(3):
        run()
    async def down(): return False
    monkeypatch.setattr(D, "_local_reachable", down)
    n = calls["cloud"]
    out = run()
    assert calls["cloud"] == n
    assert out["asks"] == ["gift_card"] and out["s"] >= 0.8      # rules still alert
    assert D.ENGINE_FAILED["c1"] is True


def test_cache_still_served_while_open(env):
    clk, calls = env
    calls["cloud_mode"] = "ok"
    asyncio.run(D.detect("c1", IRS, {}, "cloud"))      # cached
    calls["cloud_mode"] = "429"
    D.BREAKER.state, D.BREAKER.until = "open", clk.t + 50
    n = calls["cloud"]
    out = asyncio.run(D.detect("c1", IRS, {}, "cloud"))
    assert out["engine"] == "cloud" and calls["cloud"] == n and calls["local"] == 0


def test_timeout_counts(env, monkeypatch):
    clk, calls = env
    calls["cloud_mode"] = "hang"
    monkeypatch.setattr(D, "FAILOVER_CLOUD_S", 0.2)
    for _ in range(3):
        run()
    assert D.BREAKER.info()["state"] == "open"


def test_disabled_never_opens(env, monkeypatch):
    clk, calls = env
    monkeypatch.setenv("P2_BREAKER", "0")
    for _ in range(6):
        run()
    assert D.BREAKER.info()["state"] == "closed" and calls["cloud"] == 6


def test_info_shape(env):
    clk, calls = env
    for _ in range(3):
        run()
    i = D.breaker_info()
    assert i["state"] == "open" and 0 < i["retry_in_s"] <= 60 and i["until"]
