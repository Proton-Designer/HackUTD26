"""P2 detection service. Run: .venv/bin/uvicorn detection.app:app --port 8100"""
import importlib, logging, os
from fastapi import FastAPI
from . import stream

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("p2.app")
app = FastAPI(title="Backfire P2 detection")
app.include_router(stream.router)
try:  # eng1's /detect router; guarded so the app runs before it exists
    app.include_router(importlib.import_module("detection.router").router)
except Exception as e:
    log.warning("detection.router not available (%s)", type(e).__name__)
try:  # TASK-004 wires the alert machine into stream.on_final
    importlib.import_module("detection.alert").install(app)
except Exception as e:
    log.warning("alert machine not installed (%s)", type(e).__name__)

@app.get("/healthz")
def healthz():
    return {"ok": True, "engine": os.environ.get("P2_ENGINE", "cloud")}
