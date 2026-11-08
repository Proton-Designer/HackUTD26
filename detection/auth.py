"""Shared-secret auth for the public P2 routes. PIPELINE_TOKEN unset = open (logged once); set = required.
Token: header x-pipeline-token or query ?token=. Never log the token."""
import hmac, logging, os, re
from fastapi import HTTPException, Request

log = logging.getLogger("p2.auth")
CALL_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
_warned = False

def valid_call_id(cid) -> bool:
    return isinstance(cid, str) and CALL_ID_RE.fullmatch(cid) is not None

def warn_if_open():
    global _warned
    if not os.environ.get("PIPELINE_TOKEN") and not _warned:
        _warned = True
        log.warning("PIPELINE_TOKEN is not set: /stt and /detect are OPEN (no auth)")

def check_token(headers, query) -> bool:
    want = os.environ.get("PIPELINE_TOKEN")
    if not want:
        return True
    got = headers.get("x-pipeline-token") or query.get("token") or ""
    return hmac.compare_digest(got.encode(), want.encode())

async def require_token(request: Request):
    """FastAPI dependency for HTTP routes."""
    if not check_token(request.headers, request.query_params):
        raise HTTPException(401, "bad or missing pipeline token")
