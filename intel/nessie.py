"""Capital One Nessie (mock bank sandbox) client for Backfire. All data is synthetic.

Fail open everywhere: 5 s timeout, never raises; a failure returns status "unavailable" and the call flow,
the intel chain and /demo/reset carry on unchanged. Key: NESSIE_API_KEY (env first, then repo-root .env),
sent as ?key= on every request and never logged.

Confirmed against the live API (2026-11-08, see intel/DECISIONS.md):
  POST /customers                         {first_name, last_name, address{street_number,street_name,city,state,zip}}
  POST /customers/{id}/accounts           {type:"Checking", nickname, rewards, balance}   (amounts are integers)
  POST /merchants                         {name, category:str, address, geocode{lat,lng}}
  POST /accounts/{id}/deposits            {medium:"balance", transaction_date, status, amount, description}
  POST /accounts/{id}/purchases           {merchant_id, medium:"balance", purchase_date, amount, status, description}
  POST /accounts/{id}/transfers?payee_id= {transaction_date, status, amount, description}  (payee only as query param)
  GET  /accounts/{id}/transfers[?type=payer]   transfers paid by that account (no payer/payee fields returned)
  GET|PUT|DELETE /transfers/{id}          PUT {"status": "cancelled"|"pending"} -> 202 (so a hold is undoable)
  GET  /enterprise/accounts/{id}, /enterprise/transfers/{id}, /enterprise/customers/{id}   read-only, by id
"""
from __future__ import annotations

import json
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path

import httpx

from .envkeys import env_secret

log = logging.getLogger("intel.nessie")
BASE = os.getenv("NESSIE_BASE", "https://api.nessieisreal.com").rstrip("/")
TIMEOUT = float(os.getenv("NESSIE_TIMEOUT", "5"))
IDS_PATH = Path(os.getenv("NESSIE_IDS", str(Path(__file__).with_name("nessie_ids.json"))))
SOURCE = "Capital One Nessie sandbox (mock bank data)"

_transport = None  # tests inject an httpx.MockTransport
ID_RE = re.compile(r"^[0-9a-fA-F-]{24,36}$")  # Nessie ids are UUIDs; anything else never reaches a URL path


def valid_id(x) -> bool:
    return isinstance(x, str) and bool(ID_RE.fullmatch(x))


def set_transport(transport) -> None:
    global _transport
    _transport = transport


def api_key() -> str | None:
    return env_secret("NESSIE_API_KEY")


def request(method: str, path: str, body: dict | None = None, params: dict | None = None,
            timeout: float | None = None) -> dict:
    """-> {"ok", "status", "code", "data", "error"}. Never raises."""
    if _transport is None and os.getenv("NESSIE_OFFLINE") == "1":  # unit tests: never touch the live sandbox
        return {"ok": False, "status": "unavailable", "code": None, "data": None, "error": "NESSIE_OFFLINE"}
    k = api_key()
    if not k:
        return {"ok": False, "status": "unavailable", "code": None, "data": None, "error": "no NESSIE_API_KEY"}
    try:
        with httpx.Client(timeout=timeout or TIMEOUT, transport=_transport) as c:
            r = c.request(method, BASE + path, params={"key": k, **(params or {})}, json=body)
        try:
            data = r.json()
        except ValueError:
            data = None
        ok = 200 <= r.status_code < 300
        return {"ok": ok, "status": "ok" if ok else "error", "code": r.status_code, "data": data,
                "error": None if ok else f"HTTP {r.status_code}"}
    except Exception as e:  # network, timeout, TLS: fail open
        return {"ok": False, "status": "unavailable", "code": None, "data": None, "error": type(e).__name__}


def get(path, **params):
    return request("GET", path, params=params)


def post(path, body, **params):
    return request("POST", path, body=body, params=params)


def put(path, body):
    return request("PUT", path, body=body)


def delete(path):
    return request("DELETE", path)


def created_id(res: dict) -> str | None:
    d = res.get("data") or {}
    return (d.get("objectCreated") or {}).get("_id") if isinstance(d, dict) else None


# ---------- demo IDs (intel/nessie_ids.json, committed so the hub uses the same mock bank) ----------
def load_ids() -> dict | None:
    try:
        return json.loads(IDS_PATH.read_text())
    except (OSError, ValueError):
        return None


def save_ids(ids: dict) -> None:
    IDS_PATH.write_text(json.dumps(ids, indent=2) + "\n")


# ---------- helpers used by the agent and the gate ----------
def pending_transfers(account_id: str, description_contains: str | None = None, timeout: float | None = None) -> dict:
    """Pending transfers paid by account_id. Nessie returns no payee on transfers, so the destination is matched
    on the description the customer's banking app wrote ("Zelle to <handle>")."""
    if not valid_id(account_id):
        return {"status": "unavailable", "transfers": [], "error": "invalid id"}
    r = request("GET", f"/accounts/{account_id}/transfers", params={"type": "payer"}, timeout=timeout)
    if r["code"] == 404:  # Nessie answers 404 "No transfers found" for an empty list
        return {"status": "ok", "transfers": []}
    if not r["ok"] or not isinstance(r["data"], list):
        return {"status": "unavailable", "transfers": [], "error": r["error"]}
    needle = (description_contains or "").lower()
    out = [{"id": t.get("id") or t.get("_id"), "amount": t.get("amount"), "date": t.get("transaction_date"),
            "description": t.get("description")}
           for t in r["data"] if t.get("status") == "pending" and needle in str(t.get("description", "")).lower()
           and valid_id(t.get("id") or t.get("_id"))]
    return {"status": "ok", "transfers": out}


def hold_transfer(transfer_id: str) -> dict:
    """Cancel a pending transfer: PUT status cancelled (verified to work); DELETE only if PUT is rejected."""
    if not valid_id(transfer_id):
        return {"ok": False, "error": "invalid id"}
    r = put(f"/transfers/{transfer_id}", {"status": "cancelled"})
    if r["ok"]:
        return {"ok": True, "method": "PUT", "status": "cancelled", "undoable": True}
    if r["status"] == "unavailable":
        return {"ok": False, "error": r["error"]}
    d = delete(f"/transfers/{transfer_id}")
    if d["ok"]:
        return {"ok": True, "method": "DELETE", "status": "deleted", "undoable": False}
    return {"ok": False, "error": d["error"] or r["error"]}


def release_transfer(transfer_id: str) -> bool:
    """Undo a hold: back to pending."""
    if not valid_id(transfer_id):
        return False
    return put(f"/transfers/{transfer_id}", {"status": "pending"})["ok"]


def transfer_status(transfer_id: str) -> str | None:
    if not valid_id(transfer_id):
        return None
    r = get(f"/transfers/{transfer_id}")
    return (r["data"] or {}).get("status") if r["ok"] and isinstance(r["data"], dict) else None


def payee_activity(payee_account_id: str, evidence_transfer_ids: list[str]) -> dict:
    """Bank-wide evidence via enterprise READ-ONLY endpoints, by id (the enterprise list endpoints return the
    whole sandbox and time out). Nessie doesn't expose payee on transfers, so the seed records which completed
    transfers went to this payee and each one is re-verified here."""
    if not valid_id(payee_account_id):
        return {"status": "unavailable", "count": 0, "error": "invalid id"}
    acct = get(f"/enterprise/accounts/{payee_account_id}")
    if not acct["ok"]:
        return {"status": "unavailable", "count": 0, "error": acct["error"]}
    n, total = 0, 0
    tids = [t for t in evidence_transfer_ids if valid_id(t)]
    with ThreadPoolExecutor(max_workers=max(1, min(8, len(tids)))) as pool:   # parallel: one round-trip, not N
        reads = list(pool.map(lambda tid: get(f"/enterprise/transfers/{tid}"), tids))
    for t in reads:
        if not t["ok"]:
            if t["status"] == "unavailable":
                return {"status": "unavailable", "count": 0, "error": t["error"]}
            continue
        if (t["data"] or {}).get("status") == "completed":
            n += 1
            total += (t["data"] or {}).get("amount") or 0
    return {"status": "ok", "count": n, "total": total}


# ---------- destination matching (captured values stay in intel; Nessie only holds the mock payee) ----------
def destinations() -> list[dict]:
    from .demo_config import load
    d = load().get("payout_destination")
    return [d] if d and d.get("nessie_payee_account_id") else []


def dest_key(d: dict) -> str:
    return f"{d.get('rail')}:{d.get('id')}".strip().lower()


def allow_key(handle_id: str) -> str | None:
    """What to check against the verified-business allowlist: an email handle's domain, or a phone handle."""
    h = str(handle_id or "").split(":", 1)[-1].strip()
    if "@" in h:
        return h.rsplit("@", 1)[1].lower()
    return h if sum(c.isdigit() for c in h) >= 7 else None


def canon_handle(v) -> str:
    """Payment handle as STT/LLM might spell it -> one canonical form (P2 #137: 'refunds department at backfire dash demo
    dot example' and 'zelle:refunds.department@...' must match the payee 'zelle:refunds.dept@backfire-demo.example')."""
    t = " " + str(v or "").lower().strip() + " "
    for w, r in ((" dot ", "."), (" at ", "@"), (" dash ", "-"), (" hyphen ", "-"), (" underscore ", "_")):
        while w in t:
            t = t.replace(w, r)
    t = re.sub(r"\s*([.@_:-])\s*", r"\1", t.strip()).rstrip(".,;!? ")
    rail, hid = (t.split(":", 1) if re.match(r"^[a-z]+:", t) else ("", t))
    if "@" in hid:
        local, dom = hid.rsplit("@", 1)
        local = re.sub(r"\s+", ".", local)
        local = re.sub(r"(?<![a-z])(?:department|departement|depart|dep't)(?![a-z])", "dept", local)
        hid = local + "@" + dom.replace(" ", "")
    return f"{rail}:{hid}" if rail else hid


def _lev(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def handles_match(heard, payee) -> bool:
    """Tolerant payee match for STT-garbled handles (dev risk 6: no Zelle hold seen live). Exact canonical match first; else same rail
    (a missing rail on the heard side is fine), the domains equal once dots/dashes are dropped ('backfire demo dot example' lost its dash),
    and the local parts equal once separators are dropped or within a small edit distance ('refund stepped' for 'refunds dept').
    Only ever compared against the customer's own known payee, so a near-miss costs nothing but a reversible hold."""
    h, p = canon_handle(heard), canon_handle(payee)
    if h == p:
        return True
    def split(v):
        rail, hid = (v.split(":", 1) if re.match(r"^[a-z]+:", v) else ("", v))
        if "@" not in hid:
            return rail, None, None
        local, dom = hid.rsplit("@", 1)
        return rail, re.sub(r"[.\-_\s]", "", local), re.sub(r"[.\-_\s]", "", dom)
    hr, hl, hd = split(h); pr, pl, pd = split(p)
    if hl is None or pl is None or not hd or hd != pd or (hr and pr and hr != pr):
        return False
    if hl == pl:
        return True
    n = max(len(hl), len(pl))
    limit = 0 if n < 6 else 2 if n < 10 else max(3, round(n * 0.3))   # 'refundstepped' vs 'refundsdept' is 4 edits over 13 chars
    return _lev(hl, pl) <= limit


def match_destinations(arts: list[dict]) -> list[dict]:
    """Artifacts (normalized by campaigns.normalize_artifacts) that point at a known mock payee.
    payment_handle: normalized rail:id. bank: account-number hash, else last4."""
    hits, seen = [], set()
    for d in destinations():
        for a in arts:
            if a["type"] == "payment_handle":
                ok = handles_match(a.get("value"), dest_key(d))
            elif a["type"] == "bank":
                ok = bool(d.get("bank_hash")) and str(a.get("value", "")).lower() == str(d["bank_hash"]).lower() or \
                     bool(d.get("bank_last4")) and str(a.get("last4") or "") == str(d["bank_last4"])
            else:
                ok = False
            if ok and dest_key(d) not in seen:
                seen.add(dest_key(d))
                hits.append({"dest": d, "artifact": a})
    return hits


def lookup_destination(hit: dict, call_id: str | None = None, emit=None) -> tuple[dict, list[dict]]:
    """intel.lookup (source "nessie"): the customer's pending transfers to this payee + bank-wide activity.
    Returns (public result, pending transfers). Transfer ids never go into the event or to the LLM."""
    from . import lookups as L
    d = hit["dest"]
    ids = load_ids() or {}
    res = {"kind": "bank_transfer", "artifact_kind": hit["artifact"]["type"], "value": dest_key(d),
           "source": "nessie", "source_label": SOURCE, "simulated": True}
    maria = (ids.get("maria") or {}).get("account_id")
    if not maria:
        res.update(status="unavailable", reason="Nessie not seeded (python -m intel.seed_nessie)")
        L._emit_lookup(call_id, res)
        return res, []
    pend = pending_transfers(maria, description_contains=str(d.get("id")))
    act = payee_activity(d["nessie_payee_account_id"], ids.get("evidence_transfer_ids") or []) \
        if pend["status"] == "ok" else {"status": "unavailable", "count": 0}
    if pend["status"] != "ok" or act["status"] != "ok":
        res.update(status="unavailable", reason=f"lookup unavailable ({pend.get('error') or act.get('error')})")
        L._emit_lookup(call_id, res)
        return res, []
    tr = pend["transfers"]
    res.update(status="ok", pending_count=len(tr), pending_total=sum(t["amount"] or 0 for t in tr),
               activity_count=act["count"], activity_total=act["total"],
               summary=f"{len(tr)} pending transfer(s) from the customer to this payee; {act['count']} other customers sent money to it")
    L._emit_lookup(call_id, res)
    return res, tr


# ---------- laundering chain (read-only view for GET /intel/chain and the /intel/map page) ----------
_edge_cache: dict = {"t": 0.0, "edges": None}
EDGE_TTL = float(os.getenv("NESSIE_CHAIN_TTL", "60"))  # completed transfers don't change; the map polls every 3 s


def _confirm_edges(edges: list[dict]) -> tuple[list[dict], str]:
    """Confirm each recorded edge by id (enterprise read-only). Nessie down -> seeded values, status unavailable."""
    now = time.time()
    if _edge_cache["edges"] is not None and now - _edge_cache["t"] < EDGE_TTL:
        return _edge_cache["edges"], "ok"
    tids = [e.get("transfer_id") for e in edges]
    with ThreadPoolExecutor(max_workers=8) as pool:
        reads = list(pool.map(lambda tid: get(f"/enterprise/transfers/{tid}") if valid_id(tid) else None, tids))
    if any(r is not None and r["status"] == "unavailable" for r in reads):
        return [dict(e) for e in edges], "unavailable"
    out = []
    for e, r in zip(edges, reads):
        e = dict(e)
        if r is not None and r["ok"] and isinstance(r["data"], dict):
            e["amount"] = r["data"].get("amount", e["amount"])
            e["date"] = r["data"].get("transaction_date", e["date"])
            e["bank_status"] = r["data"].get("status")
        out.append(e)
    _edge_cache.update(t=now, edges=out)
    return out, "ok"


def chain(active_holds: list[dict] | None = None) -> dict:
    """Graph for the map. Built from the RECORDED chain in nessie_ids.json (Nessie can't be queried for it).
    the customer's edge is held when one of this reset's holds (intel store) reads cancelled in Nessie."""
    ids = load_ids() or {}
    c = ids.get("chain")
    if not c:
        return {"status": "unavailable", "reason": "chain not seeded (python -m intel.seed_nessie)", "nodes": [],
                "edges": [], "simulated": True}
    static = [e for e in c["edges"] if not e.get("dynamic")]
    maria_e = next((dict(e) for e in c["edges"] if e.get("dynamic")), None)
    edges, status = _confirm_edges(static)
    edges = [{**e, "held": False} for e in edges]
    if maria_e:
        held_amt = None
        for h in active_holds or []:
            st = transfer_status(h.get("transfer_id"))
            if st is None and h.get("transfer_id"):
                status = "unavailable"
            if st == "cancelled":
                held_amt = h.get("amount") or held_amt or maria_e["amount"]
        maria_e.update(held=held_amt is not None, amount=held_amt or maria_e["amount"],
                       date=maria_e.get("date") or time.strftime("%Y-%m-%d"),
                       bank_status="cancelled" if held_amt is not None else "pending")
        edges.insert(0, maria_e)
    totals = {n["id"]: {"in": 0, "out": 0} for n in c["nodes"]}
    for e in edges:
        if e["held"]:
            continue  # a cut edge moves no money
        totals[e["src"]]["out"] += e["amount"]
        if not e.get("dynamic"):  # the customer's pending transfer hasn't reached the mule (yet, or ever if Backfire holds it)
            totals[e["dst"]]["in"] += e["amount"]
    nodes = [{"id": n["id"], "label": n["label"], "role": n["role"],
              "total_in": totals[n["id"]]["in"], "total_out": totals[n["id"]]["out"]} for n in c["nodes"]]
    victims_in = [e for e in edges if e["dst"] == "mule" and e["src"] != "maria"]
    return {"status": status, "nodes": nodes,
            "edges": [{"src": e["src"], "dst": e["dst"], "amount": e["amount"], "date": e["date"],
                       "held": bool(e["held"]), "kind": "target" if e["src"] == "maria" else
                       ("cashout" if e["dst"] == "cashout" else "victim")} for e in edges],
            "victim_count": len({e["src"] for e in victims_in}),
            "mule_total_in": sum(e["amount"] for e in victims_in),
            "mule_total_out": sum(e["amount"] for e in edges if e["src"] == "mule"),
            "held_count": sum(1 for e in edges if e["held"]),
            "held_amount": sum(e["amount"] for e in edges if e["held"]),
            "simulated": True, "source": SOURCE}
