"""TASK-014: per-device pairing PIN. Protects /protection-log, /protection-log/undo, /user/action, and voip's /voip/webrtc-token.
Fail closed. Localhost is allowed only for DIRECT loopback requests: anything that came through the tunnel/proxy (cloudflared connects
from 127.0.0.1 but adds cf-/x-forwarded headers) is treated as remote. HUB_TOKEN (service secret) is also accepted."""
import hashlib, logging, os, pathlib, secrets, threading, time
from fastapi import APIRouter, Body, HTTPException, Request
from . import db

log = logging.getLogger("hub.device")
router = APIRouter()
PIN = os.environ.get("DEVICE_PIN") or "".join(secrets.choice("0123456789") for _ in range(6))
PROXY_HEADERS = ("cf-connecting-ip", "cf-ray", "x-forwarded-for", "x-forwarded-host", "forwarded", "x-real-ip")
_lock = threading.Lock()
_fails: dict = {}   # ip -> [timestamps]
MAX_FAILS, WINDOW_S, GLOBAL_FAILS = 5, 60, 30   # per-IP and across all IPs (defeats header-rotation)

def _announce():
    """Print the PIN and write $LOGDIR/device_pin.txt. No side effects under pytest or when HUB_NO_PIN_FILE=1 (never clobber a live hub's PIN file)."""
    import sys
    if "pytest" in sys.modules or os.environ.get("HUB_NO_PIN_FILE") == "1":
        return
    try:
        d = pathlib.Path(os.environ.get("LOGDIR") or pathlib.Path(__file__).resolve().parent.parent / "logs"); d.mkdir(parents=True, exist_ok=True)
        (d / "device_pin.txt").write_text(PIN + "\n")
    except Exception:
        log.warning("could not write device_pin.txt")
    print(f"DEVICE PIN (enter on Maria's phone): {PIN}", flush=True)

def _hash(t): return hashlib.sha256(t.encode()).hexdigest()

def _ensure_table():
    db.q("CREATE TABLE IF NOT EXISTS device_tokens(hash TEXT PRIMARY KEY, ts REAL)")

def is_direct_local(request: Request) -> bool:
    c = request.client
    return bool(c and c.host in ("127.0.0.1", "::1")) and not any(h in request.headers for h in PROXY_HEADERS)

def _ip(request: Request):
    h = request.headers
    return h.get("cf-connecting-ip") or (h.get("x-forwarded-for") or "").split(",")[0].strip() or (request.client.host if request.client else "?")

def _valid(token) -> bool:
    if not token:
        return False
    _ensure_table()
    return db.q("SELECT 1 FROM device_tokens WHERE hash=?", (_hash(token),)).fetchone() is not None

def _same_origin_or_none(request: Request) -> bool:
    """A cross-origin browser request (hostile page hitting localhost) must not ride the loopback bypass."""
    o = request.headers.get("origin")
    if not o:
        return True
    from urllib.parse import urlsplit
    return urlsplit(o).netloc.lower() == (request.headers.get("host") or "").lower()

def require_device(request: Request):
    """FastAPI dependency (voip may import it): direct localhost, or valid x-device-token, or x-hub-token == HUB_TOKEN."""
    if is_direct_local(request) and _same_origin_or_none(request):
        return
    hub = os.environ.get("HUB_TOKEN")
    if hub and secrets.compare_digest(request.headers.get("x-hub-token", ""), hub):
        return
    if _valid(request.headers.get("x-device-token")):
        return
    raise HTTPException(401, "pair this device first (POST /pair)")

@router.post("/pair")
def pair(request: Request, body: dict = Body(...)):
    ip, now = _ip(request), time.time()
    ok = secrets.compare_digest(str(body.get("pin", "")), PIN)
    with _lock:   # check-and-record is atomic (sync endpoints run in a threadpool)
        fails = [t for t in _fails.get(ip, []) if now - t < WINDOW_S]
        allf = sum(1 for v in _fails.values() for t in v if now - t < WINDOW_S)
        # direct-local requests (the operator at the console) skip the global cap so a remote flood can't lock out pairing entirely
        if len(fails) >= MAX_FAILS or (allf >= GLOBAL_FAILS and not is_direct_local(request)):
            raise HTTPException(429, "too many attempts; wait a minute")
        if not ok:
            fails.append(now); _fails[ip] = fails
            raise HTTPException(401, "wrong code")
        _fails.pop(ip, None)
    tok = secrets.token_urlsafe(24)
    _ensure_table(); db.q("INSERT INTO device_tokens VALUES(?,?)", (_hash(tok), now))
    return {"device_token": tok}
