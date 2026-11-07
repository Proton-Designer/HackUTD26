# Skill proposals (overnight-session) from run-20261106-2215

1. **Queue lines must be unique.** Engineers pick "first queue line not in done list" (grep -vxFf). Re-queueing an item already in done (e.g. a redo of COVER shard_05) is silently skipped. Rule: re-queue with a distinct suffix (" rerun") and say so in ASSIGN.
2. **Shell portability in task generators.** zsh does not word-split `set -- $var`; a loop created 2 malformed task files. Rule: wrap generator loops in `bash <<'EOS'`.
3. **usage-state.json can be read mid-write** (KeyError on first read). Rule: retry the read up to 3 times before acting on it.
4. **Validator-enforced typing in prompts.** Engineers repeatedly emitted string numbers / empty evidence and burned a validator round each time; adding an explicit "Output typing" section to the shared prompt cut repeats. Rule: put the validator's type rules verbatim into the worker prompt from the start.
5. **Two red teams with crossed authors** (engineer A reviews B's synthesis and vice versa) found 11 numeric errors and 4 high-severity reasoning issues the lead missed. Rule: every synthesis file gets a reviewer who did not write it, before the briefing.
6. **Grep for duration words in every output before shutdown** (hours/minutes/seconds/"first minute") when the user forbids time estimates; engineers reintroduced them in 3 places.
