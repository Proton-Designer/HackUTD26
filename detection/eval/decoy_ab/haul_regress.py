"""Haul regression (eval tool, not runtime): feed STT strings from detection/eval/decoy_ab/haul_regress.jsonl through
decoy.core.extract (real model call, bolt extractor, one request at a time) + intel.campaigns.normalize_artifacts +
intel.nessie.match_destinations and print handles + hit yes/no per case. Run: PYTHONPATH=. .venv/bin/python detection/eval/decoy_ab/haul_regress.py
(needs NVIDIA_API_KEY in the environment; pauses while the live service has an open call)."""
import asyncio, json, pathlib, re, sys, urllib.request
sys.path.insert(0, ".")
from decoy import core
from intel import nessie
from intel.campaigns import normalize_artifacts

def live():
    try: return json.load(urllib.request.urlopen("http://127.0.0.1:8100/healthz", timeout=3)).get("active_stt_sockets", 0)
    except Exception: return 0

async def main():
    path = pathlib.Path(__file__).with_name("haul_regress.jsonl"); ok = 0; n = 0
    for line in path.read_text().splitlines():
        r = json.loads(line)
        while live() > 0: await asyncio.sleep(5)
        arts = await core.extract(r["pre_lines"] + r["heard_lines"])
        na = normalize_artifacts(arts); hits = nessie.match_destinations(na)
        handles = [a["value"] for a in na if a["type"] == "payment_handle"]
        payee = "zelle:refunds.dept@backfire-demo.example"
        if r["expect"]:   # positive: hit the payee and no stray handles
            hit = any(h["artifact"]["value"] == r["expect"] for h in hits); strays = [h for h in handles if h != r["expect"] and not re.fullmatch(r"zelle:\+1\d{10}", h)]; good = hit and not strays   # a valid E.164 US phone handle (P3 ba487bf backstop) is allowed, not a stray
        else:             # negative: must NOT be canonicalised to the payee, no hit
            hit = bool(hits) or payee in handles; strays = []; good = not hit
        ok += good; n += 1
        print(f'{r["card"]:18s} {"PASS" if good else "FAIL"} hit={"yes" if hit else "no "} strays={strays} handles={handles}', flush=True)
        await asyncio.sleep(2)
    print(f"{ok}/{n} cases pass (positives: hit + no strays; negatives: no payee hit)")
asyncio.run(main())
