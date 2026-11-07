# HackIllinois: project cards (14 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackIllinois 2025

### Recycle Tracker  (HackIllinois 2025)

- **Prizes:** 2nd Place Overall [2nd]  (tier: overall_top3)
- **Pitch:** Rewards app where users upload recycling photos, with device fingerprinting, EXIF/GPS and hash checks against fraud, redeemable at local stores and with NGO location analytics.
- **Problem / user:** People lack incentive to recycle, and fraud in reward programs undermines trust and impact. / recyclers, NGOs and local businesses
- **Domain / idea type:** sustainability_climate + social_community / social_good
- **Platforms / hardware / AI:** mobile_android / False / vision
- **Stack:** langs Kotlin; TypeScript; Python; frontend Jetpack Compose; backend Cloudflare Workers; Hono.js; Django; db NeonDB PostgreSQL; Drizzle ORM; hosting Cloudflare Workers; Leapcell; Google Cloud Storage
- **Tech/APIs:** FingerprintJS Pro (auth, core); Cloudflare Workers (cloud, core); NeonDB (database, core); Google Cloud Storage (cloud, supporting); Twilio SendGrid (telecom, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 116 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** edition_mismatch: page was submitted to many hackathons (incl. HackIllinois 2025); the 2nd Place Overall badge appears under GreenPioneers, not clearly HackIllinois. Multiple repos; Kotlin app, Cloudflare Workers API.
- **Team size:** 3 | **Confidence:** medium | unverified: event_start; event_end; ui_polish; edition_mismatch; prizes
- **Links:** [Devpost](https://devpost.com/software/recycle-tracker) | [GitHub](https://github.com/jacksonkasi0/Reward-Based-Recycling-Tracker)


## HackIllinois 2026

### Cat Vision Copilot  (HackIllinois 2026)

- **Prizes:** Track: Best AI Inspection (2nd Place) [2nd]  (tier: track_winner)
- **Pitch:** Web inspection assistant mirroring the Cat Inspect interface that analyzes video, images and voice, ranks issue severity, identifies parts and answers questions with a data chatbot.
- **Problem / user:** Field equipment inspections are manual, slow and inconsistent. / heavy equipment inspectors
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs TypeScript; Python; frontend React; backend Node.js; db Supabase; hosting 
- **Tech/APIs:** YOLO (ai_model, unclear); OpenAI (ai_model, unclear); Ollama (ai_model, unclear); Hugging Face Transformers (ai_model, unclear); ElevenLabs (ai_model, unclear); OpenCV (framework, supporting); Supabase (database, supporting)
- **Sponsor APIs:**  | fit: Responds to the Caterpillar challenge of combining Cat Inspect and Cat AI Assistant; no sponsor API use stated.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Deliberately styled after Caterpillar's Cat Inspect UI; writeup names no specific model use beyond the Built With list (YOLO, OpenAI, Ollama, Hugging Face, ElevenLabs).
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish; tech_items depth
- **Links:** [Devpost](https://devpost.com/software/cat-vision)

### Cat-AR-pillar  (HackIllinois 2026)

- **Prizes:** Track: Best AI Inspection (3rd Place) [3rd]  (tier: track_winner)
- **Pitch:** Quest 3 mixed-reality inspection aid that detects excavator parts on-device with YOLO and logs voice or video notes under the part the inspector is looking at.
- **Problem / user:** Inspectors juggle checklists, tablets and the machine, and manual tagging of findings is slow and error-prone. / heavy equipment inspectors
- **Domain / idea type:** productivity_workplace + safety_security / hardware_gadget
- **Platforms / hardware / AI:** other / True / vision; speech_or_voice
- **Stack:** langs C#; Python; frontend Unity; backend ; db ; hosting 
- **Tech/APIs:** YOLOv12 Nano (ai_model, core); Unity (framework, core); Meta Quest 3 (hardware_part, core); Roboflow (other, supporting); Label Studio (HumanSignal) (other, supporting)
- **Sponsor APIs:**  | fit: Builds a hands-free AR inspection concept for Caterpillar-style machinery; no sponsor API stated.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** YOLOv12 Nano trained on about 60 hand-labelled excavator images, run locally on the headset; left-hand-gaze menu; Unity (C#) prototype on Meta Quest 3.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/cat-ar-pillar)

### ease 'n spect  (HackIllinois 2026)

- **Prizes:** Track: Best AI Inspection (1st Place) [1st]  (tier: track_winner)
- **Pitch:** Mobile app guiding excavator inspections through five 3D-cued photo steps with voice notes, then AI wear assessment and replacement-part suggestions.
- **Problem / user:** Field heavy-equipment inspections use inconsistent checklists and poor records. / heavy equipment inspectors
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** mobile_cross / False / vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; frontend React Native; Expo; React Three Fiber; backend FastAPI; db Supabase PostgreSQL; hosting Modal
- **Tech/APIs:** Gemini 2.5 Flash (ai_model, core); Whisper (ai_model, supporting); Qwen 3 (ai_model, supporting); Modal (cloud, core, sponsor); Supabase (database, core)
- **Sponsor APIs:** Modal | fit: Hosts the multimodal AI pipeline (Gemini, Whisper, Qwen) on Modal for the AI inspection track.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup medium, impact claims False
- **Notes:** React Three Fiber excavator model sets the camera cue per inspection step; Gemini vision, Whisper and Qwen 3 hosted on Modal; Pydantic schema-first parsing.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/inspectus)

### EcoApi(Recost)  (HackIllinois 2026)

- **Prizes:** Track: Best Web API (1st Place) [1st]  (tier: track_winner)
- **Pitch:** Developer tool (cloud API, dashboard, VS Code extension) that scans code for API calls and reports cost, N+1 and caching issues plus estimated energy, water and CO2.
- **Problem / user:** Developers cannot see the hidden financial and environmental cost of API calls, especially in vibe-coded apps. / software developers
- **Domain / idea type:** dev_tools + sustainability_climate / dev_tool
- **Platforms / hardware / AI:** web; other / False / llm_chat
- **Stack:** langs TypeScript; frontend React; Vite; D3.js; Recharts; Tailwind CSS; backend Cloudflare Workers; Hono; db Cloudflare D1; SQLite; hosting Cloudflare Pages
- **Tech/APIs:** Cloudflare Workers (cloud, core); Cloudflare D1/KV (database, core); Cloudflare Workers AI (Llama 3.1 8B) (ai_model, supporting); OpenAI API (ai_model, supporting); VS Code Extension API (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 86 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Three parts: Cloudflare Workers API with D1/KV, React dashboard with D3 graph, and VS Code extension with local scanning; team says it used the tool to submit a PR to OpenClaw.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/ecoapi) | [GitHub](https://github.com/AndresL230/ecoapi)

### LARYNX  (HackIllinois 2026)

- **Prizes:** Track: Best AI Inference (2nd Place) [2nd]  (tier: track_winner)
- **Pitch:** Deepfake voice detector that reconstructs implied tongue and jaw movements from audio, flags impossible speeds, and shows them in a 3D skull cross-section.
- **Problem / user:** Synthetic speech implies articulator motions beyond human biomechanical limits, but detectors rarely explain why audio is fake. / people verifying audio authenticity
- **Domain / idea type:** safety_security + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React; Three.js; React Three Fiber; GSAP; Zustand; Tone.js; backend Hono; Cloudflare Workers; db Cloudflare D1; R2; Vectorize; hosting Cloudflare Pages; Modal
- **Tech/APIs:** Modal B200 GPUs (cloud, core, sponsor); HuBERT Large (ai_model, core); Praat / parselmouth (framework, core); Cloudflare Workers, D1, R2, Vectorize, Workers AI, AI Gateway (cloud, core); Three.js / R3F (framework, core)
- **Sponsor APIs:** Modal; Cloudflare | fit: Audio inference pipeline runs on Modal B200 GPUs and streams results via SSE.
- **Repo:** public, commits 154 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims True (States 89.2% cross-validated accuracy across 73 TTS architectures and a 9x human tongue speed example.)
- **Notes:** Solo; author says it was not fully finished. HuBERT plus articulatory inference on Modal B200, Praat formants, gradient boosting classifier (89.2% CV accuracy stated), seven Cloudflare products, Three.js skull.
- **Team size:** 1 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/voxlarynx) | [GitHub](https://github.com/Gladdonilli/hackillinois-2026)

### LinkCare  (HackIllinois 2026)

- **Prizes:** Best Use of Actian VectorAI DB (3rd Place) [3rd]  (tier: sponsor_winner)
- **Pitch:** Patient peer-community platform that matches users to care circles and ranks doctors from patient experiences via RAG plus a three-persona AI consensus engine, with voice in and out.
- **Problem / user:** Newly diagnosed patients feel overwhelmed and lack peers with the same experience to guide doctor choices. / patients with a new diagnosis
- **Domain / idea type:** health_wellness + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / rag_or_search; agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; Framer Motion; backend FastAPI; db Actian VectorAI DB; hosting Modal; Docker
- **Tech/APIs:** Actian VectorAI DB (database, core, sponsor); gemini-embedding-001 (ai_model, core); Gemini (ai_model, core); OpenAI Whisper on Modal (ai_model, core); ElevenLabs (ai_model, supporting); Modal (cloud, supporting)
- **Sponsor APIs:** Actian VectorAI DB | fit: Indexes 3072-dim patient-experience embeddings in Actian VectorAI (HNSW) to power the RAG doctor recommendation pipeline.
- **Repo:** public, commits 32 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Composite doctor ranking from similarity, outcome and sentiment; three Gemini personas vote in parallel; Whisper on Modal T4 and ElevenLabs for voice; FastAPI REST bridge to Actian gRPC; PreSage SDK plan dropped.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/linkcare-2fj4ya) | [GitHub](https://github.com/prabas007/patient-hub)

### Logian  (HackIllinois 2026)

- **Prizes:** Best Use of Actian VectorAI DB (2nd Place) [2nd]  (tier: sponsor_winner)
- **Pitch:** Real-time stock sentiment engine that scrapes financial news, scores headlines with FinBERT in the background and serves precomputed per-ticker signals and a live dashboard.
- **Problem / user:** LLM inference is too slow for high-frequency trading loops, so news sentiment is not used alongside fast strategies. / algorithmic and high-frequency traders
- **Domain / idea type:** fintech_finance + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web; cli / False / predictive_ml; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React; Vite; Recharts; backend FastAPI; asyncio; db Actian VectorAI DB; hosting 
- **Tech/APIs:** Actian VectorAI DB (database, core, sponsor); FinBERT (ai_model, core); all-MiniLM-L6-v2 (ai_model, core); Yahoo Finance news (data_source, core)
- **Sponsor APIs:** Actian VectorAI DB | fit: Stores article embeddings in Actian VectorAI via gRPC for batch upserts and cosine-similarity semantic search across tickers.
- **Repo:** public, commits 11 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Inference decoupled from the query path via async background workers; Yahoo Finance RSS/HTML scraper with backoff; MiniLM embeddings in Actian VectorAI over gRPC; React dashboard on WebSockets.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/team-habs) | [GitHub](https://github.com/bilalarif3197/LogianHackIllinois)

### OpenReality  (HackIllinois 2026)

- **Prizes:** Most Creative [unknown]; Track: Best AI Inference (1st Place) [1st]; [MLH] Best Use of Gemini API [unknown]  (tier: track_winner)
- **Pitch:** Cloud spatial-AI platform where a phone camera stream builds a live 3D map and an agent plans, finds targets, and answers spatial questions from geometry.
- **Problem / user:** AI agents cannot reason about where objects are in 3D, and survey hardware like LiDAR is costly for responders. / first responders, accessibility users, developers
- **Domain / idea type:** safety_security + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend Vite; Three.js; backend Flask; Socket.IO; db ; hosting Modal
- **Tech/APIs:** Modal (H100, Volumes, tunnel) (cloud, core, sponsor); VGGT-1B (ai_model, core); SAM3 (ai_model, core); CLIP (ai_model, core); Gemini (ai_model, supporting, sponsor); Claude (ai_model, supporting); GTSAM (framework, supporting)
- **Sponsor APIs:** Modal; Gemini API | fit: Runs the whole vision pipeline on a warm Modal H100 with persisted weights; Gemini API listed in Built With.
- **Repo:** public, commits 36 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** VGGT-1B SLAM with CLIP scoring and SAM3 on a warm Modal H100, Modal tunnel for phone HTTPS streaming; agent re-runs detection retroactively when targets are added.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/real-eyes-mra8n6) | [GitHub](https://github.com/bdavidzhang/Open-Reality)

### Sparsh Mukthi  (HackIllinois 2026)

- **Prizes:** First Place – Frostbyte Champion [1st]; Second Place – Frostbyte Runner-Up [2nd]; Special Mentions & Jury Commendations [unknown]; Participation & Completion Recognition [unknown]  (tier: overall_top3)
- **Pitch:** Touchless computer control through voice commands and hand gestures, aimed at hospitals, VR and accessibility, with a Firebase referral and access system.
- **Problem / user:** Touch interfaces create hygiene, immersion and accessibility problems in ICUs, labs and shared spaces. / hospital staff, VR users, accessibility users
- **Domain / idea type:** accessibility + health_wellness / new_category
- **Platforms / hardware / AI:** desktop; web / False / vision; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend Tkinter; backend Flask; Firebase; db Firebase; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); speech_recognition (ai_model, core); pyttsx3 (other, supporting); Firebase (auth, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 25 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup medium, impact claims False (Screenshots reference market analysis and business model slides; text has no numbers.)
- **Notes:** edition_mismatch: listed under HackIllinois 2026 among ~40 hackathons; the winner badges shown are from Frostbyte Hackathon, not HackIllinois. Prototype runs on macOS Python; mobile and VR are planned.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ui_polish; edition_mismatch; prizes
- **Links:** [Devpost](https://devpost.com/software/sparsh-mukthi-ay0cwf) | [GitHub](https://github.com/Ishaan-Gpt/gesture-studio)

### Superstyle  (HackIllinois 2026)

- **Prizes:** Best Use of Supermemory [unknown]; Track: Best Web API (2nd Place) [2nd]  (tier: sponsor_winner)
- **Pitch:** Virtual try-on and AI stylist consumer app plus a Stripe-like developer API and embeddable widget so any shop can offer selfie-based try-on.
- **Problem / user:** Online clothing sites show one model, so shoppers cannot tell if items suit their body or style. / online clothing shoppers and e-commerce sites
- **Domain / idea type:** retail_consumer + dev_tools / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media; vision; llm_chat; speech_or_voice; rag_or_search; recommendation
- **Stack:** langs TypeScript; frontend Next.js 16; React 19; Tailwind CSS; shadcn/ui; Three.js; backend Hono; AWS Lambda; db DynamoDB; Supermemory; hosting AWS; Vercel
- **Tech/APIs:** Supermemory (database, core, sponsor); Gemini image generation (ai_model, core); Gemini 2.5 Flash (ai_model, core); ElevenLabs agent (ai_model, core); OpenAI API (ai_model, supporting); Meshy (ai_model, supporting); AWS Lambda / S3 / DynamoDB (cloud, core); Serper (data_source, supporting); Clerk (auth, supporting)
- **Sponsor APIs:** Supermemory | fit: Uses Supermemory user profiles and graph memory to store style preferences that feed RAG and carry across third-party sites.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims False (Describes planned subscription and affiliate monetization, no numbers.)
- **Notes:** Serverless AWS Lambda API with API-key auth, idempotency, rate limits and usage analytics; single script-tag widget; Supermemory graph memory for style profile; Meshy 3D avatars; Gemini try-on images.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/superstyle) | [GitHub](https://github.com/danielxies/superstyle)

### TerraGlide  (HackIllinois 2026)

- **Prizes:** Track: Best Hardware Hack (John Deere Mechathon) (1st Place) [1st]; Track: Best Hardware Hack (John Deere Mechathon) (Easy Track Winner) [unknown]  (tier: track_winner)
- **Pitch:** Sand-leveling rover built on a SunFounder kit with custom dozer and grader, teleoperated from a web UI, with YOLO pedestrian alerts and ultrasonic auto blade lift.
- **Problem / user:** A small earthmover needs reflexes to keep bystanders safe and avoid digging itself in. / machine operators (John Deere Mechathon scenario)
- **Domain / idea type:** safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision
- **Stack:** langs Python; frontend React; backend ; db ; hosting 
- **Tech/APIs:** SunFounder Galaxy-RVR (hardware_part, core); ESP32 (hardware_part, core); Arduino (hardware_part, core); Ultrasonic sensors (hardware_part, core); YOLO (ai_model, core); PyTorch (framework, supporting)
- **Sponsor APIs:**  | fit: Hardware rover themed on John Deere Mechathon machinery safety and terrain handling.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Custom attachments designed from caliper measurements and laser-cut or 3D printed; reverse-engineered the kit's proprietary protocol to drive it from a custom UI; ESP32 plus Arduino.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/terraglide-ai)

### Vigilante AI  (HackIllinois 2026)

- **Prizes:** Best Use of Actian VectorAI DB (1st Place) [1st]  (tier: sponsor_winner)
- **Pitch:** Turns uploaded CCTV video into searchable intelligence: detects people, scores threat level, writes incident reports and supports natural-language clip search.
- **Problem / user:** Security teams must manually scrub hours of footage to find incidents. / security teams
- **Domain / idea type:** safety_security + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; rag_or_search; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; backend FastAPI; db Actian VectorAI; SQLite; hosting Modal
- **Tech/APIs:** Actian VectorAI DB (database, core, sponsor); Modal (cloud, core); YOLO11-L (ai_model, core); CLIP ViT-L/14 (ai_model, core); Qwen2.5-VL-7B (ai_model, core); Gemini 2.5 Flash (ai_model, supporting); Supermemory (ai_model, supporting, sponsor)
- **Sponsor APIs:** Actian VectorAI DB; Supermemory | fit: Stores 768-dim CLIP clip embeddings in Actian VectorAI and runs cosine similarity search merged with keyword results.
- **Repo:** public, commits 3 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Runs YOLO11, CLIP and Qwen2.5-VL together on one Modal A100; hybrid Actian VectorAI plus SQLite search; Gemini synthesis and Supermemory for cross-video queries.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/vigilante-ai) | [GitHub](https://github.com/GALGALLOR/vigilant-ai)

### Vizem Flow (the Voicepill mogger)  (HackIllinois 2026)

- **Prizes:** Track: Best AI Inference (3rd Place) [3rd]  (tier: track_winner)
- **Pitch:** Background lip-reading dictation: press a key, record the mouth, decode visemes to phonemes to words, and an LLM turns them into a sentence typed anywhere.
- **Problem / user:** Voice typing is awkward or impossible in noisy or quiet public places, and speech-impaired users lack fast input. / people in loud or quiet settings, speech-impaired users
- **Domain / idea type:** accessibility + productivity_workplace / new_category
- **Platforms / hardware / AI:** desktop / False / vision; llm_chat
- **Stack:** langs Python; frontend ; backend FastAPI; db Supermemory; hosting Modal
- **Tech/APIs:** Modal (cloud, core, sponsor); MediaPipe (ai_model, core); OpenCV (framework, supporting); OpenAI (ai_model, core); Supermemory (database, supporting, sponsor)
- **Sponsor APIs:** Modal; Supermemory | fit: Whole decoding pipeline runs in a Modal container behind one FastAPI endpoint.
- **Repo:** public, commits 6 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims False
- **Notes:** Trained own viseme reference set from team photos; MediaPipe lip geometry pipeline served by a Modal FastAPI endpoint; OpenAI plus Supermemory to form sentences and adapt to user style.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/vizem-flow) | [GitHub](https://github.com/Akshath-Nagulapally/lipvisemes)
