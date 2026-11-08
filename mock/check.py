"""Validate mock/events.json against the contract schema (kept in sync with contracts/events.md)."""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
ATT = {"A", "B", "C", "none"}; BAND = {"low", "watch", "high", "critical"}
ASKS = {"otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app", "secrecy"}
STAGE = {"opening", "pretext", "pressure", "payment", "closing"}
ENDED = {"caller", "maria", "decoy", "system"}
T = {str: str, float: (int, float), int: int, bool: bool, list: list, dict: dict}
# type -> {field: python type or set of allowed values}
SCHEMA = {
 "call.incoming": {"from": str, "to": str, "attestation": ATT, "scam_id_score": float},
 "call.routed": {"decision": {"NORMAL", "BLOCKED_BACKFIRE", "LIVE_GUARD"}, "reason": str},
 "call.answered": {"by": str},
 "call.ended": {"ended_by": ENDED, "duration_s": float},
 "transcript.caller": {"utterance_id": str, "text": str, "is_final": bool},
 "risk.update": {"s": float, "band": BAND, "asks": list, "scam_type": str, "stage": STAGE, "impersonates": (str, type(None)), "addresses_ai_system": bool, "why_chips": list, "engine": {"cloud", "local"}},
 "alert.fired": {"level": {"first", "realert"}, "why_chips": list},
 "user.action": {"action": {"continue", "scammer_get_scammed", "hang_up"}},
 "handoff.started": {"restore_deadline": float},
 "handoff.restored": {"restore_deadline": float},
 "decoy.turn": {"speaker": {"scammer", "decoy"}, "text": str, "latency_ms": int},
 "decoy.fake_value": {"kind": str, "value": str},
 "guardrail.tripped": {"rule": str},
 "artifacts.extracted": {"artifacts": list},
 "intel.lookup": {"artifact_kind": str, "value": str, "result": dict, "source": str},
 "intel.action": {"action_id": str, "kind": str, "target": str, "status": {"applied", "queued", "approved"}, "simulated": bool},
 "injection.denied": {"attempted_target": str, "reason": str},
 "campaign.updated": {"campaign_id": str, "indicators": list, "numbers": list},
 "blocklist.updated": {"number": str, "scope": {"her", "campaign"}, "undo_token": str},
 "voice.enrolled": {"voice_id": str, "consent_version": str},
 "voice.deleted": {"voice_id": str},
}
ARTIFACT_KINDS = {"callback_phone", "domain", "url", "wallet", "payment_handle", "gift_card_brand", "bank", "remote_app", "impersonated_org", "script_tags"}

def check_field(t, k, spec, v, errs):
    if isinstance(spec, set):
        if v not in spec: errs.append(f"{t}.{k}={v!r} not in {sorted(spec)}")
    else:
        if not isinstance(v, T.get(spec, spec)) or (spec is not bool and isinstance(v, bool) and spec in (int, float)):
            errs.append(f"{t}.{k} bad type {type(v).__name__}")

def main():
    doc = json.load(open(ROOT / "mock" / "events.json"))
    errs, seen = [], set()
    for call in doc["calls"]:
        for ev in call["events"]:
            if set(ev) != {"type", "call_id", "ts", "data"}: errs.append(f"bad envelope keys {sorted(ev)}")
            t = ev["type"]; seen.add(t)
            if t not in SCHEMA: errs.append(f"unknown type {t}"); continue
            d = ev["data"]
            for k, spec in SCHEMA[t].items():
                if k not in d: errs.append(f"{t} missing {k}")
                else: check_field(t, k, spec, d[k], errs)
            for k in d:
                if k not in SCHEMA[t]: errs.append(f"{t} extra field {k}")
            if t == "risk.update":
                for a in d["asks"]:
                    if a not in ASKS: errs.append(f"bad ask {a}")
            if t == "artifacts.extracted":
                for a in d["artifacts"]:
                    if a.get("kind") not in ARTIFACT_KINDS: errs.append(f"bad artifact {a}")
    doc_types = set(re.findall(r"^\| `([a-z_.]+)` \|", (ROOT / "contracts" / "events.md").read_text(), re.M))
    if doc_types != set(SCHEMA): errs.append(f"events.md vs schema mismatch: {sorted(doc_types ^ set(SCHEMA))}")
    missing = set(SCHEMA) - seen
    if missing: errs.append(f"types not in mocks: {sorted(missing)}")
    if errs: print("FAIL"); [print(" -", e) for e in errs]; sys.exit(1)
    print(f"OK: {len(seen)} event types, {sum(len(c['events']) for c in doc['calls'])} events")
main()
