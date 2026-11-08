import base64, json, time
import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from fastapi import FastAPI
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

def test_voip_app_mounts_on_hub():
    from voip.app import app
    paths = set(app.openapi()['paths']) | {getattr(r, 'path', '') for r in app.routes}
    assert "/telnyx/webhook" in paths and "/voip/webrtc-token" in paths and "/healthz" in paths


def test_webrtc_token_fails_closed(monkeypatch, client):
    async def tok(cid): return "jwt.abc"
    monkeypatch.setattr(telnyx, "webrtc_token", tok); monkeypatch.setenv("TELNYX_TELEPHONY_CREDENTIAL_ID", "x")
    monkeypatch.delenv("HUB_TOKEN", raising=False); monkeypatch.delenv("VOIP_OPEN_TOKEN", raising=False)
    assert client.get("/voip/webrtc-token").status_code == 401
    monkeypatch.setenv("HUB_TOKEN", "s3"); assert client.get("/voip/webrtc-token").status_code == 401
    assert client.get("/voip/webrtc-token", headers={"x-hub-token": "s3"}).json() == {"token": "jwt.abc"}
    monkeypatch.delenv("HUB_TOKEN"); monkeypatch.setenv("VOIP_OPEN_TOKEN", "1")
    assert client.get("/voip/webrtc-token").json() == {"token": "jwt.abc"}

def test_sim_event_cannot_end_real_call(monkeypatch, client):
    R.CALLS["sess-real-1234567"] = {"caller_ccid": "v3:real_abcdef1234", "from": "+1", "decision": "LIVE_GUARD", "t0": 0, "ended": False, "sim": False}
    b = wh("call.hangup", call_session_id="sess-real-1234567")
    client.post("/telnyx/webhook", content=b, headers={"x-sim-call": "1"})
    assert R.CALLS["sess-real-1234567"]["ended"] is False


def test_duplicate_initiated_does_not_overwrite(client):
    R.CALLS["sess-1234567890"] = {"caller_ccid": "v3:real_abcdef1234", "from": "+1", "decision": "LIVE_GUARD", "t0": 0, "ended": False, "sim": False}
    client.post("/telnyx/webhook", content=wh("call.initiated"), headers={"x-sim-call": "1"})
    assert R.CALLS["sess-1234567890"]["caller_ccid"] == "v3:real_abcdef1234" and R.CALLS["sess-1234567890"]["sim"] is False
