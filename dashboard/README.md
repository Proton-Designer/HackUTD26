# Agent Ops dashboard (projector view)

Live view of every Claude agent on the team: which laptops are online, how many agents each runs, which pipeline and step each is on, and an animated flow of agent-to-agent messages.

![layout](../Finalized-Idea/source/README.md)

## Run it (one laptop, connected to the projector)
- **macOS:** double-click `dashboard/start-dashboard.command` (first time: right-click → Open if macOS warns). It starts the server and opens Microsoft Edge at http://localhost:7777.
- **Windows:** double-click `dashboard\start-dashboard.bat` (opens Edge).
- **Any OS, terminal:** `python3 dashboard/server.py` (Windows: `py dashboard\server.py`), then open http://localhost:7777.

Needs only Python 3.9+ (no packages) and a GitHub token: it uses `gh auth token` automatically (so `gh auth login` once), or env `GITHUB_TOKEN`. **No token = DEMO mode** (realistic simulated data; the badge says DEMO). Force demo with `--demo`.

Other laptops on the same Wi-Fi can open the LAN URL printed at start (`http://<ip>:7777`).

Keys: **F** fullscreen · **R** replay recent messages · **D** details.

## Where the data comes from
- **Messages:** GitHub Issues/comments written by `scripts/comms/send` (see `/AGENT_COMMS_SETUP.md`).
- **Agents, machines, steps:** the "📡 Agent presence board" issue, updated automatically by every machine's Claude Code hooks (≈ once a minute while working; "idle" when the agent stops). Agents report their step with `bash scripts/comms/status <step#> "what"`.
- **Pipelines and step names:** `dashboard/pipelines.json` (edit to rename steps).

A machine shows **stale** after 3 min without a heartbeat and **offline** after 10. Polling uses ETags, so it costs almost nothing against GitHub's rate limit.

Files: `server.py` (collector + SSE), `public/` (UI), `CONTRACT.md` (data contract).
