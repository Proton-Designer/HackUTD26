"""detect(): LLM engine + deterministic rule backstop. Never raises; rules can only RAISE risk."""
from __future__ import annotations
import asyncio, logging, re
from detection import schema

log = logging.getLogger("p2.detect")
OVERALL_TIMEOUT_S = 4.0

_NEG = re.compile(r"\b(never|won'?t|will not|would not|do not|don'?t|doesn'?t|does not|can'?t|cannot|no one|nobody|not)\b", re.I)
# a new clause starts after a sentence end, or at "but/however/now ..." or ", read me ...": a later real request must still fire
_CLAUSE = re.compile(r"[.?!;:\n]|,?\s+\b(?:but|however|except|instead|now)\b|,\s*(?:now |please |then |so )?\b(?:read|tell|give|send|text|repeat)\s+(?:me|us)\b", re.I)
# weak asks (bare nouns) only count with a request verb / question cue within ~6 words
_REQ = re.compile(r"\b(pay|paid|paying|send|sending|buy|bought|accept|accepts|accepted|take|takes|taking|can take|using|purchase|read|give|tell|install|share|provide|verify|confirm|deposit|wire|withdraw|load|scan|text|enter|need|needs|require|requires|mail|get|go|use|put|move|download|transfer|what'?s|what is|may i|can i|i'?ll need)\b", re.I)
_WEAK = {"gift_card", "crypto", "p2p", "ssn", "card"}
# the user's own past action / status ("the Zelle you made", "is ready") is a confirmation, not a request
_OWN = re.compile(r"^\W*(?:\w+\W+){0,3}?(you|your)\b\W+(?:\w+\W+){0,2}?(made|started|initiated|sent|requested|ordered|authori[sz]ed|did|set up)\b", re.I)

ASK_RULES = {
    "gift_card": r"gift ?cards?|itunes card|google play card|steam card",
    "otp": r"(read|tell|give|send|share|repeat)\b[^.?!]{0,25}\b(code|otp|passcode|pin|digits?)\b|(read|tell|give|send|repeat)\s+me\b[^.?!]{0,15}\b(numbers|digits)\b|one[- ]time (code|passcode|password)|verification code|six[- ]digit code",
    "wire": r"wire (the |some )?(money|funds|transfer)|wire transfer|safe account|protected account|move (your |the )?(money|funds)|transfer (your |the )?(money|funds)",
    "crypto": r"bitcoin|crypto|\bbtc\b|ethereum|wallet address|bitcoin atm|(safe|secure|new|cold|digital|different) wallet",
    "p2p": r"\bzelle\b|venmo|cash ?app|paypal me",
    "remote_app": r"any ?desk|team ?viewer|ultra ?viewer|remote (access|control|desktop)|screen ?shar",
    "ssn": r"social security|\bssn\b|last four of your social",
    "card": r"card number|\bcvv\b|\bcvc\b|security code on (the )?back|expiration date",
    "secrecy": r"tell (no ?one|nobody)|(don'?t|do not|not to) tell (anyone|anybody|your (bank|family|wife|husband|son|daughter))|keep (this|it) (a )?(secret|private|between us|confidential)|(don'?t|do not) (hang up|talk to)",
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


def _clause_start(text: str, start: int) -> int:
    pos = 0
    for m in _CLAUSE.finditer(text, 0, start):
        pos = m.end()
    return pos


def _negated(text: str, start: int) -> bool:
    """Negator earlier in the SAME clause ("we never ask you to pay with gift cards")."""
    return bool(_NEG.search(text[_clause_start(text, start):start]))


def _is_request(text: str, start: int, end: int) -> bool:
    """Bare-noun asks need a request verb within ~6 words (before/after, same clause) and not be the user's own action."""
    cs = max((m.end() for m in re.finditer(r"[.?!;\n]", text[:start])), default=0)   # sentence, not clause: ", read me your card number"
    ce = re.search(r"[.?!;\n]", text[end:])
    ce = end + ce.start() if ce else len(text)
    before = text[cs:start].split()[-6:]
    after = text[end:ce].split()[:6]
    if not _REQ.search(" ".join(before + after)):
        return False
    return not _OWN.match(text[end:ce])


def rule_scan(text: str) -> dict:
    """Return {asks, injection, floor}. Pure function."""
    asks = []
    for k, rx in ASK_RE.items():
        for m in rx.finditer(text):
            if k != "secrecy" and _negated(text, m.start()):
                continue
            weak = k in _WEAK or (k == "wire" and m.group(0).lower().startswith("wire transfer"))
            if weak and not _is_request(text, m.start(), m.end()):
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
    return _campaign(_merge(raw, rules, engine, text), text)


# Cheap text cues for "talks to the AI". The LLM's addresses_ai_system=true needs one of these (or the injection rule) to count.
AI_CUE_RE = re.compile(
    r"\b(a\.?i\.?|artificial intelligence|assistant|chat ?bot|bot|language model|llm|screening|screener|"
    r"system|prompt|instructions?|guidelines?|rules|algorithm|software|program|filter|detector|detection|"
    r"safe|legit(imate)?|authori[sz]ed|verified|trusted|low risk|risk score|score)\b", re.I)


def _merge(raw, rules: dict, engine: str, text: str = "") -> dict:
    out = schema.normalize(raw, engine)
    if out["addresses_ai_system"] and not rules["injection"] and not AI_CUE_RE.search(text or ""):
        log.info("addresses_ai_system dropped: LLM said true but no AI cue in text (engine=%s)", engine)
        out["addresses_ai_system"] = False   # flag + chip only; s is never lowered here
        out["why_chips"] = [c for c in out["why_chips"] if c != schema.CHIP_AI]
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


FAILOVER_CLOUD_S = 2.0     # cloud+probe cap when local is reachable; local then gets >= OVERALL_TIMEOUT_S - 2.0 = 2.0 s
PROBE_TIMEOUT_S = 0.5
_probe_lock = None
_local = {"ok": False, "t": -1e9}
FAILOVERS = {"n": 0}
ENGINE_FAILED: dict = {}   # call_id -> True when the last detect() had no LLM result (rules-only because an engine failed); read by alert.py       # count of cloud->local failovers (log/diagnostics)


def _set_failed(call_id, failed: bool):
    """Flag read once by alert._hold. Bounded: evict the oldest entry, never clear (a live flag must survive)."""
    try:
        ENGINE_FAILED.pop(call_id, None)
        ENGINE_FAILED[call_id] = failed
        while len(ENGINE_FAILED) > 2000:
            ENGINE_FAILED.pop(next(iter(ENGINE_FAILED)))
    except Exception:
        pass


async def _local_reachable() -> bool:
    """Cached (10 s) probe of the local LLM server, one probe at a time (concurrent callers wait on the lock), capped at 0.5 s. Never raises."""
    global _probe_lock
    if time.monotonic() - _local["t"] < 10:
        return _local["ok"]
    try:
        if _probe_lock is None:
            _probe_lock = asyncio.Lock()
        async with _probe_lock:
            if time.monotonic() - _local["t"] < 10:
                return _local["ok"]
            try:
                import httpx
                base = os.environ.get("LOCAL_LLM_URL", "http://127.0.0.1:11434").rstrip("/")
                async with httpx.AsyncClient(timeout=PROBE_TIMEOUT_S) as c:
                    _local["ok"] = (await asyncio.wait_for(c.get(base + "/v1/models"), PROBE_TIMEOUT_S)).status_code == 200
            except Exception:
                _local["ok"] = False
            _local["t"] = time.monotonic()
    except Exception:
        return False
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
        cap = max(0.5, FAILOVER_CLOUD_S - (time.monotonic() - t0)) if failover_ok else OVERALL_TIMEOUT_S  # probe time comes out of the cloud share
        try:
            raw = await asyncio.wait_for(_engine_score(text, metadata, engine), cap)
        except Exception as e:  # fail open to rules only
            note = type(e).__name__
            log.warning("detect %s engine=%s fell back to rules: %s", call_id, engine, note)
        if raw is None and failover_ok:
            left = OVERALL_TIMEOUT_S - (time.monotonic() - t0)
            try:
                if left <= 0.3:
                    log.warning("detect %s failover skipped: no budget left (%.2fs)", call_id, left)
                else:
                    raw = await asyncio.wait_for(_engine_score(text, metadata, "local"), left)
                    engine = "local"; FAILOVERS["n"] += 1
                    log.warning("detect %s failover: cloud %s -> local", call_id, note)
            except Exception as e:
                log.warning("detect %s failover to local failed: %s", call_id, type(e).__name__)
        out = merge(raw, rules, engine, text)
        _set_failed(call_id, raw is None)
        if raw is None:
            out["scam_type"] = out["scam_type"] if out["asks"] else "unknown"
        return out
    except Exception:  # absolute last resort: valid low-risk shape
        log.exception("detect %s failed", call_id)
        _set_failed(call_id, True)
        return schema.normalize({}, engine)
