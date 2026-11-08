"""Hub + voip mounted: `uvicorn voip.app:app --port 8000` (until server/main.py mounts voip itself)."""
from server.main import app, mount_router
from .router import router
mount_router(router)
