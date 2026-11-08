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

def _alaw_table():
    t = np.zeros(256, dtype=np.int16)
    for i in range(256):
        a = i ^ 0x55
        sign, exp, man = a & 0x80, (a >> 4) & 7, a & 0x0F
        v = (man << 4) + 8 if exp == 0 else ((man << 4) + 0x108) << (exp - 1)
        t[i] = v if sign else -v
    return t
_ATABLE = _alaw_table()

def alaw_decode(b: bytes) -> np.ndarray:
    """G.711 A-law bytes -> int16 PCM (8 kHz)."""
    return _ATABLE[np.frombuffer(b, dtype=np.uint8)]

def decode_media(b: bytes, encoding="PCMU", rate=8000) -> np.ndarray:
    """Telnyx media payload -> int16 mono 8 kHz. PCMU (default), PCMA, L16 (big-endian); 16 kHz input is averaged down to 8 kHz."""
    e = (encoding or "PCMU").upper()
    if e == "PCMA": x = alaw_decode(b)
    elif e in ("L16", "LINEAR16"): x = np.frombuffer(b[:len(b) // 2 * 2], dtype=">i2").astype(np.int16)
    else: x = mulaw_decode(b)
    if rate and int(rate) == 16000 and len(x) >= 2:
        x = x[:len(x) // 2 * 2].reshape(-1, 2).astype(np.int32).mean(axis=1).astype(np.int16)
    return x

def mulaw_decode(b: bytes) -> np.ndarray:
    """G.711 mu-law bytes -> int16 PCM (8 kHz)."""
    return _TABLE[np.frombuffer(b, dtype=np.uint8)]

class STT:
    name = "base"
    async def transcribe(self, pcm: np.ndarray) -> str:  # int16 mono 8 kHz
        raise NotImplementedError

# Riva gets its OWN small pool: a hung gRPC call leaves its thread stuck after wait_for gives up, and must not eat the default executor that Whisper uses
_RIVA_POOL = None
def _riva_pool():
    global _RIVA_POOL
    if _RIVA_POOL is None:
        from concurrent.futures import ThreadPoolExecutor
        _RIVA_POOL = ThreadPoolExecutor(max_workers=int(os.environ.get("P2_RIVA_THREADS", "4")), thread_name_prefix="riva")
    return _RIVA_POOL

class RivaSTT(STT):
    name = "riva-parakeet-ctc-1.1b"
    FUNC_ID = os.environ.get("RIVA_ASR_FUNCTION_ID", "1598d209-5e27-4d3c-8079-4751568b1081")
    def __init__(self, key=None):
        import riva.client
        self._rc = riva.client
        key = key or os.environ.get("NVIDIA_API_KEY")
        if not key:
            raise RuntimeError("NVIDIA_API_KEY missing")
        auth = riva.client.Auth(None, True, os.environ.get("RIVA_URI", "grpc.nvcf.nvidia.com:443"), [["function-id", self.FUNC_ID], ["authorization", "Bearer " + key]])
        self.svc = riva.client.ASRService(auth)
        self.cfg = riva.client.RecognitionConfig(encoding=riva.client.AudioEncoding.LINEAR_PCM, sample_rate_hertz=RATE,
                                                 language_code="en-US", max_alternatives=1, enable_automatic_punctuation=True, audio_channel_count=1)
    def _run(self, pcm):
        r = self.svc.offline_recognize(pcm.astype("<i2").tobytes(), self.cfg)
        return " ".join(x.alternatives[0].transcript.strip() for x in r.results if x.alternatives).strip()
    async def transcribe(self, pcm):
        return await asyncio.wait_for(asyncio.get_running_loop().run_in_executor(_riva_pool(), self._run, pcm), timeout=float(os.environ.get("P2_STT_TIMEOUT", "6")))

class WhisperSTT(STT):
    name = "faster-whisper"
    slow = True    # CPU: ~0.65 s per call and throughput-bound, so concurrent calls queue; stream.py throttles partials
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
    """Primary (Riva), then local whisper if it errors. Whisper preloads in a background thread at startup (so the first failure does not pay the
    model load) and, after BYPASS_AFTER consecutive primary failures, Riva is skipped for BYPASS_S seconds (no 6 s timeout per utterance) then re-probed."""
    BYPASS_AFTER, BYPASS_S = 2, 30.0
    def __init__(self, primary, preload=True, whisper_factory=None):
        import threading, time
        self.primary, self._fb, self.name = primary, None, primary.name
        self._mk = whisper_factory or WhisperSTT
        self._lock, self._time = threading.Lock(), time.monotonic
        self.fails, self.bypass_until, self.fb_error = 0, 0.0, None
        if preload:
            threading.Thread(target=self._load_fb, daemon=True).start()
    def _load_fb(self):
        with self._lock:                       # one load, shared by the preload thread and a first failure
            if self._fb is None:
                try:
                    self._fb = self._mk(); self.fb_error = None
                    log.info("whisper fallback loaded")
                except Exception as e:
                    self.fb_error = type(e).__name__; raise
        return self._fb
    @property
    def bypassing(self):
        return self._time() < self.bypass_until
    async def transcribe(self, pcm):
        if not self.bypassing:
            try:
                r = await self.primary.transcribe(pcm)
                self.fails = 0
                return r
            except Exception as e:
                self.fails += 1
                log.warning("primary STT failed (%s) x%d; using whisper", type(e).__name__, self.fails)
                if self.fails >= self.BYPASS_AFTER:
                    self.bypass_until = self._time() + self.BYPASS_S
                    log.warning("primary STT bypassed for %.0f s", self.BYPASS_S)
        return await (await asyncio.to_thread(self._load_fb)).transcribe(pcm)

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
