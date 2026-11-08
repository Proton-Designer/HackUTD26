import pytest
from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect
from detection import app as appmod, auth, detect as D

body = {"call_id": "c1", "window_text": "hello", "metadata": {}, "engine": "cloud"}

@pytest.fixture(autouse=True)
def stub(monkeypatch):
    async def fake(*a, **k): return {"s": 0.1}
    import detection.router as R
    monkeypatch.setattr(R, "detect", fake)
    monkeypatch.delenv("PIPELINE_TOKEN", raising=False)

def c(): return TestClient(appmod.app)

def ws_ok(cl, path, **kw):
    try:
        with cl.websocket_connect(path, **kw) as ws:
            ws.send_text('{"event":"stop"}')
        return True
    except WebSocketDisconnect as e:
        assert e.code == 1008
        return False

def test_no_token_configured_allows_all():
    assert c().post("/detect", json=body).status_code == 200
    assert ws_ok(c(), "/stt/c1")

def test_detect_with_token(monkeypatch):
    monkeypatch.setenv("PIPELINE_TOKEN", "sekret")
    cl = c()
    assert cl.post("/detect", json=body).status_code == 401
    assert cl.post("/detect", json=body, headers={"x-pipeline-token": "nope"}).status_code == 401
    assert cl.post("/detect", json=body, headers={"x-pipeline-token": "sekret"}).status_code == 200
    assert cl.post("/detect?token=sekret", json=body).status_code == 200
    assert cl.post("/detect", json={**body, "call_id": "../x"}, headers={"x-pipeline-token": "sekret"}).status_code == 422

def test_stt_with_token(monkeypatch):
    monkeypatch.setenv("PIPELINE_TOKEN", "sekret")
    cl = c()
    assert not ws_ok(cl, "/stt/c1")
    assert not ws_ok(cl, "/stt/c1?token=wrong")
    assert ws_ok(cl, "/stt/c1", headers={"x-pipeline-token": "sekret"})
    assert ws_ok(cl, "/stt/c1?token=sekret")

def test_bad_call_id_rejected():
    for bad in ["a.b", "x" * 65, "a b"]:
        assert not ws_ok(c(), f"/stt/{bad}")
    assert c().post("/detect", json={**body, "call_id": "bad id"}).status_code == 422
    assert auth.valid_call_id("c_demo-1") and not auth.valid_call_id("")

def test_healthz_open(monkeypatch):
    monkeypatch.setenv("PIPELINE_TOKEN", "sekret")
    assert c().get("/healthz").status_code == 200
