# web/command-center decisions (P4b)

One line each: chose X because Y.

## Stack
- **Plain HTML + CSS + one JS file, no build, no dependencies, no CDN.** Venue Wi-Fi is unreliable and there is no time to debug a toolchain; the page also opens straight from `file://`.
- **System fonts only** (Segoe UI / Cascadia Mono on Windows). Same reason: no network needed to look right.
- **Local fixture is a `.js` file (`fixture.js`), not JSON,** so it loads under `file://` where `fetch` is blocked.
- **Every event value is HTML-escaped before it reaches the DOM.** Transcripts and artifacts are scammer-controlled text; this screen must not be an injection path.
- **One bad event never breaks the screen:** each handler and each panel render is wrapped in try/catch (fail open, non-negotiable 8).

## Data source
- **Order: `?server=` → same origin → `http://localhost:8000` WebSocket `/events`; if none answers within 1.8 s, replay.** Ayman can mount this folder on the P1 server and it goes live with no config; on a laptop without the server it still demos.
- **Replay prefers `../../mock/events.json` (P1's file) and falls back to `fixture.js`.** P1's file is `{calls: [{call_id, events}]}` with each call's `ts` starting at 0, so calls are laid end to end with a 4 s pause. `?src=fixture` forces the local file, which is the richer full-demo rehearsal (it follows the contract enums and P4a's real intel output).
- **Once live, it stays live:** on disconnect it shows RECONNECTING, keeps everything on screen, and retries forever. It never silently switches to replay mid-demo.
- **Replay squeezes silences longer than 6 s (`?gap=`) and has `?speed=`.** Rehearsals at 2-4x; the demo itself is live.
- **Config is URL params only** (`server`, `src`, `speed`, `gap`, `mock`, `voice`). No settings UI, per the brief.
- **Rendering uses requestAnimationFrame plus a 250 ms timer fallback,** because rAF pauses in hidden windows and we may screen-capture a background window for the backup video.

## Layout (judge gets it in 5 seconds)
- **Top: one plain-English sentence + a 6-step rail (Detect → Hand off → Extract → Verify → Burn → Immune).** From across the table a judge reads the sentence and sees how far along the rail we are; panels are for the second look.
- **Campaign + immunity counter sit in the hero, top right,** because "every scam call makes every customer harder to reach" is the payoff number.
- **Three columns in story order:** the call (left) → what we learned (middle) → what we did about it (right).
- **Artifacts and their lookups are one card each,** not two panels: "wallet → 41 inflows" reads as one fact. Cards sort money-trail first (website, wallet, payment handle, callback numbers) so the payoff shows without scrolling.
- **Caller transcript and decoy turns share one feed** with a magenta divider at the handoff; decoy lines are right-aligned magenta bubbles. During the handoff, `transcript.caller` is hidden because `decoy.turn` (speaker=scammer) carries the same words.
- **The callback rejection is the loudest moment:** headline replaced, hero flashes, row added to "Applied automatically".
- **Colors:** T-Mobile magenta = Backfire acting; NVIDIA green = Nemotron engine and real lookups; amber = SIMULATED labels and poisoning; red = denied.
- **Privacy panel moved to the middle column** to give the live call feed the height it needs at 1440x900.

## Honesty labels
- **"REAL LOOKUP" only shows when live and the event is not `simulated`;** in replay every lookup is tagged "replay" and the headline says "Lookup", not "Real lookup".
- **Every network action, the attestation panel, the immunity count and the carrier network carry a SIMULATED pill.** Non-negotiable 7.
- **Decoy voice wording comes from `voice.enrolled` / `voice.deleted`.** If neither was seen (the screen opened after onboarding), it says "decoy voice", not "Maria's voice"; `?voice=clone` overrides for the demo.
- **The attestation panel is static text labeled Simulated** (no attestation event exists in the contract); it switches to on-device wording when `risk.update.engine` is `local`.

## Approve
- **Approve POSTs `/intel/actions/{id}/approve` to the server the WebSocket came from,** then flips the row to "✓ Simulated: applied". A later `intel.action` with status approved/applied from the server is merged, not duplicated.
- **If the POST fails in live mode, the row still flips, tagged "local only" with the reason.** A dead endpoint must not freeze the demo's payoff click, and the tag keeps it honest.
- **In replay, Approve applies locally** (tagged "replay: applied locally").

## Event shapes we read (seams)
- **P1/P2/P3 events: exactly the fields in `00_SHARED_RULES.md` §3.** Unknown event types are ignored.
- **`intel.lookup`: P4a's flat shape from `intel/lookups.py`** (`kind` domain|wallet|allowlist, `value`, `status`, `age_days`, `registrar`, `total_received`, `unit`, `tx_count`, `match`, `matched_org`, `source`, `simulated`). The page writes the one-line summary itself ("Registered 3 days ago", "2.31 BTC received, 41 transactions", "Matches Chase"). Verified live: real RDAP + allowlist results from `python -m intel.lookups` pushed through `dev/fake_p1.py` render with a REAL LOOKUP tag. Lookups attach to the artifact card with the same value (phones compared on the last 10 digits).
- **`intel.action`, `injection.denied`, `campaign.updated`, `blocklist.updated`: P4a's real shapes** (agreed in comms thread #17, checked against `python -m intel.demo_run`; older/looser shapes still parse):
  - `intel.action`: `{action_id, kind, target, scope, status: applied|queued|approved|denied|held, gate_status, approval: 'auto rule'|analyst|null, simulated, reason, evidence[], payload?}`. Labels come from our `KIND` map of P4a's kind names; `held` rows show in "Applied automatically" with a pause icon.
  - `injection.denied`: `{attempted_target, kind (the action kind), target, reason, source, attempted_poisoning}`. `attempted_poisoning` decides POISONING; trust changes (`mark_number_safe`, `add_trusted_contact`, `unblock_number`, `allowlist_add`) or `source: artifact:instruction_to_ai` are INJECTION; anything else is NOT CORROBORATED. P4a also sends a denied `intel.action` for the same thing; we keep one row and one trace line.
  - `campaign.updated`: `{campaign_id, status, linked_via, sightings, independent_sightings, calling_numbers, numbers[], strong_indicators[], immunity: int, poisoning_attempt_seen}`. Immunity is P4a's count of numbers and indicators now blocked or warned for every Backfire user.
  - `blocklist.updated`: `{number, scope: her|campaign|network, undo_token, reason, active}`. Matched to actions at render time (her → the caller block, campaign → the campaign link, network → the approved network block), so it works whichever arrives first; `active: false` strikes the row through as undone.
- **Agent trace comes from P4a's trace events, never invented by the page:** `intel.plan` → INPUT + PLAN (and cards appear as "awaiting lookup"), `intel.lookup` → TOOL, `intel.agent` → NEMOTRON with its plan text, `intel.proposals` → PROPOSED n, `intel.action` → one GATE line each, `injection.denied` → GATE denied, approve → ANALYST. A divider marks each new call. If `intel.agent.engine` is a fallback or an offline mock, the line and the panel header say so in amber, never "Nemotron".
- **Lookups that match no extracted artifact get their own card** (P4a's plan steps and lookups can arrive without P3's `artifacts.extracted`). Offline-fixture lookups (`simulated: true`) are tagged SIMULATED even in live mode.
- **`instruction_to_ai` artifacts are shown as "Told the AI" chips, not cards;** the gate's `injection.denied` is the payoff.

## Test helper
- **`dev/fake_p1.py`: stdlib-only stand-in for P1's WS `/events` + approve endpoint + a `/publish` endpoint** so live mode and P4a's real lookups can be tested before P1's server exists. Not on the demo path.
