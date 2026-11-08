import os
os.environ["P2_NO_HUB_WS"] = "1"
from fastapi.testclient import TestClient
from detection import app as appmod, alert, stream

def test_app_wires_alert_and_routes():
    spec = appmod.app.openapi()["paths"]
    assert "/healthz" in spec
    assert any(getattr(r, "path", "") == "/stt/{call_id}" for r in stream.router.routes)
    assert alert.machine is not None and stream.on_final == alert.machine.on_final
    with TestClient(appmod.app) as c:     # startup/shutdown handlers run without hub WS
        assert c.get("/healthz").status_code == 200

def test_lifespan_starts_hub_subscriber(monkeypatch):
    import asyncio
    seen = []
    async def fake_sub(handler, stop=None):
        seen.append(handler); await asyncio.sleep(3600)
    monkeypatch.setenv("P2_NO_HUB_WS", "0")
    monkeypatch.setattr(alert.hub, "subscribe", fake_sub)
    with TestClient(appmod.app):
        pass
    assert seen == [alert.machine.on_event]

def test_healthz_reports_wiring_without_secrets(monkeypatch):
    from fastapi.testclient import TestClient
    from detection import app as appmod, health
    monkeypatch.setenv("NVIDIA_API_KEY", "nvapi-SECRETVALUE")
    monkeypatch.setenv("LOCAL_LLM_URL", "http://127.0.0.1:9")      # nothing there
    appmod._local["t"] = 0
    health.err("hub.emit", RuntimeError("boom with http://x?key=SECRET"))
    j = TestClient(appmod.app).get("/healthz").json()
    assert j["ok"] and j["stt"]["backend"] in ("riva", "whisper") and j["engines"] == {"cloud_key_present": True, "local_reachable": False}
    assert j["hub_subscriber_connected"] in (True, False) and isinstance(j["active_stt_sockets"], int)
    assert j["last_error"]["src"] == "hub.emit" and j["last_error"]["err"] == "RuntimeError"
    assert "SECRET" not in str(j)
