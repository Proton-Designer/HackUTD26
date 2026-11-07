# McHacks — McHacks 12 (3 projects)

### Debug Debacle
*McHacks McHacks 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place [3rd]; Gumloop - Best AI project that uses the Gumloop API

**What it is:** A web game where players join a lobby and race to find and fix the same bug in code within five minutes in a Monaco-based in-browser IDE, without seeing the test cases; scores go to a persistent leaderboard.
**Problem / user:** Developers lose hours to small bugs; the game turns debugging into a friendly competition for developers wanting practice.

**Features**
- Timed multiplayer bug hunt — Players in a lobby get the same buggy code and a 5-minute limit over Socket.IO *[shown_working]*
- Hidden test cases — Solutions are checked against tests the player cannot see *[claimed]*
- In-browser Monaco IDE — Customizable code editor like VS Code's editor *[shown_working]*
- AI-generated problems and tests — Gumloop flows generate buggy problems and test cases *[claimed]*
- Persistent leaderboard — Scores stored in Supabase and shown after each game *[shown_working]*
- Login — Auth0 listed in built-with tags *[unclear]*
- Multiple concurrent games — Socket.IO connections organized per game room *[claimed]*

**Flow:** Home page → Join lobby → Open editor and find the bug within 5 minutes → Congrats screen → Updated leaderboard

**Prompt:** Gumloop prize: Best AI project that uses the Gumloop API, with six winners at $200 gift cards each. McHacks 12 itself was non-themed with overall top-3 prizes.
**Fit (explicit):** Gumloop generates the buggy problems and test cases that power each game; the README claims a Gumloop award.  *(targeted: Gumloop - Best AI project that uses the Gumloop API, 3rd Place)*
**Sponsor tools:** Gumloop (generating coding problems with bugs and test cases, core)
**AI:** Gumloop-hosted workflow generates problems and tests; underlying model not named; no AI in play loop.
**Architecture:** React/TypeScript/Tailwind/shadcn frontend with Monaco; Flask plus Flask-SocketIO backend; Supabase leaderboard; Auth0; Tempo Labs used for initial design.
**Novelty:** Turns debugging into a timed head-to-head with hidden tests, with AI as the content source rather than the player's helper.
**Scope:** small · working: Repo of 135 files, about 8.4k LOC with a demo video and gameplay screenshots; no live link. · polish: README duplicates Devpost; screens for lobby, editor, results; no tests.
**Claims:** Won 3rd place overall | README says 2nd place in Gumloop award, Devpost says it won the Gumloop prize
**Gaps:** no setup instructions; video not watched; Gumloop placement stated two ways
Sources: https://devpost.com/software/debug-debacle, evidence/mchacks-mchacks-12-debug-debacle.json, https://mchacks-12.devpost.com/

---

### Planorama
*McHacks McHacks 12 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 2nd Place [2nd]

**What it is:** A solo-built web project planner that shows tasks and dependencies as a node graph in React Flow, with sketch boards for early ideas, OpenAI task generation and prioritization from a project description, and integrations such as GitHub, Discord and Slack.
**Problem / user:** Planning tools are either too complicated or not built for developers; aimed at developers, teams and non-technical managers who want a visual plan.

**Features**
- Graph-based planning — Tasks and dependencies drawn as nodes and edges with several node types *[shown_working]*
- Sketch boards — Board page for high-level ideas plus a manager page for boards *[shown_working]*
- AI task generation — OpenAI creates tasks from a project description *[claimed]*
- AI prioritization — Tasks are ranked by priority from the description *[claimed]*
- Integrations — GitHub, Discord (via discord.js), Slack and VS Code listed *[claimed]*
- Team collaboration and auth — Assign tasks, track progress, user accounts and login *[claimed]*
- Projects dashboard and landing page — Screens shown in screenshots *[shown_working]*

**Flow:** Sign in → Open projects dashboard → Create or open a sketchboard → Map tasks as nodes and edges → Use AI to generate and prioritize tasks

**Prompt:** McHacks 12 was non-themed; top-3 overall prizes were a PS5 with Nord subscriptions (1st), 3D printer (2nd) and gaming monitor (3rd).
**Fit (none):** No stated prize link; non-themed event.  *(targeted: 2nd Place)*
**AI:** OpenAI models generate and prioritize tasks from user-entered project descriptions.
**Architecture:** Next.js/TypeScript app with React Flow graph UI, Prisma over MongoDB (Firebase also listed), discord.js and other integrations, and OpenAI calls.
**Novelty:** Node-graph planning plus integrations aimed at developers, built by one person in a hackathon.
**Scope:** medium · working: Demo video and four screenshots (landing, dashboard, sketchboards, board); no repo or live link. · polish: Multiple screens, auth, loaders; claimed integrations unverified.
**Claims:** Creator says he would use it himself | No usage metrics
**Gaps:** no repository linked; Firebase role unexplained; integration depth unverified; video not watched
Sources: https://devpost.com/software/planorama-ft9hj4, https://mchacks-12.devpost.com/

---

### SeeForMe
*McHacks McHacks 12 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 1st Place [1st]

**What it is:** A Python assistive app that runs YOLO object detection on a camera feed, announces nearby objects by voice, accepts voice commands to turn vision on or off, and gives turn-by-turn directions to a spoken destination via Google Directions.
**Problem / user:** People with visual or mobility impairments find everyday travel and routines hard; the app aims to help them get from place to place safely.

**Features**
- Real-time object detection — YOLO identifies items such as bottles, chairs, stop signs and phones in the camera view *[claimed]*
- Spoken object feedback — Detected objects are announced through voice output *[claimed]*
- Voice commands — User can switch the vision system on and off and make requests by speech *[claimed]*
- Turn-by-turn navigation — Google Geocoding and Directions APIs turn a destination into spoken steps *[claimed]*
- Multilingual support and mobile app — Listed as next steps *[planned]*

**Flow:** Activate the vision system by voice → Hear nearby objects announced → Ask for directions to a destination → Hear turn-by-turn instructions

**Prompt:** McHacks 12 was non-themed; top-3 overall prizes were a PS5 with Nord subscriptions (1st), 3D printer (2nd) and gaming monitor (3rd).
**Fit (none):** No stated prize link; non-themed event, project is an accessibility tool combining detection, navigation and voice.  *(targeted: 1st Place)*
**AI:** Pretrained YOLO object detection for the camera feed; voice recognition and synthesis libraries not named.
**Architecture:** Python application combining YOLO inference on video, speech input and output, and Google Geocoding and Directions API calls for routes.
**Novelty:** Combines object announcement and navigation in one voice-driven tool; scope limited by the small set of detectable objects.
**Scope:** small · working: Demo video linked; repo could not be read; team admits object coverage was limited by time. · polish: Devpost is brief with no metrics or screenshots described.
**Claims:** Provides 'timely and accurate feedback' (no evidence given)
**Gaps:** evidence file shows clone_failed and GitHub repo returned error; voice libraries unknown; video not watched
Sources: https://devpost.com/software/seeforme, https://mchacks-12.devpost.com/

---

