# P1 demo-day runbook (checklist)

Repo root, this Mac. No secrets here: values live in `.env` (gitignored). Never paste keys/PIN into chat or commits.
Reference detail: `docs/P1_RUNBOOK.md` (env table, endpoints), `detection/RUNBOOK.md` (P2), `decoy/README.md` (P3).
Hub = ONE process (hub + voip + relay + intel + `/app` + `/command-center`). Telnyx is Ayman's long-term account: no test calls, no config changes except the lead's `point_telnyx --apply`.

## 0. Cold start (live phone demo)
- [ ] `.env` has: `TELNYX_*` (API key, public key, app/connection/SIP/credential ids, scam line), `NVIDIA_API_KEY`, `DEVICE_PIN`, `PIPELINE_TOKEN` (same value on P2/P3), `P2_STT_URL` or `P2_BASE`, `P3_DECOY_URL` + `P3_VOICE_URL`, `MARIA_LEG` (`sip` default).
- [ ] `.env` must NOT have `SIM_MODE`, `VOIP_OPEN_TOKEN`, `DEMO_MODE`; leave `HUB_TOKEN` unset. A stale `PUBLIC_WS` in `.env` is ignored when a tunnel is reused or `NO_TUNNEL=1`.
- [ ] `ffmpeg` on PATH (decoy decodes voice enrollment, incl. iOS mp4).
- [ ] Window 1, decoy (P3), from its own venv (`decoy/.venv`, built by eng2; if missing: `python3 -m venv decoy/.venv && decoy/.venv/bin/pip install -r decoy/requirements.txt`): `set -a; . ./.env; set +a; HUB_URL=http://127.0.0.1:8000 decoy/.venv/bin/python -m uvicorn decoy.app:app --host 127.0.0.1 --port 8300`. Loopback only; it is normally already running (check `lsof -nP -iTCP:8300 -sTCP:LISTEN`; don't start a second one).
- [ ] Window 2, P2: `bash detection/scripts/run.sh` (supervised).
- [ ] Window 3, hub: `scripts/run_hub` (starts cloudflared, exports `PUBLIC_WS`, hub on :8000). Note the **public URL**. Keep this shell open: closing it kills the tunnel.
- [ ] Lead only: `scripts/point_telnyx` (dry run) then `scripts/point_telnyx --apply` (both URLs must print OK). Needed only when the tunnel URL changed.
- [ ] `scripts/preflight --live` (all PASS, exit 0). `--tunnel URL` if `logs/tunnel_url.txt` is stale.
- [ ] `<public URL>/demo/status`: voip/intel mounted, P2 + P3 `up`, `SIM_MODE` false, `HUB_TOKEN_set` false, `telnyx_ok` not false, `NVIDIA_API_KEY_set` true, `MARIA_LEG` as intended, `active_calls` 0.
- [ ] Maria's phone: open `<public URL>/app/`, pair with the PIN (once; pairing survives resets and restarts), Live Guard on, voice enroll or skip, allow sound.
- [ ] `scripts/reset_demo` (clean blocklist/intel, seeds the judge number).

## Judge call rules
- [ ] **English only** on the call (detection and the decoy are tuned for English).
- [ ] **Caller ID on**: no withheld/blocked numbers (the hub routes on the caller number; a withheld number cannot be scored or blocklisted).
- [ ] **One judged call at a time.** Wait for `call.ended` (and `active_calls` 0 in `/demo/status`) before the next judge.
- [ ] **No hub / decoy / P2 restarts during a call.** If a restart is unavoidable use `scripts/restart_hub_safe` (it refuses while a call is live; `--force` only on purpose).
- [ ] **Reset between judges:** `POST /demo/reset` (or `scripts/reset_demo`). Pairings survive resets and restarts, so the phone stays paired.
- [ ] **Tell P2 before any restart or rehearsal call** (P2 is on the shared NVIDIA quota; unannounced calls skew its tests and burn quota).
- [ ] **Customer wears earphones** (the phone mic must not hear the caller's audio: echo confuses detection and the talk path).
- [ ] **Keep the app open with the screen on** (iOS suspends a backgrounded or locked page: sockets, beeps and `/listen` audio stop). Disable auto-lock for the demo and do not switch apps.

## 1. Modes (`MARIA_LEG`, SIM)
| mode | how | what it does |
|---|---|---|
| `sip` (default) | nothing | hub dials Maria's WebRTC leg via Telnyx (conference) |
| `listen` | `MARIA_LEG=listen` | answer + caller stream only, no Maria dial; caller hears a short synthetic "Hello?"; Maria's page just listens (`WS /listen`) |
| `talk` | `MARIA_LEG=talk` | like listen, plus Maria speaks through `WS /talk/{call_id}` (her mic, muted while the decoy has the call) |
| SIM (phone-free) | `SIM_MODE=1` | simulated caller, no Telnyx requests; loopback only |
- [ ] Switch: edit `MARIA_LEG` in `.env` (or export `MARIA_LEG=talk` in the shell before the restart: it is in run_hub's keep-list, so an explicit shell value beats `.env`), then **safe restart** (section 4). Confirm in `/demo/status` flags.
- [ ] SIM on: `SIM_MODE=1 scripts/restart_hub_safe`; back to live: restart WITHOUT `SIM_MODE` and re-run `scripts/preflight --live`. Never leave SIM_MODE on with the real tunnel for a real demo.

## 2. Run a live call
- [ ] Before: section 0 green, `active_calls` 0, Maria's page open and paired.
- [ ] Caller dials the scam line. Expect: `call.incoming` + `call.routed LIVE_GUARD` (command center), Maria's page rings, she answers.
- [ ] Alert + two beeps on the scammer's ask (~8-20 s). She taps "Scammer Get Scammed": `handoff.started`, decoy takes the caller; Maria's mic is muted in talk mode.
- [ ] After hang-up, ~10-45 s: `blocklist.updated` / intel block on the command center.
- [ ] Listeners (judges' browsers) attach with `WS /listen/{call_id}` as soon as `call.incoming` is on the bus (max 3; a reconnect from the same paired device replaces its old socket).
- [ ] After: `.venv-hub/bin/python detection/scripts/call_report.py --last 1` (P2 timeline: first alert, finals, engine fallbacks, 429s). Hub side: `tail logs/hub.log`; per-socket `talk`/`listen` lines give accept/replace/close reasons and `talk_frames` counts.
- [ ] Between judges: `scripts/reset_demo`.

## 3. Phone-free (rollback if Telnyx/phones fail)
- [ ] Hub in SIM mode: `SIM_MODE=1 scripts/restart_hub_safe` (reuses the tunnel; SIM webhooks are loopback-only so the tunnel stays safe).
- [ ] Demo audio exists: `logs/sim_scam.wav` (else `scripts/make_scam_wav.sh`), also served at `GET /demo/caller.wav`.
- [ ] `scripts/preflight` (default = SIM checks) then `scripts/demo_call --reset` (prints the phone-test steps first, then a timeline). Tap the button on Maria's page after the alert. Say the caller is simulated.
- [ ] Total fallback (no P2/P3/telephony at all): second terminal `HUB_PORT=8001 scripts/run_hub --fallback` (looped replay, say it is a replay), or `POST /demo/replay` on the running hub.

## 4. Safe restart
- [ ] `scripts/restart_hub_safe --check` (prints `active_calls` and call-id prefixes; exit 2 if a call is live).
- [ ] `scripts/restart_hub_safe` refuses while `active_calls>0`; `--force` only if the call is already dead/ignored. It reuses the running cloudflared (same URL, Telnyx stays valid); `--new-tunnel` opts out (then re-point Telnyx).
- [ ] Do NOT Ctrl-C/kill the OLD `run_hub` shell: its `wait` keeps cloudflared alive; killing it kills the tunnel.
- [ ] After: `scripts/preflight --live`, `/demo/status`.

## 5. When X fails
| failure | do |
|---|---|
| Telnyx 401/10009, `telnyx_ok` false, no credit | stop; do not retry calls. Lead decides. Go to section 3 (SIM) or `--fallback` |
| NVIDIA 429 / key dead | calls still connect; P2 falls back to rules, hub `FALLBACK_DETECT=1` adds regex+LLM backup (fails to regex), intel falls back to baseline rules. Keep one call at a time; avoid extra test runs |
| Tunnel dead / URL changed | `scripts/restart_hub_safe --new-tunnel` (not while a call is live), lead runs `point_telnyx --apply`, reopen `/app/` on the phone (pairing survives) |
| P2 tunnel URL changed (P2 runs on ANOTHER machine, so its watchdog cannot write our files) | the lead writes the new origin (`https://<host>`) to `logs/p2_tunnel_url.txt` on the hub machine when P2 reports a new URL; the hub re-reads it on every P2 connect (retries every 2 s), no hub restart; `scripts/preflight` checks it. Remove the file to go back to `P2_STT_URL`/`P2_BASE` |
| P2 down | calls connect, alerts lost: set `FALLBACK_DETECT=1` (needs restart) or switch to SIM/fallback replay |
| P3 decoy down | `/demo/status` P3 not up; handoff returns false and Maria keeps the call. Restart decoy (window 1); `DECOY_STANDIN=persona` hub stand-in voice is used when `P3_DECOY_URL` is unset |
| Maria's WebRTC leg rejected | switch to `MARIA_LEG=listen` or `talk` (no dial), safe restart |
| Phone can't pair / 401 | wait 1 min (rate limit) or pair from the hub machine on localhost; check the PIN is the `.env` `DEVICE_PIN` |
| Hub crashed | `scripts/run_hub` again (no active call to protect); `scripts/preflight --live` |
