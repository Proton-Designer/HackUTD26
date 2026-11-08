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
    assert ph("555-201-3344") == "+15552013344"   # Zelle phone ids are normalised (#138)


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


def test_zelle_id_must_be_email_or_phone():   # #138 live: zelle id '920.7856782'
    assert ph("920.7856782") == "+19207856782"   # live 1b838cd2: a real 10-digit Zelle phone, keep it
    assert ph("785.6782") is None and ph("120-555-0199") is None   # too short / not a valid area code
    assert ph("(214) 555-0199") == "+12145550199"
    assert ph("1-214-555-0199") == "+12145550199"
    assert ph("jake-smith", "venmo") == "jake-smith"


def test_live_1b838cd2_sell_it_to(monkeypatch):   # #138: 'Can you Sell it to the refunds.department ...' + a garbled phone
    import asyncio, json
    import decoy.core as C

    async def fake_chat(*a, **k):
        return json.dumps({"artifacts": [{"kind": "payment_handle", "rail": "zelle", "id": "920.7856782"},
                                          {"kind": "domain", "value": "backfire-demo.example"}]})
    monkeypatch.setattr(C, "chat", fake_chat)
    arts = asyncio.run(C.extract(["Buy the gift cards first.",
                                  "Can you Sell it to the refunds.department at backfire dash demo dot example?"]))
    ids = [a["id"] for a in arts if a["kind"] == "payment_handle"]
    assert ids == ["+19207856782", H]   # the spoken Zelle phone and the refunds address (the one Nessie matches)
