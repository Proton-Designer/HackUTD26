# Failure drills (TASK-055), private stack
Hub :8190 + P2 :8102, own processes, SYNTHETIC irs.wav (Magpie voice, 2 caller lines, ask line "pay today with gift cards") streamed as Telnyx frames by `scripts/drills.py`. Gap = `alert.fired` time minus the end of the ask line (negative = alert came before the line ended). Single run each, 2026-11-08 ~04:50 CT. Real 429s were not produced: refused connections stand in for them.

| # | Drill | Result | healthz shows | Operator action |
|---|---|---|---|---|
| 1a | llama down (LOCAL_LLM_URL dead), cloud ok | 1 alert, gap -1.72 s, engine `cloud`, max s 0.97 | `local_reachable` false, `failovers.local_to_cloud` rising | none; watchdog restarts llama in ~2 min |
| 1b | llama AND cloud dead | 1 alert, gap -0.65 s from the rules floor (risk.update engine still labelled `local`), max s 0.95 | `local_reachable` false, `last_error` empty | none for the alert; restore llama/network for nuance |
| 2 | Riva and cloud LLM refuse (429 stand-in), llama up | 1 alert, gap -0.05 s (whisper finals are slower), 2 finals, engine `local`, max s 0.95 | `stt.primary_failures` 2, `primary_bypassed` true (bypass 30 s, then re-probes) | none |
| 3a | hub killed 1 s into the call, back 5 s later (before the ask) | 1 alert, gap -1.75 s, no duplicate; one early final lost while the hub was down | `hub_subscriber_connected` false then true within ~20 s; `last_error` hub.emit ConnectError | none; P2 reconnects by itself |
| 3b | hub down across the alert moment (8.5 s) | BEFORE fix: alert lost, 0 alerts (bug). AFTER fix (alert.py `_emit_alert`, retry up to 20 s): 1 alert delivered 6.9 s after the ask line, when the hub came back, no duplicate | same as 3a | none; if the hub stays down > 20 s the alert is dropped, restart the hub and press Continue/replay |
| 4 | P2 process killed mid-call (before the ask) | hub stays healthy (200); that call gets no alert (no detector); restarted P2 healthy in 0.8 s; the next call alerts normally (gap -1.03 s) | after restart: `local_reachable` true, hub sub true, counters reset | watchdog restarts p2svc on refusal; the call in progress is not recoverable from P2: P1's relay must reopen `/stt/<id>` |
| 5 | Tunnel URL changes | Not run live. Path by code + `tests/test_watchdog.py` (fake cloudflared): watchdog probes `<tunnel>/healthz` every 60 s, 3 fails in a row (~3 min) restarts p2tunnel, parses the new URL into `logs/p2_tunnel_url.txt` and logs `!!!! TUNNEL URL CHANGED !!!!`; never restarts while `active_stt_sockets`>0 | n/a (URL differs from before) | lead tells P1 `P2_STT_URL=wss://<host>`, P1 restarts the relay between calls. Faster: `WD_TUN_EVERY=1` makes detection ~1.5 min |

## Not covered
- Hub fallback detector (server/fallback_detect.py) takes caller transcripts from voip/Telnyx transcription, which this private stack does not have, so drill 4 does not show it covering a dead P2 (covered by server/tests/test_fallback.py only).
- Real 429 responses from NVIDIA, real Cloudflare tunnel churn, a hub restart under a real PSTN call, a P1 relay that reconnects after P2 dies.
- Each drill ran once. The risk.update during hub downtime is dropped (only alert.fired is retried).
Reproduce: `ACC_P2_PORT=8102 .venv/bin/python detection/scripts/drills.py 1a 1b 2 3a 3b 4` (source .env, LOCAL_LLM_URL set; drill 2 waits for `:8100` active_stt_sockets==0).
