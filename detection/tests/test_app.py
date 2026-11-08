import os
os.environ["P2_NO_HUB_WS"] = "1"
from fastapi.testclient import TestClient
from detection import app as appmod, alert, stream

def test_app_wires_alert_and_routes():
    paths = {r.path for r in appmod.app.routes}
    assert "/healthz" in paths and "/stt/{call_id}" in paths
    assert alert.machine is not None and stream.on_final == alert.machine.on_final
    with TestClient(appmod.app) as c:     # startup/shutdown handlers run without hub WS
        assert c.get("/healthz").status_code == 200
