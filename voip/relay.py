"""Fan-out of caller-track Telnyx stream frames to sinks (P2 STT now; P3 decoy in TASK-008).
Sinks run on bounded queues: a slow/broken sink drops frames, never blocks the call (fail open)."""
import asyncio, json, logging, os
log = logging.getLogger("voip.relay")

class Sink:
    def __init__(self, name, send, maxsize=200):
        self.name, self.send, self.q, self.dead, self.task = name, send, asyncio.Queue(maxsize), False, None
    def start(self): self.task = asyncio.create_task(self._run())
    async def _run(self):
        try:
            while True:
                msg = await self.q.get()
                if msg is None: break
                await self.send(msg)
        except Exception as e:
            self.dead = True; log.warning("sink %s died: %s", self.name, e)
    def offer(self, msg):
        if self.dead: return
        if self.q.full():
            try: self.q.get_nowait()
            except asyncio.QueueEmpty: pass
        self.q.put_nowait(msg)
    async def close(self):
        if self.task:
            try: self.q.put_nowait(None)
            except asyncio.QueueFull: self.task.cancel()

class Relay:
    def __init__(self): self.sinks: dict[str, Sink] = {}
    def add(self, sink: Sink): self.sinks[sink.name] = sink; sink.start()
    def remove(self, name):
        s = self.sinks.pop(name, None)
        return s
    def feed(self, raw_text: str):
        for s in list(self.sinks.values()): s.offer(raw_text)
    async def close(self):
        for s in list(self.sinks.values()): await s.close()
        self.sinks.clear()

def p2_ws_url(call_id: str, base: str | None = None) -> str | None:
    base = base or os.environ.get("P2_BASE")
    if not base: return None
    return base.replace("http", "ws", 1).rstrip("/") + f"/stt/{call_id}"

async def make_p2_sink(call_id: str) -> Sink | None:
    """Caller frames only, forwarded verbatim to P2 WS /stt/{call_id}. None if P2_BASE unset."""
    url = p2_ws_url(call_id)
    if not url: return None
    import websockets
    ws = await websockets.connect(url, open_timeout=3)
    async def send(msg): await ws.send(msg)
    s = Sink("p2", send)
    orig = s.close
    async def close():
        await orig()
        try: await ws.close()
        except Exception: pass
    s.close = close
    return s
