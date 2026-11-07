# UC Berkeley AI Hackathon: project cards (37 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## UC Berkeley AI Hackathon 2025

### AlphaRescue  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Fetch AI: Best Use of Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous emergency dispatch: a Vapi voice assistant takes distress calls, Gemini summarizes, and Fetch.ai uAgents pick the nearest hospital and ambulance type.
- **Problem / user:** Emergency response is time-critical, and dispatch needs faster, location-aware decisions with fewer false-alarm delays. / emergency dispatchers and first responders
- **Domain / idea type:** safety_security + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; Mapbox; v0.dev; backend Python; Node.js; pydantic; geopy; db Supabase; hosting Vercel
- **Tech/APIs:** Fetch.ai uAgents / Agentverse (framework, core, sponsor); Vapi (telecom, core, sponsor); Gemini (ai_model, core, sponsor); Groq (ai_model, core, sponsor); Supabase (database, core); Mapbox (maps_geo, supporting); v0.dev (other, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; Agentverse; Vapi; Gemini; Groq | fit: Built a network of Fetch.ai uAgents on Agentverse that summarize calls, choose facilities and notify authorities, interacting autonomously with each other.
- **Repo:** public, commits 5 (before/in/after event: 0/4/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Groq LLM classifies ambulance level (BLS, ALS, CCT); Gemini RAG over Supabase vectors ranks nearby facilities; Gemini flags spam calls; dashboard generated with v0 and Mapbox.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/alpharescue) | [GitHub](https://github.com/Preetam3620/Alpha-Rescue)

### Bair  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Cal Hacks: Best Beginner Hack [unknown]  (tier: track_winner)
- **Pitch:** Conversational budgeting coach that sets daily budgets, tracks savings streaks, and answers voice questions like whether to buy a concert ticket.
- **Problem / user:** Young people struggle with money due to lack of guidance, and budgeting apps track spending without coaching. / students and young adults
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend Next.js; React; Tailwind CSS; backend Flask; db ; hosting 
- **Tech/APIs:** OpenAI GPT-4 (ai_model, core); Groq (ai_model, unclear); Vapi voice (ai_model, supporting); Flask (framework, core); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Event-run Cal Hacks Best Beginner Hack award, not a sponsor challenge; page does not show a sponsor tool targeted.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Parses bank statement PDFs into categories; GPT-4 coaching prompt uses structured income, goal and streak data; Vapi voice interaction; Groq listed in the stack.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/bair) | [GitHub](https://github.com/kaifanyu/CalHacks)

### Cameron  (UC Berkeley AI Hackathon 2025)

- **Prizes:** GRAND PRIZE - Creativity Track [unknown]; Nobel Era Group: Best Projects Leveraging LLM Agents Supported by Nobel Era Group & Berkeley RDI [unknown]  (tier: track_winner)
- **Pitch:** No-code camera orchestration: describe what to watch for, and a node-graph workflow with in-browser vision models and LLM reasoning sends alerts or voice calls.
- **Problem / user:** Cameras only record; monitoring tasks need a loop of observe, interpret and act without constant human review. / operators of cameras in warehouses, retail, elder care
- **Domain / idea type:** ai_agents_infra + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend React 19; Tailwind CSS; React Router; ONNX Runtime Web; backend ; db LocalStorage; hosting 
- **Tech/APIs:** YOLOv8 (ONNX) (ai_model, core); ArcFace (ONNX) (ai_model, supporting); Google Gemini (ai_model, core); Letta + Groq (ai_model, core); Claude MCP (ai_model, supporting); Vapi (telecom, supporting); EmailJS (other, supporting); OpenCV (framework, supporting)
- **Sponsor APIs:** Letta; Groq; Vapi; Claude / MCP | fit: Uses Letta and Groq for LLM control flow and Claude MCP to coordinate multiple agents, matching the Nobel Era Group/Berkeley RDI LLM-agents prize theme.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Runs YOLOv8 and ArcFace via ONNX in the browser; workflows are visual node graphs generated from natural language or speech; alerts through Vapi voice calls and EmailJS.
- **Team size:** 4 | **Confidence:** medium | unverified: sponsor_apis_used; has_demo_video; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/cameron-9biv60) | [GitHub](https://github.com/ezpedersen/smartcam)

### ChipChat  (UC Berkeley AI Hackathon 2025)

- **Prizes:** GRAND PRIZE - Productivity and Dev Tools Track [unknown]  (tier: track_winner)
- **Pitch:** Natural-language or sketch-to-chip tool: Gemini and a Letta agent write Verilog, then Yosys, OpenLane and DigitalJS produce schematics and a fab-ready GDS file.
- **Problem / user:** Hardware design is slow and hard to learn; students and engineers struggle with Verilog and abstract diagrams. / electronics students and chip designers
- **Domain / idea type:** dev_tools + education / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision
- **Stack:** langs TypeScript; Python; Verilog; JavaScript; frontend React; Vite; DigitalJS; backend Node.js; Python; db ; hosting Vercel; Render
- **Tech/APIs:** Google Gemini (ai_model, core); Letta (framework, core); Yosys (framework, core); OpenLane (framework, core); DigitalJS (framework, core); KLayout (framework, supporting); Docker (cloud, supporting)
- **Sponsor APIs:** Letta
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Takes the whole flow from prompt or hand-drawn sketch to GDS layout; the team wrote a custom parser from synthesized Verilog to DEF; chat assistant explains the generated design.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; sponsor_apis_used; team_size
- **Links:** [Devpost](https://devpost.com/software/chitchat-5omgjw)

### DreamDirector  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Google: Best Use of Gemini; Nobel Era Group (truncated) [unknown]  (tier: sponsor_winner)
- **Pitch:** Interactive AI storyteller that turns a prompt into a branching story with generated images, short Veo videos and adaptive Lyria music, coordinated by multiple agents.
- **Problem / user:** The team wanted an immersive cinematic experience where narrative, visuals and music respond together in real time to the user's imagined world. / story and game enthusiasts
- **Domain / idea type:** creative_media + entertainment_games / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; Framer Motion; Axios; backend FastAPI; Uvicorn; Pydantic; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core, sponsor); Imagen 3 (ai_model, core, sponsor); Veo 2 (ai_model, core, sponsor); Lyria RealTime (ai_model, core, sponsor); Google ADK (framework, core, sponsor); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** Google Gemini; Imagen; Veo; Lyria; Google ADK | fit: Built the whole experience on Google's stack: Gemini for narrative, Imagen for images, Veo for video, Lyria for music, orchestrated with the Agent Development Kit.
- **Repo:** public, commits 9 (before/in/after event: 0/9/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** Multi-agent pipeline built on Google ADK using Gemini, Imagen, Veo and Lyria RealTime, with image consistency tracking and an auto-saved media gallery.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/cinematic-director) | [GitHub](https://github.com/Abdullah0x0/dreamdirector)

### EduAgent  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Anthropic: Best Use of Claude 4 [unknown]  (tier: sponsor_winner)
- **Pitch:** Six-agent CrewAI pipeline that turns a topic or document into a narrated Manim-animated educational video, using Claude for code and LMNT for voice.
- **Problem / user:** Manim-style explanatory animations like 3Blue1Brown's need heavy programming skill that educators and students lack. / educators and students
- **Domain / idea type:** education + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; generative_media; speech_or_voice
- **Stack:** langs Python; frontend ; backend CrewAI; Manim; db ; hosting 
- **Tech/APIs:** Claude (Anthropic) (ai_model, core, sponsor); CrewAI (framework, core); Manim (framework, core); LMNT voice (ai_model, core)
- **Sponsor APIs:** Claude | fit: Switched to Claude because it generated reliable Manim code from natural-language prompts, powering the animation and planning agents.
- **Repo:** public, commits 14 (before/in/after event: 0/14/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Specialized agents (extractor, lesson planner, Manim coder, LMNT narrator, composer, quality checker) coordinated by CrewAI; switched to Claude after other models produced buggy Manim; JSON inter-agent format.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; stack_frontend
- **Links:** [Devpost](https://devpost.com/software/eduagent) | [GitHub](https://github.com/A-Mundanilkunathil/EduAgent2025.git)

### Employ AI  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Groq: Best Creative Use of Groq [unknown]  (tier: sponsor_winner)
- **Pitch:** Job-search helper that drafts personalized cold emails from a resume and sends them via Gmail, plus a mock interview coach that analyzes spoken audio.
- **Problem / user:** Job applications are repetitive and demoralizing for students juggling coursework and internships. / students and job seekers
- **Domain / idea type:** productivity_workplace + education / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend Jinja2 templates; HTML; CSS; backend Flask; PyMuPDF; FFmpeg; NumPy; db Firebase Firestore; hosting Firebase
- **Tech/APIs:** Groq API (LLaMA-3) (ai_model, core, sponsor); Gmail API / Google OAuth (other, core); Firebase (Firestore, Auth, Storage) (database, supporting); FFmpeg (framework, supporting); PyMuPDF (framework, supporting); Flask (framework, core)
- **Sponsor APIs:** Groq | fit: Used LLaMA-3 through the Groq API for both cold-email generation and mock-interview question logic, handling rate limits with retries.
- **Repo:** public, commits 25 (before/in/after event: 0/24/1), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Mock interview feedback uses signal features (energy, entropy, zero-crossing rate) from FFmpeg-converted audio; LLaMA-3 on Groq generates emails and questions; real Gmail sending via OAuth.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/employ-ai) | [GitHub](http://github.com/ssridhar128/employAI)

### HireSense  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Fetch AI: Best Use of Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent hiring panel on Fetch.ai uAgents where resume, job, evaluation, optimist, skeptic and arbiter agents debate and recommend a candidate.
- **Problem / user:** Keyword-based applicant tracking systems reject qualified people and reward buzzword stuffing, while recruiters spend hours reviewing resumes. / recruiters and HR teams
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend Next.js; Tailwind CSS; backend FastAPI; db Supabase; hosting 
- **Tech/APIs:** Fetch.ai uAgents (framework, core, sponsor); ASI One (ai_model, core, sponsor); Model Context Protocol (framework, supporting); Supabase (database, supporting); FastAPI (framework, core)
- **Sponsor APIs:** Fetch.ai uAgents; ASI One | fit: Built each hiring-panel role as a Fetch.ai uAgent and used ASI One for the agents' reasoning and debate arguments.
- **Repo:** public, commits 46 (before/in/after event: 0/30/16), README none
- **Demo/writeup:** video True, live none, screenshots 0, writeup long, impact claims False
- **Notes:** Debate engine with optimist, skeptic and arbiter agents; agents modularized with uAgents, reasoning from ASI One, MCP for communication; run locally and tested through Postman.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/hiresense-x5j61u) | [GitHub](https://github.com/Jaysuun01/AIBerkHack.git)

### ICU  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Cal Hacks: Best Hardware Hack; Vapi: Best Hardware & Voice Integration [unknown]  (tier: track_winner)
- **Pitch:** Wearable-style camera on a stepper-motor mount that follows voice or pointing commands, analyzes surroundings with Gemini and MediaPipe, and answers aloud for visually impaired users.
- **Problem / user:** Existing aids for vision loss focus on text-to-speech rather than awareness of the environment, leaving users dependent on caregivers. / visually impaired and elderly users
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_ios / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; C++; frontend ; backend Python; db ; hosting 
- **Tech/APIs:** Vapi (ai_model, core, sponsor); Google Gemini (ai_model, core); MediaPipe (ai_model, core); OpenCV (framework, supporting); OpenAI GPT (ai_model, supporting); Arduino / ESP32 (hardware_part, core); Stepper motor (hardware_part, core)
- **Sponsor APIs:** Vapi | fit: Combined a motorized camera with Vapi voice interaction so users steer and query the device by speech, targeting Vapi's hardware-and-voice prize and Cal Hacks' hardware prize.
- **Repo:** public, commits 28 (before/in/after event: 0/28/0), README solid
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Motorized camera (Arduino/ESP32, stepper motor) steered by voice or hand pointing, with local MediaPipe hand landmarks plus Gemini and Vapi voice replies; video on page is a playlist embed.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/icu-2egdxy) | [GitHub](https://github.com/vyomfadia/berkeley)

### MayDay  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Fetch AI: Best Use of Fetch AI [unknown]; Unify: Best Use of Multimodal AI Agent [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-augmented air traffic control assistant that transcribes live ATC audio with a fine-tuned Whisper model, flags anomalies with agents and phones first responders.
- **Problem / user:** Controllers juggle dozens of simultaneous aircraft communications, creating heavy cognitive load and safety risk. / air traffic controllers
- **Domain / idea type:** safety_security + mobility_transport / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; WebSocket; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents / Agentverse / ASI:One (framework, core, sponsor); Groq (fine-tuned Whisper for ATC) (ai_model, core, sponsor); Vapi (telecom, supporting, sponsor); Letta memory (other, supporting, sponsor); Gemini (ai_model, supporting); Claude 4 (ai_model, supporting, sponsor); FastAPI (framework, core)
- **Sponsor APIs:** Fetch.ai uAgents; Agentverse; ASI:One; Groq; Vapi; Letta; Claude; Gemini | fit: Built the transcription, parsing and emergency-detection workflow as distributed Fetch.ai uAgents using Agentverse and ASI:One, with Vapi, Letta and other multimodal AI services integrated.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Aviation-tuned Whisper on Groq transcribes 5-second chunks of live ATC streams; Fetch.ai uAgents plus Vapi calls for emergencies; Letta memory for shift handoff; one teammate is a pilot.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/mayday-l74dub) | [GitHub](https://github.com/hunter-nguyen/ai-berkeley-2025)

### MayDay  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Unify: Best Use of Multimodal AI Agent [unknown]; Fetch AI: Best Use of Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-driven assistant for air traffic controllers that transcribes live ATC radio, structures it with LLMs, and uses agents to flag emergencies and call first responders.
- **Problem / user:** Controllers juggle many aircraft and instructions at once, and the cognitive load raises the risk of missed conflicts and runway incursions. / air traffic controllers
- **Domain / idea type:** safety_security + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; WebSocket; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents / AgentVerse / ASI:One (framework, core, sponsor); Vapi (telecom, core, sponsor); Letta (ai_model, supporting, sponsor); Groq (ai_model, core, sponsor); Whisper (ATC fine-tune) (ai_model, core); Gemini (ai_model, supporting); Claude (ai_model, supporting); FastAPI (framework, core); Next.js (framework, core)
- **Sponsor APIs:** Fetch.ai uAgents; Vapi; Letta; Groq | fit: Built a multi-agent ATC pipeline on Fetch.ai uAgents plus Vapi phone alerts and Letta memory with LLMs for the multimodal-agent challenge; Unify use itself is not named on the page.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Uses a Whisper model fine-tuned for aviation radio with Groq inference, streams 5-second audio chunks over WebSocket, and triggers a Vapi phone call to first responders on detected emergencies.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/mayday-l74dub) | [GitHub](https://github.com/hunter-nguyen/ai-berkeley-2025)

### MediBuddy  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Vapi: Best Voice-Powered AI Project [unknown]  (tier: sponsor_winner)
- **Pitch:** Healthcare app that transcribes doctor-patient visits by voice, summarizes them, and uses agents to match patients to clinical trials with explicit patient consent.
- **Problem / user:** Clinical trials go under-enrolled because patients and busy doctors rarely have time to check eligibility during appointments. / patients and doctors
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; Tailwind CSS; backend Convex; db Convex; hosting Vercel
- **Tech/APIs:** Groq Whisper v3 Large Turbo (ai_model, core, sponsor); Google Gemini (ai_model, core); ASI-1 (Fetch.ai) (ai_model, core, sponsor); Convex (database, core); React (framework, supporting); Tailwind CSS (framework, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** Groq; Fetch.ai ASI-1 | fit: Voice-to-text transcription of doctor visits via Groq Whisper; the page lists no Vapi integration, so the Vapi fit is not shown.
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup long, impact claims False
- **Notes:** Separate doctor and patient dashboards, consent flow before data goes to simulated sponsor agents built with ASI-1; Groq Whisper transcription feeds Gemini structured summaries.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/medibuddy-y7t65f) | [GitHub](https://github.com/darshanpatel44/MediBuddy-AI)

### Navo  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Nobel Era Group: Best Projects Leveraging LLM (truncated) [unknown]  (tier: sponsor_winner)
- **Pitch:** AI route planner that turns a simple prompt (fitness loop, scenic drive, foodie crawl) into a tailored route using Google Maps data and LLMs.
- **Problem / user:** Standard map apps give fastest routes but not routes tailored to a free-form goal or mood. / travelers and fitness users
- **Domain / idea type:** mobility_transport + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web; mobile_ios / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; Swift; TypeScript; JavaScript; frontend Swift; backend Python; db ; hosting Replit
- **Tech/APIs:** Google Maps Directions API (maps_geo, core); Google Geocoding API (maps_geo, supporting); OpenAI (ai_model, core); ASI1 (Fetch.ai) (ai_model, unclear); Fetch.ai (ai_model, unclear); Cursor (other, token)
- **Sponsor APIs:** Fetch.ai; ASI1 | fit: Targeted Nobel Era Group's best LLM project prize with an LLM-driven route planner; the writeup shown does not describe how Nobel Era's offering was used.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup short, impact claims False
- **Notes:** Page text is only a closing roadmap (App Store MVP); purpose inferred from the title and tags. Built-with lists Fetch.ai, ASI1, Google Maps, Directions, Geocoding, OpenAI and Swift.
- **Team size:** 3 | **Confidence:** medium | unverified: problem_statement; target_user; ui_polish; sponsor_fit_note; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/navi-google-maps-but-better)

### Octavo  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Orkes: Best Use of Orkes [unknown]  (tier: sponsor_winner)
- **Pitch:** A search engine over shared human experience: each user has a Letta memory agent, and Orkes workflows orchestrate agents to answer nuanced questions from collective memories.
- **Problem / user:** Web search returns generic pages and misses the lived experience of people who solved similar problems. / people seeking experience-based advice
- **Domain / idea type:** ai_agents_infra + social_community / new_category
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; backend Python; db ; hosting Vercel
- **Tech/APIs:** Orkes Conductor (other, core, sponsor); Letta (ai_model, core); Anthropic Claude (ai_model, core); Groq (ai_model, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Orkes | fit: Used Orkes workflows to orchestrate multiple Letta memory agents in parallel for cross-domain queries, with dynamic agent selection and real-time workflow visualization.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 19, writeup long, impact claims False
- **Notes:** Per-user Letta agents feed domain-specific collective agents; Orkes runs parallel retrieval, pattern recognition and synthesis with a live workflow visualization; memory has version history for temporal queries.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/octopus-pzv5l0)

### pFOG: Parkinson's Medical Aid Device  (UC Berkeley AI Hackathon 2025)

- **Prizes:** GRAND PRIZE - Social Impact Track [unknown]; Cal Hacks: Hacker's Choice [unknown]  (tier: track_winner)
- **Pitch:** Wearable that predicts Parkinson's freezing of gait from IMU data with a CNN-LSTM and triggers a servo 'poke' stimulation, plus a web tool to label data and fine-tune.
- **Problem / user:** Parkinson's patients suffer sudden freezing of gait; a family's manual leg poke helped, inspiring an automated version. / Parkinson's patients with freezing of gait
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / predictive_ml
- **Stack:** langs Python; frontend Next.js; React; backend Flask; db ; hosting Google Cloud
- **Tech/APIs:** PyTorch 1D-CNN + LSTM (ai_model, core); Adafruit MPU-6050 IMU (hardware_part, core); ESP32 (hardware_part, core); Servo-actuated arm (hardware_part, core); Flask (framework, supporting); Google Cloud (cloud, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 58 (before/in/after event: 0/57/1), README detailed
- **Demo/writeup:** video None, live none, screenshots 3, writeup medium, impact claims True (Claims over 90% accuracy detecting freezing episodes on the prototype.)
- **Notes:** Working prototype with MPU-6050 sensor, ESP32 and servo-actuated arm; team 3D-printed parts using another team's printer; per-patient fine-tuning via a web labeling interface.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/foggy) | [GitHub](https://github.com/harryyuncheng/parkinsons-fog-device)

### Vocal AI  (UC Berkeley AI Hackathon 2025)

- **Prizes:** Vapi: Most Ambitious Vapi Project [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-coaching platform that analyzes recordings, generates lesson plans, tracks progress and offers live practice and conversational coaching through Vapi voice agents and Letta memory.
- **Problem / user:** Vocal training is fragmented across tools; learners need personalized analysis, lessons and feedback in one place. / singers and voice learners
- **Domain / idea type:** education + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** web / False / speech_or_voice; agent_or_tool_use; llm_chat; recommendation
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend FastAPI; db Supabase; hosting Netlify; Docker; Google Cloud
- **Tech/APIs:** Vapi (ai_model, core, sponsor); Letta (ai_model, core); Groq (ai_model, supporting); Supabase (database, supporting); FastAPI (framework, supporting); React (framework, supporting); Netlify (cloud, supporting); Bolt (other, token)
- **Sponsor APIs:** Vapi | fit: Used Vapi as the voice layer for real-time vocal coaching sessions inside a larger agent-based coaching platform.
- **Repo:** public, commits 180 (before/in/after event: 0/130/50), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 27, writeup long, impact claims False
- **Notes:** Multimodal coach with dashboard, lessons, practice analysis and a live coach session; Letta provides agent memory and Vapi the voice layer; writeup reads like a README overview.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/vocai-ai-coach) | [GitHub](https://github.com/ramizik/berkley-hack)


## UC Berkeley AI Hackathon 2026

### AeroFreight AI  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Turns a natural-language international shipping request into a structured freight plan to the US, with an orchestrator agent coordinating specialist agents and generating an invoice PDF.
- **Problem / user:** Planning cross-border freight from cargo, value and preferences is manual; the tool converts a plain-language request into a priced plan. / shippers and freight forwarders
- **Domain / idea type:** mobility_transport + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend ; backend uAgents; Bureau; Pydantic; db ; hosting GCP
- **Tech/APIs:** Fetch.ai Agentverse / uAgents (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Anthropic Claude (ai_model, supporting); Stripe (payments, supporting); Google Cloud (cloud, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One; uAgents | fit: Exposed an orchestrator agent through ASI:One that coordinates several Agentverse agents to produce a freight plan, as documented in its Fetch.ai track submission.
- **Repo:** public, commits 62 (before/in/after event: 0/61/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Submission lists an ASI:One workflow and Agentverse profiles including a central orchestrator agent; uses Stripe for payment and produces an invoice PDF.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/aerofreight-ai) | [GitHub](https://github.com/aniketggg/AeroFreight-AI)

### AgriBroker  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous produce procurement marketplace: a buyer asks in plain language, and agents discover seller agents, compare inventory and prices, and arrange the cheapest fulfillment.
- **Problem / user:** Buyers sourcing produce must manually compare many sellers' stock and prices to meet a quantity and budget. / produce buyers and sellers
- **Domain / idea type:** retail_consumer + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend ; backend uAgents; db ; hosting 
- **Tech/APIs:** Fetch.ai Agentverse (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Stripe (payments, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One | fit: Built a marketplace of discoverable buyer and seller agents on Agentverse, driven by natural-language requests through ASI:One.
- **Repo:** public, commits 6 (before/in/after event: 0/6/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Buyer, seller and broker agents registered on Agentverse and reachable through a shared ASI:One chat; Stripe is used for settlement.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/agribroker) | [GitHub](https://github.com/Ai-Hackathon-2026-Berk/AgriBroker)

### baymax  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Network of per-hospital Fetch.ai agents that fuse inventory, weather and disease signals to predict shortages and have Claude negotiate and settle supply transfers between facilities.
- **Problem / user:** Hospitals discover supply shortages only when inventory is critical, and inter-facility resupply is slow and manual. / hospital supply managers
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; llm_chat; predictive_ml; vision
- **Stack:** langs Python; JavaScript; frontend HTML5; JavaScript; backend Python; db Redis; hosting 
- **Tech/APIs:** Fetch.ai agents (ai_model, core, sponsor); Anthropic Claude (ai_model, core); Arize (other, supporting); Poke (other, unclear); Redis (database, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse | fit: Built each hospital's autonomous negotiation agent on Fetch.ai, with agents settling inter-facility supply transfers.
- **Repo:** public, commits 52 (before/in/after event: 0/52/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** One agent per hospital combining edge-vision inventory counts, weather forecasts and historical surge patterns, with Arize observability and Redis state.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/baymax-1wumi3) | [GitHub](https://github.com/apollo-ullah/Baymax)

### CareLoop  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice or text health concern triaged by an orchestrator of Fetch.ai agents that route emergencies to 911, find nearby providers, estimate out-of-pocket cost and guide booking.
- **Problem / user:** Finding appropriate care, its cost and booking an appointment is fragmented across many steps for patients. / patients seeking care
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; JavaScript; backend FastAPI; Fetch.ai uAgents; Uvicorn; Pydantic; db Redis; hosting 
- **Tech/APIs:** Fetch.ai uAgents (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Deepgram (ai_model, core); CMS NPPES API (data_source, core); Stripe (payments, supporting); Redis (database, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; Fetch.ai ASI:One | fit: Built an orchestrator agent coordinating specialist triage and provider-search uAgents through ASI:One.
- **Repo:** public, commits 44 (before/in/after event: 0/44/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Specialist agents for triage and provider search use CMS NPPES provider data; Deepgram handles voice; a short writeup with no screenshots or video.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/careloop-gsiy8w) | [GitHub](https://github.com/VishalDani1602/AIHACK26.git)

### Constructa  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard for contractors that scores undeveloped land by feasibility, then turns a described build into a 3D model, permit guidance and a project timeline using Fetch.ai agents.
- **Problem / user:** Choosing where to build and navigating permits and regulations is slow and fragmented for contractors and project managers. / contractors and project managers
- **Domain / idea type:** housing_real_estate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; rag_or_search; generative_media
- **Stack:** langs TypeScript; Python; JavaScript; frontend React 19; TanStack Start; Tailwind CSS; MapLibre GL; deck.gl; react-three-fiber; GSAP; backend Node.js; Hono; FastAPI; db Redis; hosting 
- **Tech/APIs:** Fetch.ai Agentverse (ai_model, core, sponsor); Fetch.ai ASI:One (ai_model, core, sponsor); Anthropic Claude SDK (ai_model, supporting); Browserbase (other, supporting); Arize (other, supporting); MapLibre GL / deck.gl (maps_geo, core); react-three-fiber (framework, supporting); Redis (database, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One | fit: Routed land guides, compliance plans and 3D models through ASI:One as lead orchestrator over six custom Agentverse agents that produce a buy/hold/avoid call.
- **Repo:** public, commits 38 (before/in/after event: 0/35/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims False
- **Notes:** ASI:One orchestrates six uploaded Agentverse agents into a buy/hold/avoid verdict; map and 3D UI uses MapLibre, deck.gl and react-three-fiber, with Browserbase scraping and Arize observability.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split
- **Links:** [Devpost](https://devpost.com/software/constructa) | [GitHub](https://github.com/vynx1/Constructa)

### Fetch Health  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Hospital-staff simulator for donor and recipient intake and matching: staff upload medical files, agents process cases, report results and produce a voice debrief.
- **Problem / user:** Organ or donor matching intake involves heavy document processing; the tool simplifies staff intake while agents do the analysis. / hospital transplant and intake staff
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; llm_chat; speech_or_voice; rag_or_search
- **Stack:** langs Python; Shell; frontend React; backend ; db Redis; hosting 
- **Tech/APIs:** Fetch.ai agents (ai_model, core, sponsor); Anthropic Claude (ai_model, core); Deepgram (ai_model, supporting); Redis (database, supporting); Sentry (other, token); React (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse | fit: Used Fetch.ai agents as the public-facing agent layer in front of local processing for intake and matching.
- **Repo:** public, commits 11 (before/in/after event: 0/11/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Fetch.ai agents are the public agent layer while heavy processing runs on a local backend; Deepgram supplies the voice debrief; Midjourney and Sentry also listed in the stack.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/fetch-health) | [GitHub](https://github.com/abhinavprkash/Fetch-Health.git)

### Fireflai  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Dispatch console that takes a property link and 911 call text, then reconstructs a 3D model and 360-degree view of the home interior from listing photos to brief firefighters.
- **Problem / user:** Firefighters arriving at a burning home lack knowledge of its layout and where trapped occupants may be. / 911 dispatchers and firefighters
- **Domain / idea type:** safety_security + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; vision; generative_media; llm_chat; speech_or_voice
- **Stack:** langs ; frontend ; backend uAgents; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents / Agentverse (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Browserbase (other, supporting); Deepgram (ai_model, supporting); Arize (other, supporting); Aura (other, unclear)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One; uAgents | fit: Built six stage agents and a coordinator on Agentverse that can be @-mentioned from ASI:One, which also parses the 911 call text and writes the briefing.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Six stage agents plus a coordinator on Agentverse; ASI:One parses the call text and writes the briefing; Browserbase scrapes listing photos, Deepgram voice, Arize tracing.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/fireflai) | [GitHub](https://github.com/Hrishikesh-Athreya/fireflai/tree/final-code)

### FirstResponder-Relay  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Multilingual AI overflow dispatcher: callers speak any language, Claude triages urgency and checks wildfire perimeters, dispatchers reply in English that is translated back as voice.
- **Problem / user:** Emergency dispatchers cannot cover many languages during disasters when call volume spikes. / 911 dispatchers and non-English-speaking callers
- **Domain / idea type:** safety_security + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; Mapbox GL JS; backend FastAPI; WebSockets; db Redis Cloud; hosting Vercel; ngrok
- **Tech/APIs:** Claude Sonnet 4.6 (ai_model, core); Deepgram Nova-3 (ai_model, core); Deepgram Aura-2 (ai_model, supporting); Mapbox (maps_geo, core); Shapely (framework, supporting); Redis (database, supporting); Arize AX (other, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup medium, impact claims True (Cites 2018 Camp Fire call volume and Bay Area language statistics, plus its own eval accuracy numbers.)
- **Notes:** Reports a 30-case eval (90% urgency, 100% language and address accuracy) and tests 13 languages; Claude traces streamed to Arize; callers join via QR code.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/firstresponder-relay)

### Inspector  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]; Hacker's Choice Award [unknown]  (tier: honorable_or_finalist)
- **Pitch:** MCP server that lets coding agents autonomously test their own apps via computer use in cloud sandboxes, with parallel region agents and verified bug reports.
- **Problem / user:** AI coding agents hand back untested code, leaving developers to act as QA and report bugs manually. / developers using coding agents such as Claude Code or Cursor
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; cli; desktop / False / agent_or_tool_use; vision; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; Framer Motion; backend FastMCP; httpx; Pydantic; db ; hosting E2B sandboxes
- **Tech/APIs:** Anthropic Claude API (ai_model, core); FastMCP (framework, core); E2B Desktop sandbox (cloud, core); OmniParser (YOLOv8 + Florence-2) (ai_model, core); Replicate API (ai_model, supporting); Devin (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 95 (before/in/after event: 0/60/35), README detailed
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims True (Cites a claimed 41% rise in bug rates with AI coding agents as motivation; no measured results.)
- **Notes:** Splits the UI into regions with OmniParser, runs one agent per region, and confirms each finding by independent replay; supports web, Electron, Android and iOS; dashboard can hand bugs to Devin.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/inspector-23ser6) | [GitHub](https://github.com/wlu03/LoopBack)

### IronBook  (UC Berkeley AI Hackathon 2026)

- **Prizes:** GRAND PRIZE - Ddoski's Toolbox Track [unknown]; Finalist [unknown]  (tier: track_winner)
- **Pitch:** Photograph a machine from many angles to build a 3D Gaussian splat, then ask a Claude agent that flies the camera and highlights parts, to capture retiring experts' knowledge.
- **Problem / user:** Retiring skilled manufacturing workers take undocumented know-how with them, and apprenticeships are too slow. / manufacturing technicians and shop-floor trainers
- **Domain / idea type:** productivity_workplace + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React 18; Vite; WebGL2; backend FastAPI; Uvicorn; db MongoDB; hosting 
- **Tech/APIs:** Claude (vision, structured output) (ai_model, core); COLMAP (framework, core); msplat (Metal 3DGS) (framework, core); Deepgram (ai_model, supporting); Sentry (other, supporting); Langfuse (other, supporting); depth-anything ONNX (ai_model, supporting)
- **Sponsor APIs:** Deepgram; Sentry; Langfuse
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots None, writeup long, impact claims True (Cites retirement and workforce-gap statistics (e.g. 4.1M workers retiring by 2027, 584,000 unfilled jobs).)
- **Notes:** Custom WebGL2 Gaussian-splat renderer; Claude sees a live viewport screenshot and returns camera actions; three-tier reconstruction fallback (COLMAP/msplat, MLX, depth-anything); 77 tests claimed.
- **Team size:** 3 | **Confidence:** medium | unverified: sponsor_apis_used; stack_database; has_demo_video; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/ironbook)

### LifeLink  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent blood coordination network on Fetch.ai where clinicians request units in natural language through ASI:One and specialized agents source and arrange supply.
- **Problem / user:** Hospitals coordinating urgent blood supply rely on structured forms and manual processes; this lets clinicians simply ask in plain language. / clinicians and hospitals
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend uAgents; Pydantic AI; MCP; db MongoDB Atlas; hosting 
- **Tech/APIs:** Fetch.ai Agentverse / uAgents (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Pydantic AI (framework, supporting); MCP (framework, supporting); MongoDB Atlas (database, supporting); Stripe (payments, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One; uAgents | fit: Built the entire product as a network of Fetch.ai agents whose only interface is ASI:One natural-language chat.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Sole interface is ASI:One chat; network of uAgents on Agentverse coordinated with Pydantic AI, MCP and Stripe/UCP-style payment pieces listed in the stack.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/lifelink-soibwr)

### Lucid Voice  (UC Berkeley AI Hackathon 2026)

- **Prizes:** GRAND PRIZE - Ddoski's World Track [unknown]; Finalist [unknown]  (tier: track_winner)
- **Pitch:** Offline AAC tool that turns two or three tapped words into a full sentence in the user's own cloned voice, using an on-device knowledge graph and local Gemma model.
- **Problem / user:** People with ALS, stroke or aphasia have slow, robotic communication tools that do not know who they are talking to. / people who cannot rely on their own speech (AAC users)
- **Domain / idea type:** accessibility + health_wellness / social_good
- **Platforms / hardware / AI:** web; desktop / False / llm_chat; speech_or_voice; rag_or_search; recommendation
- **Stack:** langs Python; TypeScript; JavaScript; frontend React; Vite; Tailwind CSS; Framer Motion; react-force-graph; backend FastAPI; db Kuzu; Redis; hosting 
- **Tech/APIs:** Gemma via MLX (ai_model, core); Coqui XTTS (ai_model, core); Whisper / faster-whisper (ai_model, core); Kuzu graph database (database, core); Redis (database, supporting); Deepgram (ai_model, token); Sentry (other, token); Arize Phoenix (other, supporting); Claude Code (other, token)
- **Sponsor APIs:** Redis; Deepgram; Sentry; Arize Phoenix
- **Repo:** public, commits 42 (before/in/after event: 0/42/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims True (Cites about 5 million Americans and nearly 100 million people worldwide who cannot rely on their own voice.)
- **Notes:** Runs fully on-device and offline on Apple Silicon: Kuzu knowledge graph, Gemma via MLX, XTTS voice cloning, Whisper; visible learning graph; interview mode to cold-start the profile.
- **Team size:** 2 | **Confidence:** medium | unverified: sponsor_apis_used; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/lucid-voice) | [GitHub](https://github.com/dbhargav-uw/Lucid-Voice)

### Paper Cuts  (UC Berkeley AI Hackathon 2026)

- **Prizes:** GRAND PRIZE - Ddoski's Playground Track [unknown]; Finalist [unknown]; Best UI/UX [unknown]  (tier: track_winner)
- **Pitch:** Draw on an iPad or browser and your doodles are recognized, restyled into sprites and given game mechanics, then dropped into a live phone-controlled platform fighter.
- **Problem / user:** Most people only consume games; making one requires a complex engine, so the team wanted creation to feel like drawing on paper. / kids and casual creators
- **Domain / idea type:** entertainment_games + creative_media / creative_tool
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; generative_media; rag_or_search; llm_chat
- **Stack:** langs Python; JavaScript; frontend React; Vite; tldraw; HTML5 Canvas; backend FastAPI; Node.js; db Redis Stack (RediSearch HNSW); hosting AWS Trainium
- **Tech/APIs:** Redis Stack vector search (database, core, sponsor); Stable Diffusion / InstructPix2Pix (ai_model, core); Pika via fal.ai (ai_model, supporting); AWS Trainium (cloud, supporting); rembg / BiRefNet (ai_model, supporting); OpenAI (ai_model, unclear); tldraw (framework, supporting)
- **Sponsor APIs:** Redis; fal.ai; AWS Trainium | fit: Page labels Redis as a sponsor track and uses RediSearch HNSW as the doodle memory powering retrieval-augmented recognition.
- **Repo:** public, commits 148 (before/in/after event: 0/148/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Multi-model stack: CNN plus VLM plus Redis vector retrieval for recognition, a trained image-to-image sprite model, neuro-symbolic mechanic composer, generative KO videos; phones act as gamepads or pens via QR.
- **Team size:** 3 | **Confidence:** medium | unverified: sponsor_apis_used; has_demo_video; stack_hosting
- **Links:** [Devpost](https://devpost.com/software/paper-cuts) | [GitHub](https://github.com/Jeremyliu-621/paper-cuts)

### Percept  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Self-improving video ad loop: researches, generates short ads with Pika, predicts attention with TRIBE v2, and rewrites one creative lever per round using Redis memory.
- **Problem / user:** Small businesses spend ad budget before learning which video works; dashboards show failure but not why attention dropped. / small business owners running short-form video ads
- **Domain / idea type:** creative_media + retail_consumer / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media; agent_or_tool_use; predictive_ml; rag_or_search; vision
- **Stack:** langs TypeScript; Python; frontend ; backend Node.js; db Redis; Supabase; hosting Vercel
- **Tech/APIs:** Pika MCP (ai_model, core, sponsor); Redis (database, core, sponsor); TRIBE v2 (ai_model, core); Claude (ai_model, supporting); FFmpeg (framework, supporting); OpenCV (framework, supporting); YOLO (ai_model, unclear); Supabase (database, unclear)
- **Sponsor APIs:** Pika; Redis
- **Repo:** public, commits 113 (before/in/after event: 0/113/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Scores ads from a predicted neural-response time series (TRIBE v2) turned into a custom attention score; limits each rewrite to one lever; admits score is a proxy not campaign performance.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/cerebra-diqop9) | [GitHub](https://github.com/edrlu/Percept)

### Quorum : drop-in validation layer for multi-agent AI Systems  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Drop-in validation layer that intercepts factual claims in a multi-agent pipeline, runs three parallel validators and returns a structured consensus verdict.
- **Problem / user:** Unchecked factual claims propagate through chains of AI agents, so errors compound without any machine-readable verification step. / developers of multi-agent AI systems
- **Domain / idea type:** ai_agents_infra + dev_tools / dev_tool
- **Platforms / hardware / AI:** bot_or_chat; web / False / agent_or_tool_use; llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend ; backend FastAPI; uAgents; db Redis; hosting 
- **Tech/APIs:** Fetch.ai Agentverse / uAgents (ai_model, core, sponsor); ASI:One (ai_model, core, sponsor); Anthropic Claude (ai_model, core); Browserbase (other, supporting); Devin (other, token); Redis (database, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; Fetch.ai ASI:One; uAgents | fit: Published the validator as an Agentverse agent callable from ASI:One chat, providing consensus verdicts to other agents.
- **Repo:** public, commits 18 (before/in/after event: 0/17/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Registered as an Agentverse uAgent reachable through ASI:One chat; validators run in parallel including a source validator; uses Browserbase and Claude.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; project_name_short
- **Links:** [Devpost](https://devpost.com/software/quoram) | [GitHub](https://github.com/mohiitt/Quorum)

### SafeStreets  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of Claude [unknown]  (tier: sponsor_winner)
- **Pitch:** Drop a pin on a dangerous intersection and get a hazard analysis, fix, grant match, council letter and before/after render in one click.
- **Problem / user:** Evidence of unsafe intersections is scattered across many government sites, and turning it into an actionable case takes hours. / residents and city advocates
- **Domain / idea type:** civic_legal + mobility_transport / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs TypeScript; Python; frontend React; Mapbox; backend FastAPI; db Redis; hosting 
- **Tech/APIs:** Claude (Haiku) vision (ai_model, core, sponsor); Claude Code (other, supporting, sponsor); Browserbase (other, core); Redis (database, supporting); Mapbox (maps_geo, core); Imagen 4 (ai_model, supporting); Fetch.ai uAgents (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Claude | fit: Used Claude Haiku for a two-stage vision pipeline analyzing street imagery and cross-checking with community data, and Claude Code to build most of it.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Two-stage Claude vision: blind image pass, then separate corroboration against crash and 311 data; hazards assigned to named corner zones instead of pixel coordinates; Redis caching.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/safestreets-h6yprx)

### Sentinel  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Multi-agent security scanner for AI-built apps that reproduces exploits in sandboxes, explains findings plainly, and opens pull requests with fixes.
- **Problem / user:** Founders shipping AI-generated apps do not know if they are secure, and traditional scanners give jargon and false positives. / indie hackers, founders and student developers
- **Domain / idea type:** safety_security + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; JavaScript; Shell; HTML; CSS; frontend Next.js; backend Cloudflare Workers; Durable Objects; Prisma; db PostgreSQL; Upstash Redis; hosting Cloudflare; Vercel
- **Tech/APIs:** Browserbase (cloud, core, sponsor); Anthropic models (ai_model, core); OpenAI models (ai_model, supporting); Fetch.ai (other, unclear, sponsor); Redis (database, supporting, sponsor); Sentry (other, token, sponsor); Arize AI (other, token, sponsor); Cloudflare Workers (cloud, supporting)
- **Sponsor APIs:** Browserbase; Fetch.ai; Redis; Sentry; Arize
- **Repo:** public, commits 12 (before/in/after event: 0/12/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Only escalates findings that are reproduced in an isolated Browserbase sandbox; specialized agents (secrets, auth, injection, rate limit, supply chain) plus coordinator and validator; auto-PR patches.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/sentinel-poyh3v) | [GitHub](https://github.com/sudarshan-krishnan/Sentinel_AIHackathon_Berkley_2026)

### SnapCycle  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Photo-based app that identifies a bulky item, ranks local disposal options, and has an agent schedule donation, pickup or hauler quotes.
- **Problem / user:** Students moving out cannot easily find cheap, legitimate ways to dispose of bulky items. / college students moving out
- **Domain / idea type:** sustainability_climate + retail_consumer / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; rag_or_search; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend Node.js; db Redis; vector store; hosting 
- **Tech/APIs:** Gemini 2.5 Flash (ai_model, core, sponsor); Browserbase (cloud, core, sponsor); Simular (other, core, sponsor); Twilio (telecom, core, sponsor); Redis (database, supporting, sponsor); Arize (other, supporting, sponsor); Sentry (other, token, sponsor); Playwright (framework, supporting)
- **Sponsor APIs:** Browserbase; Simular; Twilio; Redis; Arize; Sentry
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims True (Own survey of 87 people: 89% unaware of disposal services, 58% would use one if aware.)
- **Notes:** Browserbase crawls local ordinances into a RAG store; Simular action agent fills forms and Twilio messages three haulers whose quotes stream in sorted; team cites its own 87-person survey.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/rrr-s98zwc) | [GitHub](https://github.com/prithsk/RRR)

### StudForge  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Finalist [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Turns a text or voice prompt into a validated, brick-based multi-robot simulation scene, exported to USD and other formats, with observer agents feeding memory back.
- **Problem / user:** Multi-robot sim scenes are hand-built or hallucinated by generative models with no guarantee they are collision-free or connected. / robotics researchers and simulation designers
- **Domain / idea type:** ai_agents_infra + creative_media / dev_tool
- **Platforms / hardware / AI:** web; cli / False / llm_chat; agent_or_tool_use; speech_or_voice; generative_media; other
- **Stack:** langs Python; frontend ; backend FastAPI; Pydantic; Typer; db Redis Cloud; hosting AWS EC2
- **Tech/APIs:** Claude (ai_model, core); Midjourney MCP (ai_model, supporting, sponsor); Deepgram Nova-3 (ai_model, supporting, sponsor); Redis Cloud (database, core, sponsor); Qwen2.5-1.5B (ai_model, supporting); PyTorch (framework, supporting); AWS EC2 / Trainium (cloud, supporting, sponsor)
- **Sponsor APIs:** Midjourney; Deepgram; Redis; AWS
- **Repo:** public, commits 62 (before/in/after event: 0/62/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Generative models (Claude, Midjourney, Deepgram) are strictly advisory behind a validator; fine-tuned Qwen2.5-1.5B with LoRA after a Trainium instance shut down mid-event; Redis-backed agent memory.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/studforge) | [GitHub](https://github.com/kokonut121/studsim)

### Theracat  (UC Berkeley AI Hackathon 2026)

- **Prizes:** GRAND PRIZE - Ddoski's Lab Track [unknown]; Finalist [unknown]; SkyDeck Grand Prize Winner [unknown]  (tier: track_winner)
- **Pitch:** Wristband with accelerometer detects rising agitation and delivers paced haptic breathing, paired with a plush cat that moves its ears and speaks grounding prompts.
- **Problem / user:** During panic attacks people cannot operate phones or apps, so help needs to arrive without any action from them. / people with anxiety and panic attacks, including children
- **Domain / idea type:** mental_health + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / predictive_ml; llm_chat; speech_or_voice
- **Stack:** langs Python; C++/Arduino; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); MPU6050 IMU (hardware_part, core); Haptic and ear motors (hardware_part, core); Bluetooth Low Energy (other, core); Claude (ai_model, core); ElevenLabs (ai_model, core); Random Forest classifier (ai_model, core)
- **Sponsor APIs:** ElevenLabs
- **Repo:** public, commits 26 (before/in/after event: 0/19/7), README detailed
- **Demo/writeup:** video None, live none, screenshots 14, writeup long, impact claims True (Cites prevalence stats (about 40M adults with anxiety, 1 in 11 with a panic attack yearly) and published model accuracies.)
- **Notes:** Built by a former clinician; ESP32 plus MPU6050 over BLE; classifier prototype uses synthetic accelerometer data and Random Forest; ElevenLabs voice with Claude and routing to 988; ear-moving plush.
- **Team size:** 4 | **Confidence:** medium | unverified: stack_languages; sponsor_apis_used; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/theracat) | [GitHub](https://github.com/emilyLi2020/Theracat)

### Vanguard Telematics  (UC Berkeley AI Hackathon 2026)

- **Prizes:** Best Use of The Agentverse by Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Streams a vehicle's accelerometer, vibration, temperature, pressure, proximity and camera data into a live 3D dashboard, with Fetch.ai agents analyzing telemetry.
- **Problem / user:** Vehicle health and proximity hazards are hard to monitor in real time from raw sensor streams. / fleet operators and vehicle engineers
- **Domain / idea type:** mobility_transport + safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / agent_or_tool_use; speech_or_voice; vision; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; Recharts; Three.js; Framer Motion; backend FastAPI; uAgents; db Redis; hosting 
- **Tech/APIs:** Fetch.ai Agentverse / uAgents (ai_model, core, sponsor); STM32 Nucleo-F401RE + IKS5A1 (hardware_part, core); Raspberry Pi 5 (hardware_part, core); QNX (other, supporting); Deepgram (ai_model, supporting); OpenAI (ai_model, supporting); Redis (database, core); Three.js (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; uAgents | fit: Ran Agentverse agents over the vehicle telemetry stream feeding the dashboard.
- **Repo:** public, commits 79 (before/in/after event: 0/78/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Industrial sensor rig on an STM32 Nucleo with ST sensor board, Raspberry Pi 5 running QNX, Redis streams feeding a React/Three.js dashboard and Agentverse agents.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; edition_blob_queue_split; problem_statement
- **Links:** [Devpost](https://devpost.com/software/vanguard-telematics) | [GitHub](https://github.com/bencejdanko/VanguardTelematics)
