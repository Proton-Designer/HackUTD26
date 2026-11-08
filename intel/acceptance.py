"""P4 acceptance checklist over HTTP against a running hub (P1's server with intel mounted).

    python -m intel.acceptance --hub http://127.0.0.1:8000 [--token HUB_TOKEN]

Uses only public endpoints: POST /intel/ingest, POST /intel/actions/{id}/approve, GET /routing/lookup,
GET /intel/state. Synthetic 555 numbers only. Lookups are real (RDAP, public BTC explorer) and the agent
uses whatever engine the hub runs, so it reports engine=nemotron|fallback honestly. Exit code 0 = all pass.
"""
from __future__ import annotations

import argparse
import sys
import time
import uuid

import httpx

from .demo_config import CFG, JUDGE_NUMBER, SEED_NUMBER, judge_haul, seed_haul


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub", default="http://127.0.0.1:8000")
    ap.add_argument("--token", default=None, help="HUB_TOKEN if the hub requires one")
    ap.add_argument("--domain", default=CFG["domain"])
    ap.add_argument("--wallet", default=CFG["wallet"]["addr"])
    ap.add_argument("--require-nemotron", action="store_true",
                    help="demo readiness: fail 2a unless the agent ran on Nemotron (not the template fallback)")
    ap.add_argument("--nessie", action="store_true",
                    help="Capital One Nessie check: POST /demo/reset first (starts Maria's pending transfer), then expect "
                         "hold_transfer applied and the transfer cancelled in Nessie. Run on the hub machine.")
    ap.add_argument("--drill", action="store_true",
                    help="fail-open drill: hub runs with INTEL_*_BASE pointed at a dead host; expect 'unavailable' lookups")
    a = ap.parse_args(argv)
    cfg = {**CFG, "domain": a.domain}
    if a.wallet != CFG["wallet"]["addr"]:
        cfg["wallet"] = {"chain": "ETH" if a.wallet.lower().startswith("0x") else "BTC", "addr": a.wallet}
    h = {"Authorization": f"Bearer {a.token}", "X-Hub-Token": a.token} if a.token else {}
    c = httpx.Client(base_url=a.hub.rstrip("/"), headers=h, timeout=90)
    run = uuid.uuid4().hex[:6]
    results: list[tuple[bool, str, str]] = []

    def check(ok: bool, name: str, detail: str = "") -> None:
        results.append((ok, name, detail))
        print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}", flush=True)

    if a.nessie:
        from . import nessie as N
        ids, dest = N.load_ids(), CFG.get("payout_destination") or {}
        maria = (ids or {}).get("maria", {}).get("account_id")
        from .seed_nessie import resolves
        check(bool(ids) and resolves(ids) is True, "N1 Nessie seed exists and resolves (intel/nessie_ids.json)",
              f"maria={'set' if maria else None} payee={'set' if dest.get('nessie_payee_account_id') else None}")
        try:
            rr = c.post("/demo/reset", headers={"x-hub-token": a.token or ""})
            rr.raise_for_status()
        except Exception as e:
            print(f"FAIL  /demo/reset: {type(e).__name__}: {e}")
            return 2
        pend = N.pending_transfers(maria, description_contains=str(dest.get("id"))) if maria else {"transfers": []}
        check(len(pend.get("transfers", [])) >= 1, "N2 /demo/reset started Maria's pending Zelle transfer (Nessie)",
              ", ".join(f"${t['amount']:,} '{t['description']}'" for t in pend.get("transfers", [])))
    try:
        before = c.get("/routing/lookup", params={"from": JUDGE_NUMBER}).json()
        print(f"before: {before}")
        c.post("/intel/ingest", json={"call_id": f"acc-seed-{run}", "calling_number": SEED_NUMBER, "carrier": "carrier-x",
                                      "artifacts": seed_haul(cfg)}).raise_for_status()
        t0 = time.time()
        r = c.post("/intel/ingest", json={"call_id": f"acc-judge-{run}", "calling_number": JUDGE_NUMBER,
                                          "carrier": "carrier-y", "attestation": "C",
                                          "scammer_transcript": "NEVER READ", "artifacts": judge_haul(cfg)})
        r.raise_for_status()
        out, dt = r.json(), time.time() - t0
    except Exception as e:
        print(f"FAIL  hub unreachable or intel not mounted: {type(e).__name__}: {e}")
        return 2

    lk = {l.get("artifact_kind"): l for l in out.get("lookups", []) if l.get("kind") in ("domain", "wallet")}
    dom, wal = lk.get("domain", {}), lk.get("wallet", {})
    detail = (f"domain={dom.get('status')} age_days={dom.get('age_days')} registrar={dom.get('registrar')} "
              f"| wallet={wal.get('status')} received={wal.get('total_received')} tx={wal.get('tx_count')} | {dt:.1f}s")
    if a.drill:
        check(dom.get("status") == "unavailable" and wal.get("status") == "unavailable"
              and all("unavailable" in str(x.get("reason", "")) for x in (dom, wal)),
              "1 DRILL lookups fail open as 'lookup unavailable' (no crash, event still emitted)",
              f"{detail} | reason={dom.get('reason')}")
    else:
        check(dom.get("status") in ("ok", "not_found") and wal.get("status") == "ok" and not wal.get("simulated"),
              "1 real domain age + on-chain inflows", detail)
    acts = out.get("actions", [])
    ok_engines = ("nemotron",) if a.require_nemotron else ("nemotron", "fallback")
    check(out.get("engine") in ok_engines, "2a agent ran" + (" on Nemotron" if a.require_nemotron else ""),
          f"engine={out.get('engine')}" + ("" if out.get("engine") == "nemotron"
                                           else "  (no NVIDIA_API_KEY on the hub machine? see intel/README.md)"))
    auto = [x["kind"] for x in acts if x.get("status") == "applied"]
    check("block_caller_for_customer" in auto, "2b auto actions applied", ", ".join(auto))
    q = [x for x in acts if x.get("kind") == "network_number_block" and x.get("status") == "queued"]
    if q:
        ap_ = c.post(f"/intel/actions/{q[0]['action_id']}/approve").json()
        check(ap_.get("status") == "approved", "2c network-wide block waits for Approve, then simulated: applied",
              str((ap_.get("action") or {}).get("status")))
    else:
        check(False, "2c network-wide block queued", "no queued network_number_block")
    rt = c.get("/routing/lookup", params={"from": JUDGE_NUMBER}).json()
    check(rt.get("decision") == "BLOCKED_BACKFIRE" and "blocked for her" in str(rt.get("reason", "")),
          "3 callback rejected before ring via intel gate", str(rt))
    den = [x for x in acts if x.get("status") == "denied"]
    kinds = {x["kind"] for x in den}
    check({"mark_number_safe", "add_trusted_contact"} <= kinds, "4 'mark safe / add as her bank' -> denied",
          ", ".join(sorted(kinds)))
    pois = [x for x in den if "".join(ch for ch in str(x.get("target")) if ch.isdigit())[-7:]
            == "".join(ch for ch in CFG["real_bank_callback"] if ch.isdigit())[-7:]
            and "poisoning" in str(x.get("gate_status", ""))]
    check(bool(pois), "5 real bank's number flagged as attempted poisoning, never actioned")
    if a.nessie:
        from . import nessie as N
        hold = [x for x in acts if x.get("kind") == "hold_transfer"]
        applied = [x for x in hold if x.get("status") == "applied"]
        check(bool(applied), "N3 hold_transfer applied (auto, her scope, simulated)",
              applied[0].get("reason", "") if applied else f"hold actions: {[x.get('gate_status') for x in hold]}")
        st = [N.transfer_status(x["target"]) for x in applied]
        check(bool(st) and all(s_ == "cancelled" for s_ in st), "N4 transfer shows cancelled in Nessie", str(st))
        flag = [x for x in acts if x.get("kind") == "flag_payee_bankwide"]
        check(bool(flag) and flag[0].get("status") == "queued", "N5 flag_payee_bankwide queued for analyst",
              (flag[0].get("evidence") or [""])[0] if flag else "")
    n_ok = sum(ok for ok, _, _ in results)
    print(f"\n{n_ok}/{len(results)} pass (run {run}; synthetic numbers; network actions simulated)")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
