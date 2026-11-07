# RULES CARD (engineers; re-read after every reset/compaction)
Run folder $SD=/Users/aymanmohammed/Documents/HackUTD-2026-Research/.claude/overnight/run-20261106-2215 · project /Users/aymanmohammed/Documents/HackUTD-2026-Research · tmux session `hackutd`

> HARD LIMIT (user order): only the lead + eng1 + eng2. Never spawn subagents, background agents, forks, or use the Agent/Task tool. Compact/reset at ~50% context.

## Talk to the lead. Your pane is NOT a channel (highest priority)
- Nobody watches your pane. EVERY report, question or blocker goes to the lead with:
  `SENDER=<you> ~/.claude/skills/overnight-session/scripts/send-to-agent.sh hackutd:lead "<message>" $SD/wip`
- Before you end ANY turn, message the lead in that turn (done / blocked / waiting on what). Never end a turn on a question written only in your pane.
- The user is asleep. Never ask the user anything. If unsure: think 30s, pick the most reasonable reading, log it in $SD/OPEN_QUESTIONS.md (`printf '…\n' >> file`), continue.

## Pipeline
- One queue item at a time (see your ASSIGN file). Report once per item, ≤ 5 lines: `ITEM · status · files · checks (pass/fail + command) · NOT done/assumed`.
- State: $SD/RESUME_PLAN-<you>.md current at every item boundary. Lane knowledge (gotchas learned): $SD/LANE-<you>.md.
- Shared files are append-only: `printf '…\n' >> $SD/<file>`.

## Never
- Spawn agents. Ask the user. Retry an operation a hook denied (find another route, tell the lead).
- Edit anything in the project's numbered folders 01_–06_, 99_, or data/raw/ (read-only inputs). Write only your assigned output files.
- Read placement/prize/dataset information while tagging (no Devpost, no GitHub, no web, no files other than your item's input + instruction file). Blindness is the point.
- Generate tag values with keyword rules or heuristic scripts. Read each record and decide. Scripts only to write/validate JSONL.
- Store team member names, credentials or API keys.

## Always
- Validate your output before reporting (line count == input, order, enums) and run the project validator named in your ASSIGN file.
- Long output → file; bring back only the tail.
- Say what you did NOT do. Retry cap: 3 failures at the same step = blocker → tell the lead, take the next item.

Lead address: tmux hackutd:lead (SendMessage name documents-b7 after 22:21 move).
