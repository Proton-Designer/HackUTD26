"""Re-run the stored RAW bolt replies of a run_ab.py json through the CURRENT core.guard (which includes speakable()) and report
leftover note echoes. Usage: python -m detection.eval.decoy_ab.reguard ab_live.json 'HEAD bolt-e4b'"""
import json, re, sys
from decoy import core
d = json.load(open(sys.argv[1])); arm = sys.argv[2]; bad = []; n = 0
for cid, c in d.items():
    for r in c["variants"].get(arm, []):
        if not r.get("raw"): continue
        n += 1; p = core.Persona("rg")
        _, spoken = core.guard(r["raw"], p, set(), lambda *a: None, r["scammer"])
        if re.search(r"private|steer|note|have:|turns left|still need|never read", spoken, re.I): bad.append(spoken)
print(f"{n} replies re-guarded, {len(bad)} still contain note text")
for b in bad[:10]: print("  SURVIVES:", b)
