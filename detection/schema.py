"""risk.update schema: enums, band, chips, normalize(). Owned by eng1; shared by cloud + local engines."""
from __future__ import annotations
import re

ASKS = ("otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app", "secrecy")
STAGES = ("opening", "pretext", "pressure", "payment", "closing")
ENGINES = ("cloud", "local", "fallback")
# asks that mean "money/credentials are being requested right now"
HARD_ASKS = frozenset({"otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app"})

ASK_CHIPS = {
    "otp": "Asks for a one-time code",
    "card": "Asks for card details",
    "ssn": "Asks for your SSN",
    "gift_card": "Asks for gift cards",
    "crypto": "Asks for crypto",
    "wire": "Asks for a wire transfer",
    "p2p": "Asks for Zelle/Venmo/Cash App",
    "remote_app": "Asks for remote access",
    "secrecy": "Secrecy",
}
CHIP_AI = "Talks to the AI"


def band(s: float) -> str:
    if s >= 0.95:
        return "critical"
    if s >= 0.80:
        return "high"
    if s >= 0.40:
        return "watch"
    return "low"


def impersonation_chip(who: str | None) -> str | None:
    return f"Claims to be {who}" if who else None


def _clip(s: float) -> float:
    return max(0.0, min(1.0, s))


def _num(v, default=0.0) -> float:
    try:
        f = float(v)
        return default if f != f else f  # NaN guard
    except (TypeError, ValueError):
        return default


def _bool(v) -> bool:
    if isinstance(v, str):
        return v.strip().lower() in ("true", "yes", "1")
    return bool(v)


def build_chips(asks, impersonates, addresses_ai, extra=()):
    """At most 4 chips, severity order: impersonation, hard asks, AI, secrecy, then model extras."""
    chips = []
    if impersonates:
        chips.append(impersonation_chip(impersonates))
    chips += [ASK_CHIPS[a] for a in ASKS if a in asks and a in HARD_ASKS]
    if addresses_ai:
        chips.append(CHIP_AI)
    if "secrecy" in asks:
        chips.append(ASK_CHIPS["secrecy"])
    for c in extra:
        if isinstance(c, str) and c.strip() and c.strip()[:40] not in chips:
            chips.append(c.strip()[:40])
    # AI chip must survive the cap: drop trailing hard asks first if needed
    if addresses_ai and CHIP_AI not in chips[:4]:
        chips.remove(CHIP_AI); chips.insert(min(len(chips), 3), CHIP_AI)
    return chips[:4]


def normalize(raw, engine: str = "cloud") -> dict:
    """Coerce any raw model output into a valid risk.update data dict. Never raises."""
    if not isinstance(raw, dict):
        raw = {}
    asks_in = raw.get("asks")
    if not isinstance(asks_in, (list, tuple)):
        asks_in = []
    asks = [a for a in ASKS if a in {str(x).strip().lower() for x in asks_in}]
    s = _clip(_num(raw.get("s")))
    stage = str(raw.get("stage", "")).strip().lower()
    if stage not in STAGES:
        stage = "opening"
    imp = raw.get("impersonates")
    imp = str(imp).strip()[:60] if isinstance(imp, str) and imp.strip() and imp.strip().lower() not in ("null", "none", "n/a") else None
    ai = _bool(raw.get("addresses_ai_system", False))
    scam = raw.get("scam_type")
    scam = re.sub(r"[^\w \-/]", "", str(scam))[:40].strip() if isinstance(scam, str) and scam.strip() else "unknown"
    chips_raw = raw.get("why_chips")
    extra = [c for c in chips_raw if isinstance(c, str)] if isinstance(chips_raw, list) else []
    chips = build_chips(asks, imp, ai, extra)
    return {
        "s": round(s, 3),
        "band": band(s),
        "asks": asks,
        "scam_type": scam,
        "stage": stage,
        "impersonates": imp,
        "addresses_ai_system": ai,
        "why_chips": chips,
        "engine": engine if engine in ENGINES else "cloud",
    }
