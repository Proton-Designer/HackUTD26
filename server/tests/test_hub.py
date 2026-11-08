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
        assert c.post("/events", json={"type": "risk.update", "call_id": "x", "data": {"s": 0.1}}).json()["ok"]
        ev = ws.receive_json(); assert ev["type"] == "risk.update" and ev["call_id"] == "x" and "ts" in ev
        bus.publish("call.incoming", "x", {"from": "+15555550001"}); ws.receive_json()
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
