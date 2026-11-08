"""The normal Backfire hub plus the Android VoIP routes, without touching P1's server/main.py.
Run from the repo root:  .venv-hub/bin/python -m uvicorn android_voip.bridge.hub_app:app --host 0.0.0.0 --port 8000
(Or P1 adds `from android_voip.bridge.router import router; mount_router(router)` to server/main.py.)"""
from server.main import app, mount_router
from .router import router

mount_router(router)

# server/main.py mounts the static /app and /command-center last so API routes win; keep that true for ours.
app.router.routes.sort(key=lambda r: r.__class__.__name__ == "Mount")
