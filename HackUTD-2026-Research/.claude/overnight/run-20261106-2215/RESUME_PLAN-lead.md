# RESUME PLAN — lead (read INSTRUCTIONS.md first; this is the state)

> HARD LIMIT: only lead + eng1 + eng2. No subagents/Agent tool. Compact at ~50% (lead too).

Project: /Users/aymanmohammed/Documents/HackUTD-2026-Research · $SD = .claude/overnight/run-20261106-2215 · tmux `hackutd` (lead, eng1, eng2).

## Done (outputs exist; see outputs/STATUS.md)
- S0 join: scripts/s0_join.py (+ s0a_extract_prize_labels.py, corrections.csv). data/processed/{projects,awards,editions,unmapped_labels}.csv, join_report.md. 1,148 counted projects; 1,232 awards; 127 paired tracks (341 projects); s_hackutd=69; 23 general 1sts at 24h events.
- S1b: scripts/s1b_fetch_devpost.py (curl). data/pages/page_facts.jsonl (NOT blind: has prize badges), cover_inputs.jsonl, images/. 1,087 pages ok.
- Blind inputs: scripts/s2_build_blind_inputs.py → data/tagged/blind_inputs.jsonl (+ scrubbed devpost_page), blind_key_map.csv.
- S2 pilot: round 1 (Sonnet×2) + round 2 (Opus vs Sonnet, revised prompt) all fields ≥70%; Opus rates presentation +0.37 vs Sonnet. data/tagged/pilot/agreement*.md. Decision: S3 all-Sonnet.
- S5 close reads DONE: outputs/close_reads/{hackutd_2024_winners,hackutd_2025_winners,calibration_tmobile_2025}.md + tables Q19_*, Q21_*.
- S6 partial: scripts/s6_q09_stacking.py (Q09_* tables). scripts/s6_tagged.py written, NOT yet run (needs content_all.jsonl). scripts/s6_lib.py helpers.

## In progress
- S4b cover test: glance DONE for all 13 shards (shard_01 rerun ok).
  Scores done: shards 00,02,03,04,06,08,12 (*_score_out.jsonl). Queued to engineers: eng1 COVER 05,09,11; eng2 COVER 07,10. shard_01 scoring: when glance ready → `python3 -I scripts/s4b_score_inputs_and_merge.py build` then prepend "COVER shard_01" to an engineer queue.
  Then: `python3 -I scripts/s4b_score_inputs_and_merge.py merge` → data/tagged/cover_test.jsonl (drops image-only glance rows). Cover scores cluster at 3/3 (ceiling) — report as limitation.
- S3+S4a tag+rate: 77 shards (data/tagged/content/shard_{pri,rest}_NN_in.jsonl, 15 rows each; pri first). Queues: $SD/queue-eng1.txt (odd lines), queue-eng2.txt. Engineers self-reset (self-reset.sh) after each item. Validate/merge: `python3 -I scripts/s3_validate_merge.py` → data/tagged/content_all.jsonl, validation_report.md, content/retag_needed.csv. Failed shard → delete its _out, re-append "S3 <shard>" to owner queue.

## Next steps (in order)
1. (after move to tmux) start watchdog: `nohup ~/.claude/skills/overnight-session/scripts/watchdog.sh $SD hackutd "2026-11-07 09:30" 20 >/dev/null 2>&1 &`; CronCreate recurring checkpoint every 10 min ("Overnight checkpoint: follow INSTRUCTIONS.md §6"). Compact self (see §6.7) since context is large.
2. Checkpoints until all 77 shards valid. When ≥ all pri shards valid you may run `python3 -I scripts/s6_tagged.py` early to debug it (it reads content_all.jsonl).
3. When cover + S3 done: run s6_tagged.py (debug errors; it has never run), s6_q09_stacking.py, check data/tables/INDEX.md. Add Q00 existing-field comparisons if missing (close-read tables cover much of Q0).
4. Board task for eng1 (when S3 queue empties): TASK-101 cross spot-check: 10 random rows from eng2's shards vs their inputs (agree/disagree per field) → data/tagged/spotcheck_eng1.md; eng2 likewise TASK-102 → spotcheck_eng2.md.
5. S7 (lead): outputs/findings.md (spec §7 outputs 0–8, mandatory finding format, every number → data/tables file), outputs/archetypes.md (Q4 cards from Q04_general_1sts.csv), outputs/sponsor_cards.md (17 sponsors: 06_ briefs + Q13_sponsor_card_rows.csv + close reads; note 06_ brief errors listed in STATUS open issues). Optionally give eng1 TASK-103 "draft sponsor_cards.md" to save lead context.
6. S8: TASK-104 for eng2 (fresh context): red team outputs/findings.md vs data/tables only → outputs/redteam_review.md (holds/weaken/drop per finding). Lead revises findings.md, logs changes.
7. S9 (lead): outputs/TRACK_DAY_KIT.md — matrix, sponsor cards, archetypes, minimum winning build, avoid list, §5 scoring sheet, cover/pitch/Devpost template, likely judge questions + answer angles.
8. STATUS.md final; shutdown per INSTRUCTIONS §7 (briefing.html → ~/Downloads, open; kill watchdog; keep-awake stop LAST).

## Facts to keep
- Usage file: ~/.claude-account-b/usage-state.json (five_hour.used_percentage, resets_at epoch). At 22:15: 5h 35% (resets 1794037800 ≈ 01:50 CST), 7d 47%.
- HarmoniQ repo has a plaintext Gemini key — user was told; mention in briefing.
- Close-read key results: HackUTD 2025 winners vs demo_ready vs random — ≥1 feature shown working 75%/42%/34%; agentic 58/34/24%; live URL 25/4/12%; 22 of 24 sponsor-domain awards used no sponsor product; no baseline entry targeted State Farm or Goldman (3 prizes each). 2024: 18/19 company-track winners solved sponsor's business problem; 11/19 used no sponsor tool; all 3 General winners banking-for-unbanked with new interaction. T-Mobile 2025: HarmoniQ gap = technical complexity (−2) and completeness (−1.5) (static JSON, missing endpoint); Auth0 = login only, ~1–3 person-hours (estimate).
- Q9: HackUTD 15 of 71 (21%) winners won 2+ awards; top pair sponsor_domain+mlh (5 of 15); general winners also won a sponsor prize 17–18% across event types.

- 22:22 lead in tmux; watchdog + checkpoint cron started (step 1 done).
- 22:24 shard_05 glance invalid again; QA regex widened; TASK-001 queued to eng2; after it: build + queue 'COVER shard_05' (append to eng1 queue).

## Checkpoint 22:26
- 30/1148 rows valid; 5 queue items done. Usage 5h 41% (resets 01:50), 7d 48%. AC power. caffeinate ok. Watchdog pid in watchdog.pid. Cron 80fd30bd every 10 min (session-only; recreate after any restart).
- context-usage needs: --project /Users/aymanmohammed/Documents --hours 3
- Lead compacted at 22:26 (367k). After compaction: re-read INSTRUCTIONS.md + this file; continue checkpoints.

## Checkpoint 22:30 (post-compact)
- eng1 COVER 11 done (scores 00-04,06,08,09,11,12 exist). Remaining: 05 (after TASK-001, eng2 at 47/85 glance), 07,10 (eng2 queue).
- NOTE: done-eng1 already contains "COVER shard_05" -> when re-queueing use a distinct line "COVER shard_05 rerun" so it is not skipped.
- 30/1148 rows valid; 6 items done. 5h 42%, 7d 48%. AC. caffeinate ok.
22:36 checkpoint: 105/1148 valid (7 S3 shards), 14 items done, 5h 45% 7d 48%, AC, caffeinate ok. Pace ~30%/h usage -> expect pause near 95%; reset 01:50.
22:45 checkpoint: 195/1148 valid, 20 items done, 5h 48% 7d 49%, AC, caffeinate ok. (usage-state.json read can race the writer; retry on KeyError)
- S6 note: empty/near-empty records get placeholder minimum ratings (eng1: 1s; eng2: minimum/unknown). In s6_tagged.py exclude rows whose blind input has no description/page text from rating means (report count excluded).
22:55 checkpoint: 302/1148 valid, 26 items done, 5h 51% 7d 49%, AC, caffeinate ok.
- 22:59 eng2 pri_21 skipped Meta Quest/Nord as "prize tracks"; prompt clarified (company product prizes count). Earlier shards may under-list sponsor_fit for product prizes -> S6: report sponsor_fit coverage vs awards with sponsor names as limitation; no re-tag.
23:05 checkpoint: 417/1148 valid, 34 items done, 5h 54% 7d 50%, AC, caffeinate ok.
- S6 note: sponsor_fit track labeling inconsistent across engineers (e.g. "Finance track" company vs organizer). In S6 join sponsor_fit entries to awards.csv sponsor mapping and keep only entries matching a real company sponsor; report dropped/added counts.
23:15 checkpoint: 510/1148 valid, 41 done, 5h 58% 7d 50%
- 23:15 s6_tagged.py trial run OK (rc 0, 528 tagged). sponsor_fit_for() already matches entries to the AWARDING sponsor by normalized name (reconciliation note mostly covered; check unmatched count). excl_weak views exist (evidence_depth C/low conf). Q15 waits on cover_test.jsonl.
- 23:22 S4b DONE: cover_test.jsonl 1071 rows (16 image-only excluded); dist 3:838 2:133 1:58 0:42 (ceiling). s6 rerun ok.
23:25 checkpoint: 624/1148 valid, 49 done, 5h 61% 7d 51%, AC ok.
- 23:36 725/1148 valid, 56 done, 5h 64%. Queued TASK-101 (eng1 checks eng2) / TASK-102 (eng2 checks eng1) after S3 items. NEXT after S3 done: final s6 run; then TASK-103 sponsor_cards draft to eng1 (write task then); lead S7 findings+archetypes.
23:45 checkpoint: 833/1148 valid, 63 done, 5h 68% 7d 52%, AC ok.
23:55 checkpoint: 953/1148 valid, 71 done, 5h 71% 7d 52%.
- 00:05 s6 bucket labels fixed (ranges like 0-2, 3-4). Spec sections 0,3,5,7 read for S7 (finding format; outputs 0-8). Early Q0: winners 2 flows 23% vs demo_ready 0%; agentic 47 vs 28%; 5-7 deps 22 vs 6%; presentation>=4 31 vs 14%; completeness>=4 22 vs 6%; data_to_decision 22 vs 48%.
00:11 S3 DONE 1148/1148. S6 final run.
- 00:11 queued TASK-103 sponsor_cards (eng1) and TASK-105 archetypes (eng2) after spot-checks. Lead now writes outputs/findings.md. After all three: TASK-104 red team (eng2).
- 00:14 findings.md v1 written (sections 0-8). Spot-checks done: 84% / 67% agreement (weak: presentation, tech rating, n_user_flows). TASK-104 red team queued to eng2 after TASK-105. NEXT lead: draft TRACK_DAY_KIT.md while eng tasks run; then revise findings after redteam.
- 00:16 TASK-105 archetypes accepted (A hw 22, B multimodal 16, C agent 11, D playful 9, E d2d 4). TRACK_DAY_KIT.md v1 written. Waiting: TASK-103 sponsor_cards (eng1), TASK-104 red team (eng2). Then revise findings/kit, STATUS.md, briefing, shutdown.
- 00:17 TASK-103 sponsor_cards accepted (17 cards, Q13_sponsor_card_stats indexed). Timing phrases removed from cards/archetypes. STATUS.md updated. TASK-106 red team kit+archetypes queued to eng1; TASK-104 (findings) running on eng2. After both: revise, then briefing+shutdown.
- 00:25 findings.md v2 (red team applied; 12 of 69 multi-award fix). Kit revised per redteam_kit_review. Close-read time estimates removed. Q15_cover_distribution_all added (835/1068). TASK-107 archetypes fixes -> eng2. NEXT: final check of kit, briefing.html, shutdown.
- 00:26 SHUTDOWN: all phases done; briefing written; engineers idle (queues empty).
