# StormHacks — StormHacks 2026 (28 projects)

### Apex FSD
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SSSS - Seb's Software Systems Python Track

**What it is:** An end-to-end driving AI for Forza Horizon 4: a PilotNet-style CNN looks at the game screen plus speed and physically turns a real Thrustmaster force-feedback wheel via a virtual controller, with instant human takeover and a loop that learns from the human corrections.
**Problem / user:** Sim-racing and ML/robotics hobbyists; tests whether a pixels-to-steering model can be built in a weekend and drive in a game, rather than stopping at a function call.

**Features**
- PilotNet-style CNN with speed fusion — 5 conv layers on a 66x200 road crop, speed fused late, outputs steering (plus throttle/brake in driving mode). *[shown_working]*
- Data recording and cleaning — Screen capture and Forza UDP telemetry on one clock; frame lag of 66 ms measured; crashes, rewinds, pauses auto-discarded. *[shown_working]*
- Physical wheel control — 100 Hz PD controller with friction compensation drives the TMX motor; vJoy virtual wheel and HidHide pass inputs to the game. *[shown_working]*
- Human takeover and safety — Grabbing wheel, tapping pedal or button disengages AI, logs cause; stale frames, telemetry or network also disengage. *[shown_working]*
- DAgger correction loop — Human corrections after AI mistakes become new training data for retraining. *[claimed]*
- Live HUD and dashboard — Browser dashboard with intended-path overlay, latency traces and tuning for gain, throttle ramp and corner limit. *[claimed]*
- Two-PC networked inference — Model runs on a GPU machine and replies over authenticated TCP to the game/wheel PC. *[shown_working]*
- Planned: voice control, real-road shadow mode — Voice aggressiveness, dash cam plus OBD-II, assist nudges, RL layer. *[planned]*

**Flow:** Record human laps in Forza → Auto-clean and train the model (Colab or desktop GPU) → Start inference server and game PC runtime → Arm the AI; wheel turns itself with HUD path → Grab wheel to take over; corrections feed retraining

**Prompt:** SSSS Python Track: "The best project using python!" with 1 winner and hardware prizes.
**Fit (implied):** The whole pipeline (PyTorch, OpenCV, DXcam, PySDL2, pytest) is Python; page lists the track win but does not discuss Python specifically.  *(targeted: SSSS - Seb's Software Systems Python Track)*
**Sponsor tools:** Tiger Data (Postgres/TimescaleDB) (Optional run analytics via forza-analytics package, supporting)
**AI:** Behavior cloning of a PilotNet CNN on about 3 hours of human laps, then DAgger; PyTorch; saliency visualisation; optional Gemini voice package listed in manifest.
**Architecture:** Game PC captures screen (DXcam) and Forza telemetry, runs 100 Hz wheel controller via vJoy/HidHide; GPU PC serves model over HMAC-authenticated TCP; recorder, trainer and dashboard tooling.
**Novelty:** Closes the loop into physical hardware: a neural net actually rotates a real wheel, with measured latency, takeover logging and DAgger, unusual for a weekend ML project.
**Scope:** large · working: Demo video, repo of about 19k LOC with tests and docs, measured error figures; generalization to unseen tracks limited. · polish: Detailed README with setup, simulated no-hardware mode, launch profiles and run reports.
**Claims:** Wheel tracking error cut from 134 to 9 degrees | 66 ms screen-to-telemetry lag measured | Held-out steering error beat zero and mean baselines | Poor generalization to unseen races (team admits)
**Gaps:** Demo video not viewable; Sponsor tool use (Tiger Data) appears only in README, not Devpost; Hardware demo outcome beyond self-reported numbers unverified
Sources: https://devpost.com/software/apex-fsd, https://github.com/iancdev/stormhacks (evidence README), https://stormhacks2026.devpost.com/

---

### Chess without Borders
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Huawei Custom Challenge #1 - Beyond Euclid

**What it is:** A two-player 3D browser chess game with linked flat 8x8 and hyperbolic boards. Players spend a turn to shift the board geometry, which opens new curved routes for pieces that follow rules adapted to the {4,5} hyperbolic tiling.
**Problem / user:** Chess players and curious learners; the aim is to make non-Euclidean geometry a strategic mechanic experienced through a game they already know.

**Features**
- Geometry shifts — Preview then commit a shift between flat and a 109-tile hyperbolic patch; shift spends a turn, with a two-move lock before the next. *[shown_working]*
- Curved-space move rules — Rooks, bishops, queens, knights, kings and pawns defined by edge routes on the hyperbolic graph; route tracing and explanations. *[shown_working]*
- Full chess rules — Check, checkmate, castling, en passant, promotion, repetition draws, plus standard mode without shifts. *[shown_working]*
- Online rooms and local play — Private room codes/links over WebSockets for two players, or both sides locally. *[shown_working]*
- 3D camera and views — Three.js orbit/pan/zoom, local recentring on selected piece via Lorentz boost, focused/helicopter/birds-eye views. *[shown_working]*
- Shared game engine — TypeScript rules engine runs in browser and server; tests included. *[shown_working]*
- Planned: bot, spherical geometry, themes — Chess bot, bonus regions, other geometries. *[planned]*

**Flow:** Create a private room or choose local play → Play flat chess moves → Preview a geometry shift and commit it → Pick a piece to see curved routes and confirm destination → Win by checkmate or resignation

**Prompt:** Huawei Challenge 1 "Beyond Euclid": build an interactive experience where Euclidean geometry no longer applies; game, visualization, tool or interface; ideas include hyperbolic and spherical spaces.
**Fit (explicit):** Uses hyperbolic tiling as a core game mechanic, not decoration; page says the geometry is a gameplay mechanic and names the challenge.  *(targeted: Huawei Custom Challenge #1 - Beyond Euclid)*
**Sponsor tools:** Huawei Beyond Euclid challenge brief (Theme: non-Euclidean interactive experience, core)
**AI:** none
**Architecture:** Vite/TypeScript client with Three.js rendering; Node 24 room server using ws; shared rules engine generating hyperbolic tiles by reflections in the hyperboloid model; chess.js for flat rules.
**Novelty:** Mathematically grounded hyperbolic movement rules and a mid-game geometry-shift mechanic, with a documented rules spec.
**Scope:** medium · working: Live demo site, YouTube video, about 4.4k LOC with tests and docs. · polish: Very detailed README of controls and rules, theme toggle, keyboard play, responsive layout.
**Claims:** Non-Euclidean geometry is a core mechanic, not a visual effect
**Gaps:** README describes later version-2 rules (shadow pieces, Curvature default); feature list follows README for rules, Devpost for framing; Huawei brief doc not read
Sources: https://devpost.com/software/chess-2-watsne, https://github.com/geoff-jiang/Chess2 (evidence README), https://stormhacks2026.devpost.com/

---

### Common Ground
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** SFU Satellite - ALEASAT - Earth Observation Track

**What it is:** A web app where residents design a neighbourhood park in 3D on real Vancouver lidar terrain, vote and comment on each other's designs, and planners see heatmaps, an AI theme summary and CSV/GeoJSON/DXF exports. Demo site is Jonathan Rogers Park.
**Problem / user:** Park planners and residents; consultation favours people who can attend meetings or fill surveys, so the app lets anyone shape and rate a design with measurable output.

**Features**
- 3D park editor on real terrain — Place benches, trees, playgrounds, ponds, paths, gardens and terraform on 1 m NRCan HRDEM elevation with city tree, garden and street data. *[shown_working]*
- Describe it — Text prompt such as "shady play area, loop path" makes Gemini draft a layout; a layout solver places by slope, routes paths with A*, scatters trees. *[shown_working]*
- Live budget and rules — Cost, canopy, hard surface, earthworks and path-slope accessibility update as you build. *[shown_working]*
- Voting and commenting — Up/down votes with reasons; item comments such as Move or Keep; walk the park at eye height. *[shown_working]*
- Planner insights — Heatmaps of placements, vote reasons, AI theme summary, exports to CSV, GeoJSON, DXF. *[shown_working]*
- Offline mode — Runs with no accounts, embedded Postgres and rule-based fallback when no AI key is set. *[shown_working]*

**Flow:** Open the demo park in the 3D editor → Place items or type a Describe-it prompt → Watch budget and rule indicators → Submit design; others walk, vote and comment → Planner views insights and exports

**Prompt:** SFU Satellite ALEASAT Earth Observation Track: put open, free Earth observation data (readable with free Python libraries) into the project doing real work; disaster relief gets extra merit.
**Fit (implied):** Uses open NRCan HRDEM lidar elevation as the terrain base; page does not mention the satellite sponsor or Python, and is not disaster-related.  *(targeted: SFU Satellite - ALEASAT - Earth Observation Track)*
**Sponsor tools:** NRCan HRDEM open elevation data (Terrain base layer for parks, core); Google Gemini (Describe-it layouts and planner summaries, supporting)
**AI:** Gemini with structured JSON output turns a prompt into a layout spec and summarises themes in comments; deterministic rule-based fallback; a non-AI solver does the geometric placement.
**Architecture:** pnpm monorepo: React + React Three Fiber web app, Hono TypeScript API, Drizzle on Postgres (pglite locally), terrain/AI/scene packages; static recorded fixtures or Vancouver Open Data, TransLink GTFS and OSM.
**Novelty:** Ties real lidar and municipal data to participatory design with planner analytics; works fully offline.
**Scope:** large · working: Demo video; repo is about 155k LOC (likely includes bundled data) with tests, CI and docs; README says nothing was deployed from the repo and nobody runs it as a service. · polish: Extensive README, BC Design System UI, quick start with seed data.
**Claims:** Works completely offline, AI included | Demo parcel is 1.4 ha with 22 trees and 56 garden plots
**Gaps:** Devpost title "Project Thing"; project called CommonGround/Parkshape in repo; No hosted demo; Prize text does not mention satellite sponsor in project
Sources: https://devpost.com/software/project-thing-cg94vo, https://github.com/zach1502/commonground (evidence README), https://stormhacks2026.devpost.com/

---

### CrimePath
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A case-management web app for investigators that turns uploaded evidence such as CCTV, photos and files into structured events using Gemini, then shows them on an interactive timeline and map with linked subjects and traceable sources.
**Problem / user:** Investigators who must build reliable timelines from fragmented evidence and easily miss inconsistencies, such as impossible travel times.

**Features**
- Case and evidence upload — Create cases and add CCTV, images and files, or enter evidence manually *[claimed]*
- AI event extraction — Gemini pulls timestamps, locations, subjects and descriptions from evidence into structured events validated by shared TypeScript schemas *[claimed]*
- Interactive timeline — Chronological view of events with detail pages linking back to evidence *[claimed]*
- Map view — Shows where events occurred and maps timelines *[claimed]*
- Subject tracking — Subjects are created and linked to many events across a case *[claimed]*
- Conflict view — Analysis screen for inconsistencies between events; mechanism not described *[unclear]*
- Time-based querying and live updates — Fast queries on TigerData Postgres with real-time evidence updates *[claimed]*
- OpenCV CCTV subject detection — Planned detection of known subjects creating timestamped candidate evidence *[planned]*

**Flow:** Create a case → Upload evidence or enter it manually → AI converts it into structured events → Open unified case view → Explore timeline, map, subjects and conflicts → Review AI output and trace events to evidence

**Prompt:** MLH prize encouraging AI-powered apps built with the Gemini API that make friends say WHOA.
**Fit (implied):** Gemini turns unstructured evidence into structured, schema-validated event data that powers the entire timeline, map and subject views.  *(targeted: [MLH] Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Analyzing uploaded evidence into structured events, core); TigerData (Postgres) (Database for cases, subjects, evidence, events, supporting)
**AI:** Gemini analyzes uploaded evidence and returns timestamps, locations, subjects and descriptions; shared schemas validate output; humans review before treating as fact.
**Architecture:** React/TypeScript frontend on Vercel, Node/Express TypeScript monorepo backend on Render, TigerData Postgres with related cases, subjects, evidence and events tables.
**Novelty:** Models many-to-many links between events, subjects and evidence and stresses uncertainty handling; idea came from a teammate's law-enforcement background.
**Scope:** medium · working: Live site crimepath.tech; no repo listed; screenshots of timeline, map, subjects and conflict views. · polish: Deployed on Vercel and Render with several screenshots; no video.
**Claims:** Detects timeline inconsistencies across evidence
**Gaps:** no repo; no video; live site not opened; screenshot count unknown
Sources: https://devpost.com/software/crimepath, https://stormhacks2026.devpost.com/

---

### Cubic
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** IATSU - Best Design Track

**What it is:** A browser two-player pixel-art co-op puzzle game: one player walks the outside of a cube and the other is trapped inside its mirrored dark walls; they talk via proximity voice to solve puzzles on six faces. Solo play uses a Gemini/ElevenLabs AI partner.
**Problem / user:** Friends playing co-op games who want communication to be the core mechanic; solo players get an AI partner.

**Features**
- Asymmetric inside/outside play — Each player sees only their own side; one holds the clue, the other the controls; inside view is mirrored. *[shown_working]*
- Six themed puzzle faces — Grass keypad, desert vault code, snow symbol rebuild, forest flowers, rooftop order, cave mirror laser, with item hand-offs and randomized seeds. *[shown_working]*
- Proximity voice chat — WebRTC voice quieter with cube distance, silent on opposite face, plus text chat. *[shown_working]*
- Lobbies and solo mode — Create/join by room code, character select, or play solo with AI partner in two voices. *[shown_working]*
- AI partner — Gemini generates partner chat and personality; ElevenLabs speaks it. *[shown_working]*
- Cross-device input — Keyboard, gamepad and touch; rebindable keys, desktop and mobile browser. *[shown_working]*

**Flow:** Open playcubic.tech → Create or join lobby, or choose solo → Pick outside or inside side → Talk through puzzles across six faces → Finish and see the unfolded cube end screen

**Prompt:** IATSU Best Design Track: "The project with the best overall design!" with a $100-value prize; design undefined.
**Fit (implied):** Team-drawn pixel art, six themed faces and a novel inside/outside mirror mechanic; page names the track win but gives no design rationale.  *(targeted: IATSU - Best Design Track)*
**Sponsor tools:** Google Gemini (AI partner chat, supporting); ElevenLabs (AI partner voices, supporting)
**AI:** Gemini produces the solo AI partner replies; ElevenLabs text-to-speech gives two selectable voices; core gameplay is not AI-driven.
**Architecture:** TypeScript monorepo: Phaser 4/Vite client on Vercel, Node + Socket.io server on Render with shared game logic, WebRTC voice with optional TURN, PostHog anonymous stats.
**Novelty:** Asymmetric two-sided cube concept with mirrored interior and distance-based voice attenuation; unusually complete game scope.
**Scope:** large · working: Live playable site, backup URL, YouTube video, about 58k LOC with tests and docs. · polish: Illustrated README, team-made sprites, licensed music credits, privacy toggle, rebindable controls.
**Claims:** Full co-op game in browser with no downloads, desktop and mobile
**Gaps:** Design process not described; Devpost lists four puzzle types, README six faces; merged
Sources: https://devpost.com/software/cubic-wu2s5i, https://github.com/ltanafranca1004/Cubic (evidence README), https://stormhacks2026.devpost.com/

---

### Deceipt
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Enactus SFU - United Nations Sustainability Development Goals (UNSDG) Track

**What it is:** A static website about paper-receipt waste that opens with a short arcade game, reveals personalised environmental figures, then offers a clickable demo app for digital receipts with warranty tracking and export.
**Problem / user:** Everyday shoppers who lose or cannot read faded paper receipts needed for returns, warranties or expenses; the pitch also targets receipt-driven paper, tree and water waste.

**Features**
- Your Paper Trail arcade game — Player counts weekly receipts, plays a 20-second canvas dodge round with keyboard or touch, and sees the yearly pile in metres. *[shown_working]*
- Personalised environmental reveal — Converts the entered receipt count into tree and water impact, with sourced caveats on each statistic. *[shown_working]*
- Digital receipt demo app — Interactive front-end prototype with a dashboard of searchable, non-fading receipts. *[shown_working]*
- Receipt verification and detail views — Prototype screens for verifying a receipt and opening its details. *[shown_working]*
- Warranty tracking — Demo screen tracking warranty status for stored receipts. *[shown_working]*
- Export to text — Receipts can be exported as text from the demo app. *[shown_working]*
- Real receipt ingestion — Email forwarding and retailer integrations plus OCR for paper receipts. *[planned]*
- On-device-first privacy model — Receipt data handled mainly on the device and not sold or used for marketing. *[planned]*

**Flow:** Land on the Your Paper Trail game → Enter how many receipts you get per week → Play the 20-second dodge round → See the yearly receipt pile and environmental reveal → Move to the digital-receipt pitch → Explore the demo app: dashboard, verification, details, warranty, export

**Prompt:** Enactus SFU UNSDG track: projects should address one or more UN Sustainable Development Goals, with special preference for Goal 17 (partnerships); one winner.
**Fit (implied):** Frames paperless receipts as reducing tree and water waste, with sourced environmental statistics; the page does not name a specific SDG or Goal 17 partnership.  *(targeted: Enactus SFU - UNSDG Track)*
**AI:** none
**Architecture:** Static React/TypeScript/Vite site on GitHub Pages with custom domain via Cloudflare DNS; canvas game and mock demo app, no backend. Repo also holds a React Native proof of concept, modules and protocol folders.
**Novelty:** Leads with a playable game as the sustainability argument before the product demo; the repo suggests a larger receipt-protocol idea (app, modules, protocol, docs) than the web page shows.
**Scope:** medium · working: Live site with game and interactive prototype; real ingestion is not built. · polish: Custom HTTPS domain, mobile fix before judging, sourced caveats on figures; repo ~26k LOC across app, modules and protocol.
**Claims:** 300 billion paper receipts printed yearly | Roughly two of three receipts discarded | About 3.3 million US trees per year | Built in 36 hours
**Gaps:** Repo README is the default React Native template; Devpost says static React/Vite while repo has React Native app, modules and protocol folders (page followed); Statistic sources not named on page; No video
Sources: https://devpost.com/software/deceipt, evidence/stormhacks-stormhacks-2026-deceipt.json, https://stormhacks2026.devpost.com/

---

### Doggin' Around
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Huawei Custom Challenge #2 - Fetching Reality

**What it is:** An interactive comic called Storm Night: upload a comic page, a rigged Gaussian-splat dog leaps out of panel 1 into a walkable rainy 3D world, and completing a small quest redraws later panels with a happier ending.
**Problem / user:** Comic readers who wish a story ended differently and want to step inside it; also built to answer the Huawei brief on turning dog photos into interactive pets.

**Features**
- Comic-to-world pipeline — Detects characters, splits a page into scenes, lifts the hero out of its panel and builds a rigged 3D character; generated offline. *[claimed]*
- Panel-to-3D transition — Hero leaps into panel 1 and it dissolves into a first-person world with rain and a Marble-generated Gaussian-splat scene. *[shown_working]*
- Branching ending quest — Dig up a key, unlock the cabin, gather firewood and light a fire; later comic panels then redraw with a new ending. *[shown_working]*
- Voice commands to the dog — Hold F and speak, e.g. sit; ElevenLabs realtime speech-to-text maps keywords to actions. *[shown_working]*
- White dog with 29 actions — 41-joint AniGen skeleton with TripoSplat Gaussians, skinning and accessories; actions include sit, dig, backflip and fetch. *[shown_working]*
- Fetch behaviour — Dog turns to a thrown ball, chases, picks it up with its mouth and carries it home. *[shown_working]*
- Gaze and attention — Dogs glance around and briefly follow the cursor with smooth head motion. *[shown_working]*
- Inspection and import tools — Toggle Gaussians, mesh or skeleton, adjust speed and density, compare photos, load an animated GLB; second tricolor dog has 12 actions. *[shown_working]*

**Flow:** Upload a comic page → Dog leaps into panel 1 and the panel dissolves into 3D → Explore the rainy world with the dog → Command the dog by voice or interaction through the quest → Return to the comic to see panels redrawn with the new ending → Optionally throw a ball or open inspection tools

**Prompt:** Huawei Custom Challenge #2 Fetching Reality: turn a static dog photo into a real-time interactive digital pet that responds, interacts with its environment or plays; SDFs, Gaussian splatting and AI tools encouraged.
**Fit (explicit):** Reconstructs two supplied dog photos into rigged Gaussian-splat dogs that obey voice, fetch, dig and track the cursor inside a generated world, rendered at 60 FPS in browser.  *(targeted: Huawei Custom Challenge #2 - Fetching Reality)*
**Sponsor tools:** ElevenLabs realtime speech-to-text (Voice commands to the dog, supporting)
**AI:** Gemini paints comic panels and in-between frames; World Labs Marble makes the splat world; AniGen, TripoSplat, BITE/D-SMAL, TRELLIS and DGE build and edit the dogs; ElevenLabs transcribes speech.
**Architecture:** Offline Python/PyTorch reconstruction on temporary GPU machines produces rigged Gaussian dogs and worlds; a Vite/TypeScript browser app renders with Three.js, Spark and Rapier physics.
**Novelty:** Combines photo-to-rigged-3D-dog research pipeline, generative comic panels and a playable world; documents skinned Gaussians, motion retargeting and a per-run GPU cost estimate.
**Scope:** large · working: Live demo, YouTube video, Playwright and voice tests; page reports 60 FPS checks on two dog models. · polish: Detailed writeup with numbers, accessories persisting across actions, controls documented.
**Claims:** Both models reach 60 FPS in Chrome at 1440x960 | White dog has 41 joints and 50,000 splats | Tricolor dog GPU cost estimated at US$2.96 | Won Huawei Challenge #2
**Gaps:** Queue github_url is the third-party AniGen repo and was not used; real repo inferred from Devpost image URLs; Repo size signals unavailable; Video not watched; Pipeline for arbitrary comics is next step so only the demo comic is shown
Sources: https://devpost.com/software/doggin-around, https://raw.githubusercontent.com/DzhanybekZakiriiaev/doggin-around/HEAD/README.md, https://stormhacks2026.devpost.com/

---

### DoubleTake
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** TiDB x AI Open Build

**What it is:** A mobile-style dating web app where two best friends form one shared duo profile and swipe on other duos, so first dates become double dates. Plain-English vibe search ranks duos using TiDB vector embeddings.
**Problem / user:** Singles who find one-on-one dating apps interview-like and nerve-wracking and would rather meet others with a friend along.

**Features**
- Duo profiles — Two friends share one profile with combined interests and a bio written together; can be edited or restarted. *[shown_working]*
- Discovery feed — Duos shown one at a time ranked by vibe similarity, like or pass with one tap. *[shown_working]*
- Vibe search — Plain-English description such as hiking and karaoke is embedded and matched by TiDB vector distance. *[shown_working]*
- Matches — When both duos like each other it is saved as a Double Take in a Matches list; Devpost says a group chat opens. *[claimed]*
- Mock-or-live API switch — One setting routes the React app to a mock API or the Spring Boot backend. *[shown_working]*
- Messaging, photos and filters — Group messaging, photo integration and richer filters. *[planned]*

**Flow:** Welcome page → Create profile → Pick a friend as duo partner and create the duo profile → Browse the discovery feed or run a vibe search → Mutual likes appear on Matches → Edit duo on Your Duo page

**Prompt:** TiDB x AI Open Build: build anything that meaningfully uses a TiDB AI capability such as vector search, full-text/hybrid search, agent memory or TiDB Cloud Filesystem.
**Fit (explicit):** Stores users, duos, swipes and matches in TiDB Cloud and uses TiDB Auto Embedding with vector distance to rank the feed and vibe search.  *(targeted: TiDB x AI Open Build, WiCS Cosmos Track (README says also submitted))*
**Sponsor tools:** TiDB Cloud vector search with auto embedding (Storage plus semantic duo ranking and vibe search, core)
**AI:** Bio and interest text embedded inside TiDB (auto embedding) and ranked by vector distance; an AiEmbeddingService turns plain-English queries into vectors. Model unnamed.
**Architecture:** React/Vite/Tailwind frontend (mobile-first) calls a Spring Boot/JPA REST API deployed on Render, backed by TiDB Cloud; contract in docs/api-contract.md.
**Novelty:** Reframes dating around a pair of friends matching another pair and uses semantic vibe search instead of profile filters.
**Scope:** small · working: Live Render site, backend and frontend folders, tests present; Devpost calls it earliest stage. · polish: Structured README with features, project layout and API contract; modest ~4.8k LOC.
**Claims:** Working vector-embedding pipeline for semantic matching | Responsive polished frontend
**Gaps:** Devpost lists Supabase without explaining role; Group chat after match only on Devpost, not README; Embedding model not named
Sources: https://devpost.com/software/doubletake-pnxuv8, evidence/stormhacks-stormhacks-2026-doubletake.json

---

### Etika
*StormHacks StormHacks 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalists

**What it is:** A compliance navigator for new sole proprietors in Vancouver, BC. After a three-step intake, three specialist agents check confirmed facts against cited official sources and return a requirement checklist, readiness score and Now/Next/Later plan.
**Problem / user:** New Vancouver sole proprietors facing fragmented registration, tax and employer rules who cannot tell what applies to them or when thresholds are crossed.

**Features**
- Three-step intake with fact confirmation — Basics, activities and a review; only answered questions become facts, unknowns stay unknown. *[shown_working]*
- Three specialist agents — Registration, Tax and Employer agents each get only retrieved evidence and return structured cited findings. *[shown_working]*
- Compliance dashboard and Now/Next/Later plan — 13 requirements with explanations, readiness score, do-first item and links to official forms. *[shown_working]*
- PST and GST threshold tracking — Rolling 12-month $10,000 PST test and four-quarter $30,000 GST test with straight-line crossing projection. *[shown_working]*
- Ask etika grounded chat — Answers only from retrieved sources with numbered citations and a sources panel; says when evidence is insufficient. *[shown_working]*
- Confirm-before-change updates — Chat proposes a fact change such as hiring; on confirm the assessment re-runs and employer duties move to Now. *[shown_working]*
- Citation validation and agent trace — Drops citations not retrieved in the run and shows a collapsible trace of tool steps. *[claimed]*
- Form prefill and deadline calendar — Pre-filled government forms, generated policy documents and renewal calendar. *[planned]*

**Flow:** Answer basics and activity questions → Review and confirm understood facts → Watch the three agents run → Answer follow-up questions with auto re-check → Read the dashboard and open requirement details → Chat a change and confirm the proposed update

**Prompt:** not public / not found
**Fit (none):** Finalist listing carries no stated prompt; the README does mention building a RAG pipeline on TiDB vector store, so a TiDB track may have been entered.  *(targeted: Finalists)*
**Sponsor tools:** TiDB Cloud (Vector and relational store for the RAG corpus, core); Gemini Flash and gemini-embedding-001 (Intake parsing, explanations, chat and embeddings, core)
**AI:** Deterministic registry engine decides requirements and score; Gemini Flash only explains, with one call per agent after code prefetches reviewed, chunked, embedded evidence from TiDB.
**Architecture:** Next.js/TypeScript frontend; FastAPI backend with coordinator and three agents; TiDB holds reviewed chunks with metadata; code computes scores, Gemini writes explanations; demo mode runs on local sample data.
**Novelty:** Hand-built official-source corpus with review status gating retrieval, rule engine separated from the LLM, rolling-window tax threshold math and an honest-gaps behaviour.
**Scope:** large · working: Backend, frontend, tests, docs and a no-backend demo route; ~18k LOC. · polish: Named specialist personas, agent trace, rate limiting, Full/Plain toggle and detailed README.
**Claims:** Gemini calls cut from 8-15 to 3 per assessment | Same facts always produce the same score | 13 requirements covered today
**Gaps:** No official finalist prompt; No demo link or video on Devpost
Sources: https://devpost.com/software/etika, evidence/stormhacks-stormhacks-2026-etika.json

---

### FloodBeacon
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [MLH] Best Use of Tiger Data

**What it is:** A responder dashboard that merges flood help requests received by SMS with before-and-after satellite imagery. Gemini turns texts into structured incident reports with follow-up questions, while a multimodal model flags visibly damaged bridges in imagery from Germany, Libya and Nepal.
**Problem / user:** Flood responders who need to see where water spread, who needs help and which bridges cut off access.

**Features**
- SMS intake — Twilio webhook with signature validation receives messages and queues them for a worker *[claimed]*
- Gemini report extraction — Extracts location, headcount, hazards and needs into validated JSON; original message kept *[claimed]*
- Follow-up questions — Asks for missing address details; sender may answer unknown *[claimed]*
- Responder triage controls — Verify reports, set priority and response status, with audit history and extraction versions *[claimed]*
- Incident map — Interactive map shows reviewed locations; GeoJSON feed of incidents *[claimed]*
- Satellite before/after overlays — Rasterio crops and aligns Maxar and Vantor imagery into georeferenced overlays with comparison images *[shown_working]*
- Bridge damage flags — Multimodal LLM annotates visible bridge destruction, kept separate from agency assessments *[shown_working]*
- Context layers — Copernicus EMSR517 flood maps and UNOSAT damage assessments referenced *[claimed]*

**Flow:** Person texts a flood request → Twilio forwards to validated webhook → Worker extracts details with Gemini and asks follow-ups if needed → Report appears on dashboard with original text → Responder verifies, prioritizes and updates status → Responder inspects satellite overlays and flagged bridges

**Prompt:** MLH prize: Tiger Data extends PostgreSQL to give student developers an ultra-fast foundation for real-time data.
**Fit (implied):** Page lists PostgreSQL for messages, extractions, incident updates, audit history and imagery annotations; it does not explicitly name Tiger Data or Timescale features.  *(targeted: [MLH] Best Use of Tiger Data)*
**Sponsor tools:** Tiger Data (PostgreSQL) (Storing messages, extraction versions, incidents and annotations; not named explicitly on page, unclear)
**AI:** Gemini extracts structured fields from SMS with schema validation and queued follow-ups; an unnamed multimodal LLM compares before/after imagery to annotate bridge damage since no pretrained model fit.
**Architecture:** Twilio to FastAPI webhook, background worker with Gemini, PostgreSQL store, FastAPI serves pre-processed Rasterio imagery to React/Vite map dashboard.
**Novelty:** Combines text-message intake and satellite damage review using real disaster imagery from three events, while separating AI findings from official assessments.
**Scope:** medium · working: Devpost claims a working SMS pipeline and imagery from three disaster sites; no repo, demo link or video. · polish: Four screenshots, two labeled before and after flood; no accuracy metrics.
**Claims:** Working SMS service producing structured reports | Identified bridge destruction in imagery from Germany, Libya and Nepal
**Gaps:** no repo, demo or video; Tiger Data usage not explicit
Sources: https://devpost.com/software/floodbeacon, https://stormhacks2026.devpost.com/

---

### HyperSpace
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** TiDB x AI Open Build

**What it is:** An explorable map of Wikipedia artificial-intelligence topics drawn on a Poincare disk, where clicking a topic recentres the hyperbolic view. TiDB powers hybrid search and Gemini grows new branches, answers questions and explains links.
**Problem / user:** Anyone exploring large knowledge collections, where lists hide relationships and node diagrams become hairballs beyond a few hundred nodes.

**Features**
- Hyperbolic navigation — Click glides the topic to centre by Mobius transformation, edges drawn as geodesics; drag, scroll and pinch to move. *[shown_working]*
- Search by meaning — TiDB runs vector and full-text search together, boosting title matches; map flies to and highlights matches. *[shown_working]*
- Grow with Gemini — Gemini picks 5-8 related Wikipedia pages as new branches, with reasons, cached in TiDB; branches graft in place. *[shown_working]*
- Ask Hyperspace — TiDB retrieves relevant topics and Gemini answers only from their summaries with clickable citations lit up on the map. *[shown_working]*
- How are these connected — Pick two topics; camera travels the path between them while Gemini explains the link. *[claimed]*
- Field lens and geometry lens — Hover lens spreads crowded rim topics; geometry rings of equal hyperbolic distance explain the layout. *[shown_working]*
- Flat Euclid view and presentation mode — Toggle same data to flat radial tree; P gives full-screen presentation; demo mode uses cached results offline. *[shown_working]*
- Listen and share links — ElevenLabs reads cards aloud when a key is set; URL tracks current topic for sharing. *[claimed]*

**Flow:** Page opens with the universe unfolding from the centre → Click a distant topic to recentre → Search by topic or question → Expand a topic to grow Gemini-picked branches → Read summary and open Wikipedia link → Toggle flat view or presentation mode

**Prompt:** TiDB x AI Open Build: build anything with TiDB meaningfully using an AI capability such as vector search, full-text/hybrid search, agent memory or Cloud Filesystem.
**Fit (explicit):** TiDB Cloud stores the topic tree with a VECTOR(1024) cosine index and full-text index, embeds text with built-in EMBED_TEXT, merges hybrid hits and caches expansions.  *(targeted: TiDB x AI Open Build)*
**Sponsor tools:** TiDB Cloud (Node store, vector plus full-text hybrid search, expansion cache, core); Gemini API (Choosing and summarising expanded topics, grounded answers, link explanations, core); .Tech Domain (hyperspacemap.tech hosting, token)
**AI:** In-database embeddings drive semantic search; Gemini selects child pages and writes strict-JSON summaries, answers questions from retrieved summaries only, and explains topic connections.
**Architecture:** Node pipeline crawls Wikipedia categories into TiDB; Next.js/React/TypeScript app renders with d3-hypertree and calls TiDB and Gemini APIs; static map file allows offline demo mode.
**Novelty:** Applies hyperbolic geometry to a knowledge graph with custom label picker, in-place graft and flat-versus-hyperbolic toggle; fits the Euclid-themed event theme.
**Scope:** medium · working: Live site, video, pipeline and app folders; README documents many working interactions. · polish: Opening animation, themes, presentation mode, offline fallback, shareable links.
**Claims:** 2,475 topics (249 categories, 2,226 articles) per Devpost | About 470 nodes rendered live | Search falls back to keyword matching when API unreachable
**Gaps:** README says 5,635 topics, Devpost says 2,475 (README may describe later dataset; feature list merges both); No benchmarks
Sources: https://devpost.com/software/hyperspace, evidence/stormhacks-stormhacks-2026-hyperspace.json

---

### Ink Habitat
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** TiDB x AI Open Build

**What it is:** A multiplayer creature-farm website where players draw their own creatures, name them, and let AI assign behaviours and a voice, then explore island habitats, visit friends and run three-on-three battles.
**Problem / user:** Players of creature or farm games who cannot create their own creatures from restricted shop options and want social play with them.

**Features**
- Draw your own creatures — In-browser drawing becomes a creature that wanders its island habitat when clicked. *[shown_working]*
- AI behaviour and attacks — Gemini picks part roles, animations and an attack for each drawn creature (free tier about 20 creatures per day). *[shown_working]*
- Creature voices — ElevenLabs generates a voice clip from the speech text given to each creature. *[shown_working]*
- Three landscapes — Grassland base island plus Desert and Ocean habitats to explore. *[shown_working]*
- Friends and farm visits — Accounts, friends list and visiting friends farms backed by shared database. *[shown_working]*
- Team battles with buff cards — Battle waiting room, three creatures each, random buff cards that help or hurt, winner picks a creature from loser side. *[shown_working]*
- Rest period after battle — Creatures must rest after fighting. *[claimed]*
- Feeding, levelling and desktop companions — Deeper creature care and appearing on player desktops. *[planned]*

**Flow:** Sign up or log in → Draw a creature and give it a name and speech → AI assigns behaviour and voice → Creature wanders the habitat; explore other landscapes → Add friends and visit farms → Challenge a friend to a three-creature battle with buff cards → Winner picks a creature

**Prompt:** TiDB x AI Open Build: build with TiDB meaningfully using an AI capability such as vector search, hybrid search, agent memory or Cloud Filesystem.
**Fit (implied):** README says accounts, friends, creatures and battles live in a shared TiDB Cloud cluster; Devpost does not mention TiDB, and no vector or hybrid search use is stated.  *(targeted: TiDB x AI Open Build)*
**Sponsor tools:** TiDB Cloud (Shared database for accounts, friends, creatures and battles (README), core); Gemini (Creature part roles, animation and attack details, supporting); ElevenLabs (Creature voice clips, supporting)
**AI:** Gemini analyses a drawn creature to assign part roles, animations and attack logic; ElevenLabs text-to-speech produces its voice, so creatures animate without hand-made rigs.
**Architecture:** Python server with frontend and backend folders serving the game site, persisting to a shared TiDB cluster, calling Gemini and ElevenLabs when keys are present; has tests and scripts.
**Novelty:** Player-drawn assets are turned into animated, voiced fighters automatically; authors say neither had made a game before.
**Scope:** small · working: Repo with frontend, backend, tests and run docs; video; no live site listed. · polish: Detailed run and settings README; screenshots of habitat, battle and win screens.
**Claims:** Built with no prior game development experience
**Gaps:** Devpost tech list omits TiDB; README shows it; Whether TiDB AI capabilities (vector search) are used is not stated
Sources: https://devpost.com/software/ink-habitat, evidence/stormhacks-stormhacks-2026-ink-habitat.json

---

### Onus.
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of ElevenLabs

**What it is:** A live map of BC's 26 public colleges and universities that grades each school's sexual violence policy two ways: what the written policy commits to, graded by AI against 17 criteria with verbatim quotes, and what students report anonymously. The gap between the two is highlighted.
**Problem / user:** BC students, and policy offices, lacking a public plain-language place to see whether campus sexual violence policies are strong, current and followed.

**Features**
- On-paper policy grade — Gemini grades each published policy against 17 Students for Consent Culture criteria; points count only with a verified word-for-word quote *[shown_working]*
- In-practice student ratings — Anonymous multiple-choice ratings from verified school email; gap ring appears with at least five real ratings, updating live via Supabase Realtime *[shown_working]*
- Interactive BC map — MapLibre map colored green to red per school, clustering when zoomed out, with support centres and hospitals layers *[shown_working]*
- School panel — Per-category scores with quoted clauses, BC rank, policy review clock and what to raise at review *[shown_working]*
- Policy viewer and Q&A — PDF.js opens highlighted quote; text or voice questions in any language answered only from that policy with section cited, refuses off-topic *[shown_working]*
- Support routing — Precomputed OSRM routes to nearest sexual assault support, counselling and hospital; crisis lines on every page *[shown_working]*
- Live grading and report-card audio — Paste a policy PDF link to grade live; ElevenLabs reads each report card aloud *[shown_working]*
- Open data and sources pages — Method, privacy policy, source links for every number and downloadable grade files *[claimed]*

**Flow:** Open the map and see all schools colored by grade → Select a school for its on-paper grade, ratings and gap → Check clause scoring, rank, review dates and nearby support with a route → Open the policy PDF to verify quotes → Ask a question by text or voice → Rate your school with a school email code → Paste a policy PDF to see live grading

**Prompt:** MLH prize: deploy natural, human-sounding audio with ElevenLabs; prize wireless earbuds.
**Fit (implied):** ElevenLabs Scribe handles voice questions, and TTS (including Farsi and Punjabi voices) reads report cards and answers, giving multilingual accessible access to policy information.  *(targeted: [MLH] Best Use of ElevenLabs)*
**Sponsor tools:** ElevenLabs STT/TTS (Voice questions to the policy Q&A and spoken report cards, multilingual, supporting); Gemini API (Policy grading, Q&A, embeddings, core)
**AI:** Gemini pipeline crawls, extracts, grades and verifies each policy against a strict 17-criterion rubric; a separate pass rejects quotes not in the PDF. Embeddings in pgvector power policy-only Q&A with citations.
**Architecture:** Next.js 16 app on Supabase (Postgres RLS, email-code auth, Realtime, pgvector); offline scripts crawl, grade and embed policies; MapLibre plus OSRM routes; Gemini and ElevenLabs APIs.
**Novelty:** Civic accountability tool pairing AI-graded written policy against student reality, with quote verification and a legal review-date clock; real data pipeline for 26 institutions.
**Scope:** large · working: Live at onusmap.tech; about 8,500 LOC, 394 files, data pipeline scripts, many Playwright test scripts; in-practice ratings mostly seeded samples. · polish: Docs, privacy and sources pages, accessibility tests, demo video.
**Claims:** Covers all 26 public BC institutions | Every scored point backed by a verified verbatim quote | Gap ring needs at least five real ratings
**Gaps:** video not watched; screenshot count unknown
Sources: https://devpost.com/software/onus-hx2fua, https://github.com/TheRoryQueen/OnusBC, https://stormhacks2026.devpost.com/

---

### Otter Nonsense
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Surge Choice Award

**What it is:** A relaxed multiplayer 3D browser game where players are otters who dive for clams and trinkets, chat, buy hats and sit by a campfire or stream, with no account needed.
**Problem / user:** Casual players who want a chill, social collection game in the spirit of WEBFISHING and Sledding Game; no formal problem stated.

**Features**
- Multiplayer otter world — Players join without an account, move around a shared 3D scene and chat with each other. *[shown_working]*
- Diving for clams and trinkets — Dive into water carrying momentum to collect clams and trinkets; shell count shown top-right. *[shown_working]*
- Hat shop — Spend collected shells on hats and accessories for your otter. *[shown_working]*
- Journal — Collection journal with a backdrop; mouse unlocks on opening and relocks on closing. *[shown_working]*
- Relaxation spots — Campfire and stream-side benches with sunrise views; reduced sit delay. *[shown_working]*
- Automatic deployment — GitHub Actions deploys to a VPS behind Caddy. *[shown_working]*
- More minigames and private servers — Extra minigames, friends-only servers, clothing beyond hats. *[planned]*

**Flow:** Open otternonsense.tech with no sign-up → Explore the world and chat → Dive for clams and trinkets → Sit at campfire or benches → Buy hats with shells → Open the journal

**Prompt:** not public / not found
**Fit (none):** Devpost lists no description for the Surge Choice Award and the page does not say it targets it; project is a polished multiplayer game.  *(targeted: Surge Choice Award)*
**AI:** None in the product; authors say AI assisted their development workflow.
**Architecture:** three.js JavaScript client with Blender models; Python server handles multiplayer over websockets with a SQLite database; Caddy serves the built frontend and proxies the websocket; CI deploy to a VPS.
**Novelty:** A complete cozy multiplayer game with a custom domain, backups and CI deploy rather than a local prototype.
**Scope:** medium · working: Live demo site, video, multiplayer server and deploy scripts; ~10k LOC. · polish: Eight screenshots, scenery, no-account onboarding, scripted deploys with DB backups.
**Claims:** Working multiplayer and automatic deployment
**Gaps:** Surge Choice prompt has no description; README is a deployment guide only; Animation issues mentioned as challenge
Sources: https://devpost.com/software/otter-nonsense, evidence/stormhacks-stormhacks-2026-otter-nonsense.json

---

### Phase Escape
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Huawei Custom Challenge #1 - Beyond Euclid

**What it is:** A chase game on the hyperbolic plane with five colour layers acting as a fourth dimension. You roll a marble through a maze, phase between layers to pass doors and shake hunters, and looping a pillar shifts layer by itself. An ESP32 tilt controller is optional.
**Problem / user:** Puzzle and chase-game players, and people curious about hyperbolic geometry; the goal is to let players feel curvature as a mechanic rather than a visual trick.

**Features**
- Hyperbolic maze — Pentagonal rooms in a Poincare disk using exact Lorentz-matrix geometry and GPU instancing at 60 FPS. *[shown_working]*
- Five colour layers — Doors and shards open only in their colour; hunters only see and hurt you in theirs; shifters change colour on a timetable. *[shown_working]*
- Holonomy layer shift — Looping around a pillar turns you 72 degrees, moving you one layer; one level disables twisting so loops are the only route. *[shown_working]*
- Tesseract view and rifts — Rotate a 4D view in XW and YW planes so shadow planks over rifts become bridges. *[shown_working]*
- ESP32 tilt controller — BNO055 sensor streams tilt at 100 Hz over BLE or USB; tilt rolls, twist phases, BOOT button turns the 4D view. *[shown_working]*
- Nine levels with scoring — Tutorial tips, lives, timer, par stars and high scores; per-layer chords in music. *[shown_working]*
- Solver and autopilot — Automated solver proves every level solvable and an autopilot plays levels with real physics; 143 tests. *[shown_working]*
- Windows Electron app — Desktop packaging so the BLE controller works. *[claimed]*

**Flow:** Pair controller or use keyboard → Read tutorial tips → Roll the marble through the maze with hunters chasing → Phase colours to pass doors and grab shards → Loop pillars or rotate tesseract to cross rifts → Collect all shards and enter the portal; see stars and high score

**Prompt:** Huawei Custom Challenge #1 Beyond Euclid: build an interactive experience where Euclidean geometry no longer applies and non-Euclidean geometry is meaningful, such as hyperbolic worlds, spherical spaces or 4D projections.
**Fit (explicit):** README says it was built for the challenge: hyperbolic plane world plus a fourth colour dimension, with curvature (holonomy) changing layer and a tesseract view.  *(targeted: Huawei Custom Challenge #1 - Beyond Euclid)*
**AI:** No AI in the game; developer built it with Claude Code and used tests to check its output.
**Architecture:** TypeScript/Three.js browser game with hyperboloid-model geometry; Electron desktop wrapper; ESP32 firmware streams IMU orientation over BLE or USB; solver and autopilot test tooling plus docs folder and CI.
**Novelty:** Curvature is the core mechanic and a physical controller carries the holonomy idea; ships a level solver and autopilot proving solvability.
**Scope:** medium · working: Demo site, video, firmware and desktop folders, 143 tests, CI; ~10k LOC. · polish: Nine levels, tutorial, music per layer, Bluetooth retry UI, six screenshots.
**Claims:** 60 FPS in curved space | Controller streams at 100 Hz | 143 automated tests | All 9 levels proven solvable
**Gaps:** README read only to first 3000 chars of 7000
Sources: https://devpost.com/software/phase-escape, evidence/stormhacks-stormhacks-2026-phase-escape.json, https://stormhacks2026.devpost.com/

---

### Pixel Cat Arena
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Game

**What it is:** A browser game about raising a pixel-art cat, equipping rarity-tiered gear and fighting scaling enemies or other players. Legendary items can be exported as Solana devnet NFTs and still used in battle.
**Problem / user:** Browser game players who like PvE, PvP and trading and want rare items they truly own rather than as database rows.

**Features**
- Cat builder and gear — Equip body, head, weapon and accessory from four rarity tiers; changes show instantly on the cat. *[shown_working]*
- PvE battles — Endless scaling enemies for coins and drops, simulated server-side with turn-by-turn playback. *[shown_working]*
- PvP challenges — Publish a build and challenge any player by username; match resolved on the server and replayed in the arena. *[shown_working]*
- Marketplace — Sell gear for coins or list it at a fixed price for other players. *[shown_working]*
- Solana NFT export — Export a legendary as a devnet NFT; it stays usable in battle but in-game selling is permanently disabled. *[shown_working]*
- Wallet-signature claim — Whoever holds the wallet signs a free message (Phantom) to claim the item into their own account. *[shown_working]*

**Flow:** Create account and build a cat → Equip gear → Fight PvE enemies for drops → Challenge another player → Trade on the marketplace → Export a legendary to Solana and claim it with a wallet

**Prompt:** Best Game: event-run category, described only as the best game project.
**Fit (implied):** A complete multiplayer browser game with server-authoritative combat and trading; Solana devnet NFT ownership layer fits the MLH Solana prize but is not stated as its target.  *(targeted: Best Game)*
**Sponsor tools:** Solana (devnet) (NFT export of legendary items and wallet-signature claim, supporting)
**AI:** none
**Architecture:** Python FastAPI/SQLAlchemy backend with SQLite resolves all fights and trades server-side; TypeScript/Vite frontend; Solana devnet mint and Phantom signature claim; AGENTS.md holds implementation plan.
**Novelty:** Hybrid ownership model: item stays in the game database for battle while an NFT carries trade rights, with a signature-based claim-back; solo build.
**Scope:** medium · working: Backend and frontend with tests, make targets, video, real devnet mint and claim reported working; no live site. · polish: Clear README, rarity system, replay arena, docs; ~8.5k LOC.
**Claims:** Real Solana devnet mint works end to end | Wallet-signature claim flow works end to end | Built solo
**Gaps:** Best Game criteria only one line
Sources: https://devpost.com/software/pixel-cat-arena, evidence/stormhacks-stormhacks-2026-pixel-cat-arena.json

---

### PunchCode
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** CSSS - SFU CS Legacy Track

**What it is:** A browser simulator of the IBM 029 keypunch where users punch Fortran programs onto cards and compile them by feeding the card stack, with a tutorial, featured levels including LeetCode-style problems, Fortran notes and sound design.
**Problem / user:** People curious about computing history and programming as done on punch cards; built as a tribute to SFU card-punch coding.

**Features**
- IBM 029 keypunch simulation — Browser interface mimicking the machine for punching Fortran onto cards. *[shown_working]*
- Compile via card stack — Punched cards are fed as a stack and the Python backend compiles and runs the Fortran. *[shown_working]*
- Tutorial and main screen — Guided intro to using the keypunch before levels. *[shown_working]*
- Featured levels — Challenge levels, some LeetCode-style problems. *[shown_working]*
- Fortran notes — In-app notes helping users learn Fortran. *[claimed]*
- Period sound design — Machine sounds meant to give atmosphere. *[claimed]*
- Accuracy modes — Selectable levels of historical accuracy or manual machine procedures. *[planned]*

**Flow:** Complete the tutorial → Reach the main screen → Choose a featured level → Punch Fortran on the simulated keypunch → Feed the card stack to compile and run

**Prompt:** CSSS SFU CS Legacy Track: create a project paying tribute to a historical computing science achievement; teams must also complete part of an SFU CS History scavenger hunt.
**Fit (explicit):** Recreates the IBM 029 card-punch coding workflow; Devpost says it was inspired by an SFU card-punch machine and the CSSS Historical Track.  *(targeted: CSSS - SFU CS Legacy Track)*
**AI:** none
**Architecture:** Next.js/TypeScript frontend renders the keypunch and card stack; Python FastAPI backend compiles and runs submitted Fortran.
**Novelty:** Turns obsolete card-punch programming into an interactive level-based experience that actually compiles Fortran.
**Scope:** small · working: Live site punchcode.tech, video and frontend/backend folders; ~3k LOC. · polish: Sound design, tutorial and levels; README is one line.
**Claims:** High historical accuracy was a main goal
**Gaps:** No step-by-step flow on page; flow inferred from captions; Fortran compile sandboxing not described
Sources: https://devpost.com/software/punchcode, evidence/stormhacks-stormhacks-2026-punchcode.json

---

### Rapid Triage
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best Hardware

**What it is:** A mass-casualty triage system: an ESP32 wearable streams heart rate, SpO2, temperature and ECG over local Wi-Fi to a Tiger Data store, a feature-based engine ranks patient priority, and a Next.js dashboard plus iOS responder app assign and locate patients.
**Problem / user:** Incident commanders and field responders in mass-casualty events, where patients outnumber responders and a one-time triage snapshot misses deterioration.

**Features**
- ESP32 vitals wearable — Collects heart rate, SpO2, body temperature and ECG with an on-device display, LED, buzzer and buttons. *[claimed]*
- Offline local networking — Sends data over a portable local Wi-Fi network without Internet; BLE used for responder proximity. *[claimed]*
- Ingestion pipeline — Python Flask service validates, parses and timestamps messages and ties them to the right patient. *[claimed]*
- Tiger Data time-series store — PostgreSQL-based layer holds vitals history, devices, patients, scores and workflow data. *[claimed]*
- Triage Engine — Computes recent averages, rate of change, persistence and multi-signal deterioration into explainable, continuously updated priority scores. *[claimed]*
- Command dashboard — Next.js view of latest vitals, trends, status and relative patient priority. *[claimed]*
- iOS responder app — Receives assignments, shows patient info, finds the wearable via BLE signal strength and marks patients treated. *[claimed]*

**Flow:** Responder places wearable on patient → Vitals stream to backend over local Wi-Fi → Engine updates priority scores → Dashboard ranks patients → Responder gets assignment in iOS app → BLE signal strength guides responder to the wearable → Responder treats and marks patient treated; priority keeps updating

**Prompt:** Best Hardware: event-run category, described only as the best hardware project.
**Fit (implied):** Custom multi-sensor ESP32 wearable with firmware, local networking and a responder loop; Tiger Data holds time-series vitals.  *(targeted: Best Hardware, MLH Best Use of Tiger Data (Devpost page describes Tiger Data as core store))*
**Sponsor tools:** Tiger Data (Time-series and relational store for vitals, scores and workflow, core)
**AI:** No machine learning claimed; an explainable feature-based scoring engine over vitals history.
**Architecture:** ESP32 firmware sends sensor data over Wi-Fi to a Flask ingestion service, into Tiger Data; analytics pipeline scores patients; Next.js dashboard and iOS app read and update assignments.
**Novelty:** End-to-end loop from body sensors to assignment, BLE-guided locating and treatment status, designed for offline incident networks; priority is explainable rather than a black box.
**Scope:** medium · working: Main repo has iOS app and backend; separate firmware repo of 14 files; no demo or video listed. · polish: Four screenshots; main README is a single heading; no quantitative testing reported.
**Claims:** End-to-end prototype across hardware, firmware, networking, storage, analytics, dashboard and iOS app
**Gaps:** Main repo README empty; firmware repo has no README (file names only); No demo, video or measurements; Working status of each feature is by description only
Sources: https://devpost.com/software/rapid-triage, evidence/stormhacks-stormhacks-2026-rapid-triage.json, https://github.com/dhingraketan/rapid_triage_firmware

---

### ReliefPool
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Solana

**What it is:** A disaster-relief fund on Solana that pays out automatically when an earthquake looks likely to cause a tsunami. An oracle watches the USGS feed, a trained classifier scores tsunami risk, and an Anchor program sends vault funds to pre-set relief wallets above a threshold.
**Problem / user:** NGOs and relief groups, whose funding reaches disaster victims days or weeks after the event.

**Features**
- On-chain relief pool — Anchor program holds donations in a vault; wallet users contribute and payouts are publicly visible *[claimed]*
- Tsunami risk classifier — Logistic regression on USGS magnitude/depth and NOAA tsunami data served by FastAPI *[shown_working]*
- Earthquake oracle — Node service polls USGS, filters by minimum magnitude, scores via classifier, and calls trigger_payout above threshold *[claimed]*
- Payout safeguards — Duplicate-event ID check, fail-safe that withholds payout if classifier fails, vault balance rules check *[claimed]*
- Automatic fund distribution — trigger_payout moves funds to admin-specified relief wallets and marks event pending then paid *[claimed]*
- Historical earthquake replay — Dashboard can replay past quakes to demonstrate the flow *[claimed]*
- Web dashboard with wallet — Vite frontend with Phantom/Solflare wallet support for Contribute button on devnet *[claimed]*

**Flow:** Create a relief pool → Fund it from a Solana wallet → Oracle monitors earthquakes → Classifier assesses tsunami risk → Threshold crossing triggers payout → Funds distributed to relief wallets and shown on dashboard

**Prompt:** MLH prize: harness Solana's core advantages like blazing-fast execution and near-zero transaction costs; prize a SenseCAP card tracker.
**Fit (explicit):** Uses Solana's cheap fast transactions so relief can be released automatically in seconds; program deployed on devnet.  *(targeted: [MLH] Best Use of Solana, Enactus SFU UN SDG track)*
**Sponsor tools:** Solana (Anchor, devnet) (Vault program and trigger_payout transfers, core)
**AI:** Logistic regression trained on joined USGS and NOAA records; reported 87% accuracy, 84% recall, 0.97 ROC-AUC; handles class imbalance and threshold trade-off.
**Architecture:** USGS feed to Node/Express oracle, which calls FastAPI classifier, then Anchor trigger_payout on Solana devnet; React/Vite dashboard; oracle can simulate chain without keypair.
**Novelty:** Parametric-insurance-style payout triggered by ML risk score and on-chain transfer, with explicit safeguards against double payout and classifier failure.
**Scope:** medium · working: About 11,300 LOC across frontend, oracle, classifier and Rust program; deployed to devnet; has tests; oracle can simulate chain. · polish: Detailed README, video, env example; run needs private oracle keypair for real chain.
**Claims:** Classifier 87% accuracy, 84% recall, ROC-AUC 0.97 | No double payout per earthquake ID
**Gaps:** video not watched; no next steps stated
Sources: https://devpost.com/software/reliefpool, https://github.com/manandrew-dev/ReliefPool, https://stormhacks2026.devpost.com/

---

### ReTrace
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Solo

**What it is:** A vehicle re-identification demo on city traffic-camera footage: it detects and tracks every vehicle, fingerprints appearance and make/model, and lets a user find a car by text, spoken witness statement or photo, then follow it across cameras on a Vancouver map. It indexes vehicles, not faces or plates.
**Problem / user:** Cities with existing traffic cameras and witnesses of stolen or hit-and-run vehicles, where plate-based systems fail when plates are swapped and witnesses remember the car.

**Features**
- Detection, tracking and classification — Fine-tuned YOLOv12n and ByteTrack; EfficientNetV2-M classifier covers 9,630 make/model/generation classes plus body type and colour. *[shown_working]*
- Appearance fingerprint — Best four quality-scored crops averaged into a 2048-D embedding per vehicle. *[shown_working]*
- Text search — CLIP ViT-B/32 ranks vehicle crops against a typed description, with parsed attributes as filters. *[shown_working]*
- Voice witness search — Whisper transcribes a spoken statement parsed for colour, body type and make. *[shown_working]*
- Photo or clip search — Upload a car image or clip to match against indexed vehicles on all cameras. *[shown_working]*
- Cross-camera journey linking — Sightings joined only by mutual best match above a threshold with body-type and colour checks. *[shown_working]*
- Route map and follow view — Route drawn on an OpenStreetMap-based Vancouver map; camera view keeps the car centred with synced boxes. *[shown_working]*
- Honest labelling — Make and model shown only when reliable, else colour and body type. *[claimed]*

**Flow:** Search by text, voice or photo → Review ranked vehicle matches → Select a vehicle to see other camera sightings → View its route on the map → Use the follow view on a camera

**Prompt:** Best Solo: event-run category, described only as the best solo project.
**Fit (explicit):** Single author built detection, re-identification models, backend and website within one weekend; the README names the Best Solo award.  *(targeted: Best Solo)*
**AI:** YOLOv12n detector, ByteTrack tracker, two EfficientNetV2-M models for classification and embeddings, CLIP for text search and Whisper for speech, with a matching rule tuned by F1 on multi-camera ground truth.
**Architecture:** Pipeline extracts clips, tracks and indexes vehicles; FastAPI on one RTX 3090 serves CLIP, Whisper and photo search; React/Vite site on GitHub Pages with cached feeds works without the GPU.
**Novelty:** Trains custom detector and re-identification models, reports metrics on CityFlowV2 and estimates per-city GPU cost; ships training code, weights and a retrain guide. Safeguard framing: no faces or plates; retention rules and search audit log listed as next steps.
**Scope:** large · working: Live demo site and GPU tunnel, 18 feeds with 697 indexed vehicles, training code and weights in repo. · polish: Story page, city map, under-the-hood metrics panel, CI, quantified evaluation.
**Claims:** Detector 88.8% precision, 86.1% recall, 92.4% AP50 | Combined models 75.0% Rank-1 on CityFlowV2 | Journey linking 66% precision at 63% recall | 68 fps detection and tracking on one RTX 3090 | About US$167 per camera hardware estimate
**Gaps:** Demo footage is public datasets placed at illustrative Vancouver intersections, not real city feeds; Qwen appears only in tags; No stated consent or deployment safeguards beyond future retention and audit rules
Sources: https://devpost.com/software/retrace-p3i7kl, evidence/stormhacks-stormhacks-2026-retrace.json

---

### SI Storage
*StormHacks StormHacks 2026 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Finalists

**What it is:** A 3D warehouse operations dashboard that shows racks and shelves from a generated template warehouse and a Neon Postgres-backed main warehouse, with OCR of shelf images appearing only as pending observations until a human edits stock.
**Problem / user:** Small warehouse teams who need to know what is on each shelf and its condition, where manual counts are slow and single photos miss hidden boxes.

**Features**
- 3D multi-warehouse dashboard — React Three Fiber scene with a generated Template Warehouse and a Main Warehouse reading real balances from Neon. *[claimed]*
- Rack and shelf inspection — Condition views, alerts and event history per rack and zone. *[claimed]*
- OCR pending observations — Selecting a zone loads two stored Cloudinary images and OCR extracts labels shown as pending, not stock. *[claimed]*
- Manual shelf editing — Edits product, quantity or condition with an atomic update that records an adjustment event. *[claimed]*
- Statistics panel — Built from inventory events, using dispatches as a demo sales proxy. *[claimed]*
- Inventory Chat — Answers from a bounded set of database facts, optional Gemini. *[claimed]*
- Firebase auth — Registration, sign-in, sessions and password reset; FastAPI verifies ID tokens. *[claimed]*
- Camera-pose mapping and review workflow — Map cameras to shelves, match cartons across views, human review, forecasts. *[planned]*

**Flow:** Register or sign in → Open Template or Main Warehouse in 3D → Inspect racks, conditions, alerts and history → Select a zone to load images and view OCR observations → Make a manual shelf edit that logs an event → Check statistics or ask Inventory Chat

**Prompt:** not public / not found
**Fit (none):** Finalist listing carries no stated prompt; Devpost page also shows a Winner tag without clarifying which prize.  *(targeted: Finalists)*
**AI:** OCR pipeline extracts label text from warehouse images into pending observations; optional Gemini powers Inventory Chat over bounded database facts.
**Architecture:** React/Three.js frontend (scene adapted from a WareTwin scene); FastAPI verifies Firebase tokens and reads and writes Neon PostgreSQL; images in Cloudinary; scans and observations stored apart from verified balances.
**Novelty:** Deliberately separates source images, OCR observations and the verified ledger so vision output never changes stock without human action.
**Scope:** medium · working: Devpost describes working dashboard, DB panels and editor, but no demo, video or readable repo. · polish: Clear scope statements and honest limits; no screenshots counted.
**Claims:** Neon-backed Main Warehouse separated from generated template data
**Gaps:** Repo clone failed and README fetch via raw and github pages failed; No demo or video; Queue shows Finalists while page shows Winner and Finalists tags
Sources: https://devpost.com/software/si-storage

---

### Soft Step
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Sports Analytics

**What it is:** A leg-worn ESP32 sensor with two IMUs on thigh and shin that estimates knee angle and landing impact during hikes, streams to a web app over Bluetooth, stores hike stats, and offers a Snowflake Cortex chatbot to review technique.
**Problem / user:** Hikers, especially beginners, who get knee pain on descents and have only guesswork about their downhill technique.

**Features**
- Knee-angle estimation — Two IMUs combined with a complementary filter on accelerometer and gyroscope data, with calibration. *[shown_working]*
- Foot-strike and poor-landing detection — Acceleration spikes mark foot strikes; knee position plus impact flags poor landings. *[claimed]*
- Wearable feedback — Device gives immediate feedback on landings. *[claimed]*
- Live hike plotting — Web app plots ESP32 step data via Chart.js, with start and stop controls and step logs held in IndexedDB. *[shown_working]*
- Hike history and stats — Saves duration, active time, steps, average impact, hardest step and knee angle at impact, with graphs; logs stored gzip-compressed in Supabase. *[shown_working]*
- Cortex chatbot — Backend fetches hike records from Supabase and sends them with the question to Snowflake Cortex to compare hikes and explain technique. *[shown_working]*

**Flow:** Strap sensor to the leg → Pair with web app over Bluetooth → Start hike and watch live data → Stop hike so stats and step logs save → Review history and graphs → Ask the chatbot about technique

**Prompt:** Best Sports Analytics: event-run category for the best data science project related to sports.
**Fit (implied):** Turns raw leg-sensor data into hiking biomechanics metrics and per-hike analytics; Snowflake Cortex chat is an extra analysis layer.  *(targeted: Best Sports Analytics, MLH Best Use of Snowflake API (Cortex chatbot))*
**Sponsor tools:** Snowflake Cortex (Chatbot answering questions over stored hike data, supporting)
**AI:** Snowflake Cortex LLM answers questions from hike records fetched by the backend; knee angle uses classical sensor fusion, not ML.
**Architecture:** ESP32 with two IMUs streams over Bluetooth to a vanilla JS web app (Chart.js, IndexedDB); Node backend and Supabase store hikes; backend calls Snowflake Cortex for chat.
**Novelty:** Applies two-IMU joint-angle sensing to downhill hiking and pairs raw step logs with an LLM review chat; next step is adaptive filter weighting.
**Scope:** small · working: Working MVP claimed with live Netlify demo; no repo or video listed. · polish: Hardware on breadboards with Velcro straps; app has history graphs; no accuracy tests.
**Claims:** Working MVP measuring knee angle and landing impact | Won Best Sports Analytics
**Gaps:** No repo linked; No video; Demo site not opened; No accuracy figures
Sources: https://devpost.com/software/hiking-sensor, https://stormhacks2026.devpost.com/

---

### SoftWear
*StormHacks StormHacks 2026 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Finalists

**What it is:** A smart jacket with an IMU and LED matrix plus a room camera that confirms a fall and tracks posture, then lights the jacket and shows paramedics a body map of likely impact points, severity and a fall graph. Page was titled Safe Landing.
**Problem / user:** Older adults who fall at home and the paramedics who treat them; the aim is to improve the minutes after a fall rather than prevent it.

**Features**
- IMU fall detection — Jacket-mounted IMU records the fall. *[claimed]*
- Room camera confirmation — Camera confirms the fall and tracks posture afterward. *[claimed]*
- Likely contact estimation — Estimates which body parts hit the floor from fall direction and final position, labelled likely or not measured rather than injury. *[claimed]*
- Jacket LED highlighting — LEDs light the body parts likely injured. *[claimed]*
- Responder dashboard — Body map of likely contact points, impact severity and a fall graph for quick reading. *[claimed]*

**Flow:** Wearer falls in the jacket → IMU records the fall → Room camera confirms and tracks posture → System estimates contact points → Jacket LEDs light affected areas → Responders read the dashboard body map

**Prompt:** not public / not found
**Fit (none):** Finalist listing carries no stated prompt; project is a wearable-plus-camera health device.  *(targeted: Finalists)*
**AI:** none
**Architecture:** ESP32 in the jacket reads IMU and drives LEDs (C firmware); room camera feed and IMU data merge in a Python backend and web front end responder dashboard.
**Novelty:** Pairs a wearable that physically shows likely impact sites with a responder-facing summary, and is careful to claim likely contact instead of diagnosing injury. Uses a room camera; page states no consent or privacy safeguards.
**Scope:** small · working: Video and three screenshots exist but their content is not described; no repo. · polish: Honest-labelling design and research basis stated; no test results.
**Claims:** About 1 in 4 adults over 65 fall each year | Dashboard readable by paramedics in seconds
**Gaps:** No repo linked; Video not watched; no walkthrough on page; Research source for impact locations not named; Camera privacy/consent not addressed
Sources: https://devpost.com/software/safe-landing

---

### SURGE
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Snowflake API

**What it is:** A two-sided flood-response platform. Officials use a dashboard to publish area instructions, see sensor-based risk, plan routes and review resident SOS reports; residents get the latest guidance, map routes to safer destinations, can send reports, and ask a voice or chat assistant.
**Problem / user:** Government emergency teams and flood-affected residents, where official warnings lag changing road and rescue conditions; inspired by Nepal flash floods.

**Features**
- Government dashboard — Publish area-specific instructions, review reports and SOS, track alerts and response activity *[shown_working]*
- Resident app — Shows latest instruction, alert history and mapped evacuation options; submits field reports and SOS *[shown_working]*
- Sensor risk scoring — Simulated rainfall (45%), river level (40%) and soil moisture (15%) normalized into Low to Extreme categories *[shown_working]*
- Route planning — Dijkstra shortest paths to Low-risk destinations respecting travel mode, hazards and blocked roads; Rasuwa and Sunsari planners *[shown_working]*
- Guidance assistant — Chat or voice questions answered from published guidance; Gemini classifies language, ElevenLabs does speech *[claimed]*
- Shared data layer — SQLite locally with optional Snowflake storage for directives, reports and events *[claimed]*
- Guardrail — Assistant does not issue orders; officials stay decision makers *[claimed]*

**Flow:** Official publishes an evacuation directive → Directive appears on resident's phone → Resident asks the voice agent for a summary and next steps → Resident reports blocked road or person needing rescue → Report shows as a located marker on the government dashboard → Officials update routes and the loop repeats

**Prompt:** MLH prize: use the Snowflake APIs to work with industry-leading LLMs on a single account; student 120-day trial, Arduino student kit.
**Fit (implied):** Snowflake serves as the shared cloud data layer for directives, routes, road conditions and reports; the local demo falls back to SQLite.  *(targeted: [MLH] Best Use of Snowflake API)*
**Sponsor tools:** Snowflake (Cloud storage of directives, reports, events (optional via key-pair connector), supporting); Gemini (Language classification, supporting); ElevenLabs (Speech to text and text to speech for residents, supporting)
**AI:** Gemini classifies the resident's language and drives guidance answers; ElevenLabs handles voice. Risk scoring and routing are fixed formulas and Dijkstra, not ML.
**Architecture:** FastAPI backend with SQLite (Snowflake optional) serving HTML/JS gov and resident pages; MapLibre planners over prepared OSM-derived datasets; sensor JSON files; provider integrations optional.
**Novelty:** Closed two-way loop between officials and residents with voice assistant, plus offline-capable route planners on real Nepal region road data.
**Scope:** medium · working: About 11,000 LOC with pytest, Node and Playwright tests; live demo on Render; runs locally without API keys. · polish: Detailed README, multiple pages, seeded sample data, demo video.
**Claims:** Directives propagate to residents in real time | Local demo runs without keys
**Gaps:** video not watched; Devpost says Next.js but repo shows plain HTML/JS front end
Sources: https://devpost.com/software/surge-u2vh86, https://github.com/awang1809/surge-stormhacks, https://stormhacks2026.devpost.com/

---

### ToughCrowd
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best Beginner; Best Highschool Hack

**What it is:** A pitch-practice web app: upload slides or describe your project, pick an AI judge panel and difficulty, answer questions out loud, and get a score, pass/fail checks and measured delivery stats. Judges can interrupt, and a timed full run-through is included.
**Problem / user:** Students and teams preparing for hackathon judging, class talks, defenses or demo days who rarely practise the hard questions.

**Features**
- Project intake — Upload slide PDF (pictures and charts read once by a vision model), speak, fill a form or paste text. *[shown_working]*
- Judge panel — Four judges (Investor, Grandma, Engineer, Teacher) with distinct ElevenLabs voices, plus custom judges. *[shown_working]*
- Spoken Q&A with feedback — Judge asks aloud, user answers aloud; gets score, what worked, four pass/fail checks and a follow-up question. *[shown_working]*
- Measured delivery stats — Verbatim ElevenLabs Scribe transcript; own code counts fillers, words per minute and pauses over 2 seconds. *[shown_working]*
- Interrupting judges — Rambling triggers a spoken cut-in and a 15-second wrap-up; tougher judges interrupt sooner. *[shown_working]*
- Full run-through — Timed pitch (for example 3 minutes) then 1 minute rapid-fire questions. *[shown_working]*
- Scenarios and difficulty — Hackathon, class, thesis, demo day or elevator pitch; Friendly to Brutal slider. *[shown_working]*
- Progress tracking — Last sessions kept in the browser to compare scores and filler counts. *[claimed]*

**Flow:** Give the project via slides, voice, form or text → Slides are summarised once → Pick judges, difficulty and occasion → Choose Q&A or full run-through → Answer aloud while judge may interrupt → Review score, checks, follow-up and annotated transcript

**Prompt:** Best Beginner (project by at least 50% first-time hackers) and Best Highschool Hack (majority, at least 60%, high schoolers): event-run categories with no theme beyond team composition.
**Fit (implied):** Page tells an origin story of two ninth-graders freezing at a judge question; neither prize is claimed on the page and team status is not stated beyond the prize.  *(targeted: Best Beginner, Best Highschool Hack)*
**Sponsor tools:** ElevenLabs (text-to-speech and Scribe) (Judge voices and verbatim timestamped transcription, core); .Tech Domain (toughcrowd.tech demo domain, token)
**AI:** Gemini 2.5 Flash via OpenRouter reads slide images once; a Claude model via OpenRouter writes questions and grades answers, chosen after side-by-side tests; ElevenLabs voices and transcription.
**Architecture:** Framework-free HTML/JS page with pdf.js; five Node functions on Vercel (slides, questions, speak, transcribe, feedback) hold keys; summary reused per request; mock mode runs without keys.
**Novelty:** Delivery metrics computed by code from word timestamps rather than guessed by an LLM; interrupting judges and custom panels; prefetches next question audio during an answer.
**Scope:** small · working: Live Vercel and toughcrowd.tech demos, video, five working API functions; ~5k LOC. · polish: Detailed README with flow diagram, mock mode, passcode, model comparison.
**Claims:** Delivery stats measured from word timestamps, not estimated | Model picked by testing four models on same inputs
**Gaps:** Team school status and first-time status not stated; Judge model named on Devpost as a Claude version; not independently verified
Sources: https://devpost.com/software/toughcrowd, evidence/stormhacks-stormhacks-2026-toughcrowd.json

---

### WeCare
*StormHacks StormHacks 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best MedTech; WiCS - WiCS Cosmos Track

**What it is:** A Raspberry Pi puppy-shaped pill-reminder device that speaks personalised dose reminders, confirms doses by a touch sensor, checks pill bottles with a webcam and Gemini vision, and logs events to a caregiver mobile app.
**Problem / user:** Seniors on many medications, often with low digital literacy, and the family caregivers who need to know whether doses were taken.

**Features**
- Spoken reminders — APScheduler fires scheduled reminders using the senior name and caregiver notes, voiced with ElevenLabs. *[shown_working]*
- Touch confirmation — Capacitive touch tap plays a jingle and logs the dose as taken; repeat reminders then missed status. *[shown_working]*
- Bottle scanning — Webcam captures label; Gemini vision says due now, later or already taken, with a confidence level. *[shown_working]*
- Refusal to guess — Unknown or unreadable meds get an I am not sure message; never calls a medication safe, only matching the schedule. *[claimed]*
- Cloud logging — Reminders, confirmations, misses and scans logged to the cloud. *[shown_working]*
- Caregiver app — Expo React Native app for setting medications and schedules, with taken, upcoming and missed views and a first-responder overview. *[shown_working]*
- Alerts, refills and multilingual support — Phone alerts for missed doses, refill reminders, weekly summaries, languages. *[planned]*

**Flow:** Caregiver sets up meds and schedule in the app → Device speaks a reminder at dose time → Senior taps the puppy to confirm → No tap leads to a repeat and then missed → Senior shows an unfamiliar bottle to the camera → Caregiver reviews events in the app

**Prompt:** Best MedTech: best project supporting medical technology. WiCS Cosmos Track: entire team identifies as women, non-binary or another gender minority; no theme stated.
**Fit (implied):** Addresses medication adherence for seniors with a device plus caregiver app; WiCS track is a team-composition track and the page does not tie the project to it.  *(targeted: Best MedTech, WiCS - WiCS Cosmos Track)*
**Sponsor tools:** Gemini API (Vision reading of medication bottle labels, core); ElevenLabs (Spoken reminders, core)
**AI:** Gemini vision reads a bottle image, matches it to the medication schedule and returns structured results with confidence, with retries and a fallback model; ElevenLabs text-to-speech for voice.
**Architecture:** Raspberry Pi Python software with touch sensor GPIO, USB webcam and Bluetooth speaker in a 3D-printed puppy; Firebase cloud logs; Expo React Native app (original Next.js prototype also in repo).
**Novelty:** Friendly physical form factor with a deliberately cautious scan response; repo includes both a native app and a device folder.
**Scope:** medium · working: Demo video, repo with mobile app, device folder and tests; Devpost says the device loop works end to end, app not yet linked to live device data. · polish: 3D-printed enclosure, Figma designs, three app screenshots; ~9k LOC.
**Claims:** Full device loop works end to end with live cloud update | Scan catches wrong-time and already-taken mistakes | Cites 1 in 4 Canadian seniors on 10+ medications
**Gaps:** README covers the app and mentions device only as a folder; app uses Cephalexin sample catalog and is not yet linked to device data; No adherence or accuracy testing
Sources: https://devpost.com/software/carebot-q8x3t6, evidence/stormhacks-stormhacks-2026-wecare.json

---

### WhatDaDogDoing
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Huawei Custom Challenge #2 - Fetching Reality

**What it is:** Photograph a dog and about 40 seconds later a rigged, furry 3D copy appears in phone AR, wandering, sniffing, eating dropped treats and fetching a thrown ball. A laptop server makes the model; the phone browser renders it.
**Problem / user:** Dog owners wanting a realistic virtual dog in their own room; built directly to the Huawei Fetching Reality brief.

**Features**
- Single-photo 3D dog — Server uses a Vision Transformer to make a mesh, fits a dog skeleton and grows about 156K fur strands in roughly 40 seconds. *[claimed]*
- Autonomous behaviour — Dog wanders, sniffs, sits, lies down and walks around furniture using motion matching on 41 minutes of dog mocap at 60 Hz. *[claimed]*
- Interaction — Tap to call the dog, drop treats to eat, throw a ball to fetch, pet by touching the screen. *[claimed]*
- Room-aware AR — Phone AR scan and depth give obstacle-aware path planning, occlusion and shadows; Android AR, iPhone camera-and-gyro view. *[claimed]*
- Multi-user rooms — Several users at once, each with their own dog and room, from any network via tunnel. *[claimed]*
- Persistent rooms and friends meeting — Remember rooms and let friends dogs meet. *[planned]*

**Flow:** Take a photo of a dog → Wait about 40 seconds for generation → Open the AR route on the phone → Dog appears in the room camera view → Call, feed, throw a ball for, and pet the dog

**Prompt:** Huawei Custom Challenge #2 Fetching Reality: turn a static dog photo into a real-time interactive digital pet that responds, interacts with its environment or plays; SDFs, Gaussian splatting and AI tools encouraged.
**Fit (explicit):** Page states it answers the brief of a one-photo 3D dog living in the real room, with fur, mocap-driven movement, fetch and AR; chose a single-shot pipeline rather than Gaussian splatting.  *(targeted: Huawei Custom Challenge #2 - Fetching Reality)*
**AI:** Vision Transformer photo-to-3D mesh, skeleton fitting and fur growth on laptop CPU; motion matching over dog mocap drives behaviour; tags also list dinov2 and stable diffusion without explanation.
**Architecture:** Python server on a laptop generates the dog and plans paths; TypeScript/three.js/React client on Vercel renders fur, occlusion and shadows on the phone; WebSockets via a Cloudflare tunnel.
**Novelty:** Runs a full photo-to-animated-fur-dog pipeline without a GPU and ships obstacle-aware AR behaviour, with measured fixes for phone memory limits.
**Scope:** medium · working: Live /ar demo link depends on a laptop tunnel; no video; repo unreadable. · polish: Detailed technical writeup of challenges and numbers; multi-user support claimed.
**Claims:** About 40 seconds from photo to generated dog | Motion selection 60 times per second from 41 minutes of mocap | About 156K fur strands
**Gaps:** Repo clone failed and README fetch failed; Demo depends on a laptop tunnel and was not opened; No video
Sources: https://devpost.com/software/whatdadogdoing, https://stormhacks2026.devpost.com/

---

### Why Did We Choose This Tech?
*StormHacks StormHacks 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best .Tech Domain Name

**What it is:** A team workspace (whydidwechoosethis.tech) that turns planning conversations, by text or voice, into versioned architecture decision records with provenance. A GitHub bot checks pull requests against published decisions, and coding agents read them through an MCP server.
**Problem / user:** Software teams, especially multi-repo ones, whose design reasoning is scattered and whose AI coding agents add unagreed scope.

**Features**
- Conversational planning — Assistant (Gemini via OpenRouter) questions assumptions and drafts an ADR from a text or voice chat *[shown_working]*
- Project workspaces — Create projects, connect GitHub repositories, invite teammates to discuss proposals *[shown_working]*
- Versioned publishing — Publish agreed decision as stable version while draft continues to change *[shown_working]*
- Provenance and decision history — Each revision links back to the conversation that produced it *[shown_working]*
- GitHub PR review bot — Checks pull requests against published decisions and flags contradictions *[shown_working]*
- MCP server — Controlled document access for coding agents via Model Context Protocol on a Cloudflare Worker *[shown_working]*
- Linear and Slack integrations — Links decisions to tickets and discussions *[claimed]*
- Voice planning — ElevenLabs voice conversations about documents *[shown_working]*

**Flow:** Log in with WorkOS → Create project and connect repos → Discuss plan with assistant by text or voice → Assistant drafts ADR → Teammates join the discussion → Publish agreed version → Bot reviews PRs and agents read via MCP

**Prompt:** MLH prize: win a .Tech domain name for up to 10 years to showcase and expand a project; desktop microphone.
**Fit (explicit):** Product is branded and deployed on whydidwechoosethis.tech (alt wdwct.tech), so the domain name is the project's identity.  *(targeted: [MLH] Best .Tech Domain Name)*
**Sponsor tools:** .Tech domain (Product's public address, core); ElevenLabs (Voice planning conversations, supporting)
**AI:** Gemini via OpenRouter AI SDK drives planning and reasoning, drafts ADRs and reviews PRs against decisions; ElevenLabs gives voice; MCP exposes decision documents to agents.
**Architecture:** vinext/React app on Cloudflare Workers with Postgres (Drizzle), WorkOS auth, realtime and MCP apps in a pnpm monorepo, GitHub, Linear and Slack integrations.
**Novelty:** Decision-provenance tracking and agent-facing MCP plus PR enforcement make a full product loop; large monorepo with Nix dev environment and CI.
**Scope:** large · working: About 50,000 LOC, 574 files; live site; Devpost says a real PR review was grounded in a published ADR. · polish: Docs directory, CI, tests, eight screenshots, video, Nix setup.
**Claims:** Linear and Slack integrations completed beyond stretch goals | Full loop demonstrated with a real PR review
**Gaps:** video not watched
Sources: https://devpost.com/software/why-did-we-choose-this-tech, https://github.com/rockydotsystems/stormhacks2026, https://stormhacks2026.devpost.com/

---

