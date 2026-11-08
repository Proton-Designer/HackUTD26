"""TASK-013: hub side of the one-stream media relay (Option A). Caller-leg frames only; Maria's audio never enters.
voip/ (eng2) owns the Telnyx WS and calls (all async, none ever raises, none blocks on P2/P3):
  await relay.open(call_id, send_to_caller, on_decoy_lost=None)   send_to_caller(frame: dict) writes a Telnyx media/clear/mark frame to the Telnyx WS
  await relay.caller_frame(call_id, frame)    every Telnyx frame (connected/start/media/stop), dict or JSON str
  await relay.start_decoy(call_id) -> bool    connect to P3, send connected+start, then relay both ways
  await relay.stop_decoy(call_id); await relay.close(call_id)
Env: P2_STT_URL (e.g. ws://host:port -> WS /stt/{call_id}), P3_DECOY_URL (e.g. wss://host -> WSS /decoy/{call_id}; unset -> built-in
echo decoy /decoy-echo/{call_id} on this hub, port HUB_PORT or 8000). In-process P2 hook: relay.feed_audio_hook = fn(call_id, frame_dict).
Fail open: connection errors are logged and dropped; queues are bounded (full -> drop frame)."""
import asyncio, json, logging, os, time
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

log = logging.getLogger("hub.relay")
router = APIRouter()
feed_audio_hook = None
QMAX = 200
SAMPLE = 50  # latency sampled every Nth media frame (keeps latency.jsonl small)
_S: dict = {}

def _lat(metric, call_id, ms):
    try:
        from . import ops
        ops._rec(metric, call_id, ms)
    except Exception:
        pass

class _Session:
    def __init__(self, call_id, send, on_lost):
        self.call_id, self.send, self.on_lost = call_id, send, on_lost
        self.p2_q = asyncio.Queue(QMAX); self.header = []; self.stream_id = None; self.p2_retry = 0.0
        self.p2_task = asyncio.create_task(_p2_pump(self))
        self.decoy_active = False; self.d_ws = None; self.d_q = None; self.d_tasks = []
        self.n = 0; self.sent_t = {}; self.dropped = 0

def _put(q, item, s):
    try:
        q.put_nowait(item)
    except asyncio.QueueFull:
        s.dropped += 1

def _url(env, path, default=None):
    """<ENV> (ws URL) or fall back to the pipeline's P2_BASE/P3_BASE (http(s) -> ws(s)), same vars /demo/status probes."""
    base = os.environ.get(env) or os.environ.get(env.replace("_STT_URL", "_BASE").replace("_DECOY_URL", "_BASE"))
    if base and base.startswith("http"):
        base = base.replace("http", "ws", 1)
    return f"{base.rstrip('/')}{path}" if base else default

async def open(call_id, send_to_caller, on_decoy_lost=None):
    try:
        if call_id in _S:
            await close(call_id)
        _S[call_id] = _Session(call_id, send_to_caller, on_decoy_lost)
    except Exception:
        log.exception("relay.open failed")

async def caller_frame(call_id, frame):
    try:
        s = _S.get(call_id)
        if s is None:
            return
        if isinstance(frame, (str, bytes)):
            frame = json.loads(frame)
        ev = frame.get("event")
        if ev == "media" and (frame.get("media") or {}).get("track") not in (None, "inbound"):
            return  # only the caller's inbound track may enter; anything else (e.g. outbound/Maria) is dropped
        if ev in ("connected", "start"):
            s.header = [h for h in s.header if h.get("event") != ev] + [frame]
            if ev == "start":
                s.stream_id = frame.get("stream_id") or (frame.get("start") or {}).get("stream_id")
        if feed_audio_hook:
            try: feed_audio_hook(call_id, frame)
            except Exception: log.exception("feed_audio_hook failed")
        if os.environ.get("P2_STT_URL") or os.environ.get("P2_BASE"):
            _put(s.p2_q, frame, s)
        if s.decoy_active and ev in ("media", "stop"):
            if ev == "media":
                s.n += 1
                if s.n % SAMPLE == 1: s.sent_t["t"] = time.time()
            _put(s.d_q, frame, s)
    except Exception:
        log.exception("relay.caller_frame failed")

async def _p2_pump(s):
    import websockets
    ws = None; skip = set()
    try:
        while True:
            frame = await s.p2_q.get()
            if frame is None:
                break
            if frame.get("event") in skip:  # already sent as part of the header replay
                skip.discard(frame["event"]); continue
            if ws is None:
                if time.time() < s.p2_retry:
                    continue
                url = _url("P2_STT_URL", f"/stt/{s.call_id}")
                try:
                    ws = await asyncio.wait_for(websockets.connect(url), 2)
                    for h in s.header:  # late connect: replay connected/start so P2 sees the stream header
                        await ws.send(json.dumps(h)); skip.add(h["event"])
                    if frame.get("event") in skip:
                        skip.discard(frame["event"]); continue
                except Exception as e:
                    log.warning("P2 connect failed (%s); dropping, retry in 5s", type(e).__name__)
                    ws = None; s.p2_retry = time.time() + 5; continue
            try:
                t0 = time.time()
                await asyncio.wait_for(ws.send(json.dumps(frame)), 1)
                if frame.get("event") == "media":
                    if int(frame["media"].get("chunk", 0) or 0) % SAMPLE == 1:
                        _lat("relay_p2_send_ms", s.call_id, (time.time() - t0) * 1000)
            except Exception as e:
                log.warning("P2 send failed (%s)", type(e).__name__)
                try: await ws.close()
                except Exception: pass
                ws = None; s.p2_retry = time.time() + 5
    except asyncio.CancelledError:
        pass
    except Exception:
        log.exception("p2 pump crashed")
    finally:
        if ws is not None:
            try: await ws.close()
            except Exception: pass

async def start_decoy(call_id):
    s = _S.get(call_id)
    if s is None:
        return False
    if s.decoy_active:
        return True
    import websockets
    port = os.environ.get("HUB_PORT", "8000")
    url = _url("P3_DECOY_URL", f"/decoy/{call_id}", f"ws://127.0.0.1:{port}/decoy-echo/{call_id}")
    try:
        ws = await asyncio.wait_for(websockets.connect(url), 3)
        sid = s.stream_id or "relay-" + call_id
        await ws.send(json.dumps({"event": "connected", "protocol": "Call", "version": "1.0.0"}))
        await ws.send(json.dumps({"event": "start", "sequence_number": "1", "stream_id": sid,
            "start": {"call_session_id": call_id, "stream_id": sid, "custom_parameters": {"call_id": call_id},
                      "media_format": {"encoding": "audio/x-mulaw", "sample_rate": 8000, "channels": 1}}}))
    except Exception as e:
        log.warning("P3 decoy connect failed (%s); decoy not started", type(e).__name__)
        return False
    s.d_ws, s.d_q, s.n = ws, asyncio.Queue(QMAX), 0
    s.decoy_active = True
    s.d_tasks = [asyncio.create_task(_d_send(s)), asyncio.create_task(_d_recv(s))]
    return True

async def _d_send(s):
    try:
        while True:
            frame = await s.d_q.get()
            if frame is None:
                return
            await asyncio.wait_for(s.d_ws.send(json.dumps(frame)), 1)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        log.warning("P3 send failed (%s)", type(e).__name__)
        await _lost(s)

async def _d_recv(s):
    try:
        async for msg in s.d_ws:
            try:
                f = json.loads(msg)
            except ValueError:
                continue
            ev = f.get("event")
            if ev not in ("media", "clear", "mark"):
                continue
            if ev == "media" and "t" in s.sent_t:
                _lat("relay_decoy_rtt_ms", s.call_id, (time.time() - s.sent_t.pop("t")) * 1000)
            try:
                await asyncio.wait_for(s.send(f), 1)
            except Exception as e:
                log.warning("send_to_caller failed (%s)", type(e).__name__)
        await _lost(s)  # P3 closed
    except asyncio.CancelledError:
        pass
    except Exception as e:
        log.warning("P3 recv failed (%s)", type(e).__name__)
        await _lost(s)

async def _lost(s):
    if not s.decoy_active:
        return
    s.decoy_active = False
    log.warning("decoy lost for %s; caller stream unaffected", s.call_id)
    if s.on_lost:
        try:
            r = s.on_lost(s.call_id)
            if asyncio.iscoroutine(r): await r
        except Exception:
            log.exception("on_decoy_lost failed")

async def stop_decoy(call_id):
    try:
        s = _S.get(call_id)
        if s is None or s.d_ws is None:
            return
        s.decoy_active = False
        for t in s.d_tasks:
            if t is not asyncio.current_task(): t.cancel()
        try:
            await asyncio.wait_for(s.d_ws.send(json.dumps({"event": "stop", "stream_id": s.stream_id or "relay-" + call_id})), 1)
            await s.d_ws.close()
        except Exception:
            pass
        s.d_ws = None; s.d_tasks = []
    except Exception:
        log.exception("relay.stop_decoy failed")

async def close(call_id):
    try:
        await stop_decoy(call_id)
        s = _S.pop(call_id, None)
        if s:
            _put(s.p2_q, None, s)
            try: await asyncio.wait_for(s.p2_task, 2)
            except Exception: s.p2_task.cancel()
    except Exception:
        log.exception("relay.close failed")

def stats(call_id):
    s = _S.get(call_id)
    return None if s is None else {"decoy_active": s.decoy_active, "dropped": s.dropped}

@router.websocket("/decoy-echo/{call_id}")
async def decoy_echo(ws: WebSocket, call_id: str):
    """Built-in test decoy: echoes caller media back as decoy audio. SIMULATED; replaced by P3."""
    await ws.accept()
    try:
        while True:
            m = json.loads(await ws.receive_text())
            if m.get("event") == "media":
                await ws.send_text(json.dumps({"event": "media", "media": {"payload": m["media"]["payload"]}}))
    except (WebSocketDisconnect, ValueError):
        pass
