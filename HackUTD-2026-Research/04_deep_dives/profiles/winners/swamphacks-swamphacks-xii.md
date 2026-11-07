# SwampHacks — SwampHacks - XII (1 projects)

### Spotle.ink
*SwampHacks SwampHacks - XII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First Timers

**What it is:** A real-time multiplayer camera scavenger hunt: 2-4 players share peer-to-peer video, an AI names an object to find, and Gemini judges the photo submitted when someone hits FOUND IT, including rejecting photos of screens.
**Problem / user:** Friends or hackathon groups wanting a physically active party game instead of screen-bound tools; no formal problem stated.

**Features**
- Room lobby — Players create or join a room by code (Devpost: four letters; README: 6-digit PIN); host starts game and picks theme *[shown_working]*
- P2P video and voice grid — PeerJS WebRTC mesh with TURN config, camera switch via replaceTrack *[shown_working]*
- AI-chosen targets — Round item drawn from a 151-item database filtered by theme (UF/SwampHacks, hackathon, general, outdoors) *[shown_working]*
- Gemini referee — JPEG frame grabbed from the video element is judged by gemini-2.5-flash with JSON output; variants accepted, other categories rejected *[shown_working]*
- Anti-screen-cheat — Prompt heuristics for moire, bezels and OS UI flag photographed screens, deny points and add a roast *[shown_working]*
- Scoring and cooldown — Placement points in README (Devpost: base plus speed bonus); rejected claims incur a short cooldown *[shown_working]*
- Extra game modes — README lists Assassin (hunt a player by selfie) and Hide and Seek modes *[claimed]*
- Retro 8-bit UI — Pixel art, mascot Ink, dynamic camera grid, win confetti *[shown_working]*

**Flow:** Open spotle.ink, create or join a room → Host picks theme and starts → Round target appears; timer runs while live feeds show opponents → Player presses FOUND IT with object in view → Server sends frame to Gemini referee → Points, commentary and scoreboard shown; next round or winner screen

**Prompt:** Best First Timers: teams where at least half the members are attending their first hackathon; one winner (keyboard/mouse bundle). General criteria include technical understanding, creativity, functionality, design and purpose.
**Fit (none):** Page does not mention first-timer status; the winning entry is a polished, live, multi-component game with its own deployment.  *(targeted: Best First Timers)*
**Sponsor tools:** Google Gemini API (Multimodal referee judging submitted frames and screen-spoof detection, core)
**AI:** gemini-2.5-flash receives a captured frame plus the target and returns structured JSON verdict with a screen-cheat flag and commentary; system instructions encode spoof-detection heuristics.
**Architecture:** React/TypeScript/Vite client; one Node/Express/Socket.io server (authoritative game engine, PeerJS broker, TURN config endpoint) calls Gemini; shared TypeScript contract; deployed on Render.
**Novelty:** AI referee with explicit anti-cheat for photographed screens, a self-hosted PeerJS broker and a TURN diagnostics page are unusual for a first-timer hack.
**Scope:** medium · working: Live site spotle.ink, about 9.7k lines excluding dependencies, unit tests, deployment blueprint. · polish: Custom pixel art, mascot, multiple modes, detailed ops README, render.yaml and /rtc-check tooling.
**Claims:** Frame capture under 15 ms | Payloads previously over 10 MB cut by resizing to 640x480 JPEG | Built in a 36-hour sprint
**Gaps:** Devpost and README disagree on room code (4 letters vs 6-digit), round length (60s vs 90s) and scoring; feature list follows both, README newer; no demo video
Sources: https://devpost.com/software/spotle-ink, evidence/swamphacks-swamphacks-xii-spotle-ink.json (README), https://swamphacks-xii.devpost.com/

---

