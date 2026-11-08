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
