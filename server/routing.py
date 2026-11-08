"""Pre-ring routing (architecture section 3). Plain code, <50 ms, fail open to NORMAL."""
import logging
from . import db
log = logging.getLogger("hub.routing")
EXEMPT = {"911", "+911", "988", "+988"}  # explicit set only; unverified short codes go to LIVE_GUARD

def decide(from_number, attestation="none"):
    try:
        n = db.norm(from_number)
        if n in EXEMPT:  # emergency numbers are never blocked; only verified callers skip Live Guard
            if attestation in ("A", "B"):
                return {"decision": "NORMAL", "reason": "Exempt (emergency number)", "attestation": attestation}
            return {"decision": "LIVE_GUARD", "reason": "Caller ID not verified", "attestation": attestation}
        # blocklist before any other exemption: an exemption must never bypass a confirmed/campaign block
        if db.has("confirmed_scammers", n):
            return {"decision": "BLOCKED_BACKFIRE", "reason": "Confirmed scammer for her", "attestation": attestation}
        if db.has("campaign_numbers", n):
            return {"decision": "BLOCKED_BACKFIRE", "reason": "Linked to a confirmed scam campaign", "attestation": attestation}
        if db.has("trusted", n) and attestation == "A":
            return {"decision": "NORMAL", "reason": "Trusted contact, caller ID verified", "attestation": attestation}
        label = "Caller ID not verified" if attestation in ("none", "C") else "Not in her trusted list"
        return {"decision": "LIVE_GUARD", "reason": label, "attestation": attestation}
    except Exception:
        log.exception("routing failed; failing open")
        return {"decision": "NORMAL", "reason": "Hub error, fail open", "attestation": attestation}
