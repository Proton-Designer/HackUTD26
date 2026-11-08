"""Telnyx telephony for Backfire (P1, 'Simulated carrier network'). Mount on the hub:
    from voip.router import router; mount_router(router)
Paths: POST /telnyx/webhook · WS /media/{call_id}?t=<token> · GET /voip/webrtc-token
call_id == Telnyx call_session_id. Fail open: no exception here may hang up or block a call."""
import asyncio, base64, json, logging, os, re, secrets, time
from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from . import telnyx
from .relay import Relay, make_p2_sink
from .security import Limiter, verify_signature

log = logging.getLogger("voip")
router = APIRouter()
from . import persona as _persona
router.include_router(_persona.router)   # built-in stand-in decoy persona: WS /decoy-standin/{call_id}
def _require_device(request: Request):
    """Credential-minting auth: a paired x-device-token (server.device) or HUB_TOKEN. NO loopback exemption (CORS/DNS-rebinding risk).
    Fail closed if server.device cannot be imported."""
    try:
        from server import device
    except Exception:
        raise HTTPException(503, "device auth unavailable")
    hub = os.environ.get("HUB_TOKEN")
    if hub and secrets.compare_digest(request.headers.get("x-hub-token", ""), hub): return
    if device._valid(request.headers.get("x-device-token")): return
    raise HTTPException(401, "pair this device first (POST /pair)")

ID_RE = re.compile(r"^[A-Za-z0-9_:.=-]{8,200}$")
CALL_CAP_S = int(os.environ.get("VOIP_CALL_CAP_S", "300"))
LIMITER = Limiter(per_caller=int(os.environ.get("VOIP_PER_CALLER", "4")), max_concurrent=int(os.environ.get("VOIP_MAX_CONCURRENT", "5")))
CALLS: dict[str, dict] = {}    # call_id -> state
RELAYS: dict[str, Relay] = {}
MAX_STREAM_FRAMES = 50 * 60 * 10  # 10 min of 20 ms frames

def sim_mode() -> bool: return os.environ.get("SIM_MODE") == "1"
def _maria_leg() -> str: return os.environ.get("MARIA_LEG", "sip").strip().lower()
def talk_mode() -> bool: return _maria_leg() == "talk"
RING_TIMEOUT_S = float(os.environ.get("VOIP_RING_S", "45"))
def ring_mode() -> bool:
    """listen/talk mode behaves like a real phone: inbound calls are NOT answered until the customer's page sends user.action 'answer' (caller hears
    ringing); 'decline' / 'hang_up' before that rejects; RING_TIMEOUT_S without an answer hangs up (no_answer). MARIA_AUTO_ANSWER=1 restores the old
    auto-answer (scripts/tests). Applies to SIM_MODE calls too."""
    return listen_mode() and os.environ.get("MARIA_AUTO_ANSWER", "") != "1"
def listen_mode() -> bool:
    """MARIA_LEG=listen|talk: never dial Maria's SIP leg (no Telnyx dial/conference calls); her page listens (talk: and speaks back via
    WS /talk -> inject_maria). Default 'sip'."""
    return _maria_leg() in ("listen", "talk")
PROXY_HEADERS = ("cf-connecting-ip", "cf-ray", "x-forwarded-for", "x-forwarded-host", "forwarded", "x-real-ip")
def direct_local(conn) -> bool:
    """Same rule as server.device.is_direct_local: loopback peer AND no proxy/tunnel headers (cloudflared connects from 127.0.0.1 but adds them)."""
    c = getattr(conn, "client", None)
    return bool(c and c.host in ("127.0.0.1", "::1")) and not any(h in conn.headers for h in PROXY_HEADERS)

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

ATT_KEYS = ("shaken_stir_attestation", "attestation")   # carrier-populated, exact names only (live location still unverified)

def attestation_of(p: dict) -> str:
    """SHAKEN/STIR level from carrier-populated payload fields only: top level or the `shaken_stir` object, exact keys.
    Never read sip_headers/custom headers (the caller controls those) and no substring or recursive matching.
    Unverified location -> 'none' (fail safe: no A means no trusted-contact bypass). Discovery: key paths are logged on call.initiated."""
    for src in (p, p.get("shaken_stir")):
        if isinstance(src, dict):
            for k in ATT_KEYS:
                v = src.get(k)
                if isinstance(v, str) and v.strip().upper() in ("A", "B", "C"): return v.strip().upper()
    return "none"

def _key_paths(o, pre="", depth=0):
    """Key paths only (never values) for discovery logging; skips caller-controlled header maps' contents."""
    out = []
    if isinstance(o, dict) and depth < 3:
        for k, v in o.items():
            out.append(pre + str(k))
            if isinstance(v, dict) and k not in ("sip_headers", "custom_headers"): out += _key_paths(v, pre + str(k) + ".", depth + 1)
    return out

def _cs(**kw): return base64.b64encode(json.dumps(kw).encode()).decode()
def _cs_load(s):
    try: return json.loads(base64.b64decode(s or ""))
    except Exception: return {}

def maria_sip_uri():
    u = os.environ.get("TELNYX_SIP_USER")
    return f"sip:{u}@sip.telnyx.com" if u else None

for _v in ("TELNYX_CALL_CONTROL_APP_ID", "TELNYX_SIP_USER", "TELNYX_API_KEY"):
    if not os.environ.get(_v): log.warning("voip: %s not set; Maria cannot be dialed / Telnyx commands will fail (fail open)", _v)

def _ops_result(ok, detail=""):
    """Feed eng1's ops.telnyx_result (hub /demo/status telnyx_ok). Never raises; absent outside the hub process."""
    try:
        from server import ops
        ops.telnyx_result(ok, detail)
    except Exception: pass

async def _safe(coro, what, sim=False):
    if sim:
        coro.close(); log.warning("sim: would %s (no Telnyx request sent)", what); return {"data": {}}   # simulated call: skip real Telnyx
    try:
        r = await coro; _ops_result(True); return r
    except Exception as e:
        log.warning("%s failed: %s", what, e); _ops_result(False, str(e)); return None

async def on_initiated(p, base_ws=None, sim=False):
    ccid, sid, frm = p.get("call_control_id"), p.get("call_session_id"), p.get("from", "")
    if not (ccid and sid and ID_RE.match(ccid) and ID_RE.match(sid)): return {}
    if sid in CALLS: return {}   # duplicate/replayed initiated for a known session: never overwrite state (sim or real)
    if _cs_load(p.get("client_state")).get("role") == "maria" or (maria_sip_uri() and p.get("to") and p["to"] == maria_sip_uri().split(":", 1)[1].split("@")[0]):
        return {}   # our own dialed Maria SIP leg also arrives as call.initiated (direction incoming, own session): never treat it as a new scam call
    att = attestation_of(p)
    log.warning("call.initiated payload key paths (no values): %s attestation=%s", sorted(_key_paths(p)), att)
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
    if ring_mode():   # real phone: leave the call ringing; answer/decline come from the customer's page (user.action)
        st = CALLS[sid]; st["ringing"] = True; st["answer_body"] = body
        log.warning("ringing %s: waiting for the customer to answer (%.0f s, MARIA_LEG=%s)", sid[:8], RING_TIMEOUT_S, _maria_leg())
        asyncio.create_task(_ring_timeout(sid))
        return out
    await _answer_now(sid, body, sim)
    return out

async def _answer_now(sid, body, sim):
    ccid = CALLS[sid]["caller_ccid"]
    if await _safe(telnyx.answer(ccid, body), "answer(stream)", sim) is None and "stream_url" in body:
        await _safe(telnyx.answer(ccid, {"client_state": body["client_state"]}), "answer(plain)")  # fail open
    asyncio.create_task(_cap(sid))

async def answer_call(sid):
    """user.action 'answer' while ringing: answer the Telnyx call with the caller stream (as the auto-answer did). Real calls get call.answered from
    Telnyx's webhook; the simulator has none after this point, so emit it here."""
    st = CALLS.get(sid)
    if not st or st["ended"] or not st.get("ringing"): return False
    st["ringing"] = False; st["answered_at"] = time.time(); sim = st.get("sim", False)
    await _answer_now(sid, st.pop("answer_body", {"client_state": _cs(sid=sid, role="caller")}), sim)
    # emit call.answered NOW (once): the hub derives "still ringing" from the bus, so a second answer must see it and get 409. Telnyx's own
    # call.answered webhook (real calls) arrives a moment later and is then a no-op (answer_emitted).
    st["listen"] = True; st["maria_answered"] = True; st["answer_emitted"] = True
    emit("call.answered", sid, {"by": "maria", "via": "talk" if talk_mode() else "listen"})
    log.warning("answered %s on the customer's tap (%.1f s after ringing started)", sid[:8], time.time() - st["t0"])
    return True

async def _end_unanswered(sid, ended_by):
    st = CALLS.get(sid)
    if not st or st["ended"] or not st.get("ringing"): return False
    st["ended"] = True; st["ringing"] = False; LIMITER.release(sid)
    await _safe(telnyx.reject(st["caller_ccid"]), f"reject ({ended_by})", st.get("sim", False))   # unanswered inbound call: reject, caller hears busy/decline
    emit("call.ended", sid, {"ended_by": ended_by, "duration_s": round(time.time() - st["t0"], 1)})
    return True

async def decline_call(sid): return await _end_unanswered(sid, "customer_declined")

async def _ring_timeout(sid):
    await asyncio.sleep(RING_TIMEOUT_S)
    if await _end_unanswered(sid, "no_answer"): log.warning("no answer for %s after %.0f s: call rejected", sid[:8], RING_TIMEOUT_S)

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
    if role == "caller" and st.get("ringing"): return   # the simulator sends call.answered on its own timer; a real call is only answered by answer_call()
    if role == "caller" and st.get("answer_emitted"): return   # already emitted by answer_call()
    if role == "caller" and listen_mode():
        st["listen"] = True; st["maria_answered"] = True   # no conference, no Maria dial: the UI flows as if she answered
        emit("call.answered", sid, {"by": "maria", "via": "talk" if talk_mode() else "listen"})
        log.warning("MARIA_LEG=listen: not dialing Maria for %s (answer + caller stream only)", sid[:8])
    elif role == "caller":
        conf = await _safe(telnyx.create_conference(st["caller_ccid"], f"bf-{sid[:12]}"), "create_conference", sim)
        st["conf_id"] = ((conf or {}).get("data") or {}).get("id")
        frm = os.environ.get("TELNYX_FROM_NUMBER") or os.environ.get("TELNYX_SCAM_LINE") or st["from"]  # UNVERIFIED which 'from' Telnyx accepts for SIP dial
        conn, to = os.environ.get("TELNYX_CALL_CONTROL_APP_ID"), maria_sip_uri()   # POST /calls needs the Call Control App id (live: cred-connection id -> 422 10015)
        if not (conn and to) and not sim:
            log.error("cannot dial Maria: TELNYX_CALL_CONTROL_APP_ID/TELNYX_SIP_USER missing"); return
        r = await _safe(telnyx.dial({"connection_id": conn, "to": to, "from": frm,
                                     "client_state": _cs(sid=sid, role="maria"), "timeout_secs": 40}), "dial maria", sim)
        st["maria_ccid"] = ((r or {}).get("data") or {}).get("call_control_id")
        if sim:
            emit("call.answered", sid, {"by": "maria"}); st["maria_answered"] = True  # simulator has no Maria leg
            asyncio.create_task(_p2_fallback(sid))
    elif role == "maria":
        st["maria_answered"] = True; st["maria_alive"] = True
        if st.get("conf_id"): await _safe(telnyx.join_conference(st["conf_id"], p["call_control_id"], start_conference_on_enter=True), "join maria", sim)
        if not st.get("restored"): emit("call.answered", sid, {"by": "maria"})

async def on_hangup(p):
    sid, st, role = _who(p)
    if not st or st["ended"]: return
    if role == "maria" and p.get("call_control_id") != st.get("maria_ccid"): return   # stale leg (e.g. before a restore re-dial)
    if role == "maria": st["maria_alive"] = False
    if role == "maria" and st.get("handed_off") and not st.get("restored"): return   # Maria put the phone down after handoff: decoy keeps the caller
    if role == "maria" and not st.get("maria_answered"): return  # Maria never picked up: caller stays with line; no call.ended yet
    st["ended"] = True; LIMITER.release(sid)
    other = st.get("maria_ccid") if role == "caller" else st.get("caller_ccid")
    if other: await _safe(telnyx.hangup(other), "hangup other leg", st.get("sim", False))
    await _stop_decoy(sid)
    _publish_demo_haul(sid)   # sim echo stand-in: haul goes out before call.ended
    emit("call.ended", sid, {"ended_by": "caller" if role == "caller" else "maria", "duration_s": round(time.time() - st["t0"], 1), **_legit(st)})
    r = RELAYS.pop(sid, None)
    if r: await r.close()

@router.post("/telnyx/webhook")
async def webhook(req: Request):
    raw = await req.body()
    global LOOP
    LOOP = asyncio.get_running_loop()
    sim = is_sim(None, req.headers)
    if sim and not direct_local(req):
        log.warning("sim webhook refused: SIM_MODE accepts x-sim-call only from a direct loopback client")
        return JSONResponse({"detail": "sim webhooks are loopback-only"}, status_code=403)   # via the tunnel a valid Telnyx signature is required
    hub_token = os.environ.get("HUB_TOKEN")   # simulator traffic must also present the hub token when one is set
    if sim and hub_token and not secrets.compare_digest(req.headers.get("x-hub-token", ""), hub_token): raise HTTPException(401, "bad token")
    if not sim and not verify_signature(raw, req.headers.get("telnyx-signature-ed25519"), req.headers.get("telnyx-timestamp")):
        raise HTTPException(403, "bad signature")
    try:
        ev = json.loads(raw)["data"]; et, p = ev["event_type"], ev["payload"]
        sim = sim or is_sim(p.get("call_control_id"))
        if et == "call.initiated" and not sim and not os.environ.get("TELNYX_PUBLIC_KEY"):
            # unsigned mode: anyone with the tunnel URL could forge call.initiated. Verify the call exists on our account; fail closed.
            try:
                d = (await telnyx.get_call(p.get("call_control_id", ""))).get("data", {})
                if not d.get("is_alive", True): raise telnyx.TelnyxError("call not alive")
            except Exception as e:
                log.warning("unsigned call.initiated rejected: call not verifiable (%s)", e)
                return JSONResponse({"ok": False, "error": "unverified call"}, status_code=403)
        if et != "call.initiated":   # sim and real events may never act on each other's calls
            cs_sid = _cs_load(p.get("client_state")).get("sid") or p.get("call_session_id")
            known = CALLS.get(cs_sid)
            if known is not None and bool(known.get("sim")) != sim: return {"ok": True}
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

# ---- evidence for the "caller track goes digital zero while Maria talks" question: per-second inbound RMS + injected-frame count (numbers only, no audio kept)
def _mu(b):
    b = ~b & 0xFF; t = ((b & 0x0F) << 3) + 0x84; t <<= (b & 0x70) >> 4
    return (0x84 - t) if (b & 0x80) else (t - 0x84)
_MU = [_mu(i) for i in range(256)]

class InStats:
    """Accumulates the caller's inbound frames; emits one compact line per second: rms (16-bit units), % frames that are digital zero, frames in, Maria frames out."""
    def __init__(s, sid): s.sid, s.t0, s.sec, s.last_out = sid, time.time(), 0, 0; s.reset()
    def reset(s): s.n = s.zero = 0; s.ss = 0.0; s.samples = 0
    def add(s, payload_b64, st):
        try: raw = base64.b64decode(payload_b64)
        except Exception: return
        if not raw: return
        v = [_MU[x] for x in raw]; e = sum(x * x for x in v)
        s.n += 1; s.ss += e; s.samples += len(v); s.zero += 1 if not any(v) else 0
        sec = int(time.time() - s.t0)
        if sec > s.sec:
            out = st.get("talk_frames", 0)
            log.warning("inrms %s t=%ds rms=%d zero=%d%% in=%d maria_out=%d", s.sid[:8], s.sec, int((s.ss / max(1, s.samples)) ** 0.5), 100 * s.zero // max(1, s.n), s.n, out - s.last_out)
            s.last_out = out; s.sec = sec; s.reset()

@router.websocket("/media/{call_id}")
async def media(ws: WebSocket, call_id: str, t: str = ""):
    st = CALLS.get(call_id)
    if not (st and st.get("token") and secrets.compare_digest(st["token"], t)):
        await ws.close(code=1008); return
    if st.get("sim") and not direct_local(ws):   # simulated call: its media may only come from a direct loopback client, never via the tunnel
        log.warning("sim media WS refused (not direct loopback)"); await ws.close(code=1008); return
    await ws.accept()
    hub = _hub_relay(); local = None
    sent = {}   # evidence: frames written back to the caller leg (decoy/echo audio), by event type (counts only)
    async def send_to_caller(frame: dict):   # Telnyx media/clear/mark frames back to the caller leg
        await ws.send_text(json.dumps(frame))
        k = str(frame.get("event", "?")) if isinstance(frame, dict) else "?"; sent[k] = sent.get(k, 0) + 1
        if k == "media" and sent[k] == 1: log.warning("first decoy->caller media frame sent on %s", call_id[:8])
    st["send_to_caller"] = send_to_caller
    # the media WS can connect BEFORE the call.answered webhook sets st["listen"] (race seen on call 497ef1d4): decide from the mode, not the flag
    hello = asyncio.create_task(_listen_hello(call_id, send_to_caller)) if (listen_mode() and not talk_mode()) else None   # talk mode: Maria says hello herself
    if listen_mode() and talk_mode(): log.warning("hello skipped for %s: MARIA_LEG=talk (Maria greets herself)", call_id[:8])
    try:
        if hub: await _maybe_await(hub.open(call_id, send_to_caller, on_decoy_lost=_decoy_lost))
        else:
            local = RELAYS[call_id] = Relay()
            s = await make_p2_sink(call_id)
            if s: local.add(s)
    except Exception as e: log.warning("relay open failed (fail open): %s", e)
    n = 0; stats = {}; ins = InStats(call_id) if (listen_mode() and os.environ.get("VOIP_RMS_LOG", "1") != "0") else None   # by mode, not st["listen"]: the media WS can connect before call.answered sets it (same race as the hello)
    try:
        while True:
            raw = await ws.receive_text(); n += 1
            if n > MAX_STREAM_FRAMES: break
            try:   # evidence for LIVE_TEST_PLAN check 3/4: event + track counts, start frame metadata (never payload audio)
                _f = json.loads(raw); _k = _f.get("event", "?") + ((":" + str(_f.get("media", {}).get("track"))) if _f.get("event") == "media" else "")
                stats[_k] = stats.get(_k, 0) + 1
                if ins and not st.get("ringing") and _f.get("event") == "media" and _f.get("media", {}).get("track") in (None, "inbound"): ins.add(_f["media"].get("payload", ""), st)
                if _f.get("event") in ("connected", "start") and stats[_k] == 1: log.warning("media %s: %s", _f["event"], json.dumps({"event": _f.get("event"), "media_format": (_f.get("start") or {}).get("media_format"), "tracks": (_f.get("start") or {}).get("tracks")})[:200])
            except Exception: pass
            if st.get("ringing"): continue   # sim caller streams before the customer answers: nothing is relayed (real Telnyx streams only after answer)
            try:   # caller track only (stream_track=inbound_track); Maria's audio never streamed
                if hub: await _maybe_await(hub.caller_frame(call_id, json.loads(raw)))
                elif local: local.feed(raw)
            except Exception as e: log.warning("relay frame error (ignored): %s", e)
    except (WebSocketDisconnect, RuntimeError): pass
    finally:
        if hello: hello.cancel()
        if st.get("talk_task"): st["talk_task"].cancel(); st.pop("talk_task", None)
        st.pop("talk_q", None); st.pop("send_to_caller", None); log.warning("media WS closed %s frames_in=%s frames_to_caller=%s talk_frames=%s talk_dropped=%s", call_id[:8], stats, sent, st.get("talk_frames", 0), st.get("talk_dropped", 0))
        try:
            if hub: await _maybe_await(hub.close(call_id))
            elif local: await local.close()
        except Exception: pass
        RELAYS.pop(call_id, None)

TALK_MAX_BYTES = 960   # one 20 ms PCMU frame is 160 bytes; tolerate up to 120 ms per message

def talk_enabled(sid) -> bool:
    """For eng1's WS /talk/{call_id}: only a live, known, talk-mode call accepts Maria's uplink."""
    st = CALLS.get(sid)
    return bool(st and st.get("listen") and talk_mode() and not st["ended"])

TALK_FRAME_S = 0.02
TALK_MAX_BACKLOG = 10   # frames (200 ms): older audio is stale, drop the overflow instead of delaying Maria

async def _talk_pacer(sid):
    """One 20 ms-cadence sender per call: the page delivers frames in bursts, Telnyx gets them evenly spaced. Sleeps when idle (sends nothing)."""
    st = CALLS.get(sid); nxt = 0.0
    try:
        while st and not st["ended"]:
            q = st.get("talk_q"); send = st.get("send_to_caller")
            if not q or not send: await asyncio.sleep(0.005); nxt = 0.0; continue
            now = time.monotonic()
            if nxt < now - 0.1: nxt = now   # after idle: restart the clock, do not burst to catch up
            if now < nxt: await asyncio.sleep(nxt - now); continue
            if st.get("handed_off") and not st.get("restored"): q.clear(); continue   # decoy has the line: discard anything still queued
            frame = q.popleft(); nxt += TALK_FRAME_S
            await send({"event": "media", "media": {"payload": frame}})
            n = st["talk_frames"] = st.get("talk_frames", 0) + 1
            if n == 1: log.warning("talk: first Maria->caller frame on %s", sid[:8])
    except asyncio.CancelledError: raise
    except Exception as e: log.warning("talk pacer stopped (%s)", type(e).__name__)

async def inject_maria(sid, payload_b64: str) -> bool:
    """MARIA_LEG=talk: queue PCMU 8 kHz frame(s) of MARIA's page microphone for the caller's bidirectional stream (same path as decoy/hello audio;
    target_legs=self); a per-call pacer sends one 160-byte frame every 20 ms, never more than 200 ms behind (overflow dropped, counted in talk_dropped).
    Returns False = dropped: not a talk call, a decoy is active (handed_off and not restored: muted), stream not ready, bad payload, or backlog full.
    Maria's audio goes ONLY to the caller leg: never to the relay/P2/recordings. Silence from Maria = nothing is sent."""
    try:
        st = CALLS.get(sid)
        if not talk_enabled(sid): return False
        if st.get("handed_off") and not st.get("restored"):
            st["talk_dropped"] = st.get("talk_dropped", 0) + 1; return False   # decoy owns the caller's ears
        if not st.get("send_to_caller"): st["talk_dropped"] = st.get("talk_dropped", 0) + 1; return False   # stream not up yet: drop, don't buffer
        if not isinstance(payload_b64, str) or len(payload_b64) > 4 * TALK_MAX_BYTES // 3 + 8: return False
        raw = base64.b64decode(payload_b64, validate=True)   # reject garbage
        if not raw or len(raw) % 160: return False
        q = st.setdefault("talk_q", __import__("collections").deque())
        ok = True
        for i in range(0, len(raw), 160):
            if len(q) >= TALK_MAX_BACKLOG: st["talk_dropped"] = st.get("talk_dropped", 0) + 1; ok = False; continue
            q.append(base64.b64encode(raw[i:i + 160]).decode())
        if not st.get("talk_task") or st["talk_task"].done(): st["talk_task"] = asyncio.create_task(_talk_pacer(sid))
        return ok
    except Exception as e:
        log.warning("inject_maria dropped (%s)", type(e).__name__); return False

async def _listen_hello(sid, send):
    """MARIA_LEG=listen: play the pre-recorded 'Hello? ... Yes, this is Maria.' (SIMULATED synthetic voice) to the caller once, then silence.
    ALWAYS plays the cached file instantly; a stale cache (voice/text changed) is regenerated in the background for the NEXT call only.
    Every outcome logs one line (sent / skipped + reason). Fail open: any error = silence."""
    try:
        st = CALLS.get(sid); loop = asyncio.get_running_loop()
        for _ in range(int(RING_TIMEOUT_S * 5) + 5):   # sim: the stream is up while the call still rings; greet only after the customer answers
            if not (st and st.get("ringing")): break
            await asyncio.sleep(0.2)
        f = _persona.cached_hello()
        if f is None:   # nothing cached yet: one blocking attempt (bounded), else silent
            f = await asyncio.wait_for(loop.run_in_executor(None, _persona.generate_hello), 35)
        else:
            loop.run_in_executor(None, _persona.generate_hello)   # refresh in the background if the key is stale (no-op when current)
        if not f: log.warning("hello skipped for %s: no audio (nothing cached; Magpie/say unavailable)", sid[:8]); return
        await asyncio.sleep(0.4)
        data = f.read_bytes()
        for k in range(0, len(data), _persona.FRAME_BYTES):
            if not st or st["ended"] or st.get("handed_off"):
                log.warning("hello skipped/stopped for %s: call %s", sid[:8], "ended" if (not st or st["ended"]) else "handed off to the decoy"); return   # the decoy owns the caller's ears once it starts
            await send({"event": "media", "media": {"payload": base64.b64encode(data[k:k + _persona.FRAME_BYTES]).decode()}})
            await asyncio.sleep(0.02)
        log.warning("hello sent for %s (%.1f s from %s)", sid[:8], len(data) / 8000, f.name)
    except asyncio.CancelledError:
        log.warning("hello cancelled for %s (media stream closed first)", sid[:8]); raise
    except Exception as e:
        log.warning("hello skipped for %s: %s %s", sid[:8], type(e).__name__, e)

async def _maybe_await(x):
    if asyncio.iscoroutine(x) or isinstance(x, asyncio.Future): return await x
    return x

@router.get("/voip/webrtc-token", dependencies=[Depends(_require_device)])
async def webrtc_token(req: Request):
    """JWT when a telephony credential is configured (502 if minting fails: no silent downgrade).
    TRIAL-ACCOUNT FALLBACK ONLY when no credential id exists: SIP login/password, and only to a paired device (never HUB_TOKEN)."""
    cred = os.environ.get("TELNYX_TELEPHONY_CREDENTIAL_ID")
    if cred:
        try: return {"token": (await telnyx.webrtc_token(cred)).strip()}
        except Exception as e:
            log.warning("webrtc token failed: %s", e); raise HTTPException(502, "token unavailable")
    u, pw = os.environ.get("TELNYX_SIP_USER"), os.environ.get("TELNYX_SIP_PASSWORD")
    from server import device
    if u and pw and device._valid(req.headers.get("x-device-token")):
        log.warning("webrtc-token: serving SIP login fallback (trial account) to a paired device")
        return {"login": u, "password": pw}
    raise HTTPException(502, "token unavailable")


# ---------------- TASK-008: handoff (Scammer Get Scammed) ----------------
RESTORE_WINDOW_S = int(os.environ.get("VOIP_RESTORE_S", "30"))
RESTORE_LOW_S = float(os.environ.get("RESTORE_LOW_S", "30"))   # demo: 10
RESTORE_BELOW = 0.50   # risk s below this = "looks legitimate"
LAST_RISK_MAX_AGE_S = float(os.environ.get("RESTORE_LAST_MAX_AGE_S", "30"))   # a last score older than this does not start the low clock at handoff
LOOP = None   # event loop, captured from the webhook so sync bus observers can schedule work

async def _stop_decoy(sid):
    hub = _hub_relay()
    if hub:
        try: await _maybe_await(hub.stop_decoy(sid))
        except Exception: log.exception("stop_decoy failed")

async def handoff(sid):
    """Decoy first (no audible gap), then take Maria out of the conference. Her leg is kept (not hung up) for the restore window.
    Fail open: if the decoy cannot start, Maria stays on the call."""
    st = CALLS.get(sid); hub = _hub_relay()
    if not st or st["ended"] or st.get("handed_off") or not hub: return False
    sim = st.get("sim", False)
    if not await _maybe_await(hub.start_decoy(sid)):
        log.warning("handoff aborted for %s: decoy not available (Maria stays)", sid); return False
    st["handed_off"] = True
    lr = st.get("last_risk")   # restore speed-up: the last known score is low (and not stale) -> the low clock starts NOW, no waiting for a fresh update
    if lr and lr[0] < RESTORE_BELOW and time.time() - lr[1] <= LAST_RISK_MAX_AGE_S:
        st["low_since"] = time.time(); log.warning("handoff %s: last risk %.2f (%.0fs old) is low, restore clock started now", sid[:8], lr[0], time.time() - lr[1])
    if st.get("conf_id") and st.get("maria_ccid"):
        await _safe(telnyx.leave_conference(st["conf_id"], st["maria_ccid"]), "leave maria", sim)
    deadline = time.time() + RESTORE_WINDOW_S; st["restore_deadline"] = deadline
    emit("handoff.started", sid, {"restore_deadline": deadline})
    if sim and not os.environ.get("P3_DECOY_URL"): asyncio.create_task(_demo_haul_later(sid))   # echo stand-in decoy extracts nothing: supply the demo haul
    asyncio.create_task(_restore_expiry(sid, deadline))
    asyncio.create_task(_low_watch(sid, deadline))
    return True

DEMO_HAUL_DELAY_S = float(os.environ.get("DEMO_HAUL_DELAY_S", "8"))

# ---- SIM_MODE only: demo resilience when P2 is down. Feed the known script text (the sentences scripts/make_scam_wav.sh voiced into
# logs/sim_scam.wav, timed across the WAV's length) into server/fallback_detect so the hub itself emits transcript.caller + risk.update
# (engine "fallback") + alert.fired. Stops the moment a real P2 event arrives. Never runs for real (non-sim) calls.
P2_WAIT_S = float(os.environ.get("PHONEFREE_P2_WAIT_S", "6"))
def _script_timeline():
    """[(offset_s, sentence)] for the caller WAV. Default = the IRS card lines from voip/test_call.card_text (the SAME source that voiced
    logs/sim_scam.wav via `test_call.py --script irs --wav-out`), each line followed by test_call.PAUSE_S of silence: speech time is split by
    character share of (WAV duration - pauses). DEMO_SCRIPT_TEXT overrides (sentences spread by character share). Fail open to no lines."""
    dur = None
    try:
        import pathlib, wave
        w = pathlib.Path(os.environ.get("DEMO_CALLER_WAV") or (pathlib.Path(os.environ.get("LOGDIR") or "logs") / "sim_scam.wav"))
        with wave.open(str(w)) as f: dur = f.getnframes() / f.getframerate()
    except Exception:
        pass
    pause = 0.0
    txt = os.environ.get("DEMO_SCRIPT_TEXT")
    if txt:
        sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+", txt) if x.strip()]
    else:
        try:
            from . import test_call as tc
            sents, pause = tc.card_text(os.environ.get("PHONEFREE_SCRIPT", "irs")), float(tc.PAUSE_S)
        except (Exception, SystemExit) as e:
            log.warning("sim fallback: cannot load card lines (%s)", e); return []
    total = sum(len(x) for x in sents) or 1
    speech = max(1.0, (dur if dur else total / 14.0 + pause * len(sents)) - pause * len(sents))
    out, t = [], 0.0
    for x in sents:
        out.append((t, x)); t += speech * len(x) / total + pause
    return out

async def _p2_fallback(sid):
    """Fail open: any error here only means no fallback alert."""
    try:
        st = CALLS.get(sid)
        if not (st and st.get("sim") and sim_mode()) or os.environ.get("PHONEFREE_FALLBACK", "1") == "0": return
        t0 = time.time()
        while time.time() - t0 < P2_WAIT_S:
            await asyncio.sleep(0.25)
            if st["ended"] or st.get("p2_seen"): return
        if st["ended"] or st.get("p2_seen"): return
        os.environ.setdefault("FALLBACK_DETECT", "1")   # SIM_MODE only; fallback_detect is off by default
        from server import fallback_detect as fd
        log.warning("sim: no P2 event %.0fs after answer for %s -> script-text fallback detector", P2_WAIT_S, sid[:8])
        for off, line in _script_timeline():
            while time.time() - t0 < off:
                await asyncio.sleep(0.2)
                if st["ended"] or st.get("p2_seen"): return
            if st["ended"] or st.get("p2_seen"): return
            await fd.ingest(sid, line, True, "inbound")
    except Exception:
        log.exception("sim p2 fallback failed (fail open)")

def _publish_demo_haul(sid):
    """SIM_MODE + no P3_DECOY_URL only (echo stand-in): publish P3's artifacts.extracted from intel's demo config, once per call, never after a restore.
    Fail open: intel missing/failing never affects the call."""
    st = CALLS.get(sid)
    if not st or not st.get("sim") or st.get("haul_sent") or st.get("restored") or not st.get("handed_off") or os.environ.get("P3_DECOY_URL") or _legit(st): return
    st["haul_sent"] = True
    try:
        from intel import demo_config
        emit("artifacts.extracted", sid, {"artifacts": demo_config.judge_haul(), "source": "demo_stand_in"})
        log.warning("sim: published demo_stand_in artifacts.extracted for %s", sid[:8])
    except Exception as e:
        log.warning("demo haul skipped (fail open): %s", e)

async def _demo_haul_later(sid):
    end = time.time() + DEMO_HAUL_DELAY_S
    while time.time() < end:
        await asyncio.sleep(0.5)
        st = CALLS.get(sid)
        if not st or st["ended"] or st.get("restored"): return
    _publish_demo_haul(sid)

async def _restore_expiry(sid, deadline):
    await asyncio.sleep(max(0, deadline - time.time()))
    st = CALLS.get(sid)
    if st and st.get("handed_off") and not st.get("restored") and st.get("maria_ccid"):
        await _safe(telnyx.hangup(st["maria_ccid"]), "hangup maria after restore window", st.get("sim", False))

def _legit(st) -> dict:
    """Additive call.ended flag: after a handoff, the caller looked legitimate (risk low for RESTORE_LOW_S) -> hub must NOT blocklist."""
    ls = st.get("low_since")
    return {"legit": True} if st.get("handed_off") and ls and time.time() - ls >= RESTORE_LOW_S else {}

def _note_risk(sid, score):
    """Runs on the loop. Remembers the last real (non-fallback) risk score at all times; after handoff it tracks continuous low risk."""
    st = CALLS.get(sid)
    if not st: return
    st["last_risk"] = (score, time.time())
    if not st.get("handed_off") or st.get("restored"): return
    if score < RESTORE_BELOW:
        if st.get("low_since") is None: st["low_since"] = time.time()
    else:
        st["low_since"] = None

async def _low_watch(sid, deadline):
    """Code, not an LLM: while the restore window is open, low risk held for RESTORE_LOW_S -> restore Maria."""
    try:
        while time.time() < deadline:
            await asyncio.sleep(0.5)
            st = CALLS.get(sid)
            if not st or st["ended"] or st.get("restored"): return
            ls = st.get("low_since")
            if ls and time.time() - ls >= RESTORE_LOW_S:
                await restore(sid); return
    except Exception:
        log.exception("low_watch failed")

async def restore(sid):
    """Bring Maria back before the deadline: stop decoy, rejoin her leg (re-dial her SIP if it was hung up), emit handoff.restored."""
    st = CALLS.get(sid)
    if not st or st["ended"] or not st.get("handed_off") or st.get("restored") or time.time() > st.get("restore_deadline", 0): return False
    sim = st.get("sim", False)
    st["restored"] = True
    await _stop_decoy(sid)
    if st.get("listen"): pass   # MARIA_LEG=listen: nothing to rejoin, stopping the decoy is the restore
    elif st.get("maria_alive", True) and st.get("maria_ccid"):
        if st.get("conf_id"): await _safe(telnyx.join_conference(st["conf_id"], st["maria_ccid"]), "rejoin maria", sim)
    else:   # her leg is gone: ring her again; on_answered(role=maria) joins her to the conference
        conn, to = os.environ.get("TELNYX_CALL_CONTROL_APP_ID"), maria_sip_uri()   # POST /calls needs the Call Control App id (live: cred-connection id -> 422 10015)
        if (conn and to) or sim:
            frm = os.environ.get("TELNYX_FROM_NUMBER") or os.environ.get("TELNYX_SCAM_LINE") or st["from"]
            r = await _safe(telnyx.dial({"connection_id": conn, "to": to, "from": frm, "client_state": _cs(sid=sid, role="maria"), "timeout_secs": 40}), "re-dial maria", sim)
            st["maria_ccid"] = ((r or {}).get("data") or {}).get("call_control_id") or st.get("maria_ccid")
    emit("handoff.restored", sid, {"restore_deadline": st["restore_deadline"]})
    return True

async def _decoy_lost(sid):
    """P3 closed/crashed: the decoy session is over. End the caller's call (ended_by decoy) so the hub blocklists the number."""
    st = CALLS.get(sid)
    if not st or st["ended"] or st.get("restored"): return
    st["ended"] = True; LIMITER.release(sid)
    sim = st.get("sim", False)
    for k in ("caller_ccid", "maria_ccid"):
        if st.get(k): await _safe(telnyx.hangup(st[k]), "hangup after decoy end", sim)
    _publish_demo_haul(sid)
    emit("call.ended", sid, {"ended_by": "decoy", "duration_s": round(time.time() - st["t0"], 1), **_legit(st)})

# ---- per-call journal for scripts/call_report: logs/calls/<sid8>.jsonl, one line per bus event with its timestamp (allowlisted scalar fields only:
# no transcript text, no audio, no secrets). Fail open.
_J_KEYS = ("s", "band", "engine", "level", "action", "decision", "reason", "ended_by", "duration_s", "legit", "restore_deadline", "by", "via",
           "scam_type", "stage", "speaker", "latency_ms", "source", "ok", "kind", "status", "route_ms", "alert_ms", "handoff_ms")
def _journal(sid, ev):
    try:
        import pathlib
        d = pathlib.Path(os.environ.get("LOGDIR") or "logs") / "calls"; d.mkdir(parents=True, exist_ok=True)
        data = ev.get("data") or {}
        row = {"ts": round(ev.get("ts") or time.time(), 3), "type": ev.get("type"), **{k: data[k] for k in _J_KEYS if isinstance(data.get(k), (str, int, float, bool))}}
        if isinstance(data.get("artifacts"), list): row["n_artifacts"] = len(data["artifacts"])
        if ev.get("type") == "transcript.caller": row["chars"] = len(str(data.get("text", "")))
        with open(d / f"{sid[:8]}.jsonl", "a") as f: f.write(json.dumps(row) + "\n")
    except Exception:
        pass

class _TsFilter(logging.Filter):
    """Prefix every voip.router log line with [HH:MM:SS] (the hub's own log has no clock); scripts/call_report reads it."""
    def filter(self, record):
        if not getattr(record, "_ts", False):
            record.msg = "[%s] %s" % (time.strftime("%H:%M:%S"), record.msg); record._ts = True
        return True
log.addFilter(_TsFilter())

def _on_bus(ev):
    """Bus observer (sync, any thread): user.action and risk.update drive the Telnyx side; work is scheduled on the captured loop."""
    try:
        if LOOP is None or ev["call_id"] not in CALLS: return
        t, d, sid = ev["type"], ev["data"], ev["call_id"]
        _journal(sid, ev)
        if (t == "risk.update" and d.get("engine") != "fallback") or (t == "transcript.caller" and not str(d.get("utterance_id", "")).startswith("fb_")):
            CALLS[sid]["p2_seen"] = True   # a real P2 event: the sim fallback detector stops
        if t == "user.action":
            if d.get("action") == "answer": asyncio.run_coroutine_threadsafe(answer_call(sid), LOOP)
            elif d.get("action") == "decline": asyncio.run_coroutine_threadsafe(decline_call(sid), LOOP)
            elif d.get("action") == "scammer_get_scammed": asyncio.run_coroutine_threadsafe(handoff(sid), LOOP)
            elif d.get("action") == "hang_up": asyncio.run_coroutine_threadsafe(_maria_hangup(sid), LOOP)
        elif t == "risk.update" and isinstance(d.get("s"), (int, float)) and d.get("engine") != "fallback":   # fallback scores never drive restore/legit
            LOOP.call_soon_threadsafe(_note_risk, sid, float(d["s"]))
    except Exception:
        log.exception("voip bus observer failed")

async def _maria_hangup(sid):
    """user.action hang_up: the customer ends the call. SIP mode: hang up Maria's leg (her WebRTC client normally does it itself). listen/talk mode
    has NO Maria leg, so hang up the CALLER leg instead (bug seen on call 0afc3446: tap at +6.6 s, caller stayed connected 100 s)."""
    st = CALLS.get(sid)
    if not st or st["ended"] or st.get("handed_off"): return
    if st.get("ringing"): await decline_call(sid); return   # hang_up before answering = decline
    sim = st.get("sim", False)
    if (st.get("listen") or listen_mode()) and not st.get("maria_ccid"):
        if st.get("caller_ccid"):
            st["customer_hangup"] = True
            log.warning("hang_up in %s mode for %s: hanging up the caller leg (no Maria leg)", _maria_leg(), sid[:8])
            await _safe(telnyx.hangup(st["caller_ccid"]), "hangup caller (customer hang_up, listen/talk)", sim)
    elif st.get("maria_ccid"):   # her WebRTC client normally hangs up itself; belt and braces
        await _safe(telnyx.hangup(st["maria_ccid"]), "maria hang_up", sim)

try:
    from server import bus as _b
    if not any(getattr(f, "__name__", "") == "_on_bus" for f in _b._observers): _b.add_observer(_on_bus)
except Exception:
    log.warning("voip: bus observer not registered (hub bus unavailable)")
