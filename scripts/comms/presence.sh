# Presence heartbeat for the team dashboard. Sourced by inbox / status (needs common.sh + $ME + $STATE_DIR).
# One comment per machine on the issue labeled "presence", edited in place (edits send no notifications).
P_STATE="$STATE_DIR/presence_$ME"            # key=value lines: step_n, step_text, status_override, last_tool, last_file
P_SESS="$STATE_DIR/sessions_$ME"             # "<epoch> <session_id> <agent_id|main>" lines
host_name() { (hostname 2>/dev/null || uname -n) | tr 'A-Z' 'a-z' | sed 's/\.local$//; s/\.lan$//' | tr -cd 'a-z0-9._-'; }
os_name()   { case "$(uname -s 2>/dev/null)" in Darwin*) echo macOS;; MINGW*|MSYS*|CYGWIN*) echo Windows;; Linux*) grep -qi microsoft /proc/version 2>/dev/null && echo "Windows (WSL)" || echo Linux;; *) echo unknown;; esac; }
pget() { grep "^$1=" "$P_STATE" 2>/dev/null | tail -1 | cut -d= -f2-; }
pset() { { grep -v "^$1=" "$P_STATE" 2>/dev/null; printf '%s=%s\n' "$1" "$2"; } > "$P_STATE.tmp" && mv "$P_STATE.tmp" "$P_STATE"; }
jfield() { printf '%s' "$1" | grep -o "\"$2\" *: *\"[^\"]*\"" | head -1 | sed 's/.*: *"//; s/"$//'; }
jesc() { printf '%s' "$1" | tr -d '\000-\037' | sed 's/\\/\\\\/g; s/"/\\"/g' | cut -c1-160; }

# Record which session / subagent fired a hook and what tool it used.
note_hook() {
  local j="$1" sid aid tool file now
  [ -z "$j" ] && return 0
  now=$(date +%s); sid=$(jfield "$j" session_id); aid=$(jfield "$j" agent_id); tool=$(jfield "$j" tool_name)
  file=$(jfield "$j" file_path); [ -z "$file" ] && file=$(jfield "$j" notebook_path)
  [ -n "$sid" ] && echo "$now $sid ${aid:-main}" >> "$P_SESS"
  [ -n "$tool" ] && pset last_tool "$tool"
  if [ -n "$file" ]; then
    file=$(printf '%s' "$file" | tr '\\' '/'); file="${file#"$ROOT"/}"; pset last_file "$file"
  fi
  return 0
}

presence_issue() {
  local n; n=$(cat "$STATE_DIR/presence_issue" 2>/dev/null | tr -dc '0-9')
  if [ -z "$n" ]; then
    n=$(T gh api -X GET "repos/$REPO/issues" -f labels=presence -f state=open -f sort=created -f direction=asc --jq '.[0].number // empty' </dev/null 2>/dev/null)
    [ -z "$n" ] && n=$(T gh api "repos/$REPO/issues" -f title="📡 Agent presence board" \
       -f body="Machine-maintained. Each machine edits its own comment (scripts/comms). Read by dashboard/server.py. Do not close." \
       -f "labels[]=presence" --jq .number </dev/null 2>/dev/null)
    [ -n "$n" ] && echo "$n" > "$STATE_DIR/presence_issue"
  fi
  echo "$n"
}

# presence_push <working|idle|blocked>  (a "blocked" set via status sticks until the next status call)
presence_push() {
  [ "${BACKFIRE_PRESENCE:-1}" = 0 ] && return 0
  local status="$1" host n cid marker now cutoff sessions agents body ov
  ov=$(pget status_override); [ -n "$ov" ] && status="$ov"
  host=$(host_name); marker="<!-- presence:$ME:$host -->"
  now=$(date +%s); cutoff=$((now - 600))
  if [ -f "$P_SESS" ]; then
    awk -v c="$cutoff" '$1>=c' "$P_SESS" > "$P_SESS.tmp" 2>/dev/null && mv "$P_SESS.tmp" "$P_SESS"
    sessions=$(awk '{print $2}' "$P_SESS" | sort -u | grep -c .)
    agents=$(awk '{print $2"/"$3}' "$P_SESS" | sort -u | grep -c .)
  fi
  sessions=${sessions:-0}; agents=${agents:-0}
  [ "$status" = idle ] || { [ "$sessions" -lt 1 ] && sessions=1; [ "$agents" -lt 1 ] && agents=1; }
  local sn; sn=$(pget step_n | tr -dc '0-9'); [ -z "$sn" ] && sn=null
  body=$(printf '%s\n```json\n{"v":1,"pipeline":"%s","host":"%s","person":"%s","os":"%s","status":"%s","step_n":%s,"step_text":"%s","last_tool":"%s","last_file":"%s","sessions":%s,"agents":%s,"updated":"%s"}\n```' \
    "$marker" "$ME" "$host" "$(jesc "$(git config user.name 2>/dev/null)")" "$(os_name)" "$status" "$sn" \
    "$(jesc "$(pget step_text)")" "$(jesc "$(pget last_tool)")" "$(jesc "$(pget last_file)")" "$sessions" "$agents" \
    "$(iso_from_epoch "$now")")
  n=$(presence_issue); [ -z "$n" ] && return 0
  cid=$(cat "$STATE_DIR/presence_comment_$ME" 2>/dev/null | tr -dc '0-9')
  if [ -n "$cid" ] && T gh api -X PATCH "repos/$REPO/issues/comments/$cid" -f body="$body" --jq .id </dev/null >/dev/null 2>&1; then return 0; fi
  cid=$(T gh api -X GET "repos/$REPO/issues/$n/comments" -f per_page=100 --jq ".[] | select(.body | startswith(\"$marker\")) | .id" </dev/null 2>/dev/null | head -1)
  if [ -n "$cid" ]; then T gh api -X PATCH "repos/$REPO/issues/comments/$cid" -f body="$body" </dev/null >/dev/null 2>&1
  else cid=$(T gh api "repos/$REPO/issues/$n/comments" -f body="$body" --jq .id </dev/null 2>/dev/null); fi
  [ -n "$cid" ] && echo "$cid" > "$STATE_DIR/presence_comment_$ME"
  return 0
}
