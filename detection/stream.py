"""WS /stt/{call_id}: P1's relay sends Telnyx media frames (verbatim JSON). We keep ONLY the inbound (caller) track,
decode mu-law, endpoint on energy, run STT, emit transcript.caller finals, and hand finals to on_final(call_id, utt).
Fail open: garbage frames are ignored; nothing here ever raises into the socket loop."""
import asyncio, base64, itertools, json, logging, os, time
import numpy as np
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from . import auth, health, hub, stt

log = logging.getLogger("p2.stream")
router = APIRouter()
FRAME = 160                      # 20 ms @ 8 kHz
ENDPOINT_MS = int(os.environ.get("P2_ENDPOINT_MS", "450"))
MIN_SPEECH_MS = 250
MAX_UTT_S = 15.0
PARTIALS = os.environ.get("P2_PARTIALS", "1") != "0"
PARTIAL_EVERY_S = float(os.environ.get("P2_PARTIAL_EVERY_S", "0.5"))
PARTIAL_MIN_MS = 400
PREROLL_FRAMES = 10              # 200 ms kept before speech onset

on_partial = None                # async callable(call_id, utt) for interim text (fast-path rules only)
on_final = None                  # async callable(call_id, utt: dict) set by detection.alert (TASK-004)
def set_on_partial(fn):
    global on_partial
    on_partial = fn

def set_on_final(fn):
    global on_final
    on_final = fn

def parse_frame(raw):
    """Telnyx JSON text -> (event, pcm_bytes|None). Only inbound media returns audio. Never raises."""
    try:
        m = json.loads(raw)
        ev = m.get("event")
        if ev == "media":
            media = m.get("media") or {}
            if media.get("track", "inbound") != "inbound":
                return "media_other_track", None
            return "media", base64.b64decode(media.get("payload", ""), validate=True)
        return ev, None
    except Exception:
        return None, None

class Segmenter:
    """Energy VAD + endpointing. feed(pcm_int16) -> list of finished utterances (int16 arrays)."""
    def __init__(self, endpoint_ms=ENDPOINT_MS):
        self.end_frames = max(1, endpoint_ms // 20)
        self.noise = 60.0
        self.buf = np.zeros(0, dtype=np.int16)   # leftover < FRAME
        self.pre = []
        self.cur = None
        self.sil = 0
        self.speech_frames = 0

    def feed(self, pcm):
        out = []
        self.buf = np.concatenate([self.buf, pcm])
        n = len(self.buf) // FRAME
        for i in range(n):
            f = self.buf[i * FRAME:(i + 1) * FRAME]
            rms = float(np.sqrt(np.mean(f.astype(np.float64) ** 2)))
            thr = max(300.0, self.noise * 3.5)
            voiced = rms > thr
            if self.cur is None:
                if voiced:
                    self.cur = list(self.pre) + [f]
                    self.sil, self.speech_frames = 0, 1
                else:
                    self.noise = 0.95 * self.noise + 0.05 * rms
                    self.pre.append(f); self.pre = self.pre[-PREROLL_FRAMES:]
            else:
                self.cur.append(f)
                if voiced:
                    self.sil = 0; self.speech_frames += 1
                else:
                    self.sil += 1
                if self.sil >= self.end_frames or len(self.cur) * FRAME / 8000 >= MAX_UTT_S:
                    out.extend(self._close())
        self.buf = self.buf[n * FRAME:]
        return out

    def snapshot(self):
        return np.concatenate(self.cur) if self.cur and self.speech_frames * 20 >= PARTIAL_MIN_MS else None

    def flush(self):
        return self._close() if self.cur is not None else []

    def _close(self):
        cur, sp = self.cur, self.speech_frames
        self.cur, self.pre, self.sil, self.speech_frames = None, [], 0, 0
        return [np.concatenate(cur)] if sp * 20 >= MIN_SPEECH_MS else []

async def handle_utterance(call_id, uid, pcm, t_end=None):
    try:
        text = (await stt.get_stt().transcribe(pcm)).strip()
    except Exception as e:
        health.err("stt", e)
        log.warning("stt failed call=%s: %s", call_id, type(e).__name__)
        return
    if not text:
        return
    if t_end:
        log.info("stt final %s: %.2fs after endpoint: %r", uid, time.time() - t_end, text[:80])
    utt = {"utterance_id": uid, "text": text, "is_final": True}
    await hub.emit("transcript.caller", call_id, utt)
    if on_final:
        try:
            await on_final(call_id, dict(utt, _t_end=t_end) if t_end else utt)   # _t_end (wall clock of endpoint) is internal, never emitted to the hub
        except Exception:
            log.exception("on_final failed (ignored, fail-open)")

@router.websocket("/stt/{call_id}")
async def stt_ws(ws: WebSocket, call_id: str):
    if not auth.valid_call_id(call_id) or not auth.check_token(ws.headers, ws.query_params):
        await ws.close(code=1008); return      # before accept: rejected handshake
    await ws.accept()
    health.STATE["active"] += 1
    seg, ids, tasks = Segmenter(), [1, 0], set()   # ids: [next utterance number, last submitted]
    pstate = {"busy": False, "t": 0.0, "text": ""}
    counts = {}   # frame diagnostics per event type, logged at close (P1 #31)
    chain = asyncio.Queue()   # preserve utterance order
    async def worker():
        while True:
            item = await chain.get()
            if item is None:
                return
            await handle_utterance(call_id, *item)
    w = asyncio.create_task(worker())
    def submit(arrs):
        for a in arrs:
            chain.put_nowait((f"{call_id}-u{ids[0]}", a, time.time())); ids[1] = ids[0]; ids[0] += 1; pstate["text"] = ""
    async def partial(n, pcm):
        try:
            text = (await stt.get_stt().transcribe(pcm)).strip()
            if text and text != pstate["text"] and ids[1] < n:      # drop if this utterance already finalized
                pstate["text"] = text
                utt = {"utterance_id": f"{call_id}-u{n}", "text": text, "is_final": False}
                await hub.emit("transcript.caller", call_id, utt)
                if on_partial:
                    await on_partial(call_id, utt)
        except Exception as e:
            log.debug("partial failed: %s", type(e).__name__)
        finally:
            pstate["busy"] = False
    try:
        while True:
            raw = await ws.receive_text()
            ev, audio = parse_frame(raw)
            counts[ev] = counts.get(ev, 0) + 1
            if sum(counts.values()) == 1:
                log.info("stt ws %s first frame: event=%s", call_id, ev)
            if ev == "media" and audio:
                try:
                    submit(seg.feed(stt.mulaw_decode(audio)))
                    if PARTIALS and not pstate["busy"] and time.monotonic() - pstate["t"] >= PARTIAL_EVERY_S:
                        snap = seg.snapshot()
                        if snap is not None:
                            pstate["busy"], pstate["t"] = True, time.monotonic()
                            tasks.add(asyncio.create_task(partial(ids[0], snap)))
                except Exception:
                    log.warning("bad audio frame ignored")
            elif ev == "stop":
                submit(seg.flush()); break
    except (WebSocketDisconnect, RuntimeError):
        submit(seg.flush())
    except Exception:
        log.exception("stt ws error")
    finally:
        health.STATE["active"] = max(0, health.STATE["active"] - 1)
        log.info("stt ws %s closed: frames=%s utterances=%d", call_id, counts, ids[1])
        chain.put_nowait(None)
        try:
            await asyncio.wait_for(w, timeout=10)
        except Exception:
            w.cancel()
        try:
            await ws.close()
        except Exception:
            pass
