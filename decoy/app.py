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
app = FastAPI(title="Backfire P3 decoy")
CAP_S = 20 * 60
BARGE_IN_MS = 300


PROXY_HEADERS = ("cf-connecting-ip", "cf-ray", "x-forwarded-for", "x-forwarded-host", "forwarded", "x-real-ip")


def allowed(host: str | None, headers) -> bool:
    """Direct loopback (the hub on the same machine), or the team's PIPELINE_TOKEN in x-pipeline-token. Fail closed."""
    import os, secrets
    if host in ("127.0.0.1", "::1") and not any(h in headers for h in PROXY_HEADERS):
        return True
    tok = os.environ.get("PIPELINE_TOKEN")
    return bool(tok) and secrets.compare_digest(headers.get("x-pipeline-token", ""), tok)


def require(request: Request):
    if not allowed(request.client.host if request.client else None, request.headers):
        raise HTTPException(401, "loopback or x-pipeline-token only")


async def emit(type_: str, call_id: str, data: dict):
    try:
        from detection import hub   # P2's fail-open hub client (HUB_URL + PIPELINE_TOKEN)
        await hub.emit(type_, call_id, data)
    except Exception as e:
        log.warning("emit %s failed: %s", type_, type(e).__name__)


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
    await emit("voice.enrolled", "onboarding", {"voice_id": vid, "consent_version": str(body.get("consent_version"))})
    return {"voice_id": vid}


@app.delete("/voice/{voice_id}", dependencies=[Depends(require)])
async def voice_delete(voice_id: str):
    if not voice.delete(voice_id):
        raise HTTPException(404, "unknown voice_id")
    await emit("voice.deleted", "onboarding", {"voice_id": voice_id})
    return {"ok": True}


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
        self.seg, self.stt, self.decode = Segmenter(), get_stt(), mulaw_decode
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
            msg = {"event": "media", "media": {"payload": base64.b64encode(f).decode()}}
            if self.stream_id:
                msg["stream_id"] = self.stream_id
            await self.ws.send_text(json.dumps(msg))
            delay = next_t - time.monotonic() - 0.1   # keep ~100 ms queued downstream
            if delay > 0:
                await asyncio.sleep(delay)

    def play(self, frames: list[bytes]):
        for f in frames:
            self.out.put_nowait(f)
        self.speaking_until = max(time.monotonic(), self.speaking_until) + len(frames) * 0.02

    async def barge_in(self):
        while not self.out.empty():
            self.out.get_nowait()
        self.speaking_until = 0
        try:
            await self.ws.send_text(json.dumps({"event": "clear", **({"stream_id": self.stream_id} if self.stream_id else {})}))
        except Exception:
            pass

    async def say(self, text: str, latency_ms: int = 0, record: bool = False):
        for sentence in [s for s in __import__("re").split(r"(?<=[.!?])\s+", text) if s.strip()]:
            if not self.active:
                return
            self.play(await self.voice.frames(sentence))
        self.ev("decoy.turn", {"speaker": "decoy", "text": text, "latency_ms": latency_ms})
        if record:
            self.history.append({"role": "assistant", "content": text})

    # -------------------------------------------------- turns
    async def on_utterance(self, pcm: np.ndarray):
        try:
            text = (await self.stt.transcribe(pcm)).strip()
        except Exception as e:
            log.warning("STT failed: %s", type(e).__name__)
            return
        if not text or not self.active:
            return
        self.scammer_lines.append(text)
        self.ev("decoy.turn", {"speaker": "scammer", "text": text, "latency_ms": 0})
        self.pending.append(text)
        if not self.busy:
            self.busy = True
            asyncio.create_task(self.reply())

    async def reply(self):
        try:
            while self.active and self.pending:
                heard, self.pending = " ".join(self.pending), []
                t0 = time.monotonic()
                if self.fillers and random.random() < 0.6:
                    self.play(random.choice(self.fillers))
                self.history.append({"role": "user", "content": f"<caller>{core.clean(heard)}</caller>"})
                out = await core.chat([{"role": "system", "content": core.SYSTEM}] + self.history[-16:])
                out = out or "I'm sorry, could you say that again? The line is terrible."
                hist, spoken = core.guard(out, self.persona, self.given, self.ev)
                self.history.append({"role": "assistant", "content": hist})
                await self.say(spoken, int((time.monotonic() - t0) * 1000))
                if time.time() - self.t0 > CAP_S:
                    await self.say(core.GOODBYE)
                    self.active = False
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
        asyncio.create_task(warm())
        speech_ms = 0
        try:
            while self.active:
                m = json.loads(await self.ws.receive_text())
                ev = m.get("event")
                if ev == "start":
                    self.stream_id = m.get("stream_id") or (m.get("start") or {}).get("stream_id")
                elif ev == "media" and (m.get("media") or {}).get("track") in (None, "inbound"):
                    pcm = self.decode(base64.b64decode(m["media"]["payload"]))
                    for utt in self.seg.feed(pcm):
                        asyncio.create_task(self.on_utterance(utt))
                    # barge-in: the caller has been talking for a moment while we're still speaking
                    speech_ms = speech_ms + 20 if self.seg.cur is not None else 0
                    if speech_ms >= BARGE_IN_MS and time.monotonic() < self.speaking_until:
                        await self.barge_in()
                elif ev == "stop":
                    break
        except (WebSocketDisconnect, RuntimeError):
            pass
        finally:
            self.active = False
            self.out.put_nowait(None)
            send_task.cancel()
            arts = await core.extract(self.scammer_lines)
            if arts:
                await emit("artifacts.extracted", self.call_id, {"artifacts": arts})
            log.info("decoy %s done: %d scammer lines, %d artifacts, voice=%s", self.call_id, len(self.scammer_lines),
                     len(arts), "clone" if self.voice.cloned else "synthetic")


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
