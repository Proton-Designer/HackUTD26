import time
import pytest
from fastapi.testclient import TestClient
from server import db, bus, routing
from server.main import app
from server import device

def paired(c=None):
    c = c or TestClient(app)
    c.headers["x-device-token"] = c.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    return c

@pytest.fixture(autouse=True)
def fresh():
    import intel.store as istore
    from intel import api as iapi
    st = istore.Store(":memory:"); istore._default = st; iapi._cfg["store"] = st; iapi._cfg["use_llm"] = False; iapi._calls.clear()
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
    c = paired()
    with c.websocket_connect("/events") as ws:
        bus.publish("call.incoming", "x", {"from": "+15555550001"}); assert ws.receive_json()["type"] == "call.incoming"
        assert c.post("/events", json={"type": "risk.update", "call_id": "x", "data": {"s": 0.1}}).json()["ok"]
        ev = ws.receive_json(); assert ev["type"] == "risk.update" and ev["call_id"] == "x" and "ts" in ev
        c.post("/user/action", json={"call_id": "x", "action": "hang_up"})
        assert ws.receive_json()["data"]["action"] == "hang_up"

def test_bad_action_and_ingest_stub():
    c = paired()
    assert not c.post("/user/action", json={"call_id": "x", "action": "nope"}).json()["ok"]
    assert c.post("/user/action", json={"call_id": "zzz", "action": "hang_up"}).status_code == 404
    assert c.post("/events", json={"type": "user.action", "call_id": "x", "data": {}}).status_code == 403
    assert c.post("/intel/ingest", json={"call_id": "x", "artifacts": []}).status_code in (200, 401)   # real intel mounted (device-gated), no stub

def test_decoy_end_blocks_caller_and_callback_rejected(monkeypatch):
    import server.main as M
    monkeypatch.setattr(M, "intel_api", None)   # fallback path: P1 stub blocks on decoy call.ended when intel is not mounted
    c = paired()
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
    c = paired(); db.add_confirmed("+15555550999")
    assert c.post("/demo/reset").json()["seconds"] < 30
    assert c.get("/protection-log").json()["blocked"] == []
    import asyncio
    from server import replay
    asyncio.run(replay.run("c_demo_bank", speed=1000))
    assert any(e["type"] == "call.ended" for e in bus.history)

def test_reset_seeds_intel_and_fails_open(monkeypatch):
    c = paired()
    r = c.post("/demo/reset").json()
    assert r["ok"] and r["seeded"] and r["check"]["campaigns"] == 1 and r["check"]["actions"] == 0 and r["check"]["blocklist"] == 0
    assert r["seed"]["sightings"] == 1
    assert c.get("/routing/lookup", params={"from": "+12145550199"}).json()["decision"] == "LIVE_GUARD"
    assert c.post("/demo/reset?seed=0").json()["seeded"] is False
    import intel.seed_demo as sd
    monkeypatch.setattr(sd, "seed", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom")))
    r = c.post("/demo/reset").json()
    assert r["ok"] and r["seeded"] is False and r["seed_error"] == "RuntimeError"

def test_demo_reset_and_replay_need_device_or_local(monkeypatch):
    db.add_confirmed("+15555550999")
    remote = TestClient(app)                                   # host "testclient" = remote
    assert remote.post("/demo/reset").status_code == 401
    assert remote.post("/demo/replay", json={}).status_code == 401
    assert db.list_confirmed()                                 # nothing was wiped
    local = TestClient(app, client=("127.0.0.1", 5000))
    assert local.post("/demo/reset", headers={"cf-connecting-ip": "1.2.3.4"}).status_code == 401   # via tunnel = remote
    assert db.list_confirmed()
    monkeypatch.setenv("HUB_TOKEN", "s3")
    assert remote.post("/demo/reset", headers={"x-hub-token": "s3"}).status_code == 200
    assert not db.list_confirmed()
    monkeypatch.delenv("HUB_TOKEN")
    assert local.post("/demo/reset").status_code == 200        # operator at the console

def test_status_reports_key_presence_never_value(monkeypatch):
    import intel.agent as ia
    c = TestClient(app, client=("127.0.0.1", 5000))
    monkeypatch.setattr(ia, "_api_key", lambda: None)
    f = c.get("/demo/status").json()["flags"]
    assert f["NVIDIA_API_KEY_set"] is False and f["intel_engine"] == "template"
    monkeypatch.setattr(ia, "_api_key", lambda: "nvapi-SECRETVALUE")
    monkeypatch.setitem(__import__("intel.api", fromlist=["_cfg"])._cfg, "use_llm", True)   # fixture runs with LLM off
    r = c.get("/demo/status")
    f = r.json()["flags"]
    assert f["NVIDIA_API_KEY_set"] is True and f["intel_engine"].startswith("nemotron:")
    assert "SECRETVALUE" not in r.text

def test_status_p2_probe_derives_from_stt_url(monkeypatch):
    from server import ops
    monkeypatch.delenv("P2_BASE", raising=False)
    assert ops._remote_base("P2_BASE") is None
    monkeypatch.setenv("P2_STT_URL", "wss://p2.example.com:9000/ignored")
    assert ops._remote_base("P2_BASE") == "https://p2.example.com:9000/healthz"
    monkeypatch.setenv("P2_STT_URL", "ws://127.0.0.1:8100")
    assert ops._remote_base("P2_BASE") == "http://127.0.0.1:8100/healthz"
    monkeypatch.setenv("P2_BASE", "http://explicit:1")
    assert ops._remote_base("P2_BASE") == "http://explicit:1"

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
    assert s["pipelines"]["P4 /intel"]["mounted"] is True    # in-process intel router counts as mounted
    assert s["pipelines"]["voip"]["mounted"] is True


def test_static_mounts_load():
    c = TestClient(app)
    for path in ("/app/", "/command-center/", "/command-center/app.js"):
        assert c.get(path).status_code == 200, path
    assert c.get("/healthz").json() == {"ok": True}  # API routes still win


def test_sim_call_helpers():
    import importlib.util, pathlib
    sp = importlib.util.spec_from_file_location("sim_call", pathlib.Path(__file__).resolve().parents[2] / "scripts" / "sim_call.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    assert m.lin2ulaw(0) == 0xFF and len(m.pcmu_tone(secs=1)) == 8000
    w = m.webhook("call.initiated", {"from": "+1"})["data"]
    assert w["event_type"] == "call.initiated" and w["payload"]["from"] == "+1"


def test_voip_mounted_in_single_process():
    from server import ops
    s = ops.status(app)["pipelines"]
    assert s["voip"]["mounted"] is True
    assert s["P3 /decoy"].get("stand_in") is True or s["P3 /decoy"]["mounted"] is False   # voip's /decoy alias is the stand-in persona, not P3; /decoy-echo is not P3
    paths = [getattr(r, "path", "") for r in app.routes]
    assert paths[-2:] == ["/command-center", "/app"] or set(paths[-2:]) == {"/command-center", "/app"}   # static mounts stay last


def test_device_pin_protects_endpoints():
    c = TestClient(app)   # client host "testclient" = remote
    for m, path, body in [("get", "/protection-log", None), ("post", "/protection-log/undo", {"undo_token": "x"}), ("post", "/user/action", {"call_id": "x", "action": "hang_up"})]:
        r = c.request(m, path, json=body); assert r.status_code == 401, path
    assert c.post("/pair", json={"pin": "wrong"}).status_code == 401
    tok = c.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    assert c.get("/protection-log", headers={"x-device-token": tok}).status_code == 200
    assert c.get("/protection-log", headers={"x-device-token": "forged"}).status_code == 401
    assert c.get("/healthz").status_code == 200

def test_localhost_bypass_not_through_tunnel():
    local = TestClient(app, client=("127.0.0.1", 5000))
    assert local.get("/protection-log").status_code == 200                               # direct local dev
    assert local.get("/protection-log", headers={"cf-connecting-ip": "1.2.3.4"}).status_code == 401   # via cloudflared: remote
    assert local.get("/protection-log", headers={"x-forwarded-for": "1.2.3.4"}).status_code == 401

def test_pair_rate_limit_and_hub_token(monkeypatch):
    device._fails.clear()
    c = TestClient(app)
    codes = [c.post("/pair", json={"pin": "000000"}).status_code for _ in range(7)]
    assert codes[:5] == [401] * 5 and codes[5:] == [429, 429]
    assert c.post("/pair", json={"pin": device.PIN}).status_code == 429   # locked out even with the right pin
    device._fails.clear()
    monkeypatch.setenv("HUB_TOKEN", "svc")
    assert c.get("/protection-log", headers={"x-hub-token": "svc"}).status_code == 200


def _wait(cond, secs=5):
    t = time.time()
    while time.time() - t < secs:
        if cond(): return True
        time.sleep(0.05)
    return False

def test_intel_mounted_blocks_after_artifacts_and_undo_works(monkeypatch):
    import server.main as M
    assert M.intel_api is not None
    # hermetic: never let a real NVIDIA key (env or repo .env) trigger a live Nemotron call; template mode only
    monkeypatch.delenv("NVIDIA_API_KEY", raising=False)
    import intel.agent as ia
    monkeypatch.setattr(ia, "_api_key", lambda: None)
    M.intel_api._cfg["use_llm"] = False
    c = paired(); n = "+15555550177"
    assert routing.decide(n)["decision"] == "LIVE_GUARD"
    bus.publish("call.incoming", "i1", {"from": n, "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    bus.publish("handoff.started", "i1", {"restore_deadline": 1.0})
    bus.publish("artifacts.extracted", "i1", {"artifacts": [{"kind": "callback_phone", "value": "+15555550166"}, {"kind": "impersonated_org", "value": "IRS"}]})
    assert _wait(lambda: routing.decide(n)["decision"] == "BLOCKED_BACKFIRE", 20), "intel did not block the caller"
    assert any(e["type"].startswith("intel.") or e["type"] == "blocklist.updated" for e in bus.history if e["call_id"] in ("i1", None))
    log = c.get("/protection-log").json()
    row = next(r for r in log["blocked"] if r["number"] == n)
    assert c.post("/protection-log/undo", json={"undo_token": row["undo_token"]}).json()["ok"]
    assert routing.decide(n)["decision"] == "LIVE_GUARD"
    assert routing.decide("911", "A")["decision"] == "NORMAL"

def test_intel_routes_protected_and_stub_removed():
    c = TestClient(app)
    assert c.post("/intel/ingest", json={"call_id": "x", "artifacts": []}).status_code == 401
    assert c.get("/intel/state").status_code == 401
    assert c.post("/intel/actions/nope/approve").status_code == 404   # exact approve route stays open (404 = reached the handler)
    assert c.get("/intel/actions/nope/approve").status_code in (401, 405)   # other methods are gated
    assert c.get("/intel/blocked", params={"number": "+15555550177"}).status_code == 401
    assert c.post("/intel/ingest", json={"call_id": "x", "artifacts": []}, headers=paired().headers).json().get("stub") is None

def test_routing_fails_open_without_intel(monkeypatch):
    import sys
    monkeypatch.setitem(sys.modules, "intel.store", None)   # import error inside decide()
    assert routing.decide("+15555550999")["decision"] == "LIVE_GUARD"
    db.add_confirmed("+15555550999"); assert routing.decide("+15555550999")["decision"] == "BLOCKED_BACKFIRE"


def test_forged_artifacts_and_trusted_numbers_cannot_poison():
    import server.main as M
    n = "+15555550155"
    bus.publish("call.incoming", "f1", {"from": n, "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    bus.publish("artifacts.extracted", "f1", {"artifacts": [{"kind": "callback_phone", "value": "+15555550156"}]})   # no hub-seen handoff
    time.sleep(0.5)
    assert routing.decide(n)["decision"] == "LIVE_GUARD"
    import intel.store as istore
    istore._default.add_block("+15555550188", "her", "poison")   # trusted bank number
    assert routing.decide("+15555550188", "A")["decision"] == "NORMAL"
    assert routing.decide("+15555550188", "none")["decision"] == "LIVE_GUARD"


def test_pipeline_token_gates_post_events(monkeypatch):
    c = TestClient(app)
    bus.publish("call.incoming", "p1", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    ev = {"type": "risk.update", "call_id": "p1", "data": {"s": 0.9}}
    assert c.post("/events", json=ev).json()["ok"]                       # unset: open (dev)
    monkeypatch.setenv("PIPELINE_TOKEN", "pt")
    assert c.post("/events", json=ev).status_code == 401
    assert c.post("/events", json=ev, headers={"x-pipeline-token": "bad"}).status_code == 401
    monkeypatch.setenv("HUB_TOKEN", "hub")                               # HUB_TOKEN is separate and not accepted here
    assert c.post("/events", json=ev, headers={"x-hub-token": "hub"}).status_code == 401
    assert c.post("/events", json=ev, headers={"x-pipeline-token": "pt"}).json()["ok"]
    assert c.post("/events", json={"type": "user.action", "call_id": "p1", "data": {}}, headers={"x-pipeline-token": "pt"}).status_code == 403


def test_legit_call_ended_is_not_blocked_by_intel_or_stub(monkeypatch):
    import server.main as M
    n = "+15555550166"
    bus.publish("call.incoming", "g1", {"from": n, "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    bus.publish("handoff.started", "g1", {"restore_deadline": 1.0})
    monkeypatch.setattr(M.intel_api, "GRACE_S", 0.2)
    bus.publish("call.ended", "g1", {"ended_by": "decoy", "duration_s": 40.0, "legit": True})
    time.sleep(1.0)
    assert routing.decide(n)["decision"] == "LIVE_GUARD"          # not blocked
    monkeypatch.setattr(M, "intel_api", None)                       # fallback stub path honors it too
    bus.publish("call.incoming", "g2", {"from": n, "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    bus.publish("handoff.started", "g2", {"restore_deadline": 1.0})
    bus.publish("call.ended", "g2", {"ended_by": "decoy", "duration_s": 40.0, "legit": True})
    assert routing.decide(n)["decision"] == "LIVE_GUARD"


def test_telnyx_ok_flag_tracks_last_rest_result(monkeypatch):
    from server import ops
    monkeypatch.setattr(ops, "telnyx_state", {"ok": None, "kind": None, "ts": None})
    c = TestClient(app, client=("127.0.0.1", 5000))
    fl = lambda: c.get("/demo/status").json()["flags"]
    assert fl()["telnyx_ok"] is None                                     # never called
    ops.telnyx_result(True); assert fl()["telnyx_ok"] is True
    ops.telnyx_result(False, '/calls -> 401 {"errors":[{"code":"10009","title":"user marked as blocked"}]}')
    assert fl()["telnyx_ok"] is False and fl()["telnyx_last_error"] == "auth"
    ops.telnyx_result(False, "ConnectTimeout"); f = fl()                 # blip: still false (last auth failure stands), kind updates
    assert f["telnyx_ok"] is False and f["telnyx_last_error"] == "unreachable"
    ops.telnyx_result(True); assert fl()["telnyx_ok"] is True and fl()["telnyx_last_error"] is None
    ops.telnyx_result(False, "boom" * 100000)                            # never raises on junk
    assert c.post("/demo/reset").status_code == 200 and fl()["telnyx_ok"] is True   # reset does not touch account health

def test_hub_routing_intel_relay_work_with_telnyx_unreachable(monkeypatch):
    """Telnyx 401/10009 or unreachable must not affect the hub: routing, events, intel blocklist, status, relay to P2, and voip's _safe all fail open."""
    import asyncio, httpx, websockets, json as _j
    monkeypatch.setenv("TELNYX_API_KEY", "dummy")
    class Dead:
        def __init__(self, *a, **k): pass
        async def __aenter__(self): raise httpx.ConnectError("telnyx unreachable (test)")
        async def __aexit__(self, *a): return False
    monkeypatch.setattr(httpx, "AsyncClient", Dead)
    c = paired()
    assert c.get("/routing/lookup", params={"from": "+15555550123"}).json()["decision"] == "LIVE_GUARD"
    assert c.get("/healthz").json()["ok"] and c.get("/demo/status").status_code == 200
    bus.publish("call.incoming", "tz", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    assert c.post("/events", json={"type": "risk.update", "call_id": "tz", "data": {"s": .5, "band": "med", "engine": "cloud"}}).status_code in (200, 202, 204)
    assert c.post("/demo/reset").json()["ok"]
    # voip's REST wrapper swallows the failure (returns None) instead of raising into the call path
    from voip import router as R, telnyx
    assert asyncio.run(R._safe(telnyx.hangup("v3:abc"), "hangup")) is None
    # P2 relay unaffected
    from server import relay
    async def go():
        got = []
        async def h2(ws):
            async for m in ws: got.append(_j.loads(m))
        srv = await websockets.serve(h2, "127.0.0.1", 0); port = srv.sockets[0].getsockname()[1]
        monkeypatch.setenv("P2_STT_URL", f"ws://127.0.0.1:{port}"); monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        async def back(f): pass
        await relay.open("tz1", back)
        await relay.caller_frame("tz1", {"event": "connected"})
        await relay.caller_frame("tz1", {"event": "start", "stream_id": "S", "start": {}})
        await relay.caller_frame("tz1", {"event": "media", "media": {"track": "inbound", "chunk": "1", "payload": "AAAA"}})
        await asyncio.sleep(0.2); await relay.close("tz1"); srv.close()
        return [m["event"] for m in got]
    assert asyncio.run(go()) == ["connected", "start", "media"]


def test_demo_caller_wav_serves_range_and_404(monkeypatch, tmp_path):
    import wave
    c = TestClient(app)                                        # remote client: no auth needed
    monkeypatch.setenv("DEMO_CALLER_WAV", str(tmp_path / "missing.wav"))
    assert c.get("/demo/caller.wav").status_code == 404
    f = tmp_path / "c.wav"
    with wave.open(str(f), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(b"\x01\x02" * 4000)
    monkeypatch.setenv("DEMO_CALLER_WAV", str(f))
    r = c.get("/demo/caller.wav")
    assert r.status_code == 200 and r.headers["content-type"] == "audio/wav" and r.content == f.read_bytes()
    r = c.get("/demo/caller.wav", headers={"Range": "bytes=0-99"})
    assert r.status_code == 206 and len(r.content) == 100 and r.headers["content-range"].startswith("bytes 0-99/")
    assert c.get("/demo/caller.wav?path=/etc/passwd").content == f.read_bytes()   # query can't change the path
    monkeypatch.delenv("DEMO_CALLER_WAV")
    monkeypatch.setenv("LOGDIR", str(tmp_path)); (tmp_path / "sim_scam.wav").write_bytes(f.read_bytes())
    assert c.get("/demo/caller.wav").status_code == 200       # default: $LOGDIR/sim_scam.wav


def test_bare_root_redirects_to_app():
    c = TestClient(app)
    r = c.get("/", follow_redirects=False)
    assert r.status_code == 307 and r.headers["location"] == "/app/"
    assert c.get("/?sim=1", follow_redirects=False).headers["location"] == "/app/?sim=1"
    assert c.get("/").status_code == 200 and c.get("/app/").status_code == 200


def test_trusted_crud_needs_device_and_validates():
    remote = TestClient(app)
    assert remote.get("/trusted").status_code == 401
    assert remote.post("/trusted", json={"number": "+15555550123"}).status_code == 401
    assert remote.delete("/trusted/+15555550188").status_code == 401
    assert db.has("trusted", "+15555550188")
    c = paired()
    assert any(t["number"] == "+15555550188" for t in c.get("/trusted").json()["trusted"])
    for bad in ("", "abc", "+1", "+0123456789", "1" * 30):
        assert c.post("/trusted", json={"number": bad}).status_code == 422
    r = c.post("/trusted", json={"number": "(555) 555-0123", "label": "Dr. Lee\x00"})
    assert r.status_code == 200 and r.json()["number"] == "+15555550123" and r.json()["label"] == "Dr. Lee"
    assert db.has("trusted", "+15555550123")
    assert c.delete("/trusted/%2B15555550123").json() == {"ok": True, "removed": True}
    assert c.delete("/trusted/%2B15555550123").json() == {"ok": True, "removed": False}   # idempotent
    assert c.delete("/trusted/garbage").status_code == 200
    assert not db.has("trusted", "+15555550123")


def test_loopback_bypass_refuses_cross_origin_browser_writes():
    local = TestClient(app, client=("127.0.0.1", 5000))
    h = {"host": "127.0.0.1:8000"}
    assert local.post("/trusted", json={"number": "+15555550123"}, headers={**h, "origin": "https://evil.example"}).status_code == 401
    assert local.delete("/trusted/%2B15555550188", headers={**h, "origin": "http://localhost:3000"}).status_code == 401
    assert db.has("trusted", "+15555550188") and not db.has("trusted", "+15555550123")
    assert local.post("/trusted", json={"number": "+15555550123"}, headers={**h, "origin": "http://127.0.0.1:8000"}).status_code == 200
    assert local.post("/trusted", json={"number": "+15555550124"}, headers=h).status_code == 200   # curl at the console


def test_status_maria_leg_flag(monkeypatch):
    c = TestClient(app, client=("127.0.0.1", 5000))
    monkeypatch.delenv("MARIA_LEG", raising=False)
    assert c.get("/demo/status").json()["flags"]["MARIA_LEG"] == "sip"
    monkeypatch.setenv("MARIA_LEG", "pstn")
    assert c.get("/demo/status").json()["flags"]["MARIA_LEG"] == "pstn"


def test_pairing_survives_demo_reset_and_replay():
    c = paired()
    tok = c.headers["x-device-token"]
    assert c.post("/demo/reset").status_code == 200
    assert c.post("/demo/reset?seed=0").status_code == 200
    assert c.post("/demo/replay", json={"speed": 1000}).status_code == 200
    assert device._valid(tok)
    assert c.get("/trusted").status_code == 200                      # still authorised
    assert TestClient(app, headers={"x-device-token": tok}).get("/trusted").status_code == 200
    db.reset_all(); db.reset_all(seed=False)                         # the db layer must not touch device_tokens either
    assert device._valid(tok)


def test_reset_never_deletes_device_tokens_even_if_intel_db_is_the_hub_db(tmp_path):
    import intel.store as istore
    from intel import api as iapi
    p = str(tmp_path / "shared.db")
    db.configure(p); db.reset_all()
    st = istore.Store(p); istore._default = st; iapi._cfg["store"] = st
    c = paired(); tok = c.headers["x-device-token"]
    assert c.post("/demo/reset").status_code == 200
    assert device._valid(tok)
    assert c.get("/trusted").status_code == 200
    db.configure(":memory:")


def test_intel_chain_and_map_open_get_only_nothing_else():
    c = TestClient(app)                                              # remote, unpaired (the tunnel)
    for p in ("/intel/chain", "/intel/map"):
        assert c.get(p).status_code in (200, 404, 422), p            # reached the handler, not the guard
        assert c.get(p).status_code != 401
        assert c.post(p).status_code in (401, 405)                 # other methods are not served
        assert c.get(p + "/", follow_redirects=False).status_code in (401, 404, 307)         # no prefix/trailing-slash widening
    for p in ("/intel/chain/x", "/intel/mapx", "/intel/state", "/intel/blocked", "/intel/campaigns", "/intel/chains"):
        assert c.get(p).status_code in (401, 404), p
    assert c.get("/intel/state").status_code == 401


def test_status_active_calls_flag():
    import asyncio
    from server import relay
    c = TestClient(app, client=("127.0.0.1", 5000))
    f = c.get("/demo/status").json()
    assert f["flags"]["active_calls"] == 0 and f["flags"]["last_call_activity_ts"] is None and f["active_call_ids"] == []
    async def go():
        async def back(x): pass
        await relay.open("ACTIVE-CALL-1", back)
        await relay.caller_frame("ACTIVE-CALL-1", {"event": "media", "media": {"track": "inbound", "payload": "AA=="}})
        s = await asyncio.to_thread(lambda: c.get("/demo/status").json())
        assert s["flags"]["active_calls"] == 1 and s["active_call_ids"] == ["ACTIVE-C"] and s["flags"]["last_call_activity_ts"] > 0
        await relay.close("ACTIVE-CALL-1")
        s = await asyncio.to_thread(lambda: c.get("/demo/status").json())
        assert s["flags"]["active_calls"] == 0
    asyncio.run(go())


def test_status_hides_call_ids_and_activity_from_remote():
    import asyncio
    from server import relay
    async def go():
        async def back(x): pass
        await relay.open("REMOTE-HIDE-1", back)
        await relay.caller_frame("REMOTE-HIDE-1", {"event": "media", "media": {"track": "inbound", "payload": "AA=="}})
        remote = await asyncio.to_thread(lambda: TestClient(app).get("/demo/status").json())
        local = await asyncio.to_thread(lambda: TestClient(app, client=("127.0.0.1", 5000)).get("/demo/status").json())
        await relay.close("REMOTE-HIDE-1")
        return remote, local
    remote, local = asyncio.run(go())
    assert remote["flags"]["active_calls"] == 1 and "active_call_ids" not in remote and "last_call_activity_ts" not in remote["flags"]
    assert local["active_call_ids"] == ["REMOTE-H"] and local["flags"]["last_call_activity_ts"] > 0


def test_device_pin_from_env_is_not_printed_or_written(tmp_path):
    import subprocess, sys, os
    env = dict(os.environ, DEVICE_PIN="987654", LOGDIR=str(tmp_path), HUB_DB=str(tmp_path / "h.db"), INTEL_DB=str(tmp_path / "i.db"))
    env.pop("HUB_NO_PIN_FILE", None)
    r = subprocess.run([sys.executable, "-c", "import server.main"], env=env, capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and "987654" not in r.stdout + r.stderr and "not printed" in r.stdout
    assert not (tmp_path / "device_pin.txt").exists()
    env.pop("DEVICE_PIN")
    r = subprocess.run([sys.executable, "-c", "import server.main"], env=env, capture_output=True, text=True, timeout=60)
    pin = (tmp_path / "device_pin.txt").read_text().strip()
    assert pin and pin in r.stdout                                     # random PIN: still shown once for the operator


def test_status_customer_name_flag(monkeypatch):
    c = TestClient(app, client=("127.0.0.1", 5000))
    monkeypatch.delenv("CUSTOMER_NAME", raising=False)
    assert c.get("/demo/status").json()["flags"]["CUSTOMER_NAME"] == "Maria"
    monkeypatch.setenv("CUSTOMER_NAME", "Dana")
    assert c.get("/demo/status").json()["flags"]["CUSTOMER_NAME"] == "Dana"
    monkeypatch.setenv("CUSTOMER_NAME", "")
    assert c.get("/demo/status").json()["flags"]["CUSTOMER_NAME"] == ""
    monkeypatch.setenv("CUSTOMER_NAME", '<b>Ev"e</b>' + "x" * 80)
    n = c.get("/demo/status").json()["flags"]["CUSTOMER_NAME"]
    assert "<" not in n and '"' not in n and len(n) <= 40


def _dev_risk(**kw):
    d = {"s": 0.91, "band": "high", "asks": ["gift_card", "secrecy"], "scam_type": "gift_card_scam", "stage": "payment",
         "impersonates": "IRS", "addresses_ai_system": False, "why_chips": ["Asks for gift cards"], "engine": "device"}
    d.update(kw); return d


def test_paired_device_may_post_only_device_risk_and_transcript(monkeypatch):
    monkeypatch.setenv("PIPELINE_TOKEN", "pt-secret")
    bus.publish("call.incoming", "DV1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    anon, dev = TestClient(app), paired()
    ev = lambda t, d, c=dev, cid="DV1": c.post("/events", json={"type": t, "call_id": cid, "data": d})
    assert ev("risk.update", _dev_risk()).status_code == 403                          # paired but holds no /listen or /talk slot for the call
    ws = dev.websocket_connect("/listen/DV1", subprotocols=["bf-device", dev.headers["x-device-token"]]); ws.__enter__()
    try:
        _device_body(anon, dev, ev)
    finally:
        ws.__exit__(None, None, None)


def _device_body(anon, dev, ev):
    assert ev("risk.update", _dev_risk(), anon).status_code == 401                   # no token at all
    n0 = len(bus.history)
    r = ev("risk.update", _dev_risk(evil="x", extra={"a": 1}))
    assert r.status_code == 200
    got = [e for e in bus.history[n0:] if e["type"] == "risk.update"][-1]["data"]
    assert got["engine"] == "device" and got["s"] == 0.91 and "evil" not in got and "extra" not in got   # rebuilt from validated fields
    assert ev("transcript.caller", {"text": "hello there", "is_final": True, "engine": "device", "utterance_id": "u1"}).status_code == 200
    assert bus.history[-1]["type"] == "transcript.caller" and bus.history[-1]["data"]["engine"] == "device"
    # nothing else, and never another engine
    for t, d in (("alert.fired", {"level": "first", "why_chips": [], "engine": "device"}), ("artifacts.extracted", {"engine": "device"}),
                 ("blocklist.updated", {"engine": "device"}), ("intel.agent", {"engine": "device"}), ("risk.update", _dev_risk(engine="cloud")),
                 ("risk.update", {k: v for k, v in _dev_risk().items() if k != "engine"})):
        assert ev(t, d).status_code == 403, (t, d.get("engine"))
    assert ev("call.ended", {"engine": "device"}).status_code == 403                  # reserved types stay hub-only
    # validation
    for bad in (_dev_risk(s=1.5), _dev_risk(s=True), _dev_risk(band="meh"), _dev_risk(stage="x"), _dev_risk(asks=["nope"]),
                _dev_risk(why_chips=["a"] * 5), _dev_risk(impersonates=5)):
        assert ev("risk.update", bad).status_code == 422, bad
    assert ev("transcript.caller", {"text": 5, "is_final": True, "engine": "device"}).status_code == 422
    assert ev("risk.update", _dev_risk(), cid="never-seen").status_code == 404        # only for calls the hub saw
    # the pipeline token still works for P2 exactly as before
    assert anon.post("/events", json={"type": "risk.update", "call_id": "DV1", "data": {"engine": "cloud", "s": 0.1}},
                     headers={"x-pipeline-token": "pt-secret"}).status_code == 200


def test_device_event_rate_limited(monkeypatch):
    from server import main as m
    monkeypatch.setenv("PIPELINE_TOKEN", "pt-secret"); m._dev_hits.clear()
    bus.publish("call.incoming", "DV2", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    dev, other = paired(), paired()
    post = lambda c: c.post("/events", json={"type": "risk.update", "call_id": "DV2", "data": _dev_risk()}).status_code
    with dev.websocket_connect("/listen/DV2", subprotocols=["bf-device", dev.headers["x-device-token"]]), \
         other.websocket_connect("/listen/DV2", subprotocols=["bf-device", other.headers["x-device-token"]]):
        codes = [post(dev) for _ in range(45)]
        assert codes[:40] == [200] * 40 and set(codes[40:]) == {429}
        assert post(other) == 200                                                    # a different device has its own budget


def test_device_events_need_active_call_and_the_slot_holder(monkeypatch):
    from server import main as m
    monkeypatch.setenv("PIPELINE_TOKEN", "pt-secret"); m._dev_hits.clear()
    bus.publish("call.incoming", "DV3", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    a, b = paired(), paired()
    post = lambda c: c.post("/events", json={"type": "risk.update", "call_id": "DV3", "data": _dev_risk()}).status_code
    with a.websocket_connect("/listen/DV3", subprotocols=["bf-device", a.headers["x-device-token"]]):
        assert post(a) == 200
        assert post(b) == 403                                                        # paired, but not the device attached to this call
        bus.publish("call.ended", "DV3", {"ended_by": "caller", "duration_s": 3})
        assert post(a) == 409                                                        # ended calls accept no device events


def test_duplicate_alert_fired_ignored_and_logged(monkeypatch, caplog):
    import logging
    from server import main as m
    monkeypatch.delenv("PIPELINE_TOKEN", raising=False); m._ALERTS.clear()
    c = TestClient(app)
    bus.publish("call.incoming", "DUP1", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    bus.publish("call.incoming", "DUP2", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    bus.publish("call.incoming", "DUP1b", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    ws_events = lambda cid: [e for e in bus.history if e["type"] == "alert.fired" and e["call_id"] == cid]
    post = lambda cid, lvl: c.post("/events", json={"type": "alert.fired", "call_id": cid, "data": {"level": lvl, "why_chips": ["Asks for gift cards"]}})
    with caplog.at_level(logging.WARNING, logger="hub"):
        assert post("DUP1", "first").json() == {"ok": True}
        r = post("DUP1", "first"); assert r.status_code == 200 and r.json().get("duplicate") is True     # retry: acknowledged, not re-published
        assert len(ws_events("DUP1")) == 1
        assert post("DUP2", "first").json() == {"ok": True} and len(ws_events("DUP2")) == 1               # other call unaffected
        assert post("DUP1", "realert").json() == {"ok": True}
        assert post("DUP1", "realert").json().get("duplicate") is True                                   # realert retry inside 3 s
        assert len(ws_events("DUP1")) == 2
        m._ALERTS[("DUP1", "realert")] -= 10                                                              # a later genuine rise
        assert post("DUP1", "realert").json() == {"ok": True} and len(ws_events("DUP1")) == 3
    assert any("dup alert ignored call=DUP1" in r.getMessage() for r in caplog.records)


def test_device_cannot_poison_alert_dedupe(monkeypatch):
    from server import main as m
    monkeypatch.setenv("PIPELINE_TOKEN", "pt-secret"); m._ALERTS.clear()
    bus.publish("call.incoming", "DV4", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    dev, anon = paired(), TestClient(app)
    with dev.websocket_connect("/listen/DV4", subprotocols=["bf-device", dev.headers["x-device-token"]]):
        r = dev.post("/events", json={"type": "alert.fired", "call_id": "DV4", "data": {"level": "first", "why_chips": [], "engine": "device"}})
        assert r.status_code == 403
        assert ("DV4", "first") not in m._ALERTS                                       # a refused device post leaves no dedupe state
    real = anon.post("/events", json={"type": "alert.fired", "call_id": "DV4", "data": {"level": "first", "why_chips": ["x"]}},
                     headers={"x-pipeline-token": "pt-secret"})
    assert real.json() == {"ok": True} and any(e["type"] == "alert.fired" and e["call_id"] == "DV4" for e in bus.history)


def test_pwa_static_headers_and_types():
    c = TestClient(app)
    m = c.get("/app/manifest.webmanifest")
    assert m.status_code == 200 and m.headers["content-type"].startswith("application/manifest+json") and m.headers["cache-control"] == "no-cache"
    icons = [i for i in m.json()["icons"]]
    assert icons
    for i in icons:                                                                   # every manifest icon exists, served with its declared type
        r = c.get("/app/" + i["src"])
        assert r.status_code == 200 and r.headers["content-type"] == i["type"] == "image/png", i["src"]
        assert "max-age" in r.headers["cache-control"] and "no-cache" not in r.headers["cache-control"]
    for path in ("/app/", "/app/index.html", "/app/app.js", "/app/style.css", "/app/ui.js"):
        r = c.get(path)
        assert r.status_code == 200 and r.headers["cache-control"] == "no-cache", path
    assert c.get("/app/assets/apple-touch-icon.png").headers["content-type"] == "image/png"
    assert c.get("/app/nope.js").status_code == 404


def test_answer_and_decline_only_while_ringing():
    c = paired()
    act = lambda cid, a: c.post("/user/action", json={"call_id": cid, "action": a})
    assert act("RING0", "answer").status_code == 404                                   # unknown call
    bus.publish("call.incoming", "RING1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    bus.publish("call.routed", "RING1", {"decision": "LIVE_GUARD", "reason": "x"})
    assert act("RING1", "answer").json() == {"ok": True}
    assert bus.history[-1]["type"] == "user.action" and bus.history[-1]["data"] == {"action": "answer"}
    bus.publish("call.answered", "RING1", {"by": "maria"})
    assert act("RING1", "answer").status_code == 409 and act("RING1", "decline").status_code == 409   # no longer ringing
    assert act("RING1", "hang_up").json() == {"ok": True}                              # other actions unchanged
    bus.publish("call.incoming", "RING2", {"from": "+15555550124", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    assert act("RING2", "decline").json() == {"ok": True}
    bus.publish("call.ended", "RING2", {"ended_by": "maria", "duration_s": 1})
    assert act("RING2", "answer").status_code == 409
    bus.publish("call.incoming", "RING3", {"from": "+15555550125", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    bus.publish("call.routed", "RING3", {"decision": "BLOCKED_BACKFIRE", "reason": "x"})
    assert act("RING3", "answer").status_code == 409                                   # a blocked call never rings
    assert act("RING3", "bogus").json()["ok"] is False
    assert TestClient(app).post("/user/action", json={"call_id": "RING1", "action": "answer"}).status_code == 401


def test_f5_restore_clears_alert_dedupe_so_new_first_alert_fires(monkeypatch):
    from server import main as m
    monkeypatch.delenv("PIPELINE_TOKEN", raising=False); m._ALERTS.clear()
    c = TestClient(app)
    bus.publish("call.incoming", "F5", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    bus.publish("call.incoming", "F5b", {"from": "+15555550001", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.5})
    first = lambda: c.post("/events", json={"type": "alert.fired", "call_id": "F5", "data": {"level": "first", "why_chips": ["x"]}}).json()
    n = lambda: len([e for e in bus.history if e["type"] == "alert.fired" and e["call_id"] == "F5"])
    assert first() == {"ok": True} and first().get("duplicate") and n() == 1
    bus.publish("handoff.started", "F5", {}); assert first().get("duplicate") and n() == 1   # still deduped during the handoff
    bus.publish("handoff.restored", "F5", {})
    assert first() == {"ok": True} and n() == 2                                                # new first alert after restore
    other = c.post("/events", json={"type": "alert.fired", "call_id": "F5b", "data": {"level": "first", "why_chips": []}}).json()
    assert other == {"ok": True}


def test_f11_reset_refused_while_a_call_is_live_unless_force():
    import asyncio
    from server import relay
    local = TestClient(app, client=("127.0.0.1", 5000))
    db.add_confirmed("+15555550999")
    async def go():
        async def back(x): pass
        await relay.open("F11LIVE-1", back)
        r1 = await asyncio.to_thread(lambda: local.post("/demo/reset"))
        kept = bool(db.list_confirmed())
        r2 = await asyncio.to_thread(lambda: local.post("/demo/reset?force=1"))
        await relay.close("F11LIVE-1")
        return r1, kept, r2
    r1, kept, r2 = asyncio.run(go())
    assert r1.status_code == 409 and "F11LIVE-" in r1.json()["detail"] and kept            # nothing wiped
    assert r2.status_code == 200 and not db.list_confirmed()
    assert local.post("/demo/reset").status_code == 200                                      # no live call: normal reset


def test_status_active_calls_detail_paired_or_loopback_only():
    inc = lambda cid, frm: bus.publish("call.incoming", cid, {"from": frm, "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    inc("AD-ringing-1", "+15555550123"); bus.publish("call.routed", "AD-ringing-1", {"decision": "LIVE_GUARD", "reason": "x"})
    inc("AD-answered-2", "+15555550124"); bus.publish("call.answered", "AD-answered-2", {"by": "maria"}); bus.publish("handoff.started", "AD-answered-2", {})
    inc("AD-restored-3", "+15555550125"); bus.publish("call.answered", "AD-restored-3", {"by": "maria"})
    bus.publish("handoff.started", "AD-restored-3", {}); bus.publish("handoff.restored", "AD-restored-3", {})
    inc("AD-ended-4", "+15555550126"); bus.publish("call.ended", "AD-ended-4", {"ended_by": "caller", "duration_s": 2})
    inc("AD-blocked-5", "+15555550127"); bus.publish("call.routed", "AD-blocked-5", {"decision": "BLOCKED_BACKFIRE", "reason": "x"})
    remote = TestClient(app).get("/demo/status").json()
    assert "active_calls_detail" not in remote and "active_call_ids" not in remote                  # unpaired/remote: omitted
    for c in (paired(), TestClient(app, client=("127.0.0.1", 5000))):
        d = {x["call_id"]: x for x in c.get("/demo/status").json()["active_calls_detail"]}
        assert set(d) == {"AD-ringing-1", "AD-answered-2", "AD-restored-3"}                           # FULL ids; ended and blocked excluded
        assert d["AD-ringing-1"] == {"call_id": "AD-ringing-1", "from": "+15555550123", "age_s": d["AD-ringing-1"]["age_s"], "handoff": "none", "answered": False}
        assert d["AD-answered-2"]["handoff"] == "started" and d["AD-answered-2"]["answered"] is True
        assert d["AD-restored-3"]["handoff"] == "restored" and d["AD-ringing-1"]["age_s"] >= 0


def test_call_registry_survives_history_eviction():
    from server import relay
    bus.publish("call.incoming", "LONG1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    for i in range(bus.HISTORY_MAX + 50):                                              # a long call: its call.incoming scrolls out of history
        bus.publish("transcript.caller", "LONG1", {"utterance_id": str(i), "text": "x", "is_final": False})
    assert not any(e["type"] == "call.incoming" for e in bus.history)
    assert relay._known_call("LONG1") and "LONG1" in bus.CALLS                         # still known: /listen, /talk, rejoin keep working
    c = TestClient(app, client=("127.0.0.1", 5000))
    assert any(x["call_id"] == "LONG1" for x in c.get("/demo/status").json()["active_calls_detail"])
    bus.publish("handoff.started", "LONG1", {})
    for i in range(bus.HISTORY_MAX + 5): bus.publish("risk.update", "LONG1", {"s": 0.5})
    assert relay._decoy_on("LONG1") and not relay._call_ended("LONG1")
    bus.publish("call.ended", "LONG1", {}); assert relay._call_ended("LONG1") and not relay._decoy_on("LONG1")
    assert not any(x["call_id"] == "LONG1" for x in c.get("/demo/status").json()["active_calls_detail"])


def test_f17_events_redaction_for_remote_unpaired_viewers(monkeypatch):
    from server import device
    remote = TestClient(app)
    local = TestClient(app, base_url="http://127.0.0.1:8000", client=("127.0.0.1", 5000))
    tok = remote.post("/pair", json={"pin": device.PIN}).json()["device_token"]
    def watch(client, **kw):
        with client.websocket_connect("/events", **kw) as ws:
            bus.publish("call.incoming", "F17", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
            a = ws.receive_json()
            bus.publish("transcript.caller", "F17", {"utterance_id": "u", "text": "send gift card 4111 1111 1111 1111", "is_final": True})
            b = ws.receive_json()
            bus.publish("artifacts.extracted", "F17", {"artifacts": [{"type": "payment", "value": "4111111111111111"}]})
            c = ws.receive_json()
            bus.publish("blocklist.updated", "F17", {"number": "+15555550123", "scope": "her"})
            d = ws.receive_json()
            return a, b, c, d
    monkeypatch.delenv("EVENTS_REDACT", raising=False)
    a, b, c, d = watch(remote)                                                      # default: unchanged (existing UIs keep working)
    assert a["data"]["from"] == "+15555550123" and "gift card" in b["data"]["text"]
    monkeypatch.setenv("EVENTS_REDACT", "1")
    a, b, c, d = watch(remote)
    assert a["data"]["from"] != "+15555550123" and a["data"]["from"].endswith("23") and "*" in a["data"]["from"] and a["data"]["attestation"] == "C"
    assert b["data"]["text"] == "" and b["data"]["redacted"] is True and c["data"]["artifacts"] == [] and d["data"]["number"].endswith("23") and "*" in d["data"]["number"]
    for kw in ({"subprotocols": ["bf-device", tok]},):                              # paired device: full stream, subprotocol accepted
        a, b, c, d = watch(remote, **kw)
        assert a["data"]["from"] == "+15555550123" and "gift card" in b["data"]["text"] and d["data"]["number"] == "+15555550123"
    a, b, c, d = watch(local, headers={"host": "127.0.0.1:8000"})                  # operator's own browser (loopback, same origin): full
    assert a["data"]["from"] == "+15555550123" and "gift card" in b["data"]["text"]
    # and the masking helper never leaves a raw number behind in nested data
    from server.main import redact_event
    r = redact_event({"type": "intel.agent", "call_id": "x", "ts": 1, "data": {"plan": ["call +1 (555) 555-0123 now"], "n": {"k": "+15555550123"}}})
    assert "555-0123" not in str(r) and "5550123" not in str(r)


def test_handoff_failed_is_hub_only_type(monkeypatch):
    monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
    assert TestClient(app).post("/events", json={"type": "handoff.failed", "call_id": "x", "data": {"reason": "decoy_unavailable"}}).status_code == 403
    assert bus.publish("handoff.failed", "x", {"reason": "decoy_unavailable"})["type"] == "handoff.failed"


def test_unknown_call_events_dropped_for_pipeline_token_and_open_modes(monkeypatch, caplog):
    import logging
    c = TestClient(app)
    drill = lambda t, cid="DRILL-1", **h: c.post("/events", json={"type": t, "call_id": cid, "data": {"s": 0.9, "text": "x", "is_final": True, "level": "first", "why_chips": []}}, headers=h)
    for pt in (None, "pt-secret"):
        if pt: monkeypatch.setenv("PIPELINE_TOKEN", pt)
        else: monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
        hdr = {"x-pipeline-token": pt} if pt else {}
        n0 = len(bus.history)
        with caplog.at_level(logging.WARNING, logger="hub"):
            for t in ("transcript.caller", "risk.update", "alert.fired", "decoy.turn", "decoy.fake_value", "guardrail.tripped", "artifacts.extracted"):
                assert drill(t, **hdr).status_code == 404, t
        assert not any(e["call_id"] == "DRILL-1" for e in bus.history[n0:])               # nothing broadcast, no fake call
        assert any("event for unknown call dropped" in r.getMessage() for r in caplog.records)
    # a real call: accepted while live and for 30 min after it ends, refused later
    monkeypatch.delenv("PIPELINE_TOKEN", raising=False)
    bus.publish("call.incoming", "REAL-1", {"from": "+15555550123", "to": "+15555550100", "attestation": "C", "scam_id_score": 0.8})
    assert drill("risk.update", "REAL-1").status_code == 200
    bus.publish("call.ended", "REAL-1", {"ended_by": "caller", "duration_s": 5})
    assert drill("artifacts.extracted", "REAL-1").status_code == 200                       # late post-call artifacts still land
    bus.CALLS["REAL-1"]["t_end"] -= 1900
    assert drill("artifacts.extracted", "REAL-1").status_code == 404
    # types that are not call-bound (intel/campaign traces) and hub-internal publishes are unaffected
    assert c.post("/events", json={"type": "intel.agent", "call_id": "any-id", "data": {}}).status_code == 200
    assert bus.publish("risk.update", "internal-only", {"s": 0.1}) is not None
