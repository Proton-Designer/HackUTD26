# web/command-center decisions (P4b)

One line each: chose X because Y.

## Stack
- **Plain HTML + CSS + one JS file, no build, no dependencies, no CDN.** Venue Wi-Fi is unreliable and there is no time to debug a toolchain; the page also opens straight from `file://`.
- **System fonts only, the same stack as Maria's phone** (`web/customer/style.css`: -apple-system / Segoe UI / Roboto; Cascadia Mono for values). No network needed to look right, and the two screens read as one product.
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

## Views (less on screen at once)
- **Three views instead of one dense console: Story (default), Agent, Everything.** The kit says make the first screen a judge sees spacious and allow density only in the one analytic view a technical judge explores (`12-visual-design.md`, "density vs white space"); the critic scored our 9-element console Design 3/5.
- **Story shows one chapter of the call at a time, two panels, bigger type:** during the call = conversation + risk; after = what the decoy extracted + agent trace; then = done automatically + Approve + denied. It follows the call by itself, and each chapter stays up at least 8 s before moving on, so the real-lookup payoff can't flash past.
- **Click a rail step to hold that chapter while you talk;** "Holding · back to live" (or Esc) follows the call again. Keys 1 / 2 / 3 switch views; the view is kept in the URL hash (`#story`, `#agent`, `#all`).
- **Agent view is for NVIDIA judges:** the full trace large, with the evidence and the gate's denials beside it.
- **A new call Maria answers restarts the rail and the Story view.** "Clear for next judge" (footer, or C) wipes this screen's state between judges without dropping the live connection; it does not touch the hub (P1's `scripts/reset_demo` does that).
- **Agent pipeline panel (after 21st.dev "AI Agent Pipeline" by Monolyth Dev, MIT; rebuilt in plain JS, no code copied).** Picked from a Dribbble / 21st.dev / component-library survey because it is the clearest "beyond a chatbot" picture for NVIDIA judges. Our real stages: Input (typed artifacts, or "demo stand-in") → Lookups (RDAP / chain / allowlist counts) → Nemotron (proposals; says "Fallback rules" or "Mock LLM" honestly) → Policy gate (decisions, "code, not the model") → done / waiting / denied. A dot travels along a link when that stage moves; the stage that moved last is outlined; the latest trace line sits underneath. It sits above the trace in Story's "what the decoy got", in Agent and in Everything, and adapts to its panel width with container queries.
- **"Done automatically" is an animated card list (after Magic UI's Animated List, MIT).** Newest card drops in on top and older cards glide down (FLIP); each card has an icon (🛡 Maria's block, 🔗 campaign, 📞 Scam Callback Protection, 🌐 approved network action, ⛔ callback rejected), scope and time. Analyst-approved network actions join the list, so the Approve click visibly lands in "what we did".
- **Panels are moved, not duplicated:** one set of panel elements; each view's layout in `app.js` places them in columns. Renderers find them by id, wherever they sit.
- **CSS and JS load with a timestamp query** so a cached copy on the demo laptop can't hide a fix pushed during the night.

- **Money trail view (key 4), drawn here from P4a's `GET /intel/chain`, not an iframe of `/intel/map`.** The embedded page was dark, had its own headline and only fit by shrinking it to ~60%; drawing it ourselves keeps the light look, our type scale at real pixel size, and labels on every node and amount. Three tiles on top (paid in by victims, moved to cash-out, held by Backfire / Maria's transfer pending), then victims → mule → cash-out with Maria's line dashed while pending and cut with "✂ HELD $X" once held. Polled every 3 s only while the view is open (CORS is open on that route). Hub not reachable: a saved snapshot in `fixture.js`, labelled "saved snapshot"; stale live data is labelled "hub not answering".

## Look (light by default, 2026-11-08 03:50, Rayan's pick)
- **Light look after Andika Wiraputra's "Sales Analytics Dashboard" on Dribbble** (`look-analytics.css`, loaded after `styles.css`): soft pink-to-mint wash, one floating frame, big white rounded cards with an icon chip per title, the black pill for the current view, the rail as hatched bar columns with the current step in textured magenta (the shot's black bar, swapped to T-Mobile magenta), risk as a segmented half-gauge with the band word inside (never a percentage), pastel status chips, green delta chips. `?look=dark` keeps the original.
- **Same rules hold in light:** text tokens re-picked for ≥4.5:1 on white (amber text darkened to #b45309, NVIDIA green to #4d7c0f), meaning never by color alone, Simulated labels unchanged. The white wordmark is inverted to near-black; the flame sits in a black circle.

## Brand
- **The team logo (flame + "Backfire" + "Caller beware.") is cut into transparent PNGs in `assets/`** (flame, wordmark, lockup, 64 px favicon), from the team's logo image, so it sits cleanly on our panels and needs no web font.
- **Header: flame + wordmark. Idle Story screen: the full lockup**, so the table reads "Backfire" from across the room before a call starts. Favicon = the flame.
- **Accent text uses the flame pink `#fe2e89`** (4.9:1 on panels). Filled buttons and the current rail step stay T-Mobile magenta `#e20074`, because white text on the lighter flame pink is only 3.5:1.
- **No animation changes opacity** (view changes slide 6 px instead): an animation paused in a background window must never leave the screen dim.

## Layout and visual design (judge gets it in 5 seconds)
Sources: `HackUTD-2026-Kit/domains/11-ux-interaction.md`, `12-visual-design.md`, `15-ai-app-design-eval.md`, `20-demo-delivery.md`, `decisions/pitch-demo.md` (template C), the HackUTD-2026-Research winner analysis, and the judge-critic review of our plan.
- **Top: one plain-English sentence + a 5-step rail grouped "During the call / After the call / Before the next ring"** (Detect, Hand off, Verify, Block, Immune). The kit caps a demo path at five steps, and the grouping uses T-Mobile's brief word for word ("before, during and after a threat"). Extract is folded into Verify ("5 artifacts · 5 lookups").
- **Idle is never blank: the headline is the tagline, word for word** as on the slides and Devpost ("T-Mobile customers hand a live scam call to an AI decoy that exposes and blocks the scammer").
- **One focal point: magenta covers about 10% of the screen** (headline emphasis, the current rail step, the one filled Approve button, the callback-rejected row). Everything else is gray. Kit: "make everything gray, give the one key series the single accent".
- **Exactly one filled button:** the first waiting Approve; the rest are outlined.
- **Color means the same thing on both screens.** Tokens copied from Maria's phone (`web/customer/style.css`): purple = Scammer Get Scammed / the decoy, red = scam / red flag / denied, green = done, amber = simulated / poisoning / held. NVIDIA green only for the engine and Nemotron trace lines.
- **Meaning never by color alone:** ✓ / ▶ on rail steps, ⚠ / ⛔ / ✓ on every lookup verdict, a word on every denial tag. Checked in grayscale.
- **Risk shows the level in words ("Likely scam", "Scam"), the detector score small underneath.** Kit anti-pattern "the bare model score", the brief's "honest confidence", and the critic's "likely scam instead of a percentage". The headline names the ask ("he's asking for her one-time code"), not a percentage.
- **Every number has a comparison:** immunity shows "+N since this screen opened"; domain age reads in human units ("3 days ago", "31 years ago").
- **Let the judge verify one claim:** real lookups (live, not simulated) carry a "verify ↗" link to the same public record (rdap.org, blockstream.info, eth.blockscout.com), URL-encoded, never the scammer's own site.
- **T-Mobile's product words:** "Scam Callback Protection", "Caller Verified" for STIR/SHAKEN A, "Scam ID (simulated)".
- **Maria's "after" is visible:** her blocks say "in Maria's protection log · she can undo" (the critic noted the console never showed her side). Undo tokens stay out of the UI.
- **Type and spacing from a fixed scale** (12/14/16/20/24/32 px, 4/8/12/16/24 px), 2 weights (400/700), one radius, 3 text grays all at least 4.5:1 on the panel color. One step up the scale at 1700 px and wider.
- **Panels are tinted, not boxed:** no borders, labels small and gray, values white. Risk and Call read as one card. Privacy is a slim always-visible footer strip (caller audio only, no audio stored, enclave attested, consented or synthetic voice, synthetic data) to give the call feed its height.
- **Motion only for state changes:** new rows get a brief tint; the hero flashes once when the callback is rejected (the one signature moment). No glows, no pulsing.
- **Tested at 1152x720 (1440x900 at 125% zoom), 1440x900 and 1920x1080.** The headline wraps to 2 lines instead of cutting off; three columns hold down to 960 px, then the page stacks and scrolls.
- **Three columns in story order:** the call → what we learned → what we did about it. Artifacts and their lookups are one card each ("wallet → 41 transactions" reads as one fact), money trail first.
- **Caller transcript and decoy turns share one feed;** during the handoff `transcript.caller` is hidden because `decoy.turn` (speaker=scammer) carries the same words.

## Honesty labels
- **"REAL LOOKUP" only shows when live and the event is not `simulated`;** in replay every lookup is tagged "replay" and the headline says "Lookup", not "Real lookup".
- **Every network action, the attestation, the immunity count and the carrier network carry a SIMULATED label.** Non-negotiable 7.
- **Decoy voice wording comes from `voice.enrolled` / `voice.deleted`.** If neither was seen (the screen opened after onboarding), it says "decoy voice", not "Maria's voice"; `?voice=clone` overrides for the demo.
- **Attestation is static text labeled Simulated** (no attestation event exists in the contract); it switches to on-device wording when `risk.update.engine` is `local`.
- **Stand-in artifacts are labeled everywhere they show (#35).** While Telnyx is blocked, P1's SIM_MODE hub publishes `artifacts.extracted` with `source: 'demo_stand_in'` (the script-card values) because P3's extractor isn't wired. The panel header says "Demo stand-in · extractor simulated", each card says "stand-in", and the trace, rail and headline say so too. The lookups that follow keep their own real / simulated tags.
- **Bank hold (#53): "$1,800 held before it reached the scammer" leads the headline** (until a callback is rejected) and the rail's Block step, and drops in as a 💵 card tagged "Simulated bank" (Capital One Nessie sandbox, mock data). An undo (`active: false`) strikes the card through and the headline falls back; a `skipped` hold (bank down) is never shown as applied, only as "not applied" in the trace. `flag_payee_bankwide` goes to the Approve queue; the `bank_transfer` lookup attaches to the payee card as "Bank (simulated)".
- **We never call a wallet, domain or number "scammer"** on screen; lookups state what the record shows ("Registered 3 days ago", "Matches Chase").

## Approve
- **Approve POSTs `/intel/actions/{id}/approve` to the server the WebSocket came from,** then flips the row to "✓ Simulated: applied". A later `intel.action` with status approved/applied from the server is merged, not duplicated.
- **If the POST fails in live mode, the row still flips, tagged "local only" with the reason.** A dead endpoint must not freeze the demo's payoff click, and the tag keeps it honest.
- **In replay, Approve applies locally** (tagged "replay: applied locally").

## Event shapes we read (seams)
- **P1/P2/P3 events: exactly the fields in `00_SHARED_RULES.md` §3.** Unknown event types are ignored.
- **`intel.lookup`: P4a's flat shape from `intel/lookups.py`** (`kind` domain|wallet|allowlist, `value`, `status`, `age_days`, `registrar`, `total_received`, `unit`, `tx_count`, `match`, `matched_org`, `source`, `simulated`). The page writes the one-line summary itself ("Registered 3 days ago", "2.31 BTC received, 41 transactions", "Matches Chase"). Verified live: real RDAP + allowlist results from `python -m intel.lookups` pushed through `dev/fake_p1.py` render with a REAL LOOKUP tag. Lookups attach to the artifact card with the same value (phones compared on the last 10 digits).
- **`intel.action`, `injection.denied`, `campaign.updated`, `blocklist.updated`: P4a's real shapes** (agreed in comms thread #17, checked against `python -m intel.demo_run`; older/looser shapes still parse):
  - `intel.action`: `{action_id, kind, target, scope, status: applied|queued|approved|denied|held, gate_status, approval: 'auto rule'|analyst|null, simulated, reason, evidence[], payload?}`. Labels come from our `KIND` map of P4a's kind names; `held` rows show in "Done automatically" with a pause icon.
  - `injection.denied`: `{attempted_target, kind (the action kind), target, reason, source, attempted_poisoning}`. `attempted_poisoning` decides POISONING; trust changes (`mark_number_safe`, `add_trusted_contact`, `unblock_number`, `allowlist_add`) or `source: artifact:instruction_to_ai` are INJECTION; anything else is NOT CORROBORATED. P4a also sends a denied `intel.action` for the same thing; we keep one row and one trace line.
  - `campaign.updated`: `{campaign_id, status, linked_via, sightings, independent_sightings, calling_numbers, numbers[], strong_indicators[], immunity: int, poisoning_attempt_seen}`. Immunity is P4a's count of numbers and indicators now blocked or warned for every Backfire user.
  - `blocklist.updated`: `{number, scope: her|campaign|network, undo_token, reason, active}`. Matched to actions at render time (her → the caller block, campaign → the campaign link, network → the approved network block), so it works whichever arrives first; `active: false` strikes the row through as undone.
- **Agent trace comes from P4a's trace events, never invented by the page:** `intel.plan` → INPUT + PLAN (and cards appear as "awaiting lookup"), `intel.lookup` → TOOL, `intel.agent` → NEMOTRON with its plan text, `intel.proposals` → PROPOSED n, `intel.action` → one GATE line each, `injection.denied` → GATE denied, approve → ANALYST. A divider marks each new call. If `intel.agent.engine` is a fallback or an offline mock, the line and the panel header say so in amber, never "Nemotron".
- **Lookups that match no extracted artifact get their own card** (P4a's plan steps and lookups can arrive without P3's `artifacts.extracted`). Offline-fixture lookups (`simulated: true`) are tagged SIMULATED even in live mode.
- **`instruction_to_ai` artifacts are shown as "Told the AI" chips, not cards;** the gate's `injection.denied` is the payoff.

## Test helper
- **`dev/fake_p1.py`: stdlib-only stand-in for P1's WS `/events` + approve endpoint + a `/publish` endpoint** so live mode and P4a's real lookups can be tested before P1's server exists. Not on the demo path.
