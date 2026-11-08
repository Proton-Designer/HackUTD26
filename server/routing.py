"""Pre-ring routing (architecture section 3). Plain code, <50 ms, fail open to NORMAL."""
import logging
from . import db
log = logging.getLogger("hub.routing")
EXEMPT = {"911", "+911", "988", "+988"}

def decide(from_number, attestation="none"):
    try:
        n = db.norm(from_number)
        if n in EXEMPT or (n and len(n.lstrip("+")) <= 6 and n.lstrip("+").isdigit()):
            return {"decision": "NORMAL", "reason": "Exempt (emergency / short code)", "attestation": attestation}
        if db.has("confirmed_scammers", n):
            return {"decision": "BLOCKED_BACKFIRE", "reason": "Confirmed scammer for her", "attestation": attestation}
        if db.has("campaign_numbers", n):
            return {"decision": "BLOCKED_BACKFIRE", "reason": "Linked to a confirmed scam campaign", "attestation": attestation}
        if db.has("trusted", n) and attestation == "A":
            return {"decision": "NORMAL", "reason": "Trusted contact, caller ID verified", "attestation": attestation}
        label = "Trusted number but caller ID not verified" if db.has("trusted", n) else (
            "Caller ID not verified" if attestation in ("none", "C") else "Not in her trusted list")
        return {"decision": "LIVE_GUARD", "reason": label, "attestation": attestation}
    except Exception:
        log.exception("routing failed; failing open")
        return {"decision": "NORMAL", "reason": "Hub error, fail open", "attestation": attestation}
