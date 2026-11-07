# HackHarvard — HackHarvard 2024 (4 projects)

### Diabeteasy
*HackHarvard HackHarvard 2024 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 3rd Place Overall Hack [3rd]

**What it is:** A hardware prototype smart insole for type 2 diabetics with foot insensitivity: three homemade pressure sensors stream plantar pressure to a dashboard, alert patient and doctor, and a servo-driven shape-changing sole is meant to correct gait.
**Problem / user:** Type 2 diabetes patients with neuropathy at risk of foot ulcers and amputation; secondary users are remote-monitoring doctors and elderly-care firms.

**Features**
- Custom pressure sensors — Three force sensors made from PU foam and graphite, read by an ESP32/Arduino because suitable parts were unavailable. *[shown_working]*
- Live streaming dashboard — WebSocket data feeds a Next.js/React dashboard (Three.js visuals) showing activity, alerts and behavior data. *[claimed]*
- Irregularity alerts — Continuous processing flags abnormal pressure and notifies patient and doctor. *[claimed]*
- Shape-changing model sole — Servo-actuated sole adjusts based on gait analysis to correct stance. *[claimed]*
- Early neural degradation flagging — Data trends meant to alert doctors to early decline. *[claimed]*

**Flow:** Patient wears insole → Pressure data streams to server → Irregularity triggers alerts to patient and doctor → Sole reshapes to adjust gait → Doctor monitors dashboard remotely

**Prompt:** HackHarvard 2024 3rd Place Overall: third best overall hack, AirPods each; judged on innovation and impact, technical complexity, functionality and usability, collaboration and learning.
**Fit (none):** Hardware-plus-software healthcare prototype; no explicit prize targeting.  *(targeted: 3rd Place Overall Hack)*
**AI:** none
**Architecture:** Insole sensors to ESP32/Arduino firmware in C++, WebSocket stream to Node.js server and Next.js dashboard, servo actuating a cardboard model sole.
**Novelty:** Built its own foam-and-graphite force sensors and couples monitoring with active mechanical correction, uncommon for a software-heavy event.
**Scope:** small · working: Devpost describes custom sensors and connecting software; demo video linked but not viewed; no repo. · polish: Cardboard-and-tape prototype; no clinical data or metrics.
**Claims:** Reduces the risk of amputation | Real-time gait correction
**Gaps:** no repository; video not viewed; gait algorithm unspecified; no measurements
Sources: https://devpost.com/software/diabeteasy, https://hackharvard-2024.devpost.com/

---

### Garuda
*HackHarvard HackHarvard 2024 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 2nd Place Overall Hack [2nd]

**What it is:** A disaster-response web dashboard that analyzes drone and uploaded video with a vision-language model, annotates damage and rescue needs, maps live hot zones, and generates greener rebuilding plans and past-disaster reports.
**Problem / user:** Recovery teams, authorities and emergency services who need faster damage assessment and lower-carbon rebuilding after natural disasters.

**Features**
- Live hot-zone heatmap — Uploaded videos record hot zones through a Flask API; Google Maps heatmap updates, with a peer-to-peer network mentioned. *[claimed]*
- Drone damage analysis — MSNet and the Llava VLM annotate tree, road, roof and water damage. *[claimed]*
- Rescue and accessibility annotations — Marks people needing rescue and whether a team can reach by land; suggests cranes, ambulances, fire control. *[claimed]*
- Drowning alert — Flags a drowning subject in footage and calls rescue teams. *[claimed]*
- Green rebuild plans — Generates rebuilding plans considering carbon footprint. *[claimed]*
- Past-disaster reports — Shows recovery cost, carbon footprint and asset and life damage. *[claimed]*
- Energy-efficient routing — Uses Google Maps to route responders. *[claimed]*

**Flow:** Upload disaster or drone video → Hot zones recorded and heatmap updates → Models assess damage and rescue needs → Report with equipment suggestions generated → Open green rebuild plan or past reports

**Prompt:** HackHarvard 2024 2nd Place Overall: second best overall hack, Apple Watch SE each; judged on innovation and impact, technical complexity, functionality and usability, collaboration and learning.
**Fit (none):** Technically broad disaster-response system; no explicit prize targeting.  *(targeted: 2nd Place Overall Hack)*
**AI:** MSNet damage-assessment model on GPUs and the Llava vision-language model for video analysis, with OpenCV and TensorFlow.
**Architecture:** Next.js frontend, Flask Python backend with GPU model inference, Firebase for media storage, Google Maps for heatmaps and routing.
**Novelty:** Pairs drone damage analysis with recovery-side green planning and past-disaster reports, a broader scope than typical damage-detection demos.
**Scope:** medium · working: Repo 57 files, about 4.4k LOC frontend-heavy (no README); demo video linked, not viewed. · polish: Next.js UI components; no tests, README or live link.
**Claims:** Real-time damage assessment | Drowning detection calls rescue teams
**Gaps:** repo has no README; only file structure in evidence; video not viewed; no metrics; model integration not verified
Sources: https://devpost.com/software/garuda-pb7qtf, https://hackharvard-2024.devpost.com/

---

### MediGuide
*HackHarvard HackHarvard 2024 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Best first-time hack

**What it is:** MediGuide is a medication adherence system where a clinician enters a prescription, an LLM extracts drug and dosage, and the patient gets reminder calls or texts via Vapi voice AI with intake confirmation and check-ins.
**Problem / user:** Patients, especially seniors, who miss prescribed doses.

**Features**
- Clinician onboarding — Doctor enters prescription and preferred reminder method. *[claimed]*
- LLM prescription parsing — Extracts medication name and dosage. *[claimed]*
- Voice and text reminders — Vapi conversational calls with intake confirmation. *[claimed]*
- Check-ins — Periodic experience questions for adverse reactions. *[claimed]*
- Adaptive reminders — Learning from behaviour; predictive analytics. *[planned]*

**Flow:** Doctor enters prescription → AI schedules reminders → Patient gets call or text → Confirms intake → System checks in

**Prompt:** not public / not found
**Fit (none):** No stated targeting; first-time prize text not found.  *(targeted: Best first-time hack)*
**Sponsor tools:** Vapi (conversational voice reminders, core)
**AI:** LLMs (OpenAI) for prescription understanding and reminder text; Vapi voice AI.
**Architecture:** Next.js dashboard starter with Flask API, Prisma on Neon Postgres, Vapi.
**Novelty:** Voice-call delivery for low-tech users, clinician-led onboarding.
**Scope:** medium · working: Demo video; 11k LOC repo built on a dashboard template; no outcomes. · polish: Three screenshots; README is template-level.
**Claims:** Built in under 36 hours | 40-75% adults miss doses (cited)
**Gaps:** No first-time prize text
Sources: https://devpost.com/software/mediguide-c9qn3t, evidence/hackharvard-hackharvard-2024-mediguide.json, prompts_cache/hackharvard-2024.md

---

### Sustain-ify
*HackHarvard HackHarvard 2024 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Best Overall Hack [1st]

**What it is:** Mobile and web app with three assistants for everyday sustainability: scan household items for DIY upcycling ideas, scan products for eco ratings and greener alternatives, and upload health reports to get shopping advice that helps both health and environment.
**Problem / user:** General consumers who want practical ways to live sustainably; page ties planetary harm to declining personal health but names no narrower audience.

**Features**
- DIY Assistant that proposes upcycling projects for scanned household items — User scans an item; agents suggest repurposing ideas; creations can be shared in a community for rewards *[claimed]*
- Eco Shopping Assistant rates scanned products and suggests greener alternatives — Product scan feeds an eco-scan API using live web search and retrieval over crawled sustainability data *[claimed]*
- Health Reports analysis tied to sustainable shopping — Uploaded medical reports are stored and analyzed by LLMs to produce personalized recommendations *[claimed]*
- Real-time web crawling for current product information — LLM-generated queries go to Serper/Tavily search and ScrapeGraph.AI scraping *[claimed]*
- Retrieval pipeline with vector index and knowledge graph — Scraped data chunked with LangChain/LlamaIndex, embedded with BGE-Large, stored in MongoDB Atlas and Neo4j *[claimed]*
- Account sign-in with JWT-secured exchanges — Appwrite handles authentication and user management *[claimed]*
- Messaging and real-time updates via Twilio, Lamini, Firebase — Listed as future integrations *[planned]*

**Flow:** Sign in through Appwrite-backed account → Pick DIY Assistant, Eco Shopping Assistant or Health Reports → Scan a household item or product with the phone camera, or upload a medical report → Agents search the web and retrieve context, then LLMs generate ideas, ratings or recommendations → Share DIY creations to the community feed

**Prompt:** Best Overall Hack: top hack of HackHarvard 2024 (theme 'Hack 4 Impact'), judged on innovation/creativity/impact, technical complexity, functionality/usability, and collaboration/learning; prize was an iPad per winning member.
**Fit (implied):** Aligns with the 'Hack 4 Impact' theme through sustainability framing, and shows breadth of technical stack (multi-agent, RAG, knowledge graph, mobile app). No stated prize targeting.  *(targeted: Best Overall Hack)*
**AI:** Multi-agent system (CrewAI) using Gemini 1.5 Pro and GPT-4o with Groq-hosted inference; retrieval-augmented generation over scraped web data in a BGE-Large vector index plus Neo4j graph.
**Architecture:** Flutter and Streamlit clients call FastAPI/Node-Express services; Appwrite auth; scraping and search feed LangChain/LlamaIndex chunking into MongoDB Atlas vectors and Neo4j; LLM agents compose answers; Firebase stores reports.
**Novelty:** Combines three distinct sustainability workflows, including a health-report angle, in one agentic stack with an unusually large tool list (Neo4j, Groq, CrewAI, ScrapeGraph).
**Scope:** medium · working: Demo video and eight screenshots on Devpost; repo has about 3.1k lines across Flutter, FastAPI and scan pages; no live link. · polish: README has workflow diagram, setup steps and Figma prototypes; no tests; many listed tools not clearly integrated.
**Claims:** Addresses both environmental and personal well-being | Planned Twilio/Lamini/Firebase real-time messaging
**Gaps:** No written demo walkthrough; Video not watched; How each listed tool is used is not detailed
Sources: https://devpost.com/software/sustain-ify, https://github.com/SrikarVamsi/Sustain-ify (evidence file README), https://hackharvard-2024.devpost.com/

---

