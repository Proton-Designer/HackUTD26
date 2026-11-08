"""In-process event bus. publish() is importable by voip/ and other pipelines."""
import asyncio, time, json, logging
log = logging.getLogger("hub.bus")
_subs: set = set()  # asyncio.Queue
_loop = None
_observers: list = []
history: list = []  # last events, for late WS subscribers / debugging
HISTORY_MAX = 500
CALLS: dict = {}   # call_id -> lifecycle state, NOT capped by HISTORY_MAX (a long call's call.incoming scrolls out of history): from, t0, answered, handoff, ended, blocked
CALLS_MAX = 500

def call_known(call_id, grace_s=1800) -> bool:
    """True for a call the hub saw (call.incoming) that is live or ended less than grace_s ago. Gate for pipeline events posted over HTTP."""
    c = CALLS.get(call_id)
    return bool(c and (not c["ended"] or time.time() - (c["t_end"] or 0) < grace_s))

def _track(ev):
    cid, t, d = ev.get("call_id"), ev.get("type"), ev.get("data") or {}
    if not cid: return
    c = CALLS.get(cid)
    if t == "call.incoming":
        CALLS[cid] = {"from": d.get("from", ""), "t0": ev["ts"], "answered": False, "handoff": "none", "ended": False, "blocked": False, "decision": None, "trusted": False, "t_end": None}
        for k in list(CALLS)[:-CALLS_MAX]:
            CALLS.pop(k, None)
    elif c is None:
        return
    elif t == "call.answered": c["answered"] = True
    elif t == "handoff.started": c["handoff"] = "started"
    elif t == "handoff.restored": c["handoff"] = "restored"
    elif t == "call.ended": c["ended"] = True; c["t_end"] = ev["ts"]
    elif t == "call.routed":
        c["decision"] = d.get("decision")
        # only a POSITIVELY trusted NORMAL (emergency exemption, or trusted contact with verified caller ID) skips scoring; fail-open NORMALs keep the detectors on
        c["trusted"] = d.get("decision") == "NORMAL" and str(d.get("reason", "")).startswith(("Exempt (emergency number)", "Trusted contact, caller ID verified"))
        if d.get("decision") == "BLOCKED_BACKFIRE": c["blocked"] = True

def make_event(type_, call_id, data=None, ts=None):
    return {"type": type_, "call_id": call_id, "ts": ts if ts is not None else time.time(), "data": data or {}}

def publish(type_, call_id, data=None, ts=None):
    """Thread/loop-safe, never raises (fail open)."""
    try:
        ev = make_event(type_, call_id, data, ts)
        history.append(ev)
        del history[:-HISTORY_MAX]
        try: _track(ev)
        except Exception: log.exception("call tracking failed")
        for q in list(_subs):
            try:
                if _loop is not None and _loop.is_running():
                    _loop.call_soon_threadsafe(q.put_nowait, ev)
                else:
                    q.put_nowait(ev)
            except Exception:
                log.exception("subscriber enqueue failed")
        for fn in list(_observers):
            try:
                fn(ev)
            except Exception:
                log.exception("observer failed")
        return ev
    except Exception:
        log.exception("publish failed")
        return None

def add_observer(fn):
    """fn(event) called synchronously on every publish; exceptions are swallowed."""
    _observers.append(fn)

def subscribe():
    global _loop
    try:
        _loop = asyncio.get_running_loop()
    except RuntimeError:
        pass
    q = asyncio.Queue(maxsize=1000)
    _subs.add(q)
    return q

def unsubscribe(q):
    _subs.discard(q)

def reset():
    history.clear(); CALLS.clear()
