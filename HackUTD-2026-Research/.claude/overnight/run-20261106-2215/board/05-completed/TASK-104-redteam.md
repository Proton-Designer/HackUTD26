# TASK-104 · S8 red team of outputs/findings.md (owner eng2, fresh context) · move to 05-completed when done
You did NOT write findings.md. Your job is to try to break it.
Read: /Users/aymanmohammed/Documents/HackUTD-2026-Research/01_ANALYSIS_SPEC.md §1 (hard rules) and §7 (format); /Users/aymanmohammed/Documents/HackUTD-2026-Research/outputs/findings.md; /Users/aymanmohammed/Documents/HackUTD-2026-Research/data/tables/INDEX.md and every table a finding cites (data/tables/*.csv). Also outputs/archetypes.md and outputs/sponsor_cards.md if they exist (same checks, lighter).
For EVERY finding (0.1 … 7.2):
1. Recompute or look up each number in the cited table. Mismatch = error (quote both).
2. Rule checks: winner-vs-non-winner claims only for HackUTD 2025; no "win rate/lift/increases chance"; counts as "n of N (pct%)"; low n flagged; TYPE correct (association not stated as cause); fact vs inference.
3. Robustness: does it hold in the excl_weak table too? Is the gap within noise for that n (e.g. < ~3 projects difference)? Is there a counterexample in the tables the finding omits?
4. Is the IMPLICATION supported by the SUPPORT, or does it overreach? Does any implication contain a time/duration estimate (forbidden by the user)?
Output /Users/aymanmohammed/Documents/HackUTD-2026-Research/outputs/redteam_review.md: per finding: verdict HOLDS / WEAKEN (say how to reword) / DROP (why), with the evidence. Then a list of numeric errors, then missing findings the tables clearly support.
Rules: do not edit findings.md; every claim you make must cite a table row.
Report: TASK-104 · done · holds/weaken/drop counts · numeric errors n.
