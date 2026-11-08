# NVIDIA quota: key split proposal (P1 handoff item 1)

Prepared by P4a, 2026-11-08 ~02:40. **No key values here or on GitHub; move keys by DM only.**

## The limit
- `integrate.api.nvidia.com` (build.nvidia.com free endpoints) shows about **40 requests/minute** as the default,
  per community reports and NVIDIA forum threads. NVIDIA doesn't publish it, so check your own build.nvidia.com
  account page.
- Responses carry **no rate-limit headers** (checked 02:38: only `x-request-id`), so a 429 is the only signal.
- The limit is most likely **per NVIDIA account, not per key**. Several keys from one account probably share the
  ~40 rpm, so the split below uses **one key per person's account**. A forum moderator reportedly said there is no official increase on the
  free tier (unconfirmed), so plan for backoff, not a higher cap.

## Who calls NVIDIA today (all read `NVIDIA_API_KEY`)
| Service | Process | NVIDIA calls | Rough load during one live call |
|---|---|---|---|
| P2 detection | `detection/app.py` | Lightning 30B per window (own token bucket `P2_CLOUD_RPM`, default **35**) + Parakeet STT via Riva per utterance | **up to ~35-45 rpm**, the biggest consumer |
| P3 decoy | `decoy/app.py` | Bolt E4B per turn + Magpie TTS per turn (+ STT if separate) | ~10-20 rpm while the decoy talks |
| Hub intel (P4a) | `server.main` (hub) | Super VL, **1 call per decoy call** (+1 retry max) | <2 rpm |
| Hub fallback detect | `server.main` (hub, only when `FALLBACK_DETECT`) | Lightning per window | 0 unless P2 is down |
| P2 eval | `detection/eval/run_eval.py` | `EVAL_CLOUD_RPM` (default 8) | 8-15 rpm for the length of the run |
| Android app | on Maria's phone | key entered in the app | phone path only |

One shared account is about 40 rpm, while detection plus decoy plus intel in a single call can need 50-60+.
That fits the 429s at 01:40.

## Proposal: one person's account per service
| Account (owner) | Used by | How to set it (no code change unless noted) |
|---|---|---|
| **A: Ayman** | **P2 detection** (LLM + STT), the live-path critical one | `NVIDIA_API_KEY=<A>` in the env of the `detection/app.py` process. Keep `P2_CLOUD_RPM` <= 30 so STT has headroom |
| **B: Evan** | **P3 decoy** (LLM + Magpie TTS) | `NVIDIA_API_KEY=<B>` in the env of the `decoy/app.py` process |
| **C: Kareem** | **Hub**: intel + fallback detect | already in the hub `.env`. Optional: `INTEL_NVIDIA_API_KEY=<C>` gives intel its own key even if the hub's `NVIDIA_API_KEY` changes (intel reads it first; added 2026-11-08) |
| **D: Rayan** | **P2 eval runs** (P2-1) + spare / Android phone | `NVIDIA_API_KEY=<D>` only in the shell that runs `run_eval.py`, at `EVAL_CLOUD_RPM<=15`; never during live rehearsals or judging |

Notes
- If P2, P3 and the hub run on one laptop (e.g. `detection/scripts/demo_local.sh`), set the key **per process**
  (`NVIDIA_API_KEY=... python -m decoy.app`) instead of in the shared `.env`. Each process reads its own env first.
- During judging, stop anything else using a live key (eval, acceptance scripts, test loops).
- If only 3 accounts exist: A = detection, B = decoy, C = hub + eval (eval only outside rehearsals).
- Fallbacks already in code: P2 cloud -> local Nemotron Nano 4B failover (463280f); intel -> deterministic fallback
  (shown as `engine: fallback`). A 429 degrades the demo but never breaks the call.

## To verify after the split
1. On the hub: `/demo/status` -> `NVIDIA_API_KEY_set: true`, `intel_engine: nemotron:...`.
2. One live call, then `python detection/scripts/call_report.py` -> 429 count should be 0.
3. `python -m intel.acceptance --hub http://localhost:8000 --require-nemotron --nessie` on the hub machine -> 12/12.

Sources: [NVIDIA forum: 40 -> 200 RPM request](https://forums.developer.nvidia.com/t/request-for-nvidia-build-api-rate-limit-increase-40-rpm-200-rpm/374704),
[NVIDIA forum: NIM 40 -> 200 RPM](https://forums.developer.nvidia.com/t/request-for-nvidia-nim-api-rate-limit-increase-40-200-rpm/380967),
[CodexBar issue (40 RPM default shown in account UI)](https://github.com/steipete/CodexBar/issues/2498),
[apis.io: NVIDIA rate limits](https://apis.io/rate-limits/nvidia/nvidia-rate-limits/).
