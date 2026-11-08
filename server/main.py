"""Backfire hub: event bus, WS /events, routing store, stubs. Run: uvicorn server.main:app --port 8000"""
import asyncio, logging, os, re, secrets, time
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import Depends, HTTPException, Request, FastAPI, WebSocket, WebSocketDisconnect, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pathlib
from . import bus, db, routing, replay, ops, relay, device

log = logging.getLogger("hub")
app = FastAPI(title="Backfire hub (Simulated carrier network)")
app.add_middleware(CORSMiddleware, allow_origins=os.environ.get("HUB_CORS_ORIGINS", "*").split(","), allow_methods=["*"], allow_headers=["*"])
HUB_TOKEN = os.environ.get("HUB_TOKEN")  # when set, service endpoints require header x-hub-token
# Events only the hub/voip may emit (via bus.publish in-process); rejected on POST /events.
RESERVED = {"call.incoming", "call.routed", "call.answered", "call.ended", "user.action", "handoff.started", "handoff.restored"}

def _auth(token):
    if HUB_TOKEN and token != HUB_TOKEN:
        raise HTTPException(401, "bad or missing token")

ACTIONS = {"continue", "scammer_get_scammed", "hang_up", "answer", "decline"}
RING_ACTIONS = {"answer", "decline"}   # the customer accepts/declines an incoming call: valid only while it is ringing

def _ringing(cid) -> bool:
    """Ringing = call.incoming seen and not yet routed BLOCKED_BACKFIRE, answered or ended."""
    seen = False
    for e in bus.history:
        if e.get("call_id") != cid: continue
        t = e.get("type")
        if t == "call.incoming": seen = True
        elif t in ("call.answered", "call.ended", "handoff.started"): return False
        elif t == "call.routed" and (e.get("data") or {}).get("decision") == "BLOCKED_BACKFIRE": return False
    return seen

app.include_router(relay.router)
app.include_router(device.router)
device._announce()

def mount_router(router, prefix=""):
    """Mount point for routers from voip/ and other pipelines."""
    app.include_router(router, prefix=prefix)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.websocket("/events")
async def ws_events(ws: WebSocket, call_id: str | None = None, token: str | None = None):
    if HUB_TOKEN and token != HUB_TOKEN:
        await ws.close(code=1008); return
    await ws.accept()
    q = bus.subscribe()
    try:
        while True:
            ev = await q.get()
            if call_id is None or ev["call_id"] == call_id:
                await ws.send_json(ev)
    except (WebSocketDisconnect, asyncio.CancelledError):
        pass
    except Exception:
        log.exception("ws /events error")
    finally:
        bus.unsubscribe(q)

@app.post("/events")
def post_event(request: Request, body: dict = Body(...)):
    pt = os.environ.get("PIPELINE_TOKEN")   # P2/P3/P4 present x-pipeline-token; when set it is required (fail closed) and separate from HUB_TOKEN
    dev_only = False
    if pt:
        if not secrets.compare_digest(request.headers.get("x-pipeline-token", ""), pt):
            if device._valid(request.headers.get("x-device-token")):
                dev_only = True    # a paired device (second client acting as the customer) may post ONLY on-device detection events
            else:
                raise HTTPException(401, "bad or missing pipeline token")
    else:
        _auth(request.headers.get("x-hub-token"))
    t, cid = body.get("type"), body.get("call_id")
    if not t or not cid:
        return {"ok": False, "error": "type and call_id required"}
    if t in RESERVED:
        raise HTTPException(403, f"{t} is hub-only")
    data = body.get("data") or {}
    lvl = data.get("level") if isinstance(data, dict) else None
    if dev_only:
        data = _device_event(request.headers.get("x-device-token"), t, cid, data)   # raises for anything but device risk/transcript: never reaches dedupe
    elif t == "alert.fired" and _dup_alert(cid, lvl):
        log.warning("dup alert ignored call=%s level=%s", str(cid)[:8], lvl)
        return {"ok": True, "duplicate": True}
    bus.publish(t, cid, data, None if dev_only else body.get("ts"))
    if t == "alert.fired" and not dev_only:
        _record_alert(cid, lvl)   # remembered only after an authorized publish
    return {"ok": True}

_ALERTS: dict = {}          # (call_id, level) -> time of the last accepted alert.fired from POST /events
REALERT_DEDUP_S = 3.0       # P2 retries a failed POST within seconds; real re-alerts (a new rise) are further apart

def _dup_alert(cid, level) -> bool:
    """P2 retries POSTs, so the same alert.fired can arrive twice. Exactly one level 'first' per call, ever; a 'realert' repeated within
    REALERT_DEDUP_S is a retry (genuine re-alerts need a dip and a new rise, so they are further apart). Read-only: see _record_alert."""
    now = time.time()
    for k in [k for k, v in _ALERTS.items() if now - v > 3600]: _ALERTS.pop(k, None)
    last = _ALERTS.get((str(cid), str(level)))
    return last is not None and (level != "realert" or now - last < REALERT_DEDUP_S)

def _record_alert(cid, level):
    _ALERTS[(str(cid), str(level))] = time.time()

# ---- paired-device events: engine "device" risk.update / transcript.caller from a second client (e.g. native Android on-device detection) ----
_BANDS = {"low", "watch", "high", "critical"}
_STAGES = {"opening", "pretext", "pressure", "payment", "closing"}
_ASKS = {"otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app", "secrecy"}
DEVICE_EVENT_LIMIT = (40, 10.0)    # at most 40 device events per 10 s per paired device
_dev_hits: dict = {}

def _device_event(token, t, cid, d):
    """Strictly validate and REBUILD the event (unknown fields dropped). Only risk.update / transcript.caller with engine == "device", only for a call
    the hub has seen that is still active and where this device holds its /listen or /talk socket, rate-limited per device. Anything else is refused: a paired device is not a pipeline."""
    import hashlib
    if t not in ("risk.update", "transcript.caller") or not isinstance(d, dict) or d.get("engine") != "device":
        raise HTTPException(403, "a paired device may post only risk.update / transcript.caller with engine 'device'")
    if cid not in CALLER_BY_CALL:
        raise HTTPException(404, "unknown call_id")
    if relay._call_ended(cid):
        raise HTTPException(409, "call already ended")
    if not relay.device_holds_slot(cid, token):
        raise HTTPException(403, "attach WS /listen or /talk for this call from this device first")
    key, now = hashlib.sha256(token.encode()).hexdigest(), time.time()
    hits = [x for x in _dev_hits.get(key, []) if now - x < DEVICE_EVENT_LIMIT[1]]
    if len(hits) >= DEVICE_EVENT_LIMIT[0]:
        _dev_hits[key] = hits
        raise HTTPException(429, "too many device events; slow down")
    hits.append(now); _dev_hits[key] = hits
    def bad(msg): raise HTTPException(422, msg)
    def txt(v, n): return "".join(c for c in str(v) if c.isprintable())[:n]
    if t == "transcript.caller":
        if not isinstance(d.get("text"), str) or not isinstance(d.get("is_final"), bool): bad("text (str) and is_final (bool) required")
        return {"utterance_id": txt(d.get("utterance_id", ""), 40), "text": txt(d["text"], 500), "is_final": d["is_final"], "engine": "device"}
    s = d.get("s")
    if isinstance(s, bool) or not isinstance(s, (int, float)) or not 0 <= s <= 1: bad("s must be a number 0-1")
    if d.get("band") not in _BANDS: bad("band must be one of %s" % sorted(_BANDS))
    if d.get("stage") not in _STAGES: bad("stage must be one of %s" % sorted(_STAGES))
    asks = d.get("asks", [])
    if not isinstance(asks, list) or any(a not in _ASKS for a in asks): bad("asks must be a list of known asks")
    chips = d.get("why_chips", [])
    if not isinstance(chips, list) or len(chips) > 4 or any(not isinstance(c, str) for c in chips): bad("why_chips: up to 4 strings")
    imp = d.get("impersonates")
    if imp is not None and not isinstance(imp, str): bad("impersonates must be a string or null")
    return {"s": round(float(s), 3), "band": d["band"], "asks": list(dict.fromkeys(asks)), "scam_type": txt(d.get("scam_type", "none"), 40) or "none",
            "stage": d["stage"], "impersonates": txt(imp, 30) if imp else None, "addresses_ai_system": bool(d.get("addresses_ai_system")),
            "why_chips": [txt(c, 60) for c in chips], "engine": "device"}

@app.get("/routing/lookup")
def lookup(request: Request, from_: str = Query("", alias="from"), attestation: str = "none"):
    _auth(request.headers.get("x-hub-token"))
    if attestation not in ("A", "B", "C", "none"):
        attestation = "none"
    return routing.decide(from_, attestation)

@app.post("/user/action", dependencies=[Depends(device.require_device)])
def user_action(body: dict = Body(...)):
    action, cid = body.get("action"), body.get("call_id")
    if action not in ACTIONS or not cid:
        return {"ok": False, "error": "call_id and action in %s required" % sorted(ACTIONS)}
    if cid not in CALLER_BY_CALL:  # only for calls the hub has seen
        raise HTTPException(404, "unknown call_id")
    if action in RING_ACTIONS and not _ringing(cid):
        raise HTTPException(409, f"'{action}' is only valid while the call is ringing")
    bus.publish("user.action", cid, {"action": action})
    return {"ok": True}

# ---- TASK-017: P4a intel mounted in-process (fail open: hub starts without it; stub fallbacks stay) ----
intel_api = None
DECOY_CALLS: set = set()   # call_ids where the decoy took over (hub-observed handoff)
def _intel_guard(request: Request):
    """Intel routes need a paired device / direct localhost / HUB_TOKEN, except exactly POST /intel/actions/<id>/approve (simulated analyst button) and GET /intel/chain, GET /intel/map (read-only, synthetic)."""
    if request.method == "POST" and re.fullmatch(r"/intel/actions/[A-Za-z0-9_-]+/approve", request.url.path):
        return   # only this exact route: command center is an unpaired browser and its actions are simulated
    if request.method == "GET" and request.url.path in ("/intel/chain", "/intel/map"):
        return   # exact-path, GET-only: read-only synthetic views the command-center map needs over the tunnel (nothing else under /intel/ opens)
    device.require_device(request)
try:
    from intel import api as intel_api
    intel_api.configure(emit=bus.publish)
    def _intel_observe(ev):
        # artifacts.extracted arrives over unauthenticated POST /events: only act on calls the hub itself saw hand off to the decoy,
        # so a forged event can't make intel block arbitrary numbers.
        if ev.get("type") == "artifacts.extracted" and ev.get("call_id") not in DECOY_CALLS:
            log.warning("ignoring artifacts.extracted for non-decoy call %s", ev.get("call_id")); return
        if ev.get("type") == "call.ended" and (ev.get("data") or {}).get("legit") is True:
            # voip saw sustained low risk after handoff: caller looked legitimate, so enforce nothing (no blocklist add on this call)
            intel_api._calls.setdefault(ev["call_id"], {})["decoy"] = False
            DECOY_CALLS.discard(ev["call_id"])
        intel_api.observe(ev)
    bus.add_observer(_intel_observe)
    app.include_router(intel_api.router, dependencies=[Depends(_intel_guard)])
except Exception:
    intel_api = None
    log.exception("intel not mounted; falling back to the P1 decoy-ended blocklist stub")

# ---- TASK-007: blocklist stub, protection log, reset, DEMO_MODE replay ----
CALLER_BY_CALL: dict = {}  # call_id -> caller number, filled from call.incoming

def _observe(ev):
    """Bus observer: track callers, log calls, and on decoy call.ended add to confirmed_scammers."""
    t, cid, d = ev["type"], ev["call_id"], ev["data"]
    if t == "call.incoming":
        CALLER_BY_CALL[cid] = d.get("from", "")
    elif t == "call.routed":
        db.log_call(cid, CALLER_BY_CALL.get(cid, ""), d.get("decision"), d.get("reason"))
    elif t in ("handoff.started",) or (t == "call.answered" and d.get("by") == "decoy"):
        DECOY_CALLS.add(cid)
    elif t == "handoff.restored":
        DECOY_CALLS.discard(cid)
        for k in [k for k in _ALERTS if k[0] == str(cid)]:   # F5: after a restore a genuinely new 'first' alert must be able to fire
            _ALERTS.pop(k, None)
    elif t == "call.ended" and cid in DECOY_CALLS and CALLER_BY_CALL.get(cid) and intel_api is None and d.get("legit") is not True:  # stub only when intel is not mounted (intel.observe blocks the caller otherwise)
        num = CALLER_BY_CALL[cid]
        if num in db.EMERGENCY or db.has("trusted", num):  # a (possibly spoofed) trusted number must not poison her blocklist
            DECOY_CALLS.discard(cid); return
        token = db.add_confirmed(num, "Decoy session ended")
        DECOY_CALLS.discard(cid)
        bus.publish("blocklist.updated", cid, {"number": num, "scope": "her", "undo_token": token})

bus.add_observer(_observe)
try:   # insurance detector, OFF unless FALLBACK_DETECT=1
    from . import fallback_detect
    fallback_detect.install()
except Exception:
    log.exception("fallback_detect unavailable (fail open)")

@app.get("/protection-log", dependencies=[Depends(device.require_device)])
def protection_log():
    blocked = [{"number": r["number"], "reason": r["reason"], "ts": r["ts"], "undo_token": r["undo_token"]} for r in db.list_confirmed()]
    if intel_api is not None:
        try:
            blocked = sorted(blocked + [dict(r, number=db.norm(r["number"])) for r in intel_api.protection_entries()], key=lambda r: r["ts"] or 0, reverse=True)[:50]
        except Exception:
            log.exception("intel protection entries failed")
    return {"blocked": blocked, "calls": db.list_calls()}

@app.post("/protection-log/undo", dependencies=[Depends(device.require_device)])
def protection_undo(body: dict = Body(...)):
    tok = body.get("undo_token", "")
    if intel_api is not None:
        try:
            if intel_api.undo_block(tok):
                return {"ok": True}
        except Exception:
            log.exception("intel undo failed")
    return {"ok": db.undo(tok)}

_E164 = re.compile(r"^\+[1-9]\d{7,14}$")

@app.get("/trusted", dependencies=[Depends(device.require_device)])
def trusted_list():
    return {"trusted": db.list_trusted()}

@app.post("/trusted", dependencies=[Depends(device.require_device)])
def trusted_add(body: dict = Body(...)):
    number = db.norm(str(body.get("number", "")))
    if not _E164.match(number):
        raise HTTPException(422, "number must be E.164, e.g. +15555550123")
    label = "".join(ch for ch in str(body.get("label") or "") if ch.isprintable())[:60]
    db.add_trusted(number, label)
    return {"ok": True, "number": number, "label": label}

@app.delete("/trusted/{number}", dependencies=[Depends(device.require_device)])
def trusted_remove(number: str):
    number = db.norm(number)
    return {"ok": True, "removed": bool(_E164.match(number)) and db.remove_trusted(number)}   # idempotent

@app.get("/demo/latency")
def demo_latency():
    return ops.latency_summary()

@app.get("/demo/status")
def demo_status(request: Request, format: str = ""):
    """Integration readiness: routers mounted, remote P2/P3/P4 probes, flags (never values), DB counts."""
    s = ops.status(app)
    try:
        device.require_device(request)
    except HTTPException:   # public/tunnel viewers get the count only: call ids and activity times stay local/paired
        s.pop("active_call_ids", None); s["flags"].pop("last_call_activity_ts", None)
    if format == "html" or (format != "json" and "text/html" in request.headers.get("accept", "")):
        return HTMLResponse(ops.status_html(s))
    return s

_HUB_OWNED_TABLES = {"device_tokens", "confirmed_scammers", "campaign_numbers", "trusted", "calls"}

def _reset_intel():
    if intel_api is None:
        return
    try:
        st = intel_api._store()
        for (name,) in st.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall():
            if name in _HUB_OWNED_TABLES:   # INTEL_DB pointed at the hub DB must never wipe pairing or routing tables
                continue
            st.x(f"DELETE FROM {name}")
        intel_api._calls.clear()
    except Exception:
        log.exception("intel reset failed")

@app.post("/demo/reset", dependencies=[Depends(device.require_device)])
def demo_reset(request: Request, seed: bool = Query(True), force: bool = Query(False)):
    """One reset for everything (data/RESET.md): hub state + intel tables, then intel.seed_demo in-process
    (yesterday's synthetic sighting) unless ?seed=0. Seeding fails open: reset still succeeds.
    Direct localhost, a paired device, or x-hub-token==HUB_TOKEN only (a remote caller must not be able to wipe the demo)."""
    t0 = time.time()
    live, _ = relay.active_calls()
    if live and not force:   # F11: a reset mid-call wipes bus history, DECOY_CALLS and blocklist state under a live call
        raise HTTPException(409, f"{len(live)} call(s) live ({', '.join(i[:8] for i in live)}): refusing to reset. Wait for call.ended or POST /demo/reset?force=1")
    db.reset_all(); bus.reset(); _reset_intel(); ops.reset(); _ALERTS.clear(); CALLER_BY_CALL.clear(); DECOY_CALLS.clear()
    out = {"ok": True, "seeded": False}
    if seed and intel_api is not None:
        try:
            from intel import seed_demo
            st = intel_api._store()
            info = seed_demo.seed(st, quiet=True)
            state = st.state()
            out.update(seeded=True, seed={"campaign_id": info.get("campaign_id"), "status": info.get("status"),
                                         "sightings": info.get("sightings"), "indicators": info.get("indicators")},
                       check={k: (len(v) if isinstance(v, list) else v) for k, v in state.items()})
        except Exception as e:
            log.exception("seed_demo failed (reset itself succeeded)")
            out["seed_error"] = type(e).__name__
    out["seconds"] = round(time.time() - t0, 3)
    return out

@app.get("/demo/caller.wav")
def demo_caller_wav():
    """Phone-free demo: the synthetic scammer audio (scripts/make_scam_wav.sh -> logs/sim_scam.wav), same file scripts/sim_call.py --wav streams.
    Path is env DEMO_CALLER_WAV or $LOGDIR/sim_scam.wav, fixed server-side (never from the request). Audio only, no auth. Range supported."""
    root = pathlib.Path(__file__).resolve().parent.parent
    p = pathlib.Path(os.environ.get("DEMO_CALLER_WAV") or (pathlib.Path(os.environ.get("LOGDIR") or "logs") / "sim_scam.wav"))
    p = p if p.is_absolute() else root / p
    if not p.is_file():
        raise HTTPException(404, "no caller WAV yet: run scripts/make_scam_wav.sh (or set DEMO_CALLER_WAV)")
    return FileResponse(p, media_type="audio/wav", filename="caller.wav", content_disposition_type="inline")

@app.post("/demo/replay", dependencies=[Depends(device.require_device)])
async def demo_replay(request: Request, body: dict = Body(default={})):
    """DEMO_MODE: replay mock/events.json on WS /events. body: {call_id?: str, speed?: float}"""
    asyncio.create_task(replay.run(body.get("call_id"), float(body.get("speed", 1.0))))
    return {"ok": True}

if os.environ.get("DEMO_MODE") == "1":
    @app.on_event("startup")
    async def _auto_replay():
        asyncio.create_task(replay.run(None, 1.0, loop=True))

# Voice enrollment (onboarding): proxies to P3 when connected, otherwise drops the audio and reports the synthetic fallback. Fail open.
try:
    from . import voice as _voice
    mount_router(_voice.router)
except Exception:
    log.exception("voice router not mounted")

# voip (Telnyx scam line: /telnyx/webhook, /media/{call_id}, /voip/webrtc-token) mounted in this one process. Fail open: hub still starts without it.
try:
    from voip.router import router as _voip_router
    mount_router(_voip_router)
except Exception:
    log.exception("voip router not mounted")

# android_voip bridge (P3 alternative carrier: /android/route|call|report|handoff + WS /android/events|media|decoy). Fail open: absent or broken -> hub still starts.
try:
    from android_voip.bridge.router import router as _android_router
    mount_router(_android_router)
except Exception:
    log.exception("android_voip bridge not mounted")

@app.get("/", include_in_schema=False)
def root(request: Request):
    """Judges type the bare URL: send them to Maria's app (keeps any ?query such as ?sim=1)."""
    q = request.url.query
    return RedirectResponse("/app/" + ("?" + q if q else ""), status_code=307)

# Maria's app, same-origin with the hub (phone via tunnel). Mounted last so API routes win.
_WEB = pathlib.Path(__file__).resolve().parent.parent / "web" / "customer"
if _WEB.is_dir():
    class _AppFiles(StaticFiles):
        """PWA delivery: pages/scripts/styles/manifest must revalidate on every load (a reload picks up a new build); images/icons may be cached."""
        async def get_response(self, path, scope):
            r = await super().get_response(path, scope)
            if r.status_code in (200, 304):
                ext = pathlib.PurePosixPath(path).suffix.lower()
                if ext in ("", ".html", ".js", ".css", ".webmanifest", ".json"):
                    r.headers["Cache-Control"] = "no-cache"
                elif ext in (".png", ".jpg", ".jpeg", ".svg", ".ico", ".webp", ".woff2", ".wav", ".mp3"):
                    r.headers["Cache-Control"] = "public, max-age=3600"
                if ext == ".webmanifest":
                    r.headers["Content-Type"] = "application/manifest+json"
            return r
    app.mount("/app", _AppFiles(directory=str(_WEB), html=True), name="customer-app")

# P4b command center, same pattern (after API routes).
_CC = pathlib.Path(__file__).resolve().parent.parent / "web" / "command-center"
if _CC.is_dir():
    app.mount("/command-center", StaticFiles(directory=str(_CC), html=True), name="command-center")
