"""Check every row in scripts.jsonl parses and follows the eval schema."""
import json, sys, collections, pathlib
ASKS = {"otp","card","ssn","gift_card","crypto","wire","p2p","remote_app","secrecy"}
REQ = {"id","split","label","scam_type","caller_lines","expected_asks","expected_alert"}
path = pathlib.Path(__file__).with_name("scripts.jsonl")
errs, ids, counts = [], set(), collections.Counter()
for n, line in enumerate(path.read_text().splitlines(), 1):
    try:
        r = json.loads(line)
    except json.JSONDecodeError as e:
        errs.append(f"line {n}: bad JSON ({e})"); continue
    miss = REQ - r.keys()
    if miss: errs.append(f"line {n}: missing {miss}")
    if r.get("id") in ids: errs.append(f"line {n}: duplicate id {r.get('id')}")
    ids.add(r.get("id"))
    if r.get("split") not in {"dev","test"}: errs.append(f"line {n}: bad split")
    if r.get("label") not in {"scam","legit","adversarial"}: errs.append(f"line {n}: bad label")
    if not isinstance(r.get("caller_lines"), list) or not r["caller_lines"]: errs.append(f"line {n}: caller_lines empty")
    bad = set(r.get("expected_asks", [])) - ASKS
    if bad: errs.append(f"line {n}: unknown asks {bad}")
    if not isinstance(r.get("expected_alert"), bool): errs.append(f"line {n}: expected_alert not bool")
    counts[(r.get("label"), r.get("split"))] += 1
print("rows:", len(ids)); print("by label/split:", dict(counts))
if errs: print("\n".join(errs)); sys.exit(1)
print("OK: all rows valid")
