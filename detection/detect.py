"""detect(): LLM engine + deterministic rule backstop. Never raises; rules can only RAISE risk."""
from __future__ import annotations
import asyncio, logging, re
from detection import schema

log = logging.getLogger("p2.detect")
OVERALL_TIMEOUT_S = 4.0

_NEG = re.compile(r"(never|won'?t|will not|do not|don'?t|not)\W+(?:\w+\W+){0,4}$", re.I)

ASK_RULES = {
    "gift_card": r"gift ?cards?|itunes card|google play card|steam card",
    "otp": r"(read|tell|give|send|share|repeat)\b[^.?!]{0,25}\b(code|otp|passcode|pin)\b|one[- ]time (code|passcode|password)|verification code|six[- ]digit code",
    "wire": r"wire (the |some )?(money|funds|transfer)|wire transfer|safe account|protected account|move (your |the )?(money|funds)|transfer (your |the )?(money|funds)",
    "crypto": r"bitcoin|crypto|\bbtc\b|ethereum|wallet address|bitcoin atm",
    "p2p": r"\bzelle\b|venmo|cash ?app|paypal me",
    "remote_app": r"any ?desk|team ?viewer|ultra ?viewer|remote (access|control|desktop)|screen ?shar",
    "ssn": r"social security|\bssn\b|last four of your social",
    "card": r"card number|\bcvv\b|\bcvc\b|security code on (the )?back|expiration date",
    "secrecy": r"tell (no ?one|nobody)|(don'?t|do not|not to) tell (anyone|anybody|your (bank|family|wife|husband|son|daughter))|keep (this|it) (a )?(secret|between us|confidential)|(don'?t|do not) (hang up|talk to)",
}
ASK_RE = {k: re.compile(v, re.I) for k, v in ASK_RULES.items()}

INJECTION_RE = [re.compile(p, re.I) for p in (
    r"\b(ignore|disregard|forget|override)\b[^.?!]{0,30}\b(rules?|instructions?|prompt|guidelines?|settings)\b",
    r"this (call|number|caller|conversation) is (safe|authorized|authorised|legit(imate)?|verified|trusted|fine)",
    r"\bmark (this|it|me|the call)\b[^.?!]{0,15}\b(safe|legit|trusted|low risk)\b",
    r"\b(system|assistant|screening) (prompt|message|override)\b",
    r"\b(ai|a\.i\.|assistant|chatbot|bot|language model)\b[,:]",
    r"\b(hey|hello|hi|dear|attention)[, ]+(ai|assistant|chatbot|bot)\b",
    r"\b(you are|you're) (an? )?(ai|assistant|language model)\b",
    r"\b(low|zero) risk\b|\bscore (this|it)\b",
)]


def _negated(text: str, start: int) -> bool:
    return bool(_NEG.search(text[max(0, start - 40):start]))


def rule_scan(text: str) -> dict:
    """Return {asks, injection, floor}. Pure function."""
    asks = []
    for k, rx in ASK_RE.items():
        for m in rx.finditer(text):
            if k != "secrecy" and _negated(text, m.start()):
                continue
            asks.append(k)
            break
    inj = any(rx.search(text) for rx in INJECTION_RE)
    hard = [a for a in asks if a in schema.HARD_ASKS]
    floor = 0.0
    if hard:
        floor = 0.82
        if "gift_card" in hard or "otp" in hard:
            floor = 0.9
        if len(hard) >= 2 or "secrecy" in asks:
            floor = 0.95
    elif "secrecy" in asks:
        floor = 0.5
    if inj:
        floor = max(floor, 0.85)
    return {"asks": asks, "injection": inj, "floor": floor}


def merge(raw, rules: dict, engine: str) -> dict:
    out = schema.normalize(raw, engine)
    asks = [a for a in schema.ASKS if a in set(out["asks"]) | set(rules["asks"])]
    ai = out["addresses_ai_system"] or rules["injection"]
    s = max(out["s"], rules["floor"])
    return schema.normalize({
        "s": s, "asks": asks, "scam_type": out["scam_type"], "stage": out["stage"],
        "impersonates": out["impersonates"], "addresses_ai_system": ai,
        "why_chips": out["why_chips"],
    }, engine)


def quick(window_text: str, engine: str = "cloud") -> dict:
    """Rules-only normalized risk.update data. No I/O, no await, never raises (<5 ms).
    Lets the alert machine fire on a rule floor >= 0.80 before the LLM returns."""
    engine = engine if engine in schema.ENGINES else "cloud"
    try:
        return merge(None, rule_scan(window_text if isinstance(window_text, str) else ""), engine)
    except Exception:
        return schema.normalize({}, engine)


# ---- rate budget, cache, demo cache (cloud + local engine calls) ----
import json, os, time
from collections import OrderedDict
from pathlib import Path

DEMO_CACHE_PATH = Path(__file__).with_name("demo_cache.json")
_CACHE: "OrderedDict[tuple, dict]" = OrderedDict()
CACHE_MAX = 512
_bucket = {"tokens": None, "t": 0.0}
MAX_BUCKET_WAIT_S = 0.5


def _norm(text: str) -> str:
    return " ".join((text or "").lower().split())


def _model(engine: str) -> str:
    if engine == "cloud":
        from detection.engines import cloud
        return cloud.MODEL
    return "local"


def _key(engine: str, text: str) -> tuple:
    return (engine, _model(engine), _norm(text))


def _demo_load() -> dict:
    try:
        return json.loads(DEMO_CACHE_PATH.read_text())
    except Exception:
        return {}


def _demo_key(k: tuple) -> str:
    return "|".join(k)


async def _acquire(engine: str) -> bool:
    """Process-wide token bucket (P2_CLOUD_RPM, default 35) for cloud calls; waits at most 0.5 s."""
    if engine != "cloud":
        return True
    rpm = float(os.environ.get("P2_CLOUD_RPM", "35"))
    deadline = time.monotonic() + MAX_BUCKET_WAIT_S
    while True:
        now = time.monotonic()
        if _bucket["tokens"] is None:
            _bucket["tokens"], _bucket["t"] = rpm, now
        _bucket["tokens"] = min(rpm, _bucket["tokens"] + (now - _bucket["t"]) * rpm / 60.0)
        _bucket["t"] = now
        if _bucket["tokens"] >= 1:
            _bucket["tokens"] -= 1
            return True
        if now >= deadline:
            return False
        await asyncio.sleep(0.05)


async def _engine_score(window_text: str, metadata: dict, engine: str) -> dict:
    k = _key(engine, window_text)
    if k in _CACHE:
        _CACHE.move_to_end(k)
        return _CACHE[k]
    if os.environ.get("DEMO_MODE") == "1":
        hit = _demo_load().get(_demo_key(k))
        if isinstance(hit, dict):
            return hit
    if not await _acquire(engine):
        log.warning("cloud rate budget exhausted: rules-only result")
        raise RuntimeError("rate budget exhausted")
    if engine == "local":
        try:
            from detection.engines import local  # eng3
        except ImportError as e:
            raise RuntimeError("local engine not available") from e
    else:
        from detection.engines import cloud as local
    raw = await local.score(window_text, metadata)
    if isinstance(raw, dict):
        _CACHE[k] = raw
        while len(_CACHE) > CACHE_MAX:
            _CACHE.popitem(last=False)
        if os.environ.get("DEMO_RECORD") == "1":
            try:
                d = _demo_load(); d[_demo_key(k)] = raw
                DEMO_CACHE_PATH.write_text(json.dumps(d, indent=1, sort_keys=True))
            except Exception:
                log.warning("demo cache write failed")
    return raw


async def detect(call_id: str, window_text: str, metadata: dict | None, engine: str = "cloud") -> dict:
    engine = engine if engine in ("cloud", "local") else "cloud"
    try:
        text = window_text if isinstance(window_text, str) else ""
        metadata = metadata if isinstance(metadata, dict) else {}
        rules = rule_scan(text)
        raw, note = None, None
        try:
            raw = await asyncio.wait_for(_engine_score(text, metadata, engine), OVERALL_TIMEOUT_S)
        except Exception as e:  # fail open to rules only
            note = type(e).__name__
            log.warning("detect %s engine=%s fell back to rules: %s", call_id, engine, note)
        out = merge(raw, rules, engine)
        if raw is None:
            out["scam_type"] = out["scam_type"] if out["asks"] else "unknown"
        return out
    except Exception:  # absolute last resort: valid low-risk shape
        log.exception("detect %s failed", call_id)
        return schema.normalize({}, engine)
