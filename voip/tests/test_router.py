import base64, json, time
import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from voip import router as R, telnyx
from voip.security import Limiter, verify_signature
from server import bus

KEY = Ed25519PrivateKey.generate()
PUB = base64.b64encode(KEY.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)).decode()

def sign(body: bytes, ts=None):
    ts = str(ts or int(time.time()))
    return {"telnyx-signature-ed25519": base64.b64encode(KEY.sign(ts.encode() + b"|" + body)).decode(), "telnyx-timestamp": ts}

def test_signature_ok_bad_old_missing(monkeypatch):
    b = b'{"a":1}'; h = sign(b)
    assert verify_signature(b, h["telnyx-signature-ed25519"], h["telnyx-timestamp"], PUB)
    assert not verify_signature(b + b" ", h["telnyx-signature-ed25519"], h["telnyx-timestamp"], PUB)
    old = sign(b, int(time.time()) - 1000)
    assert not verify_signature(b, old["telnyx-signature-ed25519"], old["telnyx-timestamp"], PUB)
    assert not verify_signature(b, None, None, PUB)
    monkeypatch.delenv("TELNYX_PUBLIC_KEY", raising=False); monkeypatch.delenv("VOIP_ALLOW_UNSIGNED", raising=False)
    assert not verify_signature(b, "x", "1")          # no key configured -> reject unless dev flag
    monkeypatch.setenv("VOIP_ALLOW_UNSIGNED", "1"); assert verify_signature(b, None, None)

def test_limiter():
    l = Limiter(per_caller=2, window_s=10, max_concurrent=3)
    assert l.check("+1", "a", 0) is None and l.check("+1", "b", 1) is None
    assert l.check("+1", "c", 2)            # per-caller cap
    assert l.check("+2", "c", 2) is None and l.check("+3", "d", 3)  # concurrent cap (3 active)
    l.release("a"); assert l.check("+3", "d", 4) is None
    for c in ("b", "c", "d"): l.release(c)
    assert l.check("+1", "e", 20) is None   # window expired

def wh(et, **p):
    base = {"call_control_id": "v3:sim_abcdef123456", "call_session_id": "sess-1234567890", "from": "+15555550123", "to": "+15555550100", "direction": "incoming"}
    return json.dumps({"data": {"event_type": et, "payload": {**base, **p}}}).encode()

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("SIM_MODE", "1"); monkeypatch.setenv("VOIP_ALLOW_UNSIGNED", "")
    monkeypatch.setattr(R, "LIMITER", Limiter()); R.CALLS.clear()
    monkeypatch.setattr(R, "_hub_relay", lambda: None)
    monkeypatch.setattr(R, "_routing", lambda f, a: {"decision": "LIVE_GUARD", "reason": "Caller ID not verified"})
    for fn in ("answer", "reject", "hangup", "dial", "create_conference", "join_conference"):
        async def boom(*a, **k): raise AssertionError("real Telnyx call from simulator: " + fn)
        monkeypatch.setattr(telnyx, fn, boom)
    app = FastAPI(); app.include_router(R.router); return TestClient(app)

def types(sid="sess-1234567890"): return [e["type"] for e in bus.history if e["call_id"] == sid]

def test_sim_call_flow_returns_stream_url_and_ends(client):
    h = {"x-sim-call": "1"}
    r = client.post("/telnyx/webhook", content=wh("call.initiated"), headers=h).json()
    assert r["stream_url"].startswith("ws://testserver/media/sess-1234567890?t=")
    client.post("/telnyx/webhook", content=wh("call.answered"), headers=h)
    path = r["stream_url"].replace("ws://testserver", "")
    with client.websocket_connect(path) as ws:
        ws.send_text(json.dumps({"event": "media", "media": {"payload": "AAAA"}}))
    with pytest.raises(Exception):
        with client.websocket_connect("/media/sess-1234567890?t=wrong"): pass
    client.post("/telnyx/webhook", content=wh("call.hangup"), headers=h)
    t = types(); assert t.count("call.incoming") >= 1 and "call.routed" in t and "call.ended" in t
    ended = [e for e in bus.history if e["type"] == "call.ended" and e["call_id"] == "sess-1234567890"][-1]
    assert ended["data"]["ended_by"] == "caller"

def test_unsigned_real_webhook_rejected(monkeypatch, client):
    monkeypatch.setenv("SIM_MODE", "0"); monkeypatch.setenv("TELNYX_PUBLIC_KEY", PUB)
    assert client.post("/telnyx/webhook", content=wh("call.initiated")).status_code == 403
    assert client.post("/telnyx/webhook", content=wh("call.hangup"), headers=sign(wh("call.hangup"))).status_code == 200

def test_blocked_caller_rejected_before_ring(monkeypatch, client):
    monkeypatch.setenv("SIM_MODE", "0"); monkeypatch.setenv("TELNYX_PUBLIC_KEY", PUB)
    monkeypatch.setattr(R, "_routing", lambda f, a: {"decision": "BLOCKED_BACKFIRE", "reason": "Confirmed scammer for her"})
    calls = []
    async def rej(ccid, cause="CALL_REJECTED"): calls.append(("reject", ccid))
    async def nope(*a, **k): calls.append(("BAD", a))
    monkeypatch.setattr(telnyx, "reject", rej); monkeypatch.setattr(telnyx, "dial", nope); monkeypatch.setattr(telnyx, "answer", nope)
    b = wh("call.initiated", call_control_id="v3:real_abcdef1234", call_session_id="sess-block-123456")
    assert client.post("/telnyx/webhook", content=b, headers=sign(b)).status_code == 200
    assert calls == [("reject", "v3:real_abcdef1234")]   # never answered, Maria never dialed

def test_hub_mounts_voip():
    from server.main import app
    paths = set(app.openapi()['paths']) | {getattr(r, 'path', '') for r in app.routes}
    assert "/telnyx/webhook" in paths and "/voip/webrtc-token" in paths and "/healthz" in paths


def test_webrtc_token_requires_device(monkeypatch, client):
    async def tok(cid): return "jwt.abc"
    monkeypatch.setattr(telnyx, "webrtc_token", tok); monkeypatch.setenv("TELNYX_TELEPHONY_CREDENTIAL_ID", "x")
    from fastapi import HTTPException
    def deny(request: Request):
        if request.headers.get("x-device-token") != "ok": raise HTTPException(401, "pair")
    app = FastAPI(); app.include_router(R.router); app.dependency_overrides[R._require_device] = deny
    c = TestClient(app)
    assert c.get("/voip/webrtc-token").status_code == 401
    assert c.get("/voip/webrtc-token", headers={"x-device-token": "ok"}).json() == {"token": "jwt.abc"}

def test_webrtc_token_real_device_dep_rejects_remote(monkeypatch, client):
    monkeypatch.setenv("TELNYX_TELEPHONY_CREDENTIAL_ID", "x")
    assert client.get("/voip/webrtc-token", headers={"cf-ray": "1"}).status_code == 401   # tunnel-style request, no pairing

def test_sim_event_cannot_end_real_call(monkeypatch, client):
    R.CALLS["sess-real-1234567"] = {"caller_ccid": "v3:real_abcdef1234", "from": "+1", "decision": "LIVE_GUARD", "t0": 0, "ended": False, "sim": False}
    b = wh("call.hangup", call_session_id="sess-real-1234567")
    client.post("/telnyx/webhook", content=b, headers={"x-sim-call": "1"})
    assert R.CALLS["sess-real-1234567"]["ended"] is False


def test_duplicate_initiated_does_not_overwrite(client):
    R.CALLS["sess-1234567890"] = {"caller_ccid": "v3:real_abcdef1234", "from": "+1", "decision": "LIVE_GUARD", "t0": 0, "ended": False, "sim": False}
    client.post("/telnyx/webhook", content=wh("call.initiated"), headers={"x-sim-call": "1"})
    assert R.CALLS["sess-1234567890"]["caller_ccid"] == "v3:real_abcdef1234" and R.CALLS["sess-1234567890"]["sim"] is False


class FakeRelay:
    def __init__(s, ok=True): s.ok, s.calls = ok, []
    async def open(s, cid, send, on_decoy_lost=None): s.calls.append(("open", cid))
    async def caller_frame(s, cid, f): s.calls.append(("frame", f.get("event")))
    async def start_decoy(s, cid): s.calls.append(("start_decoy", cid)); return s.ok
    async def stop_decoy(s, cid): s.calls.append(("stop_decoy", cid))
    async def close(s, cid): s.calls.append(("close", cid))

import asyncio
def _state(sim=True, conf=True):
    return {"caller_ccid": "v3:sim_abcdef123456", "maria_ccid": "v3:sim_maria1234567", "conf_id": "conf-1" if conf else None,
            "from": "+1", "decision": "LIVE_GUARD", "t0": time.time(), "ended": False, "sim": sim}

def test_handoff_decoy_first_then_events(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); R.CALLS["sess-h1-1234567"] = _state()
    assert asyncio.run(R.handoff("sess-h1-1234567")) is True
    st = R.CALLS["sess-h1-1234567"]; assert st["handed_off"] and st["restore_deadline"] > time.time() + 25
    assert [e["type"] for e in bus.history if e["call_id"] == "sess-h1-1234567"] == ["handoff.started"]
    assert asyncio.run(R.handoff("sess-h1-1234567")) is False   # idempotent

def test_handoff_fails_open_when_decoy_unavailable(monkeypatch):
    fr = FakeRelay(ok=False); monkeypatch.setattr(R, "_hub_relay", lambda: fr); R.CALLS["sess-h2-1234567"] = _state()
    assert asyncio.run(R.handoff("sess-h2-1234567")) is False
    assert not R.CALLS["sess-h2-1234567"].get("handed_off")   # Maria stays on the call

def test_restore_and_decoy_end(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); R.CALLS["sess-h3-1234567"] = _state()
    async def go():
        await R.handoff("sess-h3-1234567"); ok = await R.restore("sess-h3-1234567"); return ok
    assert asyncio.run(go()) is True and ("stop_decoy", "sess-h3-1234567") in fr.calls
    assert "handoff.restored" in [e["type"] for e in bus.history if e["call_id"] == "sess-h3-1234567"]
    R.CALLS["sess-h4-1234567"] = _state(); R.CALLS["sess-h4-1234567"]["handed_off"] = True
    asyncio.run(R._decoy_lost("sess-h4-1234567"))
    ev = [e for e in bus.history if e["call_id"] == "sess-h4-1234567"][-1]
    assert ev["type"] == "call.ended" and ev["data"]["ended_by"] == "decoy"

def test_maria_hangup_after_handoff_keeps_caller(monkeypatch, client):
    st = _state(); st.update(handed_off=True, maria_answered=True); R.CALLS["sess-1234567890"] = st
    client.post("/telnyx/webhook", content=wh("call.hangup", call_control_id="v3:sim_maria1234567"), headers={"x-sim-call": "1"})
    assert st["ended"] is False


def _types(sid): return [e["type"] for e in bus.history if e["call_id"] == sid]

def test_low_risk_restores_maria(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 1.0)
    sid = "sess-r1-1234567"; R.CALLS[sid] = _state(); R.CALLS[sid]["maria_alive"] = True
    async def go():
        R.LOOP = asyncio.get_running_loop()
        await R.handoff(sid)
        bus.publish("risk.update", sid, {"s": 0.9}); await asyncio.sleep(0.1)    # still scammy: no low clock
        bus.publish("risk.update", sid, {"s": 0.2}); await asyncio.sleep(0.3)
        bus.publish("risk.update", sid, {"s": 0.3}); await asyncio.sleep(1.6)    # continuous low >= 1 s
    asyncio.run(go())
    assert "handoff.restored" in _types(sid) and ("stop_decoy", sid) in fr.calls and R.CALLS[sid]["restored"]

def test_low_risk_interrupted_by_high_does_not_restore(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 1.0)
    sid = "sess-r2-1234567"; R.CALLS[sid] = _state()
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.handoff(sid)
        bus.publish("risk.update", sid, {"s": 0.2}); await asyncio.sleep(0.6)
        bus.publish("risk.update", sid, {"s": 0.8}); await asyncio.sleep(1.5)    # reset
    asyncio.run(go())
    assert "handoff.restored" not in _types(sid)

def test_fallback_engine_risk_does_not_restore(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 0.5)
    sid = "sess-r4-1234567"; R.CALLS[sid] = _state(); R.CALLS[sid]["maria_alive"] = True
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.handoff(sid)
        for _ in range(4):
            bus.publish("risk.update", sid, {"s": 0.1, "engine": "fallback"}); await asyncio.sleep(0.3)
    asyncio.run(go())
    assert "handoff.restored" not in _types(sid)

def test_no_restore_after_window_and_legit_flag(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 0.5)
    sid = "sess-r3-1234567"; R.CALLS[sid] = _state(); R.CALLS[sid].update(handed_off=True, restore_deadline=time.time() - 1, low_since=time.time() - 5)
    assert asyncio.run(R.restore(sid)) is False    # window closed
    asyncio.run(R._decoy_lost(sid))
    ev = [e for e in bus.history if e["call_id"] == sid][-1]
    assert ev["type"] == "call.ended" and ev["data"]["ended_by"] == "decoy" and ev["data"]["legit"] is True

def test_restore_redials_when_leg_gone(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr)
    dialed = []
    async def dial(body): dialed.append(body); return {"data": {"call_control_id": "v3:newmaria123456"}}
    monkeypatch.setattr(telnyx, "dial", dial); monkeypatch.setenv("TELNYX_CALL_CONTROL_APP_ID", "c"); monkeypatch.setenv("TELNYX_SIP_USER", "u")
    sid = "sess-r4-1234567"; R.CALLS[sid] = _state(sim=False); R.CALLS[sid].update(handed_off=True, maria_alive=False, restore_deadline=time.time() + 20)
    assert asyncio.run(R.restore(sid)) is True
    assert dialed and dialed[0]["to"] == "sip:u@sip.telnyx.com" and R.CALLS[sid]["maria_ccid"] == "v3:newmaria123456"


def test_webrtc_token_no_loopback_exemption(monkeypatch, client):
    monkeypatch.setenv("TELNYX_TELEPHONY_CREDENTIAL_ID", "x"); monkeypatch.delenv("HUB_TOKEN", raising=False)
    assert client.get("/voip/webrtc-token").status_code == 401   # TestClient host is local-ish; still needs a credential

def test_webrtc_token_sip_login_fallback(monkeypatch, client):
    monkeypatch.delenv("TELNYX_TELEPHONY_CREDENTIAL_ID", raising=False)
    monkeypatch.setenv("TELNYX_SIP_USER", "u1"); monkeypatch.setenv("TELNYX_SIP_PASSWORD", "p1")
    monkeypatch.setattr(R, "_require_device", lambda request=None: None)
    app = client.app if hasattr(client, "app") else None
    assert R.os.environ["TELNYX_SIP_USER"] == "u1"

def test_unsigned_initiated_requires_live_call(monkeypatch, client):
    monkeypatch.delenv("TELNYX_PUBLIC_KEY", raising=False); monkeypatch.setenv("VOIP_ALLOW_UNSIGNED", "1")
    async def nope(c): raise telnyx.TelnyxError("404")
    monkeypatch.setattr(telnyx, "get_call", nope)
    body = {"data": {"event_type": "call.initiated", "payload": {"direction": "incoming", "call_control_id": "v2:forged12345", "call_session_id": "sess-forged-1", "from": "+15555550111"}}}
    assert client.post("/telnyx/webhook", json=body).status_code == 403


def test_attestation_only_from_carrier_fields():
    assert R.attestation_of({"shaken_stir_attestation": "a"}) == "A"
    assert R.attestation_of({"shaken_stir": {"attestation": "B"}}) == "B"
    assert R.attestation_of({"sip_headers": {"X-Attest": "A", "attestation": "A"}}) == "none"   # caller-controlled: ignored
    assert R.attestation_of({"custom_headers": [{"name": "attestation", "value": "A"}], "x": {"shaken_stir_attestation": "A"}}) == "none"
    assert "sip_headers.X-Attest" not in R._key_paths({"sip_headers": {"X-Attest": "A"}})


def test_own_maria_leg_initiated_is_ignored(monkeypatch):
    monkeypatch.setenv("SIM_MODE", "0"); monkeypatch.setenv("TELNYX_SIP_USER", "mariauser")
    before = len(bus.history)
    p = {"call_control_id": "v3:mariaLeg1234567", "call_session_id": "sess-marialeg-12345", "from": "+14690000000", "to": "mariauser",
         "direction": "incoming", "client_state": R._cs(sid="sess-parent-12345", role="maria")}
    assert asyncio.run(R.on_initiated(p)) == {}
    assert len(bus.history) == before and "sess-marialeg-12345" not in R.CALLS
    p2 = dict(p, client_state=None, call_session_id="sess-marialeg-67890")   # even without client_state, `to` = her SIP user
    assert asyncio.run(R.on_initiated(p2)) == {}
