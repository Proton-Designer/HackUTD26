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


def to_pcmu_frames(pcm16: bytes, rate: int) -> list[bytes]:
    """16-bit mono PCM at any rate -> list of 160-byte mu-law frames (20 ms at 8 kHz)."""
    x = np.frombuffer(pcm16, dtype="<i2").astype(np.float32)
    if len(x) == 0:
        return []
    if rate != 8000:  # band-limit by averaging, then linear interpolation down to 8 kHz
        k = max(1, int(round(rate / 8000)))
        if k > 1:
            x = np.convolve(x, np.ones(k) / k, mode="same")
        t = np.arange(0, len(x) - 1, rate / 8000)
        x = np.interp(t, np.arange(len(x)), x)
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


def _best_window(pcm: np.ndarray, rate: int) -> np.ndarray:
    """The loudest PROMPT_MAX_S window of speech (Magpie prompts work best as a few clean seconds)."""
    win = int(PROMPT_MAX_S * rate)
    if len(pcm) <= win:
        return pcm
    hop = rate // 4
    energy = [float(np.mean(pcm[i:i + win].astype(np.float32) ** 2)) for i in range(0, len(pcm) - win, hop)]
    i = int(np.argmax(energy)) * hop
    return pcm[i:i + win]


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
        p = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", tmp.name, "-ac", "1", "-ar", str(TTS_RATE), "-f", "s16le", "pipe:1"],
                           capture_output=True, timeout=30)
    pcm = np.frombuffer(p.stdout, dtype="<i2")
    if p.returncode != 0 or len(pcm) < PROMPT_MIN_S * TTS_RATE:
        raise ValueError(f"could not decode at least {PROMPT_MIN_S:.0f} s of audio ({mime})")
    prompt = _best_window(pcm, TTS_RATE)
    vid = "v_" + secrets.token_hex(8)
    VOICES.mkdir(parents=True, exist_ok=True)
    import wave
    with wave.open(str(VOICES / f"{vid}.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(TTS_RATE); w.writeframes(prompt.tobytes())
    m = _meta(); m[vid] = {"ts": time.time(), "consent_version": consent_version, "seconds": round(len(prompt) / TTS_RATE, 1)}
    _save_meta(m)
    log.info("enrolled %s (%.1f s prompt from %.1f s, %s)", vid, len(prompt) / TTS_RATE, len(pcm) / TTS_RATE, mime)
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
        md = lambda fn: [["function-id", fn], ["authorization", "Bearer " + key]]  # noqa: E731
        self.zs = rc.SpeechSynthesisService(rc.Auth(uri=GRPC, use_ssl=True, metadata_args=md(ZEROSHOT_FN)))
        self.multi = rc.SpeechSynthesisService(rc.Auth(uri=GRPC, use_ssl=True, metadata_args=md(MULTI_FN)))

    def _synth(self, text: str) -> bytes:
        if self.cloned:
            try:
                return self.zs.synthesize(text, language_code="en-US", sample_rate_hz=TTS_RATE,
                                          zero_shot_audio_prompt_file=self.prompt, zero_shot_quality=20).audio
            except Exception as e:
                log.warning("clone TTS failed (%s); synthetic voice for the rest of the call", type(e).__name__)
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
