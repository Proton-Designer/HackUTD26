# HackNotts — HackNotts '26 (3 projects)

### Holy XP
*HackNotts HackNotts '26 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** First Time Hacker

**What it is:** A Windows XP/98-styled fake desktop (Y2K OS) in which you run a hedge fund through the dot-com crash using a Bloomberg-like terminal, a simulated stock market and email/news written by a local LLM, with browser and minigame apps on the side.
**Problem / user:** No problem statement; a humorous game for hackathon judges and players, built hand-coded as a deliberate choice.

**Features**
- Market Terminal — Simulated exchange with Gaussian-driven prices, ticker and line graphs; trade across weeks toward a $7.5M target *[shown_working]*
- Game engine rules — Single TypeScript engine holds cash, positions, events, LP confidence and a random crash in weeks 11-14 *[shown_working]*
- LLM-written news and emails — Local OpenAI-compatible model on port 8889 produces JSON news; deterministic fallback copy if offline *[shown_working]*
- Tips vs lies — Emails give insider tips, some false, which the player must judge *[claimed]*
- XP/98 desktop apps — Outlook-style email, browser with internal pages (Nottingham Financial, eBay, YouTube-style), minigames *[shown_working]*
- Session persistence — Game state saved in versioned local storage with restart option *[shown_working]*

**Flow:** Boot the Y2K desktop → Open Market Terminal → Read emails and news from the local LLM → Buy and sell assets and advance market weeks → Survive overhead and the crash to reach the target

**Prompt:** First Time Hacker prize: for teams with more than half first-timers. The hackathon also listed a 2000s-themed prize and a Machine Learning prize, names only.
**Fit (none):** Page does not mention first-timer status; project leans on the Y2K theme and a local LLM, built entirely by hand per the team.  *(targeted: First Time Hacker)*
**AI:** A locally hosted model behind an OpenAI-compatible endpoint writes headlines, summaries and emails as validated JSON; failures fall back to canned text, and AI prose cannot change game state.
**Architecture:** Vite React/TypeScript front end; pure gameEngine as source of truth with React state adapter; services call local LLM endpoint; earlier Python/tkinter simulator kept in archive; cloudflared used for connectivity during the event.
**Novelty:** Retro OS pastiche around a stock simulator with a separation between game rules and LLM flavor text; team states no AI wrote the code.
**Scope:** medium · working: Repo about 6.6k lines with detailed architecture README and run instructions; game described as buggy and playable. · polish: XP-style GUI and multiple apps; no tests, video or live demo.
**Claims:** Hand-coded without AI coding tools | Difficulty balanced through playtests and math models
**Gaps:** Devpost describes a Python-to-React port while README says production game is fully frontend and OS is Windows 98 styled; README written later and may describe post-event changes
Sources: https://devpost.com/software/y2k_os, evidence/hacknotts-hacknotts-26-holy-xp.json (README), prompts_cache/hacknotts-26.md

---

### Kitkat
*HackNotts HackNotts '26 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** First Place [1st]; Whimsy Prize

**What it is:** A flip-phone style handheld built on an ESP32 with a custom C++ operating system, a Snake game, a drawing app and a music player, housed in a 3D-printed Hello Kitty themed flip case.
**Problem / user:** No problem stated; a playful take on "cyberdecks" by walking back to the flip phone form factor.

**Features**
- Custom C++ OS on ESP32 — Own operating system developed in Arduino IDE with a toolchain meant to make app development easy. *[claimed]*
- Snake game — Classic Snake reimplemented as a built-in app. *[claimed]*
- Illustration studio — Drawing app on the touchscreen for sketching. *[claimed]*
- Music library — Plays music from SD card with wireless audio output (source of tracks unspecified). *[claimed]*
- Flip case — Hinged case designed in Fusion 360 and Blender, printed in PLA; "final product" photo on page. *[shown_working]*
- Hello Kitty theme — Cat-themed shell and retro 1999-2002 style advertisement images in the gallery. *[shown_working]*
- Long battery claim — Page says battery can last months; no measurements. *[claimed]*

**Flow:** Open the flip case → Pick an app on the touchscreen → Play Snake, draw, or play music → Close the case to pocket it

**Prompt:** Open brief; Whimsy Prize listed without description; judged on Creativity, Completeness, Technical Achievement.
**Fit (none):** A deliberately whimsical hardware toy with a cat-themed case and retro flip-phone styling; page does not name a prize.  *(targeted: First Place, Whimsy Prize)*
**AI:** none
**Architecture:** ESP32 microcontroller with touchscreen, graphics and SD card on its two buses, running a C++ OS; printed flip case. Repo has an os/ folder and a Python playsound requirement.
**Novelty:** Full custom OS plus physical enclosure built in 25 hours; had to repartition flash because the code outgrew it.
**Scope:** small · working: Devpost shows a photo of the finished device; repo has about 1,650 lines across 19 code files; no video. · polish: Custom printed case with reprints; repo README is an unedited template titled "Flipphone Alarm Clock".
**Claims:** Paper to hands in 25 hours | Battery can last months | Nearly unlimited music library
**Gaps:** README is a template mentioning an alarm clock not on Devpost; Canva "Try it out" link not read; No demo video; Wireless audio method unspecified
Sources: https://devpost.com/software/kitkat, evidence/hacknotts-hacknotts-26-kitkat.json (README is placeholder), https://hacknotts-26.devpost.com/

---

### Logicverse
*HackNotts HackNotts '26 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Place [2nd]

**What it is:** A mostly deterministic simulation of hackathon attendees: scraped public data forms a ~90,000-fact logic knowledge base queried with SPARQL to script conversations between on-screen avatars, shown on a TV that spawns a virtual alter-ego of whoever sits in front of it.
**Problem / user:** No problem stated; aims to simulate humanity in the online era for hackathon attendees and viewers.

**Features**
- Knowledge base of ~90,000 facts — Relational facts in a logic language scraped from Discord, GitHub, Devpost (and LinkedIn per story), including follows and collaborates-with links. *[claimed]*
- Query-driven dialogue — Conversation lines come from SPARQL-style queries, e.g. two people sharing a recent activity trigger a "so have I" line. *[shown_working]*
- Small-talk fallback — When people have little in common, the system picks smalltalk or self-directed topics. *[claimed]*
- Dialogue DSL and Rust librettist — A custom scripting language holds dialogue and stage directions; a Rust module deterministically picks dialogues. *[shown_working]*
- Stage renderer — Bevy-based renderer performs stage directions line by line. *[shown_working]*
- Presence detection — Frontend ML recognises who stands in front of the TV and adds their alter-ego as a character. *[claimed]*
- Cross-platform identity links — Identity facts connect one person across accounts. *[claimed]*

**Flow:** Person sits in front of the TV → System recognises them → Avatar of that person appears on screen → Librettist selects a dialogue from facts → Renderer acts it out with other avatars

**Prompt:** Open brief; judged on Creativity, Completeness, Technical Achievement. Second Place has no separate description.
**Fit (none):** Creative installation using logic programming and scraped community data; no prize named on page.  *(targeted: Second Place)*
**AI:** Mostly symbolic: logic-programming fact base and SPARQL queries with hand-written dialogue DSL; only a small frontend ML model associates faces with people.
**Architecture:** Python scrapers feed a Turtle/RDF-style fact base; Rust engine runs queries, selects dialogues via the librettist, and a Bevy renderer plays them on a TV.
**Novelty:** Uses attendees real public data and logic programming to drive theatre-like scripted scenes instead of LLM chat; admits LinkedIn bans.
**Scope:** medium · working: Eight screenshots and example script; no repo, video or accuracy numbers. · polish: Custom DSL, renderer and on-site TV installation concept.
**Claims:** About 90,000 relational facts | Dozens of queries over tens of thousands of facts | Banned four times from LinkedIn while scraping
**Gaps:** No repo or video linked; Camera hardware not specified; Privacy handling of scraped personal data not discussed on page
Sources: https://devpost.com/software/logicverse, https://hacknotts-26.devpost.com/

---

