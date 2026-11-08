"""Backfire P4a: real public lookups (never cut).

Each lookup takes an extracted artifact value, calls only public read-only
sources, returns typed JSON, and emits an `intel.lookup` event.
On any network error or timeout it fails open with status "unavailable".
We never contact scammer infrastructure: RDAP registries and public block
explorers only.

CLI:
  python -m intel.lookups domain example.com
  python -m intel.lookups wallet bc1q...            (BTC)  or 0x... (ETH)
  python -m intel.lookups allow 1-800-935-9935      (phone or domain)
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

TIMEOUT = float(os.getenv("INTEL_LOOKUP_TIMEOUT", "6"))
UA = {"User-Agent": "backfire-hackutd-intel/0.1"}
ALLOWLIST_PATH = Path(__file__).with_name("allowlist.json")
EVENTS_URL = os.getenv("BACKFIRE_EVENTS_URL")  # optional: P1 publish endpoint


# ---------- events ----------
def emit(event_type: str, call_id: str | None, data: dict) -> dict:
    """Emit a contract envelope. Prints always; POSTs to P1 if BACKFIRE_EVENTS_URL is set."""
    ev = {"type": event_type, "call_id": call_id, "ts": time.time(), "data": data}
    print(json.dumps(ev), flush=True)
    if EVENTS_URL:
        try:
            httpx.post(EVENTS_URL, json=ev, timeout=2)
        except Exception:
            pass  # fail open: the screen just misses one event
    return ev


def _unavailable(kind: str, value: str, err: str) -> dict:
    return {"kind": kind, "value": value, "status": "unavailable",
            "reason": f"lookup unavailable ({err})", "source": None, "simulated": False}


# ---------- normalization ----------
def norm_domain(raw: str) -> str:
    d = raw.strip().lower()
    d = re.sub(r"^[a-z]+://", "", d).split("/")[0].split(":")[0]
    return d[4:] if d.startswith("www.") else d


def norm_phone(raw: str) -> str:
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits


# ---------- (a) RDAP domain ----------
def parse_rdap(domain: str, j: dict) -> dict:
    events = {e.get("eventAction"): e.get("eventDate") for e in j.get("events", [])}
    reg = events.get("registration")
    registrar = None
    for ent in j.get("entities", []):
        if "registrar" in ent.get("roles", []):
            for item in (ent.get("vcardArray") or [None, []])[1]:
                if item and item[0] == "fn":
                    registrar = item[3]
            registrar = registrar or ent.get("handle")
    age_days = None
    if reg:
        dt = datetime.fromisoformat(reg.replace("Z", "+00:00"))
        age_days = (datetime.now(timezone.utc) - dt).days
    return {"kind": "domain", "value": domain, "status": "ok",
            "registered": reg, "age_days": age_days, "registrar": registrar,
            "expires": events.get("expiration"), "newly_registered": age_days is not None and age_days < 30,
            "source": "rdap.org (public RDAP)", "simulated": False}


def _emit_lookup(call_id, res: dict) -> None:
    """Contract fields (artifact_kind, value, result, source) + the flat fields the command center already reads."""
    res.setdefault("artifact_kind", res.get("value_type") or res.get("kind"))
    res["result"] = {k: v for k, v in res.items() if k not in ("artifact_kind", "result")}
    emit("intel.lookup", call_id, res)


def lookup_domain(raw: str, call_id: str | None = None, client: httpx.Client | None = None) -> dict:
    domain = norm_domain(raw)
    c = client or httpx.Client(timeout=TIMEOUT, headers=UA, follow_redirects=True)
    try:
        r = c.get(f"https://rdap.org/domain/{domain}")
        if r.status_code == 404:
            res = {"kind": "domain", "value": domain, "status": "not_found",
                   "reason": "no RDAP record (unregistered or unsupported TLD)",
                   "source": "rdap.org (public RDAP)", "simulated": False}
        else:
            r.raise_for_status()
            res = parse_rdap(domain, r.json())
    except Exception as e:
        res = _unavailable("domain", domain, type(e).__name__)
    _emit_lookup(call_id, res)
    return res


# ---------- (b) wallet inflows ----------
BTC_RE = re.compile(r"^(bc1[0-9a-z]{11,71}|[13][1-9A-HJ-NP-Za-km-z]{25,34})$")
ETH_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")


def parse_btc(addr: str, j: dict) -> dict:
    cs, ms = j.get("chain_stats", {}), j.get("mempool_stats", {})
    received = cs.get("funded_txo_sum", 0) + ms.get("funded_txo_sum", 0)
    return {"kind": "wallet", "chain": "BTC", "value": addr, "status": "ok",
            "total_received": received / 1e8, "unit": "BTC",
            "tx_count": cs.get("tx_count", 0) + ms.get("tx_count", 0),
            "source": "blockstream.info (public explorer)", "simulated": False}


def parse_eth(addr: str, info: dict, counters: dict) -> dict:
    bal = int(info.get("coin_balance") or 0) / 1e18
    return {"kind": "wallet", "chain": "ETH", "value": addr, "status": "ok",
            "balance": bal, "unit": "ETH", "total_received": None,
            "tx_count": int(counters.get("transactions_count") or 0),
            "source": "eth.blockscout.com (public explorer)", "simulated": False}


def lookup_wallet(raw: str, call_id: str | None = None, client: httpx.Client | None = None) -> dict:
    addr = raw.strip()
    c = client or httpx.Client(timeout=TIMEOUT, headers=UA, follow_redirects=True)
    try:
        if BTC_RE.match(addr):
            r = c.get(f"https://blockstream.info/api/address/{addr}")
            r.raise_for_status()
            res = parse_btc(addr, r.json())
        elif ETH_RE.match(addr):
            base = f"https://eth.blockscout.com/api/v2/addresses/{addr}"
            info, cnt = c.get(base), c.get(base + "/counters")
            info.raise_for_status(); cnt.raise_for_status()
            res = parse_eth(addr, info.json(), cnt.json())
        else:
            res = {"kind": "wallet", "value": addr, "status": "invalid",
                   "reason": "not a valid BTC or ETH address", "source": None, "simulated": False}
    except Exception as e:
        res = _unavailable("wallet", addr, type(e).__name__)
    _emit_lookup(call_id, res)
    return res


# ---------- (c) verified-business allowlist ----------
def _load_allowlist() -> list[dict]:
    try:
        return json.loads(ALLOWLIST_PATH.read_text())["entries"]
    except Exception:
        return []


def check_allowlist(raw: str, call_id: str | None = None) -> dict:
    is_phone = bool(re.fullmatch(r"[\d\s()+\-.]{7,}", raw.strip()))
    key = norm_phone(raw) if is_phone else norm_domain(raw)
    hit = None
    for e in _load_allowlist():
        phones = {norm_phone(p) for p in e.get("phones", [])}
        domains = {norm_domain(d) for d in e.get("domains", [])}
        if (is_phone and key in phones) or (not is_phone and (key in domains or any(key.endswith("." + d) for d in domains))):
            hit = e["name"]
            break
    res = {"kind": "allowlist", "value": key, "value_type": "phone" if is_phone else "domain",
           "status": "ok", "match": hit is not None, "matched_org": hit,
           "note": "verified business: never actioned; if given by a scammer, flag attempted poisoning" if hit else None,
           "source": "intel/allowlist.json (seed data, published contact info)", "simulated": False}
    _emit_lookup(call_id, res)
    return res


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] not in {"domain", "wallet", "allow"}:
        print(__doc__); return 2
    fn = {"domain": lookup_domain, "wallet": lookup_wallet, "allow": check_allowlist}[argv[1]]
    res = fn(argv[2], call_id="cli-test")
    print("\nRESULT:\n" + json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
