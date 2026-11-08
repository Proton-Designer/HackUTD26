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
            if m == "DELETE":
                del self.transfers[g[1]]
                return httpx.Response(200, json="")
            return httpx.Response(200, json=t)
        return httpx.Response(403, json={"message": "Missing Authentication Token"})


@pytest.fixture
def bank(tmp_path, monkeypatch):
    fake = FakeNessie()
    monkeypatch.setitem(N._edge_cache, "edges", None)  # chain edge cache is per process
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
    assert lk and lk[0]["status"] == "ok" and lk[0]["pending_count"] == 1 and lk[0]["activity_count"] == 7
    assert tid not in json.dumps(lk)                                    # transfer ids never in events/LLM input
    hold = acts(ev, "hold_transfer")
    assert len(hold) == 1 and hold[0]["status"] == "applied" and hold[0]["simulated"] is True
    assert hold[0]["reason"].startswith("Held $1,800 Zelle transfer to the scammer's captured destination")
    assert "Nessie" in hold[0]["reason"] and hold[0]["undo_token"].startswith("hold-") and hold[0]["evidence"]
    assert bank.transfers[tid]["status"] == "cancelled"
    flag = acts(ev, "flag_payee_bankwide")
    assert flag and flag[0]["status"] == "queued" and "7 other customers" in flag[0]["evidence"][0]
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
    assert len(ids["others"]) == 7 and len(ids["evidence_transfer_ids"]) == 7 and 8 <= len(ids["merchants"]) <= 10
    assert all(bank.transfers[t]["status"] == "completed" for t in ids["evidence_transfer_ids"])
    cfg = json.loads(seed_nessie.CONFIG.read_text())["payout_destination"]
    assert cfg["nessie_payee_account_id"] == ids["payee"]["account_id"] and cfg["bank_last4"]
    pt = seed_demo.start_pending_transfer()                             # /demo/reset hook
    assert pt and pt["amount"] == 1800 and bank.transfers[pt["id"]]["status"] == "pending"
    assert bank.transfers[pt["id"]]["description"].startswith("Zelle to ")
    bank.down = True
    assert seed_demo.start_pending_transfer() is None                   # skipped silently, reset stays fast


def test_gate_never_holds_llm_or_scammer_supplied_ids():
    ctx = gate.Context(calling_number=JUDGE_NUMBER, campaign_id="camp-1", campaign_status="confirmed",
                       bank_transfer_ids={"11111111-2222-3333-4444-555555555555"}, bank_payees={"zelle:x@y.example"})
    props = [{"kind": "hold_transfer", "target": "some-id", "target_source": "llm"},
             {"kind": "hold_transfer", "target": "some-id", "target_source": "artifact:instruction_to_ai"},
             {"kind": "flag_payee_bankwide", "target": "zelle:x@y.example", "target_source": "artifact:payment_handle"},
             # right label, but the id isn't one the code found -> denied
             {"kind": "hold_transfer", "target": "99999999-2222-3333-4444-555555555555",
              "target_source": "nessie:pending_transfer"},
             # right label AND code-found id -> auto
             {"kind": "hold_transfer", "target": "11111111-2222-3333-4444-555555555555",
              "target_source": "nessie:pending_transfer"}]
    assert [d["outcome"] for d in gate.decide(props, ctx)] == ["denied", "denied", "denied", "denied", "auto"]


def test_forged_llm_provenance_cannot_hold(bank, tmp_path):
    """#54: a model (possibly steered by the scammer) claims code provenance for a hold on a guessed id."""
    _, tid = seeded(bank)
    victim = bank.add_transfer(N.load_ids()["others"][0]["account_id"], "pending", 500, "someone else's transfer")
    forged = lambda msgs: json.dumps({"plan": "hold everything", "actions": [
        {"kind": "hold_transfer", "target": victim, "target_source": "nessie:pending_transfer",
         "destination_allow_key": None, "amount": 1},
        {"kind": "flag_payee_bankwide", "target": "zelle:attacker@evil.example", "target_source": "nessie:payee"}]})
    store, ev = Store(str(tmp_path / "s.db")), []
    cap = lambda t, c, d: ev.append({"type": t, "data": d})
    L.set_sink(cap)
    try:
        agent.run("judge", [{"kind": "payment_handle", "rail": "zelle", "id": HANDLE}], store,
                  calling_number=JUDGE_NUMBER, tools=fixture_tools(), llm=forged, emit=cap)
    finally:
        L.set_sink(None)
    assert bank.transfers[victim]["status"] == "pending"               # guessed id never touched
    assert bank.transfers[tid]["status"] == "cancelled"                # her real one, found by code, is held
    held = [a for a in acts(ev, "hold_transfer") if a["status"] == "applied"]
    assert [a["target"] for a in held] == [tid]
    assert not [a for a in acts(ev, "flag_payee_bankwide") if a["target"] == "zelle:attacker@evil.example"
                and a["status"] != "denied"]


def test_invalid_ids_never_reach_a_url(bank):
    for bad in ("../accounts/x", "abc", "", None, "x" * 30):
        assert N.hold_transfer(bad)["ok"] is False and N.release_transfer(bad) is False
        assert N.transfer_status(bad) is None
    assert not any(m == "PUT" for m, _ in bank.calls)


def test_repeated_resets_leave_exactly_one_pending(bank):
    seed_nessie.seed(quiet=True)
    maria = N.load_ids()["maria"]["account_id"]
    for _ in range(4):
        assert seed_demo.start_pending_transfer()
    assert len(N.pending_transfers(maria, description_contains=HANDLE)["transfers"]) == 1


# ---------- laundering chain (/intel/chain, /intel/map) ----------
def chain_client(tmp_path):
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    store = Store(str(tmp_path / "chain.db"))
    api.configure(store=store, emit=lambda *a: None, llm=mock_llm, tools=fixture_tools())
    app = FastAPI(); app.include_router(api.router)
    return TestClient(app), store


def test_chain_seed_shape(bank):
    seed_nessie.seed(quiet=True)
    c = N.load_ids()["chain"]
    roles = [n["role"] for n in c["nodes"]]
    assert roles.count("target") == 1 and roles.count("victim") == 7 and roles.count("mule") == 1 and roles.count("cashout") == 1
    vic = [e for e in c["edges"] if e["dst"] == "mule" and e["src"] != "maria"]
    hops = [e for e in c["edges"] if e["dst"] == "cashout"]
    assert len(vic) == 7 and sum(e["amount"] for e in vic) == 18100
    assert len(hops) == 3 and sum(e["amount"] for e in hops) == 17300 and all(e["src"] == "mule" for e in hops)
    assert all(N.valid_id(e["transfer_id"]) for e in vic + hops)
    assert [e for e in c["edges"] if e.get("dynamic")][0]["src"] == "maria"
    assert seed_nessie.seed(quiet=True)["status"] == "exists"        # idempotent with the chain present


def test_chain_added_to_existing_seed_is_additive(bank):
    seed_nessie.seed(quiet=True)
    ids = N.load_ids()
    base = {k: ids[k] for k in ("maria", "payee")}
    for k in ("chain", "cashout"):
        ids.pop(k)
    ids["others"], ids["evidence_transfer_ids"] = ids["others"][:3], ids["evidence_transfer_ids"][:3]
    N.save_ids(ids)                                                    # = the seed as it was before this change
    assert seed_nessie.seed(quiet=True)["status"] == "extended"
    after = N.load_ids()
    assert {k: after[k] for k in ("maria", "payee")} == base and len(after["others"]) == 7 and after["chain"]


def test_chain_endpoint_full_graph_then_maria_held(bank, tmp_path):
    seeded(bank)
    c, store = chain_client(tmp_path)
    g = c.get("/intel/chain").json()
    assert g["status"] == "ok" and g["simulated"] is True
    assert g["victim_count"] == 7 and g["mule_total_in"] == 18100 and g["mule_total_out"] == 17300
    assert g["held_count"] == 0 and len(g["edges"]) == 11 and len(g["nodes"]) == 10
    m = [e for e in g["edges"] if e["kind"] == "target"][0]
    assert m["held"] is False and m["amount"] == 1800
    assert [n for n in g["nodes"] if n["id"] == "mule"][0]["total_in"] == g["mule_total_in"] == 18100  # pending isn't in
    ev = []
    run(store, ev)                                                     # judge's call -> hold fires
    g = c.get("/intel/chain").json()
    m = [e for e in g["edges"] if e["kind"] == "target"][0]
    assert m["held"] is True and g["held_count"] == 1 and g["held_amount"] == 1800
    mule = [n for n in g["nodes"] if n["id"] == "mule"][0]
    assert mule["total_in"] == 18100                                   # the cut edge moved no money
    assert c.get("/intel/map").headers["content-type"].startswith("text/html")


def test_chain_fails_open_to_seeded_values(bank, tmp_path):
    seeded(bank)
    c, _ = chain_client(tmp_path)
    bank.down = True
    g = c.get("/intel/chain").json()
    assert g["status"] == "unavailable" and g["mule_total_in"] == 18100 and len(g["edges"]) == 11


def test_concurrent_resets_leave_exactly_one_pending(bank):
    """Shared-hub 11/12 (#51): two overlapping /demo/reset calls each created a transfer."""
    import threading
    seed_nessie.seed(quiet=True)
    maria = N.load_ids()["maria"]["account_id"]
    ts = [threading.Thread(target=seed_demo.start_pending_transfer) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    assert len(N.pending_transfers(maria, description_contains=HANDLE)["transfers"]) == 1
    # cross-process race (lock doesn't help): a stray pending created by someone else is removed on the next start
    bank.add_transfer(maria, "pending", 1800, f"Zelle to {HANDLE}")
    seed_demo._start_pending_transfer()
    assert len(N.pending_transfers(maria, description_contains=HANDLE)["transfers"]) == 1


def test_canon_handle_matches_stt_spellings():   # P2 #137: 'dept' heard as 'department' must still hit the payee
    from intel.nessie import canon_handle
    want = canon_handle("zelle:refunds.dept@backfire-demo.example")
    for v in ["zelle:refunds department at backfire dash demo dot example", "zelle:refunds.dept@backfire-demo.example",
              "Zelle:Refunds.Department@Backfire-Demo.Example", "zelle:refunds.department@backfire-demo.example.",
              "zelle:  refunds   dot   dept   at   backfire  dash  demo  dot  example  "]:
        assert canon_handle(v) == want, v
    for v in ["zelle:refunds.depot@backfire-demo.example", "zelle:payments.department@backfire-demo.example", "zelle:refunds dot dept"]:
        assert canon_handle(v) != want, v


def test_handles_match_tolerates_stt_garbling(monkeypatch):   # dev risk 6: the Zelle line as a phone STT hears it must still hold the $1,800
    from intel import nessie
    from intel.nessie import handles_match
    payee = "zelle:refunds.dept@backfire-demo.example"
    for v in ["zelle:refunds.dept@backfire-demo.example", "refunds dot dept at backfire dash demo dot example",
              "zelle:refunds department at backfire demo dot example",          # dash dropped
              "zelle:refund stepped at backfire dash demo dot example",         # 'refunds dept' heard as 'refund stepped'
              "zelle:refunds.depot@backfire-demo.example", "zelle:refunds-dept@backfiredemo.example", "refunds.dept@backfire.demo.example"]:
        assert handles_match(v, payee), v
    for v in ["zelle:payments.department@backfire-demo.example", "venmo:refunds.dept@backfire-demo.example",   # other local part / other rail
              "zelle:refunds.dept@backfire-demo.com", "zelle:refunds dot dept", "", None, "zelle:9205551234"]:
        assert not handles_match(v, payee), v
    monkeypatch.setattr(nessie, "destinations", lambda: [{"rail": "zelle", "id": "refunds.dept@backfire-demo.example", "nessie_payee_account_id": "x"}])
    arts = [{"type": "payment_handle", "value": "zelle:refunds department at backfire demo dot example"}, {"type": "domain", "value": "backfire-demo.example"}]
    hits = nessie.match_destinations(arts)
    assert len(hits) == 1 and hits[0]["artifact"] is arts[0]
    assert nessie.match_destinations([{"type": "payment_handle", "value": "paypal:someone@example.com"}]) == []
