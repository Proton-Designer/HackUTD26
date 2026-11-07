# Technica — Technica 2026 (2 projects)

### Atlantis - The Long Night
*Technica Technica 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [Capital One] The Best Use of Nessie

**What it is:** A browser pixel-art game set in a sinking underwater city where a player lives one year in four seasons, earning, spending, investing and borrowing. Every in-game money move is posted to Capital One Nessie, and a Modern Mirror button explains the real-world concept.
**Problem / user:** People intimidated by personal finance, including those facing real barriers like no credit history or family wealth, who learn better through play than through dry finance games.

**Features**
- Four starting classes tied to real barriers — Newcomer (no credit), First of Their Line (debt), Caretaker, Tidewalker (variable pay) change starting conditions, not rules *[shown_working]*
- Nessie-backed money layer — Each class is a Nessie customer; wages are deposits, spending purchases, loans loan records, transfers between accounts; queued, POSTed, confirmed by GET *[shown_working]*
- Seasonal turns with shocks and events — Six actions per season (work, trade, invest, borrow, save, repay), 14 market shocks, event cards with choices *[shown_working]*
- Modern Mirror — Button in each building maps game items to real concepts such as credit card, ROSCA, payday lender, Ponzi scheme *[shown_working]*
- Season report card — Engine computes grades and breakdown; Gemini writes only three feedback bullets, validated against engine numbers *[claimed]*
- Scrolls and four endings — 13 achievements and endings explained in real-world terms *[claimed]*
- Balance simulator — Bots play thousands of seeded years per class to tune numbers *[claimed]*
- In-game Ledger — Lists every Nessie record with status and checks balances against Nessie *[claimed]*

**Flow:** Pick one of four classes → Start Spring with checking, savings and credit card → Spend six tides per season on actions → Face a market shock and event cards → Read the season report card → Open Modern Mirror in any building → Reach one of four endings with a real-world explanation

**Prompt:** not public / not found
**Fit (explicit):** Treats Nessie as the game's whole money layer, mapping deposits, purchases, loans and transfers to game events with a sync queue and confirmation, and documents Nessie quirks it hit.  *(targeted: Capital One The Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (Customers, checking/savings/credit accounts, deposits, purchases, loans and transfers for every in-game money effect, core)
**AI:** Gemini writes three short feedback bullets per season; outputs are auto-checked for filler, length and any number the engine did not supply. Grades and numbers come from a deterministic engine.
**Architecture:** React/TypeScript/Vite with Phaser 3 city on Vercel; FastAPI backend on Render with SQLite for runs and a Nessie queue; deterministic seeded Python engine and config file.
**Novelty:** A full game where every coin is a real Nessie record; deterministic engine with LLM limited to validated commentary; bot-based balance simulator.
**Scope:** large · working: Live Vercel demo, about 20k estimated LOC, pytest tests, full year loop with endings. · polish: Hand-built pixel-art city, guided tour, report cards; some features disabled pending balance.
**Claims:** Every coin movement is posted to Nessie and confirmed | Balance simulator runs thousands of seeded years per class | 14 market shocks, 13 scrolls, four endings
**Gaps:** README text empty in evidence; no video; no Technica Nessie prize text
Sources: https://devpost.com/software/atlantis-the-long-night, evidence/sponsor-technica-technica-2026-atlantis-the-long-night.json

---

### Treasure Dive
*Technica Technica 2026 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner [Capital One] The Best Use of Nessie

**What it is:** An Expo mobile/web app that reads a user's Nessie purchase history, matches merchants to open class-action settlements found by a Gemini scout agent, and shows possible claims in a pixel-art treasure chest interface.
**Problem / user:** Consumers who may be owed settlement money but never find or claim it; the page cites that most people never claim money they are owed.

**Features**
- Nessie purchase scan — Reads accounts and purchases from Nessie, normalizes bank descriptions to store names and checks them against open settlements (demo: 26 stores, 44 settlements) *[shown_working]*
- Treasure tab — Lists matches with deadline countdown, match strength and verified badge *[claimed]*
- Gemini scout agent — Searches with Google grounding, converts to JSON, then code verifies each claim site loads and names company and deadline *[claimed]*
- Receipt scanning — Gemini vision reads store, date and items from a photo to check against settlements *[claimed]*
- Claims map — Map of purchases with tags for state-limited settlements and a scout Q&A *[claimed]*
- Daily dive — node-cron job finds new settlements and matches them to history *[claimed]*
- I got paid — Records a real Nessie deposit when a claim is marked paid *[claimed]*
- Accessibility and safeguards — English/Spanish, read-aloud, large text, may-qualify wording, no filing on user behalf *[claimed]*

**Flow:** Connect a Capital One (Nessie) account read-only → Watch the scan match bank lines to settlements → Chest opens on an estimated amount → Browse the Treasure tab matches → Add receipts or explore the claims map → Mark a settlement as paid to log a Nessie deposit

**Prompt:** not public / not found
**Fit (implied):** Uses Nessie sandbox customers, accounts, merchants and purchases as the matching input and writes a deposit back when a claim is paid.  *(targeted: Capital One The Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (Reading customers, accounts, merchants and purchases; writing a deposit when a settlement claim is marked paid, core)
**AI:** Gemini with Google Search grounding discovers settlements, a second call structures them, URL context reads bot-blocked sites, and vision reads receipts; code verifies sites and quotes and enforces cautious wording.
**Architecture:** Expo/React Native client with Reanimated and maps; Node/Express/TypeScript server on SQLite with node-cron, zod validation, Gemini SDK and Nessie client; mock mode for offline demo.
**Novelty:** Joins bank purchase data with an AI-researched, code-verified list of live settlements; guardrails keep the AI from overstating money.
**Scope:** large · working: Page says it runs end to end on real Nessie and Gemini; 145 automated tests stated; no live demo link. · polish: Accessibility options, bilingual UI, pixel-art design tokens; repo link later removed.
**Claims:** 145 automated tests | Demo scan checks 26 stores against 44 open settlements | Runs end to end on real Nessie accounts and deposits
**Gaps:** repo clone failed and link reportedly removed; no video or live demo; no Nessie prize text
Sources: https://devpost.com/software/treasure-dive

---

