# UC Berkeley AI Hackathon — 2025 (9 projects)

### AlphaRescue
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Fetch AI: Best Use of Fetch AI

**What it is:** An autonomous emergency-dispatch pipeline. A Vapi voice assistant takes a distress call, Gemini summarizes the transcript and screens for false alarms, Fetch.ai uAgents choose the nearest suitable hospital and ambulance type, and a live map dashboard shows incidents.
**Problem / user:** Callers in emergencies and dispatch authorities (mainly ambulance) who need fast, accurate triage; police and fire are future scope.

**Features**
- Voice emergency intake — Vapi assistant handles the call with scenario-based guidance *[claimed]*
- Transcript summary and false-alarm check — Gemini condenses the call into an incident brief and flags probable spam *[claimed]*
- uAgent coordination — Specialized Fetch.ai uAgents assess the case, check authority availability and plan a response *[shown_working]*
- Hospital ranking — RAG with Gemini over Supabase facility data plus geopy picks the nearest suitable hospital by emergency type *[claimed]*
- Ambulance type classification — Groq LLM labels the case BLS, ALS or CCT *[claimed]*
- Authority notification — Vapi calls out to notify the chosen facility *[claimed]*
- Live dashboard — React/Mapbox view of incidents, responders and dispatch outcome *[shown_working]*

**Flow:** Caller speaks to Vapi assistant → Gemini summarizes and flags false alarms → uAgents assess and check availability → Hospital ranked via RAG; ambulance type classified → Authorities notified by voice → Dashboard shows the incident

**Prompt:** Fetch AI: Best Use of Fetch AI: USD 3,000 cash across 3 winners; the prize page gives no descriptive text beyond the title.
**Fit (explicit):** Builds the dispatch decision layer as communicating Fetch.ai uAgents registered on AgentVerse, with orchestrator and per-task agents.  *(targeted: Fetch AI: Best Use of Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / AgentVerse (Autonomous agents for situation assessment, facility selection and dispatch, core); Vapi (Voice call intake and authority notification, core); Groq (Ambulance type classification, supporting)
**AI:** Gemini for summaries, spam detection and RAG hospital ranking; Groq LLM for BLS/ALS/CCT classification; Vapi voice; uAgents coordinate the steps.
**Architecture:** Vapi call to Python uAgent orchestrator and agents; Supabase holds facilities and embeddings; Node/Express plus React/Mapbox dashboard reads live state.
**Novelty:** End-to-end voice-to-dispatch chain made of cooperating agents with facility RAG; deliberate prank-call screening.
**Scope:** small · working: ~3.5k LOC repo with dashboard and agent folders and some tests; no demo or video. · polish: README lists setup and env; Devpost page text only; README also claims the Fetch prize.
**Claims:** Dispatch is autonomous with no manual steps | Groq classification has high accuracy (no figures)
**Gaps:** No demo video; Queue id groups with sibling projects HireSense and Mayday; this record covers AlphaRescue only
Sources: https://devpost.com/software/alpharescue, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-hiresense-mayday-alpharescue-alpharescue.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### Bair
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** Cal Hacks: Best Beginner Hack

**What it is:** A conversational budgeting coach for students. It sets daily and monthly budgets from income, expenses and goals, tracks savings streaks, parses uploaded PDF bank statements, and answers spending questions by text or voice, such as whether to buy a $70 concert ticket.
**Problem / user:** Students and young adults who lack guidance and structure with money; trackers show numbers but do not coach.

**Features**
- Automatic daily/monthly budgets — Analyzes income, expenses and goals to set budgets *[claimed]*
- AI purchase-decision coaching — LLM receives structured data (spending, streaks, goals) and replies in natural language *[claimed]*
- Streaks and rollover savings — Gamified tracking that feeds into advice *[claimed]*
- Voice finance Q&A — Vapi voice interaction for real-time questions *[claimed]*
- PDF bank statement parsing — Uploaded statements are parsed and transactions categorized *[claimed]*
- Budget food suggestions — Recommends meal deals and cheap places *[claimed]*

**Flow:** Enter income, expenses and goals or upload a PDF statement → App sets daily budget → Ask a question by text or voice → Coach answers using spending, streaks and goals

**Prompt:** Cal Hacks Best Beginner Hack: 1 winner receives AirPods Pro 2; no further description found.
**Fit (none):** No stated link; a full-stack AI app by presumably beginner team, but eligibility rules are not on the page.  *(targeted: Cal Hacks: Best Beginner Hack)*
**Sponsor tools:** Vapi (Voice interaction (use not explained on page), unclear); Groq / OpenAI (LLM advice (page inconsistent on provider), unclear)
**AI:** LLM prompted with structured budget data to act as a coach; page says GPT-4 in the text but lists Groq in tags.
**Architecture:** React/Tailwind mobile-first frontend; Flask API with LLM call; PDF parser for statements.
**Novelty:** Coach-style feedback with streaks and rollover rather than passive tracking.
**Scope:** small · working: Four screenshots; repo not retrievable (404). · polish: Detailed writeup; no demo or video; Plaid integration only planned.
**Claims:** Reasons through spending decisions like a human coach | No quantitative results
**Gaps:** Repo github.com/kaifanyu/CalHacks returns 404 and clone failed; Model provider inconsistent on page; Best Beginner eligibility text not found
Sources: https://devpost.com/software/bair, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### Cameron
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** GRAND PRIZE - Creativity Track; Nobel Era Group: Best Projects Leveraging LLM Agents Supported by Nobel Era Group & Berkeley RDI

**What it is:** A no-code camera orchestration tool: describe in plain language what to watch for and what to do, and a node-graph workflow is generated. Vision models run in the browser, Gemini and an LLM agent reason over events, and alerts go out by email, SMS, voice call or push.
**Problem / user:** Operators in retail, manufacturing, elder care and warehouses whose cameras only record; the tool closes the observe-interpret-act loop for non-technical users.

**Features**
- Natural-language workflow builder — Gemini 2.5 turns spoken or typed instructions into JSON node-graph configs *[claimed]*
- Drag-and-drop node graph editor — Connect events to actions visually; import/export JSON; LocalStorage persistence *[shown_working]*
- In-browser vision — YOLOv8 object detection and ArcFace identity via ONNX Runtime Web in Web Workers, with OpenCV preprocessing *[claimed]*
- Video and audio understanding — Gemini video scene analysis and speech-to-text *[claimed]*
- Multi-channel alerts — Email (EmailJS), SMS, Vapi voice calls with AI summaries, browser push, speech fallback *[claimed]*
- Chat with cameras and MCP tools — Ask about one or more cameras; Letta/Groq reasoning and Claude MCP orchestrate agents *[claimed]*
- Workflow logs — Record of triggered events *[claimed]*

**Flow:** Open the camera dashboard and pick a camera → Describe what to watch and what to do → Workflow graph is generated and can be edited → Live feed is analyzed in the browser → Condition triggers an alert or action → Review logs or chat with the camera

**Prompt:** Grand Prize Creativity Track: USD 5,000 cash for one winner, with API credits possible for a team chosen by VC panel. Nobel Era Group Best Projects Leveraging LLM Agents: USD 4,000 across three tiers, no description.
**Fit (implied):** Page lists both prizes; the LLM-agent angle is the Letta, Groq and Claude MCP agent orchestration that plans and acts on camera events.  *(targeted: GRAND PRIZE - Creativity Track, Nobel Era Group: Best Projects Leveraging LLM Agents)*
**Sponsor tools:** Letta (Reasoning and control flow with Groq API, supporting); Vapi (Voice-call alerts, supporting); Gemini (Workflow generation, video and speech understanding, core); Claude MCP (Multi-agent orchestration, supporting)
**AI:** Gemini 2.5 generates node graphs; Gemini video and STT interpret streams; YOLOv8 and ArcFace run in browser; Letta on Groq plus Claude MCP coordinate agents.
**Architecture:** React 19/TypeScript app with WebRTC video, Canvas, Web Workers running ONNX models; Gemini and agent APIs for reasoning; Vapi/EmailJS for notifications; workflows as JSON.
**Novelty:** Camera feeds become agent workflows built from plain language, with inference in the browser and no inference backend.
**Scope:** medium · working: Page describes a working prototype with visual editor and detection-to-action loop; screenshots only; repo not retrievable. · polish: Long detailed writeup and roadmap; no video or live demo.
**Claims:** Turns any existing camera into an AI agent | No backend inference required
**Gaps:** Repo ezpedersen/smartcam returns 404; clone failed; No performance numbers; Face recognition use: no consent or safeguards stated
Sources: https://devpost.com/software/cameron-9biv60, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### ChipChat
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** GRAND PRIZE - Productivity and Dev Tools Track

**What it is:** A web tool that turns a natural-language description or hand-drawn sketch of a circuit into Verilog, synthesizes it with Yosys, renders an interactive DigitalJS schematic, and pushes the design toward a fab-ready GDS file via OpenLane, with a chat assistant for questions.
**Problem / user:** Students learning logic design and engineers who spend long hours writing Verilog and iterating layouts.

**Features**
- Text or sketch to Verilog — Gemini orchestrated by a Letta agent converts a prompt or uploaded drawing into Verilog *[shown_working]*
- Interactive schematic — Yosys netlist rendered with DigitalJS; pan and inspect components *[shown_working]*
- Pipeline stage views — RTL, synthesized Verilog, place-and-route DEF and GDS layout *[claimed]*
- Chip development channel — Custom Verilog-to-DEF parser and OpenLane conversion produce a .GDS for manufacturers *[claimed]*
- Circuit assistant chat — Answers questions about the code or diagram in real time *[claimed]*

**Flow:** Type a circuit idea or upload a sketch → Gemini and Letta generate Verilog → Yosys synthesizes and DigitalJS draws the schematic → Explore code, schematic and ask the assistant → Optionally run the chip channel for GDS

**Prompt:** Grand Prize Productivity and Dev Tools Track: USD 5,000 cash for one winner; no further description.
**Fit (implied):** A developer tool for hardware design that compresses idea to Verilog to layout; the page gives no explicit track reasoning.  *(targeted: GRAND PRIZE - Productivity and Dev Tools Track)*
**Sponsor tools:** Letta (Agent memory, tool calls and pipeline coordination, core); Gemini (Verilog generation and image-to-text, core)
**AI:** Gemini writes Verilog from text or images; a Letta agent holds context and invokes tools; outputs validated by Yosys, with incomplete Verilog a noted failure mode.
**Architecture:** React/Vite frontend on Vercel; Python backend running Gemini/Letta, Yosys, a custom DEF parser and OpenLane; DigitalJS for visualization.
**Novelty:** Spans from natural language to a GDS layout file, including a self-written Verilog-to-DEF converter.
**Scope:** medium · working: Live Vercel demo and YouTube demo linked; no repo listed. · polish: Detailed writeup; claims whole flow runs in seconds.
**Claims:** Prompt to Verilog to visualization completes in seconds | End-to-end pipeline built in about 24 hours
**Gaps:** No GitHub repo linked; Video and live demo not opened; GDS output not verified
Sources: https://devpost.com/software/chitchat-5omgjw, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### DreamDirector
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Google: Best Use of Gemini; Nobel Era Group (truncated)

**What it is:** An interactive storyteller that takes a prompt and runs a branching story with generated images, 8-second Veo videos and adaptive Lyria music. A Google ADK multi-agent system (director, visual consistency, music, media orchestrator) keeps characters and world state consistent, and a gallery saves outputs.
**Problem / user:** Individual creators, students and hobbyists facing time and cost barriers to multimedia storytelling; studios are a secondary licensing target.

**Features**
- Prompt-to-world story — Story Director agent builds three-act structure and choices from any prompt *[shown_working]*
- Consistent image generation — Imagen 3.0 with character and location reference tracking *[shown_working]*
- Cinematic video moments — Veo 2.0 makes 8-second clips from image seeds at key scenes *[shown_working]*
- Adaptive music — Lyria RealTime streams layered soundtracks matching mood *[claimed]*
- Choices with persistent consequences — State carries relationships and world across scenes *[claimed]*
- Media gallery — Saves every generated image, video and track *[shown_working]*

**Flow:** Sign in and enter a story prompt → Agents generate scene, visuals and music → Choose among generated options → Video generated at key moments → Browse saved media in the gallery

**Prompt:** Google Best Use of Gemini: one winner receives Pixel Watches; no criteria text. Nobel Era Group LLM-agents prize: USD 4,000 in three tiers.
**Fit (explicit):** Uses Gemini, Imagen, Veo and Lyria through Google GenAI SDK and a four-agent ADK system; the agent angle matches the Nobel Era theme.  *(targeted: Google: Best Use of Gemini, Nobel Era Group: Best Projects Leveraging LLM Agents)*
**Sponsor tools:** Google Gemini / ADK (Story reasoning and agent orchestration, core); Imagen 3.0, Veo 2.0, Lyria RealTime (Images, video, music, core)
**AI:** Google ADK agents with structured function calls; Gemini reasons the narrative, Imagen/Veo/Lyria generate media with reference tracking and persistent state.
**Architecture:** React/Vite frontend, FastAPI async backend, Google ADK agents calling GenAI SDK models, media stored for a gallery.
**Novelty:** Combines text, image, video and streaming music generation in one interactive loop.
**Scope:** medium · working: README screenshots of landing, gameplay, video and gallery; YouTube demo; tests and Docker flagged; node_modules committed. · polish: Polished README and UI screenshots; claims 4K and 48kHz outputs.
**Claims:** First truly multimodal storytelling engine | 4K visuals and 48kHz audio | Hollywood-quality soundtracks in real time
**Gaps:** Queue prize string truncated; page lists both prizes; Roadmap: multiplayer, mobile, enterprise API
Sources: https://devpost.com/software/cinematic-director, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-dreamdirector.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### EduAgent
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Anthropic: Best Use of Claude 4

**What it is:** A six-agent CrewAI pipeline that turns a topic, PDF or image into a narrated Manim-animated explainer video. Claude writes scripts and animation code, LMNT supplies voice, and a quality-check agent sends videos back for fixes.
**Problem / user:** Educators and students who learn advanced topics from dense textbooks and lack accessible visual explanations.

**Features**
- Content extraction — Reads PDFs and images with OCR for text, diagrams and graphs *[claimed]*
- Lesson planning — Claude orders concepts and specifies visuals *[claimed]*
- Manim animation generation — Claude writes Manim code per script segment, with strict validation and error handling *[shown_working]*
- LMNT narration — Synthesized voiceover with timing cues for sync *[shown_working]*
- Video composition — MoviePy assembles animations, audio and transitions into MP4 *[shown_working]*
- Quality checker — Validates clarity, sync and pedagogy and requests adjustments *[claimed]*
- Gradio web interface and CLI — Run python web_interface.py on port 7860 *[claimed]*

**Flow:** Enter a concept or upload a document → Content extracted and lesson planned → Manim code and narration generated → Video composed and quality-checked → Download MP4

**Prompt:** Anthropic Best Use of Claude 4: one winner receives USD 2,500 in API credits; no description beyond that.
**Fit (explicit):** README lists Anthropic as the core content-analysis and generation integration; page says the team switched to Claude after other models produced broken Manim code.  *(targeted: Anthropic: Best Use of Claude 4)*
**Sponsor tools:** Anthropic Claude (Lesson planning, scripts and Manim code generation, core); LMNT (Narration, supporting)
**AI:** CrewAI orchestrates six agents; Claude plans and generates Manim code with validation; LMNT TTS; README also lists Google Vision OCR, Groq and Fetch.ai.
**Architecture:** Gradio UI to CrewAI crew (extractor, planner, Manim, narrator, composer, QA) passing structured JSON; renders with Manim and MoviePy.
**Novelty:** Closed loop of animation code generation, TTS timing and QA review, with JSON hand-offs carrying tone and pacing.
**Scope:** medium · working: Demo derivatives video on YouTube, demo_outputs and output_videos folders in repo; tests present. · polish: README with sponsor alignment; some README claims (Fetch.ai, cost savings) go beyond the page.
**Claims:** README: $500 to $0 and 10 hours to 10 minutes per video | LMNT latency under 300 ms (README)
**Gaps:** README claims (Fetch.ai, Vision OCR) not on Devpost page; Agent names differ between page sections
Sources: https://devpost.com/software/eduagent, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-eduagent.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### employAI
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Groq: Best Creative Use of Groq

**What it is:** A Flask web app with two tools for job seekers: personalized cold-email drafting from an uploaded resume, sent through the user's Gmail, and a mock interview coach that asks 10 resume-based questions and analyzes recorded spoken answers.
**Problem / user:** Students and early-career job seekers for whom repetitive, demoralizing applications crowd out coursework and other obligations.

**Features**
- Resume parsing — PyMuPDF extracts text and an LLM pulls key experiences *[claimed]*
- Cold email generation — LLaMA-3 on Groq writes email from company, recruiter name and email *[claimed]*
- Gmail sending — Google OAuth and Gmail API send real emails *[claimed]*
- Mock interview questions — 10 questions tailored to the resume and target job *[claimed]*
- Spoken answer analysis — Browser recording converted with FFmpeg; energy, entropy and zero-crossing rate features inform delivery feedback *[claimed]*
- Accounts and storage — Firebase auth, Firestore and storage *[claimed]*

**Flow:** Sign in and upload resume → Enter company and recruiter details → Generate and send cold email → Or choose a job and answer 10 recorded questions → Receive content and delivery feedback

**Prompt:** Groq Best Creative Use of Groq: USD 500 API credits, feature on Groq channels, office tour and guaranteed internship interview.
**Fit (implied):** Uses LLaMA-3 served by Groq for email and interview logic; the page does not describe how it counts as creative use.  *(targeted: Groq: Best Creative Use of Groq)*
**Sponsor tools:** Groq (LLaMA-3) (Email generation and interview logic, core)
**AI:** LLaMA-3 via Groq API for generation; hand-built acoustic features for delivery analysis rather than a speech model.
**Architecture:** Flask backend with Jinja2 templates, Firebase, PyMuPDF, FFmpeg, Groq API and Gmail API with OAuth.
**Novelty:** Pairs outreach sending with interview practice that scores audio signal features.
**Scope:** small · working: Claims real Gmail sends; ~3.3k LOC Flask repo with templates; no demo or video. · polish: README is a single title line; page is detailed.
**Claims:** End-to-end Gmail integration sends real cold emails
**Gaps:** README near empty; No demo; Planned: tone feedback, job scraping, difficulty levels
Sources: https://devpost.com/software/employ-ai, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-employ-ai.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### HireSense
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Fetch AI: Best Use of Fetch AI

**What it is:** A multi-agent hiring panel on Fetch.ai uAgents with ASI:One as LLM. Resume and job agents extract data, an evaluation agent scores fit, optimist and skeptic agents debate for multiple rounds, an arbiter judges, and a final agent recommends; results log to Supabase.
**Problem / user:** Recruiters and HR teams stuck with keyword-matching ATS tools that reject qualified candidates and reward buzzword stuffing.

**Features**
- Resume and job parsing agents — Extract skills, experience, certifications, requirements *[shown_working]*
- Evaluation agent — Compares the two and produces match score, gaps and strengths *[shown_working]*
- Optimist vs skeptic debate — Pro-hire and anti-hire agents argue three rounds *[shown_working]*
- Arbiter and final agent — Judges the debate and issues recommendation with confidence *[shown_working]*
- Supabase logging — Stores results and top candidates *[claimed]*
- Graceful fallbacks — README says it works even with API connection problems *[claimed]*

**Flow:** Submit resume and job description → Parsing agents extract fields → Evaluation agent scores → Debate rounds run → Arbiter and final agent recommend

**Prompt:** Fetch AI: Best Use of Fetch AI: USD 3,000 cash across 3 winners; the prize page gives no descriptive text beyond the title.
**Fit (explicit):** Whole system is distributed uAgents that talk to each other with ASI:One reasoning; page says the team's first use of uAgents.  *(targeted: Fetch AI: Best Use of Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents (Agent framework and messaging, core); ASI:One (LLM for agent reasoning, core)
**AI:** Seven role-specific agents prompt ASI:One for structured JSON output; adversarial debate gives explainable decisions; MCP listed for memory.
**Architecture:** Python/FastAPI backend with uAgents; Supabase; Next.js/Tailwind frontend listed; simple demo script for testing.
**Novelty:** Adversarial pro/con debate with arbiter in place of single-pass scoring.
**Scope:** medium · working: ~9.6k LOC with frontend and backend; demo script and Postman testing; no UI described, no video. · polish: README documents agents and flow; no tests.
**Claims:** Mimics a hiring committee with explainable decisions
**Gaps:** Queue id groups siblings; this record is HireSense only; Frontend completeness unclear
Sources: https://devpost.com/software/hiresense-x5j61u, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-hiresense-mayday-alpharescue-hiresense.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

### ICU
*UC Berkeley AI Hackathon 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Cal Hacks: Best Hardware Hack; Vapi: Best Hardware & Voice Integration

**What it is:** An assistive prototype for visually impaired users: a camera on a stepper-motor pan mount follows voice commands or pointing gestures, sends video to Gemini for scene description, and speaks back. A second fixed camera tracks the user's hand with MediaPipe.
**Problem / user:** Visually impaired people, especially elderly users, who lack environmental awareness; existing tools focus on text-to-speech.

**Features**
- Voice conversation — Vapi voice agent and local Whisper answer questions like what is in front of me *[claimed]*
- Pointing-gesture camera control — MediaPipe hand landmarks plus inverse kinematics convert pointing to pan direction *[shown_working]*
- Motorized camera — ESP-32 drives a stepper pan-tilt mount *[shown_working]*
- Scene analysis — Gemini identifies objects, hazards and text from live frames *[claimed]*
- Low-latency streaming — WebSockets link phone cameras, local ML and cloud inference *[claimed]*

**Flow:** Speak a command or point → Fixed camera reads hand pose → Moving camera turns toward target → Gemini analyzes video → Answer is spoken back

**Prompt:** Cal Hacks Best Hardware Hack: one winner gets Flipper Zeros. Vapi Best Hardware & Voice Integration: 750 Vapi credits plus swag.
**Fit (implied):** Combines ESP-32 motorized camera hardware with a Vapi voice agent; both prizes match the hardware-plus-voice design.  *(targeted: Cal Hacks: Best Hardware Hack, Vapi: Best Hardware & Voice Integration)*
**Sponsor tools:** Vapi (Two-way voice agent, core); Gemini (Visual analysis, core)
**AI:** Gemini for cloud visual inference, local Whisper for speech, MediaPipe for on-device hand landmarks, inverse kinematics for aiming.
**Architecture:** Phones and cameras stream via WebSockets to Flask and ML microservices; ESP-32 controls stepper; Vapi voice agent speaks results.
**Novelty:** Gesture-aimed camera for assistive scene description rather than OCR; tremor handling in elderly users noted.
**Scope:** small · working: Page claims first end-to-end test worked and near-real-time response; hardware, frontend, voice-agent folders in ~2k LOC repo; tests flagged. · polish: README with roadmap; no public demo; joke Built-With tags.
**Claims:** Near-real-time responsiveness (no latency figures) | Projected 70% footprint cut on Pi Zero 2 W (not measured)
**Gaps:** No demo video; Servo vs stepper wording inconsistent; No user testing yet
Sources: https://devpost.com/software/icu-2egdxy, evidence/uc-berkeley-ai-hackathon-uc-berkeley-ai-hackathon-2025-icu.json, https://uc-berkeley-ai-hackathon-2025.devpost.com/

---

