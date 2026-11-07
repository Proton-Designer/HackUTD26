---
id: TASK-001
title: Redo cover glance for shard_05 (text-first)
lane: cover
risk: low
assigned: eng2
created_at: 2026-11-06T22:24
---
## Goal
The Haiku glance for cover shard_05 answered from images only (ignored taglines). Redo it.
## Do
Follow /Users/aymanmohammed/Documents/HackUTD-2026-Research/scripts/prompts/s4b_cover_glance.md exactly (incl. last two sections: one project at a time; title+tagline are the main source). You are simulating a FAST first glance: answer from title + tagline + image only, a few seconds per project, nothing else.
Input: data/tagged/cover/shard_05_in.jsonl. Output: data/tagged/cover/shard_05_glance.jsonl (project-relative to /Users/aymanmohammed/Documents/HackUTD-2026-Research).
## Accept
85 lines, input order; `python3 -I scripts/s4b_check_glance.py | grep shard_05` says ok. Then mv this file to board/05-completed/.
