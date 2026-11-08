"""Shared live state for GET /healthz. No secrets: only names, counts and exception class names."""
import time
STATE = {"hub_sub": False, "active": 0, "last_error": None}

def err(src: str, e) -> None:
    """Remember the latest error as 'src: ExceptionClass' with a timestamp (never the message, which could carry URLs/keys)."""
    STATE["last_error"] = {"src": src, "err": type(e).__name__ if isinstance(e, BaseException) else str(e)[:40], "t": time.strftime("%H:%M:%S")}
