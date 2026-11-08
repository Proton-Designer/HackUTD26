"""Hub client: POST {HUB_URL}/events (fail-open, never raises) and WS {HUB_URL}/events subscriber (TASK-004 adds subscribe())."""
import logging, os, time
import httpx

log = logging.getLogger("p2.hub")
_client = None

def hub_url() -> str:
    return os.environ.get("HUB_URL", "http://localhost:8000").rstrip("/")

def headers() -> dict:
    h = {}
    if os.environ.get("PIPELINE_TOKEN"):
        h["x-pipeline-token"] = os.environ["PIPELINE_TOKEN"]
    elif os.environ.get("HUB_TOKEN"):
        h["x-hub-token"] = os.environ["HUB_TOKEN"]
    return h

async def emit(type_: str, call_id: str, data: dict) -> bool:
    """Publish one event. Returns False on any failure (logged without secrets); never raises."""
    global _client
    try:
        if _client is None:
            _client = httpx.AsyncClient(timeout=2.0)
        r = await _client.post(hub_url() + "/events", json={"type": type_, "call_id": call_id, "ts": time.time(), "data": data}, headers=headers())
        if r.status_code >= 300:
            log.warning("hub rejected %s: %s", type_, r.status_code)
            return False
        return True
    except Exception as e:
        log.warning("hub emit %s failed: %s", type_, type(e).__name__)
        return False
