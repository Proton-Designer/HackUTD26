# Shared helpers for Backfire agent comms. Sourced by send / inbox / setup.
# Portable: macOS (bash 3.2, BSD date), Linux, Windows Git Bash (GNU tools). Needs only git + gh.
REPO="${BACKFIRE_REPO:-Proton-Designer/HackUTD26}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
ID_FILE="$ROOT/.backfire-pipeline"
STATE_DIR="$(git rev-parse --git-path backfire-comms 2>/dev/null || echo "$ROOT/.git/backfire-comms")"
case "$STATE_DIR" in /*|[A-Za-z]:*) ;; *) STATE_DIR="$ROOT/$STATE_DIR";; esac
mkdir -p "$STATE_DIR" 2>/dev/null

me() {
  local v="${BACKFIRE_PIPELINE:-}"
  [ -z "$v" ] && [ -f "$ID_FILE" ] && v="$(tr -d '[:space:]' < "$ID_FILE")"
  case "$v" in P1|P2|P3|P4|P4a|P4b) echo "$v";; *) echo "";; esac
}

# Labels whose messages this pipeline receives. P4a (intel) and P4b (command center + story) also get to:P4.
my_labels() {
  echo "to:$1"
  case "$1" in P4a|P4b) echo "to:P4";; esac
  echo "to:ALL"
}
TARGETS="P1 P2 P3 P4 P4a P4b ALL"

# Run a command with an 8s cap when a GNU-style timeout exists (Git Bash, Linux, brew coreutils).
T() {
  if timeout --version >/dev/null 2>&1; then timeout 8 "$@"
  elif command -v gtimeout >/dev/null 2>&1; then gtimeout 8 "$@"
  else "$@"; fi
}

# epoch seconds -> ISO-8601 UTC (GNU date or BSD date)
iso_from_epoch() {
  date -u -d "@$1" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -r "$1" +%Y-%m-%dT%H:%M:%SZ
}
