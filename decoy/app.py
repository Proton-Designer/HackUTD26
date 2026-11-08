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
import os
import time

import numpy as np
from fastapi import Body, Depends, FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect

from . import core, playbooks as PB, voice

log = logging.getLogger("p3.decoy")
_p3 = logging.getLogger("p3")   # nobody configures logging under uvicorn, so p3 INFO lines (per-turn latency) were dropped
if not _p3.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s", "%H:%M:%S"))
    _p3.addHandler(_h); _p3.setLevel(logging.INFO); _p3.propagate = False
app = FastAPI(title="Backfire P3 decoy")
# #127 bail rules: hard cap on decoy time, caller silence, no progress after we asked for the top target twice.
CAP_S = float(os.environ.get("DECOY_CAP_S", "180"))
SILENCE_S = float(os.environ.get("DECOY_SILENCE_S", "15"))
# Counted from the later of: last new artifact, or the 2nd time we went after the current target (a 5-line card plus its
# payment step must not trip it; 90 s, not 75, leaves room for the payment step at ~15 s per line).
NO_PROGRESS_TURNS, NO_PROGRESS_S = 5, 90.0
PLAYBOOKS_ON = os.environ.get("DECOY_PLAYBOOKS", "0") == "1"   # stage B: classify + per-type targets (else generic)
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
STALLS = ["Oh, sorry, the line went funny. Say that again?",
          "Sorry, can you repeat that? I was writing.", "Wait, wait, slow down a little for me.",
          "Hmm, hang on, I dropped my pen.", "Sorry, it's a bit noisy here. What was that last part?",
          "One second, let me get a piece of paper.", "Okay, okay. And then what do I do?"]
# First ~20 s of what the decoy sends, saved per call to logs/decoy_audio/<call_id>.wav (gitignored) to verify the
# handoff voice (#124). DECOY_RECORD_S=0 turns it off.
RECORD_S = float(__import__("os").environ.get("DECOY_RECORD_S", "20"))
RECORD_DIR = __import__("pathlib").Path(__file__).resolve().parent.parent / "logs" / "decoy_audio"
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


class KeyFailoverSTT:
    """P2's Riva STT, one client per NVIDIA key (#123): a rate-limited/rejected key moves on to the next key before the
    whisper fallback is used. Built here so P2's detection/stt.py is unchanged."""

    def __init__(self, keys: list[str]):
        from detection.stt import RivaSTT
        self.by_key = {k: RivaSTT(k) for k in keys}
        self.name, self.slow = RivaSTT.name, False

    async def transcribe(self, pcm):
        from decoy.core import is_key_error, key_failed, keys_in_order
        keys = [k for k in keys_in_order() if k in self.by_key]
        for i, key in enumerate(keys):
            try:
                return await self.by_key[key].transcribe(pcm)
            except Exception as e:
                if is_key_error(e) and i + 1 < len(keys):
                    key_failed(key, "STT " + e.code().name)
                    continue
                raise


def _shared_stt(make):
    """One STT client for the process (P2's get_stt logs its fallback probe once, not per call). With backup NVIDIA keys
    set, Riva fails over across keys, then to P2's whisper fallback."""
    global _STT
    if _STT is None:
        from decoy.core import nvidia_keys
        keys = nvidia_keys()
        if len(keys) > 1 and os.environ.get("P2_STT", "riva") != "whisper":
            try:
                from detection.stt import FallbackSTT
                _STT = FallbackSTT(KeyFailoverSTT(keys))
                log.info("decoy STT: Riva with %d NVIDIA keys (failover), whisper fallback", len(keys))
            except Exception as e:
                log.warning("decoy STT key failover init failed (%s); using P2 default", type(e).__name__)
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
        self.scam = "generic"            # playbook (#127)
        self.asks: dict[str, int] = {}   # target -> times the note told the model to go after it
        self.used_pulls: set[str] = set()
        self.caller_turns = 0
        self.new_art_turn, self.new_art_t = 0, time.monotonic()
        self.refusals = 0
        self.asked2 = (0, time.monotonic())   # (caller turn, time) when we went after the current target the 2nd time
        self.bail_now: str | None = None   # suspicion/hostile/refused: say goodbye on the next turn
        self.bail_reason: str | None = None
        self.last_heard = time.monotonic()
        self.stt_inflight = 0
        self.rec: list[bytes] = []     # first RECORD_S of outbound audio (PCMU frames)

    def save_recording(self):
        if not self.rec:
            return
        try:
            import re as _re, wave
            RECORD_DIR.mkdir(parents=True, exist_ok=True)
            name = _re.sub(r"[^A-Za-z0-9_-]", "_", self.call_id)[:80] or "call"
            pcm = np.concatenate([self.decode(f) for f in self.rec]).astype("<i2")
            with wave.open(str(RECORD_DIR / f"{name}.wav"), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(pcm.tobytes())
        except Exception as e:
            log.warning("decoy recording not saved: %s", type(e).__name__)

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
            if len(self.rec) < RECORD_S * 50:
                self.rec.append(f)
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
        sentences = [s for s in __import__("re").split(r"(?<=[.!?])\s+", text) if s.strip()]
        self.said = (self.said + sentences)[-6:]
        # Whole reply per TTS request (#102): per-sentence synthesis gave every sentence its own flat, final-sounding
        # contour and no natural pauses (pitch spread 4.7 vs the speaker's own 5.7 semitones; 1 vs 7 mid-reply pauses).
        # Same first-audio latency (one request ~0.8 s). Long replies go in ~240-char chunks.
        chunks, cur = [], ""
        for snt in sentences:
            if cur and len(cur) + len(snt) > 240:
                chunks.append(cur); cur = snt
            else:
                cur = (cur + " " + snt).strip()
        if cur:
            chunks.append(cur)
        for sentence in chunks:
            if not self.active:
                return first_ms
            fr = await self.voice.frames(sentence)
            if not fr and self.voice.cloned and (self.stalls or self.fillers):
                # clone TTS failed mid-call: a pre-rendered line in the SAME clone voice, never the synthetic one (#100)
                fr = random.choice(self.stalls or self.fillers)
                log.info("decoy %s: clone TTS failed, cached clone line instead", self.call_id)
                self.play(fr)
                break
            self.play(fr)
            first_ms = first_ms or int((time.monotonic() - t0) * 1000)
        self.ev("decoy.turn", {"speaker": "decoy", "text": text, "latency_ms": latency_ms})
        if record:
            self.history.append({"role": "assistant", "content": text})
        return first_ms

    # -------------------------------------------------- turns
    async def on_utterance(self, pcm: np.ndarray, maybe_echo: bool = False):
        self.last_heard = time.monotonic()   # they just finished speaking: not silence, even while STT runs
        self.stt_inflight += 1
        try:
            t_stt = time.monotonic()
            text = (await asyncio.wait_for(self.stt.transcribe(pcm), STT_TIMEOUT_S)).strip()
            self.stt_ms = int((time.monotonic() - t_stt) * 1000)
            self.stt_inflight -= 1
        except Exception as e:
            self.stt_inflight -= 1
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
        self.caller_turns += 1
        self.last_heard = time.monotonic()
        if PLAYBOOKS_ON:
            new = PB.classify(self.scammer_lines, self.scam)
            if new != self.scam:
                log.info("decoy %s: scam type %s -> %s", self.call_id, self.scam, new)
                self.scam = new
        if not self.bail_now:
            if PB.SUSPICION.search(text):
                self.bail_now = "suspicion"
            elif PB.HOSTILE.search(text):
                self.bail_now = "hostile"
            elif PB.REFUSAL.search(text):
                self.refusals += 1
                if self.refusals >= 2:
                    self.bail_now = "refused"
            if self.bail_now:
                log.info("decoy %s: bail signal %s", self.call_id, self.bail_now)
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
        self.bail_reason = self.bail_reason or why
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
        if new:
            self.new_art_turn, self.new_art_t = self.caller_turns, time.monotonic()
        kinds = {a.get("kind") for a in self.arts.values()}
        top = PB.PLAYBOOKS[self.scam]["targets"][0]
        got_top = top in PB.have(list(self.arts.values()))
        if self.wrap_at is None and (kinds & STRONG_KINDS or got_top) and len(kinds) >= 2:
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

    def steer(self) -> str:
        """Per-turn note (#127 4): scam type, what we have, the next target, turns left. Not stored in history."""
        arts = list(self.arts.values())
        need = [t for t in PB.missing(self.scam, arts) if t != "impersonated_org"]
        pull = None
        if need:
            self.asks[need[0]] = self.asks.get(need[0], 0) + 1
            if self.asks[need[0]] == 2:
                self.asked2 = (self.caller_turns, time.monotonic())
            fresh = [p for p in PB.PULLS.get(need[0], []) if p not in self.used_pulls]
            if fresh:
                pull = random.choice(fresh); self.used_pulls.add(pull)
        if self.wrap_at is not None:
            left = max(1, self.wrap_at - self.turns)
        else:
            left = max(1, int((CAP_S - (time.time() - self.t0)) / 15))
        return PB.note(self.scam, arts, left, pull)

    def bail_check(self) -> str | None:
        """After each of our replies: which bail rule fires, if any (#127 5a-c; d is handled before the reply)."""
        if self.wrap_at is not None and self.turns >= self.wrap_at:
            return "got_payment_details"
        if time.time() - self.t0 > CAP_S:
            return "time_cap"
        need = [t for t in PB.missing(self.scam, list(self.arts.values())) if t != "impersonated_org"]
        since_turn = max(self.new_art_turn, self.asked2[0])
        since_t = max(self.new_art_t, self.asked2[1])
        if need and self.asks.get(need[0], 0) >= 2 and (self.caller_turns - since_turn >= NO_PROGRESS_TURNS
                                                         or time.monotonic() - since_t >= NO_PROGRESS_S):
            return "no_progress"
        return None

    async def silence_watch(self):
        """#127 5e: caller silent SILENCE_S (after our last audio and their last line) -> goodbye."""
        while self.active:
            await asyncio.sleep(1.0)
            if self.caller_talking() or self.stt_inflight or self.pending:
                self.last_heard = time.monotonic()
            quiet_since = max(self.last_heard, self.speaking_until)
            if (not self.busy and not self.speaking() and not self.caller_talking() and not self.stt_inflight
                    and time.monotonic() - quiet_since > SILENCE_S):
                self.busy = True
                await self.finish(PB.GOODBYES["silence"], "silence")
                return

    async def reply(self):
        redo = 0
        try:
            while self.active and self.pending:
                heard, self.pending = " ".join(self.pending), []
                t0 = time.monotonic()
                self.history.append({"role": "user", "content": f"<caller>{core.clean(heard)}</caller>"})
                if self.bail_now:   # suspicion / hostile / refused twice: don't argue, leave now (#127 5d)
                    await self.finish(PB.GOODBYES[self.bail_now], self.bail_now)
                    return
                msgs = [{"role": "system", "content": core.SYSTEM}] + self.history[-16:] + [{"role": "system", "content": self.steer()}]
                task = asyncio.create_task(core.chat(msgs))
                done, _ = await asyncio.wait({task}, timeout=FILLER_AFTER_S)
                # never before the first real reply (#124): the handoff should sound like the rest of the call
                if not done and self.turns > 0 and self.fillers and not self.speaking() and not self.caller_talking():
                    self.play(random.choice(self.fillers))     # mask the thinking time
                try:
                    out = await asyncio.wait_for(task, LLM_TIMEOUT_S - FILLER_AFTER_S)
                except Exception as e:
                    log.warning("LLM failed: %s", type(e).__name__)
                    out = None
                if not out and time.monotonic() - t0 < LLM_RETRY_WITHIN_S:   # fast failure (429 etc): one retry
                    await asyncio.sleep(0.4)
                    try:
                        out = await asyncio.wait_for(core.chat(msgs),
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
                why = self.bail_check()
                if why:
                    await self.finish(PB.GOODBYES[why], why)
        except Exception:
            log.exception("turn failed (decoy keeps listening)")
        finally:
            self.busy = False

    async def run(self):
        send_task = asyncio.create_task(self.sender())
        async def warm_stt():   # first real utterance shouldn't pay the STT cold start (~0.85 s seen)
            try:
                await asyncio.wait_for(self.stt.transcribe(np.zeros(4000, dtype=np.int16)), 5)
            except Exception:
                pass
        asyncio.create_task(warm_stt())

        async def warm():
            # opener first and alone; the rest one at a time after it has been queued (no burst of clone requests)
            await self.say(core.OPENER, record=True)
            for f in core.FILLERS:
                fr = await self.voice.frames(f)
                if fr:
                    self.fillers.append(fr)
            for t in STALLS[:3]:   # only a few pre-rendered: every one is a clone request at call start (429 risk)
                fr = await self.voice.frames(t)
                if fr:
                    self.stalls.append(fr)
        asyncio.create_task(warm())
        asyncio.create_task(self.silence_watch())
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
            self.save_recording()
            t_end = time.monotonic()
            for _ in range(40):                      # an incremental pass may still be running
                if not self.extracting:
                    break
                await asyncio.sleep(0.1)
            if len(self.scammer_lines) > self.extracted_upto:   # final pass over everything, with retries
                await self.extract_now(tries=3)
            arts = list(self.arts.values())
            ok = await emit_retry("artifacts.extracted", self.call_id, {"artifacts": arts}) if arts else True
            kinds = sorted(a["kind"] + (":" + a["rail"] if a.get("rail") else "") for a in arts)   # kinds only, no values
            reason = self.bail_reason or "caller_hung_up"
            log.info("decoy %s done: reason=%s scam=%s, %d scammer lines, %d artifacts %s (%s, %.1f s after stop), voice=%s",
                     self.call_id, reason, self.scam, len(self.scammer_lines), len(arts), kinds, "posted" if ok else "NOT POSTED",
                     time.monotonic() - t_end, "clone" if self.voice.cloned else "synthetic")
            await emit("decoy.done", self.call_id, {"reason": reason, "scam_type": self.scam, "turns": self.turns,
                                                    "caller_turns": self.caller_turns, "artifact_kinds": kinds,
                                                    "duration_s": round(time.time() - self.t0, 1)})


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
