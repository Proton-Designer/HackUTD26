"""Webhook Ed25519 verification + abuse limits (per-caller rate, concurrent cap)."""
import base64, os, time, logging
from collections import defaultdict, deque
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

log = logging.getLogger("voip.security")
TOLERANCE_S = 300

def verify_signature(raw_body: bytes, signature_b64: str | None, timestamp: str | None,
                     public_key_b64: str | None = None, now: float | None = None) -> bool:
    """Telnyx signs `timestamp|body` with Ed25519. Missing key -> only OK if VOIP_ALLOW_UNSIGNED=1 (dev)."""
    key = public_key_b64 if public_key_b64 is not None else os.environ.get("TELNYX_PUBLIC_KEY")
    if not key:
        ok = os.environ.get("VOIP_ALLOW_UNSIGNED") == "1"
        if ok: log.warning("accepting UNSIGNED webhook (VOIP_ALLOW_UNSIGNED=1, no TELNYX_PUBLIC_KEY)")
        return ok
    try:
        if not signature_b64 or not timestamp: return False
        if abs((now if now is not None else time.time()) - int(timestamp)) > TOLERANCE_S: return False
        Ed25519PublicKey.from_public_bytes(base64.b64decode(key)).verify(
            base64.b64decode(signature_b64), timestamp.encode() + b"|" + raw_body)
        return True
    except (InvalidSignature, ValueError, TypeError):
        return False

class Limiter:
    """Per-caller sliding window + global concurrent-call cap. In-memory, demo scale."""
    def __init__(self, per_caller=4, window_s=600, max_concurrent=5):
        self.per_caller, self.window_s, self.max_concurrent = per_caller, window_s, max_concurrent
        self.hits: dict[str, deque] = defaultdict(deque)
        self.active: set[str] = set()

    def check(self, caller: str, call_id: str, now: float | None = None) -> str | None:
        """Return a reject reason or None (and register the call)."""
        now = now if now is not None else time.time()
        q = self.hits[caller]
        while q and now - q[0] > self.window_s: q.popleft()
        if len(q) >= self.per_caller: return "Too many calls from this number"
        if len(self.active) >= self.max_concurrent: return "Line is busy"
        q.append(now); self.active.add(call_id)
        return None

    def release(self, call_id: str): self.active.discard(call_id)
