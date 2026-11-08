"""Reset the intel DB and seed one earlier synthetic sighting, for rehearsals and the live demo.

    python -m intel.seed_demo            # INTEL_DB (default intel/intel.db)
    python -m intel.seed_demo --check    # print state only, change nothing

Campaigns confirm only after 2 independent sightings, but the judge makes one call. The seed is "another Backfire
customer's decoy call yesterday": same wallet + callback number as the demo haul (intel/demo_config.json), a
different calling number, carrier and day. So the judge's call is sighting #2: the campaign confirms live and the
campaign block, Callback Protection and immunity counter all fire on stage.

Idempotent and fast (no network, no LLM): it clears rows instead of deleting the file, so a running hub keeps its
SQLite connection. It writes nothing to Maria's block list. The seed is a sighting only, not an action.
"""
from __future__ import annotations

import argparse
import sys
import time
from datetime import date, timedelta

from . import campaigns
from .demo_config import CFG, SEED_NUMBER, seed_haul
from .store import Store, default_store

TABLES = ("campaigns", "indicators", "sightings", "actions", "blocklist", "callback_warnings", "denied", "holds")
SEED_CALL_ID = "seed-yesterday"


def reset(store: Store) -> None:
    with store.lock:
        for t in TABLES:
            store.db.execute(f"DELETE FROM {t}")
        if store.db.execute("SELECT 1 FROM sqlite_master WHERE name='sqlite_sequence'").fetchone():
            store.db.execute("DELETE FROM sqlite_sequence")  # AUTOINCREMENT counters restart too
        store.db.commit()


def start_pending_transfer() -> dict | None:
    """Scripted demo moment: Maria starts a Zelle transfer to the scammer's destination in her banking app.
    ONE Nessie call, 3 s timeout; skipped silently with no key, no seed (python -m intel.seed_nessie) or any error,
    so /demo/reset stays fast and never fails because of Nessie."""
    try:
        from . import nessie as N
        ids, dest = N.load_ids(), CFG.get("payout_destination") or {}
        payee = (ids or {}).get("payee", {}).get("account_id")
        maria = (ids or {}).get("maria", {}).get("account_id")
        if not (payee and maria and dest.get("id")):
            return None
        body = {"transaction_date": date.today().isoformat(), "status": "pending",
                "amount": int(dest.get("demo_transfer_amount", 1800)), "description": f"Zelle to {dest['id']}"}
        r = N.request("POST", f"/accounts/{maria}/transfers", body=body, params={"payee_id": payee}, timeout=3)
        tid = N.created_id(r)
        return {"id": tid, "amount": body["amount"], "description": body["description"]} if tid else None
    except Exception:
        return None


def seed(store: Store | None = None, quiet: bool = False) -> dict:
    store = store or default_store()
    t0 = time.perf_counter()
    reset(store)
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    info = campaigns.link_sighting(store, SEED_CALL_ID, seed_haul(), calling_number=SEED_NUMBER,
                                   carrier="seed-carrier", day=yesterday, stages=CFG["stages"],
                                   emit=lambda *a, **k: None)  # silent: the screen starts clean
    info["nessie_pending_transfer"] = start_pending_transfer()
    ms = (time.perf_counter() - t0) * 1000
    if not quiet:
        ph = " (PLACEHOLDER values: set BACKFIRE_DEMO_DOMAIN / BACKFIRE_DEMO_WALLET)" if CFG.get("placeholder") else ""
        print(f"intel DB reset + seeded in {ms:.0f} ms -> {store.path}{ph}")
        print(f"  campaign {info['campaign_id']}: {info['status']}, {info['sightings']} sighting "
              f"(caller {SEED_NUMBER}, seed-carrier, {yesterday})")
        print(f"  shared indicators: {', '.join(info['indicators'])}")
        print("  next: the judge's call with this wallet or callback = sighting #2 -> campaign confirms live")
        pt = info["nessie_pending_transfer"]
        print(f"  Nessie: pending ${pt['amount']:,} '{pt['description']}' from Maria (scripted, mock bank)" if pt
              else "  Nessie: skipped (no key, not seeded, or unreachable)")
    return info


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="show current state, change nothing")
    a = ap.parse_args(argv)
    if a.check:
        s = default_store().state()
        print({k: (len(v) if isinstance(v, list) else v) for k, v in s.items()})
        return 0
    seed()
    return 0


if __name__ == "__main__":
    sys.exit(main())
