"""Per-call alert state machine (code, not an LLM). Final caller utterance -> detect() -> risk.update; alert.fired decisions.
Rules: first alert once when s>=ALERT_S, or a hard ask with s>=HARD_ASK_S. After user.action=continue: ONE realert per rise, only when
band newly reaches critical or a NEW hard ask appears; must drop below 0.80 before another. Never continuous. No auto handoff.
Quiet switch-off after QUIET_S of s<0.40 (only if no alert fired on the call). Fail open: nothing raises."""
import asyncio, logging, os, time
from collections import deque
from . import hub, stream, schema

log = logging.getLogger("p2.alert")
ALERT_S = float(os.environ.get("ALERT_S", "0.80"))
HARD_ASK_S = float(os.environ.get("HARD_ASK_S", "0.60"))   # decision: a hard ask plus moderate risk alerts early (hard asks are rarely innocent)
REARM_BELOW = 0.80
QUIET_S = float(os.environ.get("QUIET_S", "180"))
WINDOW_N, WINDOW_S = 6, 60.0

class Call:
    def __init__(self):
        self.utts = deque()          # (t, text)
        self.busy = False; self.dirty = False
        self.fired = False; self.continued = False; self.armed = False
        self.prev_band = "low"; self.known_hard = set()
        self.decoy = False; self.muted = False; self.normal_since = None
        self.last = None

class AlertMachine:
    def __init__(self, emit=None, detect=None, clock=time.time, engine=None):
        self.emit = emit or hub.emit
        self._detect = detect
        self.clock = clock
        self.engine = engine or os.environ.get("P2_ENGINE", "cloud")
        self.calls: dict[str, Call] = {}

    async def detect(self, call_id, text, meta):
        if self._detect is None:
            from .detect import detect as d
            self._detect = d
        return await self._detect(call_id, text, meta, self.engine)

    def _call(self, cid):
        return self.calls.setdefault(cid, Call())

    async def on_final(self, call_id, utt):
        try:
            c = self._call(call_id)
            if c.muted:
                return
            now = self.clock()
            c.utts.append((now, str(utt.get("text", ""))))
            while len(c.utts) > WINDOW_N or (c.utts and now - c.utts[0][0] > WINDOW_S):
                c.utts.popleft()
            c.dirty = True
            if c.busy:
                return                       # coalesce: the running loop re-scores the newest window
            c.busy = True
            try:
                while c.dirty and not c.muted:
                    c.dirty = False
                    text = "\n".join(t for _, t in c.utts)
                    try:
                        r = await self.detect(call_id, text, {"utterances": len(c.utts)})
                    except Exception:
                        log.exception("detect failed (ignored)")
                        continue
                    await self._process(call_id, c, r)
            finally:
                c.busy = False
        except Exception:
            log.exception("on_final crashed (ignored, fail-open)")

    async def _process(self, cid, c, r):
        if not isinstance(r, dict) or not isinstance(r.get("s"), (int, float)):
            return
        s, asks = float(r["s"]), set(r.get("asks") or [])
        hard = asks & schema.HARD_ASKS
        chips = [x for x in (r.get("why_chips") or []) if isinstance(x, str)][:4]
        await self.emit("risk.update", cid, r)
        now, bnd = self.clock(), r.get("band") or schema.band(s)
        # quiet switch-off
        if s < 0.40 and not c.fired and not c.decoy:
            c.normal_since = c.normal_since if c.normal_since is not None else now
            if now - c.normal_since >= QUIET_S:
                c.muted = True
                log.info("call %s clearly normal for %.0fs: detection switched off", cid, QUIET_S)
        else:
            c.normal_since = None
        if not c.decoy:
            if not c.fired:
                if s >= ALERT_S or (hard and s >= HARD_ASK_S):
                    c.fired = True
                    c.known_hard = set(hard)
                    await self.emit("alert.fired", cid, {"level": "first", "why_chips": chips})
            elif c.continued:
                if s < REARM_BELOW:
                    c.armed = True
                elif c.armed and ((bnd == "critical" and c.prev_band != "critical") or (hard - c.known_hard)):
                    c.armed = False
                    await self.emit("alert.fired", cid, {"level": "realert", "why_chips": chips})
                c.known_hard |= hard
        c.prev_band, c.last = bnd, r

    async def on_event(self, ev):
        try:
            t, cid, d = ev.get("type"), ev.get("call_id"), ev.get("data") or {}
            if not cid:
                return
            if t == "user.action" and d.get("action") == "continue":
                c = self._call(cid)
                c.continued, c.armed = True, True   # prev_band stays: critical must be a NEW transition after Continue
                c.known_hard = set(c.last.get("asks", [])) & schema.HARD_ASKS if c.last else set()
            elif t == "handoff.started":
                self._call(cid).decoy = True
            elif t == "handoff.restored":
                c = self._call(cid); c.decoy = False; c.fired = False; c.continued = False; c.armed = False
            elif t in ("call.ended",) or (t == "user.action" and d.get("action") == "hang_up"):
                self.calls.pop(cid, None)
        except Exception:
            log.exception("on_event failed (ignored)")

machine = None

def install(app=None):
    """Create the machine and wire stream.on_final. The hub subscriber runs in lifespan() (app.py passes it to FastAPI)."""
    global machine
    machine = AlertMachine()
    stream.set_on_final(machine.on_final)

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    task = None
    if machine is not None and os.environ.get("P2_NO_HUB_WS") != "1":
        task = asyncio.create_task(hub.subscribe(machine.on_event))
    try:
        yield
    finally:
        if task:
            task.cancel()
