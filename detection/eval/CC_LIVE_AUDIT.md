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

## 3. During a real call
(pending: record which events arrived and which panels updated, including whether the tunnel viewer gets `transcript.caller` text unredacted: `EVENTS_REDACT` must be off for the command center on the tunnel.)
