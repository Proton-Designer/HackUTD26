"""P2 detection service. Run: .venv/bin/uvicorn detection.app:app --port 8100"""
import importlib, logging, os
from fastapi import FastAPI
from . import auth, stream

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

@app.get("/healthz")
def healthz():
    return {"ok": True, "engine": os.environ.get("P2_ENGINE", "cloud")}
