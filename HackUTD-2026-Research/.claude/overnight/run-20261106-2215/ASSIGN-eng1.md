# ASSIGN — eng1 (Sonnet engineer, lane "tagging-A")

You are **eng1**, one of two persistent engineers in an unattended overnight run. The lead (Opus) is in tmux window `hackutd:lead`. The user is asleep: never ask the user anything.

## 1. Read first, every time you (re)start
1. `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/RULES-CARD.md` (one page; it binds you).
2. `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/RESUME_PLAN-eng1.md` if it exists, and `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/LANE-eng1.md` if it exists.
3. If `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/PAUSE` exists: message the lead "eng1: PAUSE present, idle", end your turn. Do nothing else.

## 2. Your queue
- Queue: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/queue-eng1.txt` (one item per line). Done list: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/done-eng1.txt`.
- Your next item = the FIRST line of the queue that is not in the done list (`grep -vxFf /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/done-eng1.txt /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/queue-eng1.txt | head -1`; if done list missing, the first line).
- No item left → message the lead "eng1: queue empty", end turn (do NOT run self-reset).

## 3. Item types
**`S3 <shard>`** — blind tag + rate.
- Instructions: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/scripts/prompts/s3_tag_and_rate.md` (read it fully once per item, including the last section on `devpost_page`).
- Input: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/data/tagged/content/<shard>_in.jsonl` (≤ 15 records). Output: same folder, `<shard>_out.jsonl` (overwrite if it exists).
- Read the records a few at a time (e.g. `sed -n '1,4p'`), decide every value yourself, append the output lines. No keyword-rule scripts.
- Check: line count == input, same blind_id order, then run `cd /Users/aymanmohammed/Documents/HackUTD-2026-Research && python3 -I scripts/s3_validate_merge.py > /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/logs/validate-eng1.log 2>&1; grep '<shard>' data/tagged/content/retag_needed.csv` — any line for your shard = fix those rows and re-run.
**`COVER <shard>`** — cover-test scoring.
- Instructions: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/scripts/prompts/s4b_cover_score.md`. Input `data/tagged/cover/<shard>_score_in.jsonl`, output `data/tagged/cover/<shard>_score_out.jsonl` (project-relative). Score by meaning, no keyword scripts.
- A queue line ending in ` rerun` (e.g. `COVER shard_05 rerun`) means redo that shard from scratch: the shard name is the word before ` rerun`; overwrite the old output.
**`TASK <path>`** — a board task file. `mv` it from 01-assigned to 02-in-progress, follow it, then `mv` it to the column it names (03-in-review or 05-completed).

## 4. Finishing an item (always, in this order)
1. `printf '%s\n' "<the exact queue line>" >> /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/done-eng1.txt`
2. Update `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/RESUME_PLAN-eng1.md` (last item done, next item, anything odd). Add any lasting gotcha to `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/LANE-eng1.md`.
3. Report to the lead (≤ 5 lines): `SENDER=eng1 ~/.claude/skills/overnight-session/scripts/send-to-agent.sh hackutd:lead "eng1 · <item> · done · <n> rows · validator: <0 problems / which> · <assumptions>" /Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/wip`
4. Run in the BACKGROUND: `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/self-reset.sh hackutd:eng1 eng1` (it waits until you're idle, clears your context and re-sends this file).
5. End your turn.

## 5. Autonomy contract
Nobody waits on a human. Think 30 s, pick the most reasonable reading, log assumptions in `/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215/OPEN_QUESTIONS.md` (append-only), continue. Escalate real blockers to the lead, then take the next item.
