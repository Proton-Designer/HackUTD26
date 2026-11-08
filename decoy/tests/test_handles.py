"""#137: STT-shaped Zelle handles canonicalise to the seeded payee; malformed ones are dropped (no network)."""
import sys
sys.path.insert(0, ".")
from decoy.core import fix_zelle, validate

H = "refunds.dept@backfire-demo.example"


def ph(i, rail="zelle"):
    v = validate({"kind": "payment_handle", "rail": rail, "id": i})
    return v and v["id"]


def test_dept_forms():
    assert ph("refunds.department@backfire-demo.example") == H
    assert ph("Refunds.Department@Backfire-Demo.Example.") == H
    assert ph("refunds dot dept at backfire dash demo dot example") == H
    assert ph("refunds department@backfire-demo.example") == H   # P2 edge: model emits a spaced local part
    assert fix_zelle("by Zelle to refunds department at backfire dash demo dot example") == \
        "by Zelle to refunds dot dept at backfire dash demo dot example"
    assert fix_zelle("by sell to Refunds dot department at backfire dash demo dot example").startswith("by Zelle to Refunds dot dept at")


def test_no_false_rewrites():
    assert fix_zelle("I work in the billing department at the hospital") == "I work in the billing department at the hospital"
    assert ph("payments.department@x-y.example") == "payments.dept@x-y.example"   # same rule, different local part: still not the seeded payee
    assert ph("refunds.depot@backfire-demo.example") == "refunds.depot@backfire-demo.example"


def test_malformed_and_non_email():
    assert ph("zelle disputes@your bank") is None
    assert ph("@jake-smith", "venmo") == "@jake-smith"
    assert ph("555-201-3344") == "555-201-3344"


def test_truncated_local_part_repaired(monkeypatch):   # #137 card 6: model returned 'dept@...' next to the full handle
    import asyncio, json
    import decoy.core as C

    async def fake_chat(*a, **k):
        return json.dumps({"artifacts": [{"kind": "payment_handle", "rail": "zelle", "id": "dept@backfire-demo.example"},
                                          {"kind": "payment_handle", "rail": "zelle", "id": H},
                                          {"kind": "payment_handle", "rail": "zelle", "id": "ops@other-site.example"}]})
    monkeypatch.setattr(C, "chat", fake_chat)
    ids = [a["id"] for a in asyncio.run(C.extract(["Send it by Zelle to refunds dot dept at backfire dash demo dot example."]))]
    assert ids == [H, "ops@other-site.example"]
