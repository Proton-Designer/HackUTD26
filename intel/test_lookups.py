"""Offline tests: parsing + fail-open, using httpx.MockTransport (no network)."""
import httpx
from intel import lookups as L

RDAP = {"events": [{"eventAction": "registration", "eventDate": "2026-11-05T10:00:00Z"},
                   {"eventAction": "expiration", "eventDate": "2027-11-05T10:00:00Z"}],
        "entities": [{"roles": ["registrar"], "vcardArray": ["vcard", [["version", {}, "text", "4.0"], ["fn", {}, "text", "NameCheap, Inc."]]]}]}
BTC = {"chain_stats": {"funded_txo_sum": 150000000, "tx_count": 7}, "mempool_stats": {"funded_txo_sum": 0, "tx_count": 0}}

def client(handler):
    return httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True)

def test_domain_ok():
    r = L.lookup_domain("https://www.Scam-Refund.com/pay", client=client(lambda req: httpx.Response(200, json=RDAP)))
    assert r["value"] == "scam-refund.com" and r["registrar"] == "NameCheap, Inc." and r["newly_registered"]

def test_domain_timeout_fails_open():
    def boom(req): raise httpx.ConnectTimeout("t")
    r = L.lookup_domain("x.com", client=client(boom))
    assert r["status"] == "unavailable"

def test_btc_ok():
    r = L.lookup_wallet("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", client=client(lambda req: httpx.Response(200, json=BTC)))
    assert r["total_received"] == 1.5 and r["tx_count"] == 7

def test_eth_ok():
    def h(req):
        return httpx.Response(200, json={"transactions_count": "12"} if req.url.path.endswith("counters") else {"coin_balance": "2000000000000000000"})
    r = L.lookup_wallet("0x" + "a" * 40, client=client(h))
    assert r["chain"] == "ETH" and r["balance"] == 2.0 and r["tx_count"] == 12

def test_wallet_invalid():
    assert L.lookup_wallet("not-a-wallet", client=client(lambda r: httpx.Response(500)))["status"] == "invalid"

def test_allowlist_phone_poisoning():
    r = L.check_allowlist("(800) 935-9935")
    assert r["match"] and r["matched_org"] == "Chase"

def test_allowlist_domain_and_subdomain():
    assert L.check_allowlist("https://secure.chase.com/login")["match"]
    assert not L.check_allowlist("chase-secure-verify.com")["match"]
