"""Backfire hub: event bus, WS /events, routing store, stubs. Run: uvicorn server.main:app --port 8000"""
import asyncio, logging, os, re, time
from fastapi.responses import HTMLResponse
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

ACTIONS = {"continue", "scammer_get_scammed", "hang_up"}

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
    _auth(request.headers.get("x-hub-token"))
    t, cid = body.get("type"), body.get("call_id")
    if not t or not cid:
        return {"ok": False, "error": "type and call_id required"}
    if t in RESERVED:
        raise HTTPException(403, f"{t} is hub-only")
    bus.publish(t, cid, body.get("data") or {}, body.get("ts"))
    return {"ok": True}

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
    bus.publish("user.action", cid, {"action": action})
    return {"ok": True}

# ---- TASK-017: P4a intel mounted in-process (fail open: hub starts without it; stub fallbacks stay) ----
intel_api = None
DECOY_CALLS: set = set()   # call_ids where the decoy took over (hub-observed handoff)
def _intel_guard(request: Request):
    """Intel routes need a paired device / direct localhost / HUB_TOKEN, except exactly POST /intel/actions/<id>/approve (simulated analyst button)."""
    if request.method == "POST" and re.fullmatch(r"/intel/actions/[A-Za-z0-9_-]+/approve", request.url.path):
        return   # only this exact route: command center is an unpaired browser and its actions are simulated
    device.require_device(request)
try:
    from intel import api as intel_api
    intel_api.configure(emit=bus.publish)
    def _intel_observe(ev):
        # artifacts.extracted arrives over unauthenticated POST /events: only act on calls the hub itself saw hand off to the decoy,
        # so a forged event can't make intel block arbitrary numbers.
        if ev.get("type") == "artifacts.extracted" and ev.get("call_id") not in DECOY_CALLS:
            log.warning("ignoring artifacts.extracted for non-decoy call %s", ev.get("call_id")); return
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
    elif t == "call.ended" and cid in DECOY_CALLS and CALLER_BY_CALL.get(cid) and intel_api is None:  # stub only when intel is not mounted (intel.observe blocks the caller otherwise)
        num = CALLER_BY_CALL[cid]
        if num in db.EMERGENCY or db.has("trusted", num):  # a (possibly spoofed) trusted number must not poison her blocklist
            DECOY_CALLS.discard(cid); return
        token = db.add_confirmed(num, "Decoy session ended")
        DECOY_CALLS.discard(cid)
        bus.publish("blocklist.updated", cid, {"number": num, "scope": "her", "undo_token": token})

bus.add_observer(_observe)

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

@app.get("/demo/latency")
def demo_latency():
    return ops.latency_summary()

@app.get("/demo/status")
def demo_status(request: Request, format: str = ""):
    """Integration readiness: routers mounted, remote P2/P3/P4 probes, flags (never values), DB counts."""
    s = ops.status(app)
    if format == "html" or (format != "json" and "text/html" in request.headers.get("accept", "")):
        return HTMLResponse(ops.status_html(s))
    return s

def _reset_intel():
    if intel_api is None:
        return
    try:
        st = intel_api._store()
        for (name,) in st.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall():
            st.x(f"DELETE FROM {name}")
        intel_api._calls.clear()
    except Exception:
        log.exception("intel reset failed")

@app.post("/demo/reset")
def demo_reset(request: Request):
    _auth(request.headers.get("x-hub-token"))
    t0 = time.time()
    db.reset_all(); bus.reset(); _reset_intel(); ops.reset(); CALLER_BY_CALL.clear(); DECOY_CALLS.clear()
    return {"ok": True, "seconds": round(time.time() - t0, 3)}

@app.post("/demo/replay")
async def demo_replay(request: Request, body: dict = Body(default={})):
    _auth(request.headers.get("x-hub-token"))
    """DEMO_MODE: replay mock/events.json on WS /events. body: {call_id?: str, speed?: float}"""
    asyncio.create_task(replay.run(body.get("call_id"), float(body.get("speed", 1.0))))
    return {"ok": True}

if os.environ.get("DEMO_MODE") == "1":
    @app.on_event("startup")
    async def _auto_replay():
        asyncio.create_task(replay.run(None, 1.0, loop=True))

# voip (Telnyx scam line: /telnyx/webhook, /media/{call_id}, /voip/webrtc-token) mounted in this one process. Fail open: hub still starts without it.
try:
    from voip.router import router as _voip_router
    mount_router(_voip_router)
except Exception:
    log.exception("voip router not mounted")

# Maria's app, same-origin with the hub (phone via tunnel). Mounted last so API routes win.
_WEB = pathlib.Path(__file__).resolve().parent.parent / "web" / "customer"
if _WEB.is_dir():
    app.mount("/app", StaticFiles(directory=str(_WEB), html=True), name="customer-app")

# P4b command center, same pattern (after API routes).
_CC = pathlib.Path(__file__).resolve().parent.parent / "web" / "command-center"
if _CC.is_dir():
    app.mount("/command-center", StaticFiles(directory=str(_CC), html=True), name="command-center")
