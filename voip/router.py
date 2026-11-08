"""Telnyx telephony for Backfire (P1, 'Simulated carrier network'). Mount on the hub:
    from voip.router import router; mount_router(router)
Paths: POST /telnyx/webhook · WS /media/{call_id}?t=<token> · GET /voip/webrtc-token
call_id == Telnyx call_session_id. Fail open: no exception here may hang up or block a call."""
import asyncio, base64, json, logging, os, re, secrets, time
from fastapi import APIRouter, HTTPException, Request, WebSocket, WebSocketDisconnect
from . import telnyx
from .relay import Relay, make_p2_sink
from .security import Limiter, verify_signature

log = logging.getLogger("voip")
router = APIRouter()
ID_RE = re.compile(r"^[A-Za-z0-9_:.=-]{8,200}$")
CALL_CAP_S = int(os.environ.get("VOIP_CALL_CAP_S", "300"))
LIMITER = Limiter(per_caller=int(os.environ.get("VOIP_PER_CALLER", "4")), max_concurrent=int(os.environ.get("VOIP_MAX_CONCURRENT", "5")))
CALLS: dict[str, dict] = {}    # call_id -> state
RELAYS: dict[str, Relay] = {}
MAX_STREAM_FRAMES = 50 * 60 * 10  # 10 min of 20 ms frames

def sim_mode() -> bool: return os.environ.get("SIM_MODE") == "1"
def is_sim(ccid, headers=None) -> bool:
    """SIM_MODE only: simulator calls (ccid 'v3:sim_*' or x-sim-call header) never hit the real Telnyx API."""
    return sim_mode() and (str(ccid or "").startswith("v3:sim_") or bool(headers and headers.get("x-sim-call")))

def _bus():
    from server import bus  # hub in-process event bus
    return bus
def emit(type_, cid, data=None):
    try: _bus().publish(type_, cid, data or {})
    except Exception: log.exception("emit %s failed", type_)

def _routing(frm, att):
    try:
        from server import routing
        return routing.decide(frm, att)
    except Exception:
        log.exception("routing failed; fail open"); return {"decision": "NORMAL", "reason": "Routing error, fail open"}

def attestation_of(p: dict) -> str:
    """Best-effort SHAKEN/STIR read. UNVERIFIED field names (see API_EVIDENCE.md) -> 'none' when absent."""
    for src in (p, p.get("shaken_stir") or {}, p.get("sip_headers") or {}):
        v = src.get("shaken_stir_attestation") or src.get("attestation") if isinstance(src, dict) else None
        if isinstance(v, str) and v.strip().upper()[:1] in ("A", "B", "C"): return v.strip().upper()[:1]
    return "none"

def _cs(**kw): return base64.b64encode(json.dumps(kw).encode()).decode()
def _cs_load(s):
    try: return json.loads(base64.b64decode(s or ""))
    except Exception: return {}

def maria_sip_uri(): return f"sip:{os.environ['TELNYX_SIP_USER']}@sip.telnyx.com"

async def _safe(coro, what, sim=False):
    if sim:
        coro.close(); return {"data": {}}   # simulated call: skip real Telnyx
    try: return await coro
    except Exception as e:
        log.warning("%s failed: %s", what, e); return None

async def on_initiated(p, base_ws=None, sim=False):
    ccid, sid, frm = p.get("call_control_id"), p.get("call_session_id"), p.get("from", "")
    if not (ccid and sid and ID_RE.match(ccid) and ID_RE.match(sid)): return {}
    att = attestation_of(p)
    emit("call.incoming", sid, {"from": frm, "to": p.get("to", ""), "attestation": att, "scam_id_score": 0.8 if att in ("C", "none") else 0.1})
    d = _routing(frm, att)
    reason = LIMITER.check(frm, sid) if d["decision"] != "BLOCKED_BACKFIRE" else None
    if reason: d = {"decision": "BLOCKED_BACKFIRE", "reason": reason}
    emit("call.routed", sid, {"decision": d["decision"], "reason": d["reason"]})
    if d["decision"] == "BLOCKED_BACKFIRE":
        await _safe(telnyx.reject(ccid), "reject", sim); return {}   # pre-ring: Maria is never dialed
    CALLS[sid] = {"caller_ccid": ccid, "from": frm, "decision": d["decision"], "t0": time.time(), "ended": False, "sim": sim}
    body = {"client_state": _cs(sid=sid, role="caller")}
    out = {}
    ws_base = os.environ.get("PUBLIC_WS") or (base_ws if sim else None)
    if d["decision"] == "LIVE_GUARD" and ws_base:
        tok = secrets.token_urlsafe(16); CALLS[sid]["token"] = tok
        body.update(stream_url=f"{ws_base}/media/{sid}?t={tok}", stream_track="inbound_track", stream_codec="PCMU",
                    stream_bidirectional_mode="rtp", stream_bidirectional_codec="PCMU",
                    stream_bidirectional_target_legs=os.environ.get("TARGET_LEGS", "self"))
    if sim and "stream_url" in body: out["stream_url"] = body["stream_url"]   # SIM_MODE: hand the tokenized URL to the simulator
    if await _safe(telnyx.answer(ccid, body), "answer(stream)", sim) is None and "stream_url" in body:
        await _safe(telnyx.answer(ccid, {"client_state": body["client_state"]}), "answer(plain)")  # fail open
    asyncio.create_task(_cap(sid))
    return out

async def _cap(sid):
    await asyncio.sleep(CALL_CAP_S)
    st = CALLS.get(sid)
    if st and not st["ended"]:
        log.info("call cap hit %s", sid)
        for k in ("maria_ccid", "caller_ccid"):
            if st.get(k): await _safe(telnyx.hangup(st[k]), "cap hangup", st.get("sim", False))

def _who(p):
    cs = _cs_load(p.get("client_state")); sid = cs.get("sid") or p.get("call_session_id"); st = CALLS.get(sid)
    role = cs.get("role") or ("caller" if st and p.get("call_control_id") == st["caller_ccid"] else "maria")
    return sid, st, role

async def on_answered(p):
    sid, st, role = _who(p)
    if not st: return
    sim = st.get("sim", False)
    if role == "caller":
        conf = await _safe(telnyx.create_conference(st["caller_ccid"], f"bf-{sid[:12]}"), "create_conference", sim)
        st["conf_id"] = ((conf or {}).get("data") or {}).get("id")
        frm = os.environ.get("TELNYX_FROM_NUMBER") or st["from"]  # UNVERIFIED which 'from' Telnyx accepts for SIP dial
        r = await _safe(telnyx.dial({"connection_id": os.environ["TELNYX_CRED_CONNECTION_ID"], "to": maria_sip_uri(), "from": frm,
                                     "client_state": _cs(sid=sid, role="maria"), "timeout_secs": 40}), "dial maria", sim)
        st["maria_ccid"] = ((r or {}).get("data") or {}).get("call_control_id")
        if sim: emit("call.answered", sid, {"by": "maria"}); st["maria_answered"] = True  # simulator has no Maria leg
    elif role == "maria":
        st["maria_answered"] = True
        if st.get("conf_id"): await _safe(telnyx.join_conference(st["conf_id"], p["call_control_id"], start_conference_on_enter=True), "join maria", sim)
        emit("call.answered", sid, {"by": "maria"})

async def on_hangup(p):
    sid, st, role = _who(p)
    if not st or st["ended"]: return
    if role == "maria" and not st.get("maria_answered"): return  # Maria never picked up: caller stays with line; no call.ended yet
    st["ended"] = True; LIMITER.release(sid)
    other = st.get("maria_ccid") if role == "caller" else st.get("caller_ccid")
    if other: await _safe(telnyx.hangup(other), "hangup other leg", st.get("sim", False))
    emit("call.ended", sid, {"ended_by": "caller" if role == "caller" else "maria", "duration_s": round(time.time() - st["t0"], 1)})
    r = RELAYS.pop(sid, None)
    if r: await r.close()

@router.post("/telnyx/webhook")
async def webhook(req: Request):
    raw = await req.body()
    sim = is_sim(None, req.headers)
    if not sim and not verify_signature(raw, req.headers.get("telnyx-signature-ed25519"), req.headers.get("telnyx-timestamp")):
        raise HTTPException(403, "bad signature")
    try:
        ev = json.loads(raw)["data"]; et, p = ev["event_type"], ev["payload"]
        sim = sim or is_sim(p.get("call_control_id"))
        if et == "call.initiated" and p.get("direction") == "incoming":
            return {"ok": True, **(await on_initiated(p, base_ws=str(req.base_url).replace("http", "ws", 1).rstrip("/"), sim=sim))}
        elif et == "call.answered": await on_answered(p)
        elif et == "call.hangup": await on_hangup(p)
    except Exception:
        log.exception("webhook handler error (ignored, fail open)")
    return {"ok": True}

def _hub_relay():
    """eng1's server/relay.py (TASK-013) when present: open/caller_frame/start_decoy/stop_decoy/close. Else voip's local fan-out (P2 only)."""
    try:
        from server import relay as r
        return r if hasattr(r, "caller_frame") else None
    except Exception:
        return None

@router.websocket("/media/{call_id}")
async def media(ws: WebSocket, call_id: str, t: str = ""):
    st = CALLS.get(call_id)
    if not (st and st.get("token") and secrets.compare_digest(st["token"], t)):
        await ws.close(code=1008); return
    await ws.accept()
    hub = _hub_relay(); local = None
    async def send_to_caller(frame: dict): await ws.send_text(json.dumps(frame))   # Telnyx media/clear/mark frames back to the caller leg
    st["send_to_caller"] = send_to_caller
    try:
        if hub: await _maybe_await(hub.open(call_id, send_to_caller))
        else:
            local = RELAYS[call_id] = Relay()
            s = await make_p2_sink(call_id)
            if s: local.add(s)
    except Exception as e: log.warning("relay open failed (fail open): %s", e)
    n = 0
    try:
        while True:
            raw = await ws.receive_text(); n += 1
            if n > MAX_STREAM_FRAMES: break
            try:   # caller track only (stream_track=inbound_track); Maria's audio never streamed
                if hub: await _maybe_await(hub.caller_frame(call_id, json.loads(raw)))
                elif local: local.feed(raw)
            except Exception as e: log.warning("relay frame error (ignored): %s", e)
    except (WebSocketDisconnect, RuntimeError): pass
    finally:
        st.pop("send_to_caller", None)
        try:
            if hub: await _maybe_await(hub.close(call_id))
            elif local: await local.close()
        except Exception: pass
        RELAYS.pop(call_id, None)

async def _maybe_await(x):
    if asyncio.iscoroutine(x) or isinstance(x, asyncio.Future): return await x
    return x

@router.get("/voip/webrtc-token")
async def webrtc_token(req: Request):
    hub_token = os.environ.get("HUB_TOKEN")
    if hub_token and req.headers.get("x-hub-token") != hub_token: raise HTTPException(401, "bad or missing token")
    try: tok = await telnyx.webrtc_token(os.environ["TELNYX_TELEPHONY_CREDENTIAL_ID"])
    except Exception as e:
        log.warning("webrtc token failed: %s", e); raise HTTPException(502, "token unavailable")
    return {"token": tok.strip()}
