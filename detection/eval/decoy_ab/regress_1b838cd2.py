"""Regression for live call 1b838cd2 (no Nessie hold): caller lines the decoy heard + the extractor output seen live (LLM mocked). Run from the repo root: python -m detection.eval.decoy_ab.regress_1b838cd2 (eval tool, not runtime). Expect: refunds.dept handle present and a Nessie hit."""
import asyncio, json, sys
from decoy import core
from intel import campaigns, nessie as N
LINES = ["You need to buy Target gift cards and send them to us.",
         "Can you Sell it to the refunds.department at backfire-demo.example",
         "Send it by Zell to the account.",
         "The Zell account at 920 7856782"]
# What the (bolt) extractor model returned live (haul at 08:47:39): gift card, domain, ONLY the phone-number handle
async def fake(msgs, **k):
    return json.dumps({"artifacts": [{"kind": "gift_card_brand", "value": "target"}, {"kind": "domain", "value": "backfire-demo.example"},
                                      {"kind": "payment_handle", "rail": "zelle", "id": "920 7856782"}]})
core.chat = fake
out = asyncio.run(core.extract(LINES))
hs = [a for a in out if a["kind"] == "payment_handle"]
print("handles:", [a["rail"] + ":" + a["id"] for a in hs])
print("nessie hits:", [len(N.match_destinations(campaigns.normalize_artifacts([h]))) for h in hs], "| any hit:", any(N.match_destinations(campaigns.normalize_artifacts([h])) for h in hs))
print("stray 920 handle present:", any("920" in a["id"] for a in hs))
