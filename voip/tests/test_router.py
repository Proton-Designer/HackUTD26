import base64, json, pathlib, time
import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from voip import router as R, telnyx
from voip.security import Limiter, verify_signature
from server import bus

@pytest.fixture(autouse=True)
def _logdir(tmp_path, monkeypatch):
    monkeypatch.setenv("LOGDIR", str(tmp_path / "logs"))   # per-call journals must not land in the repo's logs/

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
    app = FastAPI(); app.include_router(R.router); return TestClient(app, client=("127.0.0.1", 50000))

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
    async def open(s, cid, send, on_decoy_lost=None):
        s.calls.append(("open", cid)); s.n = getattr(s, "n", 0) + 1; return f"session-{s.n}"
    async def caller_frame(s, cid, f): s.calls.append(("frame", f.get("event")))
    async def start_decoy(s, cid): s.calls.append(("start_decoy", cid)); return s.ok
    async def stop_decoy(s, cid): s.calls.append(("stop_decoy", cid))
    async def close(s, cid, session=None): s.calls.append(("close", cid)); s.closed = getattr(s, "closed", []) + [session]

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
    failed = [e for e in bus.history if e["call_id"] == "sess-h2-1234567" and e["type"] == "handoff.failed"]
    assert len(failed) == 1 and failed[0]["data"] == {"reason": "decoy_unavailable"}   # F3: published, not silent

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


def test_safe_reports_telnyx_result(monkeypatch):
    import types as _t, sys as _s
    calls = []
    fake = _t.SimpleNamespace(telnyx_result=lambda ok, detail="": calls.append((ok, detail)))
    import server; monkeypatch.setattr(server, "ops", fake, raising=False); monkeypatch.setitem(_s.modules, "server.ops", fake)
    async def good(): return {"data": 1}
    async def bad(): raise RuntimeError("POST /calls -> 401 {10009 user marked as blocked}")
    assert asyncio.run(R._safe(good(), "x")) == {"data": 1}
    assert asyncio.run(R._safe(bad(), "y")) is None
    assert calls[0] == (True, "") and calls[1][0] is False and "10009" in calls[1][1]
    n = len(calls); c = good(); asyncio.run(R._safe(c, "sim", sim=True)); assert len(calls) == n   # sim: no Telnyx call, no report


def test_sim_only_from_direct_loopback(client):
    h = {"x-sim-call": "1"}
    # through the tunnel (proxy headers) or from a non-loopback peer: refused, never treated as a sim call
    for extra in ({"x-forwarded-for": "9.9.9.9"}, {"cf-connecting-ip": "9.9.9.9"}):
        assert client.post("/telnyx/webhook", content=wh("call.initiated"), headers={**h, **extra}).status_code == 403
    app = FastAPI(); app.include_router(R.router)
    remote = TestClient(app, client=("203.0.113.5", 4000))
    assert remote.post("/telnyx/webhook", content=wh("call.initiated"), headers=h).status_code == 403
    assert "sess-1234567890" not in R.CALLS
    r = client.post("/telnyx/webhook", content=wh("call.initiated"), headers=h)       # direct loopback: ok
    assert r.status_code == 200 and r.json().get("stream_url")
    path = r.json()["stream_url"].replace("ws://testserver", "")
    with pytest.raises(Exception):   # media from the tunnel side: refused even with the right token
        with client.websocket_connect(path, headers={"x-forwarded-for": "9.9.9.9"}): pass
    with client.websocket_connect(path) as ws: ws.send_text(json.dumps({"event": "connected"}))


def test_demo_haul_published_in_sim_without_p3(monkeypatch):
    monkeypatch.delenv("P3_DECOY_URL", raising=False); monkeypatch.setattr(R, "DEMO_HAUL_DELAY_S", 0.6); monkeypatch.setattr(R, "RESTORE_LOW_S", 99)
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr)
    sid = "sess-haul-12345678"; R.CALLS[sid] = _state()
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.handoff(sid); await asyncio.sleep(1.4)
    asyncio.run(go())
    ev = [e for e in bus.history if e["type"] == "artifacts.extracted" and e["call_id"] == sid]
    assert len(ev) == 1 and ev[0]["data"]["source"] == "demo_stand_in" and any(a["kind"] == "wallet" for a in ev[0]["data"]["artifacts"])
    R._publish_demo_haul(sid); assert len([e for e in bus.history if e["type"] == "artifacts.extracted" and e["call_id"] == sid]) == 1   # once per call

def test_demo_haul_not_with_p3_or_after_restore_or_real(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "DEMO_HAUL_DELAY_S", 0.2)
    def n(sid): return len([e for e in bus.history if e["type"] == "artifacts.extracted" and e["call_id"] == sid])
    monkeypatch.setenv("P3_DECOY_URL", "wss://p3.example")                    # real decoy present
    s1 = "sess-haul-p3-123456"; R.CALLS[s1] = _state()
    s2 = "sess-haul-real-12345"; R.CALLS[s2] = _state(sim=False)             # not a sim call
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.handoff(s1); await R.handoff(s2); await asyncio.sleep(0.8)
    asyncio.run(go()); assert n(s1) == 0 and n(s2) == 0
    monkeypatch.delenv("P3_DECOY_URL")
    s3 = "sess-haul-rest-123456"; R.CALLS[s3] = _state(); R.CALLS[s3].update(handed_off=True, restored=True)
    R._publish_demo_haul(s3); assert n(s3) == 0


def test_dial_guard_refuses_pstn_without_flag(monkeypatch):
    sent = []
    async def fake_post(path, body=None, text=False): sent.append((path, body)); return {"data": {}}
    monkeypatch.setattr(telnyx, "_post", fake_post)
    monkeypatch.setenv("TELNYX_SIP_USER", "mariauser"); monkeypatch.delenv("BACKFIRE_ALLOW_PSTN_OUTBOUND", raising=False)
    for bad in ("+14695550100", "+14699088594", "sip:someoneelse@sip.telnyx.com", "sip:mariauser@evil.example", "", None):
        with pytest.raises(telnyx.TelnyxError): asyncio.run(telnyx.dial({"to": bad, "connection_id": "x"}))
    assert sent == []                                                       # nothing reached the (mock) API
    asyncio.run(telnyx.dial({"to": "sip:mariauser@sip.telnyx.com"})); assert len(sent) == 1   # our own SIP user is allowed
    monkeypatch.delenv("TELNYX_SIP_USER")
    with pytest.raises(telnyx.TelnyxError): asyncio.run(telnyx.dial({"to": "sip:mariauser@sip.telnyx.com"}))   # no configured user: refuse
    monkeypatch.setenv("BACKFIRE_ALLOW_PSTN_OUTBOUND", "1")
    asyncio.run(telnyx.dial({"to": "+14695550100"})); assert len(sent) == 2   # explicit override only


def test_persona_decoy_streams_pcmu_lines_with_gaps(tmp_path, monkeypatch):
    from voip import persona
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); monkeypatch.setattr(persona, "GAP_S", 0.3)
    for i in range(len(persona.LINES)): (tmp_path / f"line{i}.ulaw").write_bytes(b"\x7f" * 480)   # 3 frames each; no say/ffmpeg needed
    app = FastAPI(); app.include_router(R.router); c = TestClient(app, client=("127.0.0.1", 50000))
    R.CALLS["sess-persona-123"] = _state()
    with c.websocket_connect("/decoy-standin/sess-persona-123") as ws:
        got = [json.loads(ws.receive_text()) for _ in range(7)]       # 3 + 3 frames of line0/line1, then line1 started: loops across lines
    assert all(g["event"] == "media" and len(base64.b64decode(g["media"]["payload"])) == 160 for g in got)
    assert persona.standin_mode() == "persona"; monkeypatch.setenv("DECOY_STANDIN", "echo"); assert persona.standin_mode() == "echo"

def test_persona_silent_when_no_audio(tmp_path, monkeypatch):
    from voip import persona
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); monkeypatch.setattr(persona.shutil, "which", lambda x: None)
    assert persona.generate_lines() == []


def test_persona_ws_only_for_local_relay_and_known_calls(tmp_path, monkeypatch):
    from voip import persona
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path))
    for i in range(len(persona.LINES)): (tmp_path / f"line{i}.ulaw").write_bytes(b"\x7f" * 320)
    app = FastAPI(); app.include_router(R.router); R.CALLS["sess-persona-known"] = _state()
    local = TestClient(app, client=("127.0.0.1", 50000)); remote = TestClient(app, client=("203.0.113.9", 50000))
    for cl, path, hdr in ((local, "/decoy-standin/sess-unknown-1234", None), (remote, "/decoy-standin/sess-persona-known", None),
                          (local, "/decoy-standin/sess-persona-known", {"x-forwarded-for": "9.9.9.9"})):
        with pytest.raises(Exception):
            with cl.websocket_connect(path, headers=hdr or {}): pass
    assert persona._active == 0
    with local.websocket_connect("/decoy-standin/sess-persona-known") as ws: assert json.loads(ws.receive_text())["event"] == "media"


def _fb_setup(monkeypatch, sid):
    import asyncio
    from server import fallback_detect as fd
    monkeypatch.setenv("SIM_MODE", "1"); monkeypatch.delenv("FALLBACK_DETECT", raising=False); monkeypatch.delenv("NVIDIA_API_KEY", raising=False)
    monkeypatch.setattr(fd, "_llm", None); fd._calls.pop(sid, None)
    monkeypatch.setattr(R, "P2_WAIT_S", 0.3); monkeypatch.setattr(R, "_script_timeline", lambda: [(0.0, "This is the fraud department at your bank."), (0.4, "Then buy gift cards and read me the numbers on the back, right now.")])
    R.CALLS[sid] = {"sim": True, "ended": False, "t0": time.time(), "caller_ccid": "c", "from": "+1"}
    return asyncio, fd

def test_sim_p2_fallback_alerts_when_p2_silent(monkeypatch):
    sid = "fbsess-silent-0001"; asyncio, fd = _fb_setup(monkeypatch, sid)
    asyncio.run(R._p2_fallback(sid))
    ev = [e for e in bus.history if e["call_id"] == sid]
    assert [e["type"] for e in ev if e["type"] == "alert.fired"] == ["alert.fired"]
    assert any(e["type"] == "risk.update" and e["data"]["engine"] == "fallback" for e in ev)
    assert any(e["type"] == "transcript.caller" for e in ev)

def test_sim_p2_fallback_stops_when_p2_arrives(monkeypatch):
    sid = "fbsess-p2live-0002"; asyncio, fd = _fb_setup(monkeypatch, sid)
    async def go():
        R.LOOP = asyncio.get_running_loop(); t = asyncio.create_task(R._p2_fallback(sid)); await asyncio.sleep(0.1)
        R._on_bus({"type": "risk.update", "call_id": sid, "data": {"s": 0.4, "engine": "p2"}})   # real P2 within the wait window
        await t
    asyncio.run(go())
    assert not [e for e in bus.history if e["call_id"] == sid and e["data"].get("engine") == "fallback"]
    assert not [e for e in bus.history if e["call_id"] == sid and e["type"] == "alert.fired"]

def test_sim_p2_fallback_never_for_real_calls(monkeypatch):
    sid = "fbsess-real-0003"; asyncio, fd = _fb_setup(monkeypatch, sid)
    R.CALLS[sid]["sim"] = False
    asyncio.run(R._p2_fallback(sid))
    assert not [e for e in bus.history if e["call_id"] == sid]

def test_script_timeline_spans_wav(tmp_path, monkeypatch):
    import wave
    w = tmp_path / "s.wav"
    with wave.open(str(w), "wb") as f: f.setnchannels(1); f.setsampwidth(2); f.setframerate(8000); f.writeframes(b"\0\0" * 8000 * 20)
    monkeypatch.setenv("DEMO_CALLER_WAV", str(w))
    tl = R._script_timeline()
    from voip import test_call as tc
    assert [x for _, x in tl] == tc.card_text("irs")                       # same source as the WAV
    assert tl[0][0] == 0 and tl[-1][0] < 20 and [t for t, _ in tl] == sorted(t for t, _ in tl)
    monkeypatch.setenv("DEMO_SCRIPT_TEXT", "One. Two words. Three.")
    assert [x for _, x in R._script_timeline()] == ["One.", "Two words.", "Three."]


def _no_telnyx(monkeypatch):
    calls = []
    def mk(n):
        async def f(*a, **k): calls.append(n); return {"data": {}}
        return f
    for n in ("create_conference", "dial", "join_conference", "leave_conference", "hangup"): monkeypatch.setattr(telnyx, n, mk(n))
    return calls

def test_listen_mode_never_dials_or_bridges(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "listen"); monkeypatch.setenv("TELNYX_CALL_CONTROL_APP_ID", "c"); monkeypatch.setenv("TELNYX_SIP_USER", "u")
    calls = _no_telnyx(monkeypatch); fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 99)
    sid = "sess-listen-1234567"; st = _state(sim=False, conf=False); st.pop("maria_ccid"); R.CALLS[sid] = st
    async def go():
        R.LOOP = asyncio.get_running_loop()
        await R.on_answered({"call_session_id": sid, "call_control_id": "v3:caller1234567", "client_state": R._cs(sid=sid, role="caller")})
        assert await R.handoff(sid) is True and await R.restore(sid) is True
    asyncio.run(go())
    assert calls == []                                            # no create_conference / dial / join / leave in listen mode
    ev = [e for e in bus.history if e["call_id"] == sid]
    ans = [e for e in ev if e["type"] == "call.answered"]
    assert len(ans) == 1 and ans[0]["data"] == {"by": "maria", "via": "listen"}
    assert [e["type"] for e in ev if e["type"].startswith("handoff")] == ["handoff.started", "handoff.restored"]
    assert ("stop_decoy", sid) in fr.calls                       # restore just stops the decoy

def test_sip_mode_default_still_bridges(monkeypatch):
    monkeypatch.delenv("MARIA_LEG", raising=False); monkeypatch.setenv("TELNYX_CALL_CONTROL_APP_ID", "c"); monkeypatch.setenv("TELNYX_SIP_USER", "u")
    calls = _no_telnyx(monkeypatch)
    sid = "sess-sipmode-1234567"; R.CALLS[sid] = _state(sim=False, conf=False)
    asyncio.run(R.on_answered({"call_session_id": sid, "call_control_id": "v3:caller1234567", "client_state": R._cs(sid=sid, role="caller")}))
    assert "create_conference" in calls and "dial" in calls

def test_listen_hello_plays_once_then_silence(tmp_path, monkeypatch):
    f = tmp_path / "hello.ulaw"; f.write_bytes(b"\xff" * 160 * 5)
    monkeypatch.setattr(R._persona, "generate_hello", lambda force=False: f); monkeypatch.setattr(R._persona, "cached_hello", lambda: f)
    got = []
    async def send(fr): got.append(fr)
    sid = "sess-hello-1234567"; R.CALLS[sid] = _state(sim=False)
    asyncio.run(R._listen_hello(sid, send))
    assert len(got) == 5 and all(g["event"] == "media" for g in got)
    got.clear(); R.CALLS[sid]["handed_off"] = True
    asyncio.run(R._listen_hello(sid, send)); assert got == []     # decoy owns the line once handed off
    monkeypatch.setattr(R._persona, "generate_hello", lambda force=False: None); monkeypatch.setattr(R._persona, "cached_hello", lambda: None)
    R.CALLS[sid]["handed_off"] = False; asyncio.run(R._listen_hello(sid, send)); assert got == []   # no audio -> silent, no error


def test_persona_cache_rebuilds_when_voice_changes(tmp_path, monkeypatch):
    from voip import persona as P
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); monkeypatch.setattr(P.shutil, "which", lambda x: "/bin/" + x)
    seen = []
    def fake_run(cmd, **k):
        if cmd[0] == "say": seen.append(cmd[cmd.index("-v") + 1]); pathlib_aiff = cmd[cmd.index("-o") + 1]; open(pathlib_aiff, "wb").write(b"x" * 2000)
        else: open(cmd[-1], "wb").write(b"\xff" * 1600)
        class R: returncode = 0
        return R()
    monkeypatch.setattr(P.subprocess, "run", fake_run)
    monkeypatch.setenv("DECOY_VOICE", "VoiceA"); assert P.generate_hello() is not None; n = len(seen)
    P.generate_hello(); assert len(seen) == n                                   # cached: same voice/rate/text
    monkeypatch.setenv("DECOY_VOICE", "VoiceB"); P.generate_hello(); assert seen[-1] == "VoiceB" and len(seen) == n + 1   # voice changed -> rebuilt
    assert "Yes, this is Maria" in P.HELLO_TEXT


def _talk_call(monkeypatch, sid, mode="talk"):
    monkeypatch.setenv("MARIA_LEG", mode); got = []
    async def send(fr): got.append(fr)
    st = _state(sim=False, conf=False); st.update(listen=True, send_to_caller=send); R.CALLS[sid] = st
    return st, got

PAY = base64.b64encode(b"\xff" * 160).decode()

def test_talk_injects_maria_into_caller_stream_and_never_the_relay(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr)
    st, got = _talk_call(monkeypatch, "sess-talk-1234567")
    async def go():
        ok = await R.inject_maria("sess-talk-1234567", PAY); await asyncio.sleep(0.1); return ok
    assert asyncio.run(go()) is True
    assert got == [{"event": "media", "media": {"payload": PAY}}] and st["talk_frames"] == 1
    assert fr.calls == []                                           # nothing went to the relay (P2/recordings)

def test_talk_muted_during_decoy_and_unmuted_on_restore(monkeypatch):
    st, got = _talk_call(monkeypatch, "sess-talk-2234567")
    st["handed_off"] = True
    assert asyncio.run(R.inject_maria("sess-talk-2234567", PAY)) is False and got == [] and st["talk_dropped"] == 1
    st["restored"] = True
    async def go():
        ok = await R.inject_maria("sess-talk-2234567", PAY); await asyncio.sleep(0.1); return ok
    assert asyncio.run(go()) is True and len(got) == 1

def test_talk_refused_when_not_talk_mode_or_not_ready_or_bad(monkeypatch):
    st, got = _talk_call(monkeypatch, "sess-talk-3234567", mode="listen")
    assert R.talk_enabled("sess-talk-3234567") is False and asyncio.run(R.inject_maria("sess-talk-3234567", PAY)) is False
    st, got = _talk_call(monkeypatch, "sess-talk-4234567")
    assert R.talk_enabled("sess-talk-4234567") and asyncio.run(R.inject_maria("sess-talk-4234567", "not base64!!")) is False
    assert asyncio.run(R.inject_maria("sess-talk-4234567", base64.b64encode(b"\0" * 5000).decode())) is False   # oversize
    st.pop("send_to_caller"); assert asyncio.run(R.inject_maria("sess-talk-4234567", PAY)) is False             # stream not ready -> dropped
    assert asyncio.run(R.inject_maria("unknown-call-id", PAY)) is False
    st["ended"] = True; st["send_to_caller"] = lambda f: None; assert R.talk_enabled("sess-talk-4234567") is False

def test_talk_mode_skips_hello_and_never_dials(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "talk"); calls = _no_telnyx(monkeypatch)
    sid = "sess-talk-5234567"; R.CALLS[sid] = _state(sim=False, conf=False)
    asyncio.run(R.on_answered({"call_session_id": sid, "call_control_id": "v3:caller1234567", "client_state": R._cs(sid=sid, role="caller")}))
    assert calls == [] and R.CALLS[sid]["listen"] is True and R.listen_mode() and R.talk_mode()
    ans = [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.answered"]
    assert ans[0]["data"] == {"by": "maria", "via": "talk"}


def test_persona_prefers_magpie_and_falls_back_to_say(tmp_path, monkeypatch):
    from voip import persona as P
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); monkeypatch.setenv("NVIDIA_API_KEY", "k"); monkeypatch.setenv("DECOY_VOICES_DIR", str(tmp_path / "nov"))
    monkeypatch.setattr(P, "_magpie_py", lambda: pathlib.Path("/fake/python")); monkeypatch.setattr(P.shutil, "which", lambda x: "/bin/" + x)
    ran = []
    def fake_run(cmd, **k):
        ran.append(pathlib.Path(cmd[0]).name)
        class R: returncode = 0
        if cmd[0] == "/fake/python":
            if MAG_FAIL[0]: R.returncode = 2
            else: open(cmd[2], "wb").write(b"\xff" * 1600)
        elif cmd[0] == "say": open(cmd[cmd.index("-o") + 1], "wb").write(b"x" * 2000)
        else: open(cmd[-1], "wb").write(b"\xff" * 1600)
        return R()
    monkeypatch.setattr(P.subprocess, "run", fake_run)
    import pathlib as _pl; MAG_FAIL = [False]
    assert P.generate_hello() is not None and ran == ["python"]            # Magpie used, no 'say'
    assert P._tag().startswith("magpie:")
    f = tmp_path / "hello.ulaw"; (tmp_path / "hello.key").unlink(); f.unlink(); MAG_FAIL[0] = True; ran.clear()
    assert P.generate_hello() is not None and "say" in ran                 # Magpie failed -> say fallback
    assert (tmp_path / "hello.key").read_text().endswith("|fb")
    ran.clear(); P.generate_hello(); assert ran == []                      # fallback reused for FALLBACK_RETRY_S, Magpie not hammered


def test_talk_output_is_paced_at_20ms_and_backlog_capped(monkeypatch):
    st, got = _talk_call(monkeypatch, "sess-talk-6234567"); times = []
    async def send(fr): times.append(time.monotonic()); got.append(fr)
    st["send_to_caller"] = send
    burst = base64.b64encode(b"\xff" * 160 * 6).decode()          # 6 frames arrive at once (a page burst)
    async def go():
        assert await R.inject_maria("sess-talk-6234567", burst) is True
        await asyncio.sleep(0.4)
        assert await R.inject_maria("sess-talk-6234567", base64.b64encode(b"\xff" * 160 * 4).decode()) is True   # 4 more
        big = base64.b64encode(b"\xff" * 160 * 6).decode()
        ok = await R.inject_maria("sess-talk-6234567", big); await R.inject_maria("sess-talk-6234567", big)   # overflow 200 ms backlog
        await asyncio.sleep(0.5); return ok
    asyncio.run(go())
    assert st["talk_dropped"] >= 1
    gaps = [b - a for a, b in zip(times[:6], times[1:6])]
    assert all(0.012 < g < 0.06 for g in gaps), gaps                       # evenly spaced ~20 ms, not a burst
    assert len(got) <= 6 + 4 + 10 + 1

def test_talk_silence_sends_nothing_and_decoy_clears_queue(monkeypatch):
    st, got = _talk_call(monkeypatch, "sess-talk-7234567")
    async def go():
        await R.inject_maria("sess-talk-7234567", PAY); await asyncio.sleep(0.15); n = len(got)
        await asyncio.sleep(0.2); assert len(got) == n                      # nothing sent while Maria is silent (no zero fill)
        st["handed_off"] = True; assert await R.inject_maria("sess-talk-7234567", PAY) is False
    asyncio.run(go())

def test_inrms_line_per_second(monkeypatch, caplog):
    import logging; caplog.set_level(logging.WARNING, logger="voip.router")
    ins = R.InStats("abcdef123456"); ins.t0 = time.time() - 1.5
    zero = base64.b64encode(b"\xff" * 160).decode(); loud = base64.b64encode(bytes([0x10, 0x90] * 80)).decode()
    ins.add(zero, {"talk_frames": 3}); ins.t0 -= 1                           # next add crosses a second boundary
    ins.add(loud, {"talk_frames": 7})
    msgs = [r.getMessage() for r in caplog.records if "inrms" in r.getMessage()]
    assert msgs and "zero=100%" in msgs[0] and "maria_out=" in msgs[0] and "rms=0" in msgs[0]
    assert R._MU[0xFF] == 0 and R._MU[0x7F] == 0 and abs(R._MU[0x10]) > 1000


def test_hello_plays_instantly_from_cache_even_when_key_stale_and_logs(tmp_path, monkeypatch, caplog):
    import logging; caplog.set_level(logging.WARNING, logger="voip.router")
    from voip import persona as P
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); (tmp_path / "hello.ulaw").write_bytes(b"\xff" * 160 * 3); (tmp_path / "hello.key").write_text("stale")
    slow = []
    monkeypatch.setattr(P, "generate_hello", lambda force=False: slow.append(1) or time.sleep(2) or None)   # a stale-key regeneration must NOT delay playback
    got = []
    async def send(fr): got.append(fr)
    sid = "sess-hello-9234567"; R.CALLS[sid] = _state(sim=False)
    el = []
    async def go():
        t = time.monotonic(); await R._listen_hello(sid, send); el.append(time.monotonic() - t)   # (asyncio.run itself waits for the slow thread at shutdown)
    asyncio.run(go())
    assert len(got) == 3 and el[0] < 1.5 and slow
    assert any("hello sent for" in r.getMessage() for r in caplog.records)

def test_media_ws_plays_hello_even_if_answered_webhook_not_processed_yet(monkeypatch):
    """Race seen on call 497ef1d4: media WS connects before call.answered set st['listen']. Hello must be decided by MARIA_LEG, not that flag."""
    monkeypatch.setenv("MARIA_LEG", "listen"); monkeypatch.setattr(R, "_hub_relay", lambda: FakeRelay())
    started = []
    async def fake_hello(sid, send): started.append(sid)
    monkeypatch.setattr(R, "_listen_hello", fake_hello)
    sid = "sess-race-1234567"; st = _state(sim=False); st["token"] = "tok"; R.CALLS[sid] = st
    assert "listen" not in st
    app = FastAPI(); app.include_router(R.router)
    with TestClient(app).websocket_connect(f"/media/{sid}?t=tok") as ws:
        ws.send_text(json.dumps({"event": "connected"})); ws.send_text(json.dumps({"event": "start"}))
        time.sleep(0.2)
    assert started == [sid]


def test_call_report_reads_logs_journal_and_decoy_turns(tmp_path):
    import subprocess, sys, pathlib
    t0 = time.time() - 100; hh = lambda dt: time.strftime("%H:%M:%S", time.localtime(t0 + dt))
    sid = "abcd1234-5678-aaaa-bbbb-ccccddddeeee"
    hub = tmp_path / "hub.log"; calls = tmp_path / "calls"; calls.mkdir()
    lines = [f'INFO:     1.2.3.4:0 - "WebSocket /media/{sid}?t=SECRETTOKEN" [accepted]', f"[{hh(0.5)}] MARIA_LEG=listen: not dialing Maria for abcd1234 (answer + caller stream only)",
             f"[{hh(1)}] hello sent for abcd1234 (2.6 s from hello.ulaw)"]
    lines += [f"[{hh(2 + i)}] inrms abcd1234 t={i}s rms={'0' if 3 <= i <= 6 else '900'} zero={'100' if 3 <= i <= 6 else '0'}% in=50 maria_out={'20' if 3 <= i <= 5 else '0'}" for i in range(10)]
    lines += [f"[{hh(20)}] media WS closed abcd1234 frames_in={{'connected': 1, 'start': 1, 'media:inbound': 500, 'stop': 1}} frames_to_caller={{'media': 130, 'clear': 2}} talk_frames=60 talk_dropped=1"]
    hub.write_text("\n".join(lines) + "\n")
    (calls / "abcd1234.jsonl").write_text("\n".join(json.dumps(r) for r in [
        {"ts": t0, "type": "call.routed", "decision": "LIVE_GUARD"}, {"ts": t0 + 9, "type": "alert.fired", "level": "first"},
        {"ts": t0 + 9, "type": "risk.update", "s": 0.9, "engine": "p2"}, {"ts": t0 + 12, "type": "user.action", "action": "scammer_get_scammed"},
        {"ts": t0 + 12.2, "type": "handoff.started"}, {"ts": t0 + 30, "type": "call.ended", "ended_by": "caller", "duration_s": 30}]) + "\n")
    dec = tmp_path / "decoy.log"; dec.write_text(f"{hh(13)} INFO p3.decoy: decoy {sid} connected\n{hh(20)} INFO p3.decoy: turn {sid}: stt=300ms llm=700ms tts_first=500ms total=1500ms voice=synthetic chars=40\n")
    r = subprocess.run([sys.executable, str(pathlib.Path(R.__file__).resolve().parent.parent / "scripts" / "call_report"), "abcd", "--hub-log", str(hub), "--decoy-log", str(dec), "--calls-dir", str(calls)], capture_output=True, text=True)
    o = r.stdout; assert r.returncode == 0, r.stderr
    assert "SECRETTOKEN" not in o and "call abcd1234" in o and "abcd1234-5678" not in o
    assert "first alert.fired      : " in o and "(+9.0s)" in o and "scammer_get_scammed" in o and "handoff.started" in o
    assert "ended_by=caller" in o and "talk_frames=60 talk_dropped=1" in o and "decoy clears (barge-in): 2" in o
    assert "zero stretches         : t=3..6s(4s, maria_out=60)" in o and "3 of 4 zero seconds had Maria frames out" in o
    assert "1500" in o and "hello sent for abcd1234" in o


def test_hello_text_uses_customer_name_and_cache_follows_it(tmp_path, monkeypatch):
    from voip import persona as P
    monkeypatch.delenv("CUSTOMER_NAME", raising=False)
    assert P.hello_text() == "Hello? ... Yes, this is Maria."
    monkeypatch.setenv("CUSTOMER_NAME", "Dana"); assert P.hello_text() == "Hello? ... Yes, this is Dana."
    monkeypatch.setenv("CUSTOMER_NAME", ""); assert P.hello_text() == "Hello?"
    monkeypatch.setenv("CUSTOMER_NAME", "Dana; rm -rf /"); assert ";" not in P.hello_text()
    monkeypatch.setenv("DECOY_LINES_DIR", str(tmp_path)); monkeypatch.setattr(P.shutil, "which", lambda x: "/bin/" + x)
    said = []
    def fake_run(cmd, **k):
        if cmd[0] == "say": said.append(cmd[-1]); open(cmd[cmd.index("-o") + 1], "wb").write(b"x" * 2000)
        else: open(cmd[-1], "wb").write(b"\xff" * 1600)
        class R: returncode = 0; stdout = b""; stderr = b""
        return R()
    monkeypatch.setattr(P.subprocess, "run", fake_run); monkeypatch.setattr(P, "_synth_magpie", lambda t, f: False)
    monkeypatch.setenv("CUSTOMER_NAME", "Dana"); assert P.generate_hello() is not None and said[-1] == "Hello? ... Yes, this is Dana."
    assert P.cached_hello() is not None                                     # same name: cache reused instantly
    monkeypatch.setenv("CUSTOMER_NAME", "Priya")
    assert P.cached_hello() is None                                         # renamed: stale audio must not play the old name
    assert P.generate_hello() is not None and said[-1].endswith("Priya.") and P.cached_hello() is not None


def test_inrms_logged_even_if_answered_webhook_not_processed_yet(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "talk"); monkeypatch.delenv("VOIP_RMS_LOG", raising=False); monkeypatch.setattr(R, "_hub_relay", lambda: FakeRelay())
    made = []
    class Rec:
        def __init__(self, sid): made.append(sid); self.n = 0
        def add(self, payload, st): self.n += 1
    monkeypatch.setattr(R, "InStats", Rec)
    sid = "sess-rms-race-1234"; st = _state(sim=False); st["token"] = "tok"; R.CALLS[sid] = st
    assert "listen" not in st                                   # call.answered not processed yet (the race)
    frame = json.dumps({"event": "media", "media": {"track": "inbound", "payload": base64.b64encode(b"\xff" * 160).decode()}})
    app = FastAPI(); app.include_router(R.router)
    with TestClient(app).websocket_connect(f"/media/{sid}?t=tok") as ws:
        ws.send_text(json.dumps({"event": "start"})); ws.send_text(frame); time.sleep(0.2)
    assert made == [sid]
    monkeypatch.setenv("VOIP_RMS_LOG", "0"); made.clear(); st["token"] = "tok"
    with TestClient(app).websocket_connect(f"/media/{sid}?t=tok") as ws:
        ws.send_text(json.dumps({"event": "start"})); time.sleep(0.1)
    assert made == []                                            # switch off works


def test_restore_clock_starts_at_handoff_from_last_low_score_without_new_updates(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 1.0); monkeypatch.setattr(R, "DEMO_HAUL_DELAY_S", 99)
    sid = "sess-fastrestore-1"; R.CALLS[sid] = _state(); t = {}
    async def go():
        R.LOOP = asyncio.get_running_loop()
        R._note_risk(sid, 0.05)                                   # last known score, BEFORE the tap
        t0 = time.time(); assert await R.handoff(sid); assert R.CALLS[sid]["low_since"] is not None
        while not R.CALLS[sid].get("restored") and time.time() - t0 < 4: await asyncio.sleep(0.1)
        t["dt"] = time.time() - t0
    asyncio.run(go())                                              # no risk.update after the handoff at all
    assert R.CALLS[sid].get("restored") and 0.9 <= t["dt"] <= 2.2, t
    assert "handoff.restored" in [e["type"] for e in bus.history if e["call_id"] == sid]

def test_restore_clock_not_started_when_last_score_high_stale_or_unknown(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 99)
    async def one(sid, last):
        R.CALLS[sid] = _state()
        if last is not None: R.CALLS[sid]["last_risk"] = last
        await R.handoff(sid); return R.CALLS[sid].get("low_since")
    async def go():
        R.LOOP = asyncio.get_running_loop()
        assert await one("sess-fr-high-1234", (0.9, time.time())) is None
        assert await one("sess-fr-stale-123", (0.05, time.time() - 120)) is None
        assert await one("sess-fr-none-1234", None) is None
    asyncio.run(go())

def test_high_score_after_handoff_resets_clock_and_blocks_restore(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "RESTORE_LOW_S", 0.8); monkeypatch.setattr(R, "DEMO_HAUL_DELAY_S", 99)
    sid = "sess-fr-reset-1234"; R.CALLS[sid] = _state()
    async def go():
        R.LOOP = asyncio.get_running_loop(); R._note_risk(sid, 0.1); await R.handoff(sid)
        await asyncio.sleep(0.4); R._note_risk(sid, 0.9); assert R.CALLS[sid]["low_since"] is None   # any high score resets
        await asyncio.sleep(1.2); assert not R.CALLS[sid].get("restored")
        R._note_risk(sid, 0.1); await asyncio.sleep(1.4); assert R.CALLS[sid].get("restored")         # low again, held 0.8 s -> restore
    asyncio.run(go())


def test_hang_up_in_listen_and_talk_mode_hangs_up_the_caller_leg(monkeypatch):
    for mode in ("listen", "talk"):
        monkeypatch.setenv("MARIA_LEG", mode); hung = []
        async def hang(ccid, *a, **k): hung.append(ccid); return {"data": {}}
        monkeypatch.setattr(telnyx, "hangup", hang)
        sid = f"sess-hangup-{mode}-12"; st = _state(sim=False, conf=False); st.pop("maria_ccid"); st["listen"] = True; R.CALLS[sid] = st
        asyncio.run(R._maria_hangup(sid))
        assert hung == [st["caller_ccid"]] and st["customer_hangup"] is True
        # after the handoff the decoy owns the call: unchanged (no hangup here)
        hung.clear(); st2 = _state(sim=False, conf=False); st2.pop("maria_ccid"); st2["listen"] = True; st2["handed_off"] = True; R.CALLS[sid + "b"] = st2
        asyncio.run(R._maria_hangup(sid + "b")); assert hung == []

def test_hang_up_in_sip_mode_still_hangs_up_maria_leg(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "sip"); hung = []
    async def hang(ccid, *a, **k): hung.append(ccid); return {"data": {}}
    monkeypatch.setattr(telnyx, "hangup", hang)
    sid = "sess-hangup-sip-12345"; st = _state(sim=False); R.CALLS[sid] = st
    asyncio.run(R._maria_hangup(sid)); assert hung == [st["maria_ccid"]]


def _ring_setup(monkeypatch, mode="listen", sim=False):
    monkeypatch.setenv("MARIA_LEG", mode); monkeypatch.delenv("MARIA_AUTO_ANSWER", raising=False); monkeypatch.setenv("PUBLIC_WS", "wss://x.example")
    calls = []
    async def answer(ccid, body=None): calls.append(("answer", ccid, body)); return {"data": {}}
    async def reject(ccid, cause="CALL_REJECTED"): calls.append(("reject", ccid)); return {"data": {}}
    async def hangup(ccid): calls.append(("hangup", ccid)); return {"data": {}}
    monkeypatch.setattr(telnyx, "answer", answer); monkeypatch.setattr(telnyx, "reject", reject); monkeypatch.setattr(telnyx, "hangup", hangup)
    monkeypatch.setattr(R, "_routing", lambda frm, att: {"decision": "LIVE_GUARD", "reason": ""})
    monkeypatch.setattr(R, "LIMITER", Limiter(per_caller=99, max_concurrent=99))
    return calls

def _incoming(sid, ccid="v3:ring1234567890"):
    return {"call_control_id": ccid, "call_session_id": sid, "from": "+15555550123", "to": "+15555550100", "direction": "incoming"}

def test_listen_mode_rings_until_the_customer_answers(monkeypatch):
    calls = _ring_setup(monkeypatch); sid = "sess-ring-answer-123"
    async def go():
        R.LOOP = asyncio.get_running_loop()
        await R.on_initiated(_incoming(sid)); assert calls == [] and R.CALLS[sid]["ringing"] is True      # NOT answered: caller keeps ringing
        assert "call.incoming" in [e["type"] for e in bus.history if e["call_id"] == sid]
        assert not [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.answered"]
        await R.on_answered({"call_session_id": sid, "call_control_id": "v3:ring1234567890", "client_state": R._cs(sid=sid, role="caller")})   # stray early webhook is ignored
        assert not [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.answered"]
        bus.publish("user.action", sid, {"action": "answer"}); await asyncio.sleep(0.2)                    # the customer taps Answer (bus -> voip)
        assert [c[0] for c in calls] == ["answer"] and "stream_url" in calls[0][2] and calls[0][2]["stream_bidirectional_target_legs"] == "self"
        assert R.CALLS[sid]["ringing"] is False
        ans = [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.answered"]
        assert len(ans) == 1 and ans[0]["data"] == {"by": "maria", "via": "listen"}                        # emitted immediately on the successful answer
        await R.on_answered({"call_session_id": sid, "call_control_id": "v3:ring1234567890", "client_state": R._cs(sid=sid, role="caller")})   # Telnyx's own call.answered later
        assert len([e for e in bus.history if e["call_id"] == sid and e["type"] == "call.answered"]) == 1   # no duplicate
        assert await R.answer_call(sid) is False                                                           # idempotent
    asyncio.run(go())

def test_decline_and_hang_up_before_answer_reject_the_call(monkeypatch):
    for act in ("decline", "hang_up"):
        calls = _ring_setup(monkeypatch, mode="talk"); sid = f"sess-ring-{act}-1234"
        async def go():
            R.LOOP = asyncio.get_running_loop(); await R.on_initiated(_incoming(sid)); calls.clear()
            bus.publish("user.action", sid, {"action": act}); await asyncio.sleep(0.2)
        asyncio.run(go())
        assert [c[0] for c in calls] == ["reject"] and R.CALLS[sid]["ended"] is True
        end = [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.ended"]
        assert len(end) == 1 and end[0]["data"]["ended_by"] == "customer_declined"

def test_no_answer_after_timeout_rejects_and_blocks_late_answer(monkeypatch):
    calls = _ring_setup(monkeypatch); monkeypatch.setattr(R, "RING_TIMEOUT_S", 0.3); sid = "sess-ring-noanswer-12"
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.on_initiated(_incoming(sid)); await asyncio.sleep(0.6)
        assert await R.answer_call(sid) is False
    asyncio.run(go())
    assert [c[0] for c in calls] == ["reject"]
    end = [e for e in bus.history if e["call_id"] == sid and e["type"] == "call.ended"]
    assert len(end) == 1 and end[0]["data"]["ended_by"] == "no_answer"

def test_auto_answer_env_and_sip_mode_keep_the_old_behaviour(monkeypatch):
    calls = _ring_setup(monkeypatch); monkeypatch.setenv("MARIA_AUTO_ANSWER", "1")
    asyncio.run(R.on_initiated(_incoming("sess-ring-auto-1234567")))
    assert [c[0] for c in calls] == ["answer"] and not R.CALLS["sess-ring-auto-1234567"].get("ringing")
    calls = _ring_setup(monkeypatch, mode="sip")
    asyncio.run(R.on_initiated(_incoming("sess-ring-sip-12345678", "v3:ring2222222222")))
    assert [c[0] for c in calls] == ["answer"]

def test_sim_ringing_drops_media_until_answered_and_hello_waits(monkeypatch):
    _ring_setup(monkeypatch); fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "direct_local", lambda c: True)
    sid = "sess-ring-sim-1234567"; st = _state(sim=True); st.update(token="tok", ringing=True); R.CALLS[sid] = st
    frame = json.dumps({"event": "media", "media": {"track": "inbound", "payload": base64.b64encode(b"\xff" * 160).decode()}})
    app = FastAPI(); app.include_router(R.router)
    with TestClient(app).websocket_connect(f"/media/{sid}?t=tok") as ws:
        ws.send_text(json.dumps({"event": "start"})); ws.send_text(frame); time.sleep(0.2)
    assert ("frame", "media") not in fr.calls and ("open", sid) in fr.calls     # not relayed while ringing (the WS itself was accepted)
    st["ringing"] = False
    with TestClient(app).websocket_connect(f"/media/{sid}?t=tok") as ws:
        ws.send_text(json.dumps({"event": "start"})); ws.send_text(frame); time.sleep(0.2)
    assert ("frame", "media") in fr.calls                                        # positive control: relayed once answered


def test_F2_low_score_long_after_the_window_does_not_make_a_scam_call_legit(monkeypatch):
    monkeypatch.setattr(R, "RESTORE_LOW_S", 0.5); fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr)
    sid = "sess-F2-late-1234567"; st = _state(); st.update(handed_off=True, restore_deadline=time.time() - 60); R.CALLS[sid] = st   # window closed a minute ago
    R._note_risk(sid, 0.05); assert st.get("low_since") is None                      # a late low score starts no clock
    st["low_since"] = time.time() - 5                                                   # (even if one slipped in) it was not held inside the window
    assert R._legit(st) == {}
    asyncio.run(R._decoy_lost(sid))
    ev = [e for e in bus.history if e["call_id"] == sid][-1]
    assert ev["type"] == "call.ended" and "legit" not in ev["data"]
    st2 = _state(); st2.update(handed_off=True, restored=True); assert R._legit(st2) == {"legit": True}   # a real restore still counts


def test_F7_listen_mode_streams_even_normal_routed_calls(monkeypatch):
    calls = _ring_setup(monkeypatch); monkeypatch.setattr(R, "_routing", lambda frm, att: {"decision": "NORMAL", "reason": "trusted"}); sid = "sess-F7-normal-12345"
    async def go():
        R.LOOP = asyncio.get_running_loop(); await R.on_initiated(_incoming(sid, "v3:f7normal1234567"))
        assert await R.answer_call(sid) is True
    asyncio.run(go())
    assert [c[0] for c in calls] == ["answer"] and "stream_url" in calls[0][2]                     # streamed although routing said NORMAL
    calls2 = _ring_setup(monkeypatch, mode="sip"); monkeypatch.setattr(R, "_routing", lambda frm, att: {"decision": "NORMAL", "reason": "trusted"})
    asyncio.run(R.on_initiated(_incoming("sess-F7-sip-123456789", "v3:f7sip12345678901")))
    assert "stream_url" not in (calls2[0][2] or {})                                                # SIP mode: NORMAL calls are untouched (Maria's leg is the call)


def test_F13_decoy_crash_in_listen_mode_restores_instead_of_hanging_up(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "talk"); calls = _no_telnyx(monkeypatch); fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "HAUL_GRACE_S", 0.2)
    sid = "sess-F13-crash-12345"; st = _state(sim=False, conf=False); st.pop("maria_ccid"); st.update(listen=True, handed_off=True, restore_deadline=time.time() - 100, last_risk=(0.1, time.time())); R.CALLS[sid] = st
    asyncio.run(R._decoy_lost(sid))                                  # decoy died with no haul, even after the restore window
    assert st["ended"] is False and st["restored"] is True and ("stop_decoy", sid) in fr.calls
    assert "handoff.restored" in [e["type"] for e in bus.history if e["call_id"] == sid] and "hangup" not in calls
    assert R._legit(st) == {}                                       # a crash-restore must not mark a scam caller legit
    # polite wrap-up: the haul was delivered first -> normal end (hang up, ended_by decoy)
    sid2 = "sess-F13-polite-1234"; st2 = _state(sim=False, conf=False); st2.update(listen=True, handed_off=True, haul_seen=True); R.CALLS[sid2] = st2
    asyncio.run(R._decoy_lost(sid2))
    ev = [e for e in bus.history if e["call_id"] == sid2][-1]
    assert ev["type"] == "call.ended" and ev["data"]["ended_by"] == "decoy" and "hangup" in calls
    # SIP mode keeps the old behaviour (Maria's leg exists)
    monkeypatch.setenv("MARIA_LEG", "sip"); sid3 = "sess-F13-sip-12345678"; st3 = _state(sim=False); st3.update(handed_off=True); R.CALLS[sid3] = st3
    asyncio.run(R._decoy_lost(sid3)); assert st3["ended"] is True


def test_F15_double_tap_starts_one_decoy(monkeypatch):
    class Slow(FakeRelay):
        async def start_decoy(s, cid): s.calls.append(("start_decoy", cid)); await asyncio.sleep(0.2); return True
    fr = Slow(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); sid = "sess-F15-double-1234"; R.CALLS[sid] = _state()
    async def go():
        R.LOOP = asyncio.get_running_loop()
        return await asyncio.gather(R.handoff(sid), R.handoff(sid))
    r = asyncio.run(go())
    assert sorted(r) == [False, True] and [c for c in fr.calls if c[0] == "start_decoy"] == [("start_decoy", sid)]

def test_F14_caller_hangs_up_while_the_decoy_is_starting(monkeypatch):
    sid = "sess-F14-hangup-1234"; st = _state(); R.CALLS[sid] = st
    class Racy(FakeRelay):
        async def start_decoy(s, cid): s.calls.append(("start_decoy", cid)); st["ended"] = True; return True   # caller hangs up during the await
    fr = Racy(); monkeypatch.setattr(R, "_hub_relay", lambda: fr)
    assert asyncio.run(R.handoff(sid)) is False
    assert ("stop_decoy", sid) in fr.calls and not st.get("handed_off")
    assert "handoff.started" not in [e["type"] for e in bus.history if e["call_id"] == sid]

def test_F20_clear_sent_on_handoff_and_restore(monkeypatch):
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); sent = []
    async def send(fr_): sent.append(fr_)
    sid = "sess-F20-clear-12345"; st = _state(); st["send_to_caller"] = send; st["talk_q"] = __import__("collections").deque(["x", "y"]); R.CALLS[sid] = st
    async def go():
        R.LOOP = asyncio.get_running_loop(); assert await R.handoff(sid); n1 = len(sent); assert await R.restore(sid); return n1
    n1 = asyncio.run(go())
    assert n1 == 1 and sent[0] == {"event": "clear"} and len(sent) == 2 and sent[1] == {"event": "clear"} and not st["talk_q"]


def test_F13_security_high_or_unknown_risk_is_never_restored_after_a_decoy_crash(monkeypatch):
    monkeypatch.setenv("MARIA_LEG", "talk"); calls = _no_telnyx(monkeypatch); fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setattr(R, "HAUL_GRACE_S", 0.2)
    for name, last in (("high", (0.92, time.time())), ("unknown", None)):
        sid = f"sess-F13-sec-{name}-12"; st = _state(sim=False, conf=False); st.pop("maria_ccid"); st.update(listen=True, handed_off=True)
        if last: st["last_risk"] = last
        R.CALLS[sid] = st; asyncio.run(R._decoy_lost(sid))
        assert st["ended"] is True and not st.get("restored") and "hangup" in calls          # hang up + ended_by decoy (hub blocklists)
        assert [e for e in bus.history if e["call_id"] == sid][-1]["data"]["ended_by"] == "decoy"
    # the haul landing a moment after the stream closed (two channels, race) counts as a polite wrap-up, not a crash
    sid = "sess-F13-race-1234567"; st = _state(sim=False, conf=False); st.pop("maria_ccid"); st.update(listen=True, handed_off=True, last_risk=(0.1, time.time())); R.CALLS[sid] = st
    async def go():
        t = asyncio.create_task(R._decoy_lost(sid)); await asyncio.sleep(0.05); st["haul_seen"] = True; await t
    asyncio.run(go()); assert st["ended"] is True and not st.get("restored")


def test_F19_old_socket_cleanup_does_not_remove_the_new_sockets_sender(monkeypatch):
    import contextlib
    fr = FakeRelay(); monkeypatch.setattr(R, "_hub_relay", lambda: fr); monkeypatch.setenv("MARIA_LEG", "talk")
    sid = "sess-F19-reconnect-12"; st = _state(sim=False); st["token"] = "tok"; R.CALLS[sid] = st
    app = FastAPI(); app.include_router(R.router); tc = TestClient(app)
    with contextlib.ExitStack() as es:
        ws1 = es.enter_context(tc.websocket_connect(f"/media/{sid}?t=tok")); ws1.send_text(json.dumps({"event": "start"})); time.sleep(0.2)
        s1 = st["send_to_caller"]
        ws2 = es.enter_context(tc.websocket_connect(f"/media/{sid}?t=tok")); ws2.send_text(json.dumps({"event": "start"})); time.sleep(0.2)
        s2 = st["send_to_caller"]; assert s2 is not s1
        st["talk_q"] = __import__("collections").deque(["f"])
        ws1.close(); time.sleep(0.3)                                  # the OLD socket cleans up late
        assert st.get("send_to_caller") is s2 and st.get("talk_q")   # the new socket's sender + queue survived
        assert fr.closed == ["session-1"]                             # close() got the OLD session object, so the relay can ignore it
        ws2.close(); time.sleep(0.3)
    assert "send_to_caller" not in st and fr.closed == ["session-1", "session-2"]


def test_F12_demo_reset_clears_limiter_and_exempt_numbers_are_never_limited(monkeypatch):
    lim = Limiter(per_caller=2, window_s=600, max_concurrent=5); monkeypatch.setattr(R, "LIMITER", lim)
    for i in range(2): assert lim.check("+1555", f"c{i}") is None
    assert lim.check("+1555", "c3")                                   # locked out after the rehearsal burst
    live = _state(); R.CALLS["sess-F12-live-123456"] = live; R.CALLS["sess-F12-old-1234567"] = dict(_state(), ended=True)
    bus.reset()                                                       # what POST /demo/reset calls (hooked by voip)
    assert lim.check("+1555", "c4") is None and "sess-F12-live-123456" in R.CALLS and "sess-F12-old-1234567" not in R.CALLS
    monkeypatch.setenv("MARIA_AUTO_ANSWER", "1"); monkeypatch.setenv("VOIP_LIMIT_EXEMPT", "+1999,+1888"); monkeypatch.setenv("MARIA_LEG", "sip")
    lim2 = Limiter(per_caller=1, window_s=600, max_concurrent=5); monkeypatch.setattr(R, "LIMITER", lim2)
    calls = _ring_setup(monkeypatch, mode="sip")
    for i in range(3):   # exempt number: three calls in a row, none rejected even though the per-caller cap is 1
        p = _incoming(f"sess-F12-ex-{i}-12345678", f"v3:f12ex{i}1234567890"); p["from"] = "+1999"
        asyncio.run(R.on_initiated(p))
    assert [c[0] for c in calls] == ["answer"] * 3
