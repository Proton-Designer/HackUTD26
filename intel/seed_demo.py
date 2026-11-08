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

TABLES = ("campaigns", "indicators", "sightings", "actions", "blocklist", "callback_warnings", "denied")
SEED_CALL_ID = "seed-yesterday"


def reset(store: Store) -> None:
    with store.lock:
        for t in TABLES:
            store.db.execute(f"DELETE FROM {t}")
        if store.db.execute("SELECT 1 FROM sqlite_master WHERE name='sqlite_sequence'").fetchone():
            store.db.execute("DELETE FROM sqlite_sequence")  # AUTOINCREMENT counters restart too
        store.db.commit()


def seed(store: Store | None = None, quiet: bool = False) -> dict:
    store = store or default_store()
    t0 = time.perf_counter()
    reset(store)
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    info = campaigns.link_sighting(store, SEED_CALL_ID, seed_haul(), calling_number=SEED_NUMBER,
                                   carrier="seed-carrier", day=yesterday, stages=CFG["stages"],
                                   emit=lambda *a, **k: None)  # silent: the screen starts clean
    ms = (time.perf_counter() - t0) * 1000
    if not quiet:
        ph = " (PLACEHOLDER values: set BACKFIRE_DEMO_DOMAIN / BACKFIRE_DEMO_WALLET)" if CFG.get("placeholder") else ""
        print(f"intel DB reset + seeded in {ms:.0f} ms -> {store.path}{ph}")
        print(f"  campaign {info['campaign_id']}: {info['status']}, {info['sightings']} sighting "
              f"(caller {SEED_NUMBER}, seed-carrier, {yesterday})")
        print(f"  shared indicators: {', '.join(info['indicators'])}")
        print("  next: the judge's call with this wallet or callback = sighting #2 -> campaign confirms live")
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
