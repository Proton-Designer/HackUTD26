"""Android VoIP alternative to Telnyx (P3), mounted in the hub process next to voip/ (P1).

Roles (see android_voip/BACKFIRE.md):
  signaling server (server/server.js) = the "carrier": asks /android/route before ringing Maria, reports answer/hangup,
      and on user.action=scammer_get_scammed moves the scammer's call to the `decoy` peer.
  Maria's phone   -> WS /android/events/{call_id}  (her call's bus events: alert.fired, handoff.started, ...)
                  -> WS /android/media/{call_id}   (binary PCM16 LE 8 kHz mono: the CALLER's audio only, never hers)
  decoy peer      -> WS /android/decoy/{call_id}   (the scammer's audio after handoff; gets the decoy voice back)

Audio from both sources becomes Telnyx-format frames and goes through server/relay.py, so P2 (/stt) and P3 (/decoy)
see exactly what they would on the Telnyx path. Fail open everywhere: nothing here can end or block a call.

Auth: carrier + decoy peer = direct localhost or x-hub-token/?t= HUB_TOKEN. Phone = device token from POST /pair (?d=).
"""
import asyncio, base64, json, logging, os, secrets, time
from fastapi import APIRouter, Body, HTTPException, Request, WebSocket, WebSocketDisconnect

from . import ulaw

log = logging.getLogger("android")
router = APIRouter()
CALLS: dict = {}       # call_id -> {from, to, decision, t0, handed_off, ended}
OPENED: set = set()    # call_ids with an open server/relay.py session
SINKS: dict = {}       # call_id -> async fn(frame) that plays decoy audio to the scammer (the decoy peer's WS)
FRAME_BYTES = 320      # 20 ms of PCM16 at 8 kHz
DECISIONS = ("NORMAL", "BLOCKED_BACKFIRE", "LIVE_GUARD")


def _bus():
    from server import bus
    return bus


def _relay():
    from server import relay
    return relay


def emit(type_, cid, data=None):
    try:
        _bus().publish(type_, cid, data or {})
    except Exception:
        log.exception("emit %s failed", type_)


def _local(host, headers) -> bool:
    try:
        from server.device import PROXY_HEADERS
    except Exception:
        PROXY_HEADERS = ("x-forwarded-for", "cf-connecting-ip")
    return host in ("127.0.0.1", "::1") and not any(h in headers for h in PROXY_HEADERS)


def _hub_token_ok(given) -> bool:
    tok = os.environ.get("HUB_TOKEN")
    return bool(tok and given and secrets.compare_digest(given, tok))


def _service(request: Request):
    if _local(request.client.host if request.client else "", request.headers) or _hub_token_ok(request.headers.get("x-hub-token")):
        return
    raise HTTPException(401, "carrier only (localhost or x-hub-token)")


def _ws_service(ws: WebSocket) -> bool:
    return _local(ws.client.host if ws.client else "", ws.headers) or _hub_token_ok(ws.query_params.get("t"))


def _ws_device(ws: WebSocket) -> bool:
    if _ws_service(ws):
        return True
    try:
        from server import device
        return device._valid(ws.query_params.get("d"))
    except Exception:
        log.exception("device check failed")
        return False


# ---------------------------------------------------------------- carrier (signaling server) endpoints

@router.post("/android/route")
def route(request: Request, body: dict = Body(...)):
    """Before Maria's phone rings. Returns {decision, reason}. Fail open to NORMAL."""
    _service(request)
    cid, frm, to = str(body.get("call_id") or ""), str(body.get("from") or ""), str(body.get("to") or "")
    if not cid or not frm:
        raise HTTPException(400, "call_id and from required")
    att = body.get("attestation") if body.get("attestation") in ("A", "B", "C", "none") else "none"
    if cid in CALLS:  # repeated offer for the same call: never re-emit
        c = CALLS[cid]
        return {"decision": c["decision"], "reason": c["reason"]}
    emit("call.incoming", cid, {"from": frm, "to": to, "attestation": att, "scam_id_score": 0.1})
    try:
        from server import routing
        d = routing.decide(frm, att)
    except Exception:
        log.exception("routing failed; fail open")
        d = {"decision": "NORMAL", "reason": "Routing error, fail open"}
    if d.get("decision") not in DECISIONS:
        d = {"decision": "NORMAL", "reason": "Routing error, fail open"}
    emit("call.routed", cid, {"decision": d["decision"], "reason": d["reason"]})
    if d["decision"] != "BLOCKED_BACKFIRE":
        CALLS[cid] = {"from": frm, "to": to, "decision": d["decision"], "reason": d["reason"], "t0": time.time(),
                      "handed_off": False, "phone_decoy": False, "ended": False}
    return {"decision": d["decision"], "reason": d["reason"]}


@router.post("/android/call")
async def call_event(request: Request, body: dict = Body(...)):
    """{call_id, event: answered|handoff|ended, by?, ended_by?} from the carrier."""
    _service(request)
    cid, ev = str(body.get("call_id") or ""), body.get("event")
    st = CALLS.get(cid)
    if st is None or st["ended"]:
        return {"ok": False, "error": "unknown call"}
    if ev == "answered":
        by = "decoy" if body.get("by") == "decoy" else "maria"
        emit("call.answered", cid, {"by": by})
    elif ev == "handoff":
        if not st["handed_off"]:
            st["handed_off"] = True
            emit("handoff.started", cid, {"restore_deadline": time.time() + 30})
    elif ev == "ended":
        st["ended"] = True
        eb = body.get("ended_by") if body.get("ended_by") in ("caller", "maria", "decoy", "system") else "system"
        emit("call.ended", cid, {"ended_by": eb, "duration_s": round(time.time() - st["t0"], 1)})
        await _close(cid)
        CALLS.pop(cid, None)
    else:
        return {"ok": False, "error": "event must be answered|handoff|ended"}
    return {"ok": True}


# ---------------------------------------------------------------- relay plumbing

async def _send_to_caller(cid, frame):
    sink = SINKS.get(cid)
    if sink is not None:
        await sink(frame)  # before the decoy peer joins there is nobody to play to: drop


async def _ensure_relay(cid):
    if cid in OPENED:
        return
    OPENED.add(cid)
    r = _relay()
    await r.open(cid, lambda f, _c=cid: _send_to_caller(_c, f))
    sid = "android-" + cid
    await r.caller_frame(cid, {"event": "connected", "protocol": "Call", "version": "1.0.0"})
    await r.caller_frame(cid, {"event": "start", "sequence_number": "1", "stream_id": sid,
                               "start": {"call_session_id": cid, "stream_id": sid, "custom_parameters": {"call_id": cid},
                                         "media_format": {"encoding": "audio/x-mulaw", "sample_rate": 8000, "channels": 1}}})


async def _close(cid):
    SINKS.pop(cid, None)
    if cid in OPENED:
        OPENED.discard(cid)
        try:
            await _relay().close(cid)
        except Exception:
            log.exception("relay close failed")


class _Framer:
    """Binary PCM16 8 kHz chunks of any size -> 20 ms Telnyx media frames (caller/inbound track)."""

    def __init__(self, cid):
        self.cid, self.buf, self.chunk, self.ms = cid, b"", 0, 0

    async def feed(self, pcm: bytes):
        self.buf += pcm
        while len(self.buf) >= FRAME_BYTES:
            raw, self.buf = self.buf[:FRAME_BYTES], self.buf[FRAME_BYTES:]
            self.chunk += 1
            self.ms += 20
            await _relay().caller_frame(self.cid, {
                "event": "media", "sequence_number": str(self.chunk + 1), "stream_id": "android-" + self.cid,
                "media": {"track": "inbound", "chunk": str(self.chunk), "timestamp": str(self.ms),
                          "payload": base64.b64encode(ulaw.encode(raw)).decode()}})


async def _pump_binary(ws: WebSocket, cid: str, stop_when=lambda: False):
    framer = _Framer(cid)
    while True:
        m = await ws.receive()
        if m.get("type") == "websocket.disconnect":
            return
        if stop_when():
            return
        data = m.get("bytes")
        if data:
            await framer.feed(data)


# ---------------------------------------------------------------- Maria's phone

REPORTABLE = {"risk.update", "alert.fired", "decoy.turn", "decoy.fake_value", "guardrail.tripped", "artifacts.extracted"}
ARTIFACT_KINDS = {"callback_phone", "domain", "url", "wallet", "payment_handle", "gift_card_brand", "bank", "remote_app",
                  "impersonated_org", "script_tags", "instruction_to_ai"}
ASKS = {"otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app", "secrecy"}
STAGES = {"opening", "pretext", "pressure", "payment", "closing"}


def _clean_report(t, d):
    """Scores only, in contract shape. Anything else (transcripts, audio, free text beyond short chips) is dropped."""
    chips = [str(c)[:40] for c in (d.get("why_chips") or [])][:4]
    if t == "decoy.turn":
        return {"speaker": "decoy" if d.get("speaker") == "decoy" else "scammer", "text": str(d.get("text") or "")[:500],
                "latency_ms": int(d.get("latency_ms") or 0)}
    if t == "decoy.fake_value":
        return {"kind": str(d.get("kind") or "")[:40], "value": str(d.get("value") or "")[:80]}
    if t == "guardrail.tripped":
        return {"rule": str(d.get("rule") or "")[:60]}
    if t == "artifacts.extracted":
        items = [a for a in (d.get("artifacts") or []) if isinstance(a, dict) and a.get("kind") in ARTIFACT_KINDS][:40]
        return {"artifacts": [{k: (v if isinstance(v, list) else str(v)[:200]) for k, v in a.items()} for a in items]}
    if t == "alert.fired":
        return {"level": "realert" if d.get("level") == "realert" else "first", "why_chips": chips}
    s = max(0.0, min(1.0, float(d.get("s", 0))))
    band = "critical" if s >= 0.95 else "high" if s >= 0.80 else "watch" if s >= 0.40 else "low"
    imp = d.get("impersonates")
    return {"s": s, "band": band, "asks": [a for a in (d.get("asks") or []) if a in ASKS],
            "scam_type": str(d.get("scam_type") or "unknown")[:40],
            "stage": d.get("stage") if d.get("stage") in STAGES else "opening",
            "impersonates": str(imp)[:40] if imp else None, "addresses_ai_system": bool(d.get("addresses_ai_system")),
            "why_chips": chips, "engine": "local" if d.get("engine") == "local" else "cloud"}


@router.post("/android/report")
def report(request: Request, body: dict = Body(...)):
    """The Backfire app's detection result for a live call on this phone: risk.update / alert.fired only."""
    from server import device
    device.require_device(request)
    cid, t = str(body.get("call_id") or ""), body.get("type")
    st = CALLS.get(cid)
    if t not in REPORTABLE or st is None or st["ended"]:
        raise HTTPException(400, "type must be risk.update|alert.fired for a live call")
    try:
        data = _clean_report(t, body.get("data") or {})
    except (TypeError, ValueError):
        raise HTTPException(400, "bad data")
    emit(t, cid, data)
    return {"ok": True}


@router.post("/android/handoff")
def phone_handoff(request: Request, body: dict = Body(...)):
    """Scammer Get Scammed with the decoy running ON MARIA'S PHONE (Backfire app): no transfer. The network records
    user.action + handoff.started + call.answered(by decoy), so dashboards update and the number is blocked at the end."""
    from server import device
    device.require_device(request)
    cid = str(body.get("call_id") or "")
    st = CALLS.get(cid)
    if st is None or st["ended"]:
        raise HTTPException(404, "unknown or ended call")
    if not st["handed_off"]:
        st["handed_off"] = st["phone_decoy"] = True
        emit("user.action", cid, {"action": "scammer_get_scammed", "by": "phone"})   # by=phone: the carrier won't transfer
        emit("handoff.started", cid, {"restore_deadline": time.time() + 30})
        emit("call.answered", cid, {"by": "decoy"})
    return {"ok": True}


@router.websocket("/android/events/{call_id}")
async def events(ws: WebSocket, call_id: str):
    """This call's bus events, history first (so a late subscriber still sees call.routed / alert.fired)."""
    if not _ws_device(ws):
        await ws.close(code=1008); return
    await ws.accept()
    bus = _bus()
    q = bus.subscribe()
    try:
        for ev in [e for e in bus.history if e.get("call_id") == call_id]:
            await ws.send_json(ev)
        while True:
            ev = await q.get()
            if ev.get("call_id") == call_id:
                await ws.send_json(ev)
    except (WebSocketDisconnect, asyncio.CancelledError, RuntimeError):
        pass
    except Exception:
        log.exception("android events ws error")
    finally:
        bus.unsubscribe(q)


@router.websocket("/android/media/{call_id}")
async def maria_media(ws: WebSocket, call_id: str):
    """The caller's audio as heard on Maria's phone (binary PCM16 LE 8 kHz mono). Only for Live Guard calls,
    only until handoff (after that the decoy peer hears the scammer directly). Maria's own mic never comes here."""
    st = CALLS.get(call_id)
    if not _ws_device(ws) or st is None or st["decision"] != "LIVE_GUARD" or st["handed_off"]:
        await ws.close(code=1008); return
    await ws.accept()
    try:
        await _ensure_relay(call_id)
        await _pump_binary(ws, call_id, stop_when=lambda: st["handed_off"] or st["ended"])
    except (WebSocketDisconnect, RuntimeError):
        pass
    except Exception:
        log.exception("android media ws error (ignored)")


# ---------------------------------------------------------------- decoy peer (laptop, joined the call after handoff)

@router.websocket("/android/decoy/{call_id}")
async def decoy_peer(ws: WebSocket, call_id: str):
    """In: binary PCM16 8 kHz = the scammer. Out: Telnyx frames from P3's decoy (media / clear / mark), passed through."""
    st = CALLS.get(call_id)
    if not _ws_service(ws) or st is None or st["ended"]:
        await ws.close(code=1008); return
    await ws.accept()

    async def sink(frame):
        await ws.send_text(json.dumps(frame))

    try:
        await _ensure_relay(call_id)
        SINKS[call_id] = sink
        ok = await _relay().start_decoy(call_id)
        await ws.send_text(json.dumps({"event": "backfire", "decoy": "connected" if ok else "unavailable"}))
        if not ok:
            log.warning("decoy unavailable for %s (P3_DECOY_URL down?); scammer hears silence", call_id)
        await _pump_binary(ws, call_id, stop_when=lambda: st["ended"])
    except (WebSocketDisconnect, RuntimeError):
        pass
    except Exception:
        log.exception("android decoy ws error (ignored)")
    finally:
        if SINKS.get(call_id) is sink:
            SINKS.pop(call_id, None)
        try:
            await _relay().stop_decoy(call_id)
        except Exception:
            pass
