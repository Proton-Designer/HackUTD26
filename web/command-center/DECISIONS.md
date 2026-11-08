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
- **Replay prefers `../../mock/events.json` (P1's file) and falls back to `fixture.js`.** The swap is automatic the moment P1 pushes `mock/`. `?src=fixture` forces the local file.
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
- **`intel.action`, `injection.denied`, `campaign.updated`: P4 guide leaves the fields open, so this is our proposal to P4a** (the fixture uses it; the parser is tolerant of missing fields):
  - `intel.action`: `{action_id, kind, label, target, scope: her|backfire_users|all_customers|external, approval: auto|analyst, status: auto_applied|queued|approved|applied|denied, simulated, evidence[], expiry, undo_token, reason}`
  - `injection.denied`: `{kind: injection|poisoning, attempt, requested_action, target, source, rule}`
  - `campaign.updated`: `{campaign_id, name, scam_type, status: observed|corroborated|confirmed, sightings, calling_numbers, strong_indicators[], immunity: {count, label, simulated}}`
- **Agent trace is built from those events** (INPUT on `artifacts.extracted`, TOOL per `intel.lookup`, PROPOSE + GATE per `intel.action`, GATE denied per `injection.denied`, ANALYST on approve). No extra trace event needed; nothing on it is invented by the page.
- **`blocklist.updated` merges into the matching auto action** (same number for scope her, the campaign link for scope campaign) so a block isn't listed twice; with P1's stub alone it shows as its own row.

## Test helper
- **`dev/fake_p1.py`: stdlib-only stand-in for P1's WS `/events` + approve endpoint + a `/publish` endpoint** so live mode and P4a's real lookups can be tested before P1's server exists. Not on the demo path.
