"""Backfire hub: event bus, WS /events, routing store, stubs. Run: uvicorn server.main:app --port 8000"""
import asyncio, logging, os, time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from . import bus, db, routing, replay

log = logging.getLogger("hub")
app = FastAPI(title="Backfire hub (Simulated carrier network)")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
ACTIONS = {"continue", "scammer_get_scammed", "hang_up"}
ingested: list = []

def mount_router(router, prefix=""):
    """Mount point for routers from voip/ and other pipelines."""
    app.include_router(router, prefix=prefix)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.websocket("/events")
async def ws_events(ws: WebSocket, call_id: str | None = None):
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
def post_event(body: dict = Body(...)):
    t, cid = body.get("type"), body.get("call_id")
    if not t or not cid:
        return {"ok": False, "error": "type and call_id required"}
    bus.publish(t, cid, body.get("data") or {}, body.get("ts"))
    return {"ok": True}

@app.get("/routing/lookup")
def lookup(from_: str = Query("", alias="from"), attestation: str = "none"):
    return routing.decide(from_, attestation)

@app.post("/user/action")
def user_action(body: dict = Body(...)):
    action, cid = body.get("action"), body.get("call_id")
    if action not in ACTIONS or not cid:
        return {"ok": False, "error": "call_id and action in %s required" % sorted(ACTIONS)}
    bus.publish("user.action", cid, {"action": action})
    return {"ok": True}

@app.post("/intel/ingest")
def intel_ingest(body: dict = Body(default={})):
    """P1 stub: logs only. P4 replaces."""
    ingested.append(body)
    log.info("intel.ingest stub call_id=%s artifacts=%d", body.get("call_id"), len(body.get("artifacts") or []))
    return {"ok": True, "stub": True}

# ---- TASK-007: blocklist stub, protection log, reset, DEMO_MODE replay ----
CALLER_BY_CALL: dict = {}  # call_id -> caller number, filled from call.incoming
DECOY_CALLS: set = set()   # call_ids where the decoy took over

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
    elif t == "call.ended" and cid in DECOY_CALLS and CALLER_BY_CALL.get(cid):
        num = CALLER_BY_CALL[cid]
        token = db.add_confirmed(num, "Decoy session ended")
        DECOY_CALLS.discard(cid)
        bus.publish("blocklist.updated", cid, {"number": num, "scope": "her", "undo_token": token})

bus.add_observer(_observe)

@app.get("/protection-log")
def protection_log():
    blocked = [{"number": r["number"], "reason": r["reason"], "ts": r["ts"], "undo_token": r["undo_token"]} for r in db.list_confirmed()]
    return {"blocked": blocked, "calls": db.list_calls()}

@app.post("/protection-log/undo")
def protection_undo(body: dict = Body(...)):
    return {"ok": db.undo(body.get("undo_token", ""))}

@app.post("/demo/reset")
def demo_reset():
    t0 = time.time()
    db.reset_all(); bus.reset(); CALLER_BY_CALL.clear(); DECOY_CALLS.clear(); ingested.clear()
    return {"ok": True, "seconds": round(time.time() - t0, 3)}

@app.post("/demo/replay")
async def demo_replay(body: dict = Body(default={})):
    """DEMO_MODE: replay mock/events.json on WS /events. body: {call_id?: str, speed?: float}"""
    asyncio.create_task(replay.run(body.get("call_id"), float(body.get("speed", 1.0))))
    return {"ok": True}

if os.environ.get("DEMO_MODE") == "1":
    @app.on_event("startup")
    async def _auto_replay():
        asyncio.create_task(replay.run(None, 1.0, loop=True))
