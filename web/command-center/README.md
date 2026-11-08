# T-Mobile command center (P4b)

The judge-facing screen. One page, no build step, no dependencies.

## Run it

**Demo (live):** the P1 hub serves this folder (`server/main.py`), so open `http://<hub-host>:<port>/command-center/`. It connects to `WS /events` on the same host automatically, and Approve posts to the same origin (no CORS).

**Anywhere else:** open the page with the server's address:

```
http://localhost:5180/web/command-center/?server=http://192.168.1.20:8000
```

**No server yet (rehearsal):** from the repo root run `python -m http.server 5180` and open `http://localhost:5180/web/command-center/`. It looks for a server for ~2 s, then replays `mock/events.json` (or `fixture.js` until P1 pushes `mock/`). Double-clicking `index.html` also works and replays `fixture.js`.

## URL params (no settings screen)

| Param | Meaning |
|---|---|
| `server=http://host:port` | P1 base URL (WS `/events` and POST `/intel/actions/{id}/approve`) |
| `src=live\|mock\|fixture` | Force a source. Default: live if reachable, else replay |
| `speed=2` | Replay speed |
| `gap=6` | Replay: squeeze silences longer than this many seconds |
| `voice=clone|synthetic` |
| `brand=capitalone` | Capital One co-brand for the Nessie track: "Backfire × Capital One" lockup, "Fraud desk" title, Capital One navy instead of T-Mobile magenta. Leave it off for T-Mobile and NVIDIA judges |\|synthetic` | Decoy-voice wording if `voice.enrolled` happened before the page opened |

## Views and keys

Two views. The screen follows the call by itself: it shows **Live call** until the decoy has the scammer's payment details, then moves to **Money trail**.

| View | Key | Shows |
|---|---|---|
| **Live call** | 1 | The banner and progress steps, the caller-only transcript and decoy turns, and the risk gauge |
| **Money trail** | 2 | The ending. Left: where his money goes (victims → mule account → cash-out, from P4a's `GET /intel/chain`, Capital One Nessie sandbox, mock data), with the customer's line cut once the transfer is stopped. Right: the payoff checklist, ticked as it happens: payout account captured → customer's pending Zelle stopped → that account took $X from N people → **Approve · flag this account** (the one click) → his callback rejected. After the click the banner reads "Scammer get scammed. He got $0." |

Pressing a key holds that view; **Esc** (or "back to live") follows the call again.

Live: **Clear for next judge** (footer button, or C) wipes this screen between judges; the live connection stays on. It does not reset the hub.
Replay: **Space** pause/play · **R** restart · click the bar to jump.
Open a view directly: `.../command-center/?view=money`. After pulling an update, reload once with Ctrl+F5.
Look: light by default; `?look=dark` brings back the original magenta on dark.

## Test live mode without P1

```
python web/command-center/dev/fake_p1.py              # WS on :8765, plays a short built-in call
```
Open `...?server=http://localhost:8765`. Push P4a's real lookups onto the screen:
```
BACKFIRE_EVENTS_URL=http://localhost:8765/publish python -m intel.lookups domain example.com
```

## Files
- `index.html`, `styles.css`, `app.js`: the page
- `fixture.js`: the 90-second demo as contract events (synthetic), used until `mock/events.json` exists
- `dev/fake_p1.py`: test stand-in for P1's server
- `DECISIONS.md`: why things are the way they are, and the event shapes we read
