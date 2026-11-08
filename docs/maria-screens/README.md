# Maria's app: every screen (iPhone 13, 390x844, Chromium emulation, current build)

Regenerate: `E2E_VENV=<venv with playwright> $E2E_VENV/bin/python web/customer/tests/make_screens.py` (static server + a mock hub inside Playwright: no hub, no Telnyx, no real calls, no secrets; fake WebSockets and a fake microphone drive the states).
Files: `index.html` markup, `style.css` look, `app.js` call screen + events, `ui.js` onboarding/Protection, `pair.js` pairing, `sim.js` caller/decoy audio (/listen), `talk.js` Maria's mic (/talk), `judge.html` scammer card.

| # | Screen | Triggered by | Edit |
|---|---|---|---|
| 01 | Pair this phone | hub answers 401 (no device token) | `index.html #pairView`, `pair.js`, `style.css #pairView` |
| 02 | Onboarding 1: Turn on Backfire | first launch after pairing | `index.html #step1`, `ui.js` (setup) |
| 03 | Onboarding 2: voice consent (I agree / Skip, use a synthetic voice) | Turn on, or Protection > Set up my voice | `index.html #step2`, `ui.js` |
| 04 | Onboarding 3: read-aloud, idle | I agree | `index.html #stepRec`, `ui.js` (PARAS, newParagraph) |
| 05 | Recording with level meter + timer | Start recording (Stop enabled after 3 s, auto-stop 60 s) | `ui.js` (recBtn, meter), `style.css .meter` |
| 06 | Review: Save my voice / Record again | Stop | `index.html #recReview`, `ui.js` |
| 07 | Saved: "Your voice is set up" banner, then Do Not Screen step | POST /voice/enroll returns a voice_id | `ui.js enroll()/toDns()`, `index.html #dnsNote` |
| 08 | Not saved: "Your voice wasn't saved; Backfire will use a synthetic voice" | /voice/enroll returns {voice_id:null,fallback:'synthetic'} | same as 07 |
| 09 | Do Not Screen list (add/remove numbers) | after voice step; Protection > Manage this list | `index.html #stepDns`, `ui.js` (dns*) |
| 10 | Onboarding done | Continue | `index.html #step3` |
| 11 | Idle: "Live Guard on" | normal state | `index.html #ended/#phone`, `app.js` |
| 12 | Incoming ring: Scam Likely, Decline/Answer | call.incoming + call.routed | `index.html #incoming`, `app.js ring()` |
| 13 | Active call, listening mode (caller audio, "Listening to the caller") | hub flag MARIA_LEG=listen (or ?listen=1) | `sim.js`, `index.html #decoyMsg` |
| 14 | Active call, talk mode, mic live (green dot) | MARIA_LEG=talk (or ?talk=1) | `talk.js`, `index.html #talkBox`, `style.css .talk/.mic/.dot` |
| 15 | Talk mode, muted | tap the mic button | `talk.js render()` |
| 16 | "Tap for sound" badge (audio blocked by the browser) | AudioContext suspended / autoplay blocked | `app.js unlockAudio`, `sim.js` |
| 17 | Alert: why chips + Continue / Scammer Get Scammed / Hang up | alert.fired (two beeps) | `index.html #alertBox`, `app.js`, `style.css .alert/.chips` |
| 18 | Handed off: "We've got it" + "Listening to Backfire's decoy" | Scammer Get Scammed / handoff.started | `app.js showHandoff`, `sim.js` |
| 19 | Restored: "You're back on the call" | handoff.restored | `app.js` |
| 20 | Call ended | call.ended / hang up | `index.html #ended`, `app.js endCall` |
| 21 | Protection tab: Live Guard, blocked numbers + Undo, calls handled, what we keep, voice profile (Delete my voice) | Protection tab | `index.html #protView`, `ui.js renderProtection` |
| 22 | Protection > Do Not Screen manage | "Manage this list" | `index.html #stepDns`, `ui.js` |
| 23 | judge.html: "You are the scammer" card | open /app/judge.html | `judge.html` |

Notes: the screenshots use a mock hub, so numbers and calls are synthetic. No pairing code or token appears in any image (the pair screen shows only the placeholder). The status-bar flame and wordmarks come from `assets/`.
