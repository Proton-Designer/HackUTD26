"""Q21 support: HackUTD 2025 T-Mobile-targeting entries (3 winners vs demo_ready vs random baseline).

Reads (read-only):
  data/tables/Q19_hackutd2025_track_targeting.csv   (which entries targeted T-Mobile)
  01_winners/data/project_records.jsonl, 02_baseline_non_winners/data/project_records.jsonl
  04_deep_dives/data/deepdive_all.jsonl
Writes:
  data/tables/Q21_tmobile2025_entries.csv  (one row per entry, derived keyword flags)
  data/tables/Q21_tmobile2025_counts.csv   (n of N per group per flag; groups never pooled)

Flags are keyword matches over the existing record + deep-dive text (no new LLM tagging).
They mean "mentioned in our existing record text", not "verified working".
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)


def jl(path):
    with open(P(path)) as f:
        return [json.loads(l) for l in f if l.strip()]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


targets = {}
with open(P("data/tables/Q19_hackutd2025_track_targeting.csv")) as f:
    for row in csv.DictReader(f):
        if row["track"] == "T-Mobile":
            for n in row["names"].split(";"):
                if n.strip():
                    targets[norm(n.strip())] = (n.strip(), row["group"])

recs = {}
for r in jl("01_winners/data/project_records.jsonl") + jl("02_baseline_non_winners/data/project_records.jsonl"):
    if r.get("edition") == "HackUTD 2025" or "hackutd" in r.get("project_id", ""):
        recs.setdefault(norm(r["project_name"]), r)
dds = {}
for r in jl("04_deep_dives/data/deepdive_all.jsonl"):
    if r.get("edition") == "HackUTD 2025":
        dds.setdefault(norm(r["project_name"]), r)

FLAGS = {
    "happiness_index": r"happiness|\bchi\b",
    "map_or_heatmap": r"heat ?map|\bmap\b|geograph|leaflet|mapbox",
    "llm_actions": r"recommend|suggest|action|opportunit|insight",
    "auth0": r"auth0",
    "synthetic_or_mock_mentioned": r"synthetic|simulat|mock|fake|sample data|seed",
    "call_or_voice": r"twilio|call transcript|voice|vapi|speech",
    "outage_data": r"outage|downdetector",
}

rows = []
for key, (name, group) in sorted(targets.items(), key=lambda kv: (kv[1][1], kv[1][0].lower())):
    rec = recs.get(key) or next((v for k, v in recs.items() if k.startswith(key[:8])), None)
    dd = dds.get(key) or next((v for k, v in dds.items() if k.startswith(key[:8])), None)
    text = json.dumps(rec or {}).lower() + " " + json.dumps(dd or {}).lower()
    row = {
        "name": name,
        "group": group,
        "record_found": bool(rec),
        "deepdive_found": bool(dd),
        "devpost_url": (rec or dd or {}).get("devpost_url"),
        "n_tech_items": len((rec or {}).get("tech_items") or []),
        "n_screenshots": (rec or {}).get("n_screenshots"),
        "has_live_demo": (rec or {}).get("has_live_demo"),
        "ai_types": "|".join((rec or {}).get("ai_types") or []),
    }
    for flag, pat in FLAGS.items():
        row[flag] = bool(re.search(pat, text))
    rows.append(row)

os.makedirs(P("data/tables"), exist_ok=True)
with open(P("data/tables/Q21_tmobile2025_entries.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

with open(P("data/tables/Q21_tmobile2025_counts.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["metric", "group", "n", "N", "pct", "low_n", "names"])
    for group in ["winner", "demo_ready", "random"]:
        g = [r for r in rows if r["group"] == group]
        N = len(g)
        for flag in list(FLAGS) + ["has_live_demo"]:
            hit = [r["name"] for r in g if r[flag] is True]
            w.writerow([flag, group, len(hit), N, f"{100*len(hit)/N:.0f}" if N else "", N < 5, "; ".join(hit)])
        med = sorted(r["n_tech_items"] for r in g)
        w.writerow(["median_n_tech_items", group, med[len(med)//2] if med else "", N, "", N < 5, ""])
print(f"wrote {len(rows)} rows")
for r in rows:
    print(r["group"], r["name"], r["record_found"], r["deepdive_found"], r["n_tech_items"])
