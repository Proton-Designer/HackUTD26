# ShellHacks — ShellHacks 2025 (5 projects)

### Agent Zero
*ShellHacks ShellHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One

**What it is:** A multi-agent invoice fraud detector: an LLM orchestrator picks specialist agents, each scoring a distinct fraud signal, and the results combine into a reliability prediction for an invoice. Backed by BigQuery data pipeline and a React/FastAPI app.
**Problem / user:** Individuals, small businesses and AP teams without legal or finance staff, exposed to false or duplicate invoices.

**Features**
- Orchestrator agent — LLM coordinator decides which specialist agents to run for an input *[claimed]*
- Specialist fraud agents — Each agent scores one subtle signal (amounts, vendor, line items, attachments) against a rubric *[claimed]*
- Parallel execution — Up to six agents run at once to cut latency *[claimed]*
- Aggregated reliability score — Per-metric risks combined into one concise prediction with confidence *[claimed]*
- Agent Development Kit — Modular ADK so new agents can be added and tested locally *[shown_working]*
- Frontend and API — React/TypeScript UI and FastAPI service for demoing *[shown_working]*

**Flow:** Submit an invoice → Coordinator selects agents → Agents run in parallel and score → View aggregated reliability prediction

**Prompt:** Capital One ShellHacks 2025 'Innovate & elevate - future of finance': build a financial-services app using emerging tech such as Gen AI or blockchain.
**Fit (implied):** Applies Gemini and trained models in an agent system to financial fraud; page names the Capital One track but not the prompt text.  *(targeted: Capital One)*
**AI:** Gemini-driven coordinator routes to specialist agents; in-house models (TensorFlow) pretrained on fraud datasets and invoice data sourced via YOLOv11; BigQuery stores features.
**Architecture:** Python FastAPI backend with coordinator, agents, BigQuery pipeline; Node/Express and React/TypeScript frontend; agent ADK and tools folders.
**Novelty:** Frames fraud detection as many narrow trained agents with a routing layer, with a reusable agent SDK; larger than typical hackathon repos.
**Scope:** large · working: Repo has backend, frontend, tests, docker and CI; YouTube demo embedded; no accuracy numbers. · polish: Detailed README with architecture overview and deployment notes.
**Claims:** Agents pretrained on financial data | Boasts great results but reports no numbers
**Gaps:** video not watchable; no benchmark numbers
Sources: https://devpost.com/software/agentzero-tnh9p3, https://github.com/BonelessWater/shellHacks_1 (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2025)

---

### GreenLight
*ShellHacks ShellHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner State Farm

**What it is:** A driver-education web app: users upload dashcam clips of unsafe driving, Gemini identifies the behavior, and an ADK agent generates a Three.js 3D replay with alternate safer actions, followed by quizzes earning safety points.
**Problem / user:** Drivers with unsafe habits who want to learn from real incidents; ties to insurance education.

**Features**
- Dashcam upload and analysis — Gemini reviews the video and names unsafe behaviors *[claimed]*
- 3D incident replay — Gemini via Google ADK writes Three.js simulations of the event *[claimed]*
- What-if mitigation view — Simulation shows how different driver actions could avoid the incident *[claimed]*
- Targeted quizzes and points — Questions follow each incident; correct answers earn safe-driving points with feedback *[claimed]*
- Insurance and driving quiz section — Separate quizzes on safe driving and insurance *[claimed]*
- Dashboard, incidents, light/dark modes — React/shadcn UI with Firebase data *[shown_working]*

**Flow:** Sign up or log in → Upload dashcam footage on dashboard → Gemini analyzes the clip → Open incident page to see 3D simulation and summary → Answer incident question and quizzes for points

**Prompt:** State Farm ShellHacks 2025: make insurance easier to grasp and useful so students can prepare for everyday risks like theft, fire or accidents; tools, gamification and education welcome.
**Fit (implied):** Gamified safe-driving learning from real incidents plus an insurance quiz section; the page lists the State Farm win without quoting the prompt.  *(targeted: State Farm)*
**AI:** Gemini analyzes video for unsafe behavior; Gemini with Google ADK generates Three.js simulation code; agent was rearchitected to a single command, cutting processing time about 50% (team claim).
**Architecture:** React/TypeScript/Tailwind frontend; FastAPI backend with ADK agent and Gemini; Firebase stores users, incidents, quizzes; Three.js renders replays.
**Novelty:** Turns video into generated 3D simulation code via an LLM agent rather than only text feedback.
**Scope:** medium · working: YouTube demo linked, repo with frontend (83 files) and backend; no live link or tests; README is a one-liner. · polish: Figma-designed UI with dark mode and help modal.
**Claims:** Agent redesign cut processing time about 50%
**Gaps:** video not watchable; README nearly empty
Sources: https://devpost.com/software/greenlight-idnv6o, https://github.com/thashin04/GreenLight-Driving (evidence README), sponsor_prompts_*.jsonl (ShellHacks 2025)

---

### Next Step
*ShellHacks ShellHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner State Farm

**What it is:** An insurance-education app where an AI voice agent runs time-sensitive practice scenarios in auto, home or health insurance and scores the user from 0 to 100 on safety, insurance knowledge, procedure and decision quality.
**Problem / user:** People learning insurance who find textbooks dense and lacking real-time practice.

**Features**
- Voice scenario simulation — Vapi voice agent plays realistic urgent situations and the user responds live *[claimed]*
- Three insurance domains — User picks auto, home or health scenarios *[shown_working]*
- Four-criteria scoring — AI scores Safety Awareness, Insurance Knowledge, Procedural Understanding, Decision-Making 0-100 *[claimed]*
- Results page — Screens for home, practice and results shown in screenshots *[shown_working]*

**Flow:** Open home page and choose a domain → Start a scenario and speak with the voice agent → Receive scores on four criteria → Review results

**Prompt:** State Farm ShellHacks 2025: make insurance easier to grasp and useful for students preparing for everyday risks; tools, gamification and education encouraged.
**Fit (implied):** Interactive scenario practice in three insurance areas with graded feedback; page lists the win but does not cite the prompt.  *(targeted: State Farm)*
**AI:** Vapi voice agent drives conversations; prompt-engineered scoring against four criteria; agent tuned by the team.
**Architecture:** Next.js/React/TypeScript/Tailwind frontend with Flask Python backend calling the Vapi agent and scoring prompts.
**Novelty:** Spoken, role-play style insurance training with rubric scoring.
**Scope:** small · working: YouTube demo embedded and screenshots; repo not readable by extraction. · polish: Home, scenario and results screens; no live link.
**Gaps:** repo clone failed; video not watchable
Sources: https://devpost.com/software/next-step-cme06a, sponsor_prompts_*.jsonl (ShellHacks 2025)

---

### The Rat Race
*ShellHacks ShellHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner State Farm

**What it is:** A humorous choose-your-own-adventure web game where the player is an intern at a rat-run insurance company; tasks, customer claims and choices raise sales and coworker scores and lead to one of six endings while teaching insurance terms.
**Problem / user:** Anyone, especially students, who find insurance dull; teaches plans, deductibles, premiums and risk through play.

**Features**
- Branching story with six endings — Choices change Sales, Coworker and karma values leading to endings like Promotion or King of Ratopia *[claimed]*
- Customer service scenarios — Player guides customers through plans and claims; empathy and accuracy affect scores *[claimed]*
- Insurance concept teaching — Covers plan selection, deductibles, premiums and risk assessment inside story events *[claimed]*
- Whimsical claims — Absurd cases such as UFO damage or stolen cheese *[claimed]*

**Flow:** Start as new intern at Snout Farm Insurance → Meet King Rat and do daily tasks → Answer customer questions and claims → Reach one of six endings

**Prompt:** State Farm ShellHacks 2025: make insurance easier to grasp for students via tools, gamification or education.
**Fit (implied):** Gamified, humorous narrative that embeds insurance vocabulary; page lists State Farm and Netflix wins.  *(targeted: State Farm, Netflix)*
**AI:** none
**Architecture:** Next.js/React web game with scripted branching narrative and Adobe-made art; no backend described.
**Novelty:** Narrative game with satirical office theme instead of a calculator or chatbot.
**Scope:** small · working: YouTube demo embedded; no repo or live link found. · polish: Named characters, six defined endings, scoring systems described.
**Claims:** Winner of State Farm and Netflix challenges
**Gaps:** no repo; challenges and next steps sections empty
Sources: https://devpost.com/software/the-rat-race, sponsor_prompts_*.jsonl (ShellHacks 2025)

---

### VL-ADK
*ShellHacks ShellHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** NVIDIA (Hack for the Future with NVIDIA); Waymo; Microsoft

**What it is:** A natural-language robot controller: Google ADK agents (Director, Pilot, Observer) drive a JetBot with an NVIDIA Jetson Orin Nano, using YOLOE to pre-process the camera feed before Gemini reasons, with a React control panel.
**Problem / user:** Students and hobbyists wanting an affordable embodied-agent proof of concept; no formal user stated.

**Features**
- Natural-language tasks — User asks the agents to find an object, guide them or entertain them *[claimed]*
- Director/Pilot/Observer agents — Three ADK agent roles split planning, driving and perception *[claimed]*
- Robot control API — Python endpoints expose motion to ADK tools *[claimed]*
- Live control panel — React/TypeScript UI streams camera view over WebSockets *[claimed]*
- YOLOE middle layer — Object detection summarizes frames to cut tokens sent to Gemini *[claimed]*

**Flow:** Type a request in the control panel → Director interprets and delegates → Pilot moves the robot → Observer reports from camera feed → User watches live view

**Prompt:** NVIDIA 'Hack for the Future': use AI, graphics or accelerated computing to improve life with NVIDIA tools; Waymo and Microsoft prizes also won.
**Fit (implied):** Runs an agentic robot on a Jetson Orin Nano with on-device YOLOE; page lists the three wins without quoting prompts.  *(targeted: NVIDIA (Hack for the Future with NVIDIA), Waymo, Microsoft)*
**Sponsor tools:** NVIDIA Jetson Orin Nano (Onboard compute for the JetBot, core)
**AI:** Google ADK multi-agent setup with Gemini reasoning; YOLOE detections compress vision input to reduce context and token cost.
**Architecture:** Host runs ADK agents and React panel; SSH tunnels to the Jetson, which exposes Python control endpoints and a camera stream via WebSockets.
**Novelty:** Hardware-embodied multi-agent system on a student budget; no LiDAR.
**Scope:** medium · working: Demo video embedded; no quantitative results; repo not linked. · polish: Logo and console screenshots; page calls itself a proof of concept.
**Claims:** Won NVIDIA, Waymo and Microsoft awards at ShellHacks 2025
**Gaps:** no repo linked; video not watchable
Sources: https://devpost.com/software/vl-adk, sponsor_prompts_*.jsonl (ShellHacks 2025)

---

