"""Q19 close read, HackUTD 2024 half: manual per-project tags -> counts.

Tags were assigned by hand while reading
04_deep_dives/profiles/winners/hackutd-hackutd-2024.md plus the matching rows of
04_deep_dives/data/deepdive_all.jsonl and 01_winners/data/project_records.jsonl.
Writes data/tables/Q19_hackutd2024_close_read_tags.csv and prints every count
used in outputs/close_reads/hackutd_2024_winners.md with the names behind it.

Tag definitions
- kind: general | domain_sponsor (company challenge track) | tool_sponsor (Pinata,
  SambaNova) | side (HackUTD side prizes) | mlh. Primary kind = highest of
  general > domain_sponsor > tool_sponsor > side > mlh.
- sponsor_depth (for the domain/tool sponsor track won): core | core_data
  (sponsor-supplied dataset is the core input) | problem_only | unknown | na.
- ai_role: core_llm | llm_addon | own_ml (self-trained/classical ML, stats, CV) | none.
- data_source: live (live API, sensor, audio/video stream, real transactions) |
  static_dataset | synthetic | user_input | unclear.
- core_shown: profile marks a core feature [shown_working].
- video: a demo-video URL in project_records or has_video true in deepdive.
- live_demo: has_live_demo true in both files.
- inference-flagged values are suffixed '*' in the CSV (sponsor_depth only).
"""
import csv, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "tables", "Q19_hackutd2024_close_read_tags.csv")

# name, kind, tracks_won_at_hackutd, n_prizes, sponsor_depth, ai_role, hardware,
# data_source, core_shown, video, live_demo, unbanked_focus, data_or_analytics, evidence
ROWS = [
    ("Lumo", "general", "General; Goldman Sachs", 2, "problem_only", "none", 0, "live", 0, 1, 0, 1, 0, "A"),
    ("TalkTuahBank", "general", "General; Goldman Sachs", 2, "problem_only", "core_llm", 0, "live", 1, 1, 1, 1, 0, "A"),
    ("Ripple Banking", "general", "General", 1, "na", "own_ml", 0, "user_input", 1, 1, 0, 1, 0, "A"),
    ("AllBank", "domain_sponsor", "Goldman Sachs", 1, "problem_only", "llm_addon", 0, "user_input", 0, 0, 0, 1, 0, "A"),
    ("Data Pattern Observatory", "domain_sponsor", "PNC Bank", 1, "problem_only", "own_ml", 0, "unclear", 0, 0, 0, 0, 1, "A"),
    ("FinnAI", "domain_sponsor", "PNC Bank", 1, "problem_only", "core_llm", 0, "user_input", 0, 1, 0, 0, 0, "B"),
    ("Hermes", "domain_sponsor", "PNC Bank", 1, "problem_only", "own_ml", 0, "live", 0, 1, 0, 1, 0, "A"),
    ("FUELICIENT", "domain_sponsor", "Toyota (1st)", 1, "core_data", "none", 0, "static_dataset", 0, 1, 1, 0, 1, "B"),
    ("KaizenDrive", "domain_sponsor", "Toyota", 1, "core_data*", "llm_addon", 0, "static_dataset", 0, 1, 0, 0, 1, "A"),
    ("ToyoTrends", "domain_sponsor", "Toyota", 1, "core_data*", "llm_addon", 0, "static_dataset", 1, 1, 0, 0, 1, "B"),
    ("PipeBrAIns", "domain_sponsor", "EOG Resources", 1, "core_data", "own_ml", 0, "static_dataset", 0, 1, 0, 0, 1, "A"),
    ("DHy-n0", "domain_sponsor", "EOG Resources; [MLH] .Tech", 2, "core_data*", "own_ml", 0, "static_dataset", 0, 1, 1, 0, 1, "A"),
    ("Eco Fast Track", "domain_sponsor", "CBRE; Veolia", 2, "problem_only", "llm_addon", 1, "live", 1, 1, 0, 0, 0, "A"),
    ("EcoVerse", "domain_sponsor", "CBRE", 1, "problem_only", "llm_addon", 1, "synthetic", 0, 0, 0, 0, 0, "A"),
    ("Greenify", "domain_sponsor", "CBRE", 1, "core_data", "core_llm", 0, "static_dataset", 0, 1, 0, 0, 1, "A"),
    ("EcoLens (Sustainable Building Manager)", "domain_sponsor", "Veolia", 1, "problem_only", "none", 0, "unclear", 0, 0, 0, 0, 1, "A"),
    ("FrontierMap", "domain_sponsor", "Frontier", 1, "problem_only", "none", 0, "user_input", 1, 1, 1, 0, 0, "A"),
    ("Homelander", "domain_sponsor", "Frontier", 1, "core_data", "own_ml", 0, "static_dataset", 0, 0, 1, 0, 1, "B"),
    ("Promising Products", "domain_sponsor", "Frontier", 1, "problem_only", "own_ml", 0, "static_dataset", 0, 1, 0, 0, 0, "A"),
    ("InvestIQ", "domain_sponsor", "Infosys", 1, "unknown", "core_llm", 0, "synthetic", 0, 1, 0, 0, 0, "A"),
    ("Monch", "tool_sponsor", "Pinata (1st)", 1, "core", "own_ml", 0, "user_input", 1, 1, 1, 0, 0, "A"),
    ("Capsule", "tool_sponsor", "Pinata (2nd)", 1, "core", "none", 0, "user_input", 1, 0, 1, 0, 0, "B"),
    ("Cheddarboxd", "tool_sponsor", "Pinata (3rd per master list); Best Solo Hack", 2, "core", "none", 0, "user_input", 0, 1, 0, 0, 0, "A"),
    ("Notable", "tool_sponsor", "SambaNova", 1, "core", "core_llm", 0, "live", 0, 0, 1, 0, 0, "A"),
    ("Vestique", "tool_sponsor", "SambaNova; [MLH] Streamlit", 2, "core", "core_llm", 0, "user_input", 0, 1, 0, 0, 0, "A"),
    ("Backtracc", "tool_sponsor", "SambaNova; Hardware; [MLH] Cloudflare", 3, "core", "core_llm", 1, "live", 1, 1, 1, 0, 0, "A"),
    ("Echo", "side", "Best Design", 1, "na", "own_ml", 0, "live", 0, 0, 0, 0, 0, "A"),
    ("EcoLens (property evaluator)", "side", "Best Beginner", 1, "na", "core_llm", 0, "user_input", 0, 1, 0, 0, 0, "B"),
    ("poyo.ed", "side", "Poyo's Prize", 1, "na", "core_llm", 1, "live", 1, 0, 0, 0, 0, "A"),
    ("Planet Score", "side", "Best Devpost", 1, "na", "none", 0, "live", 0, 0, 0, 0, 0, "A"),
    ("DuckTalk", "side", "Guided Track", 1, "na", "none", 0, "live", 0, 0, 0, 0, 0, "B"),
    ("What's The Move?", "side", "Most Relatable", 1, "na", "none", 0, "live", 1, 0, 1, 0, 0, "A"),
    ("GitFile", "mlh", "[MLH] Best Use of Terraform", 1, "na", "none", 0, "user_input", 0, 1, 1, 0, 0, "A"),
]
EXCLUDED = {
    "Roomie (unverified on Devpost)": "evidence C; year unconfirmed; no Devpost page",
    "The Virtual Fitness Assistant": "prize badges appear under Student Hacks, not HackUTD 2024",
}
COLS = ["name", "kind", "tracks_won", "n_prizes", "sponsor_depth", "ai_role", "hardware",
        "data_source", "core_shown", "video", "live_demo", "unbanked_focus",
        "data_or_analytics", "evidence"]


def show(label, names, N):
    pct = 100 * len(names) / N if N else 0
    low = " (low n)" if N < 5 else ""
    print(f"{label}: {len(names)} of {N} ({pct:.0f}%){low}: {', '.join(names)}")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLS + ["included"])
        for r in ROWS:
            w.writerow(list(r) + [1])
        for n, why in EXCLUDED.items():
            w.writerow([n] + [""] * (len(COLS) - 1) + ["0: " + why])
    rows = [dict(zip(COLS, r)) for r in ROWS]
    N = len(rows)
    print("N included =", N, "| excluded:", list(EXCLUDED))
    by = lambda pred, rs=rows: [r["name"] for r in rs if pred(r)]
    for k in ["general", "domain_sponsor", "tool_sponsor", "side", "mlh"]:
        show(f"kind={k}", by(lambda r: r["kind"] == k), N)
    gen = [r for r in rows if r["kind"] == "general"]
    dom = [r for r in rows if r["kind"] == "domain_sponsor"]
    tool = [r for r in rows if r["kind"] == "tool_sponsor"]
    dom_any = dom + [r for r in gen if "Goldman" in r["tracks_won"]]  # won >=1 domain-sponsor track
    print("-- won any domain-sponsor track (incl. General+Goldman)")
    for dep in ["core_data", "core_data*", "problem_only", "unknown"]:
        show(f"  depth={dep}", by(lambda r: r["sponsor_depth"] == dep, dom_any), len(dom_any))
    show("  no LLM (own_ml or none)", by(lambda r: r["ai_role"] in ("own_ml", "none"), dom_any), len(dom_any))
    show("  multi-prize", by(lambda r: r["n_prizes"] >= 2, dom_any), len(dom_any))
    for role in ["core_llm", "llm_addon", "own_ml", "none"]:
        show(f"ai_role={role}", by(lambda r: r["ai_role"] == role), N)
    show("any AI", by(lambda r: r["ai_role"] != "none"), N)
    show("hardware", by(lambda r: r["hardware"] == 1), N)
    for d in ["live", "static_dataset", "synthetic", "user_input", "unclear"]:
        show(f"data_source={d}", by(lambda r: r["data_source"] == d), N)
    show("core feature shown working", by(lambda r: r["core_shown"] == 1), N)
    show("video", by(lambda r: r["video"] == 1), N)
    show("live demo", by(lambda r: r["live_demo"] == 1), N)
    show("video or live demo", by(lambda r: r["video"] or r["live_demo"]), N)
    show("neither video nor live demo", by(lambda r: not (r["video"] or r["live_demo"])), N)
    show("multi-prize", by(lambda r: r["n_prizes"] >= 2), N)
    show("unbanked/underbanked focus", by(lambda r: r["unbanked_focus"] == 1), N)
    print("-- domain-sponsor winners")
    for dep in ["core_data", "core_data*", "problem_only", "unknown"]:
        show(f"  depth={dep}", by(lambda r: r["sponsor_depth"] == dep, dom), len(dom))
    show("  no LLM (own_ml or none)", by(lambda r: r["ai_role"] in ("own_ml", "none"), dom), len(dom))
    tef = [r for r in dom if any(s in r["tracks_won"] for s in ("Toyota", "EOG", "Frontier"))]
    show("  Toyota/EOG/Frontier winners with no LLM", by(lambda r: r["ai_role"] in ("own_ml", "none"), tef), len(tef))
    show("  data_or_analytics", by(lambda r: r["data_or_analytics"] == 1, dom), len(dom))
    print("-- tool-sponsor winners")
    show("  depth=core", by(lambda r: r["sponsor_depth"] == "core", tool), len(tool))
    print("-- general winners")
    show("  also won Goldman", by(lambda r: "Goldman" in r["tracks_won"], gen), len(gen))
    show("  unbanked focus", by(lambda r: r["unbanked_focus"] == 1, gen), len(gen))
    show("  data_or_analytics", by(lambda r: r["data_or_analytics"] == 1, gen), len(gen))
    show("  hardware", by(lambda r: r["hardware"] == 1, gen), len(gen))
    gs = [r for r in rows if "Goldman" in r["tracks_won"]]
    show("Goldman winners with unbanked focus", by(lambda r: r["unbanked_focus"] == 1, gs), len(gs))
    known = [r for r in rows if any(p in r["tracks_won"] for p in ("(1st)", "(2nd)", "(3rd"))]
    show("known-placement projects with no LLM", by(lambda r: r["ai_role"] in ("own_ml", "none"), known), len(known))
    # tool-sponsor mentions: projects whose profile Sponsor tools/Architecture/What it is/Fit
    # line names the tool (verified by awk over the profile file)
    pinata = ["Backtracc", "Capsule", "Cheddarboxd", "Echo", "Eco Fast Track",
              "EcoLens (property evaluator)", "FrontierMap", "FUELICIENT", "GitFile",
              "KaizenDrive", "Monch", "poyo.ed", "Promising Products", "TalkTuahBank",
              "What's The Move?"]
    samba = ["Backtracc", "Echo", "EcoVerse", "InvestIQ", "Notable", "poyo.ed",
             "ToyoTrends", "Vestique"]
    show("uses/mentions Pinata", pinata, N)
    show("  of those, won Pinata", [n for n in pinata if "Pinata" in dict((r["name"], r["tracks_won"]) for r in rows)[n]], len(pinata))
    show("uses/mentions SambaNova", samba, N)
    show("  of those, won SambaNova", [n for n in samba if "SambaNova" in dict((r["name"], r["tracks_won"]) for r in rows)[n]], len(samba))
    hw = [r for r in rows if r["hardware"] == 1]
    print("hardware prizes:", {r["name"]: r["n_prizes"] for r in hw})
    print("mean prizes hardware vs other:",
          round(sum(r["n_prizes"] for r in hw) / len(hw), 2),
          round(sum(r["n_prizes"] for r in rows if not r["hardware"]) / (N - len(hw)), 2))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
