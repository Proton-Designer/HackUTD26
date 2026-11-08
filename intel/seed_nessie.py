"""One-time, idempotent seed of the Capital One Nessie mock bank for the demo. All people and data are synthetic.

    python -m intel.seed_nessie            # skip if intel/nessie_ids.json still resolves, else create
    python -m intel.seed_nessie --force    # create a fresh set (old objects are left in the sandbox)

Creates: "Maria Sandbox" checking (~$4,200) with 45 days of history (weekly paycheck deposits; groceries, gas,
phone bill, streaming and more against 9 fake merchants); 3 other mock customers with checking; one payee account
labeled as the SIMULATED scammer destination; 3 completed transfers from the other customers to that payee over the
past 2 weeks (bank-wide evidence). Every id goes to intel/nessie_ids.json (committed, so the hub uses the same mock
bank with the same key) and the payee mapping goes to intel/demo_config.json -> payout_destination.
Nessie amounts are integers (decimals get truncated), so all amounts are whole dollars.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import date, timedelta
from pathlib import Path

from . import nessie as N

ADDR = {"street_number": "100", "street_name": "Synthetic Demo Ave", "city": "Testville", "state": "TX", "zip": "75080"}
MERCHANTS = [("Fake Fresh Grocery (demo)", "grocery"), ("Demo Fuel Stop (fake)", "gas"),
             ("Sandbox Wireless (fake phone carrier)", "utilities"), ("StreamFake Video (demo)", "entertainment"),
             ("Mock Pharmacy (demo)", "health"), ("Pretend Coffee Co (demo)", "food"),
             ("Fictional Diner (demo)", "food"), ("Demo Hardware (fake)", "home"), ("Placeholder Books (demo)", "shopping")]
OTHERS = [("Alex", "Sandbox"), ("Priya", "Sandbox"), ("Jordan", "Sandbox")]
EVIDENCE = [(13, 950), (8, 2400), (3, 1500)]  # (days ago, amount) completed transfers to the payee
# Laundering chain (additive): more victims paying the mule, then the mule's hop to a cash-out account.
EXTRA_VICTIMS = [("Sam", 11, 3200), ("Taylor", 9, 4100), ("Morgan", 6, 2650), ("Casey", 4, 3300)]  # +13,250 -> 18,100 in
CASHOUT_HOPS = [(7, 6000), (5, 7500), (2, 3800)]  # (days ago, amount) mule -> cash-out, 17,300 out
CONFIG = Path(__file__).with_name("demo_config.json")


def _ok(res: dict, what: str) -> str:
    oid = N.created_id(res)
    if not oid:
        raise RuntimeError(f"Nessie: could not create {what} ({res.get('error')})")
    return oid


def _customer(first: str, last: str) -> str:
    return _ok(N.post("/customers", {"first_name": first, "last_name": last, "address": ADDR}), f"customer {first}")


def _checking(cid: str, nickname: str, balance: int) -> tuple[str, str]:
    r = N.post(f"/customers/{cid}/accounts", {"type": "Checking", "nickname": nickname, "rewards": 0, "balance": balance})
    return _ok(r, f"account {nickname}"), str((r["data"] or {}).get("objectCreated", {}).get("account_number", ""))


def resolves(ids: dict | None) -> bool | None:
    """True if the customer's and the payee's accounts still exist; None if Nessie is unreachable."""
    if not ids:
        return False
    for acc in (ids.get("maria", {}).get("account_id"), ids.get("payee", {}).get("account_id")):
        r = N.get(f"/accounts/{acc}")
        if r["status"] == "unavailable":
            return None
        if not r["ok"]:
            return False
    return True


def _transfer(src: str, dst: str, days_ago: int, amount: int, what: str) -> dict:
    day = (date.today() - timedelta(days=days_ago)).isoformat()
    r = N.post(f"/accounts/{src}/transfers",
               {"transaction_date": day, "status": "completed", "amount": amount, "description": "Zelle payment"},
               payee_id=dst)
    return {"src_account": src, "dst_account": dst, "transfer_id": _ok(r, what), "amount": amount, "date": day}


def seed_chain(ids: dict, say=print) -> dict:
    """Add the laundering chain to an existing seed WITHOUT touching Maria, the mule (payee) or her flow.
    Nessie transfer reads return no payer/payee and the list endpoints time out, so the graph is RECORDED here as an
    edge list (ids["chain"]) and only confirmed by id at read time, never discovered."""
    mule = ids["payee"]["account_id"]
    edges = []
    # existing evidence edges: confirm amount/date by id (fast enterprise read), else the seeded constants
    for (days, amt), o, tid in zip(EVIDENCE, ids["others"][:len(EVIDENCE)], ids["evidence_transfer_ids"]):
        t = N.get(f"/enterprise/transfers/{tid}")
        td = t["data"] if t["ok"] and isinstance(t["data"], dict) else {}
        edges.append({"src_account": o["account_id"], "dst_account": mule, "transfer_id": tid,
                      "amount": td.get("amount", amt),
                      "date": td.get("transaction_date", (date.today() - timedelta(days=days)).isoformat())})
    for first, days, amt in EXTRA_VICTIMS:
        cid = _customer(first, "Sandbox")
        aid, _ = _checking(cid, f"{first} checking (synthetic)", 2500 + amt)
        ids["others"].append({"name": f"{first} Sandbox", "customer_id": cid, "account_id": aid})
        e = _transfer(aid, mule, days, amt, f"victim transfer {first}")
        ids["evidence_transfer_ids"].append(e["transfer_id"])
        edges.append(e)
    co_c = _customer("SIMULATED", "CashOut")
    co_a, _ = _checking(co_c, "SIMULATED cash-out account (demo)", 0)
    ids["cashout"] = {"label": "SIMULATED cash-out account", "customer_id": co_c, "account_id": co_a}
    for days, amt in CASHOUT_HOPS:
        edges.append(_transfer(mule, co_a, days, amt, "cash-out hop"))

    nodes = [{"id": "maria", "role": "target", "label": "The customer (protected by Backfire)",
              "account_id": ids["maria"]["account_id"]}]
    nodes += [{"id": f"v{i + 1}", "role": "victim", "label": o["name"], "account_id": o["account_id"]}
              for i, o in enumerate(ids["others"])]
    nodes += [{"id": "mule", "role": "mule", "label": "SIMULATED mule account (scammer destination)", "account_id": mule},
              {"id": "cashout", "role": "cashout", "label": "SIMULATED cash-out account", "account_id": co_a}]
    by_acct = {n["account_id"]: n["id"] for n in nodes}
    for e in edges:
        e["src"], e["dst"] = by_acct[e["src_account"]], by_acct[e["dst_account"]]
    # the customer's edge is the one Backfire cuts. Its transfer is created at every /demo/reset, so it's resolved live.
    edges.insert(0, {"src": "maria", "dst": "mule", "src_account": ids["maria"]["account_id"], "dst_account": mule,
                     "transfer_id": None, "dynamic": "maria_pending_demo_transfer",
                     "amount": int(json.loads(CONFIG.read_text()).get("payout_destination", {})
                                   .get("demo_transfer_amount", 1800)), "date": None})
    ids["chain"] = {"_note": "Recorded edge list (not discovered): Nessie transfers expose no payer/payee. Synthetic.",
                    "nodes": nodes, "edges": edges}
    N.save_ids(ids)
    n_in = sum(e["amount"] for e in edges if e["dst"] == "mule" and e["src"] != "maria")
    say(f"  chain: {len(ids['others'])} victims -> mule (${n_in:,}) -> cash-out "
        f"(${sum(a for _, a in CASHOUT_HOPS):,} in {len(CASHOUT_HOPS)} hops); the customer's edge resolved live")
    return ids


def resolves_account(account_id: str) -> bool:
    return bool(N.get(f"/accounts/{account_id}")["ok"])


def seed(force: bool = False, quiet: bool = False) -> dict:
    say = (lambda *a: None) if quiet else print
    if not N.api_key():
        say("NESSIE_API_KEY not set (env or repo-root .env): nothing to do")
        return {"status": "no_key"}
    existing = N.load_ids()
    if not force:
        r = resolves(existing)
        if r is None:
            say("Nessie unreachable: keeping intel/nessie_ids.json as is (fail open)")
            return {"status": "unavailable"}
        if r and existing.get("chain") and existing.get("cashout") and resolves_account(existing["cashout"]["account_id"]):
            say(f"Nessie already seeded (intel/nessie_ids.json resolves, chain present): skip")
            return {"status": "exists", **existing}
        if r:
            say("Nessie base seed resolves; adding the laundering chain (additive)")
            return {"status": "extended", **seed_chain(existing, say)}
    t0 = time.time()
    today = date.today()
    d = lambda n: (today - timedelta(days=n)).isoformat()

    maria_c = _customer("Demo", "Customer")
    maria_a, _ = _checking(maria_c, "Customer checking (synthetic)", 4200)
    merchants = []
    for name, cat in MERCHANTS:
        merchants.append(_ok(N.post("/merchants", {"name": name, "category": cat, "address": ADDR,
                                                  "geocode": {"lat": 32.99, "lng": -96.75}}), name))
    groc, gas, phone, stream = merchants[0], merchants[1], merchants[2], merchants[3]
    n_tx = 0
    for day in range(45, 0, -7):  # weekly paycheck + groceries
        N.post(f"/accounts/{maria_a}/deposits", {"medium": "balance", "transaction_date": d(day), "status": "completed",
                                                 "amount": 1150, "description": "Paycheck (synthetic employer)"})
        N.post(f"/accounts/{maria_a}/purchases", {"merchant_id": groc, "medium": "balance", "purchase_date": d(day - 1),
                                                  "amount": 85 + day % 20, "status": "completed", "description": "Groceries"})
        n_tx += 2
    for day, mid, amt, desc in [(40, gas, 42, "Gas"), (26, gas, 39, "Gas"), (12, gas, 45, "Gas"),
                                (38, phone, 65, "Phone bill"), (8, phone, 65, "Phone bill"),
                                (35, stream, 16, "Streaming subscription"), (5, stream, 16, "Streaming subscription"),
                                (30, merchants[4], 24, "Pharmacy"), (21, merchants[5], 6, "Coffee"),
                                (17, merchants[6], 31, "Diner"), (14, merchants[7], 58, "Hardware"),
                                (9, merchants[8], 19, "Books"), (2, merchants[5], 5, "Coffee")]:
        N.post(f"/accounts/{maria_a}/purchases", {"merchant_id": mid, "medium": "balance", "purchase_date": d(day),
                                                  "amount": amt, "status": "completed", "description": desc})
        n_tx += 1

    others = []
    for first, last in OTHERS:
        cid = _customer(first, last)
        aid, _ = _checking(cid, f"{first} checking (synthetic)", 3000 + 500 * len(others))
        others.append({"name": f"{first} {last}", "customer_id": cid, "account_id": aid})
    payee_c = _customer("SIMULATED", "ScammerDestination")
    payee_a, payee_num = _checking(payee_c, "SIMULATED scammer destination (demo payee)", 0)
    evidence = []
    for (days, amt), o in zip(EVIDENCE, others):
        r = N.post(f"/accounts/{o['account_id']}/transfers",
                   {"transaction_date": d(days), "status": "completed", "amount": amt, "description": "Zelle payment"},
                   payee_id=payee_a)
        evidence.append(_ok(r, "evidence transfer"))

    ids = {"_note": "Synthetic Nessie sandbox objects for the Backfire demo (python -m intel.seed_nessie). No real people.",
           "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "base": N.BASE,
           "maria": {"name": "Demo Customer", "customer_id": maria_c, "account_id": maria_a},
           "others": others,
           "payee": {"label": "SIMULATED scammer destination", "customer_id": payee_c, "account_id": payee_a},
           "merchants": merchants, "evidence_transfer_ids": evidence}
    N.save_ids(ids)
    seed_chain(ids, say)
    cfg = json.loads(CONFIG.read_text())
    pd = cfg.setdefault("payout_destination", {})
    pd.update(nessie_payee_account_id=payee_a, bank_last4=payee_num[-4:] or None,
              bank_hash=hashlib.sha256(payee_num.encode()).hexdigest() if payee_num else None)
    CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")
    say(f"Nessie seeded in {time.time() - t0:.1f} s: Maria + {n_tx} history items, {len(merchants)} merchants, "
        f"{len(others)} other customers, payee, {len(evidence)} completed transfers to the payee")
    say("  ids -> intel/nessie_ids.json, payee mapping -> intel/demo_config.json payout_destination")
    return {"status": "created", **ids}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args(argv)
    try:
        r = seed(force=a.force)
    except RuntimeError as e:
        print(e)
        return 1
    return 0 if r["status"] in ("created", "extended", "exists", "no_key", "unavailable") else 1


if __name__ == "__main__":
    sys.exit(main())
