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
    monkeypatch.setattr(R._persona, "generate_hello", lambda force=False: f)
    got = []
    async def send(fr): got.append(fr)
    sid = "sess-hello-1234567"; R.CALLS[sid] = _state(sim=False)
    asyncio.run(R._listen_hello(sid, send))
    assert len(got) == 5 and all(g["event"] == "media" for g in got)
    got.clear(); R.CALLS[sid]["handed_off"] = True
    asyncio.run(R._listen_hello(sid, send)); assert got == []     # decoy owns the line once handed off
    monkeypatch.setattr(R._persona, "generate_hello", lambda force=False: None)
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
