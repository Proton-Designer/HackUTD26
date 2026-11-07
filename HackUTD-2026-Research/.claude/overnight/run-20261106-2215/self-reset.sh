#!/usr/bin/env bash
# self-reset.sh <tmux-target> <name> -- run in the BACKGROUND by an engineer as the last action of a queue item.
# Waits until the pane is idle, sends /clear, then re-primes the engineer from its ASSIGN file.
# Stateless queue work keeps no useful context, so /clear is cheaper than /compact (logged in SKILL-PROPOSALS).
T="$1"; N="$2"; SD="$(cd "$(dirname "$0")" && pwd)"
for i in $(seq 1 90); do
  sleep 6
  tmux capture-pane -p -t "$T" | tail -6 | grep -q 'esc to interrupt' || { idle=$((idle+1)); }
  [ "${idle:-0}" -ge 3 ] && break
done
[ -f "$SD/PAUSE" ] && { echo "$(date +%H:%M) $N paused, no reset" >> "$SD/logs/self-reset.log"; exit 0; }
tmux send-keys -t "$T" '/clear' Enter; sleep 8
"$HOME/.claude/skills/overnight-session/scripts/send-to-agent.sh" "$T" "Read $SD/ASSIGN-$N.md in full and follow it (fresh context after a queue-item reset)." "$SD/wip" >/dev/null 2>&1
echo "$(date +%H:%M) reset $N" >> "$SD/logs/self-reset.log"
