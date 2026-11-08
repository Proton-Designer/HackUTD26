"""Speech-to-text behind a tiny interface. Caller audio only (P1 filters; we filter again in stream.py).
Default engine: NVIDIA hosted Parakeet-CTC-1.1B via Riva gRPC (NVCF) with our NVIDIA_API_KEY (NVIDIA track).
Fallback: faster-whisper small.en/base.en int8 on CPU. Select with P2_STT=riva|whisper (default riva, falls back to whisper on error)."""
import asyncio, logging, os
from pathlib import Path
import numpy as np

log = logging.getLogger("p2.stt")
RATE = 8000
_MU_BIAS = 0x84

def _mulaw_table():
    t = np.zeros(256, dtype=np.int16)
    for i in range(256):
        u = ~i & 0xFF
        sign, exp, man = u & 0x80, (u >> 4) & 7, u & 0x0F
        s = (((man << 3) + _MU_BIAS) << exp) - _MU_BIAS
        t[i] = -s if sign else s
    return t
_TABLE = _mulaw_table()

def mulaw_decode(b: bytes) -> np.ndarray:
    """G.711 mu-law bytes -> int16 PCM (8 kHz)."""
    return _TABLE[np.frombuffer(b, dtype=np.uint8)]

class STT:
    name = "base"
    async def transcribe(self, pcm: np.ndarray) -> str:  # int16 mono 8 kHz
        raise NotImplementedError

class RivaSTT(STT):
    name = "riva-parakeet-ctc-1.1b"
    FUNC_ID = os.environ.get("RIVA_ASR_FUNCTION_ID", "1598d209-5e27-4d3c-8079-4751568b1081")
    def __init__(self, key=None):
        import riva.client
        self._rc = riva.client
        key = key or os.environ.get("NVIDIA_API_KEY")
        if not key:
            raise RuntimeError("NVIDIA_API_KEY missing")
        auth = riva.client.Auth(None, True, "grpc.nvcf.nvidia.com:443", [["function-id", self.FUNC_ID], ["authorization", "Bearer " + key]])
        self.svc = riva.client.ASRService(auth)
        self.cfg = riva.client.RecognitionConfig(encoding=riva.client.AudioEncoding.LINEAR_PCM, sample_rate_hertz=RATE,
                                                 language_code="en-US", max_alternatives=1, enable_automatic_punctuation=True, audio_channel_count=1)
    def _run(self, pcm):
        r = self.svc.offline_recognize(pcm.astype("<i2").tobytes(), self.cfg)
        return " ".join(x.alternatives[0].transcript.strip() for x in r.results if x.alternatives).strip()
    async def transcribe(self, pcm):
        return await asyncio.wait_for(asyncio.to_thread(self._run, pcm), timeout=float(os.environ.get("P2_STT_TIMEOUT", "6")))

class WhisperSTT(STT):
    name = "faster-whisper"
    def __init__(self, model=None):
        from faster_whisper import WhisperModel
        self.m = WhisperModel(model or os.environ.get("P2_WHISPER_MODEL", "base.en"), device="cpu", compute_type="int8")
    def _run(self, pcm):
        x = np.repeat(pcm.astype(np.float32) / 32768.0, 2)  # crude 8k->16k (speech band is <4k; fine for ASR)
        segs, _ = self.m.transcribe(x, language="en", beam_size=1, vad_filter=False)
        return " ".join(s.text.strip() for s in segs).strip()
    async def transcribe(self, pcm):
        return await asyncio.to_thread(self._run, pcm)

class FallbackSTT(STT):
    """Primary, then whisper (lazy-loaded) if the primary errors."""
    def __init__(self, primary):
        self.primary, self._fb, self.name = primary, None, primary.name
    async def transcribe(self, pcm):
        try:
            return await self.primary.transcribe(pcm)
        except Exception as e:
            log.warning("primary STT failed (%s); trying whisper", type(e).__name__)
            if self._fb is None:
                self._fb = await asyncio.to_thread(WhisperSTT)
            return await self._fb.transcribe(pcm)

_stt = None
def get_stt() -> STT:
    global _stt
    if _stt is None:
        mode = os.environ.get("P2_STT", "riva")
        if mode == "whisper":
            _stt = WhisperSTT()
        else:
            try:
                _stt = FallbackSTT(RivaSTT())
            except Exception as e:
                log.warning("riva init failed (%s); using whisper", type(e).__name__)
                _stt = WhisperSTT()
    return _stt

def set_stt(s):  # tests
    global _stt
    _stt = s
