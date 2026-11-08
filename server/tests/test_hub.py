import time
import pytest
from fastapi.testclient import TestClient
from server import db, bus, routing
from server.main import app

@pytest.fixture(autouse=True)
def fresh():
    db.configure(":memory:"); db.reset_all(); bus.reset(); yield

def test_routing_decisions():
    assert routing.decide("+15555550999")["decision"] == "LIVE_GUARD"
    assert routing.decide("+15555550188", "A")["decision"] == "NORMAL"          # trusted + A
    assert routing.decide("+15555550188", "C")["decision"] == "LIVE_GUARD"      # trusted, spoofed
    db.add_confirmed("555-555-0999")
    r = routing.decide("+15555550999"); assert r["decision"] == "BLOCKED_BACKFIRE"
    db.add_campaign("+15555550123")
    assert routing.decide("+15555550123", "A")["decision"] == "BLOCKED_BACKFIRE"
    assert routing.decide("911")["decision"] == "NORMAL"

def test_undo_unblocks():
    t = db.add_confirmed("+15555550999"); assert db.undo(t)
    assert routing.decide("+15555550999")["decision"] == "LIVE_GUARD"

def test_lookup_fast_and_http():
    c = TestClient(app); db.add_confirmed("+15555550999")
    t0 = time.perf_counter(); r = c.get("/routing/lookup", params={"from": "+15555550999"})
    assert r.json()["decision"] == "BLOCKED_BACKFIRE"; assert time.perf_counter() - t0 < 0.05

def test_fail_open(monkeypatch):
    monkeypatch.setattr(db, "has", lambda *a: 1 / 0)
    assert routing.decide("+15555550999")["decision"] == "NORMAL"

def test_ws_events_and_post():
    c = TestClient(app)
    with c.websocket_connect("/events") as ws:
        assert c.post("/events", json={"type": "call.routed", "call_id": "x", "data": {"decision": "NORMAL", "reason": "r"}}).json()["ok"]
        ev = ws.receive_json(); assert ev["type"] == "call.routed" and ev["call_id"] == "x" and "ts" in ev
        c.post("/user/action", json={"call_id": "x", "action": "hang_up"})
        assert ws.receive_json()["data"]["action"] == "hang_up"

def test_bad_action_and_ingest_stub():
    c = TestClient(app)
    assert not c.post("/user/action", json={"call_id": "x", "action": "nope"}).json()["ok"]
    assert c.post("/intel/ingest", json={"call_id": "x", "artifacts": []}).json()["stub"]
