# HackTX — HackTX 2026 (1 projects)

### Once Upon a Focus
*HackTX HackTX 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [Best Novice Hack] The First Chapter [1st]

**What it is:** A Chrome extension that overlays a fairytale pet on every page during study sessions; it uses Gemini to see the screen, roast drift, lock pages until a trial is passed, and offers shared study rooms and break-time games.
**Problem / user:** Students who drift to distracting tabs, find blockers easy to bypass, and feel isolated when studying alone.

**Features**
- Eight fairytale pet characters with moods — SVG characters with seven poses; a mood machine escalates from happy to suspicious, annoyed, furious, then lockdown, with three strictness levels. *[shown_working]*
- Gemini screen checks and roasts — Downscaled screenshot to Gemini Flash returns JSON focus verdict and a roast hook referencing the real page. *[shown_working]*
- Lockdown overlay with trials — Page locks until riddle, topic quiz, backwards oath or friend challenge is passed; holding Esc 5 seconds escapes. *[shown_working]*
- Ask the pet with screen view — Tutor Q&A optionally attaches a screenshot to explain diagrams or errors. *[shown_working]*
- Study Table and Group Study Room — Friend codes, presence, nudges, challenges via Firebase; shared chat with Gemini Study Spirit that makes flashcards and quizzes. *[shown_working]*
- Break Tavern games — Spellbound word race, Tic-Tac-Toe, Connect Four versus friends or matched strangers or bot, with AI icebreakers and add-friend. *[shown_working]*
- Cinderella focus clock and demo mode — Pomodoro, 52/17 or custom timers synced across tabs by Chrome alarms; demo mode compresses time to seconds. *[shown_working]*
- Offline fallbacks — Model ladder with quota resting, then curated storybook lines; local mode with demo friends if Firebase absent. *[shown_working]*

**Flow:** Install extension and pick a character → Name the pet and enter study topic → Begin session; timer ring and Study Table appear → Drift to a distracting site and watch mood escalate with roasts → Solve a lockdown trial to unlock → Break clock opens Tavern to play a game → Join Group Study Room for shared flashcards

**Prompt:** not public / not found
**Fit (explicit):** README explicitly lists Gemini as the pet's eyes and social brain and a playful roasting pet for the entertainment track; the novice prize text was not retrieved. Theme is fairytale (#OnceUponAHack).  *(targeted: Best Novice Hack (The First Chapter), Best Use of Gemini API, Jester's Court Most Entertaining)*
**Sponsor tools:** Google Gemini API (Screen-aware focus detection, roasts, tutor, quizzes, study-room chat, icebreakers, core); Firebase (anonymous auth, Firestore) (Friends, presence, rooms, matchmaking and live games, supporting)
**AI:** Gemini Flash multimodal screenshots yield structured JSON verdicts; a ladder of Flash models with retry and quota handling; text generation for quizzes, riddles, icebreakers and shared study chat.
**Architecture:** WXT/React MV3 extension: background service worker (timers, mood engine, screenshots, AI calls), Shadow DOM content widget and lockdown, offscreen page for Firebase via a storage bridge; Firestore transactions for games.
**Novelty:** Treats focus enforcement as a character-driven game with screen-aware roasts and escalating lockdown, plus multiplayer break games, all inside a browser extension.
**Scope:** medium · working: About 8.9k LOC extension with detailed setup, demo mode and test hooks; no tests or live link. · polish: Eight hand-built SVG characters with seven poses, README with demo script and architecture, Devpost write-up.
**Claims:** Layered fallbacks keep AI and backend features working during outages | Eight characters each with seven poses
**Gaps:** HackTX prize text not retrievable; no video or live demo link
Sources: https://devpost.com/software/once-upon-a-focus, https://github.com/phoebe-yw/HackTX-26

---

