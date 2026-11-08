"""P3 voice: Maria's consented voice clone (NVIDIA Magpie TTS Zero-shot) with a synthetic fallback (Magpie Multilingual),
plus conversion to the phone line format (PCMU / mu-law 8 kHz, 20 ms frames).

Enrollment: POST /voice/enroll stores a short, cleaned voice prompt (3-8 s of her recording) locally under
decoy/voices/ (git-ignored). Nothing else of the recording is kept. DELETE /voice/{id} removes it.
The decoy speaks with the most recent enrolled voice; if there is none, or cloning fails, it uses the labeled synthetic voice.
"""
from __future__ import annotations

import asyncio
import base64
import json
import logging
import os
import pathlib
import secrets
import shutil
import subprocess
import time

import numpy as np

log = logging.getLogger("p3.voice")
GRPC = "grpc.nvcf.nvidia.com:443"
ZEROSHOT_FN = os.environ.get("MAGPIE_ZEROSHOT_FUNCTION_ID", "55cf67bf-600f-4b04-8eac-12ed39537a08")
MULTI_FN = os.environ.get("MAGPIE_MULTI_FUNCTION_ID", "877104f7-e885-42b9-8de8-f6e4c6303969")
SYNTH_VOICE = os.environ.get("DECOY_SYNTH_VOICE", "Magpie-Multilingual.EN-US.Aria.Calm")
TTS_RATE = 22050
VOICES = pathlib.Path(os.environ.get("DECOY_VOICES_DIR", pathlib.Path(__file__).parent / "voices"))
PROMPT_MIN_S, PROMPT_MAX_S = 3.0, 8.0

# ---------------------------------------------------------------- mu-law

_BIAS, _CLIP = 0x84, 32635


def _enc_table() -> np.ndarray:
    s = np.arange(-32768, 32768, dtype=np.int32)
    sign = np.where(s < 0, 0x80, 0)
    m = np.minimum(np.abs(s), _CLIP) + _BIAS
    exp = np.floor(np.log2(m)).astype(np.int32) - 7
    mant = (m >> (exp + 3)) & 0x0F
    return (~(sign | (exp << 4) | mant) & 0xFF).astype(np.uint8)


_ENC = _enc_table()


# Anti-alias corner before 8 kHz (#102). Measured trade-off (ECAPA likeness on the phone line, 3 runs each): old 3-tap
# average 0.74 but buzzy aliasing; strict 3.6 kHz 0.65; 3.9 kHz 0.71. 3.9 kHz keeps nearly the whole phone band and still
# removes what folds down from above 4 kHz. DECOY_ANTIALIAS_HZ=off restores the old behaviour (decide by ear).
ANTIALIAS = os.environ.get("DECOY_ANTIALIAS_HZ", "3900")


def _lowpass(rate: int, cutoff: float = 3900.0, taps: int = 255) -> np.ndarray:
    """Blackman-windowed sinc low-pass (anti-alias before 8 kHz). Cached per rate."""
    k = (rate, cutoff, taps)
    if k not in _LP:
        n = np.arange(taps) - (taps - 1) / 2
        h = np.sinc(2 * cutoff / rate * n) * np.blackman(taps)
        _LP[k] = (h / h.sum()).astype(np.float32)
    return _LP[k]


_LP: dict = {}


def to_pcmu_frames(pcm16: bytes, rate: int) -> list[bytes]:
    """16-bit mono PCM at any rate -> list of 160-byte mu-law frames (20 ms at 8 kHz).
    Proper anti-alias filter before resampling (#102: the old 3-tap average let 4-10 kHz TTS sibilants/breath fold
    into the phone band as metallic buzz), and a steady speech level (RMS ~-20 dBFS, peaks under -3 dBFS)."""
    x = np.frombuffer(pcm16, dtype="<i2").astype(np.float32)
    if len(x) == 0:
        return []
    if rate != 8000 and ANTIALIAS.lower() in ("off", "0", "legacy"):
        k = max(1, int(round(rate / 8000)))   # legacy: 3-tap average (lets 4-10 kHz fold into the band)
        x = np.convolve(x, np.ones(k) / k, mode="same")
        t = np.arange(0, len(x) - 1, rate / 8000)
        x = np.interp(t, np.arange(len(x)), x)
    elif rate != 8000:
        x = np.convolve(x, _lowpass(rate, float(ANTIALIAS)), mode="same")
        t = np.arange(0, len(x) - 1, rate / 8000)
        x = np.interp(t, np.arange(len(x)), x)   # band-limited to 3.6 kHz first, so interpolation is clean
    rms = float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0
    if rms > 50:   # same loudness for every reply (no level jumps between turns), never clipping
        x = x * min(3277.0 / rms, 23197.0 / (float(np.abs(x).max()) or 1.0))
    u = _ENC[(np.clip(x, -32768, 32767).astype(np.int32) + 32768)].tobytes()
    u += b"\xff" * (-len(u) % 160)  # pad with mu-law silence
    return [u[i:i + 160] for i in range(0, len(u), 160)]


# ---------------------------------------------------------------- enrolled voices

def _meta() -> dict:
    f = VOICES / "voices.json"
    try:
        return json.loads(f.read_text())
    except Exception:
        return {}


def _save_meta(m: dict):
    VOICES.mkdir(parents=True, exist_ok=True)
    (VOICES / "voices.json").write_text(json.dumps(m, indent=1))


def active_voice() -> pathlib.Path | None:
    """Most recently enrolled voice prompt (single-customer demo)."""
    m = _meta()
    if not m:
        return None
    vid = max(m, key=lambda k: m[k]["ts"])
    p = VOICES / f"{vid}.wav"
    return p if p.exists() else None


def quality(pcm: np.ndarray, rate: int) -> dict:
    """What decides clone quality (measured, #90): bandwidth. A phone-quality (<4 kHz) reference drops speaker
    similarity from ~0.82 to ~0.56 (ECAPA, controlled A/B); Magpie settings (quality, transcript) change ~0.01."""
    x = pcm.astype(np.float64)
    X = np.abs(np.fft.rfft(x)) ** 2; f = np.fft.rfftfreq(len(x), 1 / rate); tot = float(X.sum()) or 1.0
    band = lambda lo, hi: round(100 * float(X[(f >= lo) & (f < hi)].sum()) / tot, 2)  # noqa: E731
    q = {"seconds": round(len(x) / rate, 1), "above_4k_pct": band(4000, rate / 2), "below_120hz_pct": band(0, 120),
         "rms": int(np.sqrt(np.mean(x ** 2))), "clipped": int((np.abs(x) >= 32000).sum())}
    q["narrowband"] = q["above_4k_pct"] < 0.5          # phone-line audio or a heavily processed recording
    q["verdict"] = ("RE-RECORD: phone-quality audio (nothing above 4 kHz); record in the app with the phone's mic, not over a call"
                    if q["narrowband"] else "RE-RECORD: too quiet" if q["rms"] < 300
                    else "RE-RECORD: clipped/distorted, hold the phone a bit further away" if q["clipped"] > rate // 100
                    else "ok")
    return q


def _best_window(pcm: np.ndarray, rate: int) -> np.ndarray:
    """The PROMPT_MAX_S window with the most speech (voiced 20 ms frames), not merely the loudest one, and with
    the fewest clipped samples; edges snapped to quiet frames so it never starts or ends mid-word."""
    win = int(PROMPT_MAX_S * rate)
    if len(pcm) <= win:
        return pcm
    fl = rate // 50
    fr = pcm[: len(pcm) // fl * fl].astype(np.float32).reshape(-1, fl)
    rms = np.sqrt((fr ** 2).mean(1)); clip = (np.abs(fr) >= 32000).sum(1)
    voiced = rms > max(300.0, 0.15 * float(np.percentile(rms, 95)))
    n = win // fl
    best, score = 0, -1e9
    for i in range(0, len(fr) - n, 5):
        sc = voiced[i:i + n].sum() - 5 * clip[i:i + n].sum()
        if sc > score:
            best, score = i, sc
    # snap start back / end forward to the nearest quiet frame (within 0.5 s)
    s0 = best
    for j in range(best, max(0, best - 25), -1):
        if not voiced[j]:
            s0 = j; break
    e0 = min(len(fr), s0 + n)
    for j in range(e0, min(len(fr), e0 + 25)):
        if not voiced[j]:
            e0 = j; break
    return pcm[s0 * fl: e0 * fl]


def _normalize(pcm: np.ndarray) -> np.ndarray:
    """Gain only (no denoising, which smears timbre): speech RMS ~ -20 dBFS, peaks kept under -1 dBFS."""
    x = pcm.astype(np.float32)
    rms = float(np.sqrt(np.mean(x ** 2))) or 1.0
    g = min(3277.0 / rms, 29000.0 / (float(np.abs(x).max()) or 1.0))
    return np.clip(x * g, -32768, 32767).astype("<i2")


def enroll(recording_b64: str, mime: str, consent_version: str) -> str:
    """Store a cleaned voice prompt from Maria's recording. Returns voice_id. Raises ValueError on bad input."""
    if not consent_version:
        raise ValueError("consent_version required")
    try:
        raw = base64.b64decode(recording_b64, validate=False)
    except Exception:
        raise ValueError("recording must be base64")
    if len(raw) < 2000 or len(raw) > 20_000_000:
        raise ValueError("recording too short or too large")
    if not shutil.which("ffmpeg"):
        raise ValueError("server can't decode audio (ffmpeg missing)")
    # webm/opus, ogg, mp4/aac (iOS), wav: ffmpeg sniffs the container itself; mime is informational.
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".rec") as tmp:   # a file, not a pipe: iOS mp4 keeps its index at the end
        tmp.write(raw); tmp.flush()
        # full band kept (22.05 kHz); only a 70 Hz high-pass for handling noise/hum
        p = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", tmp.name, "-ac", "1", "-af", "highpass=f=70", "-ar", str(TTS_RATE),
                            "-f", "s16le", "pipe:1"],
                           capture_output=True, timeout=30)
    pcm = np.frombuffer(p.stdout, dtype="<i2")
    if p.returncode != 0 or len(pcm) < PROMPT_MIN_S * TTS_RATE:
        raise ValueError(f"could not decode at least {PROMPT_MIN_S:.0f} s of audio ({mime})")
    prompt = _normalize(_best_window(pcm, TTS_RATE))
    q = quality(prompt, TTS_RATE)
    if q["verdict"] != "ok":
        log.warning("voice enrollment quality: %s (%s)", q["verdict"], {k: q[k] for k in ("above_4k_pct", "rms", "clipped")})
    vid = "v_" + secrets.token_hex(8)
    VOICES.mkdir(parents=True, exist_ok=True)
    import wave
    with wave.open(str(VOICES / f"{vid}.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(TTS_RATE); w.writeframes(prompt.tobytes())
    m = _meta(); m[vid] = {"ts": time.time(), "consent_version": consent_version, "seconds": round(len(prompt) / TTS_RATE, 1),
                           "mime": mime, "source_seconds": round(len(pcm) / TTS_RATE, 1), "quality": q}
    _save_meta(m)
    log.info("enrolled %s (%.1f s prompt from %.1f s, %s, %.1f%% energy above 4 kHz, %s)", vid, len(prompt) / TTS_RATE,
             len(pcm) / TTS_RATE, mime, q["above_4k_pct"], q["verdict"])
    return vid


def delete(voice_id: str) -> bool:
    m = _meta()
    if voice_id not in m:
        return False
    (VOICES / f"{voice_id}.wav").unlink(missing_ok=True)
    m.pop(voice_id); _save_meta(m)
    return True


# ---------------------------------------------------------------- TTS

class Voice:
    """Speaks with the enrolled clone when present, else the synthetic voice. Blocking calls run in a thread."""

    def __init__(self, prompt: pathlib.Path | None = None):
        import riva.client as rc
        self.rc = rc
        key = os.environ.get("NVIDIA_API_KEY", "")
        self.prompt = prompt if prompt is not None else active_voice()
        self.cloned = self.prompt is not None
        self.locked = False   # True once this call has spoken in the clone voice: never switch after that
        md = lambda fn: [["function-id", fn], ["authorization", "Bearer " + key]]  # noqa: E731
        self.zs = rc.SpeechSynthesisService(rc.Auth(uri=GRPC, use_ssl=True, metadata_args=md(ZEROSHOT_FN)))
        self.multi = rc.SpeechSynthesisService(rc.Auth(uri=GRPC, use_ssl=True, metadata_args=md(MULTI_FN)))

    def _synth(self, text: str) -> bytes:
        """One voice per call (#100: a mid-call switch is a giveaway). The call locks to the clone at its first clone
        success; after that a clone failure gets one retry and then raises (the decoy plays a cached clone-voice line).
        Only if the clone fails before ANY clone audio was made does the whole call use the synthetic voice."""
        if self.cloned:
            for attempt in (1, 2):
                try:
                    a = self.zs.synthesize(text, language_code="en-US", sample_rate_hz=TTS_RATE,
                                           zero_shot_audio_prompt_file=self.prompt, zero_shot_quality=20).audio
                    self.locked = True
                    return a
                except Exception as e:
                    log.warning("clone TTS failed (%s), attempt %d", type(e).__name__, attempt)
                    if attempt == 1:
                        time.sleep(0.35)
            if self.locked:
                raise RuntimeError("clone TTS unavailable; keep the clone voice (cached line)")
            log.warning("clone unavailable before the first sentence: synthetic voice for this whole call")
            self.cloned = False
        return self.multi.synthesize(text, voice_name=SYNTH_VOICE, language_code="en-US", sample_rate_hz=TTS_RATE).audio

    async def frames(self, text: str) -> list[bytes]:
        """Text -> PCMU 20 ms frames. [] on failure."""
        try:
            pcm = await asyncio.wait_for(asyncio.to_thread(self._synth, text), timeout=10)
            return to_pcmu_frames(pcm, TTS_RATE)
        except Exception as e:
            log.warning("TTS failed: %s", type(e).__name__)
            return []


def report() -> None:
    """python -m decoy.voice : quality report for every enrolled voice (the active one last). No audio leaves the machine."""
    import wave
    m = _meta()
    if not m:
        print("no enrolled voices"); return
    for vid in sorted(m, key=lambda k: m[k]["ts"]):
        p = VOICES / f"{vid}.wav"
        if not p.exists():
            print(vid, "missing file"); continue
        w = wave.open(str(p)); x = np.frombuffer(w.readframes(w.getnframes()), "<i2"); r = w.getframerate()
        q = quality(x, r)
        print(f"{vid}  enrolled {time.strftime('%H:%M', time.localtime(m[vid]['ts']))}  {q['seconds']} s  "
              f"above 4 kHz {q['above_4k_pct']}%  rms {q['rms']}  clipped {q['clipped']}  mime {m[vid].get('mime', '?')}  -> {q['verdict']}")
    print("active (used by the decoy):", active_voice().name if active_voice() else None)


if __name__ == "__main__":
    report()
