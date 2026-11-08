"""FastAPI router for P4a. P1 mounts it:  app.include_router(intel.api.router)
and wires events to its bus:            intel.api.configure(emit=bus_publish)
where bus_publish(type, call_id, data) publishes the contract envelope."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from . import agent, gate, lookups as L
from .store import Store, default_store

router = APIRouter(prefix="/intel", tags=["intel"])
_cfg: dict = {"store": None, "emit": L.emit, "llm": None, "tools": None, "use_llm": True}


def configure(store: Store | None = None, emit=None, llm=None, tools=None, use_llm: bool | None = None) -> None:
    for k, v in {"store": store, "emit": emit, "llm": llm, "tools": tools, "use_llm": use_llm}.items():
        if v is not None:
            _cfg[k] = v


def _store() -> Store:
    return _cfg["store"] or default_store()


class Ingest(BaseModel):
    call_id: str
    scammer_transcript: str | None = None   # accepted for the contract, never read (agent sees typed artifacts only)
    artifacts: list | dict = []
    calling_number: str | None = None        # ask P1 to include this (needed to block the caller)
    attestation: str | None = None
    carrier: str | None = None


@router.post("/ingest")
def ingest(body: Ingest):
    return agent.run(body.call_id, body.artifacts, _store(), calling_number=body.calling_number,
                     attestation=body.attestation, carrier=body.carrier, llm=_cfg["llm"], tools=_cfg["tools"],
                     emit=_cfg["emit"], use_llm=_cfg["use_llm"])


@router.post("/actions/{action_id}/approve")
def approve(action_id: str):
    try:
        return gate.approve(_store(), action_id, emit=_cfg["emit"])
    except KeyError:
        raise HTTPException(404, "unknown action")


@router.post("/blocklist/{undo_token}/undo")
def undo(undo_token: str):
    row = _store().undo(undo_token)
    if not row:
        raise HTTPException(404, "unknown or already undone")
    _cfg["emit"]("blocklist.updated", None, {"number": row["number"], "scope": row["scope"],
                                             "undo_token": undo_token, "active": False, "reason": "undone by customer"})
    return {"undone": True, **row}


@router.get("/blocked")
def blocked(number: str):
    """For P1's pre-ring routing: {blocked, reason}."""
    b, reason = _store().is_blocked(number)
    return {"blocked": b, "reason": reason}


@router.get("/state")
def state():
    return _store().state()
