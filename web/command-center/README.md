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
| `voice=clone\|synthetic` | Decoy-voice wording if `voice.enrolled` happened before the page opened |

## Views and keys

| View | Key | For |
|---|---|---|
| **Story** (default) | 1 | The table. One chapter of the call at a time, big: during the call → what the decoy got → what we did. Follows the call; click a rail step to hold a chapter, Esc to follow again |
| **Agent** | 2 | NVIDIA judges: the agent pipeline (artifacts → lookups → Nemotron → policy gate) and the full trace, with the evidence and denials beside it |
| **Everything** | 3 | A technical judge who wants every panel at once |

Live: **Clear for next judge** (footer button, or C) wipes this screen between judges; the live connection stays on. It does not reset the hub.
Replay: **Space** pause/play · **R** restart · click the bar to jump.
Open a view directly: `.../command-center/#agent`. After pulling an update, reload once with Ctrl+F5.

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
