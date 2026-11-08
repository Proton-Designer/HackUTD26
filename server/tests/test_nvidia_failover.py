import asyncio, json, logging
import httpx
import pytest
from server import nvidia_keys as NK, fallback_detect as fd


def _handler(plan, seen):
    def h(req):
        tok = req.headers["authorization"].split()[-1]
        seen.append(tok)
        code = plan.get(tok, 200)
        return httpx.Response(code, json={"choices": [{"message": {"content": "{}"}}]} if code == 200 else {})
    return h


_REAL_ASYNC = httpx.AsyncClient


def _patch_async(monkeypatch, plan, seen):
    real = _REAL_ASYNC
    monkeypatch.setattr(httpx, "AsyncClient", lambda **kw: real(transport=httpx.MockTransport(_handler(plan, seen)), **kw))


def test_fallback_fails_over_k1_k2_k3_and_remembers_healthy_key_60s(monkeypatch, caplog):
    for n, v in (("NVIDIA_API_KEY", "AAA-1"), ("NVIDIA_API_KEY_2", "BBB-2"), ("NVIDIA_API_KEY_3", "CCC-3")): monkeypatch.setenv(n, v)
    monkeypatch.setenv("FALLBACK_429_BACKOFF_S", "0")
    seen = []; _patch_async(monkeypatch, {"AAA-1": 429, "BBB-2": 401}, seen)
    with caplog.at_level(logging.WARNING, logger="hub.nvkeys"):
        assert asyncio.run(fd.call_nemotron("x")) == "{}"
    assert seen == ["AAA-1", "BBB-2", "CCC-3"]                                   # same request, next key each time
    log_txt = " ".join(r.getMessage() for r in caplog.records)
    assert "429" in log_txt and "401" in log_txt and "key #1" in log_txt and "AAA" not in log_txt and "BBB" not in log_txt and "CCC" not in log_txt
    seen.clear(); _patch_async(monkeypatch, {"AAA-1": 429, "BBB-2": 401}, seen)
    assert asyncio.run(fd.call_nemotron("y")) == "{}" and seen == ["CCC-3"]       # healthy key remembered: no wasted retries
    NK._good["fallback"] = ("NVIDIA_API_KEY_3", NK._good["fallback"][1] - 61)                 # 60 s later: back to the primary order
    seen.clear(); _patch_async(monkeypatch, {}, seen)
    assert asyncio.run(fd.call_nemotron("z")) == "{}" and seen == ["AAA-1"]


def test_fallback_all_keys_throttled_then_one_backoff_retry_and_raise(monkeypatch):
    for n, v in (("NVIDIA_API_KEY", "AAA-1"), ("NVIDIA_API_KEY_2", "BBB-2")): monkeypatch.setenv(n, v)
    monkeypatch.setenv("FALLBACK_429_BACKOFF_S", "0")
    seen = []; _patch_async(monkeypatch, {"AAA-1": 429, "BBB-2": 429}, seen)
    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(fd.call_nemotron("x"))
    assert seen == ["AAA-1", "BBB-2", "AAA-1"]


def test_fallback_non_failover_error_does_not_burn_other_keys(monkeypatch):
    for n, v in (("NVIDIA_API_KEY", "AAA-1"), ("NVIDIA_API_KEY_2", "BBB-2")): monkeypatch.setenv(n, v)
    seen = []; _patch_async(monkeypatch, {"AAA-1": 500}, seen)
    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(fd.call_nemotron("x"))
    assert seen == ["AAA-1"]                                                      # 500 is not a key problem


def test_intel_agent_fails_over_with_mock_transport(monkeypatch):
    from intel import agent
    for n, v in (("NVIDIA_API_KEY", "AAA-1"), ("NVIDIA_API_KEY_2", "BBB-2"), ("NVIDIA_API_KEY_3", "CCC-3")): monkeypatch.setenv(n, v)
    seen = []
    c = httpx.Client(transport=httpx.MockTransport(_handler({"AAA-1": 403, "BBB-2": 429}, seen)))
    assert agent.call_nemotron([{"role": "user", "content": "hi"}], client=c) == "{}" and seen == ["AAA-1", "BBB-2", "CCC-3"]
    seen.clear()
    assert agent.call_nemotron([{"role": "user", "content": "hi"}], client=c) == "{}" and seen == ["CCC-3"]    # remembered
    monkeypatch.setenv("INTEL_NVIDIA_API_KEY", "III-0"); NK.reset(); seen.clear()                              # intel's own key goes first
    assert agent.call_nemotron([{"role": "user", "content": "hi"}], client=httpx.Client(transport=httpx.MockTransport(_handler({}, seen)))) == "{}" and seen == ["III-0"]
    monkeypatch.delenv("NVIDIA_API_KEY"); monkeypatch.delenv("NVIDIA_API_KEY_2"); monkeypatch.delenv("NVIDIA_API_KEY_3"); monkeypatch.delenv("INTEL_NVIDIA_API_KEY")
    monkeypatch.setattr(agent, "_api_key", lambda: None)
    with pytest.raises(RuntimeError):
        agent.call_nemotron([], client=c)


def test_status_flags_for_backup_keys_are_booleans_only(monkeypatch):
    from fastapi.testclient import TestClient
    from server.main import app
    c = TestClient(app, client=("127.0.0.1", 5000))
    f = c.get("/demo/status").json()["flags"]
    assert f["NVIDIA_API_KEY_2_set"] is False and f["NVIDIA_API_KEY_3_set"] is False
    monkeypatch.setenv("NVIDIA_API_KEY_2", "SEKRET-2")
    body = c.get("/demo/status").text
    assert json.loads(body)["flags"]["NVIDIA_API_KEY_2_set"] is True and "SEKRET" not in body
