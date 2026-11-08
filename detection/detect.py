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
    "crypto": r"bitcoin|crypto|\bbtc\b|ethereum|wallet address|bitcoin atm|(safe|secure|new|cold|digital|different) wallet",
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


def _campaign(out: dict, text: str) -> dict:
    """Raise-only: known scam script similarity adds +0.1 and the chip (kept within 4 chips)."""
    try:
        from detection import campaign
        if campaign.match(text):
            out["s"] = round(min(1.0, out["s"] + campaign.BOOST), 3)
            out["band"] = schema.band(out["s"])
            if campaign.CHIP not in out["why_chips"]:
                out["why_chips"] = out["why_chips"][:3] + [campaign.CHIP]
    except Exception:
        pass
    return out


def merge(raw, rules: dict, engine: str, text: str = "") -> dict:
    return _campaign(_merge(raw, rules, engine), text)


def _merge(raw, rules: dict, engine: str) -> dict:
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
        t = window_text if isinstance(window_text, str) else ""
        return merge(None, rule_scan(t), engine, t)
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


FUZZY_COS = 0.92
_FUZZY = {"n": -1, "rows": []}


def _vec(text: str):
    from detection.campaign import _grams
    g = _grams(text); n = sum(v * v for v in g.values()) ** 0.5 or 1.0
    return g, n


def _demo_fuzzy(k: tuple):
    """DEMO_MODE only: nearest recorded window by char n-gram cosine >= 0.92, accepted only if the live text's rule asks
    are a subset of the cached asks (never serve a lower-risk answer for a new hard ask). The rule floor is applied by merge()."""
    try:
        cache = _demo_load(); pre = f"{k[0]}|{k[1]}|"
        if _FUZZY["n"] != len(cache):
            _FUZZY["rows"] = [(key[len(pre):], v) + _vec(key[len(pre):]) for key, v in cache.items() if key.startswith(pre)]
            _FUZZY["n"] = len(cache)
        g, n = _vec(k[2]); best, bc = None, 0.0
        for text, v, g2, n2 in _FUZZY["rows"]:
            c = sum(c1 * g2.get(t, 0) for t, c1 in g.items()) / (n * n2)
            if c > bc: best, bc = v, c
        if best is None or bc < FUZZY_COS:
            return None
        if not set(rule_scan(k[2])["asks"]) <= set(best.get("asks") or []):
            log.info("demo fuzzy rejected (new ask) cos=%.3f", bc); return None
        log.info("demo cache fuzzy hit cos=%.3f", bc)
        return best
    except Exception:
        return None


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
            log.info("demo cache hit")
            return hit
        hit = _demo_fuzzy(k)
        if hit is not None:
            return hit
        log.info("demo cache miss: %s", _norm(window_text)[-60:])
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


FAILOVER_CLOUD_S = 2.5     # cloud attempt cap when local is reachable, so local still has budget inside OVERALL_TIMEOUT_S
_local = {"ok": False, "t": -1e9}
FAILOVERS = {"n": 0}
ENGINE_FAILED: dict = {}   # call_id -> True when the last detect() had no LLM result (rules-only because an engine failed); read by alert.py       # count of cloud->local failovers (log/diagnostics)


async def _local_reachable() -> bool:
    """Cached (10 s) probe of the local LLM server. Never raises; no per-call HTTP check."""
    now = time.monotonic()
    if now - _local["t"] < 10:
        return _local["ok"]
    _local["t"] = now
    try:
        import httpx
        base = os.environ.get("LOCAL_LLM_URL", "http://127.0.0.1:11434").rstrip("/")
        async with httpx.AsyncClient(timeout=1.0) as c:
            _local["ok"] = (await c.get(base + "/v1/models")).status_code == 200
    except Exception:
        _local["ok"] = False
    return _local["ok"]


async def detect(call_id: str, window_text: str, metadata: dict | None, engine: str = "cloud") -> dict:
    engine = engine if engine in ("cloud", "local") else "cloud"
    try:
        text = window_text if isinstance(window_text, str) else ""
        metadata = metadata if isinstance(metadata, dict) else {}
        rules = rule_scan(text)
        raw, note = None, None
        t0 = time.monotonic()
        failover_ok = engine == "cloud" and os.environ.get("P2_FAILOVER", "1") != "0" and await _local_reachable()
        try:
            raw = await asyncio.wait_for(_engine_score(text, metadata, engine), FAILOVER_CLOUD_S if failover_ok else OVERALL_TIMEOUT_S)
        except Exception as e:  # fail open to rules only
            note = type(e).__name__
            log.warning("detect %s engine=%s fell back to rules: %s", call_id, engine, note)
        if raw is None and failover_ok:
            left = OVERALL_TIMEOUT_S - (time.monotonic() - t0)
            try:
                if left > 0.3:
                    raw = await asyncio.wait_for(_engine_score(text, metadata, "local"), left)
                    engine = "local"; FAILOVERS["n"] += 1
                    log.warning("detect %s failover: cloud %s -> local", call_id, note)
            except Exception as e:
                log.warning("detect %s failover to local failed: %s", call_id, type(e).__name__)
        out = merge(raw, rules, engine, text)
        ENGINE_FAILED[call_id] = raw is None
        if len(ENGINE_FAILED) > 2000:
            ENGINE_FAILED.clear()
        if raw is None:
            out["scam_type"] = out["scam_type"] if out["asks"] else "unknown"
        return out
    except Exception:  # absolute last resort: valid low-risk shape
        log.exception("detect %s failed", call_id)
        return schema.normalize({}, engine)
