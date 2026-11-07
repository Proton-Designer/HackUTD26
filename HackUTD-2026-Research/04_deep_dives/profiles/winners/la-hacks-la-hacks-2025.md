# LA Hacks — LA Hacks 2025 (20 projects)

### AERIS
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best of Groq

**What it is:** Autonomous Emergency Response and Intelligence System: a dashboard pipeline that ingests live DJI drone video, detects people and hazards with a custom YOLOv8 model, triages victims with Groq-hosted LLaMA, and uses Dain agents to find hospitals and place Twilio calls.
**Problem / user:** Search-and-rescue teams in disasters where victims lose phone service and rescuers search blindly for hours.

**Features**
- Live drone video ingest — Dockerized NGINX RTMP server plus FFmpeg receive the DJI feed and pass frames to the backend. *[claimed]*
- Victim and hazard detection — FastAPI endpoints run a custom Ultralytics YOLOv8 model trained on disaster datasets for humans, fire, smoke, flood, debris and collapse. *[claimed]*
- LLM triage — Groq-hosted LLaMA ranks detected victims by urgency. *[claimed]*
- Command dashboard — Next.js with Leaflet map shows victim and hazard pins from Supabase real-time events. *[claimed]*
- Hospital lookup and calls — Dain agents find nearest hospitals to pinned coordinates with numbers and distances and automate Twilio calls. *[claimed]*
- Responder dispatch and safe routing — Responders sent to victim coordinates along routes avoiding obstacles; full autonomy listed as future. *[claimed]*

**Flow:** Drone streams video to RTMP server → Frames reach FastAPI and YOLOv8 detects victims and hazards → Groq LLaMA triages by urgency → Results logged to Supabase and shown on map → Dain agents find hospitals and call via Twilio → Responders directed to coordinates

**Prompt:** Build a creative, interactive multimodal app powered by Groq; judged on how many modalities Groq powers (text, vision, audio), innovation on a real-world problem, UX and design.
**Fit (implied):** Groq-hosted LLaMA triages victims inside a pipeline that also uses vision (YOLOv8 on video) and voice calls via Twilio; Groq powers text only per the README. README does not state the prize target.  *(targeted: Best of Groq)*
**Sponsor tools:** Groq (LLaMA) (Victim triage by urgency, core); Dain Protocol and Butterfly (Mission-control agents and hospital coordination, supporting); Twilio (Automated emergency calls, supporting)
**AI:** Custom YOLOv8 object detection on frames; Groq LLaMA for triage text; Dain agents orchestrate hospital lookup and calls.
**Architecture:** DJI feed to NGINX RTMP and FFmpeg to FastAPI CV service writing to Supabase; Next.js dashboard subscribes; Dain hospital and report services call Twilio.
**Novelty:** Combines drone video, hazard detection, LLM triage and agent-placed phone calls in one rescue dashboard.
**Scope:** small · working: Repo about 1.8k LOC with frontend, backend, hospital and report services; no video or live demo; page gives no metrics. · polish: Three screenshots; emoji-styled README; no setup steps.
**Claims:** Over 60% of disaster victims lose phone service (motivating statistic) | Gets responders to critical victims faster than traditional teams (unmeasured)
**Gaps:** No video or demo; Unclear whether drone flight was live in the demo
Sources: https://devpost.com/software/aeris-ej7d9k, evidence/la-hacks-la-hacks-2025-aeris.json, prompts_cache/la-hacks-2025.md, https://la-hacks-2025.devpost.com/

---

### AI Escape
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** ROBLOX Civility Challenge: Building A Better Digital World

**What it is:** A Roblox escape-room game in which the player wakes in a haunted house and solves puzzles, quizzes and mini-games about AI literacy and cybersecurity to unlock keys and escape.
**Problem / user:** Players of all ages who need approachable lessons on responsible AI use, data privacy, bias, misinformation and security risks.

**Features**
- Story-driven escape room — Player wakes in a house and progresses through rooms by solving puzzles toward escape. *[shown_working]*
- AI literacy quizzes — Challenges cover what AI is, data privacy and algorithmic bias, written for all ages. *[shown_working]*
- Key-unlocking mini-games — Each mini-game completed unlocks a key needed to exit. *[shown_working]*
- Security and ethics content — Lessons on misinformation, ethical AI use and security vulnerabilities embedded in the puzzles. *[claimed]*

**Flow:** Spawn in the house on Roblox → Solve puzzles and answer AI quizzes → Complete mini-games to earn keys → Use keys to escape

**Prompt:** Use Roblox Cube, Roblox's generative AI for 3D and 4D, to build experiences that teach others about online safety and well-being; cash prizes for four winners.
**Fit (implied):** Educational Roblox game about AI literacy and digital safety. The page does not mention Roblox Cube, so use of the required generative tool is unconfirmed.  *(targeted: ROBLOX Civility Challenge: Building A Better Digital World)*
**Sponsor tools:** Roblox Studio (Building the game in Lua, core)
**AI:** none
**Architecture:** Single Roblox experience written in Lua in Roblox Studio; curriculum content authored by the team; no backend described.
**Novelty:** Teaches AI and cybersecurity concepts through an escape-room format on Roblox; built by two developers new to Roblox Studio and Lua.
**Scope:** small · working: Published Roblox game link and embedded video; page calls it almost fully functioning; no repo. · polish: No metrics or screenshots verified; stages changed several times.
**Claims:** Game described as almost fully functioning
**Gaps:** No repo linked; Game and video not played or watched; Use of Roblox Cube not mentioned; Project ID suggests team or project aliases (uncblox, bloom ai, kindness maxxing); not resolved
Sources: https://devpost.com/software/ai-escape, https://la-hacks-2025.devpost.com/

---

### Alto
*LA Hacks LA Hacks 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Overall: 1st Place [1st]; Track: AI Agents League (Fetch.ai)

**What it is:** A multi-agent pipeline for mobile bug triage. It ingests a bug report, pulls related code from GitHub, asks Gemini for root-cause hypotheses, generates a Maestro UI script to reproduce the bug, and posts the findings to Slack.
**Problem / user:** Mobile developers and QA teams who lose time diagnosing and reproducing app bugs.

**Features**
- ExtractorAgent — Classifies bug type, priority and error source from a report using ASI-1 mini *[claimed]*
- TriageAgent — Fetches relevant repo code with the gitingest library run locally *[shown_working]*
- HypothesisAgent — Gemini proposes root causes, code locations and severity *[shown_working]*
- MaestroGenAgent — Generates Maestro YAML scripts replicating bug steps (experimental) *[claimed]*
- ReplicatorAgent — Runs the script locally to confirm the bug reproduces *[claimed]*
- NotifierAgent — Posts hypotheses, severity and replication status to Slack via webhook *[shown_working]*
- GatewayAgent — Flask REST endpoint lets CI/CD or external systems trigger the workflow *[shown_working]*

**Flow:** Bug report arrives from Instabug or via gateway API → Agents extract and classify it → Relevant code is fetched → Gemini generates hypotheses and a Maestro script → Replication is attempted → Results post to Slack

**Prompt:** Fetch.ai AI Agents League: build agents that reason with the ASI1-Mini LLM using the uAgents framework or Fetch.ai SDK, in areas such as healthcare, education, finance or sustainability; sub-prizes for vertical impact, ASI-1 Mini use and multi-agent systems.
**Fit (explicit):** Seven uAgents-framework agents registered with Agentverse form a debugging workflow, with ASI-1 mini in the extractor step and Gemini elsewhere. Vertical is developer tooling rather than the listed domains.  *(targeted: Fetch.ai AI Agents League, Overall)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (Agent framework and registry for all seven agents, core); ASI-1 mini (Bug classification in ExtractorAgent, supporting)
**AI:** Gemini (flash and 2.5 pro preview) for hypotheses and Maestro YAML with JSON-constrained prompts; ASI-1 mini for classification; multi-agent message passing.
**Architecture:** uAgents in Python communicate with typed models; Flask gateway thread bridges to the agent loop; gitingest for repo context; Instabug input, Slack output.
**Novelty:** Chains bug ingestion to automatic reproduction script generation inside an agent mesh; replication reliability is the experimental part.
**Scope:** medium · working: Claims end-to-end prototype and has a Vercel demo link; screenshots of landing page and Slack post; no metrics. · polish: Landing page deployed; no video listed.
**Claims:** End-to-end prototype from gateway to Slack notification
**Gaps:** GitHub repo not retrievable (clone failed, fetch failed); No video
Sources: https://devpost.com/software/alto, https://la-hacks-2025.devpost.com/

---

### Bandaid Maps
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Melissa Data Challenge

**What it is:** A web app that takes a latitude and longitude, scores nearby healthcare access from 0 to 100 using Melissa location data, asks Gemini for a tailored emergency action plan, and shows nearby care locations on a map.
**Problem / user:** Students, travelers and residents who want to know how prepared their location is for medical emergencies before one happens.

**Features**
- Health Readiness Score — Scores 0-100 from proximity to trauma centers, urgent care, pharmacies and mental health services. *[shown_working]*
- Gemini emergency action plan — Gemini Pro writes a plan based on the readiness level and available nearby care. *[shown_working]*
- Interactive care map — React Leaflet map shows nearby healthcare locations. *[shown_working]*
- Symptom-aware recommendations — Optional feature suggesting care types by symptoms. *[claimed]*
- Emergency mode — Optional filter for 24/7 services. *[claimed]*

**Flow:** Enter current latitude and longitude → App computes Health Readiness Score → Gemini generates action plan → Map displays nearby healthcare locations

**Prompt:** Using the Melissa UCLA dataset, plot data on a map and build a solution finding the nearest relevant locations for a community problem, optimizing proximity with Melissa APIs.
**Fit (explicit):** Uses Melissa location data to find nearby care and rank readiness by proximity, displayed on a map. README names Melissa as the data source for the readiness score.  *(targeted: Melissa Data Challenge)*
**Sponsor tools:** Melissa APIs (Location data for nearby healthcare services, core); Google Gemini Pro (Emergency action plan text, supporting)
**AI:** Gemini Pro generates a personalized action plan from the computed score and nearby services; scoring itself is distance-based.
**Architecture:** React frontend with Leaflet map calls a FastAPI backend that queries Melissa and MongoDB, computes the score and calls Gemini.
**Novelty:** Frames care-access as a preparedness score for an arbitrary location rather than a symptom-triggered finder.
**Scope:** tiny · working: Repo about 400 LOC with demo video link; no live site; inputs are raw coordinates. · polish: Short README; mismatch (Streamlit versus React/FastAPI) suggests an earlier prototype.
**Claims:** Score uses proximity to trauma centers, urgent care, pharmacies and mental health services
**Gaps:** Video not watched; README and Devpost mention Streamlit while stack lists FastAPI and React; No challenges or next steps on page
Sources: https://devpost.com/software/bandaid-maps, evidence/la-hacks-la-hacks-2025-bandaid-maps.json, https://la-hacks-2025.devpost.com/

---

### Cena Can See
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Google Gemini: Chase the Future!

**What it is:** A zero-shot control pipeline for a Nao humanoid robot: spoken commands and the robot's camera go to Gemini, which breaks tasks into subtasks, locates objects with bounding boxes and segmentation, and calls low-level walking and arm functions to clean spills or sort items.
**Problem / user:** Aimed at making household-capable humanoid robots feasible without costly reinforcement-learning policy training; no specific end user named.

**Features**
- Voice command intake — Robot's microphone captures spoken tasks such as clean up the table or sort kitchen items. *[claimed]*
- Task decomposition — Gemini splits a command into subtasks (walk, reach, grasp) and judges the best approach for each. *[claimed]*
- Object perception — Gemini spatial understanding gives bounding boxes and segmentation for spills and cleaning items from the RGB camera. *[shown_working]*
- Tool ranking and trash handling — Scans for cleaning items, prefers paper towels and cloths over brushes, and separates trash from keepers. *[claimed]*
- Pixel-to-joint motion — Camera pixel coordinates mapped to robot frame and joint angles by inverse kinematics after calibration. *[shown_working]*
- Function-calling robot control — Gemini function calls trigger a custom walking and arm controller on the Nao. *[shown_working]*
- Custom firmware flashing tools — Built after a firmware failure bricked the robot. *[claimed]*

**Flow:** User speaks a task → Robot captures the scene → Gemini identifies objects and ranks tools → Task split into walk, reach, grasp subtasks → Gemini function calls move the robot → Screenshots show reaching for gummies and spill segmentation

**Prompt:** Gemini 2.0/2.5 APIs must be the core component; judged on multimodal input, advanced reasoning, code generation, personalization or real-time conversation.
**Fit (explicit):** Gemini provides perception, spatial reasoning, task planning and function calling for the robot, so it is the central component; page names the prize it won.  *(targeted: Google Gemini: Chase the Future!)*
**Sponsor tools:** Google Gemini API (Multimodal understanding, spatial reasoning, bounding boxes, function calling to robot controls, core)
**AI:** Gemini multimodal model plans subtasks, detects and segments objects zero-shot from camera images, and issues function calls; classic inverse kinematics handles motion.
**Architecture:** Nao robot (Python 2.7 controller, camera, microphone) linked to Gemini API for perception and planning; coordinate transform and IK layer; custom firmware tools.
**Novelty:** Avoids RL and imitation learning by using a general multimodal model on an old Nao platform with custom walking and arm control.
**Scope:** small · working: Page shows screenshots of reaching, walking toward an object and segmentation; repo has about 1.5k LOC in 3 code files; no video or metrics. · polish: Repo README contains only a link back to Devpost; no setup steps.
**Claims:** Complete robot foundation pipeline for embodied AI built in a short time | Operates zero-shot without RL or imitation learning
**Gaps:** Repo README is a link only; No video; No success rates; which tasks worked end to end is unclear
Sources: https://devpost.com/software/cena-can-see, evidence/la-hacks-la-hacks-2025-cena-can-see.json, prompts_cache/la-hacks-2025.md

---

### Delphi
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Track: Heart of The Matter

**What it is:** A voice-driven browsing assistant for blind users built as four Fetch.ai agents on Gemini 2.0 Flash: a voice agent, an orchestrator, a browser-use agent that acts on websites, and a vision agent that narrates what is on screen.
**Problem / user:** Blind and visually impaired computer users who juggle tabs, shortcuts and changing interfaces; inspired by a blind friend.

**Features**
- Hermes voice agent — Gemini 2.0 Flash Live converses with the user, identifies intents and confirms actions aloud. *[claimed]*
- Zeus orchestrator — Gemini-powered planner holds task state with memory and a queue, delegates to other agents. *[claimed]*
- Athena browser agent — browser-use running Gemini executes clicks, keystrokes and navigation on any website. *[claimed]*
- Theia vision agent — Gemini vision reads screenshots to find landmarks and UI elements and narrates results. *[claimed]*
- Spoken feedback — Text-to-speech reads responses and results aloud. *[claimed]*
- Modular agent network — Each agent is a separate uAgent on Agentverse so parts can be swapped independently. *[claimed]*

**Flow:** Open browsefor.us → Speak a request to Hermes → Hermes confirms intent → Zeus plans and delegates → Theia reads the screen; Athena acts in the browser → Theia narrates the result aloud

**Prompt:** Heart of the Matter (healthcare track): mental wellness platforms, diagnostics, fitness apps and related health tools.
**Fit (implied):** Accessibility tool for visually impaired users; the page names the track as won but does not explain the healthcare link. Also uses Fetch.ai uAgents (another LA Hacks sponsor).  *(targeted: Track: Heart of The Matter)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (Hosting the four cooperating agents, core); Google Gemini 2.0 Flash (All four agents including live voice and vision, core)
**AI:** Gemini 2.0 Flash for planning, live voice and screenshot vision; browser-use drives the browser; multi-agent split with orchestrator.
**Architecture:** Next.js frontend connects to Python backend of Fetch.ai agents (Zeus, Hermes, Athena, Theia) using Gemini and browser-use, over websockets.
**Novelty:** Splits voice, planning, browsing and narration into four named agents on a decentralized agent network, aimed at screen-reader replacement workflows.
**Scope:** small · working: Live site browsefor.us linked; repo about 2.3k LOC; no video or user-test results. · polish: One screenshot; short README; page lists challenges such as latency and error recovery.
**Claims:** Works on any website | Persistence across tasks via orchestrator memory and queue
**Gaps:** No video; Live site not tested; No accuracy or user-testing data
Sources: https://devpost.com/software/delphi-lxes1j, evidence/la-hacks-la-hacks-2025-delphi.json, prompts_cache/la-hacks-2025.md

---

### Devin & Kevin
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: hack2school; DAIN Challenge: AI Agent Excellence & Innovation Awards

**What it is:** A multi-agent system meant to take over product-manager chores. Given a project input it produces a detailed plan covering technical scoping, staffing, daily standups and budget allocation, and it can create and solve GitHub issues.
**Problem / user:** Product managers and the tech teams they support; the page argues PM work (scoping, staffing, budgeting, standups) has no equivalent of developer copilots and can be automated.

**Features**
- Technical scoping of a project spec — Agents read the project input and break it into a technical scope; this was the first thing built. *[claimed]*
- Assigning people to work — Staffing agent allocates human capital to scoped tasks; added after asking other teams which PM duties mattered. *[claimed]*
- Daily standups — Agents conduct standup check-ins as part of the PM loop. *[claimed]*
- Budget allocation — Agents distribute a budget across the planned work. *[claimed]*
- GitHub issue creation and solving — The multi-agent system opens issues for planned work and has agents attempt to resolve them. *[claimed]*
- Project plan output — One project input yields a detailed project plan. *[claimed]*

**Flow:** User submits a project description → Agents scope it technically → Agents assign people and allocate budget → Agents run standups and create/solve GitHub issues → User receives a detailed project plan

**Prompt:** Hack2School track: AI-driven tools for education and productivity. DAIN challenge: use the DAIN platform and Butterfly app to build and deploy AI agent services for consumers or businesses, aiming at a profitable AI business.
**Fit (implied):** Built as a DAIN-based multi-agent service that automates the product-manager role, which maps to the DAIN agent-service challenge and a productivity framing; no explicit statement of targeting beyond the awards listed.  *(targeted: Track: hack2school, DAIN Challenge: AI Agent Excellence & Innovation Awards)*
**Sponsor tools:** DAIN (Platform the multi-agent system was built on (built-with tag), core)
**AI:** Several LLM agents each handle a PM function (scoping, staffing, standups, budgets, GitHub issues); the page names no models or prompting details.
**Architecture:** TypeScript agents on the DAIN platform coordinate through a multi-agent flow that reads a project input, plans it and touches GitHub issues. No further components described.
**Novelty:** Frames AI as replacing the product manager rather than the developer; scope grew from scoping alone to a broader PM suite after informal feedback from other teams.
**Scope:** small · working: No repo, demo or video linked; only a short text description. · polish: None visible; the page is brief and tongue-in-cheek.
**Claims:** PM role can be completely automated | Agents make and solve GitHub issues
**Gaps:** No repo linked; No demo or video; Page is very short; no UI or model details; Built-with tags only dain and typescript
Sources: https://devpost.com/software/kevin-4m6rbf, https://la-hacks-2025.devpost.com/

---

### Embers
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Cold Hard Cache; Google Gemini: Chase the Future!

**What it is:** A web app that turns a short home walkthrough video into an itemized, valued inventory for insurance. YOLO finds valuables, crops them, Gemini estimates replacement values, and a voice assistant answers questions about the inventory.
**Problem / user:** Homeowners, renters and small businesses who never document their belongings and then struggle to prove value to insurers after a disaster such as a wildfire.

**Features**
- Walkthrough video analysis — Uploaded video frames go through Ultralytics YOLO v11 to detect valuables, with multi-frame deduplication and non-max suppression to avoid double counting. *[shown_working]*
- Item snapshot catalog — Detected objects are cropped into individual images forming an organized inventory. *[shown_working]*
- Gemini replacement valuation — Gemini 2.0/2.5 looks at each crop, infers condition and brand hints, and estimates replacement value. *[shown_working]*
- Voice assistant queries — User speaks a question such as the value of a named TV; speech recognition plus lookup returns stored valuations. *[claimed]*
- Supabase storage — Items, valuations and video records saved in normalized tables with image storage URLs referenced separately. *[shown_working]*
- Post-fire comparison and claim export — Planned second walkthrough to flag missing items and generate insurer-ready reports. *[planned]*

**Flow:** Land on site and read About pages → Upload a short house-tour video → Wait for detection and cropping → View itemized results with estimated values → Review identification steps per item → Ask the voice assistant about an item's value

**Prompt:** Cold Hard Cache track: fintech ideas such as financial literacy and investment platforms. Gemini challenge: Gemini 2.0/2.5 APIs must be the core, using multimodal input, reasoning or real-time interaction.
**Fit (implied):** Uses Gemini multimodal reasoning as the valuation engine over cropped images, and frames the product as insurance/financial protection; the page names Gemini 2.0/2.5 prominently and wins on both.  *(targeted: Track: Cold Hard Cache, Google Gemini: Chase the Future!)*
**Sponsor tools:** Google Gemini 2.0/2.5 (Multimodal valuation of each detected item, core)
**AI:** YOLO v11 object detection over video frames, then Gemini multimodal prompts per cropped item to infer brand/condition and price; speech via a voice assistant (Whisper/OpenAI listed).
**Architecture:** Next.js/Tailwind frontend uploads video to a Python Flask backend; YOLO detects and crops, Gemini values items, results and images persist in Supabase, voice assistant queries them.
**Novelty:** Combines classic object detection with LLM appraisal to automate home-inventory documentation, aimed at pre-disaster preparation rather than post-claim recovery.
**Scope:** medium · working: About 4k LOC across Python backend and Next.js frontend; Devpost screenshots show upload and results pages. · polish: Landing, About, Upload, Results pages with framer-motion; no tests, Docker or CI.
**Claims:** A 2-minute video becomes a full digital inventory | Gemini 2.5 valuations described as accurate and realistic (unmeasured) | Backend scales to millions of items
**Gaps:** No demo video; Voice assistant working status not demonstrated; No quantitative accuracy results
Sources: https://devpost.com/software/insurefire, https://github.com/twistyyb/insurefire, https://la-hacks-2025.devpost.com/

---

### Fynd
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Track: AI Agents League (Fetch.ai)

**What it is:** A Tinder-style shopping app: agents crawl Shopify, Amazon and Etsy for products, the user swipes right or left, and the preferences refine recommendations. Web, mobile and Snap Spectacles AR frontends let the user preview picks in augmented reality.
**Problem / user:** Online shoppers facing too many choices across storefronts, causing decision fatigue and endless scrolling.

**Features**
- Agentic product crawling — Fetch.ai agents with custom connectors pull product data from Shopify, Amazon and Etsy. *[claimed]*
- Swipe-to-decide cards — React card UI: swipe right to like, left to skip; likes feed real-time preference learning. *[shown_working]*
- Recommendation engine — Aggregates liked items to suggest tailored products and cut scrolling. *[claimed]*
- Spectacles AR preview — Snap Spectacles app for hands-free browsing and AR product preview, with Dain/Butterfly handling AR visualization. *[claimed]*
- Button fallback for swipes — Gesture swiping on Spectacles failed, so buttons replace gestures there. *[claimed]*
- Cart and search — Screenshots show search, recommendations, cart and AR view screens. *[unclear]*
- Three synced frontends — Web, mobile and AR interfaces kept in sync with the agent backend. *[claimed]*

**Flow:** Search for what you want to buy → Browse product cards and swipe like or skip → Preferences update recommendations → Add items to cart → Open an AR preview on Spectacles

**Prompt:** Fetch.ai AI Agents League: use ASI1-Mini for agent reasoning and build with uAgents or the Fetch.ai SDK for real-world verticals such as healthcare, education, finance, sustainability.
**Fit (implied):** Fetch.ai agents handle crawling and recommendation logic across e-commerce data; the page says they were integrated with live product streams. It does not mention ASI1-Mini specifically.  *(targeted: Track: AI Agents League (Fetch.ai))*
**Sponsor tools:** Fetch.ai agents (Crawling stores and driving recommendation logic, core); Dain / Butterfly (AR visualization, supporting); Snap Spectacles (Hands-free AR product preview, supporting); Google Gemini (Listed in built-with; role not explained, unclear)
**AI:** Agentic crawlers collect product data and a preference-learning recommender updates from swipes; Gemini and TensorFlow are tagged but their roles are not described.
**Architecture:** Fetch.ai agents with Shopify, Amazon and Etsy connectors feed a recommendation backend; React web/mobile swipe UI and a Spectacles AR client read from it.
**Novelty:** Combines swipe-based preference learning, multi-store agent crawling and an AR glasses preview in one 48-hour build.
**Scope:** medium · working: Claims an MVP with three frontends; four screenshots and a YouTube demo link (unavailable to read); repo link is only an org listing. · polish: Prototype-level; AR gestures fell back to buttons.
**Claims:** Functional MVP with three interconnected frontends in 48 hours | Fetch.ai agents integrated with live e-commerce data streams
**Gaps:** Linked repo is only the LAHacks-2025 org listing; clone failed; YouTube demo page not readable; Roles of Gemini and TensorFlow unexplained
Sources: https://devpost.com/software/fynd-myi2jc, https://la-hacks-2025.devpost.com/

---

### Ghostface Cookah
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Snap Inc. Challenge: Dream it. Build it.

**What it is:** A Snapchat Spectacles Lens that turns a cooking video into timestamped recipe steps and shows the video, directions and a timer in AR, locked to the cook's head movement, controllable by voice or AR buttons.
**Problem / user:** Home cooks, especially beginners, who have messy hands and don't want to handle a phone or recipe book while cooking.

**Features**
- Recipe extraction from a cooking video — yt-dlp downloads the video, Whisper via Groq transcribes it, and the result is JSON of main steps with timestamps. *[claimed]*
- AR video overlay — Lens Studio video provider plays the recipe video in the user's field of view. *[shown_working]*
- Voice playback control — Spoken commands pause, play and skip steps. *[claimed]*
- AR button controls — On-screen AR buttons offer play, pause and next or previous step as an alternative to voice. *[claimed]*
- Timestamped directions — Step list generated from the transcript jumps the video to each step. *[claimed]*
- Head-locked timer and player — Manual timer, video and directions follow the wearer's head; screenshots label this view. *[shown_working]*

**Flow:** A cooking video is turned into timestamped steps → Wearer opens the Lens and sees the recipe view → Video player and directions appear head-locked → Use voice or AR buttons to play, pause or skip steps → Set the manual timer while cooking

**Prompt:** Snap Inc. Challenge: create a Lens on Spectacles that pushes wearable AR; themes include AI on AR glasses with camera access, health, dream worlds and everyday utility.
**Fit (implied):** Everyday-utility Spectacles Lens built in Lens Studio with voice and AR UI; the page credits Snap staff help. No explicit statement of which theme it targets.  *(targeted: Snap Inc. Challenge: Dream it. Build it.)*
**Sponsor tools:** Snap Spectacles / Lens Studio (AR display, UI, voice input and scripting in TypeScript, core); Groq Cloud Whisper (Transcribing recipe video into timestamped steps, supporting)
**AI:** Whisper speech-to-text through Groq on the video audio, with step extraction into JSON; Gemini/OpenAI are tagged but their roles are not stated.
**Architecture:** Offline pipeline (yt-dlp, Whisper) produces recipe JSON stored locally; a TypeScript Lens Studio Lens on Spectacles renders the video player, directions and timer.
**Novelty:** Puts recipe video and step timestamps into head-locked AR glasses; the team chose local storage over runtime LLM or fetch calls.
**Scope:** medium · working: Large Lens Studio project (953 files, mostly assets); screenshots of Recipe View and Video and Timer views; no video. · polish: Built by a team new to AR; no tests or CI; storage limits on device noted.
**Claims:** Product that could change lives (stated by team)
**Gaps:** Repo evidence has no README text; Raw README fetch failed; No demo video; Pipeline code location unclear (LOC mostly Lens Studio assets)
Sources: https://devpost.com/software/ghostface-cookah, https://github.com/joycechen721/lahacks25-spectacles, https://la-hacks-2025.devpost.com/

---

### GMax
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** MSI Lucky's Hackening

**What it is:** A Gmail Chrome extension with a FastAPI backend that watches new mail in real time, classifies spam and phishing with Gemini, drafts replies in the user's own writing style, and asks for approval by SMS before sending.
**Problem / user:** Busy professionals who lose hours to email (page cites 28% of the workday) and want routine mail handled automatically.

**Features**
- Real-time email intake — Gmail push notifications via Google Cloud Pub/Sub alert the backend when mail arrives. *[claimed]*
- Gemini analysis — Gemini classifies spam, detects phishing with a confidence score and decides whether a reply is needed. *[claimed]*
- Email persona — Indexes the user's sent messages to model their tone and write drafts in the same style. *[claimed]*
- SMS human-in-the-loop approval — Textbelt texts the email and suggested reply; user approval triggers automatic sending. *[claimed]*
- Spam rescue and labeling — Moves legitimate mail like interview invites out of spam and applies user or AI labels (Selenium used for labeling). *[claimed]*
- Chrome extension UI — React/TypeScript panel injected into Gmail with WebSocket status, quick actions, settings toggles and action history. *[claimed]*

**Flow:** Install extension and connect Gmail via OAuth → New email arrives and backend is notified → Pipeline classifies and labels it, rescuing non-spam → If a reply is needed, a persona-style draft is made → User gets an SMS with draft and approves → Reply is sent; user can review or edit in the extension

**Prompt:** MSI Lucky's Hackening: teams of four make the best project using MSI hardware; only selected UCLA teams, judged by MSI.
**Fit (explicit):** README states first place for the MSI track; the prompt is hardware-use based and nothing in the page ties the product to MSI hardware.  *(targeted: MSI Lucky's Hackening)*
**Sponsor tools:** Google Gemini (Spam/phishing classification, intent and reply generation, core)
**AI:** Gemini via Google Generative AI classifies mail, scores phishing, judges reply need and writes replies using a persona derived from indexed sent mail.
**Architecture:** Chrome extension (React/TS) talks to FastAPI over REST and WebSockets; Gmail API plus Pub/Sub feed a multi-stage pipeline with Gemini; Supabase stores history; Textbelt sends SMS.
**Novelty:** Closes the loop from inbox to sent reply through SMS approval rather than a UI-only review, with style-matched drafts.
**Scope:** medium · working: About 5k LOC across backend and extension with detailed README; no demo video or screenshots found. · polish: Detailed README with setup; no tests, Docker or CI.
**Claims:** Professionals spend 28% of workday (2.6h/day) on email (motivation statistic) | No permanent storage of email content
**Gaps:** No challenges section; No demo evidence of working end to end
Sources: https://devpost.com/software/gmax, https://github.com/aroy23/GMax, https://la-hacks-2025.devpost.com/

---

### Leadify; Brew
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Linkd Challenge: Best Use of Linkd People Search

**What it is:** The Devpost page (Leadify) describes a pipeline that turns event details into five ranked sponsor/speaker leads from Linkd people search, with outreach drafts. The linked repo README describes a related app, Brew, that finds people with Linkd, writes personalized LinkedIn or email messages and can send them via browser automation.
**Problem / user:** Event organizers, especially small teams or solo club founders, who manually hunt for sponsors and speakers on LinkedIn and write cold emails. Brew extends this to anyone doing cold outreach.

**Features**
- Event-to-lead planning — Gemini reads theme, audience and funding need and proposes target industries, companies, universities and roles, then turns them into iterative search queries. *[claimed]*
- Linkd people search with dedup — Queries go to the Linkd API to retrieve real LinkedIn profiles; duplicates are removed. *[shown_working]*
- AI lead scoring and Top 5 — Gemini scores each lead on location, experience, event fit and response likelihood and explains the match. *[claimed]*
- Outreach and proposal drafts — Personalized messages and sponsorship proposals written for top leads, ready to edit. *[claimed]*
- Approval-first agents — No agent step proceeds without user approval; Fetch.ai hosts parallel agent tasks. *[claimed]*
- Brew message generation — Per README, messages reference the user's saved profile, objective and target's profile; user edits before sending. *[claimed]*
- Brew agentic sending — Browserbase Stagehand drives LinkedIn or Gmail to send messages, with Google and LinkedIn login. *[claimed]*
- Brew outreach dashboard — Tracks cold-outreach progress. *[claimed]*

**Flow:** Enter event details (Leadify) or profile and objective (Brew) → Review proposed targets and generated Linkd search results → See ranked Top 5 leads with fit explanations → Review and edit generated outreach drafts → Approve before any agent action or send

**Prompt:** Linkd Challenge: best and most creative interaction layer on top of a provided search API and a database of 350,000 UCLA alumni.
**Fit (implied):** Leadify and Brew both build an agent-style layer over Linkd search that turns a goal into queries, ranked people and drafted messages; README credits Linkd for people search.  *(targeted: Linkd Challenge: Best Use of Linkd People Search)*
**Sponsor tools:** Linkd API (People search and lead discovery, core); Google Gemini (Query generation, lead ranking and drafting, core); Fetch.ai (Agent hosting and parallel tasks (Leadify page), supporting); Browserbase Stagehand (Browser automation for sending messages (Brew), supporting)
**AI:** Gemini chains planning, search-query generation, lead scoring with explanations, and draft writing; async Python orchestrates the stages. Brew adds Gemini message generation and a browser-automation agent.
**Architecture:** Next.js/React frontend with async Python orchestration (Leadify) or Next.js 15 API routes (Brew repo) calling Gemini and Linkd; Fetch.ai agents or Stagehand perform actions.
**Novelty:** Uses the sponsor's people-search API as the data layer of a goal-driven outreach agent that ranks and explains leads; repo and page cover two related products.
**Scope:** medium · working: Repo has about 5k LOC Next.js app with setup steps; Devpost shows three screenshots; no video or live demo. · polish: Clean README and UI components; no tests, Docker or CI.
**Claims:** Would have saved weeks of work when starting a club (self-reported) | No agent action without user approval
**Gaps:** Devpost page is Leadify and README is Brew; they may be two separate submissions or one repo; feature list merges both and marks which; Leadify's Python/Fetch.ai code not seen in repo evidence; No repo link on Devpost page
Sources: https://devpost.com/software/momentum-94wfd6, https://github.com/EvanAd7/la-hacks, https://la-hacks-2025.devpost.com/

---

### LingoBuddy
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Google Gemini: Chase the Future!

**What it is:** A web language-learning platform where learners chat with Gemini to get custom lessons, vocabulary cards, example sentences, grammar explanations and cultural notes, with text-to-speech and speech-to-text for pronunciation practice.
**Problem / user:** Language learners, particularly busy CS students, who find Duolingo tedious and its speech features limited and want quick, pronunciation-focused practice.

**Features**
- Chat-generated custom lessons — Learner types in English or the target language and Gemini produces lesson plans, exercises and grammar explanations. *[shown_working]*
- Vocabulary cards with pronunciation — Cards and example sentences have text-to-speech buttons; Gemini supplies pronunciation help. *[shown_working]*
- Speech-to-text practice — Microphone input with a language prompter transcribes the learner's speech. *[claimed]*
- Accounts and profile — Supabase-backed login, personalized profile, language and level selector, lesson landing page. *[shown_working]*
- AI-generated lesson topics and cultural notes — Lesson page proposes topics and shows cultural notes plus practice; screenshots show French, Chinese, Norwegian. *[shown_working]*
- Live conversation mode — Planned dynamic spoken conversation with Gemini; dropped for time and latency. *[planned]*

**Flow:** Sign up or log in → Set profile, language and level → Land on a lesson page with AI topics → Study vocab cards, hear them via text-to-speech → Speak with the mic and prompter → Read cultural notes and do practice

**Prompt:** Google Gemini: Chase the Future! Gemini 2.0/2.5 APIs must be the core, using multimodal input, reasoning, code generation, personalization or real-time conversation.
**Fit (implied):** Gemini multimodal models generate lessons and handle text-to-speech and speech-to-text; the page lists google-gemini and multimodal tags and wins this challenge.  *(targeted: Google Gemini: Chase the Future!)*
**Sponsor tools:** Google Gemini (Lesson generation, TTS and STT, pronunciation help, core)
**AI:** Gemini multimodal models generate lessons from chat, produce audio for pronunciation and transcribe speech; free tier limited non-English pronunciation.
**Architecture:** Next.js frontend with Supabase auth/database; FastAPI/Uvicorn backend calls Gemini for generation and audio.
**Novelty:** Targets speech-first practice with AI-built lessons from free chat rather than fixed curricula; live conversation was attempted but cut.
**Scope:** small · working: Small repo (about 1.7k LOC) with setup steps; team calls it mostly working; Devpost screenshots show multiple languages. · polish: Typewriter animations and custom UI; README thin on features; no tests.
**Claims:** Mostly working product with custom login and AI integration
**Gaps:** README mentions quizzes and conversation simulations that Devpost says were not built; No video
Sources: https://devpost.com/software/lingobuddy-fkj4g0, https://github.com/sebomaniac/lingobuddy, https://la-hacks-2025.devpost.com/

---

### Lumos
*LA Hacks LA Hacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Overall: 2nd Place [2nd]; Track: AI Agents League (Fetch.ai)

**What it is:** A memory-assistance system for people with Alzheimer's. Snapchat Spectacles recognize familiar faces and show names and relationships as AR overlays, Fetch.ai agents handle safety and notifications, and a caregiver React Native app manages profiles, safe zones and alerts.
**Problem / user:** Alzheimer's patients who lose recognition of people and places, and their caregivers who need to track safety.

**Features**
- AR face recognition overlay — Spectacles lens identifies stored faces and displays name and relationship cue *[claimed]*
- Face Recognition Agent — Fetch.ai uAgent matches faces to stored profiles using DeepFace in the repo *[claimed]*
- Safe-zone monitoring — Safety agent watches GPS against geofences and alerts caregivers *[claimed]*
- Caregiver app — React Native/Expo app to manage patient profiles, reminders, safe zones, journals and receive alerts *[claimed]*
- Gemini memory prompts and voice journaling — Gemini 2.5 produces reminders and daily reflection prompts *[claimed]*
- Healthcare agent and nearest hospital — DAIN agent and Melissa API provide hospital lookup and health insights *[claimed]*

**Flow:** Caregiver configures patient profile, safe zones and reminders → Patient wears Spectacles → Familiar face triggers a name/relationship overlay → Leaving a safe zone alerts the caregiver → Patient journals by voice

**Prompt:** Fetch.ai AI Agents League: build agents that reason with the ASI1-Mini LLM using the uAgents framework or Fetch.ai SDK, in areas such as healthcare, education, finance or sustainability; sub-prizes for vertical impact, ASI-1 Mini use and multi-agent systems.
**Fit (implied):** Healthcare vertical built from Fetch.ai uAgents for face recognition, safety and notification, plus a DAIN healthcare agent. ASI-1 Mini use is not mentioned; Gemini does the reasoning.  *(targeted: Fetch.ai AI Agents League, Overall)*
**Sponsor tools:** Fetch.ai uAgents (Face recognition, safety and notification agents, core); DAIN (Healthcare agent, supporting); Melissa API (Nearest hospital lookup, supporting)
**AI:** DeepFace-based face recognition; Fetch.ai uAgents coordinate tasks; Gemini 2.5 handles prompts, decisions and journaling.
**Architecture:** Spectacles lens (TypeScript) to Python agents; Node/Express and MongoDB Atlas backend with Cloudflare Workers and WebSockets; React Native caregiver app.
**Novelty:** Pairs AR glasses with an agent mesh and caregiver app; broad scope across hardware, agents, backend and mobile.
**Scope:** large · working: Repo with four components and tests, screenshots incl. Spectacle's view; no demo or video link on page. · polish: Architecture diagram, detailed README; no metrics.
**Gaps:** No video or demo link; Latency/accuracy not measured
Sources: https://devpost.com/software/lumos-f8h0mn, evidence/la-hacks-la-hacks-2025-lumos.json, https://la-hacks-2025.devpost.com/

---

### Magic Mirror
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: Clean Code

**What it is:** A voice-controlled virtual try-on studio. A LiveKit voice agent drives a web app; FastSAM and YOLO segment the user and garment, and the open-source FitDiT model composes an image of the user wearing the clothing, optionally from an OpenAI-generated garment.
**Problem / user:** Online clothing shoppers who can't tell how items will fit or look, driving costly returns (page cites 30-40% return rates and about $40B yearly).

**Features**
- Virtual try-on image generation — Pipeline segments user and clothing, then FitDiT places the garment onto the user's photo. *[claimed]*
- Voice-controlled interface — LiveKit conversational agent lets users operate the app hands-free. *[claimed]*
- User-supplied clothing images — A clothing photo can be provided and used as the garment input. *[claimed]*
- AI-generated clothing — Optionally calls OpenAI image generation to create a new garment before try-on. *[claimed]*
- Segmentation with FastSAM and YOLO — Custom pipeline masks person and garment regions before synthesis. *[claimed]*
- GPU-backed Flask services — Python/Flask backend with PyTorch models run on rented H100 GPUs; Next.js/Tailwind frontend. *[claimed]*

**Flow:** Open the web frontend → Speak to the voice agent → Provide a clothing image or ask for a generated one → Pipeline segments and applies the garment → View the generated image of yourself wearing it

**Prompt:** Clean Code track (sustainability): build projects that help communities and ecosystems flourish, e.g. shared-resource platforms and eco-friendly tools.
**Fit (implied):** Pitch ties fewer clothing returns to lower emissions and waste; the page cites return and greenhouse-gas figures as motivation.  *(targeted: Track: Clean Code)*
**Sponsor tools:** LiveKit (Conversational voice agent, core); OpenAI image generation (Optional garment generation, supporting)
**AI:** Segmentation models (FastSAM, YOLO) plus FitDiT diffusion-based try-on on H100 GPUs, a LiveKit voice agent, and optional OpenAI image generation.
**Architecture:** Next.js frontend and LiveKit agent call Flask/FastAPI servers wrapping the segmentation and FitDiT try-on pipeline on GPU; results return as images.
**Novelty:** Voice-first try-on stitched from open-source vision models, with repo sizable because it vendors a full try-on codebase and Gradio demo.
**Scope:** large · working: Repo 612 files, about 69k LOC including clothing-tryon code; no video or demo link. · polish: Has tests and Docker; no CI; README is the Devpost text.
**Claims:** Returns of 30-40% and about $40B yearly cited as problem size | Hands-off interactive experience
**Gaps:** No demo video; Challenges section is brief; Much of repo LOC is vendored try-on code
Sources: https://devpost.com/software/magic-mirror-muya4w, https://github.com/KevinWu098/magic-mirror, https://la-hacks-2025.devpost.com/

---

### OpenSesame.Work
*LA Hacks LA Hacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Overall: 3rd Place [3rd]

**What it is:** A job-search autopilot: the user enters preferences and uploads a resume, then Gemini-driven browser automation applies to matching postings and sends personalized LinkedIn connection requests to recruiters.
**Problem / user:** Job seekers worn out by repetitive applications and cold outreach with little response.

**Features**
- Preference and resume intake — Collects experience level, industry, job preferences and a resume; extracts keywords *[shown_working]*
- Automatic job applications — Gemini Browser-Use agent fills out and submits applications on online postings *[shown_working]*
- Personalized recruiter outreach — AI-written LinkedIn connection requests based on profile and goals *[shown_working]*
- Parallel browser workflows with retries — Runs multiple browser sessions and falls back on failure *[claimed]*
- Response-rate learning and dashboard — RL-based message improvement and tracking dashboard *[planned]*

**Flow:** Choose experience, industry and job preferences → Upload resume → Start the run → System applies to matching postings → System sends LinkedIn requests to recruiters

**Prompt:** not public / not found
**Fit (none):** Page names no track; submission is a general-purpose agentic automation of job search. Overall prizes were judged on originality, usefulness, feasibility and track relation.  *(targeted: Overall 3rd place)*
**AI:** Gemini model drives the Browser-Use library to operate real sites; resume keyword extraction and LLM-written outreach messages.
**Architecture:** Flask backend serving a React/Next frontend; Playwright browser automation via Browser-Use with parallel workers; Gemini as model.
**Novelty:** Executes real applications and LinkedIn actions end-to-end rather than only suggesting matches; small codebase.
**Scope:** small · working: Claims real applications and outreach in the demo; no video or live link listed. · polish: Minimal README; 1.7k lines; simple UI.
**Gaps:** Track not stated; No video
Sources: https://devpost.com/software/opensesame-work, evidence/la-hacks-la-hacks-2025-opensesame-work.json

---

### Pulse
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Snap Inc. Challenge: Dream it. Build it.

**What it is:** A Snap Spectacles AR Lens that coaches a bystander through CPR: a pre-check screen, hand-placement overlay on the victim's chest, rhythm cues with live BPM, and a voice-opened AR map pointing to nearby AEDs.
**Problem / user:** Untrained bystanders who freeze when someone collapses; the page says only about 20% of Americans are current on CPR training.

**Features**
- Pre-CPR check screen — Opening screens (two screenshots) prepare the user before compressions begin. *[shown_working]*
- Hand-placement AR overlay — Overlay marks correct hand position on the victim's chest in the wearer's view; pose detection mentioned but unspecified. *[claimed]*
- Rhythm cues with live BPM — Visual and audio metronome cues plus a live compression BPM readout during CPR. *[shown_working]*
- Compression force and motion tracking — Page says sensors track hand movement and force to check accuracy. *[claimed]*
- AED map in AR — Registered AED locations and approximate distances are placed in the AR world; precise only at Pauley Pavilion. *[shown_working]*
- Voice open/close of map — A voice recognition module lets hands-busy users show or hide the AED map. *[claimed]*

**Flow:** Put on Spectacles and open the Lens → Complete the pre-CPR check → Follow hand-placement overlay and start compressions → Watch BPM and rhythm cues → Say a voice command to bring up nearby AEDs

**Prompt:** Snap Inc. Challenge: create a Lens on Spectacles that pushes wearable AR; themes include AI on glasses with camera access, health and fitness, and everyday utility.
**Fit (implied):** Health-and-safety Spectacles Lens using AR overlays, camera-based pose detection and voice input; built-with tags and credits show Lens Studio and Spectacles Interaction Kit.  *(targeted: Snap Inc. Challenge: Dream it. Build it.)*
**Sponsor tools:** Snap Spectacles / Lens Studio / Interaction Kit (AR overlays, UI, voice and sensors, core)
**AI:** Pose detection for hand placement and compression measurement is mentioned, but the page leaves the method as an unfinished placeholder; voice recognition via a voice module.
**Architecture:** Single Lens Studio TypeScript project on Spectacles combining camera/pose tracking, audio metronome, voice commands and a GPS-anchored AED map.
**Novelty:** Applies AR glasses to emergency first aid, combining hands-free guidance with AED locating in one Lens.
**Scope:** medium · working: Repo is a large Lens Studio project (1,263 files); four screenshots incl. live CPR with BPM; no video. · polish: Page contains an unfilled placeholder; GPS accuracy limited; no tests.
**Claims:** Only 20% of Americans are current with CPR training (motivation) | AED locations precise at Pauley Pavilion
**Gaps:** Repo evidence has no README; Devpost has a placeholder where pose detection method should be; No demo video; AED data source unnamed
Sources: https://devpost.com/software/pulse-n06ij9, https://github.com/jackyydai/LAHack2025-Pulse, https://la-hacks-2025.devpost.com/

---

### SnapDrobe
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Snap Inc. Challenge: Dream it. Build it.

**What it is:** A Snap Spectacles voice app: say 'Add to wardrobe' to capture a garment, Gemini turns the image into structured metadata saved in DynamoDB, and later a spoken request returns a weather- and time-aware outfit with an AI-generated mockup shown in AR.
**Problem / user:** People who struggle to choose and match outfits and want to capture style inspiration hands-free, from novices to fashion-savvy users.

**Features**
- Voice wardrobe capture — Spectacles camera takes a picture when the user says 'Add to wardrobe'. *[claimed]*
- Gemini garment description — Submit endpoint sends image to Gemini, which returns JSON (name, gender, colors with hex, material, weather, time of day, occasions) stored in DynamoDB. *[claimed]*
- Natural-language outfit requests — Ask endpoint transcribes speech, analyzes intent with Gemini and selects matching wardrobe items. *[claimed]*
- Weather and time context — OpenWeather data for location and time of day informs which items are picked. *[claimed]*
- Full look with accessories — Outfit includes top, bottom, footwear and optional cap, jacket or bag. *[claimed]*
- AI outfit mockup — Gemini generates an image of the assembled outfit displayed on the Spectacles. *[claimed]*
- Planned extras — AR try-on overlay, friend wardrobes, calendar notifications, offline cache. *[planned]*

**Flow:** See a garment and say 'Add to wardrobe' → Spectacles capture; Gemini saves its metadata → Later say 'Ask for outfit' with the occasion → Backend combines weather, time and wardrobe → View the generated outfit mockup in AR

**Prompt:** Snap Inc. Challenge: create a Lens on Spectacles that pushes wearable AR; themes include AI on glasses with camera access, health, dream worlds, everyday utility.
**Fit (implied):** Everyday-utility Spectacles Lens using camera capture, voice triggers and AI image generation; README says it started from getting the new Spectacles.  *(targeted: Snap Inc. Challenge: Dream it. Build it.)*
**Sponsor tools:** Snap Spectacles / Lens Studio / Interaction Kit (Voice commands, capture, AR UI, core); Google Gemini (Image-to-JSON, reasoning, outfit mockup generation, core); Fetch.ai uAgents (Device to cloud communication, supporting)
**AI:** Gemini does image-to-structured-JSON analysis, prompt reasoning for outfit selection and image generation for the mockup; speech-to-text feeds the request (ElevenLabs in requirements).
**Architecture:** Lens Studio TypeScript client posts to Python uAgent endpoints on Render; backend calls Gemini, OpenWeather and DynamoDB (boto3), returning outfit data and image.
**Novelty:** Stores AI-written text descriptions of items seen in the wild rather than images, and returns weather-aware outfits on AR glasses.
**Scope:** small · working: Backend repo is six files (about 280 LOC); Lens project not in the evidence; no demo link. · polish: Detailed README; challenges section on Devpost left as placeholder.
**Claims:** End-to-end system linking AR wearables, cloud AI and environment sensing | Built with no prior AR experience
**Gaps:** Repo is only the API; Lens Studio client not seen; Devpost challenges section is a placeholder; No demo video
Sources: https://devpost.com/software/snapdrobe, https://github.com/venkatnikhilm/SnapDrobeAPI, https://la-hacks-2025.devpost.com/

---

### stackwise
*LA Hacks LA Hacks 2025 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Warp Challenge: Best Developer Tool

**What it is:** A web app where a plain-English project description becomes a Gemini-recommended tech stack drawn as an editable node graph. Users can edit nodes and links, chat to adjust, and generate bash scaffolding scripts and a builder prompt for the repository.
**Problem / user:** Junior developers who don't know where to start with a stack and senior engineers who want production-minded choices.

**Features**
- Stack generation from plain English — Gemini converts the project description into parsable JSON of technologies and relationships. *[shown_working]*
- Interactive stack graph — React graph with node detail views, drag-and-drop menu, and editing of technologies and connections. *[shown_working]*
- AI chat adjustment — Gemini chat window revises the stack; Flask backend keeps chat history and graph structure. *[shown_working]*
- Bash repo scaffold — Generates a bash script from the finalized graph that creates the project structure. *[shown_working]*
- Builder prompt — Produces a prompt describing the stack for use with other coding tools (screenshot shown). *[shown_working]*
- Direct GitHub export — Planned export to real repositories, plus cost/speed toggles and security suggestions. *[planned]*

**Flow:** Describe the project in the chat → Gemini proposes a stack → Inspect and edit the graph nodes and links → Ask the AI to tweak recommendations → Generate bash scaffold script or builder prompt

**Prompt:** Warp Challenge: build a hack that improves developer experience, across creating, modifying or testing software.
**Fit (implied):** Developer tool for stack selection and project scaffolding that shortens idea-to-structure setup; the page does not mention Warp itself.  *(targeted: Winner Warp Challenge: Best Developer Tool)*
**Sponsor tools:** Google Gemini (Stack recommendation, graph JSON, chat, script generation, core)
**AI:** Gemini prompted to emit structured JSON graphs and to reason over technology relationships when users chat; also generates scaffold scripts and prompts.
**Architecture:** React/TypeScript/Vite and Next.js frontend on Vercel talks to a Flask backend on Railway that calls Gemini and stores chat history and graph state.
**Novelty:** Treats the stack as an editable graph linked to scaffold generation, rather than a text recommendation.
**Scope:** small · working: Live Vercel demo link and eight UI screenshots; no repo or video. · polish: Deployed frontend and backend; no tests visible.
**Claims:** Path from idea to deployable structure in a few minutes | Useful for production planning beyond the hackathon
**Gaps:** No repo listed; Live demo not opened; No video
Sources: https://devpost.com/software/stackwise, https://la-hacks-2025.devpost.com/

---

### StartNOW
*LA Hacks LA Hacks 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Track: AI Agents League (Fetch.ai)

**What it is:** A startup simulator: you pitch an idea and watch a boardroom of personality-driven uAgents (unpaid intern, CTO, PM, investor, marketer) debate it with ASI:One Mini, while you can interject as the boss. It outputs a pitch deck, meeting report, mood board and investor pitch.
**Problem / user:** Founders and aspiring entrepreneurs overwhelmed by what to do next who want varied perspectives on an idea.

**Features**
- Agent boardroom debate — Agents with distinct personas exchange messages via uAgents event-driven messaging, producing debate and collaboration. *[shown_working]*
- Agent factory — Spawns a consistent team, each agent seeded with a personality archetype. *[claimed]*
- User interjection as boss — Flask REST endpoints take human input and agents adapt their discussion. *[claimed]*
- Live conversation view — React frontend visualizes the discussion with updates pushed from the backend. *[shown_working]*
- Agent personalization — Screenshots show a personalize-agents screen. *[claimed]*
- Meeting report — Gemini receives the full conversation and writes an actionable summary of best next steps. *[claimed]*
- Pitch deck, mood board, investor pitch — Post-session outputs; repo uses reportlab/weasyprint and a spectacle deck library. *[claimed]*

**Flow:** Open landing page and pitch a startup idea → Watch the agent board brainstorm and disagree → Optionally personalize agents or inject guidance → End session and receive deck, report and mood board → Generate an investor pitch

**Prompt:** Fetch.ai AI Agents League: use ASI1-Mini for agent reasoning and build with uAgents or the Fetch.ai SDK for real-world verticals such as healthcare, education, finance.
**Fit (explicit):** Multi-agent system built on uAgents with ASI:One Mini driving each agent's responses; the page and README name these tools directly.  *(targeted: Track: AI Agents League (Fetch.ai))*
**Sponsor tools:** Fetch.ai uAgents (Event-driven agent-to-agent messaging and agent factory, core); ASI:One Mini (Agent tone, responses and decisions, core); Google Gemini (Summarized meeting report, supporting)
**AI:** Each agent has a role prompt on ASI:One Mini and converses with others over uAgents; Gemini summarizes the whole transcript into a report.
**Architecture:** Python Flask backend with a uAgents runner; agents message each other and push updates to a React/JSX frontend; REST endpoints receive human input.
**Novelty:** Frames startup advice as an observable agent-to-agent boardroom with humorous personas rather than a single chatbot.
**Scope:** medium · working: Repo of 46 files and about 3.5k LOC with run instructions; Devpost screenshots; no demo or video. · polish: Persona-themed UI and multiple outputs; README very brief; no tests.
**Claims:** Can surface ideas the user had not considered
**Gaps:** No demo or video; Working status of deck and mood board generation not evidenced
Sources: https://devpost.com/software/startnow, https://github.com/c00lme/startup-sim, https://la-hacks-2025.devpost.com/

---

