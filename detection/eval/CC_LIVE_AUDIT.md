# Command center: live-data audit (TASK-093, eng1, read-only on P4b/P1 files; trunk as of ~06:25 CT)
Files: `web/command-center/app.js` (A), `fixture.js` (F), `index.html` (H). Part 3 (events and panels during a real call) is added after the call.

## 1. Current behaviour: live vs replay (to verify against P4b's change when it lands)
- Tunnel check (curl + a read-only `wss://.../events` subscribe from WSL, no events posted): page 200, WebSocket opened in **0.2 s**, 0 events in 12 s while idle (expected, no call). Redaction on the tunnel could not be judged without a call (see part 3).
- `boot()` (A:1526-1540), `src=auto`: candidates = [same origin, `TEAM_HUB`, `http://localhost:8000`]. Per-candidate timeout **5 s remote / 1.8 s local** (A:1459, not 2 s). On a hub-served page the first two are the same URL, so a slow tunnel costs 5 + 5 + 1.8 = **~12 s**, then `startReplay()` (A:1519-1522) plays `mock/events.json` or the fixture call.
- **No way back:** nothing retries live after `startReplay()`. A single tunnel hiccup at page load means replay for the rest of the session. Only `?src=live` retries forever.
- **Label:** the REPLAY/LIVE pill (`renderSource`, A:1206) is a no-op now: `#source` and `#engine` no longer exist in index.html (P4b removed the header pills, cdc48b2). What remains: footer text (A:1413) `N events · wss://host/events` for live vs `k/N events · space pause...` + a play button for replay. The replayed fixture call (Daniel / Chase / Alex Sandbox...) looks exactly like a real call on the main panels. Judges would not notice.
- **Money trail:** `pollChain()` (A:1233-1250) on any fetch error uses `window.BACKFIRE_CHAIN` (F:189, 7 named victims, $18,100 in, $1,800 customer line) even while the WebSocket is live, labelled only by the small `map-meta` text `saved snapshot` (A:918). The payoff checklist (A:1107-1120, "That account took $18,100 from 7 other people") reads the same data and has no label.
- **Stale tunnel URL:** `TEAM_HUB` is hard-coded (A:1447) to today's trycloudflare host; it also feeds the Approve POST base and `pollChain`.

**Exact fix for P4b** (same as #112, with line pointers):
1. `boot()`: when the page is served over http(s) from the hub (same origin), never fall back to replay: set `MODE` to reconnecting and `retryForever(origin)` (replay only with explicit `?src=mock|fixture`). Dedupe `cands` (origin == TEAM_HUB). Remote handshake timeout 5 s is fine to keep for the first try; the retry loop makes it harmless.
2. Always-visible badge (a `<span id="source">` in the header or the hero): `LIVE` green / `RECONNECTING` amber / `REPLAY (recorded call)` red, with a red top border on the whole screen in replay. `renderSource` already builds the strings; it only needs its element back.
3. `pollChain()`: if `MODE.kind` is `live` or `reconnecting`, never assign `BACKFIRE_CHAIN`; keep the last live data marked stale, or show "waiting for the hub". Snapshot only when `MODE.kind === 'replay'`.
4. `TEAM_HUB`: read it from `?server=` or `location.origin` only; keep the constant for a replay-from-file case, not for live.

## 1b. Verification of P4b's b0b4e3d (#112), ~06:40 CT (code + jsdom, `index.html` + real `fixture.js`/`app.js`, URL `https://hub.example/command-center/`, mock WebSocket)
| scenario | result |
|---|---|
| hub-served page, WS handshake always fails (checked +1.5 s and +21 s) | badge `RECONNECTING to the hub…`, mode `reconnecting`, 0 events, **no replay started** (old build: replay after ~12 s) |
| hub-served, WS opens | badge hidden, mode `live` |
| socket drops after live | badge `RECONNECTING to the hub…` (screen content kept) |
| `?src=fixture` while a WS would open | badge `REPLAY · recorded test call`, mode `replay`, fixture events (headline "Ringing the customer...") |
| `?src=mock` | same replay badge |
- Badge cannot show "live" on a replay: it is hidden only when `MODE.kind` is `live`; `startReplay()` sets `kind:'replay'` and calls `renderAll()` (A:1522-1524). A replay page never opens a socket (`boot()` returns before `serverCandidates()` for `mock`/`fixture`).
- Money trail: the snapshot is assigned only when `MODE.kind === 'replay'` (A:1245-ish). Live failure leaves `CHAIN.data` null / stale-labelled.
- **Still not clean (all low, P4b):** (a) `TEAM_HUB` (A:1449) is still in `serverCandidates()` after the same origin, and `pollChain` falls back to it (`MODE.base || CFG.server || TEAM_HUB`, A:1238) before the first connect: after a tunnel restart a stale host could be attached or polled; also `http://localhost:8000` is a candidate, so a dev hub on the viewing laptop could be attached and shown as live. When `FROM_HUB`, use `[location.origin]` only. (b) "Live stays clean" means no positive LIVE badge: a judge cannot tell "live and idle" from "frozen" except the footer `N events · wss://host`; consider a small green LIVE dot. (c) Static text "The scammer is now talking to Nemotron" (A:487) is not read from an event (true for the demo). (d) Whether the tunnel viewer gets unredacted `transcript.caller` depends on the hub's `EVENTS_REDACT`; check during the call.
- Nothing else hard-coded remains on the live path: `BACKFIRE_FIXTURE` and `BACKFIRE_CHAIN` are reachable only in replay; amounts, victim names, counts and the immunity number come from events or `GET /intel/chain`.

## 2. Hard-coded or fixture-only content that can reach the screen on a live path
| file:line | what | live field / action | owner |
|---|---|---|---|
| A:1519-1522, F:1-184 | whole fixture call (Daniel / Chase / SSN-OTP text, risk 0.22..0.95, decoy turns, intel events) plays whenever live probe fails | never auto-replay when served by the hub (fix 1) | P4b |
| A:1233-1250, F:189 | `BACKFIRE_CHAIN` snapshot: 7 victims (Alex/Priya/Jordan/Sam/Taylor/Morgan/Casey Sandbox), $18,100 in, $17,300 out, customer $1,800 line, cash-out amounts | `GET /intel/chain` only; no snapshot while live (fix 3) | P4b |
| A:918 | map-meta shows `saved snapshot` only in small text | red label or hide the map when not live | P4b |
| A:1107-1120 | payoff lines "took $X from N other people / $Y already moved" use CHAIN.data (may be snapshot) | same gate as above; show only when `CHAIN.live` | P4b |
| A:1447-1452 | `TEAM_HUB` tunnel URL constant (stale after any tunnel restart) | `location.origin` / `?server=` | P4b |
| A:1206-1216 | source pill code with no element in H | restore a visible LIVE/REPLAY badge | P4b |
| A:487-488 | "The scammer is now talking to Nemotron" static text on handoff (true for the demo: decoy = Nemotron; not read from an event) | acceptable; or use `decoy.turn.engine` if the hub sends it | P4b (low) |
| A:283-291 | "He got $0" / "$X stopped" only after real `intel.action` events (hold amount from the event) | fine: driven by events | none |
| A:681-700 | immunity count from `campaign.updated` | fine | none |
| H:73 | `map-meta` default "Capital One Nessie sandbox · mock bank data" | true label; keep | none |
| H:43 and idle hero text | marketing line shown before the first call | fine, but identical to the "waiting" state of a dead connection: show RECONNECTING when no socket | P4b |
| P2 via risk.update | band and s come from `detection` (`schema.band`), `engine`/`model` from the event | verified in jsdom (TASK-078) | none |
| customer app (web/customer/*) | no detection numbers, accuracy or model names; voice text is static consent copy | fine | none |

## 3. During a real call (judge's-seat QA, eng1, read-only mirror, 08:19-08:21 CT)
Method: a read-only websocket (never posts) on the hub tunnel `wss://reg-subjects-curriculum-whenever.trycloudflare.com/events`, every event fed to the REAL `web/command-center/app.js` in jsdom; one line per panel change with the wall clock (`$S/jd/mirror2.js`, scratch). jsdom shows DOM text and logic, not pixels or animation timing.
- **Redaction: OFF for the tunnel viewer.** `transcript.caller` arrived with its text through the tunnel. The tunnel request carries Cloudflare proxy headers, which `server/device.py:37` treats as NOT direct-local, so this was a remote viewer, and it still got the words. (If `EVENTS_REDACT=1` were on the text would be empty.)
- **A screen that joins mid-call shows nothing for that call** (P4b #119: events for a call it never saw ring are ignored). Call 5921f090 (08:50 joined late): 100+ events counted, no panel moved. This is by design but a judge who opens the page during a call sees the idle state until the next call rings.
- **Call 6853b298 (rang 08:19:29; full path seen from the ring), panel by panel:**
| time (wall) | event | what the screen did | lag |
|---|---|---|---|
| 08:19:29 | call.incoming, call.routed | headline "Ringing the customer with Live Guard on", sub "+1 512-... · Caller ID not verified" | <1 s |
| 08:19:37 | user.action (answer), call.answered | "The customer answered. Live Guard hears the caller only." | <1 s |
| 08:19:46 | first risk.update | "Live Guard is listening · low risk", risk 0.05 | |
| 08:19:48 | alert.fired | headline "Likely scam: he's asking for gift cards", hero alert class, risk 0.90 "Two beeps sent", rail step 1 lit | 0.4 s after the event |
| 08:19:50 | user.action + handoff.started | "The decoy took over in the decoy voice", rail step 2, risk 0.95 stage payment, "impersonates extended warranty" | <1 s |
| 08:19:52 onward | decoy.turn | "The scammer is talking to the decoy in decoy voice", sub "Reply in N ms" per turn (684-808 ms) | |
- **Odd/wrong, judge-visible:** (1) the first decoy line shows "Reply in 0 ms" (08:19:52): the generated first line reports `latency_ms` 0. (2) A call answered and ended 1.7 s later (58e9ec64) left no stuck state. (3) Between calls the page returns to the idle headline "T-Mobile customers hand a scam call to an AI decoy..." (good).
- **Not seen yet in this window:** artifacts/haul panel, Money trail (`/intel/chain`), blocklist/campaign panels, restored. Events for the post-call intel chain did arrive on the wire for the earlier call 5921f090 (intel.plan, campaign.updated, intel.agent, intel.proposals, blocklist.updated, 4 intel.action at +107-109 s) but were ignored by the screen because that call never rang here, so the panels they drive are unverified live.

## Event matrix (TASK-094, eng2, read-only, trunk as of ~06:35 CT; checklist for the Card 2 call)
Method: grepped every emit/publish site (`server/ voip/ decoy/ detection/ intel/`), the hub bus + WS code (`server/bus.py:35-59`, `server/main.py:61-80`), and the handler table in `web/command-center/app.js:403-708` (dispatch `app.js:805-818`). Not verified on the live hub host (it is not on this machine): the live env flags. **Forwarding rule:** every `bus.publish` goes to every `WS /events` subscriber (`bus.py:43-48`; filter is only `?call_id=`). With `EVENTS_REDACT=1` a remote viewer that is not loopback/paired gets `transcript.caller.text=""` and `artifacts.extracted.artifacts=[]` plus masked phone numbers (`main.py:53-59`, `docs/P1_RUNBOOK.md:81`). Check this is OFF for the command-center tunnel viewer, or the feed shows no caller words and the artifacts panel is empty.

| event | emitted live by (file:line) | trigger on a live call | hub to WS | app.js handler (panel) | live-path gap? |
|---|---|---|---|---|---|
| call.incoming / routed / answered / ended | P1 `voip/router.py:129,135,173,182,212,230,244,688` | Telnyx webhook; ended on hangup | yes | `:403/411/425/435` (header, call focus, `call.routed` also payoff+map) | none |
| transcript.caller | P2 `detection/stream.py:118,178` via POST /events | caller utterance (partial + final) | yes (**redacted text if EVENTS_REDACT=1**) | `:441` (feed). Ignored while `handoff` and not `restored` (`:444`): decoy.turn carries both sides | none; redaction risk above |
| risk.update | P2 `detection/alert.py:224` | each scored window | yes | `:452` (Risk panel, header, attest) | none |
| alert.fired | P2 `detection/alert.py:184,193`; hub fallback `server/fallback_detect.py:219` only if `FALLBACK_DETECT=1` (off live) | first at s>=0.80 / hard ask; realert on rise | yes (hub drops duplicates, `main.py:100`) | `:474` (feed line "Two beeps", Detect stage) | none |
| user.action | hub `server/main.py:185` (POST /user/action) | customer taps Fire Back / Continue / Hang up / Answer / Decline | yes | `:480` (feed; `scammer_get_scammed` sets Handoff stage + banner) | `answer`/`decline` have no text in the handler's map (falls to generic "Customer: ...") |
| handoff.started / restored / failed | P1 `voip/router.py:524 / 662 / 512` | after Fire Back (restore = customer steps back in) | yes | `:490`, `:499`; **`handoff.failed` has NO handler** (`H['handoff.failed']` absent, falls through at `:808`) | **UI expects nothing for failed**: "decoy unavailable" never shows |
| decoy.turn | P3 `decoy/app.py:274 (decoy), 298 (scammer)` via POST /events | each decoy reply / scammer turn after handoff | yes | `:506` (feed, header, latency) | needs the real P3 decoy running (`P3_DECOY_URL`); stand-in/echo decoy emits none |
| decoy.fake_value | P3 `decoy/core.py:121` (hooked through `app.py ev`) | decoy gives a code-made fake number | yes | `:516` (tags the decoy line) | real P3 only |
| guardrail.tripped | P3 `decoy/core.py:113` | model output hit a rule | yes | `:522` (denied list) | real P3 only, fires rarely (do not expect it in the Card 2 call) |
| artifacts.extracted | P3 `decoy/app.py:478` (real); P1 `voip/router.py:594` **demo_stand_in** only if `SIM_MODE=1` and no `P3_DECOY_URL` | decoy extracts artifacts after the scammer speaks | yes (**emptied if EVENTS_REDACT=1**); intel acts only if the hub saw the call hand off (`main.py:202-205`) | `:528` (Artifacts panel, Input stage, payoff + map) | live needs real P3; SIM stand-in must show as SIMULATED |
| intel.plan / agent / proposals | P4 `intel/agent.py:169,213,226` | background thread after artifacts.extracted (and ~INTEL_EXTRACT_GRACE s after a decoy call ends with none) | yes | `:557/570/582` (pipeline strip) | trace only |
| intel.lookup | P4 `intel/lookups.py:108` | one per artifact lookup | yes | `:591` (Lookups panel) | needs artifacts |
| intel.action | P4 `intel/gate.py:194,211` | gate outcome per proposal: auto / queued / denied | yes | `:608` (actions, "He got $0", payoff) | needs artifacts |
| hold_transfer, flag_payee_bankwide | are `intel.action` `kind`s, proposed by code `intel/agent.py:115-131` | only if a **Nessie pending transfer matches the payout destination the decoy captured** (`bank_proposals`: no match = nothing) | yes (as intel.action) | `:264-274`, `:847` (payoff "stopped $X", Approve for flag_payee) | **only fires if the scammer gives a destination that matches the seeded pending transfer**; otherwise payoff shows no bank action (not a bug: say so) |
| injection.denied | P4 `intel/gate.py:181` | an artifact tried to poison/steer (`instruction_to_ai` etc.) | yes | `:660` (denied list) | only if the scammer says something steering |
| campaign.updated | P4 `intel/campaigns.py:147` (from `agent.py:181`) | every intel run | yes | `:681` (immunity/campaign) | needs artifacts |
| blocklist.updated | P4 `intel/gate.py:159,167,208`; P1 stub `server/main.py:239` only when intel is not mounted | `block_caller_for_customer` (scope her) after the run; campaign scope when confirmed; network on analyst Approve | yes | `:650` | needs artifacts or a decoy-ended call |
| voice.enrolled / deleted | `server/voice.py:90,102` (call id `c_onboard`) | customer voice onboarding only | yes | `:707-708` (attest) | not in the call itself |
| GET /intel/chain | `intel/api.py:105` (mounted `server/main.py:199-212`; open to GET without a token, `_intel_guard`) | polled by `pollChain` `app.js:1233-1250` | n/a (HTTP) | money-trail map; see section 2 for the snapshot fallback | on fetch error shows the saved snapshot even if live (eng1 section 2) |

**UI expects, nobody emits on the live path:** `call.answered by:"decoy"` and `ended_by:"system"` (not emitted anywhere), and the whole decoy/intel group (`decoy.*`, `guardrail.tripped`, `artifacts.extracted`, `intel.*`, `campaign.updated`, network `blocklist.updated`) unless the **real P3 decoy** runs (`P3_DECOY_URL` set, `SIM_MODE` unset). With only the Telnyx + P2 path (no handoff) the live screen can show only call.*, transcript.caller, risk.update, alert.fired, user.action.
**Emitted, no UI consumer:** `call.answered` fields `via` (talk/listen), `handoff.failed`, `intel.lookup` flat fields beyond what `:591` reads (harmless), `engine:"device"`.
**Checklist order for the Card 2 call** (watch `WS /events` or the page): call.incoming, call.routed(NORMAL), call.answered, transcript.caller (text visible?), risk.update, alert.fired (+0.3-3 s after the scam words; P2 `call_report --last 1`), user.action (Fire Back), handoff.started, decoy.turn x N, decoy.fake_value, artifacts.extracted, intel.plan, intel.lookup, intel.agent, intel.proposals, intel.action (+hold_transfer only on a destination match), campaign.updated, blocklist.updated(her), call.ended.
