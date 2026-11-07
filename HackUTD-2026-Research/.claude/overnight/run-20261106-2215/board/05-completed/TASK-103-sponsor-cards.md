# TASK-103 · draft outputs/sponsor_cards.md (owner eng1) · move to 03-in-review when done
Not blind (synthesis task): you may read data/tables, outputs/close_reads, 06_hackutd_2026_sponsors (read-only), 01_ANALYSIS_SPEC.md §0.2, §3 Q11-Q14, §7.
Inputs: /Users/aymanmohammed/Documents/HackUTD-2026-Research/data/tables/Q13_sponsor_card_rows.csv (one row per past winner of a HackUTD-2026 sponsor), Q11_pattern_x_industry.csv, Q10_sponsor_fit_by_placement.csv, Q19_hackutd2025_* tables, outputs/close_reads/*.md, 06_hackutd_2026_sponsors/<sponsor>.md, outputs/STATUS.md "open issues" (06_ brief errors: dataset wins over briefs).
Output /Users/aymanmohammed/Documents/HackUTD-2026-Research/outputs/sponsor_cards.md: one card per sponsor in spec §0.2 (all 17; sponsors with 0 dataset winners get a short "no dataset winners" card from the brief only, labeled [brief only]). Card fields:
- What the sponsor asked (from brief; mark [V]/[U] as the brief does) · prize structure if known
- Past winners in dataset: n, events, and per winner one line (name, placement, pattern, one_sentence, link)
- Counts from Q13: pattern distribution; problem_owner; prompt_literalness (0/1/2/na); sponsor_removable yes/no; median sponsor_features_used — every count as "n of N (pct%)", n<5 flagged low n
- What won (FINDING in spec §7 format: FINDING/SUPPORT/COUNTEREXAMPLES/CONFIDENCE/TYPE/IMPLICATION FOR US), 1–2 findings per sponsor max
- Pitch angle + integration depth rule for us (labelled inference)
Rules: every number must come from a table (name the table in each card footer). No team member names, no keys. Never invent winners. Keep the whole file under ~700 lines.
Report: TASK-103 · done · n cards · sponsors with 0 winners.
