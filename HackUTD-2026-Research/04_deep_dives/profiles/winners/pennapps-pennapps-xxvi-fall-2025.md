# PennApps — PennApps XXVI (Fall 2025) (4 projects)

### Dispatch
*PennApps PennApps XXVI (Fall 2025) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Place Overall [2nd]

**What it is:** A browser-based auxiliary monitor for 911 dispatchers that transcribes a call live, summarizes the incident, classifies it as police, fire or medical with a priority, suggests what to ask next and keeps a call queue with a time-to-dispatch timer.
**Problem / user:** 911 dispatchers who must listen, type and recall protocols under stress; author cites a slow, chaotic 911 experience after a robbery.

**Features**
- Live call transcription — Browser Web Speech API converts speech to text as the call proceeds. *[shown_working]*
- Incident summarizer — Local Ollama (llama3.2) analyzes the transcript into a structured brief; mock responses used if Ollama is absent. *[shown_working]*
- Suggested script and questions — Generates dispatcher prompts based on conversation context and protocol patterns. *[shown_working]*
- Classification and priority — Assigns police, fire or medical plus urgency, grounded in NYC, Seattle and NENA datasets. *[shown_working]*
- Call queue and history — Active calls ranked by risk, completed calls retained; time-to-dispatch timer. *[shown_working]*
- JSON/PDF export — Incident data downloadable. *[claimed]*
- Stress detection and multilingual translation — Listed on Devpost; no detail or README support. *[claimed]*

**Flow:** Open dashboard and start a call → Speech is transcribed live → AI produces brief, category and priority → Call joins ranked queue → Dispatcher follows suggested questions and exports incident

**Prompt:** PennApps XXVI overall prizes judged on technology difficulty, design, completion (does it work) and learning; no theme text.
**Fit (none):** Working live dashboard with local LLM and real datasets; no explicit prize targeting.  *(targeted: 2nd Place Overall)*
**AI:** Local Ollama llama3.2 for summaries and suggested scripts, with rule-based classification calibrated on public 911 datasets and mock fallback; browser speech recognition for STT.
**Architecture:** Static web app (vanilla/Next frontend deployed on Vercel) using Web Speech API, optional local Ollama server, and bundled datasets for classification; all processing local.
**Novelty:** Runs privately in the browser with local LLM and public dispatch datasets, in a high-stakes domain with dispatcher-facing queue and timer.
**Scope:** small · working: 22 files, about 6k LOC (partly data), live Vercel demo link and README. · polish: Landing, demo and queue pages; no tests; no video.
**Claims:** Seconds saved equal lives saved | All data processed locally | Priority scoring grounded in Seattle and NYC data
**Gaps:** no video; no accuracy or latency metrics; stress detection and translation not evidenced in README
Sources: https://devpost.com/software/dispatch-evf2sq, https://github.com/us-abdullah/dispatch10, https://pennapps-xxvi.devpost.com/

---

### Intention.ai
*PennApps PennApps XXVI (Fall 2025) · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Best Beginner Hack (>2 members first time)

**What it is:** Intention.ai is a Chrome extension plus web dashboard that uses the webcam and face-api.js to classify a student as focused, tired or stressed, logs focus patterns and has Gemini suggest breaks. It processes camera video of the user, who enables it via a toggle.
**Problem / user:** High-achieving students losing focus while studying.

**Features**
- Webcam state detection — face-api.js landmarks and heuristics (blink, slouch, tilt) classify focused/tired/stressed in the browser. *[claimed]*
- Chrome extension toggle — Turn tracking on or off. *[claimed]*
- Gemini suggestions — Context-aware break and focus recommendations with fallback logic. *[claimed]*
- Trend dashboard — Next.js dashboard with focus patterns and longest focus stretch, JWT auth, MongoDB. *[claimed]*

**Flow:** Enable extension → Webcam tracks state while studying → Extension logs patterns → Gemini advises → Review dashboard

**Prompt:** not public / not found
**Fit (none):** Page states Best Beginner Hack win; no prize text cached.  *(targeted: Best Beginner Hack (>2 members first time))*
**Sponsor tools:** Google Gemini API (personalised productivity recommendations, supporting)
**AI:** Browser CV with face-api.js; Gemini prompts for suggestions with refinement.
**Architecture:** Chrome extension and Next.js/React app, TypeScript REST API, MongoDB.
**Novelty:** Webcam-based focus classification in-browser with micro-signals.
**Scope:** small · working: Demo video embedded; no repo or live link. · polish: Dashboard described; no metrics.
**Claims:** Real-time emotion detection | Tagline 64% of students struggle with focus
**Gaps:** No repo; No official beginner prize text; Privacy handling of webcam not stated
Sources: https://devpost.com/software/pennapps-f2k83a, prompts_cache/pennapps-xxvi-fall-2025.md

---

### kinemo
*PennApps PennApps XXVI (Fall 2025) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 1st Place Overall [1st]

**What it is:** A Python motion-controlled two-player game console that needs only a laptop webcam. Hand gestures navigate the menu and body pose tracking drives three games: Boxing, Flying Fruits and Reaction Time.
**Problem / user:** Groups of friends wanting party games without Kinect-style hardware; began as a boxing motion tracker for AI feedback.

**Features**
- Gesture-controlled menu — Hand tracking library moves the cursor to pick a game; one hand may need to be hidden. *[shown_working]*
- Boxing — Punch, kick, weave from pose tracking; 12 hearts, punch 1 and kick 3 damage, timed weave stun, 0.5s cooldown. *[shown_working]*
- Flying Fruits — 30-second slicing round: fast hand swipes through fruit score +1, bombs cost 5, slice angle animated. *[shown_working]*
- Reaction Time — Players raise both hands after a green light; moving early gives opponent the point. *[shown_working]*
- Two-player pose tracking — MediaPipe pose estimation on one webcam feed tracks both players; NumPy computes velocities. *[shown_working]*
- Post-match stats — Statistics screen shown after a match (screenshot). *[claimed]*

**Flow:** Stand a few feet from webcam → Pick a game with hand gestures → Two players compete → See results and stats

**Prompt:** PennApps XXVI overall prizes judged on technology difficulty, design, completion (does it work) and learning; no theme text.
**Fit (none):** Complete, playable multi-game product from commodity hardware; no explicit prize targeting.  *(targeted: 1st Place Overall)*
**AI:** MediaPipe pose estimation and a hand-tracking library supply landmarks; game logic uses hand-coded velocity and timing rules. No generative AI shipped.
**Architecture:** Single Python app: OpenCV webcam capture into MediaPipe, NumPy motion math, Pygame rendering and audio, with per-game modules.
**Novelty:** Console-style multi-game experience from only a webcam, with tuned combat rules, rather than a single tech demo.
**Scope:** small · working: 43 files, about 1.7k LOC, README with run steps and game rules; no video or live link. · polish: Menu, three games with detailed rules, assets and audio; no tests.
**Claims:** Built in 36 hours (README) or under 48 hours (Devpost) | Only a laptop camera needed
**Gaps:** no demo video; no performance metrics
Sources: https://devpost.com/software/kinemo, https://github.com/arvinmefsha/kinemo, https://pennapps-xxvi.devpost.com/

---

### OverSEA
*PennApps PennApps XXVI (Fall 2025) · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place Overall [3rd]

**What it is:** A maritime monitoring dashboard that cross-checks Sentinel-1 radar vessel detections against AIS broadcasts to find untracked fishing vessels, plots them and predicted hot spots on a 3D globe, and offers Gemini and Exa agents for reports and maritime-law research.
**Problem / user:** Coast guards and maritime enforcers with huge patrol areas and limited resources against untracked illegal fishing; clearance-level login suggests agency staff.

**Features**
- Untracked vessel detection — Global Fishing Watch SAR detections are compared with AIS; unmatched points stored in MongoDB. *[shown_working]*
- 3D interactive globe — Mapbox globe shows vessel points and hot spots with one-click detail; tens of thousands of points rendered. *[shown_working]*
- Hot spot prediction — SciPy density clustering with risk factors including port proximity, fishing season and influence decay. *[claimed]*
- Clearance-based access — Auth0 roles gate tracked vs untracked views and the AI agent to Confidential and above. *[shown_working]*
- Gemini research agent — Gemini suggests actions, using Exa to research maritime law at each vessel's coordinates. *[shown_working]*
- Environmental impact report — Gemini estimates illegal fishing impact over a user-chosen period. *[claimed]*
- Chat agent — Conversational helper to prioritize regions; prompts and replies stored in MongoDB. *[claimed]*

**Flow:** Log in via Auth0 → View globe of vessel activity → Click vessel or hot spot → Ask agent for law research or suggestions → Generate an impact report

**Prompt:** PennApps XXVI overall prizes judged on technology difficulty, design, completion (does it work) and learning; no theme text.
**Fit (none):** Real satellite data pipeline with 3D UI and agents; no explicit prize targeting.  *(targeted: 3rd Place Overall)*
**Sponsor tools:** Exa (researching maritime law at vessel coordinates, supporting); Auth0 (clearance-level roles and permissions, supporting); MongoDB (vessel results pipeline and agent history, core); Google Gemini (agent, reports, chat, core)
**AI:** Gemini agent, report writer and chat grounded with Exa search results; SciPy density clustering and multi-factor risk scoring for hot spots.
**Architecture:** Python backend pulls Global Fishing Watch SAR and AIS data, clusters and stores results in MongoDB; Next.js frontend with Mapbox globe, Auth0 and Gemini/Exa agent calls.
**Novelty:** Uses open satellite radar and AIS cross-matching with role-gated agent tooling, tying real geospatial data to a decision workflow.
**Scope:** medium · working: 185 files, about 11k LOC including raw SAR sample data; screenshots of landing, dashboard and console. · polish: 3D UI, auth tiers, architecture screenshots; no tests, video or live link.
**Claims:** 72-76% of industrial fishing vessels are not publicly tracked | Handles tens of thousands of points on the globe
**Gaps:** no video; no detection accuracy; clustering validity unmeasured
Sources: https://devpost.com/software/oversear, https://github.com/spicybigmac/pennapps, https://pennapps-xxvi.devpost.com/

---

