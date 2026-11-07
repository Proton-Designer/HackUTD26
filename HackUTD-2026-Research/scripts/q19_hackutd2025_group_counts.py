"""Q19/Q0 support: HackUTD 2025 winners vs demo_ready vs random non-winners.

Reads existing research inputs (read-only) and writes:
  data/tables/Q19_hackutd2025_per_project.csv  (one row per project, derived fields)
  data/tables/Q19_hackutd2025_group_counts.csv (n of N per group per metric, with names)

Groups are never pooled. Winner duplicate (ProDuh) collapsed via duplicate_of.
All fields are derived from existing records; nothing is LLM-tagged here.
"""
import csv
import json
import os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)


def load(path):
    with open(P(path)) as f:
        return [json.loads(l) for l in f if l.strip()]


deep = load("04_deep_dives/data/deepdive_all.jsonl")
win_fp = {x["project_id"]: x for x in load("01_winners/data/project_records.jsonl")}
base_fp = {x["project_id"]: x for x in load("02_baseline_non_winners/data/project_records.jsonl")}

rows = []
for d in deep:
    pid = d["project_id"]
    if d["dataset"] == "winners" and pid.startswith("hackutd-2025-"):
        if d.get("duplicate_of"):
            continue
        fp = win_fp.get(pid)
        group = "winner"
    elif d["dataset"] == "baseline":
        fp = base_fp.get(pid)
        group = fp["sample_group"]
    else:
        continue
    if fp is None:
        raise SystemExit(f"no first-pass record for {pid}")

    feats = d.get("core_features") or []
    status = [f.get("working_status") for f in feats]
    pa = d.get("presentation_assets") or {}
    sc = d.get("scope_and_completeness") or {}
    rs = d.get("repo_signals") or {}
    stu = d.get("sponsor_tool_use") or []
    pf = d.get("prompt_fit") or {}
    nshots = fp.get("n_screenshots")
    share = fp.get("share_commits_in_window")
    rows.append(OrderedDict(
        group=group,
        project_id=pid,
        name=d["project_name"],
        devpost_url=d.get("devpost_url"),
        prizes="; ".join(p if isinstance(p, str) else str(p) for p in (d.get("prizes") or [])),
        n_prizes=len(d.get("prizes") or []),
        evidence_depth=(d.get("evidence") or {}).get("depth"),
        confidence=d.get("confidence"),
        scope_scale=sc.get("scale"),
        n_features=len(feats),
        n_shown_working=status.count("shown_working"),
        n_planned=status.count("planned"),
        n_flow_steps=len(d.get("user_flow") or []),
        has_video=bool(fp.get("has_demo_video")),
        has_video_url=bool(fp.get("demo_video_url")),
        has_live_demo_url=bool(fp.get("live_demo_url")),
        has_live_demo=bool(fp.get("has_live_demo")),
        n_screenshots=nshots,
        has_arch_diagram=pa.get("has_architecture_diagram"),
        has_repo=bool(fp.get("github_url")),
        repo_has_tests=rs.get("has_tests"),
        loc_estimate=rs.get("loc_estimate"),
        readme_quality=fp.get("readme_quality"),
        writeup_length=fp.get("writeup_length"),
        n_writeup_sections=len(fp.get("writeup_sections") or []),
        has_impact_claims=fp.get("has_impact_claims"),
        ai_used=fp.get("ai_used"),
        ai_types="|".join(fp.get("ai_types") or []),
        has_hardware=fp.get("has_hardware"),
        any_sponsor_tool_core=any((s.get("depth") == "core") for s in stu),
        prompt_fit_level=pf.get("evidence") or "",
        target_user=fp.get("target_user"),
        share_commits_in_window=share,
    ))

# prompt_fit field name discovery (keep robust)
sample_pf = next((d.get("prompt_fit") for d in deep if d.get("prompt_fit")), {})

out_dir = P("data", "tables")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "Q19_hackutd2025_per_project.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

metrics = OrderedDict([
    ("has_video", lambda r: r["has_video"]),
    ("has_live_demo", lambda r: r["has_live_demo"]),
    ("has_video_url", lambda r: r["has_video_url"]),
    ("has_live_demo_url", lambda r: r["has_live_demo_url"]),
    ("video_or_live_demo", lambda r: r["has_video"] or r["has_live_demo"]),
    ("screenshots_ge_3", lambda r: (r["n_screenshots"] or 0) >= 3),
    ("screenshots_ge_5", lambda r: (r["n_screenshots"] or 0) >= 5),
    ("has_arch_diagram", lambda r: r["has_arch_diagram"] is True),
    ("has_repo", lambda r: r["has_repo"]),
    ("repo_has_tests", lambda r: r["repo_has_tests"] is True),
    ("loc_ge_5000", lambda r: (r["loc_estimate"] or 0) >= 5000),
    ("writeup_long", lambda r: r["writeup_length"] == "long"),
    ("writeup_ge_6_sections", lambda r: r["n_writeup_sections"] >= 6),
    ("has_impact_claims", lambda r: r["has_impact_claims"] is True),
    ("ai_used", lambda r: r["ai_used"] is True),
    ("ai_agent_or_tool_use", lambda r: "agent_or_tool_use" in r["ai_types"]),
    ("has_hardware", lambda r: r["has_hardware"] is True),
    ("any_sponsor_tool_core", lambda r: r["any_sponsor_tool_core"]),
    ("scope_large", lambda r: r["scope_scale"] == "large"),
    ("scope_small_or_tiny", lambda r: r["scope_scale"] in ("small", "tiny")),
    ("shown_working_ge_1", lambda r: r["n_shown_working"] >= 1),
    ("shown_working_ge_3", lambda r: r["n_shown_working"] >= 3),
    ("any_planned_feature", lambda r: r["n_planned"] >= 1),
    ("evidence_depth_A", lambda r: r["evidence_depth"] == "A"),
    ("evidence_depth_C", lambda r: r["evidence_depth"] == "C"),
    ("multi_prize", lambda r: r["n_prizes"] >= 2),
    ("prompt_fit_explicit", lambda r: r["prompt_fit_level"] == "explicit"),
    ("prompt_fit_none", lambda r: r["prompt_fit_level"] == "none"),
])

groups = ["winner", "demo_ready", "random"]
with open(os.path.join(out_dir, "Q19_hackutd2025_group_counts.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["metric", "group", "n", "N", "pct", "low_n", "names"])
    for subset, keep in [("all", lambda r: True), ("depthA", lambda r: r["evidence_depth"] == "A")]:
      for m, fn in metrics.items():
        for g in groups:
            gr = [r for r in rows if r["group"] == g and keep(r)]
            m_out = m if subset == "all" else f"{m}__depthA_only"
            hit = [r["name"] for r in gr if fn(r)]
            N = len(gr)
            w.writerow([m_out, g, len(hit), N, round(100 * len(hit) / N) if N else "",
                        "yes" if N < 5 or len(hit) < 5 else "", "; ".join(hit)])
    # medians
    import statistics
    for m in ["n_features", "n_shown_working", "n_flow_steps", "n_screenshots", "loc_estimate", "share_commits_in_window"]:
        for g in groups:
            vals = [r[m] for r in rows if r["group"] == g and isinstance(r[m], (int, float))]
            w.writerow([f"median_{m}", g, statistics.median(vals) if vals else "", len(vals), "", "", ""])

print("rows", {g: sum(r["group"] == g for r in rows) for g in groups})
print("prompt_fit sample keys", list(sample_pf.keys()) if isinstance(sample_pf, dict) else sample_pf)

# ---- Track targeting per group (keyword match on prompt_fit.targeted_prizes) ----
TRACK_KEYS = OrderedDict([
    ("T-Mobile", ["t-mobile"]),
    ("EOG Resources", ["eog", "cauldron"]),
    ("Toyota Financial Services", ["toyota"]),
    ("PNC Bank", ["pnc"]),
    ("Northmark (NMC2)", ["northmark", "nmc"]),
    ("Nvidia", ["nvidia", "nemotron"]),
    ("StateFarm", ["state farm", "statefarm"]),
    ("Goldman Sachs", ["goldman"]),
    ("CBRE", ["cbre"]),
    ("Capital One", ["capital one"]),
    ("General Track", ["general track"]),
    ("Best Hardware", ["hardware"]),
    ("ElevenLabs", ["elevenlabs"]),
    ("Gemini (MLH)", ["gemini"]),
    ("Auth0", ["auth0"]),
])
by_id = {d["project_id"]: d for d in deep}
with open(os.path.join(out_dir, "Q19_hackutd2025_track_targeting.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["track", "group", "n_targeting", "N", "names"])
    for t, keys in TRACK_KEYS.items():
        for g in groups:
            gr = [r for r in rows if r["group"] == g]
            hit = []
            for r in gr:
                tp = " ".join((by_id[r["project_id"]].get("prompt_fit") or {}).get("targeted_prizes") or []).lower()
                if g == "winner":
                    tp = r["prizes"].lower()  # winners: use the track actually won
                if any(k in tp for k in keys):
                    hit.append(r["name"])
            w.writerow([t, g, len(hit), len(gr), "; ".join(hit)])


# ---- Manual close-read judgments (data/tagged/close_reads), counted here ----
jd = P("data", "tagged", "close_reads")
with open(os.path.join(jd, "q19_hackutd2025_award_integration.csv")) as f:
    aw = list(csv.DictReader(f))
with open(os.path.join(out_dir, "Q19_hackutd2025_award_integration_counts.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["award_kind", "integration_depth", "n_awards", "N_awards_of_kind", "names"])
    kinds = sorted(set(a["award_kind"] for a in aw))
    for k in kinds:
        ak = [a for a in aw if a["award_kind"] == k]
        for dpt in sorted(set(a["integration_depth"] for a in ak)):
            hit = [f'{a["name"]} ({a["award"]})' for a in ak if a["integration_depth"] == dpt]
            w.writerow([k, dpt, len(hit), len(ak), "; ".join(hit)])
    w.writerow(["ALL", "total_awards", len(aw), len(aw), ""])
with open(os.path.join(jd, "q19_hackutd2025_named_user.csv")) as f:
    nu = list(csv.DictReader(f))
with open(os.path.join(out_dir, "Q19_hackutd2025_named_user_counts.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["group", "named_user_specific", "n", "N", "pct", "names"])
    for g in ["winner", "demo_ready"]:
        gr = [x for x in nu if x["group"] == g]
        for v in ["yes", "no"]:
            hit = [x["name"] for x in gr if x["named_user_specific"] == v]
            w.writerow([g, v, len(hit), len(gr), round(100 * len(hit) / len(gr)), "; ".join(hit)])

# ---- Prompt-fit explicitness restricted to company-problem (sponsor_domain) tracks ----
DOMAIN_TRACKS = ["T-Mobile", "EOG Resources", "Toyota Financial Services", "PNC Bank", "Northmark (NMC2)",
                 "StateFarm", "Goldman Sachs", "CBRE", "Capital One"]
dom_win = sorted(set(a["name"] for a in aw if a["award_kind"] == "sponsor_domain"))
def targets_domain(r):
    tp = " ".join((by_id[r["project_id"]].get("prompt_fit") or {}).get("targeted_prizes") or []).lower()
    return any(k in tp for t in DOMAIN_TRACKS for k in TRACK_KEYS[t])
with open(os.path.join(out_dir, "Q19_hackutd2025_domain_track_prompt_fit.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["group", "prompt_fit_level", "n", "N", "pct", "names"])
    for g in groups:
        if g == "winner":
            gr = [r for r in rows if r["group"] == g and r["name"] in dom_win]
        else:
            gr = [r for r in rows if r["group"] == g and targets_domain(r)]
        for lvl in ["explicit", "implied", "none"]:
            hit = [r["name"] for r in gr if r["prompt_fit_level"] == lvl]
            w.writerow([g, lvl, len(hit), len(gr), round(100 * len(hit) / len(gr)) if gr else "", "; ".join(hit)])
