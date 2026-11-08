"""Capital One Nessie integration, offline: an in-memory fake of the API paths confirmed on the live sandbox."""
import json
import re
import uuid

import httpx
import pytest

from intel import agent, api, gate, lookups as L, nessie as N, seed_demo, seed_nessie
from intel.demo_run import JUDGE_NUMBER, fixture_tools, mock_llm
from intel.store import Store

HANDLE = "refunds.dept@backfire-demo.example"


class FakeNessie:
    """Just enough of Nessie: create objects, list payer transfers, PUT status, enterprise reads by id."""

    def __init__(self):
        self.objs, self.transfers, self.payer = {}, {}, {}
        self.calls = []
        self.down = False

    def new(self, kind, body):
        oid = str(uuid.uuid4())
        o = {**body, "_id": oid}
        if kind == "account":
            o["account_number"] = str(uuid.uuid4().int)[:16]
        self.objs[oid] = (kind, o)
        return o

    def add_transfer(self, payer, status, amount, description):
        oid = str(uuid.uuid4())
        self.transfers[oid] = {"id": oid, "transaction_date": "2026-11-08", "status": status, "amount": amount,
                               "description": description}
        self.payer[oid] = payer
        return oid

    def __call__(self, req: httpx.Request) -> httpx.Response:
        if self.down:
            raise httpx.ConnectError("nessie down", request=req)
        assert req.url.params.get("key"), "every request carries ?key="
        m, p = req.method, req.url.path
        self.calls.append((m, p))
        body = json.loads(req.content) if req.content else {}
        created = lambda o: httpx.Response(201, json={"code": 201, "message": "created", "objectCreated": o})
        if m == "POST" and p == "/customers":
            return created(self.new("customer", body))
        if m == "POST" and (g := re.fullmatch(r"/customers/([^/]+)/accounts", p)):
            return created(self.new("account", {**body, "customer_id": g[1]}))
        if m == "POST" and p == "/merchants":
            return created(self.new("merchant", body))
        if m == "POST" and re.fullmatch(r"/accounts/[^/]+/(deposits|purchases)", p):
            return created(self.new("tx", body))
        if m == "POST" and (g := re.fullmatch(r"/accounts/([^/]+)/transfers", p)):
            assert "payee_id" in req.url.params and "payee_id" not in body
            tid = self.add_transfer(g[1], body["status"], body["amount"], body["description"])
            return created({**self.transfers[tid], "_id": tid})
        if m == "GET" and (g := re.fullmatch(r"/accounts/([^/]+)/transfers", p)):
            out = [t for tid, t in self.transfers.items() if self.payer[tid] == g[1]]
            return httpx.Response(200, json=out) if out else httpx.Response(404, json="No transfers found")
        if m == "GET" and (g := re.fullmatch(r"/(?:enterprise/)?accounts/([^/]+)", p)):
            o = self.objs.get(g[1])
            return httpx.Response(200, json=o[1]) if o and o[0] == "account" else httpx.Response(404, json="nf")
        if (g := re.fullmatch(r"/(?:enterprise/)?transfers/([^/]+)", p)):
            t = self.transfers.get(g[1])
            if not t:
                return httpx.Response(404, json="nf")
            if m == "PUT":
                t.update(body)
                return httpx.Response(202, json={"code": 202, "objectUpdated": t})
            return httpx.Response(200, json=t)
        return httpx.Response(403, json={"message": "Missing Authentication Token"})


@pytest.fixture
def bank(tmp_path, monkeypatch):
    fake = FakeNessie()
    monkeypatch.setenv("NESSIE_API_KEY", "test-key")
    monkeypatch.setattr(N, "IDS_PATH", tmp_path / "nessie_ids.json")
    cfg_path = tmp_path / "demo_config.json"
    cfg_path.write_text((N.Path(N.__file__).with_name("demo_config.json")).read_text())
    monkeypatch.setenv("INTEL_DEMO_CONFIG", str(cfg_path))
    monkeypatch.setattr(seed_nessie, "CONFIG", cfg_path)
    N.set_transport(httpx.MockTransport(fake))
    yield fake
    N.set_transport(None)


def seeded(bank, handle=HANDLE):
    """Run the real seed against the fake, then point the payout destination at `handle`."""
    r = seed_nessie.seed(quiet=True)
    assert r["status"] == "created"
    cfg = json.loads(seed_nessie.CONFIG.read_text())
    cfg["payout_destination"]["id"] = handle
    seed_nessie.CONFIG.write_text(json.dumps(cfg))
    ids = N.load_ids()
    tid = bank.add_transfer(ids["maria"]["account_id"], "pending", 1800, f"Zelle to {handle}")
    return ids, tid


def run(store, ev, handle=HANDLE):
    arts = [{"kind": "payment_handle", "rail": "zelle", "id": handle},
            {"kind": "callback_phone", "value": "1-888-555-0123"}]
    cap = lambda t, c, d: ev.append({"type": t, "data": d})
    L.set_sink(cap)  # lookups (incl. Nessie) emit via the module sink, as on the hub
    try:
        return agent.run("judge", arts, store, calling_number=JUDGE_NUMBER, carrier="y", tools=fixture_tools(),
                         llm=mock_llm, emit=cap)
    finally:
        L.set_sink(None)


def acts(ev, kind):
    return [e["data"] for e in ev if e["type"] == "intel.action" and e["data"]["kind"] == kind]


def test_hold_applied_and_undoable(bank, tmp_path):
    ids, tid = seeded(bank)
    store, ev = Store(str(tmp_path / "s.db")), []
    run(store, ev)
    lk = [e["data"] for e in ev if e["type"] == "intel.lookup" and e["data"].get("source") == "nessie"]
    assert lk and lk[0]["status"] == "ok" and lk[0]["pending_count"] == 1 and lk[0]["activity_count"] == 3
    assert tid not in json.dumps(lk)                                    # transfer ids never in events/LLM input
    hold = acts(ev, "hold_transfer")
    assert len(hold) == 1 and hold[0]["status"] == "applied" and hold[0]["simulated"] is True
    assert hold[0]["reason"].startswith("Held $1,800 Zelle transfer to the scammer's captured destination")
    assert "Nessie" in hold[0]["reason"] and hold[0]["undo_token"].startswith("hold-") and hold[0]["evidence"]
    assert bank.transfers[tid]["status"] == "cancelled"
    flag = acts(ev, "flag_payee_bankwide")
    assert flag and flag[0]["status"] == "queued" and "3 other customers" in flag[0]["evidence"][0]
    q = [a for a in store.actions("pending_approval") if a["kind"] == "flag_payee_bankwide"]
    assert q[0]["payload"]["body"]["payeeAccountId"] == ids["payee"]["account_id"]
    api.configure(store=store, emit=lambda *a: None)
    assert api.undo_block(hold[0]["undo_token"]) and bank.transfers[tid]["status"] == "pending"


def test_nessie_down_fails_open(bank, tmp_path):
    _, tid = seeded(bank)
    bank.down = True
    store, ev = Store(str(tmp_path / "s.db")), []
    r = run(store, ev)
    lk = [e["data"] for e in ev if e["type"] == "intel.lookup" and e["data"].get("source") == "nessie"]
    assert lk and lk[0]["status"] == "unavailable"
    assert not acts(ev, "hold_transfer") and not acts(ev, "flag_payee_bankwide")
    assert any(a["kind"] == "block_caller_for_customer" and a["status"] == "applied" for a in r["actions"])
    assert bank.transfers[tid]["status"] == "pending"


def test_allowlisted_destination_is_attempted_poisoning(bank, tmp_path):
    _, tid = seeded(bank, handle="billing@chase.com")               # a real bank's domain (allowlist seed)
    store, ev = Store(str(tmp_path / "s.db")), []
    run(store, ev, handle="billing@chase.com")
    hold = acts(ev, "hold_transfer")
    assert hold and hold[0]["status"] == "denied" and "poisoning" in hold[0]["gate_status"]
    assert any(e["type"] == "injection.denied" and e["data"]["kind"] == "hold_transfer"
               and e["data"]["attempted_poisoning"] for e in ev)
    assert bank.transfers[tid]["status"] == "pending"                  # never actioned


def test_no_mapping_no_bank_action(bank, tmp_path):
    seeded(bank)
    store, ev = Store(str(tmp_path / "s.db")), []
    run(store, ev, handle="someone.else@backfire-demo.example")
    assert not [e for e in ev if e["type"] == "intel.lookup" and e["data"].get("source") == "nessie"]
    assert not acts(ev, "hold_transfer") and not acts(ev, "flag_payee_bankwide")


def test_seed_idempotent_and_reset_hook(bank, tmp_path):
    assert seed_nessie.seed(quiet=True)["status"] == "created"
    n_posts = sum(1 for m, _ in bank.calls if m == "POST")
    assert seed_nessie.seed(quiet=True)["status"] == "exists"
    assert sum(1 for m, _ in bank.calls if m == "POST") == n_posts      # second run creates nothing
    ids = N.load_ids()
    assert len(ids["others"]) == 3 and len(ids["evidence_transfer_ids"]) == 3 and 8 <= len(ids["merchants"]) <= 10
    assert all(bank.transfers[t]["status"] == "completed" for t in ids["evidence_transfer_ids"])
    cfg = json.loads(seed_nessie.CONFIG.read_text())["payout_destination"]
    assert cfg["nessie_payee_account_id"] == ids["payee"]["account_id"] and cfg["bank_last4"]
    pt = seed_demo.start_pending_transfer()                             # /demo/reset hook
    assert pt and pt["amount"] == 1800 and bank.transfers[pt["id"]]["status"] == "pending"
    assert bank.transfers[pt["id"]]["description"].startswith("Zelle to ")
    bank.down = True
    assert seed_demo.start_pending_transfer() is None                   # skipped silently, reset stays fast


def test_gate_never_holds_llm_or_scammer_supplied_ids():
    ctx = gate.Context(calling_number=JUDGE_NUMBER, campaign_id="camp-1", campaign_status="confirmed")
    props = [{"kind": "hold_transfer", "target": "some-id", "target_source": "llm"},
             {"kind": "hold_transfer", "target": "some-id", "target_source": "artifact:instruction_to_ai"},
             {"kind": "flag_payee_bankwide", "target": "zelle:x@y.example", "target_source": "artifact:payment_handle"}]
    assert [d["outcome"] for d in gate.decide(props, ctx)] == ["denied", "denied", "denied"]
