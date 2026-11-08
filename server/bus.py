"""In-process event bus. publish() is importable by voip/ and other pipelines."""
import asyncio, time, json, logging
log = logging.getLogger("hub.bus")
_subs: set = set()  # asyncio.Queue
_loop = None
history: list = []  # last events, for late WS subscribers / debugging
HISTORY_MAX = 500

def make_event(type_, call_id, data=None, ts=None):
    return {"type": type_, "call_id": call_id, "ts": ts if ts is not None else time.time(), "data": data or {}}

def publish(type_, call_id, data=None, ts=None):
    """Thread/loop-safe, never raises (fail open)."""
    try:
        ev = make_event(type_, call_id, data, ts)
        history.append(ev)
        del history[:-HISTORY_MAX]
        for q in list(_subs):
            try:
                if _loop is not None and _loop.is_running():
                    _loop.call_soon_threadsafe(q.put_nowait, ev)
                else:
                    q.put_nowait(ev)
            except Exception:
                log.exception("subscriber enqueue failed")
        return ev
    except Exception:
        log.exception("publish failed")
        return None

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
    history.clear()
