"""FastAPI router for P4a. P1 mounts it:  app.include_router(intel.api.router)
and wires events to its bus:            intel.api.configure(emit=bus_publish)
where bus_publish(type, call_id, data) publishes the contract envelope."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from . import agent, gate, lookups as L
from .store import Store, default_store

router = APIRouter(prefix="/intel", tags=["intel"])
_cfg: dict = {"store": None, "emit": L.emit, "llm": None, "tools": None, "use_llm": True}


def configure(store: Store | None = None, emit=None, llm=None, tools=None, use_llm: bool | None = None) -> None:
    for k, v in {"store": store, "emit": emit, "llm": llm, "tools": tools, "use_llm": use_llm}.items():
        if v is not None:
            _cfg[k] = v
    if emit is not None:
        L.set_sink(emit)  # lookups emit intel.lookup themselves; route them to the same bus


def _store() -> Store:
    return _cfg["store"] or default_store()


class Ingest(BaseModel):
    call_id: str
    scammer_transcript: str | None = None   # accepted for the contract, never read (agent sees typed artifacts only)
    artifacts: list | dict = []
    calling_number: str | None = None        # ask P1 to include this (needed to block the caller)
    customer_number: str | None = None       # the protected customer's own number: never a target (echo guard)
    attestation: str | None = None
    carrier: str | None = None


@router.post("/ingest")
def ingest(body: Ingest):
    return agent.run(body.call_id, body.artifacts, _store(), calling_number=body.calling_number,
                     customer_number=body.customer_number,
                     attestation=body.attestation, carrier=body.carrier, llm=_cfg["llm"], tools=_cfg["tools"],
                     emit=_cfg["emit"], use_llm=_cfg["use_llm"])


@router.post("/actions/{action_id}/approve")
def approve(action_id: str):
    try:
        a = gate.approve(_store(), action_id, emit=_cfg["emit"])
        return {"ok": True, "status": "approved" if a["status"] == "simulated: applied" else a["status"], "action": a}
    except KeyError:
        raise HTTPException(404, "unknown action")


def _undo_hold(token: str) -> dict | None:
    """Undo a Nessie transfer hold: transfer back to pending (PUT status, verified on the sandbox)."""
    from . import nessie
    row = _store().q("SELECT * FROM holds WHERE undo_token=? AND active=1", token)
    if not row or not nessie.release_transfer(row[0]["transfer_id"]):
        return None  # unknown token, or Nessie down: hold stays (fail safe for her money)
    _store().undo_hold(token)
    _cfg["emit"]("intel.action", row[0]["call_id"], {
        "action_id": row[0]["action_id"], "kind": "hold_transfer", "target": row[0]["transfer_id"], "scope": "her",
        "status": "applied", "gate_status": "undone by customer: transfer back to pending", "active": False,
        "simulated": True, "undo_token": token, "reason": "Hold released by the customer (Nessie sandbox)"})
    return row[0]


@router.post("/blocklist/{undo_token}/undo")
def undo(undo_token: str):
    if undo_token.startswith("hold-"):
        row = _undo_hold(undo_token)
        if not row:
            raise HTTPException(404, "unknown or already undone, or Nessie unavailable")
        return {"undone": True, "kind": "hold_transfer", "transfer_id": row["transfer_id"]}
    row = _store().undo(undo_token)
    if not row:
        raise HTTPException(404, "unknown or already undone")
    _emit_undo(row)
    return {"undone": True, **row}


def _emit_undo(row: dict) -> None:
    """blocklist.updated active=false for the undone block and every other block lifted on that number (F16)."""
    for r in [row] + list(row.get("also_undone") or []):
        _cfg["emit"]("blocklist.updated", None, {"number": r["number"], "scope": r["scope"], "undo_token": r["undo_token"],
                                                 "active": False, "reason": "undone by customer"})


@router.get("/blocked")
def blocked(number: str):
    """For P1's pre-ring routing: {blocked, reason}."""
    b, reason = _store().is_blocked(number)
    return {"blocked": b, "reason": reason}


@router.get("/state")
def state():
    return _store().state()


@router.get("/chain")
def chain():
    """Read-only laundering-chain graph (Capital One Nessie sandbox, mock data) for the /intel/map page.
    Never raises: Nessie down -> seeded values with status 'unavailable'."""
    from . import nessie
    try:
        holds = _store().q("SELECT transfer_id, amount FROM holds WHERE active=1")
    except Exception:
        holds = []
    try:
        return nessie.chain(active_holds=holds)
    except Exception as e:  # fail open
        return {"status": "unavailable", "reason": type(e).__name__, "nodes": [], "edges": [], "simulated": True}


@router.get("/map")
def chain_map():
    """Standalone network-map page (self-contained HTML; it only fetches /intel/chain, same origin)."""
    return FileResponse(Path(__file__).with_name("chain_map.html"), media_type="text/html")


# ---- In-process seam for P1's hub (no HTTP hop): bus.add_observer(intel.api.observe) ----
import logging
import os
import threading

log = logging.getLogger("intel")
GRACE_S = float(os.getenv("INTEL_EXTRACT_GRACE", "20"))  # wait this long after a decoy call ends for artifacts
_calls: dict = {}          # call_id -> {"from", "attestation", "decoy", "ingested"}
_calls_lock = threading.Lock()


def _run_bg(call_id: str, artifacts) -> None:
    kind = "artifacts" if artifacts else "fallback"
    with _calls_lock:
        c = _calls.setdefault(call_id, {})
        if c.get("legit"):  # legit: the customer was restored, caller looked legitimate -> enforce nothing
            return
        # A real haul always runs once, even after the no-artifact fallback already ran for a slow extractor
        # (otherwise late artifacts were dropped: no lookups, no hold). The fallback never runs after a haul.
        if c.get("ingested") == "artifacts" or (kind == "fallback" and c.get("ingested")):
            return
        c["ingested"] = kind

    def work():
        try:
            agent.run(call_id, artifacts, _store(), calling_number=c.get("from"), customer_number=c.get("to"),
                      attestation=c.get("attestation"),
                      carrier=c.get("carrier"), llm=_cfg["llm"], tools=_cfg["tools"], emit=_cfg["emit"],
                      use_llm=_cfg["use_llm"])
        except Exception:  # fail open: intel never breaks the call path
            log.exception("intel run failed for %s", call_id)
    threading.Thread(target=work, name=f"intel-{call_id}", daemon=True).start()


def observe(ev: dict) -> None:
    """Bus observer. Never raises, never blocks (the agent runs on a background thread, ~5 s with Nemotron).
    - call.incoming: remember the network calling number + attestation (trusted metadata).
    - handoff.started / call.answered by decoy: mark it a decoy call.
    - artifacts.extracted (P3): run the intel chain on the typed artifacts (scammer_transcript is never read).
    - call.ended with legit=true: the call is never actioned (no block, no campaign sighting), even if artifacts follow.
    - call.ended on a decoy call: if no artifacts arrive within INTEL_EXTRACT_GRACE s, run with none, which still
      blocks the caller for her (replaces P1's call.ended blocklist stub)."""
    try:
        t, cid, d = ev.get("type"), ev.get("call_id"), ev.get("data") or {}
        if not cid:
            return
        if t == "call.incoming":
            with _calls_lock:
                _calls[cid] = {"from": d.get("from"), "to": d.get("to"), "attestation": d.get("attestation"),
                               "carrier": d.get("carrier")}
        elif t == "handoff.started" or (t == "call.answered" and d.get("by") == "decoy"):
            with _calls_lock:
                _calls.setdefault(cid, {})["decoy"] = True
        elif t == "handoff.restored":
            with _calls_lock:
                _calls.setdefault(cid, {})["decoy"] = False
        elif t == "artifacts.extracted":
            _run_bg(cid, d.get("artifacts") or [])
        elif t == "call.ended" and d.get("legit") is True:
            # contracts/events.md: legit=true -> hub/intel must NOT blocklist this call (no block, no sighting)
            with _calls_lock:
                _calls.setdefault(cid, {}).update(legit=True, decoy=False)
        elif t == "call.ended" and _calls.get(cid, {}).get("decoy"):
            threading.Timer(GRACE_S, _run_bg, args=(cid, [])).start()
    except Exception:
        log.exception("intel observe failed")


def protection_entries(scope: str = "her") -> list[dict]:
    """Rows for P1's GET /protection-log 'blocked' list: {number, reason, ts, undo_token}, newest first."""
    rows = _store().q("SELECT number, reason, created, undo_token FROM blocklist WHERE active=1 AND scope=? "
                      "ORDER BY created DESC LIMIT 50", scope)
    return [{"number": r["number"], "reason": r["reason"], "ts": r["created"], "undo_token": r["undo_token"]} for r in rows]


def undo_block(undo_token: str) -> bool:
    """In-process undo for P1's POST /protection-log/undo. Emits blocklist.updated with active=false
    (or, for a 'hold-' token, releases the Nessie transfer hold)."""
    if str(undo_token).startswith("hold-"):
        return _undo_hold(undo_token) is not None
    row = _store().undo(undo_token)
    if row:
        _emit_undo(row)
    return bool(row)
