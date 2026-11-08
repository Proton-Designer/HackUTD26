"""Backfire hub: event bus, WS /events, routing store, stubs. Run: uvicorn server.main:app --port 8000"""
import asyncio, logging, os, time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from . import bus, db, routing

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
