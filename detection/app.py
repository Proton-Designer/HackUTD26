"""P2 detection service. Run: .venv/bin/uvicorn detection.app:app --port 8100"""
import importlib, logging, os
from fastapi import FastAPI
from . import auth, health, stream, stt

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("p2.app")
from . import alert
alert.install()
auth.warn_if_open()
app = FastAPI(title="Backfire P2 detection", lifespan=alert.lifespan)
app.include_router(stream.router)
try:  # eng1's /detect router; guarded so the app runs before it exists
    app.include_router(importlib.import_module("detection.router").router)
except Exception as e:
    log.warning("detection.router not available (%s)", type(e).__name__)

_local = {"t": 0.0, "ok": False}

async def _local_reachable():
    """Cached 10 s probe of the local LLM server (OpenAI-style /v1/models; llama-server and Ollama both answer). Never raises."""
    import time, httpx
    if time.time() - _local["t"] > 10:
        _local["t"] = time.time()
        try:
            async with httpx.AsyncClient(timeout=1.0) as c:
                _local["ok"] = (await c.get(os.environ.get("LOCAL_LLM_URL", "http://127.0.0.1:11434").rstrip("/") + "/v1/models")).status_code == 200
        except Exception:
            _local["ok"] = False
    return _local["ok"]

@app.get("/healthz")
async def healthz():
    """Liveness + what is wired. No secrets (booleans, names, counts, exception class names only)."""
    cur = stt._stt
    backend = ("whisper" if getattr(cur, "name", "").startswith("whisper") or cur.__class__.__name__ == "WhisperSTT" else "riva") if cur else \
        ("whisper" if os.environ.get("P2_STT") == "whisper" else "riva")
    return {"ok": True, "engine": os.environ.get("P2_ENGINE", "cloud"),
            "stt": {"backend": backend, "initialized": cur is not None, "whisper_fallback_loaded": bool(getattr(cur, "_fb", None))},
            "engines": {"cloud_key_present": bool(os.environ.get("NVIDIA_API_KEY")), "local_reachable": await _local_reachable()},
            "hub_subscriber_connected": health.STATE["hub_sub"], "active_stt_sockets": health.STATE["active"],
            "last_error": health.STATE["last_error"]}
