# Pipeline: agents, models, stages and data flow

This file defines HOW the analysis in `01_ANALYSIS_SPEC.md` is run: which agent does what, with which model, in what order, and which files each stage reads and writes. The spec defines WHAT to measure. If the two ever disagree on a definition, the spec wins.

**Starting point:** data collection is mostly done. Folders `01_`–`06_` hold 1,152 projects read in depth, a non-winner baseline, sponsor research and 2026 sponsor briefs. This pipeline builds on those files. It does not re-collect them. All new work goes in `data/`, `scripts/` and `outputs/`.

## Principles

1. **Code counts, models judge.** Python scripts produce every number, percentage, crosstab and comparison from tagged data. No model writes a statistic from memory or by estimating.
2. **Derive before tagging.** If a spec field can be computed or mapped from existing records (spec §2.0.1), a script does it. Models tag only what is left.
3. **Models tag against fixed definitions.** Tagging agents fill the schema with an evidence quote or `unknown`. They do not draw conclusions.
4. **Synthesis, tagging and review are separate jobs.** The agent that writes findings never grades them. An independent reviewer does.
5. **Everything is a file.** Each stage reads from and writes to a fixed location, so any stage can be re-run or audited. Never modify folders `01_`–`06_` or `99_`. They are inputs.
6. **Blind where it matters.** Cover-test and deep-rating agents must not see placement, prizes or `dataset` labels. Strip them from the input.

## Roles and models

| Role | Model | Why |
|---|---|---|
| Orchestrator / lead | Claude Opus | Plans, dispatches shards, checks each stage's outputs against its contract, owns `outputs/STATUS.md`. |
| Join, derive, validators, statistics | Python scripts in `scripts/` | Deterministic and auditable. |
| Gap-fill readers (second pass, any expansion) | Claude Sonnet, in parallel | Same reading task the earlier passes did, against the existing data dictionary. |
| Field taggers (remaining spec fields) | Claude Sonnet, in parallel | Reliable at reading records against explicit definitions. Parallelizes well. |
| Deep raters (rubric 1–5) | Claude Sonnet; Claude Opus for HackUTD rows, the HackUTD 2025 baseline and paired 1st-vs-2nd/3rd sets | The strata that matter most for decisions get the strongest judgment. |
| Cover-test agent | Claude Haiku, blind | Deliberately simulates a fast, shallow first impression, like a judge glancing at a station. |
| Cover-test scorer | Claude Sonnet | Compares the blind answer with the full record and scores it 0–3. |
| Close reader | Claude Opus | Q19 (every HackUTD winner) and Q21 (the calibration case). |
| Synthesizer | Claude Opus | Turns computed tables and close-read notes into findings in the spec §7 format. |
| Red-team reviewer | A fresh Claude Opus or Sonnet instance that took no part in synthesis | Checks every finding against the tables. Honest and balanced, not contrarian. |

## Stages

### S0: Join and derive (Python)
- **In:** `04_deep_dives/data/deepdive_all.jsonl`, `01_winners/data/project_records.jsonl`, `02_baseline_non_winners/data/project_records.jsonl`, `03_sponsor_tracks/data/project_records.jsonl`, `ALL_PROJECTS_INDEX.csv`.
- **Do:**
  - Join everything into one table per project, following the join rules in spec §2.0. Collapse records listed in `duplicate_of`.
  - Compute every field the spec §2.0.1 mapping marks as derivable.
  - Assign `event_type`, `weight` and `recent` from the hackathon, edition and event dates.
  - Map prizes to `prize_kind` and `sponsor_industry`. Write any labels the script can't map to a review list.
  - Flag the analysis strata: HackUTD rows, the HackUTD 2025 baseline, paired sets with published placements, multi-award projects.
- **Out:**
  - `data/processed/projects.csv` (one row per project, with nested lists kept as JSON strings)
  - `data/processed/awards.csv`
  - `data/processed/editions.csv`
  - `data/processed/unmapped_labels.csv`
  - `data/processed/join_report.md`: counts, unmatched IDs, duplicates collapsed, placement coverage, and how many records are in each stratum.

### S1: Gap fill
- **S1a, second pass:** re-read the 289 projects in `04_deep_dives/second_pass_queue.txt` (evidence depth B/C or low confidence). Start with those in P1 strata. Sonnet readers use the deep-dive schema. Write updated records to `data/processed/second_pass.jsonl`. Never overwrite `04_`.
- **S1b, cover-test inputs:** for every project, fetch the exact Devpost title, tagline and first gallery image URL. Write them to `data/pages/cover_inputs.jsonl`.
- **S1c, expansion (lower priority):** the roughly 1,340 unanalyzed winners in `05_master_winner_lists` (smaller events, mostly unranked). Analyze them with the same schemas if broader coverage is wanted. Write to `data/processed/expansion.jsonl`.
- **S1d, baseline extension (lower priority):** a HackUTD 2024 non-winner baseline built the same way as `02_` (demo_ready plus random). Write to `data/processed/baseline_2024.jsonl`.
- Log what was fetched, what failed and what is still missing in `data/processed/gapfill_report.md`.

### S2: Tagger pilot (2 × Sonnet, independent)
- **In:** 30 projects stratified across HackUTD, the HackUTD baseline, other 24h events, sponsor vs general, placed vs unranked.
- **Do:** both taggers independently fill the spec fields that still need tagging. A script computes agreement for each field.
- **Out:**
  - `data/tagged/pilot/tagger_a.jsonl`
  - `data/tagged/pilot/tagger_b.jsonl`
  - `data/tagged/pilot/agreement.md`
- Any field under 70% agreement gets redefined and re-piloted, or dropped. Record the decision in `outputs/STATUS.md`.

### S3: Field tagging (Sonnet, parallel shards)
- **In:** for each project, its joined record plus its profile card. Go back to the Devpost page when a P1-critical field rests on depth B/C evidence.
- **Do:** fill the remaining spec §2.3 fields, with an evidence quote or `unknown` for each. A validation script checks the schema, the enums and that evidence is present. Invalid rows get re-tagged.
- **Out:**
  - `data/tagged/content/shard_XX.jsonl`
  - `data/tagged/content_all.jsonl`
  - `data/tagged/validation_report.md`

### S4a: Deep rating (Sonnet; Opus on the priority strata)
- **In:** joined record and profile with placement, prizes and dataset label removed.
- **Do:** score the six rubric dimensions in spec §2.4 from 1 to 5, with a one-line justification for each. Rate every project, priority strata first.
- **Out:** `data/tagged/deep_ratings.jsonl`

### S4b: Blind cover test (Haiku, then a Sonnet scorer)
- **In:** title, tagline and first image only, from `data/pages/cover_inputs.jsonl`.
- **Do:** the Haiku agent answers what it does, for whom, and why it matters. The scorer compares that answer with the full record and gives 0–3.
- **Out:** `data/tagged/cover_test.jsonl`

### S5: Close reads (Opus)
- **Q19:** read every HackUTD 2024/2025 winner in full: the profile cards in `04_deep_dives/profiles/winners/hackutd-*.md`, plus the Devpost page where needed. Write notes per project and patterns across projects. Contrast them with the HackUTD 2025 `demo_ready` baseline.
- **Q21:** HarmoniQ vs InsighT vs Beacon (HackUTD 2025 T-Mobile), as set out in spec Q21. Use `06_hackutd_2026_sponsors/t-mobile.md` for context.
- **Out:**
  - `outputs/close_reads/hackutd_winners.md`
  - `outputs/close_reads/calibration_tmobile_2025.md`
- This stage can run alongside S2–S4. Human teammates can add notes here too.

### S6: Compute (Python)
- **In:** `data/processed/*`, `data/tagged/*`.
- **Do:** run every computation named in spec §3 (Q0–Q23): baseline comparisons, paired gaps, the floor/differentiator table, minimum and spread, prize pairings, the pattern × sponsor-industry matrix and recency splits. Produce weighted and unweighted versions. Every cell carries n and N, and low-n cells are flagged. Where depth C or low-confidence records could change a result, report it with and without them.
- **Out:**
  - `data/tables/Qxx_<name>.csv` (one or more per question)
  - `data/tables/INDEX.md`, listing each table, the question it serves and the script that produced it

### S7: Synthesis (Opus)
- **In:** `data/tables/`, `outputs/close_reads/`, `06_hackutd_2026_sponsors/`, `03_sponsor_tracks/sponsor_prompt_library.md`, the spec.
- **Do:** write every required output in spec §7, with every finding in the mandatory format (FINDING / SUPPORT / COUNTEREXAMPLES / CONFIDENCE / TYPE / IMPLICATION). Cite a table file for every number.
- **Out:**
  - `outputs/findings.md`
  - `outputs/archetypes.md`
  - `outputs/sponsor_cards.md` (one card per confirmed 2026 sponsor, combining the `06_` briefs with past-winner evidence)

### S8: Red-team review (fresh instance)
- **In:** `outputs/findings.md` and `data/tables/`. The synthesizer's reasoning is not included.
- **Do:** check each finding:
  - Is the number in the cited table?
  - Is n large enough?
  - Is it labeled correctly as fact, association or inference?
  - Does a counterexample undercut it?
  - Is a winners-only comparison being misused?
  - Is the baseline comparison limited to HackUTD 2025?

  Give a balanced verdict for each: `holds`, `weaken` or `drop`.
- **Out:** `outputs/redteam_review.md`. The synthesizer then revises `outputs/findings.md` and logs the changes.

### S9: Track-day kit (Opus)
- **In:** the final `outputs/findings.md`, `outputs/sponsor_cards.md`, and spec §5–§6.
- **Do:** compress everything into a short, printable decision kit:
  - pattern × sponsor matrix
  - sponsor cards for the 17 confirmed sponsors
  - archetype cards
  - minimum winning build spec
  - avoid list
  - the §5 scoring sheet
  - cover, pitch and Devpost template
  - likely judge questions, with angles for answering them
- **Out:** `outputs/TRACK_DAY_KIT.md`, plus a .docx if the team wants a printable copy.

## Dependency graph

```
existing data (01_–06_)
   └─ S0 join+derive ─┬─ S1a/S1b gap fill ─┬─ S2 pilot → S3 tag ─┐
                      │                    ├─ S4a deep rating ───┤
                      │                    └─ S4b cover test ────┼─ S6 compute → S7 synthesize → S8 red team → S7 revise → S9 kit
                      └─ S5 close reads ─────────────────────────┘
   (S1c expansion and S1d baseline extension feed S0 again if run)
```

## Status tracking
The orchestrator keeps `outputs/STATUS.md` up to date. For each stage it records the state (not started / running / done / blocked), output files, counts and open issues. It also logs decisions, for example fields dropped after the pilot or how unmapped prize labels were resolved.
