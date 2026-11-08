"""P2 detection service. Run: .venv/bin/uvicorn detection.app:app --port 8100"""
import importlib, logging, os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from . import auth, health, stream, stt

logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s %(message)s", datefmt="%H:%M:%S")   # timestamps: scripts/call_report.py needs them
log = logging.getLogger("p2.app")
from . import alert
alert.install()
auth.warn_if_open()
def _warm_stt():
    """Build the STT stack (Riva client + Whisper preload thread) before the first call. Blocking; run in a thread."""
    s = stt.get_stt()
    if s.__class__.__name__ == "WhisperSTT":      # P2_STT=whisper: its model loads lazily, so push one silent half-second through it now
        import asyncio, numpy as np
        asyncio.run(s.transcribe(np.zeros(4000, dtype="<i2")))
    return s

async def warmup_stt():
    """Fail-open background warmup (P2_STT_WARMUP=0 disables): never raises, never blocks startup or /healthz."""
    if os.environ.get("P2_STT_WARMUP", "1") == "0":
        return
    try:
        import asyncio
        await asyncio.to_thread(_warm_stt)
        log.info("stt warmup done")
    except Exception as e:
        log.warning("stt warmup failed (%s); STT will build at the first call", type(e).__name__)

@asynccontextmanager
async def _lifespan(a):
    import asyncio
    task = asyncio.create_task(warmup_stt())
    try:
        async with alert.lifespan(a):
            yield
    finally:
        task.cancel()

app = FastAPI(title="Backfire P2 detection", lifespan=_lifespan)
app.include_router(stream.router)
try:  # eng1's /detect router; guarded so the app runs before it exists
    app.include_router(importlib.import_module("detection.router").router)
except Exception as e:
    log.warning("detection.router not available (%s)", type(e).__name__)

from detection.detect import _local_reachable, breaker_info, local_probe_ms, FAILOVERS  # one shared cached probe

@app.get("/healthz")
async def healthz():
    """Liveness + what is wired. No secrets (booleans, names, counts, exception class names only)."""
    cur = stt._stt
    backend = ("whisper" if getattr(cur, "name", "").startswith("whisper") or cur.__class__.__name__ == "WhisperSTT" else "riva") if cur else \
        ("whisper" if os.environ.get("P2_STT") == "whisper" else "riva")
    return {"ok": True, "engine": os.environ.get("P2_ENGINE", "cloud"),
            "stt": {"backend": backend, "initialized": cur is not None, "whisper_fallback_loaded": bool(getattr(cur, "_fb", None)), "primary_failures": getattr(cur, "fails", 0), "primary_bypassed": bool(getattr(cur, "bypassing", False)), "whisper_model": os.environ.get("P2_WHISPER_MODEL", "base.en")},
            "engines": {"cloud_key_present": bool(os.environ.get("NVIDIA_API_KEY")), "local_reachable": await _local_reachable(), "primary": os.environ.get("P2_ENGINE", "cloud"), "local_probe_ms": local_probe_ms(), "failovers": {"cloud_to_local": FAILOVERS["n"], "local_to_cloud": FAILOVERS.get("reverse", 0)}},
            "cloud_breaker": breaker_info(),
            "hub_subscriber_connected": health.STATE["hub_sub"], "active_stt_sockets": health.STATE["active"],
            "last_error": health.STATE["last_error"]}
