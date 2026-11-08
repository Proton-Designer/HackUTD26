"""Campaign linking: follow the scam, not the number.

A sighting joins a campaign only via a shared STRONG indicator (wallet, callback
phone, domain, payment handle, bank hash) or a high script similarity with the
same stage sequence. A calling number alone never merges campaigns.
"""
from __future__ import annotations

import json
import time
import uuid
from datetime import date

from .lookups import emit as default_emit, norm_domain, norm_phone

STRONG = {"wallet", "callback_phone", "domain", "payment_handle", "bank"}
SCALAR_TYPES = {"callback_phone", "domain", "url", "gift_card_brand", "remote_app", "impersonated_org"}


def normalize_artifacts(artifacts) -> list[dict]:
    """Accepts the contract's typed dict ({callback_phone: ..., wallet: {chain, addr}, ...}) or a list of
    {type, ...} items. Returns a flat list of {type, value, ...extra}."""
    out: list[dict] = []
    if isinstance(artifacts, dict):
        items = []
        for k, v in artifacts.items():
            for one in (v if isinstance(v, list) else [v]):
                if one in (None, "", []):
                    continue
                items.append({"type": k, **one} if isinstance(one, dict) else {"type": k, "value": one})
    else:
        items = list(artifacts or [])
    for a in items:
        t = a.get("type") or a.get("kind")  # contract items are {"kind": K, ...}
        if t == "script_tags":
            vals = a.get("value")
            for tag in (vals if isinstance(vals, list) else [vals]):
                out.append({"type": "script_tag", "value": str(tag)})
            continue
        if t == "wallet":
            out.append({"type": "wallet", "value": a.get("addr") or a.get("value"), "chain": a.get("chain")})
        elif t == "payment_handle":
            val = a.get("value") or f"{a.get('rail')}:{a.get('id')}"
            out.append({"type": "payment_handle", "value": str(val).lower(), "rail": a.get("rail")})
        elif t == "bank":
            out.append({"type": "bank", "value": a.get("hash") or a.get("value"), "last4": a.get("last4")})
        elif t == "instruction_to_ai":
            out.append({"type": t, "value": a.get("text") or a.get("value"), "target": a.get("target"),
                        "requested_kind": a.get("requested_kind", "mark_number_safe")})
        else:
            out.append({"type": t, "value": a.get("value")})
    return [a for a in out if a.get("value")]


def key(a: dict) -> str:
    t, v = a["type"], str(a["value"])
    if t in ("callback_phone", "calling_number"):
        return norm_phone(v)
    if t in ("domain", "url"):
        return norm_domain(v)
    return v.strip().lower() if t != "wallet" else v.strip()


def _jaccard(a, b) -> float:
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def _campaign_lists(store, cid: str) -> dict:
    rows = store.q("SELECT type, value, strong FROM indicators WHERE campaign_id=?", cid)
    numbers = sorted({r["value"] for r in rows if r["type"] == "calling_number"})
    strong = [r for r in rows if r["strong"]]
    return {"indicators": [f'{r["type"]}:{r["value"]}' for r in strong],  # contract: list[str], strong only
            "numbers": numbers,                                          # contract: list[str]
            "n_indicators": len(rows), "calling_numbers": len(numbers),
            "strong_indicators": sorted({r["type"] for r in strong}), "immunity": store.immunity()}


def link_sighting(store, call_id: str, artifacts, calling_number: str | None = None, carrier: str | None = None,
                  day: str | None = None, stages: list[str] | None = None, allowlist_hits=(),
                  emit=default_emit, sim_threshold: float = 0.8) -> dict:
    arts = normalize_artifacts(artifacts)
    hits = set(allowlist_hits)  # already normalized by lookups.check_allowlist
    tags = sorted({a["value"] for a in arts if a["type"] == "script_tag"})
    stages = stages or []
    strong = [(a["type"] if a["type"] != "url" else "domain", key(a)) for a in arts
              if (a["type"] in STRONG or a["type"] == "url") and key(a) not in hits]

    cid, via = None, None
    for t, v in strong:
        r = store.q("SELECT campaign_id FROM indicators WHERE type=? AND value=?", t, v)
        if r:
            cid, via = r[0]["campaign_id"], f"shared {t}"
            break
    if cid is None and tags and stages:
        for c in store.q("SELECT * FROM campaigns"):
            if _jaccard(tags, json.loads(c["script_tags"] or "[]")) >= sim_threshold and json.loads(c["stages"] or "[]") == stages:
                cid, via = c["id"], "script match + same stage sequence"
                break
    new = cid is None
    now = time.time()
    org = next((a["value"] for a in arts if a["type"] == "impersonated_org"), None)
    if new:
        cid = "camp-" + uuid.uuid4().hex[:6]
        store.x("INSERT INTO campaigns VALUES(?,?,?,?,?,?,0,?,?)", cid, None, org, "observed",
                json.dumps(tags), json.dumps(stages), now, now)

    for t, v in strong:
        store.x("INSERT OR IGNORE INTO indicators VALUES(?,?,?,?,?,?)", t, v, cid, 1, call_id, now)
    for a in arts:
        if a["type"] in ("gift_card_brand", "remote_app", "impersonated_org"):
            store.x("INSERT OR IGNORE INTO indicators VALUES(?,?,?,?,?,?)", a["type"], key(a), cid, 0, call_id, now)
    if calling_number:
        store.x("INSERT OR IGNORE INTO indicators VALUES(?,?,?,?,?,?)", "calling_number", norm_phone(calling_number), cid, 0, call_id, now)
    if hits:
        store.x("UPDATE campaigns SET conflict=1 WHERE id=?", cid)
    store.x("INSERT INTO sightings(campaign_id,call_id,calling_number,carrier,day,created) VALUES(?,?,?,?,?,?)",
            cid, call_id, norm_phone(calling_number or ""), carrier or "unknown", day or date.today().isoformat(), now)

    sights = store.q("SELECT calling_number, carrier, day FROM sightings WHERE campaign_id=?", cid)
    # Demo independence rule: distinct (calling number, carrier, day). Production: different carriers AND days.
    independent = len({(s["calling_number"], s["carrier"], s["day"]) for s in sights})
    conflict = store.q("SELECT conflict FROM campaigns WHERE id=?", cid)[0]["conflict"]
    # Allowlisted values were excluded from the campaign's indicators above, so a poisoning attempt
    # (scammer giving a real bank's number) is recorded but does not stop confirmation.
    status = "confirmed" if independent >= 2 else ("corroborated" if len(sights) >= 2 else "observed")
    store.x("UPDATE campaigns SET status=?, updated=?, impersonated_org=COALESCE(impersonated_org, ?) WHERE id=?",
            status, now, org, cid)
    info = {"campaign_id": cid, "status": status, "new": new, "linked_via": via, "sightings": len(sights),
            "independent_sightings": independent, "poisoning_attempt_seen": bool(conflict),
            **_campaign_lists(store, cid)}
    emit("campaign.updated", call_id, info)
    return info


def campaign_calling_numbers(store, campaign_id: str) -> list[str]:
    return [r["value"] for r in store.q("SELECT value FROM indicators WHERE campaign_id=? AND type='calling_number'", campaign_id)]
