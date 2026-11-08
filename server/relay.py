"""TASK-013: hub side of the one-stream media relay (Option A). Caller-leg frames only; Maria's audio never enters.
voip/ (eng2) owns the Telnyx WS and calls (all async, none ever raises, none blocks on P2/P3):
  await relay.open(call_id, send_to_caller, on_decoy_lost=None)   send_to_caller(frame: dict) writes a Telnyx media/clear/mark frame to the Telnyx WS
  await relay.caller_frame(call_id, frame)    every Telnyx frame (connected/start/media/stop), dict or JSON str
  await relay.start_decoy(call_id) -> bool    connect to P3, send connected+start, then relay both ways
  await relay.stop_decoy(call_id); await relay.close(call_id)
Env: P2_STT_URL (e.g. ws://host:port -> WS /stt/{call_id}), P3_DECOY_URL (e.g. wss://host -> WSS /decoy/{call_id}; unset -> built-in
stand-in persona /decoy-standin/{call_id} (voip/persona.py) on this hub, port HUB_PORT or 8000; DECOY_STANDIN=echo -> /decoy-echo/{call_id}). In-process P2 hook: relay.feed_audio_hook = fn(call_id, frame_dict).
Fail open: connection errors are logged and dropped; queues are bounded (full -> drop frame)."""
import asyncio, json, logging, os, pathlib, time
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

P2_RETRY_S = float(os.environ.get("P2_RETRY_S", "2"))     # reconnect spacing while P2 is down during a call
P2_FAST_TRIES = int(os.environ.get("P2_FAST_TRIES", "3"))  # consecutive failed connects at P2_RETRY_S before slowing to P2_SLOW_S
P2_SLOW_S = float(os.environ.get("P2_SLOW_S", "10"))

class _Session:
    def __init__(self, call_id, send, on_lost):
        self.call_id, self.send, self.on_lost = call_id, send, on_lost
        self.p2_q = asyncio.Queue(QMAX); self.header = []; self.stream_id = None; self.p2_retry = 0.0; self.p2_fail = 0
        self.p2_task = asyncio.create_task(_p2_pump(self))
        self.decoy_active = False; self.d_ws = None; self.d_q = None; self.d_tasks = []
        self.n = 0; self.sent_t = {}; self.dropped = 0; self.t_act = time.time()

# --- WS /listen/{call_id}: judges hear the caller + decoy audio in the phone-free demo. Caller inbound track and decoy->caller frames only
# (Maria's audio never enters the relay). Text frames: {"track":"caller"|"decoy","payload": PCMU 8k base64} (20 ms each).
MAX_LISTENERS = 3
LISTEN_IDLE_S = 300   # no frames for 5 min -> listener closed
_LQ: dict = {}   # call_id -> set of per-listener bounded queues

def _fan(call_id, track, frame):
    qs = _LQ.get(call_id)
    if not qs:
        return
    payload = (frame.get("media") or {}).get("payload")
    if not payload:
        return
    msg = json.dumps({"track": track, "payload": payload})
    for q in list(qs):
        try: q.put_nowait(msg)
        except asyncio.QueueFull: pass   # slow listener: drop the frame; the listener loop closes it if its socket stalls

def active_calls():
    """Live calls with an open media session (relay.open ran, relay.close has not): ([call_id...], last_activity_ts or None). Used by the restart guard."""
    ids = list(_S.keys())
    return ids, (max((x.t_act for x in _S.values()), default=None))

def listener_count():
    return sum(len(v) for v in _LQ.values())

def _put(q, item, s):
    try:
        q.put_nowait(item)
    except asyncio.QueueFull:
        s.dropped += 1

def p2_tunnel_origin():
    """F9: P2 behind a quick tunnel changes URL on every restart. If $LOGDIR/p2_tunnel_url.txt exists (first line: https://host or wss://host), it
    overrides P2_STT_URL / P2_BASE, re-read on every connect attempt (no hub restart). Returns 'https://host[:port]' / 'http://...' or None.
    Only scheme+host are kept (path/query/credentials in the file are ignored/rejected)."""
    from urllib.parse import urlsplit
    try:
        f = pathlib.Path(os.environ.get("LOGDIR") or "logs") / "p2_tunnel_url.txt"
        if not f.is_file():
            return None
        line = (f.read_text().strip().splitlines() or [""])[0].strip()
        sp = urlsplit(line)
        if sp.scheme not in ("https", "http", "wss", "ws") or not sp.hostname or sp.username or sp.password:
            log.warning("p2_tunnel_url.txt ignored: not a plain http(s)/ws(s) host URL")
            return None
        return f"{'https' if sp.scheme in ('https', 'wss') else 'http'}://{sp.netloc}"
    except Exception:
        return None

def _url(env, path, default=None):
    """<ENV> (ws URL) or fall back to the pipeline's P2_BASE/P3_BASE (http(s) -> ws(s)), same vars /demo/status probes."""
    base = (p2_tunnel_origin() if env == "P2_STT_URL" else None) or os.environ.get(env) or os.environ.get(env.replace("_STT_URL", "_BASE").replace("_DECOY_URL", "_BASE"))
    if base and base.startswith("http"):
        base = base.replace("http", "ws", 1)
    return f"{base.rstrip('/')}{path}" if base else default

async def _connect_p2(url):
    """Open WS /stt/{call_id} on P2. When PIPELINE_TOKEN is set it goes ONLY in the x-pipeline-token header (never in the URL: URLs
    land in proxy/tunnel logs) and never over plaintext ws:// to a non-loopback host. Either failure raises, so the relay treats P2 as
    unreachable (call still connects, fail open). The token is never logged."""
    import inspect, websockets
    from urllib.parse import urlsplit
    tok = os.environ.get("PIPELINE_TOKEN")
    if not tok:
        return await websockets.connect(url)
    sp = urlsplit(url)
    if sp.scheme == "ws" and sp.hostname not in ("127.0.0.1", "localhost", "::1"):
        raise ConnectionError("refusing to send PIPELINE_TOKEN over plaintext ws:// to a non-loopback host; use wss://")
    params = inspect.signature(websockets.connect).parameters
    kw = "additional_headers" if "additional_headers" in params else "extra_headers" if "extra_headers" in params else None
    if kw is None:
        raise ConnectionError("this websockets build cannot set headers; not sending PIPELINE_TOKEN in the URL")
    return await websockets.connect(url, **{kw: {"x-pipeline-token": tok}})

async def open(call_id, send_to_caller, on_decoy_lost=None):
    """Open the relay session for a call and RETURN it. A media-WS reconnect replaces the old session (F19): the old one is shut down but
    the /listen sockets stay attached. Pass the returned session to close(call_id, session) so a stale socket's cleanup cannot close the new one."""
    try:
        old = _S.get(call_id)
        s = _Session(call_id, send_to_caller, on_decoy_lost)
        _S[call_id] = s                       # new session owns the call from here on, before any await
        if old is not None:
            await _shutdown(old, release_listeners=False)
            log.warning("relay session for %s replaced by a reconnect", call_id[:8])
        return s
    except Exception:
        log.exception("relay.open failed")

def _routed_normal(call_id) -> bool:
    try:
        from . import bus
        c = bus.CALLS.get(call_id)
        return bool(c and c.get("trusted"))
    except Exception:
        return False

async def caller_frame(call_id, frame):
    try:
        s = _S.get(call_id)
        if s is None:
            return
        s.t_act = time.time()
        if isinstance(frame, (str, bytes)):
            frame = json.loads(frame)
        ev = frame.get("event")
        if ev == "media" and (frame.get("media") or {}).get("track") not in (None, "inbound"):
            return  # only the caller's inbound track may enter; anything else (e.g. outbound/Maria) is dropped
        if ev in ("connected", "start"):
            s.header = [h for h in s.header if h.get("event") != ev] + [frame]
            if ev == "start":
                s.stream_id = frame.get("stream_id") or (frame.get("start") or {}).get("stream_id")
        if ev == "media":
            _fan(call_id, "caller", frame)
        normal = _routed_normal(call_id)   # F7: trusted (+A) / fail-open NORMAL calls are streamed for /listen but never scored or sent to P2
        if feed_audio_hook and not normal:
            try: feed_audio_hook(call_id, frame)
            except Exception: log.exception("feed_audio_hook failed")
        if not normal and (os.environ.get("P2_STT_URL") or os.environ.get("P2_BASE") or p2_tunnel_origin()):
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
    ws = None; skip = set(); sent = 0; ever = False   # sent/ever feed the per-call connect/close log (warning level so uvicorn shows it)
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
                    ws = await asyncio.wait_for(_connect_p2(url), 2)
                    for h in s.header:  # late connect: replay connected/start so P2 sees the stream header
                        await ws.send(json.dumps(h)); skip.add(h["event"]); sent += 1
                    ever = True
                    log.warning("P2 connected call=%s%s", s.call_id[:8], f" after {s.p2_fail} failed attempt(s)" if s.p2_fail else "")
                    s.p2_fail = 0
                    if frame.get("event") in skip:
                        skip.discard(frame["event"]); continue
                except Exception as e:
                    s.p2_fail += 1
                    wait = P2_RETRY_S if s.p2_fail <= P2_FAST_TRIES else P2_SLOW_S   # 3 quick retries 2 s apart, then a slow heartbeat (never give up for the call)
                    log.warning("P2 connect failed (%s) call=%s attempt=%d; frames dropped, retry in %ds", type(e).__name__, s.call_id[:8], s.p2_fail, wait)
                    ws = None; s.p2_retry = time.time() + wait; continue
            try:
                t0 = time.time()
                await asyncio.wait_for(ws.send(json.dumps(frame)), 1)
                sent += 1
                if frame.get("event") == "media":
                    if int(frame["media"].get("chunk", 0) or 0) % SAMPLE == 1:
                        _lat("relay_p2_send_ms", s.call_id, (time.time() - t0) * 1000)
            except Exception as e:
                log.warning("P2 send failed (%s)", type(e).__name__)
                try: await ws.close()
                except Exception: pass
                ws = None; s.p2_retry = time.time() + P2_RETRY_S
    except asyncio.CancelledError:
        pass
    except Exception:
        log.exception("p2 pump crashed")
    finally:
        log.warning("P2 closed call=%s frames_sent=%d connected=%s", s.call_id[:8], sent, ever)   # also when it never connected: frames_sent=0 connected=False
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
    _kind = "echo" if os.environ.get("DECOY_STANDIN", "persona").strip().lower() == "echo" else "standin"
    standin = f"ws://127.0.0.1:{port}/decoy-{_kind}/{call_id}"
    url = _url("P3_DECOY_URL", f"/decoy/{call_id}", standin)
    try:
        try:
            ws = await asyncio.wait_for(websockets.connect(url), 3)
        except Exception as e:
            if url == standin: raise
            log.warning("P3 decoy connect failed (%s); falling back to the built-in stand-in persona", type(e).__name__)   # F3: the tap still gives the caller a decoy
            ws = await asyncio.wait_for(websockets.connect(standin), 3)
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
            if ev == "media":
                _fan(s.call_id, "decoy", f)
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

async def _shutdown(s, release_listeners=True):
    """Stop a session's decoy and P2 pump; optionally release its /listen sockets."""
    try:
        if s.d_ws is not None:
            s.decoy_active = False
            for t in s.d_tasks:
                if t is not asyncio.current_task(): t.cancel()
            try:
                await asyncio.wait_for(s.d_ws.send(json.dumps({"event": "stop", "stream_id": s.stream_id or "relay-" + s.call_id})), 1)
                await s.d_ws.close()
            except Exception:
                pass
            s.d_ws = None; s.d_tasks = []
        if release_listeners:
            for lq in list(_LQ.get(s.call_id, ())):      # end of call: release the listeners' slots
                try: lq.put_nowait(None)
                except asyncio.QueueFull: pass
        _put(s.p2_q, None, s)
        try: await asyncio.wait_for(s.p2_task, 2)
        except Exception: s.p2_task.cancel()
    except Exception:
        log.exception("relay.close failed")

async def close(call_id, session=None):
    """End the call's relay session. With `session` (the object open() returned) this is a no-op unless it is still the CURRENT session,
    so a replaced media WS cleaning up late cannot kill its successor (F19). Without it: legacy behaviour, closes whatever is current."""
    try:
        cur = _S.get(call_id)
        if session is not None and cur is not session:
            log.warning("relay.close for %s ignored: session was replaced by a newer connection", call_id[:8])
            return
        s = _S.pop(call_id, None)
        if s is None:
            for lq in list(_LQ.get(call_id, ())):
                try: lq.put_nowait(None)
                except asyncio.QueueFull: pass
            return
        await _shutdown(s)
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


def _same_origin_or_none(ws: WebSocket) -> bool:
    """Loopback bypass only for non-browser clients (no Origin) or a page served by this hub (Origin host == Host header, and Host is a
    loopback name). Blocks cross-site WebSocket hijacking from a malicious page in the operator's browser, and DNS rebinding."""
    from urllib.parse import urlsplit
    host = ws.headers.get("host", "")
    hn = urlsplit("//" + host).hostname or ""
    if hn not in ("127.0.0.1", "localhost", "::1"):
        return False
    origin = ws.headers.get("origin")
    return origin is None or urlsplit(origin).netloc.lower() == host.lower()

def _known_call(call_id) -> bool:
    """Only listen to calls the hub knows: a live relay session, or a call_id seen on the event bus (listener may attach at call.incoming, before the media stream opens)."""
    if call_id in _S:
        return True
    try:
        from . import bus
        return call_id in bus.CALLS or any(e.get("call_id") == call_id for e in bus.history)
    except Exception:
        return False

def _identity(ws: WebSocket) -> str:
    """Who is connecting, for replace-on-reconnect: a paired device token (hashed), the hub token, or the local console. Never logs the token."""
    import hashlib
    from . import device
    protos = [p.strip() for p in ws.headers.get("sec-websocket-protocol", "").split(",") if p.strip()]
    for t in [ws.headers.get("x-device-token")] + [p for p in protos if p != "bf-device"]:
        if t and device._valid(t):
            return "dev:" + hashlib.sha256(t.encode()).hexdigest()[:10]
    if device.is_direct_local(ws):
        return "local"
    return "hub"

_LIDENT: dict = {}    # id(queue) -> (ident, ws) for each live /listen socket

async def _replace_listeners(call_id, ident, kind):
    """A reconnect from the same device replaces its old /listen sockets for this call (frees the slot at once)."""
    for q in list(_LQ.get(call_id, ())):
        ident0, ws0 = _LIDENT.get(id(q), (None, None))
        if ident0 == ident and ident.startswith("dev:"):   # only a paired device replaces itself; local/hub tabs are separate listeners (cap applies)
            _LQ[call_id].discard(q); _LIDENT.pop(id(q), None)
            try: q.put_nowait(None)
            except Exception: pass
            try: await ws0.close(1000)
            except Exception: pass
            log.warning("%s %s: replaced by a new connection from the same device", kind, call_id[:8])

def device_holds_slot(call_id, token) -> bool:
    """True when the paired device with this token currently holds a /talk or /listen socket for the call (used to bind device events to a live participant)."""
    import hashlib
    if not token:
        return False
    ident = "dev:" + hashlib.sha256(token.encode()).hexdigest()[:10]
    t = _TALKERS.get(call_id)
    if t is not None and t[0] == ident:
        return True
    return any(_LIDENT.get(id(q), (None,))[0] == ident for q in _LQ.get(call_id, ()))

def _listen_authorized(ws: WebSocket):
    """Direct loopback (no token needed), x-hub-token == HUB_TOKEN, or a paired device token. Browsers can't set headers and the token must
    not be in the URL, so the client opens new WebSocket(url, ['bf-device', <token>]): Sec-WebSocket-Protocol 'bf-device, <token>'.
    Returns (ok, subprotocol_to_accept_with)."""
    import secrets
    from . import device
    protos = [p.strip() for p in ws.headers.get("sec-websocket-protocol", "").split(",") if p.strip()]
    sub = "bf-device" if "bf-device" in protos else None
    if device.is_direct_local(ws) and _same_origin_or_none(ws):
        return True, sub
    hub = os.environ.get("HUB_TOKEN")
    if hub and secrets.compare_digest(ws.headers.get("x-hub-token", ""), hub):
        return True, sub
    if device._valid(ws.headers.get("x-device-token")):
        return True, sub
    if sub and any(device._valid(p) for p in protos if p != "bf-device"):
        return True, sub
    return False, None

# --- WS /talk/{call_id}: two-way Maria for role-play demos. One talker per call; her PCMU goes ONLY to voip's uplink injector
# (voip.router.maria_uplink(call_id, pcmu_bytes)), never to P2/P3, never stored or logged. Dropped while the decoy is on the line.
TALK_FPS = 60
_TALKERS: dict = {}   # call_id -> (ident, ws)

def _decoy_on(call_id) -> bool:
    s = _S.get(call_id)
    if s is not None and s.decoy_active:
        return True
    try:
        from . import bus
        c = bus.CALLS.get(call_id)
        return bool(c and c["handoff"] == "started" and not c["ended"])
    except Exception:
        return False

def _call_ended(call_id) -> bool:
    try:
        from . import bus
        c = bus.CALLS.get(call_id)
        return bool(c and c["ended"])
    except Exception:
        return False

def _voip():
    try:
        from voip import router as vr
        return vr if hasattr(vr, "inject_maria") and hasattr(vr, "talk_enabled") else None
    except Exception:
        return None

@router.websocket("/talk/{call_id}")
async def talk(ws: WebSocket, call_id: str):
    import re, base64, binascii
    ok, proto = _listen_authorized(ws)
    V = _voip()
    try:
        enabled = bool(V and V.talk_enabled(call_id))
    except Exception:
        enabled = False
    if not ok or not re.fullmatch(r"[A-Za-z0-9_.:-]{1,80}", call_id) or not _known_call(call_id) or not enabled:
        await ws.close(code=1008); return
    ident = _identity(ws)
    old = _TALKERS.get(call_id)
    if old is not None:
        if old[0] != ident:
            log.warning("talk %s refused: another device is already talking", call_id[:8])
            await ws.close(code=1013); return        # one talker per call, and it is not you
    _TALKERS[call_id] = (ident, ws)                  # claim the slot BEFORE any await (no window for another device to slip in)
    if old is not None:                              # same device reconnecting: its old socket is replaced
        try: await old[1].close(1000)
        except Exception: pass
        log.warning("talk %s: replaced the old socket from the same device", call_id[:8])
    sent = dropped = 0
    reason = "client closed"
    try:
        await ws.accept(subprotocol=proto)
        log.warning("talk %s accepted (%s)", call_id[:8], ident)
        tokens, last, n = float(TALK_FPS), time.monotonic(), 0
        while True:
            try:
                m = await asyncio.wait_for(ws.receive(), LISTEN_IDLE_S)
            except asyncio.TimeoutError:
                reason = "idle timeout"; break
            if m.get("type") == "websocket.disconnect":
                break
            b64 = None
            if m.get("bytes") is not None:
                b64 = base64.b64encode(m["bytes"]).decode() if len(m["bytes"]) % 160 == 0 else None
            elif m.get("text") is not None:
                try:
                    jm = json.loads(m["text"])
                    if isinstance(jm, dict) and "diag" in jm:   # P1 09:20: the page's mic state (no audio), for silent-call diagnosis
                        log.warning("talk %s diag: %s", call_id[:8], json.dumps(jm["diag"])[:300]); continue
                    b64 = jm["payload"]
                    raw = base64.b64decode(b64, validate=True)
                    if not raw or len(raw) % 160 or len(raw) > 960: b64 = None
                except (ValueError, KeyError, TypeError, binascii.Error):
                    b64 = None
            n += 1
            if n % 25 == 0 and _call_ended(call_id):
                reason = "call ended"; break
            frames = max(1, len(base64.b64decode(b64)) // 160) if b64 else 1
            now = time.monotonic()
            tokens = min(float(TALK_FPS), tokens + (now - last) * TALK_FPS); last = now
            if b64 is None or tokens < frames or _decoy_on(call_id):
                dropped += 1; continue                 # bad frame, over 60 frames/s, or the decoy has the call: drop
            tokens -= frames
            try:
                if await V.inject_maria(call_id, b64): sent += 1
                else: dropped += 1                     # voip dropped it (muted by decoy / stream not ready): just continue
            except Exception:
                dropped += 1                           # fail open: never raises into the call
    except Exception:
        reason = "socket error"
    finally:
        if _TALKERS.get(call_id, (None, None))[1] is ws:   # a replacement may already own the slot
            _TALKERS.pop(call_id, None)
        log.warning("talk %s closed (%s): msgs_sent=%d dropped=%d", call_id[:8], reason, sent, dropped)


@router.websocket("/listen/{call_id}")
async def listen(ws: WebSocket, call_id: str):
    import re
    ok, proto = _listen_authorized(ws)
    if not ok or not re.fullmatch(r"[A-Za-z0-9_.:-]{1,80}", call_id) or not _known_call(call_id):
        await ws.close(code=1008); return
    ident = _identity(ws)
    await _replace_listeners(call_id, ident, "listen")
    if listener_count() >= MAX_LISTENERS:
        log.warning("listen %s refused: %d listeners already (max %d)", call_id[:8], listener_count(), MAX_LISTENERS)
        await ws.close(code=1013); return          # try again later: at most 3 listeners
    q = asyncio.Queue(100)
    _LQ.setdefault(call_id, set()).add(q); _LIDENT[id(q)] = (ident, ws)
    reason = "client closed"
    try:
        await ws.accept(subprotocol=proto)
        log.warning("listen %s accepted (%s)", call_id[:8], ident)
        async def _drain():                         # notice the browser going away
            try:
                while True: await ws.receive_text()
            except Exception: pass
        gone = asyncio.create_task(_drain())
        try:
            idle = time.time()
            while not gone.done():
                try: msg = await asyncio.wait_for(q.get(), 0.5)
                except asyncio.TimeoutError:
                    if time.time() - idle > LISTEN_IDLE_S: reason = "idle timeout"; break      # a stale listener must not hold one of the 3 slots forever
                    continue
                if msg is None: reason = "call ended or replaced"; break                                  # call/relay session closed
                idle = time.time()
                await asyncio.wait_for(ws.send_text(msg), 1)   # a listener that cannot take a frame within 1 s is dropped
        finally:
            gone.cancel()
    except Exception:
        pass
    finally:
        _LQ.get(call_id, set()).discard(q); _LIDENT.pop(id(q), None)
        if not _LQ.get(call_id): _LQ.pop(call_id, None)
        log.warning("listen %s closed (%s)", call_id[:8], reason)
