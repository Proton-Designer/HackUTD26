# Innovation Hacks — Innovation Hacks 2.0 (2 projects)

### Dollar Dash
*Innovation Hacks Innovation Hacks 2.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner State Farm: Financial Wellness Track

**What it is:** A real-time multiplayer classroom stock-trading game: a host projects a room code, students join on phones and trade four fictional stocks as scripted news headlines move prices, ending in a leaderboard with grades and badges.
**Problem / user:** Students, especially in underserved classrooms, who get little hands-on financial education; teachers can run it with just phones.

**Features**
- Room creation with QR join — Host shows a code and QR; players join at /play without installs or accounts. *[shown_working]*
- Simulated market — Prices tick every 250 ms from drift, volatility and active news over four stocks of differing risk. *[shown_working]*
- News-driven events — 25 curated headlines fire every few seconds moving specific stocks. *[shown_working]*
- Live leaderboard, grades, badges, titles — Rankings update each tick; 8 badges and titles from Intern to Partner by return. *[shown_working]*
- Day system and custom duration — 30-second trading days with transition screens; game length 1-5 minutes or custom up to 30. *[shown_working]*
- Story mode — Solo interactive tutorial teaching trading basics. *[shown_working]*
- ElevenLabs voice — Listed as built-with and a dependency; role not described. *[unclear]*

**Flow:** Host creates a room and projects the code → Players join by phone → Host starts the game → Headlines move prices; players buy and sell → Time runs out → Leaderboard shows grades, badges and titles

**Prompt:** State Farm Financial Wellness Track at Innovation Hacks 2.0: address a financial-wellness problem statement given in an external document not shown on the page.
**Fit (implied):** Teaches investing, diversification and risk to students through a live classroom game.  *(targeted: State Farm Financial Wellness Track, MLH Best Use of ElevenLabs)*
**AI:** none
**Architecture:** React/Vite/Tailwind client with custom canvas charts; Node/Express server with Socket.io running the market tick loop and rooms; hosted on Render.
**Novelty:** Projector-plus-phones classroom format with scripted news events and canvas charts, closer to a polished game than a typical finance tool.
**Scope:** medium · working: Live Render demo and detailed README; about 6.8k LOC. · polish: Press Start 2P pixel styling, confetti, badges, named stocks and instructions page; no video.
**Claims:** Zero friction: no downloads or accounts, only a phone
**Gaps:** State Farm problem statement doc not found; no AI content
Sources: https://devpost.com/software/dollar-dash, https://github.com/WillBlair/dollardash

---

### Redreemer
*Innovation Hacks Innovation Hacks 2.0 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner State Farm: Financial Wellness Track

**What it is:** A free SMS service where homeless or reentry users text one number and a Gemini-based assistant gives local resources, guides them through an 8-step stability ladder, blocks predatory lenders, and sends voice milestone clips; caseworkers get a dashboard.
**Problem / user:** People who are homeless or recently released from prison without a smartphone, email or bank account; cites 582,000 homeless Americans and 600,000 annual releases.

**Features**
- SMS assistant with step-aware local resources — Gemini 2.5 Flash replies in the user's language with Phoenix addresses and phones matched to their current step. *[shown_working]*
- Predatory lender interception — Payday and title loan keywords are caught before the model and trigger a bilingual warning with safer options. *[claimed]*
- Guided flows — Bank account, ID recovery, benefits eligibility, credit explainer, expungement checker and money-personality quiz run as SMS conversations. *[claimed]*
- Fair-chance employer finder — Lists six real Phoenix employers from step 4 onward. *[claimed]*
- Crisis detection and 20-layer pipeline — Each text screened in order, crisis first, pointing to 988 and homeless hotlines. *[claimed]*
- Scheduled check-ins and voice clips — Weekly progress and wins SMS via cron; ElevenLabs voice sent as MMS on step advance. *[claimed]*
- Caseworker dashboard — Auth0-protected client management with step notes, silent-client alerts and risk scoring. *[shown_working]*

**Flow:** User texts the number → Message passes the detection pipeline → Gemini replies with local resources for current step → User advances through 8 steps and gets voice milestone clips → Caseworker monitors progress on dashboard

**Prompt:** State Farm Financial Wellness Track at Innovation Hacks 2.0: address a financial-wellness problem statement given in an external document not shown on the page.
**Fit (implied):** Delivers financial inclusion and stability guidance to people lacking banks or smartphones, framed as exclusion being a design problem.  *(targeted: State Farm Financial Wellness Track)*
**AI:** Gemini 2.5 Flash answers texts with step context and a persona tuned by a money-personality quiz; keyword and rule layers run before the model; ElevenLabs generates milestone voice clips.
**Architecture:** Twilio SMS webhook to Node/Express server with layered detectors, Gemini, Supabase Postgres and cron jobs; React caseworker dashboard behind Auth0; ElevenLabs audio via MMS; Vercel deployment.
**Novelty:** Targets users with no smartphone via SMS, with safety-first message ordering and a caseworker side; resource data limited to Phoenix.
**Scope:** large · working: Demo site, video and slides; about 20.6k LOC with tests across server, client and UI folders. · polish: Extensive README, bilingual flows, separate UI and client apps, i18n.
**Claims:** First SMS platform to intercept predatory lenders in real time | 23 scam attempts blocked so far
**Gaps:** State Farm problem statement doc not found; SMS behavior not tested
Sources: https://devpost.com/software/redreemer, https://github.com/sumedha092/redreemer

---

