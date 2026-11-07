# TASK-101 · cross spot-check (owner: eng1) · move to 05-completed when done
Goal: independent check of 10 rows tagged by eng2.
1. List shards eng2 tagged: `grep '^S3' /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/done-eng2.txt | awk '{print $2}'`. Pick 10 rows at random across them (python random with seed 101; record it).
2. For each row: read ONLY the input record (data/tagged/content/<shard>_in.jsonl, matched by blind_id) and the instruction file /Users/aymanmohammed/Documents/HackUTD-2026-Research/scripts/prompts/s3_tag_and_rate.md. Decide your own values for: pattern, ai_role, named_user, n_user_flows, has_hardware, live_data, novelty_source, the rubric ratings, and the sponsor_fit track list. THEN open eng2's output row (<shard>_out.jsonl) and compare.
3. Write /Users/aymanmohammed/Documents/HackUTD-2026-Research/data/tagged/spotcheck_eng1.md: table blind_id | field | yours | theirs | agree(y/n) | note; then per-field agreement (n of 10) and overall %; then systematic differences (e.g. organizer-vs-company track calls, rating offsets).
Rules: blind (no Devpost/web/other files), no keyword scripts, do NOT edit eng2's outputs.
Report: TASK-101 · done · overall agreement % · lowest field.
