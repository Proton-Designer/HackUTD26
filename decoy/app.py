"""P3 decoy service. Run from the repo root (NVIDIA_API_KEY and HUB_URL in the environment):
    .venv-hub/bin/python -m uvicorn decoy.app:app --host 127.0.0.1 --port 8300
then on the hub: P3_DECOY_URL=ws://127.0.0.1:8300 and P3_VOICE_URL=http://127.0.0.1:8300

WS  /decoy/{call_id}   Telnyx media-streaming frames both ways (contracts/interfaces.md, seam #2): in = connected/start/
                       media(PCMU 8 kHz, caller only)/stop; out = media (decoy voice), clear (barge-in).
POST /voice/enroll     {recording: base64, mime, consent_version} -> {voice_id}; emits voice.enrolled
DELETE /voice/{id}     -> {ok}; emits voice.deleted
Events to the hub (POST /events, PIPELINE_TOKEN): decoy.turn, decoy.fake_value, guardrail.tripped, artifacts.extracted.
Fail open: any error here only ends the decoy; it never touches the call itself.
"""
from __future__ import annotations

import asyncio
import base64
import json
import logging
import random
import time

import numpy as np
from fastapi import Body, Depends, FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect

from . import core, voice

log = logging.getLogger("p3.decoy")
_p3 = logging.getLogger("p3")   # nobody configures logging under uvicorn, so p3 INFO lines (per-turn latency) were dropped
if not _p3.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s", "%H:%M:%S"))
    _p3.addHandler(_h); _p3.setLevel(logging.INFO); _p3.propagate = False
app = FastAPI(title="Backfire P3 decoy")
CAP_S = 20 * 60
# Barge-in (Ayman's real call 93c95fd6: 21 self-clears in 17 s, our own voice echoing back on the PSTN leg).
BARGE_IN_MS = 500          # sustained loud caller audio needed to cut the decoy off
BARGE_GRACE_S = 0.4        # ignore inbound right after we start speaking (echo onset)
ECHO_MARGIN = 3.0          # inbound must be ~10 dB over the estimated echo of our own voice
OUT_RATIO = 0.3            # ...and within ~10 dB of our own outbound level (real echo is far quieter)
STT_TIMEOUT_S, LLM_TIMEOUT_S = 6.0, 7.0
# Turn-taking (Ayman, real call adad65a0: "often speaks out of turn"). P2's 450 ms end-of-speech is tuned for fast
# detection; callers pause longer than that mid-sentence on PSTN, so the decoy waits longer before it takes its turn,
# and holds a ready reply while the caller is still talking (re-thinking if they added something).
DECOY_ENDPOINT_MS = int(__import__("os").environ.get("DECOY_ENDPOINT_MS", "800"))
HOLD_MAX_S = 4.0           # longest we hold a ready reply for a caller who keeps talking
REDO_MAX = 2               # re-think at most twice per turn when the caller adds more
# Polite wrap-up (P1/Ayman, #86 e): once we have how they get paid (handle / site / wallet) plus one more artifact type,
# play along for a few more turns, then say goodbye and close; the hub hangs up the caller (ended_by=decoy).
STRONG_KINDS = {"payment_handle", "domain", "url", "wallet"}
WRAP_TURNS = int(__import__("os").environ.get("DECOY_WRAP_TURNS", "3"))
WRAP_LINE = "Okay, I've got all of that written down. I'm going to go take care of it right now. Bye bye."
FILLER_AFTER_S = 0.6       # play a filler only if Nemotron hasn't answered by then
STALLS = ["Hold on, let me find my glasses.", "Oh, sorry, the line went funny. Say that again?",
          "Sorry, can you repeat that? I was writing.", "Wait, wait, slow down a little for me.",
          "Hmm, hang on, I dropped my pen.", "Sorry, it's a bit noisy here. What was that last part?",
          "One second, let me get a piece of paper.", "Okay, okay. And then what do I do?"]
LLM_RETRY_WITHIN_S = 3.0   # a fast failure (e.g. 429) gets one retry after a short backoff before we stall (#92)


PROXY_HEADERS = ("cf-connecting-ip", "cf-ray", "x-forwarded-for", "x-forwarded-host", "forwarded", "x-real-ip")


def allowed(host: str | None, headers) -> bool:
    """Direct loopback (the hub on the same machine), or the team's PIPELINE_TOKEN in x-pipeline-token. Fail closed."""
    import os, secrets
    if host in ("127.0.0.1", "::1") and not any(h in headers for h in PROXY_HEADERS):
        from urllib.parse import urlsplit   # loopback Host name (no DNS rebinding) and no foreign Origin (no browser CSRF)
        hh = headers.get("host", "")
        origin = headers.get("origin")
        if (urlsplit("//" + hh).hostname or "") in ("127.0.0.1", "localhost", "::1") and \
                (origin is None or urlsplit(origin).netloc.lower() == hh.lower()):
            return True
    tok = os.environ.get("PIPELINE_TOKEN")
    return bool(tok) and secrets.compare_digest(headers.get("x-pipeline-token", ""), tok)


def require(request: Request):
    if not allowed(request.client.host if request.client else None, request.headers):
        raise HTTPException(401, "loopback or x-pipeline-token only")


async def emit(type_: str, call_id: str, data: dict) -> bool:
    try:
        from detection import hub   # P2's fail-open hub client (HUB_URL + PIPELINE_TOKEN)
        return bool(await hub.emit(type_, call_id, data))
    except Exception as e:
        log.warning("emit %s failed: %s", type_, type(e).__name__)
        return False


async def emit_retry(type_: str, call_id: str, data: dict, tries: int = 4) -> bool:
    """For events that must not be lost (the haul): retry with backoff, ~3.5 s worst case."""
    for i in range(tries):
        if await emit(type_, call_id, data):
            return True
        await asyncio.sleep(0.5 * (2 ** i))
    log.error("emit %s for %s failed after %d tries", type_, call_id, tries)
    return False


@app.get("/healthz")
def healthz():
    return {"ok": True, "cloned_voice": voice.active_voice() is not None, "model": core.MODEL}


@app.post("/voice/enroll", dependencies=[Depends(require)])
async def voice_enroll(body: dict = Body(...)):
    try:
        vid = await asyncio.to_thread(voice.enroll, str(body.get("recording") or ""), str(body.get("mime") or ""),
                                      str(body.get("consent_version") or ""))
    except ValueError as e:
        raise HTTPException(400, str(e))
    # voice.enrolled is published by the hub's proxy (server/voice.py), the only caller; emitting here too would duplicate it.
    q = (voice._meta().get(vid) or {}).get("quality") or {}
    # additive: 'quality' = "ok" or a RE-RECORD reason the page can show (phone-quality audio clones at ~60%)
    return {"voice_id": vid, "quality": q.get("verdict", "ok"), "above_4k_pct": q.get("above_4k_pct")}


@app.delete("/voice/{voice_id}", dependencies=[Depends(require)])
async def voice_delete(voice_id: str):
    if not voice.delete(voice_id):
        raise HTTPException(404, "unknown voice_id")
    return {"ok": True}   # voice.deleted: published by the hub's proxy (server/voice.py)


_STT = None


def _shared_stt(make):
    """One STT client for the process (P2's get_stt logs its fallback probe once, not per call)."""
    global _STT
    if _STT is None:
        _STT = make()
    return _STT


class Session:
    """One decoy conversation on one call."""

    def __init__(self, ws: WebSocket, call_id: str):
        self.ws, self.call_id = ws, call_id
        self.persona = core.Persona(call_id)
        self.voice = voice.Voice()
        self.out: asyncio.Queue = asyncio.Queue()
        self.history: list[dict] = []
        self.scammer_lines: list[str] = []
        self.pending: list[str] = []
        self.given: set = set()
        self.busy = False
        self.speaking_until = 0.0
        self.active = True
        self.t0 = time.time()
        self.fillers: list[list[bytes]] = []
        from detection.stream import Segmenter
        from detection.stt import get_stt, mulaw_decode
        self.seg, self.stt, self.decode = Segmenter(endpoint_ms=DECOY_ENDPOINT_MS), _shared_stt(get_stt), mulaw_decode
        self.stt_ms = 0
        self.speak_start = 0.0         # when the current stretch of our speech started
        self.out_rms = 0.0             # peak-hold level of what we're sending
        self.coupling = 0.1            # echo level / our outbound level, learned from the quietest frames
        self.said: list[str] = []      # our recent sentences, to recognise our own words coming back
        self.loud_ms = 0
        self.last_barge = 0.0
        self.spoke: list[tuple[float, float]] = []   # recent (start, end) of our speech, for echo-utterance filtering
        self.stalls: list[list[bytes]] = []
        self.last_stall = -1
        self.arts: dict[str, dict] = {}      # haul so far, deduped (incremental extraction during the call)
        self.extracted_upto = 0
        self.extracting = False
        self.turns = 0
        self.wrap_at: int | None = None
        self.stream_id = None

    def ev(self, type_, data):
        asyncio.create_task(emit(type_, self.call_id, data))

    # -------------------------------------------------- audio out: paced at real time so `clear` can cut it short
    async def sender(self):
        next_t = time.monotonic()
        while self.active:
            f = await self.out.get()
            if f is None:
                return
            next_t = max(next_t, time.monotonic() - 0.04) + 0.02
            pcm = self.decode(f).astype(np.float32)
            self.out_rms = max(float(np.sqrt(np.mean(pcm * pcm))), self.out_rms * 0.9)
            msg = {"event": "media", "media": {"payload": base64.b64encode(f).decode()}}
            if self.stream_id:
                msg["stream_id"] = self.stream_id
            await self.ws.send_text(json.dumps(msg))
            delay = next_t - time.monotonic() - 0.1   # keep ~100 ms queued downstream
            if delay > 0:
                await asyncio.sleep(delay)

    def play(self, frames: list[bytes]):
        if not frames:
            return
        now = time.monotonic()
        if now >= self.speaking_until:          # starting to speak after silence: echo grace period starts
            self.speak_start = now
            self.spoke.append((now, now))
            self.spoke = self.spoke[-20:]
        for f in frames:
            self.out.put_nowait(f)
        self.speaking_until = max(now, self.speaking_until) + len(frames) * 0.02
        self.spoke[-1] = (self.spoke[-1][0], self.speaking_until)

    def speaking(self) -> bool:
        return time.monotonic() < self.speaking_until

    def caller_loud(self, pcm: np.ndarray) -> bool:
        """Echo gate for one 20 ms inbound frame while we're speaking."""
        x = pcm.astype(np.float32)
        rms = float(np.sqrt(np.mean(x * x)))
        if self.out_rms > 200:   # echo coupling: falls fast, rises slowly, so the caller's speech can't inflate it
            r = min(0.5, max(0.02, rms / self.out_rms))
            self.coupling += (0.3 if r < self.coupling else 0.003) * (r - self.coupling)
        return rms > max(ECHO_MARGIN * self.coupling * self.out_rms, OUT_RATIO * self.out_rms, 2 * self.seg.noise)

    def overlapped_us(self, utt: np.ndarray) -> bool:
        """Heard mostly while we were talking, with no barge-in: it may be our own voice coming back."""
        end = time.monotonic(); start = end - len(utt) / 8000 - 0.45   # + segmenter endpoint wait
        if self.last_barge >= start:
            return False
        overlap = sum(max(0.0, min(e, end) - max(s0, start)) for s0, e in self.spoke)
        return overlap > 0.5 * (end - start)

    def is_our_words(self, text: str) -> bool:
        """The transcript is mostly words we just said (echo), not the caller."""
        import re
        heard = re.findall(r"[a-z']+", text.lower())
        ours = set(re.findall(r"[a-z']+", " ".join(self.said[-4:]).lower()))
        return len(heard) > 0 and sum(w in ours for w in heard) >= 0.6 * len(heard)

    async def barge_in(self):
        while not self.out.empty():
            self.out.get_nowait()
        self.speaking_until = 0
        self.last_barge = time.monotonic()
        if self.spoke:
            self.spoke[-1] = (self.spoke[-1][0], self.last_barge)
        try:
            await self.ws.send_text(json.dumps({"event": "clear", **({"stream_id": self.stream_id} if self.stream_id else {})}))
        except Exception:
            pass

    async def say(self, text: str, latency_ms: int = 0, record: bool = False) -> int:
        """Speaks text sentence by sentence. Returns ms until the first sentence's audio was queued (TTS time)."""
        t0, first_ms = time.monotonic(), 0
        for sentence in [s for s in __import__("re").split(r"(?<=[.!?])\s+", text) if s.strip()]:
            if not self.active:
                return first_ms
            self.said = (self.said + [sentence])[-6:]
            self.play(await self.voice.frames(sentence))
            first_ms = first_ms or int((time.monotonic() - t0) * 1000)
        self.ev("decoy.turn", {"speaker": "decoy", "text": text, "latency_ms": latency_ms})
        if record:
            self.history.append({"role": "assistant", "content": text})
        return first_ms

    # -------------------------------------------------- turns
    async def on_utterance(self, pcm: np.ndarray, maybe_echo: bool = False):
        try:
            t_stt = time.monotonic()
            text = (await asyncio.wait_for(self.stt.transcribe(pcm), STT_TIMEOUT_S)).strip()
            self.stt_ms = int((time.monotonic() - t_stt) * 1000)
        except Exception as e:
            log.warning("STT failed: %s", type(e).__name__)
            if self.active and not self.speaking() and not self.caller_talking() and self.stalls:
                self.play(random.choice(self.stalls))   # never dead air
            return
        if not text or not self.active:
            return
        if maybe_echo and self.is_our_words(text):
            log.info("drop %s: echo of our own words (%r)", self.call_id, text[:60])
            return
        self.scammer_lines.append(text)
        if len(self.scammer_lines) - self.extracted_upto >= 2 and not self.extracting:
            asyncio.create_task(self.extract_now())
        self.ev("decoy.turn", {"speaker": "scammer", "text": text, "latency_ms": 0})
        self.pending.append(text)
        if not self.busy:
            self.busy = True
            asyncio.create_task(self.reply())

    async def finish(self, line: str, why: str):
        """Say goodbye, let it play out, then end: the WS closes and the hub hangs up the caller (ended_by=decoy)."""
        await self.hold_floor()
        await self.say(line)
        while self.active and time.monotonic() < self.speaking_until + 0.6:
            await asyncio.sleep(0.05)
        log.info("decoy %s wrapping up: %s", self.call_id, why)
        self.active = False
        try:
            await self.ws.close()
        except Exception:
            pass

    def caller_talking(self) -> bool:
        """The caller is mid-utterance right now (and it isn't just our own voice coming back)."""
        return self.seg.cur is not None and not self.speaking()

    async def hold_floor(self) -> bool:
        """Wait while the caller is still talking. True if they finished; False if we gave up (keep waiting is worse)."""
        t = time.monotonic()
        while self.active and self.caller_talking() and time.monotonic() - t < HOLD_MAX_S:
            await asyncio.sleep(0.05)
        return not self.caller_talking()

    # -------------------------------------------------- haul: incremental extraction, so a failure at hangup loses nothing
    def ours(self, a: dict) -> bool:
        """An extracted value that is one of OUR fake values (echo of the decoy), not the scammer's."""
        import re
        fakes = {re.sub(r"\D", "", str(v)) for v in self.persona.raw.values()}
        fakes = {f for f in fakes if len(f) >= 4}
        vals = [str(a.get(k) or "") for k in ("value", "id", "addr", "text", "last4")]
        return any(re.sub(r"\D", "", v) in fakes for v in vals if len(re.sub(r"\D", "", v)) >= 4)

    def merge(self, arts: list[dict]) -> int:
        new = 0
        for a in arts or []:
            if self.ours(a):
                log.info("haul %s: dropped our own fake value (%s)", self.call_id, a.get("kind"))
                continue
            k = json.dumps(a, sort_keys=True)
            if k not in self.arts:
                self.arts[k] = a; new += 1
        kinds = {a.get("kind") for a in self.arts.values()}
        if self.wrap_at is None and kinds & STRONG_KINDS and len(kinds) >= 2:
            self.wrap_at = self.turns + WRAP_TURNS
            log.info("haul %s: payment details + %d types (%s); wrapping up after %d more turns", self.call_id,
                     len(kinds), ",".join(sorted(k for k in kinds if k)), WRAP_TURNS)
        return new

    async def extract_now(self, tries: int = 1) -> bool:
        self.extracting = True
        try:
            upto = len(self.scammer_lines)
            for i in range(tries):
                try:
                    arts = await core.extract(list(self.scammer_lines[:upto]))
                    self.merge(arts)
                    self.extracted_upto = upto
                    return True
                except Exception as e:
                    log.warning("extractor failed (%s), try %d/%d", type(e).__name__, i + 1, tries)
                    await asyncio.sleep(0.7 * (i + 1))
            return False
        finally:
            self.extracting = False

    async def reply(self):
        redo = 0
        try:
            while self.active and self.pending:
                heard, self.pending = " ".join(self.pending), []
                t0 = time.monotonic()
                self.history.append({"role": "user", "content": f"<caller>{core.clean(heard)}</caller>"})
                task = asyncio.create_task(core.chat([{"role": "system", "content": core.SYSTEM}] + self.history[-16:]))
                done, _ = await asyncio.wait({task}, timeout=FILLER_AFTER_S)
                if not done and self.fillers and not self.speaking() and not self.caller_talking():
                    self.play(random.choice(self.fillers))     # mask the thinking time
                try:
                    out = await asyncio.wait_for(task, LLM_TIMEOUT_S - FILLER_AFTER_S)
                except Exception as e:
                    log.warning("LLM failed: %s", type(e).__name__)
                    out = None
                if not out and time.monotonic() - t0 < LLM_RETRY_WITHIN_S:   # fast failure (429 etc): one retry
                    await asyncio.sleep(0.4)
                    try:
                        out = await asyncio.wait_for(core.chat([{"role": "system", "content": core.SYSTEM}] + self.history[-16:]),
                                                     max(1.0, LLM_TIMEOUT_S - (time.monotonic() - t0)))
                    except Exception as e:
                        log.warning("LLM retry failed: %s", type(e).__name__)
                llm_ms = int((time.monotonic() - t0) * 1000)
                await self.hold_floor()
                if self.pending and redo < REDO_MAX:
                    # they said more while we were thinking: answer everything they said, not a stale fragment
                    redo += 1
                    self.history.pop()
                    self.pending = [heard] + self.pending
                    log.info("turn %s: caller kept talking, re-thinking (%d)", self.call_id, redo)
                    continue
                redo = 0
                if not out:   # stall, never the same line twice in a row
                    i = random.choice([k for k in range(len(STALLS)) if k != self.last_stall])
                    self.last_stall, out = i, STALLS[i]
                hist, spoken = core.guard(out, self.persona, self.given, self.ev)
                self.history.append({"role": "assistant", "content": hist})
                tts_ms = await self.say(spoken, llm_ms)
                self.turns += 1
                # Caller stopped talking -> first decoy audio queued = stt + llm + tts (the segmenter's end-of-speech wait is extra).
                log.info("turn %s: stt=%dms llm=%dms tts_first=%dms total=%dms voice=%s chars=%d", self.call_id, self.stt_ms,
                         llm_ms, tts_ms, self.stt_ms + llm_ms + tts_ms, "clone" if self.voice.cloned else "synthetic", len(spoken))
                if time.time() - self.t0 > CAP_S:
                    await self.finish(core.GOODBYE, "time cap")
                elif self.wrap_at is not None and self.turns >= self.wrap_at:
                    await self.finish(WRAP_LINE, "got the payment details")
        except Exception:
            log.exception("turn failed (decoy keeps listening)")
        finally:
            self.busy = False

    async def run(self):
        send_task = asyncio.create_task(self.sender())
        async def warm():
            await self.say(core.OPENER, record=True)
            for f in core.FILLERS:
                fr = await self.voice.frames(f)
                if fr:
                    self.fillers.append(fr)
            for t in STALLS:
                fr = await self.voice.frames(t)
                if fr:
                    self.stalls.append(fr)
        asyncio.create_task(warm())
        try:
            while self.active:
                m = json.loads(await self.ws.receive_text())
                ev = m.get("event")
                if ev == "start":
                    self.stream_id = m.get("stream_id") or (m.get("start") or {}).get("stream_id")
                elif ev == "media" and (m.get("media") or {}).get("track") in (None, "inbound"):
                    pcm = self.decode(base64.b64decode(m["media"]["payload"]))
                    for utt in self.seg.feed(pcm):
                        asyncio.create_task(self.on_utterance(utt, self.overlapped_us(utt)))
                    # barge-in: sustained caller speech clearly above our echo, after the onset grace period
                    if self.speaking() and time.monotonic() - self.speak_start > BARGE_GRACE_S:
                        self.loud_ms = self.loud_ms + 20 if self.caller_loud(pcm) else max(0, self.loud_ms - 10)   # tolerate syllable gaps
                        if self.loud_ms >= BARGE_IN_MS:
                            self.loud_ms = 0
                            log.info("barge-in %s (in=%.0f coupling=%.2f out=%.0f)", self.call_id,
                                     float(np.sqrt(np.mean(pcm.astype(np.float32) ** 2))), self.coupling, self.out_rms)
                            await self.barge_in()
                    else:
                        self.loud_ms = 0
                elif ev == "stop":
                    break
        except (WebSocketDisconnect, RuntimeError):
            pass
        finally:
            self.active = False
            self.out.put_nowait(None)
            send_task.cancel()
            t_end = time.monotonic()
            for _ in range(40):                      # an incremental pass may still be running
                if not self.extracting:
                    break
                await asyncio.sleep(0.1)
            if len(self.scammer_lines) > self.extracted_upto:   # final pass over everything, with retries
                await self.extract_now(tries=3)
            arts = list(self.arts.values())
            ok = await emit_retry("artifacts.extracted", self.call_id, {"artifacts": arts}) if arts else True
            log.info("decoy %s done: %d scammer lines, %d artifacts (%s, %.1f s after stop), voice=%s", self.call_id,
                     len(self.scammer_lines), len(arts), "posted" if ok else "NOT POSTED", time.monotonic() - t_end,
                     "clone" if self.voice.cloned else "synthetic")


@app.websocket("/decoy/{call_id}")
async def decoy_ws(ws: WebSocket, call_id: str):
    if not allowed(ws.client.host if ws.client else None, ws.headers):
        await ws.close(code=1008); return
    await ws.accept()
    log.info("decoy %s connected", call_id)
    try:
        await Session(ws, call_id).run()
    except Exception:
        log.exception("decoy %s crashed (call unaffected)", call_id)
