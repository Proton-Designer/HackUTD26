"""Per-call alert state machine (code, not an LLM). Final caller utterance -> detect() -> risk.update; alert.fired decisions.
Rules: first alert once when s>=ALERT_S, or a hard ask with s>=HARD_ASK_S. After user.action=continue: ONE realert per rise, only when
band newly reaches critical or a NEW hard ask appears; must drop below 0.80 before another. Never continuous. No auto handoff.
Quiet switch-off after QUIET_S of s<0.40 (only if no alert fired on the call). Fail open: nothing raises."""
import asyncio, logging, os, time
from collections import deque
from . import health, hub, stream, schema
from .detect import quick, ENGINE_FAILED

log = logging.getLogger("p2.alert")
ALERT_S = float(os.environ.get("ALERT_S", "0.80"))
HARD_ASK_S = float(os.environ.get("HARD_ASK_S", "0.60"))   # decision: a hard ask plus moderate risk alerts early (hard asks are rarely innocent)
REARM_BELOW = 0.80
QUIET_S = float(os.environ.get("QUIET_S", "180"))
WINDOW_N, WINDOW_S = 6, 60.0
ALERT_RETRY_S = float(os.environ.get("P2_ALERT_RETRY_S", "20")); ALERT_RETRY_EVERY_S = float(os.environ.get("P2_ALERT_RETRY_EVERY_S", "1.0"))
HOLD_S, HOLD_N = 10.0, 3     # engine-failed (rules-only) window: hold last LLM-backed s for <=10 s / 3 windows, then decay

class Call:
    def __init__(self):
        self.utts = deque()          # (t, text)
        self.busy = False; self.dirty = False
        self.fired = False; self.continued = False; self.armed = False
        self.prev_band = "low"; self.known_hard = set()
        self.decoy = False; self.muted = False; self.normal_since = None
        self.last = None
        self.llm = None; self.llm_t = 0.0; self.fail_n = 0; self.clean_n = 0; self.epoch = 0; self.seq = 0; self.emit_seq = 0; self.cont_t = 0.0; self.src = "llm"     # last LLM-backed result, its time, consecutive failed windows

class AlertMachine:
    def __init__(self, emit=None, detect=None, clock=time.time, engine=None):
        self.emit = emit or hub.emit
        self._detect = detect
        self.clock = clock
        self.engine = engine or os.environ.get("P2_ENGINE", "cloud")
        self.calls: dict[str, Call] = {}
        self.ended: dict[str, float] = {}      # call_ids the hub said ended: late STT finals/partials must not re-create state or alert (TASK-038)

    async def detect(self, call_id, text, meta):
        if self._detect is None:
            from .detect import detect as d
            self._detect = d
        return await self._detect(call_id, text, meta, self.engine)

    def _call(self, cid):
        return self.calls.setdefault(cid, Call())

    def _mark_ended(self, cid):
        self.calls.pop(cid, None); self.ended[cid] = self.clock()
        while len(self.ended) > 500:
            self.ended.pop(next(iter(self.ended)))

    def _rearm(self, call_id, c, text):
        """TASK-062 F22: a switched-off (muted) call re-arms when ONE line hits the rules fast path (any ask or score >= 0.5). Rules only, no I/O."""
        try:
            q = quick(str(text or ""), self.engine)
            if isinstance(q, dict) and (q.get("asks") or q.get("s", 0) >= 0.5):
                c.muted = False; c.normal_since = None
                log.info("call %s re-armed: rules hit on a switched-off call (s=%.2f asks=%s)", call_id, q.get("s", 0), ",".join(sorted(q.get("asks") or [])) or "-")
                return True
        except Exception:
            log.exception("rearm check failed (ignored)")
        return False

    async def on_partial(self, call_id, utt):
        """Interim text: rules-only fast path on window + partial. Never calls the LLM, never changes window state."""
        try:
            if call_id in self.ended:
                return
            c = self._call(call_id)
            if c.muted and not self._rearm(call_id, c, utt.get("text")):
                return
            te = utt.get("_t_end")
            if te and c.cont_t and te < c.cont_t:
                log.info("drop late partial: audio snapshot before Continue call=%s", call_id); return
            now = self.clock()
            win = [t for ts, t in c.utts if now - ts <= WINDOW_S][-(WINDOW_N - 1):] + [str(utt.get("text", ""))]
            q = quick("\n".join(win), self.engine)
            c.src = "fast-partial"
            if self._decide(c, q):
                log.info("fast-path alert (partial) call=%s s=%.2f", call_id, q["s"])
                await self._process(call_id, c, q)
            if q.get("s", 0) >= 0.5 and q["s"] >= (c.llm or {"s": 0})["s"]:
                c.llm, c.llm_t = q, now          # hold anchor (rules never lower risk)
        except Exception:
            log.exception("on_partial crashed (ignored)")

    async def on_final(self, call_id, utt):
        try:
            if call_id in self.ended:
                log.info("drop final: call already ended call=%s", call_id); return
            c = self._call(call_id)
            if c.muted and not self._rearm(call_id, c, utt.get("text")):
                return
            te = utt.get("_t_end")
            if te and c.cont_t and te < c.cont_t:
                log.info("drop late final: audio ended before Continue call=%s", call_id); return   # STT lag: a pre-Continue utterance must not re-enter the cleared window
            now = self.clock()
            c.utts.append((now, str(utt.get("text", ""))))
            while len(c.utts) > WINDOW_N or (c.utts and now - c.utts[0][0] > WINDOW_S):
                c.utts.popleft()
            c.dirty = True; c.seq += 1; sq0 = c.seq     # window seq: bumped on every append (TASK-046 residual)
            q = quick("\n".join(t for _, t in c.utts), self.engine)      # rules only, no I/O: alert before the LLM returns
            c.src = "fast-final"
            if self._decide(c, q):
                log.info("fast-path alert call=%s s=%.2f", call_id, q["s"])
                await self._process(call_id, c, q, sq0)
            if isinstance(q, dict) and q.get("s", 0) >= (c.llm or {"s": 0})["s"] and q.get("s", 0) >= 0.5:
                c.llm, c.llm_t = q, now          # rule-backed score is a valid hold anchor too (rules never lower risk)
            if c.busy:
                return                       # coalesce: the running loop re-scores the newest window
            c.busy = True
            try:
                while c.dirty and not c.muted:
                    c.dirty = False
                    text = "\n".join(t for _, t in c.utts); ep = c.epoch; sq = c.seq
                    try:
                        r = await self.detect(call_id, text, {"utterances": len(c.utts)})
                    except Exception:
                        log.exception("detect failed (ignored)"); health.err("detect", __import__("sys").exc_info()[1])
                        continue
                    if ep != c.epoch:
                        log.info("drop stale result: Continue arrived mid-flight call=%s", call_id)
                        continue             # Continue arrived mid-flight: this result scored the pre-Continue window, drop it
                    if sq < c.emit_seq:
                        log.info("drop stale result: newer window already emitted call=%s seq=%d<%d", call_id, sq, c.emit_seq)
                        continue             # an older window must not overwrite c.last/prev_band or emit an s dip (checked before _hold so the anchor is untouched too)
                    r = self._floor(r, quick(text, self.engine)); c.src = "llm"
                    await self._process(call_id, c, self._hold(call_id, c, r), sq)
            finally:
                c.busy = False
        except Exception:
            log.exception("on_final crashed (ignored, fail-open)")

    def _hold(self, cid, c, r):
        """An engine-failed window (detect flagged it; NOT 'the LLM said low') must not dip s and re-arm the alert machine:
        keep max(last LLM-backed s, rules s) for HOLD_S / HOLD_N windows, then let it decay. Real low LLM scores pass through."""
        try:
            if not isinstance(r, dict) or not isinstance(r.get("s"), (int, float)):
                return r
            if not ENGINE_FAILED.pop(cid, False):
                c.llm, c.llm_t, c.fail_n, c.clean_n = r, self.clock(), 0, 0
                return r
            c.fail_n += 1
            if r["s"] < 0.2 and not r.get("asks"):   # rules-clean failed window (e.g. normal talk after the scam): hold only the first, so restore is not delayed
                c.clean_n += 1
                if c.clean_n > 1:
                    return r
            if c.llm is None or c.fail_n > HOLD_N or self.clock() - c.llm_t > HOLD_S or c.llm["s"] <= r["s"]:
                return r
            out = dict(r); out["s"] = c.llm["s"]; out["band"] = schema.band(out["s"])
            out["asks"] = [a for a in schema.ASKS if a in set(r.get("asks") or []) | set(c.llm.get("asks") or [])]
            log.info("hold last score call=%s s=%.2f (engine failed, window %d)", cid, out["s"], c.fail_n)
            return out
        except Exception:
            return r

    @staticmethod
    def _floor(r, q):
        """max(quick, llm) for the SAME window only; later windows are scored fresh so s can fall."""
        if not (isinstance(r, dict) and isinstance(r.get("s"), (int, float))) or not isinstance(q, dict) or q.get("s", 0) <= r["s"]:
            return r
        out = dict(r); out["s"] = q["s"]; out["band"] = schema.band(q["s"])
        out["asks"] = [a for a in schema.ASKS if a in set(r.get("asks") or []) | set(q.get("asks") or [])]
        out["why_chips"] = list(dict.fromkeys([*(q.get("why_chips") or []), *(r.get("why_chips") or [])]))[:6]
        return out

    def _decide(self, c, r):
        """Pure: which alert level (if any) this result would fire now."""
        if c.decoy or c.muted or not isinstance(r, dict) or not isinstance(r.get("s"), (int, float)):
            return None
        s = float(r["s"]); hard = set(r.get("asks") or []) & schema.HARD_ASKS
        bnd = r.get("band") or schema.band(s)
        if not c.fired:
            return "first" if (s >= ALERT_S or (hard and s >= HARD_ASK_S)) else None
        if c.continued and c.armed and s >= REARM_BELOW and ((bnd == "critical" and c.prev_band != "critical") or (hard - c.known_hard)):
            return "realert"
        return None

    async def _emit_alert(self, cid, c, level, chips):
        """alert.fired is the one event that must not be lost: if the hub POST fails (hub restarting, TASK-055 drill 3b), retry in the background
        for up to ALERT_RETRY_S while the call is live. hub.emit returns False on failure; other emit callables return None and are not retried."""
        data = {"level": level, "why_chips": chips}
        if await self.emit("alert.fired", cid, data) is not False:
            return
        ep = c.epoch      # Continue / handoff.restored bumps the epoch: the user already acted on this alert, drop the retry
        async def retry():
            t_end = self.clock() + ALERT_RETRY_S
            while self.clock() < t_end and cid not in self.ended and c.epoch == ep:
                await asyncio.sleep(ALERT_RETRY_EVERY_S)
                if cid in self.ended or c.epoch != ep: break
                try:
                    if await self.emit("alert.fired", cid, data) is not False:
                        log.info("alert.fired %s delivered on retry call=%s", level, cid); return
                except Exception:
                    log.exception("alert retry failed (ignored)")
            log.warning("alert.fired %s NOT delivered call=%s", level, cid)
        t = asyncio.get_running_loop().create_task(retry()); stream._bg.add(t); t.add_done_callback(stream._bg.discard)

    async def _process(self, cid, c, r, seq=None):
        """seq = window seq of the scored text (final-based scorings only; interim partials pass None and are neither checked nor recorded)."""
        if cid in self.ended:
            log.info("drop result: call already ended call=%s", cid); return      # in-flight detect landing after call.ended
        if not isinstance(r, dict) or not isinstance(r.get("s"), (int, float)):
            return
        if seq is not None:
            if seq < c.emit_seq:
                log.info("drop stale result: older window call=%s seq=%d<%d", cid, seq, c.emit_seq); return
            c.emit_seq = seq
        s, asks = float(r["s"]), set(r.get("asks") or [])
        hard = asks & schema.HARD_ASKS
        chips = [x for x in (r.get("why_chips") or []) if isinstance(x, str)][:4]
        log.info("risk.update call=%s s=%.2f band=%s engine=%s src=%s asks=%s", cid, s, r.get("band") or schema.band(s), r.get("engine"), c.src, ",".join(sorted(asks)) or "-")
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
                    log.info("alert.fired call=%s level=first src=%s s=%.2f", cid, c.src, s)
                    await self._emit_alert(cid, c, "first", chips)
            elif c.continued:
                if s < REARM_BELOW:
                    c.armed = True
                elif c.armed and ((bnd == "critical" and c.prev_band != "critical") or (hard - c.known_hard)):
                    c.armed = False
                    log.info("alert.fired call=%s level=realert src=%s s=%.2f", cid, c.src, s)
                    await self._emit_alert(cid, c, "realert", chips)
                c.known_hard |= hard
        c.prev_band, c.last = bnd, r

    async def on_event(self, ev):
        try:
            t, cid, d = ev.get("type"), ev.get("call_id"), ev.get("data") or {}
            if not cid:
                return
            if t == "user.action" and d.get("action") == "continue":
                log.info("user.action continue seen call=%s", cid)
                c = self._call(cid)
                c.continued, c.armed = True, True   # prev_band stays: critical must be a NEW transition after Continue
                c.known_hard = set(c.last.get("asks", [])) & schema.HARD_ASKS if c.last else set()
                c.utts.clear(); c.epoch += 1; c.dirty = False; c.cont_t = self.clock(); c.llm, c.llm_t, c.fail_n, c.clean_n = None, 0.0, 0, 0   # also drop the held pre-Continue score (TASK-046 L3); the user saw the alert and chose Continue: score only what is said from now on, so benign talk restores s within a line or two (a new hard ask still fires on its own)
            elif t == "handoff.started":
                self._call(cid).decoy = True
            elif t == "handoff.restored":
                log.info("handoff.restored seen call=%s", cid)
                c = self._call(cid); c.decoy = False; c.fired = False; c.continued = False; c.armed = False
                # restored = judged legit and handed back: like Continue, score only what is said from now on (old scam text must not re-fire 'first'); in-flight results drop (TASK-046 M1)
                c.utts.clear(); c.epoch += 1; c.dirty = False; c.cont_t = self.clock(); c.llm, c.llm_t, c.fail_n, c.clean_n = None, 0.0, 0, 0; c.prev_band = "low"; c.known_hard = set()
            elif t == "call.ended":
                self._mark_ended(cid)     # only the Telnyx caller hangup (call.ended) ends P2 state
            elif t == "user.action" and d.get("action") == "hang_up":
                # TASK-061: the customer's Decline/Hang up tap is not the caller leaving. In listen/talk mode the caller stayed on for 100 s and every final was
                # dropped ("call already ended") while P2 should have kept scoring. Keep state; call.ended is the real end (late finals after it are still dropped, TASK-038).
                log.info("user.action hang_up seen call=%s (ignored: caller leg still counts until call.ended)", cid)
            elif t == "decoy.turn":
                # TASK-058 instrumentation only (local log, no state): lets echo leaks be measured against caller finals
                log.info("echo.decoy call=%s speaker=%s text=%r", cid, d.get("speaker"), str(d.get("text") or "")[:120])
            elif t == "transcript.caller" and d.get("is_final", True):
                log.info("echo.caller call=%s id=%s text=%r", cid, d.get("utterance_id"), str(d.get("text") or "")[:120])
        except Exception:
            log.exception("on_event failed (ignored)")

machine = None

def install(app=None):
    """Create the machine and wire stream.on_final. The hub subscriber runs in lifespan() (app.py passes it to FastAPI)."""
    global machine
    machine = AlertMachine()
    stream.set_on_final(machine.on_final)
    stream.set_on_partial(machine.on_partial)

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
