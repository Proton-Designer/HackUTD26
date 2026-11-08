"""NVIDIA key failover for the hub's callers (intel agent, fallback detector). Keys: NVIDIA_API_KEY, NVIDIA_API_KEY_2, NVIDIA_API_KEY_3
(intel may also have INTEL_NVIDIA_API_KEY first). On 429/401/403 the SAME request is retried with the next key. The key that last worked
is preferred for 60 s per scope, then the order resets to the primary. Values come from the process env, else the repo .env; they are never
logged or returned (only 1-based positions and booleans leave this module)."""
import logging, os, pathlib, threading, time

log = logging.getLogger("hub.nvkeys")
FAILOVER_STATUS = {429, 401, 403}
HEALTHY_S = 60.0
BASE_NAMES = ("NVIDIA_API_KEY", "NVIDIA_API_KEY_2", "NVIDIA_API_KEY_3")
ENV_FILE = pathlib.Path(__file__).resolve().parent.parent / ".env"
_lock = threading.Lock()
_primary: dict = {}   # scope -> configured first-choice name
_good: dict = {}   # scope -> (name, monotonic ts) of the last key that worked while it was NOT the first choice


def secret(name):
    v = os.environ.get(name)
    if v:
        return v
    try:
        for ln in ENV_FILE.read_text().splitlines():
            k, _, val = ln.strip().partition("=")
            if k.removeprefix("export ").strip() == name and val.strip():
                return val.strip().strip('"').strip("'")
    except OSError:
        pass
    return None


def key_set(name) -> bool:
    return bool(secret(name))


def ordered(scope="hub", extra_first=()):
    """[(name, value)] in try order: configured keys only, de-duplicated by value, the recently-healthy one first."""
    seen, keys = set(), []
    for n in tuple(extra_first) + BASE_NAMES:
        v = secret(n)
        if v and v not in seen:
            seen.add(v); keys.append((n, v))
    with _lock:
        if keys: _primary[scope] = keys[0][0]
        g = _good.get(scope)
    if g and time.monotonic() - g[1] < HEALTHY_S:
        keys.sort(key=lambda kv: 0 if kv[0] == g[0] else 1)   # stable: others keep their order
    return keys


def note_result(scope, name, _first_name=None, ok=True):
    """Remember a non-primary key that worked for HEALTHY_S (fixed window, not extended by further successes). A success on the primary clears it."""
    with _lock:
        if not ok:
            return
        if name == _primary.get(scope):
            _good.pop(scope, None)
            return
        g = _good.get(scope)
        if not g or g[0] != name or time.monotonic() - g[1] >= HEALTHY_S:
            _good[scope] = (name, time.monotonic())


def label(keys, name):
    return f"key #{[n for n, _ in keys].index(name) + 1}"   # position only, never the value


def failover_note(scope, keys, name, status):
    log.warning("NVIDIA %s on %s %s; trying the next key", status, scope, label(keys, name))


def reset():
    with _lock:
        _good.clear(); _primary.clear()
