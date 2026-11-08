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
    assert routing.decide("911", "A")["decision"] == "NORMAL"
    assert routing.decide("911")["decision"] == "LIVE_GUARD"  # unverified 911 caller ID is not a free pass
    assert routing.decide("12345")["decision"] == "LIVE_GUARD"  # unverified short code not exempt
    db.add_confirmed("12345"); assert routing.decide("12345")["decision"] == "BLOCKED_BACKFIRE"

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
        assert c.post("/events", json={"type": "risk.update", "call_id": "x", "data": {"s": 0.1}}).json()["ok"]
        ev = ws.receive_json(); assert ev["type"] == "risk.update" and ev["call_id"] == "x" and "ts" in ev
        bus.publish("call.incoming", "x", {"from": "+15555550001"}); ws.receive_json()
        c.post("/user/action", json={"call_id": "x", "action": "hang_up"})
        assert ws.receive_json()["data"]["action"] == "hang_up"

def test_bad_action_and_ingest_stub():
    c = TestClient(app)
    assert not c.post("/user/action", json={"call_id": "x", "action": "nope"}).json()["ok"]
    assert c.post("/user/action", json={"call_id": "zzz", "action": "hang_up"}).status_code == 404
    assert c.post("/events", json={"type": "user.action", "call_id": "x", "data": {}}).status_code == 403
    assert c.post("/intel/ingest", json={"call_id": "x", "artifacts": []}).json()["stub"]

def test_decoy_end_blocks_caller_and_callback_rejected():
    c = TestClient(app)
    with c.websocket_connect("/events") as ws:
        for t, d in [("call.incoming", {"from": "+15555550142", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.7}),
                     ("call.routed", {"decision": "LIVE_GUARD", "reason": "x"}),
                     ("handoff.started", {"restore_deadline": 1.0}),
                     ("call.ended", {"ended_by": "caller", "duration_s": 5.0})]:
            bus.publish(t, "k1", d)
        types = [ws.receive_json()["type"] for _ in range(5)]
        assert types[-1] == "blocklist.updated"
    assert c.get("/routing/lookup", params={"from": "+15555550142"}).json()["decision"] == "BLOCKED_BACKFIRE"
    log = c.get("/protection-log").json(); tok = log["blocked"][0]["undo_token"]
    assert c.post("/protection-log/undo", json={"undo_token": tok}).json()["ok"]
    assert c.get("/routing/lookup", params={"from": "+15555550142"}).json()["decision"] == "LIVE_GUARD"

def test_reset_and_replay():
    c = TestClient(app); db.add_confirmed("+15555550999")
    assert c.post("/demo/reset").json()["seconds"] < 30
    assert c.get("/protection-log").json()["blocked"] == []
    import asyncio
    from server import replay
    asyncio.run(replay.run("c_demo_bank", speed=1000))
    assert any(e["type"] == "call.ended" for e in bus.history)

def test_token_required(monkeypatch):
    import server.main as m
    monkeypatch.setattr(m, "HUB_TOKEN", "s3")
    c = TestClient(app)
    assert c.get("/routing/lookup", params={"from": "+1"}).status_code == 401
    assert c.get("/routing/lookup", params={"from": "+1"}, headers={"x-hub-token": "s3"}).status_code == 200
    assert c.post("/events", json={"type": "risk.update", "call_id": "x"}).status_code == 401

def test_trusted_number_not_auto_blocked():
    for t, d in [("call.incoming", {"from": "+15555550188", "attestation": "C"}), ("handoff.started", {}), ("call.ended", {})]:
        bus.publish(t, "k9", d)
    assert routing.decide("+15555550188", "A")["decision"] == "NORMAL"

def test_emergency_never_blocked():
    with pytest.raises(ValueError):
        db.add_confirmed("911")
    db.q("INSERT INTO confirmed_scammers VALUES('+911','t','x',0)")  # even if forced in
    assert routing.decide("911", "A")["decision"] == "NORMAL"
    assert routing.decide("911")["decision"] == "LIVE_GUARD"  # unverified 911 caller ID is not a free pass

def test_app_mounted_same_origin():
    c = TestClient(app)
    assert c.get("/app/").status_code == 200
    assert c.get("/healthz").json()["ok"]


def test_latency_and_status(tmp_path, monkeypatch):
    from server import ops
    monkeypatch.setattr(ops, "LATENCY_LOG", tmp_path / "lat.jsonl")
    ops.reset()
    bus.publish("call.incoming", "L1", {"from": "+15555550123"})
    bus.publish("call.routed", "L1", {"decision": "LIVE_GUARD", "reason": "x"})
    bus.publish("alert.fired", "L1", {})
    bus.publish("user.action", "L1", {"action": "scammer_get_scammed"})
    bus.publish("handoff.started", "L1", {})
    c = TestClient(app)
    m = c.get("/demo/latency").json()["metrics"]
    assert {"route_ms", "alert_ms", "handoff_ms"} <= set(m)
    assert len((tmp_path / "lat.jsonl").read_text().splitlines()) == 3
    s = c.get("/demo/status").json()
    assert s["hub"] == "up" and "P2 /detect" in s["pipelines"] and "HUB_TOKEN_set" in s["flags"]
    assert "HUB_TOKEN" not in str(s.get("flags", {}).values())
    assert "<table>" in c.get("/demo/status?format=html").text


def test_static_mounts_load():
    c = TestClient(app)
    for path in ("/app/", "/command-center/", "/command-center/app.js"):
        assert c.get(path).status_code == 200, path
    assert c.get("/healthz").json() == {"ok": True}  # API routes still win
