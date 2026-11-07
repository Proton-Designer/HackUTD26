# Pipeline status

Concurrency (overnight run 2026-11-06/07): lead + 2 persistent engineers (overnight-session skill). No duration estimates anywhere; work is tracked by objective and dependency.

| Stage | State | Outputs | Notes |
|---|---|---|---|
| S0 Join + derive | done | `data/processed/projects.csv`, `awards.csv`, `editions.csv`, `unmapped_labels.csv`, `join_report.md`; `scripts/s0a_extract_prize_labels.py`, `s0_join.py`, `corrections.csv` | 1,148 counted projects; 127 paired tracks; HackUTD 69 winners, no published placement. |
| S1a Second pass | skipped | | Devpost page text (S1b) replaced it. |
| S1b Page fetch + cover inputs | done | `data/pages/page_facts.jsonl` (NOT blind), `cover_inputs.jsonl`, `images/`; `scripts/s1b_fetch_devpost.py` (curl) | 1,087 pages ok. |
| S1c / S1d optional expansions | deferred (not run) | | Out of scope for this run. |
| S2 Tagger pilot | done (2 rounds) | `data/tagged/pilot/agreement*.md` | All fields ≥ 70%; Opus rates presentation +0.37 vs Sonnet → all S3 tagging by Sonnet. |
| S3 + S4a Blind tag + rate | done | `data/tagged/content_all.jsonl` (1,148 of 1,148 valid), `data/tagged/content/shard_*`, `validation_report.md` | 77 shards by 2 engineers; `scripts/s3_make_shards.py`, `s3_validate_merge.py`; prompt `scripts/prompts/s3_tag_and_rate.md`. Cross spot-check 84% / 67% exact agreement (`data/tagged/spotcheck_eng1.md`, `spotcheck_eng2.md`). |
| S4b Cover test | done | `data/tagged/cover_test.jsonl` (1,071 rows) | Two-step blind glance + score; 16 image-only glance rows excluded; ceiling: 835 of 1,068 tagged projects = 3/3 (`Q15_cover_distribution_all.csv`). |
| S5 Close reads (Q19, Q21) | done | `outputs/close_reads/*.md`; tables `Q19_*`, `Q21_*` | |
| S6 Compute | done | `data/tables/` (see `INDEX.md`); `scripts/s6_tagged.py`, `s6_q09_stacking.py`, `q04_archetype_counts.py` | Re-run order: s3_validate_merge → s4b merge → s6_tagged → s6_q09_stacking. |
| S7 Synthesis | done (v2 after S8) | `outputs/findings.md`, `outputs/archetypes.md`, `outputs/sponsor_cards.md` | |
| S8 Red team | done | `outputs/redteam_review.md` (findings: 3 hold / 22 weaken / 2 drop; 11 numeric fixes), `outputs/redteam_kit_review.md` (kit + archetypes: 4 high / 16 med / 7 low) | Fresh-context engineers; findings.md v2 and kit revised; change log at end of findings.md. |
| S9 Track-day kit | done | `outputs/TRACK_DAY_KIT.md` | |

## Decisions log
- **HarmoniQ** is treated as an ordinary winner (user's past project; new team this year).
- **Tagging + rating in one blind pass (S3 + S4a merged).** Every agent input is scrubbed: no placement, prizes, dataset, sample group, IDs, URLs or source paths; sentences mentioning winning/prizes/placement removed; the same whitelisted fields for every dataset; "sponsor tracks considered" is taken from `prompt_fit.targeted_prizes` for winners and non-winners alike. Remaining limit: winners' targeted lists were partly written from what they won, so they may be narrower than non-winners' lists.
- **prize_kind enum + `theme_track`:** organizer-run themed categories (Healthcare Track, Education Track…) are neither general nor sponsor prizes.
- **event_type `unknown_duration`** for editions with no source on length (2 projects). Hybrid events are classed by hours like in-person events.
- **HackUTD "Toyota" track → Toyota Financial Services** (assumed).
- **Prize-label classification** was done by two Sonnet agents with keyword rules plus hand overrides. They shared one scratch folder, so `scripts/s0b_label_rules/` holds the last-written rule script only; the classified JSONL files are the authoritative record. 136 labels with low confidence or notes are listed in `unmapped_labels.csv` for review.
- **Pilot revisions after round 1:** `cost_of_problem_stated` — system/engineering metrics (latency, cold start) no longer count as `measured_by_team`; describing a gap without claiming size = `none`. `prompt_literalness` — anchors made concrete (prompt kappa was 0.43 on n = 27).

- **Corrections file** `data/processed/corrections.csv`, applied by `s0_join.py` (inputs stay read-only): InvestIQ "First Place" dropped (other hackathon's badge); Roomie and The Virtual Fitness Assistant excluded from HackUTD 2024 (unverified / Student Hacks badges). HackUTD now has 69 winners and no published general-track placement.
- **S6 Q9 computed** (`scripts/s6_q09_stacking.py`, tables `Q09_*`).

- **Overnight run decisions (2026-11-06/07):** single tagger model (Sonnet); empty/bundled records tagged with placeholders and covered by the excl_weak view; sponsor_fit used only when matched to the awarding sponsor by name (organizer-vs-company track calls varied by tagger); S6 bucket labels are ranges (0-2, 3-4…).

## Open issues
- HarmoniQ repo contains a plaintext Gemini API key (found in S5 calibration read; value not recorded). Owner told to rotate.
- Sponsor briefs `pnc.md`, `toyota_financial_services.md` say "2024 unknown" but the dataset has 3 winners each; `cbre.md` cites 2024 CBRE winner EcoManage, absent from the dataset. Sponsor cards (S7) must use the dataset.
- Video presence conflicts between first-pass and deep-dive on 14 of 35 HackUTD 2024 rows; DuckTalk and Backtracc share a video link (copy error). S1b page fetch (video embed) is the tiebreaker.
- `has_video` sources disagree (first-pass 774 true vs deep-dive 452 true). Devpost page fetch will settle it (video embed detection).
- Event-date errors in first-pass data (e.g. Hacklytics 2025 recorded as 2026; Knight Hacks "IX (2025)" is actually 2026) — S0 now uses web-verified dates.
