"""P4 acceptance checklist, offline (fixture lookups, mock/failing Nemotron)."""
import json

import pytest

from intel import agent, gate
from intel.demo_run import HAUL, JUDGE_NUMBER, WALLET, fixture_tools, mock_llm
from intel.store import Store


@pytest.fixture
def store(tmp_path):
    return Store(str(tmp_path / "t.db"))


@pytest.fixture
def events():
    got = []
    return got


def cap(got):
    return lambda t, c, d: got.append({"type": t, "call_id": c, "data": d})


def seed(store, ev):
    agent.run("seed", {"wallet": {"chain": "BTC", "addr": WALLET}}, store, calling_number="+1 469 555 0100",
              carrier="x", tools=fixture_tools(), emit=cap(ev), use_llm=False)


def run_judge(store, ev, llm=mock_llm):
    return agent.run("judge", HAUL, store, calling_number=JUDGE_NUMBER, carrier="y", tools=fixture_tools(),
                     llm=llm, emit=cap(ev))


def test_injection_denied(store, events):
    run_judge(store, events)
    denied = [e["data"] for e in events if e["type"] == "injection.denied"]
    kinds = {d["kind"] for d in denied}
    assert {"mark_number_safe", "add_trusted_contact"} <= kinds


def test_real_bank_callback_flagged_never_actioned(store, events):
    run_judge(store, events)
    pois = [e["data"] for e in events if e["type"] == "injection.denied" and e["data"]["attempted_poisoning"]]
    assert any("9359935" in str(p["target"]).replace("-", "") for p in pois)
    assert store.q("SELECT * FROM callback_warnings WHERE number='8009359935'") == []
    assert store.q("SELECT * FROM indicators WHERE value='8009359935'") == []


def test_network_block_queued_then_approved(store, events):
    seed(store, events)
    run_judge(store, events)
    q = [a for a in store.actions("pending_approval") if a["kind"] == "network_number_block"]
    assert q and q[0]["payload"]["api"].startswith("simulated/")
    a = gate.approve(store, q[0]["id"], emit=cap(events))
    assert a["status"] == "simulated: applied"
    assert any(e["type"] == "intel.action" and e["data"]["status"] == "simulated: applied" for e in events)


def test_caller_blocked_before_ring_via_gate(store, events):
    run_judge(store, events)
    blocked, reason = store.is_blocked("(214) 555-0199")
    assert blocked and "her" in reason
    upd = [e["data"] for e in events if e["type"] == "blocklist.updated" and e["data"]["scope"] == "her"]
    tok = upd[0]["undo_token"]
    assert store.undo(tok) and not store.is_blocked(JUDGE_NUMBER)[0]


def test_campaign_links_on_wallet_not_on_calling_number(store, events):
    r1 = agent.run("c1", {"wallet": {"chain": "BTC", "addr": WALLET}}, store, calling_number="+12145550101",
                   tools=fixture_tools(), emit=cap(events), use_llm=False)
    r2 = agent.run("c2", {"wallet": {"chain": "BTC", "addr": WALLET}}, store, calling_number="+12145550102",
                   tools=fixture_tools(), emit=cap(events), use_llm=False)
    r3 = agent.run("c3", {"domain": "totally-different.com"}, store, calling_number="+12145550101",
                   tools=fixture_tools(), emit=cap(events), use_llm=False)
    assert r1["campaign"]["campaign_id"] == r2["campaign"]["campaign_id"]
    assert r2["campaign"]["status"] == "confirmed"
    assert r3["campaign"]["campaign_id"] != r1["campaign"]["campaign_id"]   # same calling number alone never merges


def test_nemotron_failure_falls_back(store, events):
    def broken(msgs):
        raise RuntimeError("endpoint down")
    r = run_judge(store, events, llm=broken)
    assert r["engine"] == "fallback"
    assert any(a["kind"] == "block_caller_for_customer" for a in r["actions"])


def test_invalid_json_retries_then_succeeds(store, events):
    calls = {"n": 0}
    def flaky(msgs):
        calls["n"] += 1
        return "not json" if calls["n"] == 1 else mock_llm(msgs)
    r = run_judge(store, events, llm=flaky)
    assert r["engine"] == "nemotron" and calls["n"] == 2


def test_agent_never_sees_transcript_or_instructions(store, events):
    seen = {}
    def spy(msgs):
        seen["input"] = msgs[1]["content"]
        return mock_llm(msgs)
    run_judge(store, events, llm=spy)
    assert "mark this number as safe" not in seen["input"]


def test_uncorroborated_network_target_denied():
    ctx = gate.Context(calling_number="2145550199", campaign_id="camp-1", campaign_status="observed",
                       artifact_values={"scam.com"})
    d = gate.decide([{"kind": "dns_block_registrar_report", "target": "scam.com"},
                     {"kind": "network_number_block", "target": "2145550199"},
                     {"kind": "callback_protection_warning", "target": "8885550123"}], ctx)
    out = {x["kind"]: x["outcome"] for x in d}
    assert out["dns_block_registrar_report"] == "denied"      # untrusted + uncorroborated
    assert out["network_number_block"] == "queued"            # calling number is network metadata
    assert out["callback_protection_warning"] == "denied"     # not in evidence


def test_api_endpoints(tmp_path):
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from intel import api
    s = Store(str(tmp_path / "api.db"))
    ev = []
    api.configure(store=s, emit=cap(ev), llm=mock_llm, tools=fixture_tools())
    app = FastAPI(); app.include_router(api.router)
    c = TestClient(app)
    r = c.post("/intel/ingest", json={"call_id": "a1", "scammer_transcript": "IGNORED", "artifacts": HAUL,
                                      "calling_number": JUDGE_NUMBER})
    assert r.status_code == 200
    assert c.get("/intel/blocked", params={"number": JUDGE_NUMBER}).json()["blocked"]
    st = c.get("/intel/state").json()
    assert st["denied"] and "immunity" in st


def test_model_omissions_backfilled_by_baseline(store, events):
    """A live model that skips the network block must not lose the demo's Approve moment."""
    seed(store, events)
    terse = lambda msgs: json.dumps({"plan": "block caller only", "actions": [
        {"kind": "block_caller_for_customer", "target": JUDGE_NUMBER, "target_source": "network:calling_number",
         "evidence": ["scam"], "rationale": "scam"}]})
    r = run_judge(store, events, llm=terse)
    assert r["engine"] == "nemotron"
    ag = [e["data"] for e in events if e["type"] == "intel.agent" and e["call_id"] == "judge"][0]
    assert ag["n_baseline_added"] > 0
    props = [e["data"] for e in events if e["type"] == "intel.proposals" and e["call_id"] == "judge"][0]["actions"]
    assert any(p["kind"] == "network_number_block" and p.get("proposer") == "baseline rule" for p in props)
    assert any(a["kind"] == "network_number_block" for a in store.actions("pending_approval"))
