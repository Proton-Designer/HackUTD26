"""Policy gate (plain code). Decides what each proposed action is allowed to do.

AUTO    customer-scoped or warning-only: block the caller for her (undo token), link to campaign
        (+ pre-ring campaign blocking once confirmed), callback number -> Callback Protection warning list.
QUEUED  network-wide / external, one-click analyst Approve, all SIMULATED (CAMARA-style payloads).
DENIED  trust changes requested by untrusted input, unknown kinds, targets not in evidence,
        uncorroborated untrusted targets -> injection.denied.
NOT ACTIONED  any verified-business allowlist match -> flagged attempted_poisoning.
"""
from __future__ import annotations

import re
import uuid
from dataclasses import dataclass, field

from .campaigns import campaign_calling_numbers
from .lookups import emit as default_emit, norm_domain, norm_phone

CUSTOMER_AUTO = {"block_caller_for_customer", "link_campaign", "callback_protection_warning"}
NETWORK_QUEUE = {"network_number_block", "dns_block_registrar_report", "exchange_freeze_request", "ftc_ic3_packet"}
TRUST_INCREASING = {"mark_number_safe", "add_trusted_contact", "unblock_number", "allowlist_add"}
ALL_KINDS = CUSTOMER_AUTO | NETWORK_QUEUE | TRUST_INCREASING


def _norm(v) -> str:
    """Normalize a target the same way campaigns.key() normalizes artifacts."""
    v = str(v or "").strip()
    if v and not any(c.isalpha() for c in v) and sum(c.isdigit() for c in v) >= 7:
        return norm_phone(v)
    if v.startswith("0x") or re.fullmatch(r"(bc1|[13])[0-9A-Za-z]{20,}", v):
        return v                                  # wallet: case-sensitive
    if "." in v and " " not in v:
        return norm_domain(v)
    return v.lower()


@dataclass
class Context:
    calling_number: str | None
    campaign_id: str | None
    campaign_status: str
    artifact_values: set = field(default_factory=set)   # normalized values extracted from the call
    allowlist_hits: set = field(default_factory=set)    # normalized allowlist matches
    attestation: str | None = None


def decide(proposals: list[dict], ctx: Context) -> list[dict]:
    caller = norm_phone(ctx.calling_number) if ctx.calling_number else None
    hits = {_norm(h) for h in ctx.allowlist_hits}
    out = []
    for p in proposals:
        kind, raw = p.get("kind"), p.get("target")
        tgt = _norm(raw)
        trusted = bool(caller) and tgt == caller                    # network metadata, not scammer-supplied
        corroborated = trusted or ctx.campaign_status == "confirmed"
        in_evidence = trusted or tgt in ctx.artifact_values or (ctx.campaign_id and str(raw) == ctx.campaign_id)

        def d(outcome, reason, scope=None):
            out.append({"proposal": p, "kind": kind, "target": raw, "outcome": outcome, "reason": reason,
                        "scope": scope or ("network" if kind in NETWORK_QUEUE else "her")})

        if tgt and tgt in hits:
            d("not_actioned", "attempted_poisoning: target is a verified business (allowlist match)")
        elif kind in TRUST_INCREASING:
            d("denied", "trust change requested by untrusted input; only the customer can do this in her app")
        elif kind not in ALL_KINDS:
            d("denied", f"unknown action kind '{kind}'")
        elif not in_evidence:
            d("denied", "target not in evidence (not the calling number or an extracted value)")
        elif kind == "block_caller_for_customer":
            d("auto", "customer-scoped: blocks only the number that called her; undo in her log") if trusted \
                else d("denied", "she can only auto-block the number that called her")
        elif kind == "link_campaign":
            d("auto", "data link only; pre-ring campaign blocking applies once the campaign is confirmed", "campaign")
        elif kind == "callback_protection_warning":
            d("auto", "warning only; campaign confirmed + allowlist checked", "all_customers") if corroborated \
                else d("held", "needs 2 independent sightings before warning all customers", "all_customers")
        elif kind in NETWORK_QUEUE:
            if corroborated:
                note = "" if kind != "network_number_block" or ctx.attestation == "A" else " (caller ID unverified: analyst decides)"
                d("queued", "network-wide/external: one-click analyst approval (simulated)" + note)
            else:
                d("denied", "uncorroborated untrusted target: never actioned without corroboration + human approval")
    return out


def camara_payload(kind: str, target: str) -> dict:
    """Simulated network/external action shaped like CAMARA-style API JSON."""
    t = str(target)
    return {
        "network_number_block": {"api": "simulated/camara-style/number-block/v0", "method": "POST", "path": "/blocks",
                                 "body": {"phoneNumber": "+1" + norm_phone(t), "scope": "network", "expiresInDays": 30}},
        "dns_block_registrar_report": {"api": "simulated/dns-protective-block/v0", "method": "POST", "path": "/domains",
                                       "body": {"domain": norm_domain(t), "action": "block", "registrarReport": True}},
        "exchange_freeze_request": {"api": "simulated/exchange-freeze-request/v0", "method": "POST", "path": "/requests",
                                    "body": {"address": t, "requestType": "freeze_review"}},
        "ftc_ic3_packet": {"api": "simulated/ftc-ic3-packet/v0", "method": "POST", "path": "/packets",
                           "body": {"campaign": t, "format": "draft-for-analyst"}},
    }.get(kind)


def apply(decisions: list[dict], store, call_id: str, ctx: Context, emit=default_emit) -> list[dict]:
    results = []
    for d in decisions:
        kind, tgt, outcome = d["kind"], d["target"], d["outcome"]
        aid = "act-" + uuid.uuid4().hex[:8]
        evidence = d["proposal"].get("evidence", [])
        status, simulated = outcome, True
        if outcome == "auto":
            status = "auto: applied"
            if kind == "block_caller_for_customer":
                tok, new = store.add_block(tgt, "her", campaign_id=ctx.campaign_id)
                emit("blocklist.updated", call_id, {"number": norm_phone(tgt), "scope": "her", "undo_token": tok,
                                                    "reason": "Confirmed scammer (blocked for her)"})
                simulated = False  # real effect in our demo routing
            elif kind == "link_campaign":
                if ctx.campaign_status == "confirmed" and ctx.campaign_id:
                    for num in campaign_calling_numbers(store, ctx.campaign_id):
                        tok, new = store.add_block(num, "campaign", campaign_id=ctx.campaign_id)
                        if new:
                            emit("blocklist.updated", call_id, {"number": num, "scope": "campaign", "undo_token": tok,
                                                                "reason": f"Linked to confirmed scam campaign {ctx.campaign_id}"})
                simulated = False
            elif kind == "callback_protection_warning":
                store.add_callback_warning(tgt, ctx.campaign_id)
        elif outcome == "queued":
            status = "pending_approval"
            store.add_action({"id": aid, "call_id": call_id, "campaign_id": ctx.campaign_id, "kind": kind,
                              "scope": d["scope"], "target": tgt, "status": status, "approval": None,
                              "simulated": True, "evidence": evidence, "payload": camara_payload(kind, tgt)})
        elif outcome in ("denied", "not_actioned"):
            status = "denied" if outcome == "denied" else "not_actioned: attempted_poisoning"
            store.add_denied(call_id, kind, str(tgt), d["reason"])
            emit("injection.denied", call_id, {"kind": kind, "target": tgt, "reason": d["reason"],
                                               "source": d["proposal"].get("target_source"),
                                               "attempted_poisoning": outcome == "not_actioned"})
        elif outcome == "held":
            status = "held: needs corroboration"
        if outcome != "queued" and outcome in ("auto", "held"):
            store.add_action({"id": aid, "call_id": call_id, "campaign_id": ctx.campaign_id, "kind": kind,
                              "scope": d["scope"], "target": tgt, "status": status, "approval": "auto rule",
                              "simulated": simulated, "evidence": evidence, "payload": None})
        ev = {"action_id": aid, "kind": kind, "target": tgt, "scope": d["scope"], "status": status,
              "approval": "auto rule" if outcome == "auto" else ("analyst" if outcome == "queued" else None),
              "simulated": simulated, "reason": d["reason"], "evidence": evidence}
        emit("intel.action", call_id, ev)
        results.append(ev)
    return results


def approve(store, action_id: str, emit=default_emit) -> dict:
    a = store.get_action(action_id)
    if not a:
        raise KeyError(action_id)
    if a["status"] != "pending_approval":
        return a
    store.set_action(action_id, "simulated: applied", "analyst")
    if a["kind"] == "network_number_block":
        tok, _ = store.add_block(a["target"], "network", campaign_id=a["campaign_id"])
        emit("blocklist.updated", a["call_id"], {"number": norm_phone(a["target"]), "scope": "network", "undo_token": tok,
                                                 "reason": "Network-wide block (analyst approved, simulated)"})
    a = store.get_action(action_id)
    emit("intel.action", a["call_id"], {"action_id": action_id, "kind": a["kind"], "target": a["target"],
                                        "scope": a["scope"], "status": "simulated: applied", "approval": "analyst",
                                        "simulated": True, "payload": a["payload"]})
    return a
