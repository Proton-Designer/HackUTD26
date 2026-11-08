"""Haul regression (eval tool, not runtime): feed STT strings from detection/eval/decoy_ab/haul_regress.jsonl through
decoy.core.extract (real model call, bolt extractor, one request at a time) + intel.campaigns.normalize_artifacts +
intel.nessie.match_destinations and print handles + hit yes/no per case. Run: PYTHONPATH=. .venv/bin/python detection/eval/decoy_ab/haul_regress.py
(needs NVIDIA_API_KEY in the environment; pauses while the live service has an open call)."""
import asyncio, json, pathlib, sys, urllib.request
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
        hit = any(h["artifact"]["value"] == r["expect"] for h in hits); ok += hit; n += 1
        print(f'{r["card"]:14s} hit={"yes" if hit else "NO "} handles={handles}', flush=True)
        await asyncio.sleep(2)
    print(f"{ok}/{n} cases hit {r['expect']}")
asyncio.run(main())
