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
VAD_FLOOR = float(os.environ.get("P2_VAD_FLOOR", "60"))     # min RMS (int16) to count as speech; real PSTN lines can be quiet (TASK-032)
VAD_REL = float(os.environ.get("P2_VAD_REL", "2.5"))         # threshold = noise floor x this
NOISE_CAP = float(os.environ.get("P2_NOISE_CAP", "300"))     # thr never exceeds NOISE_CAP*VAD_REL (750)
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
        self.noise = 30.0
        self.buf = np.zeros(0, dtype=np.int16)   # leftover < FRAME
        self.pre = []
        self.cur = None
        self.sil = 0
        self.speech_frames = 0
        self.rms_hist, self.voiced_total = [], 0        # diagnostics (TASK-032): per-frame RMS, bounded
    def diag(self):
        h = np.array(self.rms_hist[-30000:] or [0.0])
        return {"frames": len(self.rms_hist), "p50": round(float(np.percentile(h, 50)), 1), "p90": round(float(np.percentile(h, 90)), 1),
                "max": round(float(h.max()), 1), "voiced": self.voiced_total, "noise": round(self.noise, 1), "thr": round(self.thr(), 1)}
    def thr(self):
        return max(VAD_FLOOR, self.noise * VAD_REL)

    def feed(self, pcm):
        out = []
        self.buf = np.concatenate([self.buf, pcm])
        n = len(self.buf) // FRAME
        for i in range(n):
            f = self.buf[i * FRAME:(i + 1) * FRAME]
            rms = float(np.sqrt(np.mean(f.astype(np.float64) ** 2)))
            thr = self.thr()
            voiced = rms > thr
            if len(self.rms_hist) < 60000: self.rms_hist.append(rms)
            self.voiced_total += voiced
            if self.cur is None:
                if voiced:
                    self.cur = list(self.pre) + [f]
                    self.sil, self.speech_frames = 0, 1
                else:
                    a = 0.8 if rms < self.noise else 0.98     # falls fast, rises slowly; capped so a long loud/silent intro can't push thr up
                    self.noise = min(NOISE_CAP, a * self.noise + (1 - a) * rms)
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
        _spawn(_run_on_final(call_id, dict(utt, _t_end=t_end) if t_end else utt))   # _t_end (wall clock of endpoint) is internal, never emitted to the hub

_bg: set = set()   # strong refs to in-flight on_final tasks (a bare create_task can be garbage collected)

def _spawn(coro):
    t = asyncio.get_running_loop().create_task(coro); _bg.add(t); t.add_done_callback(_bg.discard); return t

async def _run_on_final(call_id, utt):
    """Alert/detect work runs OFF the per-call STT worker (TASK-047): the next utterance is transcribed while detect() (2-5 s on local) is still
    running. Tasks start in creation order and alert.on_final appends to the window before its first await, so FIFO order holds; it coalesces
    to one detect in flight per call and drops everything for a call the hub has ended."""
    try:
        await on_final(call_id, utt)
    except Exception:
        log.exception("on_final failed (ignored, fail-open)")

async def drain(timeout=10.0):
    """Wait for in-flight on_final tasks (tests / orderly shutdown)."""
    if _bg:
        await asyncio.wait(list(_bg), timeout=timeout)

SLOW_PARTIAL_EVERY_S = float(os.environ.get("P2_SLOW_PARTIAL_EVERY_S", "1.5"))
def _stt_slow():
    cur = stt._stt
    return bool(cur is not None and (getattr(cur, "slow", False) or getattr(cur, "bypassing", False)))

@router.websocket("/stt/{call_id}")
async def stt_ws(ws: WebSocket, call_id: str):
    if not auth.valid_call_id(call_id) or not auth.check_token(ws.headers, ws.query_params):
        await ws.close(code=1008); return      # before accept: rejected handshake
    await ws.accept()
    health.STATE["active"] += 1
    seg, ids, tasks = Segmenter(), [1, 0], set()   # ids: [next utterance number, last submitted]
    pstate = {"busy": False, "t": 0.0, "text": ""}
    counts = {}   # frame diagnostics per event type, logged at close (P1 #31)
    fmt = {"enc": "PCMU", "rate": 8000}       # from the start frame's media_format when present
    dump = [] if os.environ.get("P2_DUMP_AUDIO") == "1" else None   # decoded inbound PCM, local debugging only (logs/ is gitignored)
    chain = asyncio.Queue()   # preserve utterance order
    async def worker():
        while True:
            item = await chain.get()
            if item is None:
                return
            try:
                await handle_utterance(call_id, *item)
            finally:
                health.STATE["finals_pending"] = max(0, health.STATE.get("finals_pending", 0) - 1)
    w = asyncio.create_task(worker())
    def submit(arrs):
        for a in arrs:
            health.STATE["finals_pending"] = health.STATE.get("finals_pending", 0) + 1
            chain.put_nowait((f"{call_id}-u{ids[0]}", a, time.time())); ids[1] = ids[0]; ids[0] += 1; pstate["text"] = ""
    async def partial(n, pcm, t_snap):
        try:
            text = (await stt.get_stt().transcribe(pcm)).strip()
            if text and text != pstate["text"] and ids[1] < n:      # drop if this utterance already finalized
                pstate["text"] = text
                utt = {"utterance_id": f"{call_id}-u{n}", "text": text, "is_final": False}
                await hub.emit("transcript.caller", call_id, utt)
                if on_partial:
                    await on_partial(call_id, dict(utt, _t_end=t_snap))   # _t_end = wall clock of the audio snapshot, internal only (hub got plain utt)
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
                    pcm = stt.decode_media(audio, fmt["enc"], fmt["rate"])
                    if dump is not None and len(dump) < 90000: dump.append(pcm.astype("<i2").tobytes())
                    submit(seg.feed(pcm))
                    if PARTIALS and not pstate["busy"] and time.monotonic() - pstate["t"] >= (SLOW_PARTIAL_EVERY_S if _stt_slow() else PARTIAL_EVERY_S) \
                            and not (_stt_slow() and health.STATE.get("finals_pending", 0)):   # CPU whisper: finals first, partials are best-effort
                        snap = seg.snapshot()
                        if snap is not None:
                            pstate["busy"], pstate["t"] = True, time.monotonic()
                            tasks.add(asyncio.create_task(partial(ids[0], snap, time.time())))
                except Exception:
                    log.warning("bad audio frame ignored")
            elif ev == "start":
                try:
                    m = json.loads(raw); st = m.get("start") or {}
                    mf = st.get("media_format") or {}
                    fmt["enc"], fmt["rate"] = mf.get("encoding") or "PCMU", mf.get("sample_rate") or 8000
                    log.info("stt ws %s start: media_format=%s start_keys=%s", call_id, st.get("media_format"), sorted(st.keys()))
                except Exception:
                    pass
            elif ev == "stop":
                submit(seg.flush()); break
    except (WebSocketDisconnect, RuntimeError):
        submit(seg.flush())
    except Exception:
        log.exception("stt ws error")
    finally:
        health.STATE["active"] = max(0, health.STATE["active"] - 1)
        log.info("stt ws %s closed: frames=%s utterances=%d", call_id, counts, ids[1])
        try:
            log.info("stt ws %s rms(per 20ms frame): %s", call_id, seg.diag())
            if dump:
                import wave
                os.makedirs("logs/audio", exist_ok=True)
                with wave.open(f"logs/audio/{call_id}.wav", "wb") as wf:
                    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(8000); wf.writeframes(b"".join(dump))
                log.info("stt ws %s audio dumped to logs/audio/%s.wav (local only)", call_id, call_id)
        except Exception:
            log.exception("diag failed (ignored)")
        chain.put_nowait(None)
        try:
            await asyncio.wait_for(w, timeout=10)
        except Exception:
            w.cancel()
        try:
            await ws.close()
        except Exception:
            pass
