# Cal Hacks: project cards (36 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Cal Hacks 11.0 (2024)

### Blockify  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks / Berkeley RDI: Berkeley RDI Web3 Prize [unknown]; Winner Sui: Reimagine the internet with Sui [unknown]  (tier: sponsor_winner)
- **Pitch:** Blockchain royalty platform where artists attach Sui smart contracts to uploaded music so payouts trigger automatically from Spotify stream counts.
- **Problem / user:** Artists lose ownership and most revenue to labels and distributors, and royalty payments are slow and opaque. / independent music artists
- **Domain / idea type:** creative_media + fintech_finance / new_category
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Move; JavaScript; frontend React; backend Node.js; db ; hosting 
- **Tech/APIs:** Sui blockchain (other, core, sponsor); Move (framework, core, sponsor); Sui SDK / wallets (other, core, sponsor); Spotify API (data_source, core); React (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:** Sui | fit: Targeted the Sui challenge by writing Move smart contracts on Sui and integrating Sui wallets/SDK to pay royalties.
- **Repo:** public, commits 5 (before/in/after event: 5/0/0), README none
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Smart contracts written in Move on Sui; Spotify API stream data meant to trigger wallet payments; first blockchain project for both teammates.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/blockify-x2owt7) | [GitHub](https://github.com/ChiragSeth14/CalHacks)

### Duet: Brainwaves -> Live Music  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: 1st Overall [1st]  (tier: overall_top3)
- **Pitch:** EEG headset reads focus and relaxation and a Gemini-driven live composer turns them into adaptive Sonic Pi music, aimed at kids with developmental disabilities.
- **Problem / user:** Children with developmental disabilities, especially non-verbal ones, lack tools to express emotion and creativity through music. / children with developmental disabilities, music therapists
- **Domain / idea type:** accessibility + creative_media / creative_tool
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; generative_media
- **Stack:** langs Python; Ruby; JavaScript; frontend Next.js; three.js; backend Python; Emotiv Cortex library; Sonic Pi; db SingleStore; hosting 
- **Tech/APIs:** Emotiv EEG headset (hardware_part, core); Google Gemini (ai_model, core); Sonic Pi (framework, core); SingleStore (database, supporting, sponsor); Next.js (framework, supporting); three.js (framework, supporting)
- **Sponsor APIs:** SingleStore
- **Repo:** public, commits 12 (before/in/after event: 12/0/0), README solid
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims True (Cites 1 in 10 US children with developmental disabilities and a 15.59% projected music therapy market growth rate.)
- **Notes:** LLM acts as a live composer each few seconds using recent EEG state, available instruments and its prior output; Sonic Pi plays it; Three.js 3D brain visualiser.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; n_screenshots; SingleStore is_sponsor; ui_polish; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/duet-0tbkxe) | [GitHub](https://github.com/daniel04wawng/duet-frontend ; https://github.com/soapantelope/duet-backend)

### GhostWriter  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: 2nd Overall [2nd]  (tier: overall_top3)
- **Pitch:** Listens to live office-hour conversation and automatically inserts the useful points into the right lines of course notes using transcription, retrieval and LLM edits.
- **Problem / user:** Short-staffed teaching assistants struggle to keep course notes and documentation updated while helping students. / teaching assistants and instructors
- **Domain / idea type:** education + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; speech_or_voice
- **Stack:** langs Python; frontend Reflex; React; backend Reflex; Python; db ChromaDB; hosting 
- **Tech/APIs:** Deepgram live transcription (ai_model, core); Google Gemini (summaries, embeddings) (ai_model, core); ChromaDB (database, core); Groq (llama3-70b) (ai_model, core); Reflex (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 24 (before/in/after event: 24/0/0), README solid
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Inserts generated markdown at line-level points using unique tokens in the source text; embedding distance thresholds decide whether to skip, append or create a note.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; ui_polish; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/ghostwriter-491kuy) | [GitHub](https://github.com/rqchao/calhacks24)

### MafiAI  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: Hack on AI [unknown]  (tier: track_winner)
- **Pitch:** Party game of Mafia in which LLM-driven characters discuss and vote to work out who the mafia are.
- **Problem / user:** Not stated on the page; the project applies LLM agents to a social deduction game. / casual game players
- **Domain / idea type:** entertainment_games + ai_agents_infra / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React; backend Python; WebSockets; db ; hosting 
- **Tech/APIs:** Groq (ai_model, unclear); Gemini (ai_model, unclear); Cartesia (ai_model, unclear); React (framework, supporting); WebSockets (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 15 (before/in/after event: 15/0/0), README thin
- **Demo/writeup:** video True, live none, screenshots 2, writeup short, impact claims False
- **Notes:** Page is a one-line blurb with no sections; stack named as Python, React, TypeScript, websockets plus Cartesia, Groq and Gemini.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; problem_statement
- **Links:** [Devpost](https://devpost.com/software/mafiai) | [GitHub](https://github.com/KevinL10/mafia)

### Resililink  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: Hack for Impact [unknown]; Winner Skylo: Seamlessly Switch from Cellular to Satellite [unknown]  (tier: sponsor_winner)
- **Pitch:** LoRa mesh network of cheap ESP32 nodes whose satellite-equipped super node relays messages via Skylo to a server that texts recipients through Twilio and returns an acknowledgment.
- **Problem / user:** During hurricanes and other disasters, cell and internet service fails and people cannot contact family or responders. / people in disaster-prone regions and emergency contacts
- **Domain / idea type:** telecom_networking + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs Python; JavaScript; frontend React; Vite; backend Python; MQTT; Protocol Buffers; db ; hosting Microsoft Azure
- **Tech/APIs:** Skylo satellite connectivity (telecom, core, sponsor); LoRa radio / ESP32 (hardware_part, core); Twilio SMS (telecom, core); Microsoft Azure (cloud, supporting); MQTT (framework, supporting); Protocol Buffers (framework, supporting); Raspberry Pi (hardware_part, supporting); React/Vite (framework, supporting)
- **Sponsor APIs:** Skylo | fit: Targeted the Skylo challenge by using a Skylo satellite modem on a super node to bridge LoRa mesh traffic to the internet over MQTT.
- **Repo:** public, commits 5 (before/in/after event: 5/0/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Custom protobuf protocol within a 256-byte packet limit; Skylo satellite modem evaluation board with poorly documented AT commands; MQTT to an Azure-hosted server; nodes are one LoRa radio plus ESP32.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; live_demo_url
- **Links:** [Devpost](https://devpost.com/software/resilink) | [GitHub](https://github.com/12458/calhacks)

### SnackSnap - recycle to feed your pet  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: 3rd Overall [3rd]  (tier: overall_top3)
- **Pitch:** iOS app where you photograph yourself recycling, Gemini validates the photo, and you feed a digital pet and earn XP rewards.
- **Problem / user:** Recycling feels inconvenient so people throw recyclables in the trash; a pet game makes it rewarding. / everyday consumers, recycling-minded phone users
- **Domain / idea type:** sustainability_climate + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / vision
- **Stack:** langs Swift; frontend SwiftUI; backend Firebase; db Firebase; hosting Firebase Storage
- **Tech/APIs:** Google Gemini 1.5 Pro (ai_model, core); Firebase (cloud, supporting); Firebase Storage (cloud, supporting); SwiftUI (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Gemini image recognition gates the pet-feeding mechanic; XP redeemable for rewards such as early product access.
- **Team size:** 2 | **Confidence:** medium | unverified: has_demo_video; ui_polish; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/snacksnap-lw4b9q)

### Talk Tuah  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: Best Beginner Hack [unknown]; Winner Deepgram: Deepgram Voice Agent Quest [unknown]  (tier: track_winner)
- **Pitch:** AR glasses that listen to and watch a conversation partner, read their mood, and show a suggested reply on a small OLED display.
- **Problem / user:** Introverted or socially awkward people struggle to find good responses in live conversation. / introverts and socially anxious people
- **Domain / idea type:** accessibility + mental_health / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross / True / llm_chat; speech_or_voice; vision
- **Stack:** langs Python; C; JavaScript; frontend React Native; backend Flask; ngrok; db ; hosting 
- **Tech/APIs:** OpenAI API (ai_model, core); Deepgram (ai_model, core, sponsor); Hume (ai_model, supporting); Arduino (hardware_part, supporting); Raspberry Pi (hardware_part, supporting); React Native (framework, core); Flask (framework, supporting)
- **Sponsor APIs:** Deepgram | fit: Targeted the Deepgram Voice Agent Quest by using the Deepgram API to transcribe the other speaker's speech and help infer their mood for reply suggestions.
- **Repo:** public, commits 23 (before/in/after event: 23/0/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Wearable prototype combining camera, microphone, OLED display and a React Native companion app; mood detection uses Deepgram speech plus Hume emotion analysis; Figma design linked.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; placement_tier
- **Links:** [Devpost](https://devpost.com/software/talk-tuah) | [GitHub](https://github.com/steven-mu12/talk-tuah/tree/main)

### TeachXR  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: Hackers' Choice [unknown]; Winner Vapi: Show us your Voice AI [unknown]  (tier: track_winner)
- **Pitch:** XR study assistant where learners point or gesture at material, crop it, and ask questions by voice to get spoken answers and interactive help.
- **Problem / user:** A global shortage of teachers leaves students without individual guidance. / students
- **Domain / idea type:** education + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web; other / True / llm_chat; speech_or_voice; vision
- **Stack:** langs JavaScript; frontend React; Tailwind; backend MediaPipe; OCR microservices; db SingleStore; hosting 
- **Tech/APIs:** Vapi (ai_model, core, sponsor); Deepgram (ai_model, supporting, sponsor); Cartesia (ai_model, supporting, sponsor); Gemini (ai_model, core); MediaPipe (framework, core); SingleStore (database, supporting, sponsor); React (framework, core)
- **Sponsor APIs:** Vapi; Deepgram; Cartesia; SingleStore | fit: Targeted the Vapi Voice AI challenge by using Vapi for the spoken, hands-free question-and-answer layer of the XR study assistant.
- **Repo:** public, commits 33 (before/in/after event: 32/0/1), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup long, impact claims True (Cites a 23:1 global primary student-to-teacher ratio as motivation.)
- **Notes:** Microservice architecture with three repos (frontend, dataflow backend, gesture backend); MediaPipe hand-gesture detection drives image cropping, then OCR and Gemini; voice via Vapi, Deepgram and Cartesia.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/teachxr) | [GitHub](https://github.com/VietRocHack/TeachXR-frontend/)

### Unreal EngJam  (Cal Hacks 11.0 (2024))

- **Prizes:** Winner Cal Hacks: Most Entertaining Hack [unknown]; Winner Warp: Best Developer Tool by Warp [unknown]  (tier: track_winner)
- **Pitch:** A visual programming language that lives inside Figma, where designers whiteboard code, color-code it, and get a Clippy-style assistant that flags mistakes.
- **Problem / user:** Text-only coding limits visual expression; the team wanted Scratch-like visual programming with a real language's power. / programmers and designers who like visual coding
- **Domain / idea type:** dev_tools + entertainment_games / creative_tool
- **Platforms / hardware / AI:** other / False / False
- **Stack:** langs TypeScript; frontend Figma plugin API; backend ; db ; hosting 
- **Tech/APIs:** Figma plugin API (framework, core); TypeScript (framework, core)
- **Sponsor APIs:**  | fit: Targeted Warp's Best Developer Tool prize as a new programming language and editor environment; the page does not show use of Warp's own product.
- **Repo:** public, commits 5 (before/in/after event: 5/0/0), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Programming language written from scratch with no dependencies in TypeScript; a Figma plugin traverses the document to build an AST; includes a Clippy-style error helper; humorous framing.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/unreal-engjam) | [GitHub](https://github.com/kognise/aldente)


## Cal Hacks 12.0 (2025)

### ADLOVIN  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner AppLovin: Ad Intelligence Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Pipeline that extracts visual, text and audio features from ad images and videos into embeddings for ad performance insights and ranking models.
- **Problem / user:** Ad recommendation systems need rich multimodal understanding of ad creatives to predict performance. / ad platforms and marketing analysts
- **Domain / idea type:** ai_agents_infra + retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; rag_or_search; predictive_ml; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Tailwind; backend Python; FFmpeg; Librosa; db ChromaDB; hosting 
- **Tech/APIs:** Claude (ai_model, supporting); CLIP / vision transformer (ai_model, core); EasyOCR (ai_model, supporting); ChromaDB (database, core); Hugging Face (ai_model, supporting); scikit-learn (framework, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted AppLovin's Ad Intelligence Challenge by building a multimodal embedding pipeline over ad creatives, inspired by AppLovin's Axon recommender; no AppLovin API use shown.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Python feature-extraction pipeline using FFmpeg keyframes, Librosa audio analysis, CLIP-style vision embeddings, EasyOCR and ChromaDB; React/TypeScript front end; two repos linked on page (second repo https://github.com/abtonmoy/calhacks12).
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes; placement_tier
- **Links:** [Devpost](https://devpost.com/software/adlovin-media-intelligence) | [GitHub](https://github.com/SisuKah/calhacks2)

### Bob  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Cal Hacks: Most Creative Hack [unknown]  (tier: track_winner)
- **Pitch:** Agentic AR glasses on Snap Spectacles that watch the wearer's task, answer by voice and highlight objects to guide repairs and builds.
- **Problem / user:** There is a shortage of skilled tradespeople; guidance that watches a physical task in real time could help novices do simple technical work. / homeowners, trade trainees and technicians
- **Domain / idea type:** education + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; other / True / llm_chat; agent_or_tool_use; vision; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Lens Studio; backend Python; WebSockets; db ; hosting 
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core); Gemini Live (ai_model, core); YOLOE-11 (ai_model, core); Google Generative AI SDK (Search, Maps) (ai_model, supporting); Slack SDK (other, supporting); Gmail via SMTP (other, supporting); WebSockets (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 93 (before/in/after event: 0/93/0), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims True (Cites US shortfall of 70,000 electricians and 642,000 mechanics and age share of tradespeople.)
- **Notes:** Spectacles stream video/audio to a Python WebSocket server that proxies Gemini Live; YOLOE-11 text-prompted detection draws bounding-box overlays; tools include Gmail, Slack, Search and Maps.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; team_size; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/bob-vj43mq) | [GitHub](https://github.com/raghavrajsah/tethyr/)

### Duck Duck Goose  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner AppLovin: Query Planner Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** A fast query engine on DuckDB that uses on-disk layout, materialized views, query rewriting and caching to answer analytics queries in milliseconds.
- **Problem / user:** Baseline analytics queries on the challenge dataset took tens of seconds and needed a much faster planner. / data engineers and analytics teams
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** cli / False / False
- **Stack:** langs Python; frontend ; backend DuckDB; db DuckDB; hosting 
- **Tech/APIs:** DuckDB (database, core); Python (framework, core)
- **Sponsor APIs:**  | fit: Submitted to AppLovin's Query Planner Challenge, optimizing query execution speed on the challenge workload with materialized views and query rewriting.
- **Repo:** public, commits 26 (before/in/after event: 0/26/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup short, impact claims True (Reports roughly 1300x speedup versus baseline (about 45 s to 30 ms) and 5 minutes of preprocessing.)
- **Notes:** Solo Python entry to a query-planner optimization challenge; claims about 1300x speedup (about 45 s to 30 ms) on an M3 Pro; writeup is only a short note pointing to the GitHub README.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; prizes; platforms
- **Links:** [Devpost](https://devpost.com/software/duck-duck-goose-jelxr9) | [GitHub](https://github.com/KevinL10/applovin-query)

### Elda AI  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Claude: Best Use of Claude [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-first eldercare platform that tracks medication, mood and behavior patterns and sends doctors and caregivers summaries flagging possible cognitive decline.
- **Problem / user:** Dementia erodes elders' routines such as taking medicine, and caregivers lack continuous insight into changes. / elderly people with dementia, caregivers and doctors
- **Domain / idea type:** health_wellness + ai_agents_infra / social_good
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat; speech_or_voice; rag_or_search; predictive_ml
- **Stack:** langs Python; TypeScript; JavaScript; Java; frontend React Native; Expo; Next.js; Tailwind; backend FastAPI; APScheduler; JWT; db PostgreSQL; Chroma; hosting Firebase
- **Tech/APIs:** Claude (ai_model, core, sponsor); Letta (ai_model, core); Chroma (database, core); Twilio (telecom, supporting); Firebase (cloud, supporting); FastAPI (framework, core); React Native / Expo (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:** Claude | fit: Targeted Best Use of Claude by using Claude for speech intent and emotion/sentiment analysis that feeds daily and monthly caregiver health summaries.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 28, writeup medium, impact claims False
- **Notes:** Claude handles intent and sentiment, Letta holds behavioral memory, Chroma detects pattern changes; Twilio voice calls; React Native/Expo elder app plus Next.js caregiver dashboard; 28 gallery images.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; prizes; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/elda-ai) | [GitHub](https://github.com/Gaurav890/Elda.git)

### Expungo  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Promise: Public Impact Prize (sponsored by Promise) [unknown]; Winner Cal Hacks: Greatest Social Impact [unknown]  (tier: sponsor_winner)
- **Pitch:** Web platform that reads uploaded court or RAP sheets, judges criminal record expungement eligibility against state law, talks users through it by voice and fills forms.
- **Problem / user:** Expungement information is hard to find and the official process is long and confusing for people with old convictions. / people seeking record expungement
- **Domain / idea type:** civic_legal + ai_agents_infra / social_good
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind CSS; backend FastAPI; LangChain; Pydantic; db ChromaDB; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, core); OpenAI GPT-4 (ai_model, core); LiveKit Agents (framework, core); ChromaDB (database, core); LangChain (framework, supporting); FastAPI (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Entered for the Promise public impact prize by building an expungement-eligibility and form-filling assistant; the page does not show use of a Promise product.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** RAG over expungement statutes for all 50 states in ChromaDB, Gemini PDF parsing of scanned RAP sheets, LiveKit voice agent; all data kept in memory with no database.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; is_sponsor
- **Links:** [Devpost](https://devpost.com/software/clearpathai)

### FaceTimeOS: AI Mac Agent  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Cal Hacks: 1st Overall [1st]  (tier: overall_top3)
- **Pitch:** Call or iMessage your Mac and a Claude-orchestrated agent answers, runs computer-use tasks, speaks progress back and texts a confirming screenshot.
- **Problem / user:** Remote desktop tools are clunky and visual; people away from their Mac need quick conversational access to files, apps and scripts. / Mac users away from their computer, developers running long scripts
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend Electron; React; Tailwind CSS; backend Flask; REST; db ; hosting 
- **Tech/APIs:** Claude (ai_model, core, sponsor); Fish Audio (ai_model, core, sponsor); Fetch.ai (other, core, sponsor); Groq (ai_model, supporting, sponsor); Electron (framework, core); Flask (framework, supporting); Hugging Face (ai_model, token)
- **Sponsor APIs:** Claude; Fish Audio; Fetch.ai; Groq
- **Repo:** public, commits 114 (before/in/after event: 0/101/13), README detailed
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Uses Fish Audio virtual mic and speaker devices to pipe live FaceTime call audio to the agent and speak replies back, with no official FaceTime API.
- **Team size:** 3 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates from memory; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/facetime-macos-ai-agent) | [GitHub](https://github.com/ThePickleGawd/calhacks-25)

### Hardware Context Protocol (MCP for Hardware)  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Crater: Play-Do Prize [unknown]; Winner Cal Hacks: Best Hardware Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** SDK and protocol letting LLMs discover and control hardware nodes over a custom TCP pub/sub layer, demoed with an inverse-kinematics robot arm that picks ingredients.
- **Problem / user:** LLMs lack a standard way to sense and act in the physical world, such as household tasks like preparing food. / robotics and hardware developers
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** hardware; desktop / True / llm_chat; agent_or_tool_use; vision
- **Stack:** langs Python; frontend ; backend Flask; TCP; db ; hosting 
- **Tech/APIs:** SOARM101 robot arm (hardware_part, core); OpenCV / AprilTags (framework, core); ASI:One (ai_model, unclear); Flask (framework, supporting); Custom TCP pub/sub layer (framework, core)
- **Sponsor APIs:**  | fit: Won the Crater Play-Do prize with an LLM-driven robot arm demo; the page does not state what Crater required.
- **Repo:** public, commits 95 (before/in/after event: 0/95/0), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** JSON hardware-node definitions generate a TCP networking layer; SOARM101 arm needed a custom inverse kinematics solver and simulator; AprilTags with OpenCV supply object positions.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; is_sponsor; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/hardware-context-protocol) | [GitHub](https://github.com/danielzyy/calhacks2025)

### Haven  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Fetch AI: Best Use of Fetch AI [unknown]; Winner Y Combinator: Build an Iconic YC Company - 1st Place [1st]; Winner LiveKit: Best Start-up Idea [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent hospital command center: a LiveKit voice assistant collects patient needs, monitoring agents raise alerts, and nurses get consolidated summaries.
- **Problem / user:** Understaffed hospitals leave patients waiting while nurses spend much time hunting through fragmented systems for information. / nurses, patients and families
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice; vision; llm_chat
- **Stack:** langs Python; TypeScript; Swift; SQL; Shell; frontend ; backend WebSocket; db ; hosting 
- **Tech/APIs:** LiveKit (other, core, sponsor); Fetch.ai (other, core, sponsor); Claude (ai_model, core, sponsor); OpenAI Realtime API (ai_model, core); OpenAI Whisper (ai_model, supporting); Grok (ai_model, supporting); OpenCV (framework, supporting); rPPG (other, supporting)
- **Sponsor APIs:** LiveKit; Fetch.ai; Claude | fit: Targeted Fetch AI, YC and LiveKit prizes by using LiveKit for the WebRTC voice interface, Fetch.ai agents for monitoring and alerts, and Claude agents, pitched as a hospital startup idea.
- **Repo:** public, commits 293 (before/in/after event: 0/291/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims True (Claims nurses spend up to 50% of time on documentation and a 20-minute workflow reduced.)
- **Notes:** Three layers: LiveKit WebRTC voice agent with OpenAI Realtime and Whisper, Fetch.ai monitoring and alert agents, and Claude agents; also lists OpenCV and remote photoplethysmography vitals; won three sponsor prizes.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; prizes; stack_languages
- **Links:** [Devpost](https://devpost.com/software/haven-536r1q) | [GitHub](https://github.com/scrappydevs/haven)

### Orbit  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Fetch AI: Best Use of Fetch AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Multi-agent assistant that listens to meetings and voice commands, turns them into structured actions and executes them via Jira, email and calendar integrations.
- **Problem / user:** Meetings produce action items that rarely get done; note-taking tools record work but do not carry it out. / professionals and teams in meetings
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / True / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; frontend ; backend Python; db ; hosting Fetch.ai Agentverse
- **Tech/APIs:** Fetch.ai Agentverse (other, core, sponsor); Sim.ai (ai_model, core); Composio MCP (framework, core); Omi mic (hardware_part, supporting); Model Context Protocol (framework, core)
- **Sponsor APIs:** Fetch.ai Agentverse | fit: Targeted Best Use of Fetch AI by hosting the autonomous Orbit agent on Fetch.ai Agentverse for persistence and agent collaboration.
- **Repo:** public, commits 11 (before/in/after event: 0/11/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims True (Cites 11.3 weekly meeting hours, 57% of week on communication, $29,000 annual cost per employee, and pricing of $20-30 per user.)
- **Notes:** Middleware agent called Nexus connects to any MCP server via Composio; agent hosted on Fetch.ai Agentverse; Omi mic gives voice-triggered commands; writeup includes go-to-market and pricing.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/orbit-n97hqz) | [GitHub](https://github.com/Ganeshmohank/orbit.git)

### Physical Digital Darts (Wii Darts)  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Cal Hacks: Best Beginner Hack [unknown]  (tier: track_winner)
- **Pitch:** 3D-printed dart with an accelerometer and Arduino that captures a throwing motion and launches a dart on a Python-simulated dartboard.
- **Problem / user:** The team wanted an accessible, immersive Wii-style game that links physical motion to a digital game. / casual gamers
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / False
- **Stack:** langs Python; Rust; frontend Pygame; backend PySerial; db ; hosting 
- **Tech/APIs:** MPU6050 accelerometer/gyro (hardware_part, core); Arduino Nano (hardware_part, core); Pygame (framework, core); PySerial (framework, supporting); 3D-printed casing (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 36 (before/in/after event: 0/36/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** MPU6050 drift handled with a custom filter and double-tap recalibration; Arduino Nano sends roll/pitch/yaw over serial to a Pygame simulator; team repaired three broken venue 3D printers.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/digital-physical-darts-wii-darts) | [GitHub](https://github.com/commonkestrel/physical-digital-darts)

### Ted.AI  (Cal Hacks 12.0 (2025))

- **Prizes:** Winner Cal Hacks: 2nd Overall [2nd]; Winner LiveKit: Most Creative Project [unknown]  (tier: overall_top3)
- **Pitch:** Sensor-laden teddy bear that senses hugs, motion and heart rate, talks with an LLM to calm children, and feeds a clinician dashboard.
- **Problem / user:** Children with anxiety, ADHD or loneliness lack an empathetic companion that helps regulate emotions; parents and clinicians lack visibility. / children with emotional struggles, parents, educators, clinicians
- **Domain / idea type:** mental_health + education / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; frontend React; D3.js; backend Flask; LangChain; MQTT; db MongoDB; InfluxDB; Firebase; hosting AWS; Docker
- **Tech/APIs:** ESP32 with pulse, touch and MPU6050 sensors (hardware_part, core); OpenAI Whisper (ai_model, core); OpenAI GPT (ai_model, core); RoBERTa (ai_model, supporting); LangChain (framework, supporting); MQTT (other, supporting); Fetch.ai (other, unclear, sponsor); Gemini (ai_model, unclear); LiveKit (other, unclear, sponsor); AWS (cloud, unclear)
- **Sponsor APIs:** LiveKit; Fetch.ai | fit: LiveKit prize listed; the writeup does not describe LiveKit use, though Fetch.ai appears in Built With.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots None, writeup long, impact claims False
- **Notes:** ESP32 bear with pulse, touch and accelerometer sensors; fuses sensor data over MQTT; dashboard shows simulated brain-region activations. Long stack list incl. TensorFlow Lite Micro, InfluxDB.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; n_screenshots; ui_polish; sponsor_apis_used; event dates from memory
- **Links:** [Devpost](https://devpost.com/software/ted-ai-x8537t)


## Cal Hacks 13.0 (2026)

### ANNEAL  (Cal Hacks 13.0 (2026))

- **Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance [unknown]  (tier: sponsor_winner)
- **Pitch:** Agent that spots Formula 1 crashes in live car data, classifies likely damaged parts and drafts spares, freight and accounting entries against the cost cap.
- **Problem / user:** After a crash, F1 engineering, logistics and finance keep inconsistent versions of the damage, so parts and cost-cap planning run on wrong numbers. / F1 team finance and operations staff
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Three.js; backend FastAPI; Node.js; Pydantic; SpacetimeDB; db SpacetimeDB; hosting Azure Container Apps; Docker; Bicep
- **Tech/APIs:** Microsoft Dynamics 365 Business Central (other, core, sponsor); Azure OpenAI (ai_model, core, sponsor); Azure Container Apps (cloud, supporting, sponsor); Azure Key Vault (cloud, supporting, sponsor); Claude (ai_model, core); TypeSafe (other, core, sponsor); Apify (data_source, supporting); OpenF1 (data_source, core); Jolpica F1 API (data_source, core); SpacetimeDB (database, supporting); Microsoft Teams / Outlook (other, supporting, sponsor)
- **Sponsor APIs:** Microsoft Dynamics 365 Business Central; Azure OpenAI; Azure Container Apps; Azure Key Vault; TypeSafe | fit: Targeted Hyphenate's autonomous-finance challenge by having an agent turn detected crashes into spares reservations, freight plans and accounting entries in Business Central with Azure services.
- **Repo:** public, commits 47 (before/in/after event: 0/47/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims True (Cites a roughly $4 million Williams crash repair bill and claims crash detection 9 to 26 seconds before red flags.)
- **Notes:** Uses real race data (OpenF1, Jolpica, FIA documents via Apify) and claims detection of Williams crashes 9 to 26 seconds before red flags; posts accounting entries into Dynamics 365 Business Central; Three.js car view.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_apis_used; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/anneal-u3xh1o) | [GitHub](https://github.com/gaviiin/calhacks/tree/main)

### Arigami  (Cal Hacks 13.0 (2026))

- **Prizes:** Winner Cal Hacks Best Beginner Hack [unknown]  (tier: track_winner)
- **Pitch:** Chrome/Edge extension that rewrites the current page into a layout for focus, motor-impairment or screen-reader needs, with optional AI redesign and head-tracking navigation.
- **Problem / user:** Websites are hard for people with motor impairments or other accessibility needs to use independently. / people with motor impairments, attention or vision accessibility needs
- **Domain / idea type:** accessibility + dev_tools / creative_tool
- **Platforms / hardware / AI:** browser_extension / False / llm_chat; vision
- **Stack:** langs JavaScript; frontend Chrome Manifest V3 extension; Figma; backend ; db ; hosting Figma Sites
- **Tech/APIs:** Claude (ai_model, supporting); Apify (other, supporting); Figma (other, supporting); Chrome Manifest V3 (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: 0/3/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Three accessibility modes; scroll gradient and head-tracking replace a planned eye-tracker; AI redesign path uses Apify scraping plus Claude; designs prototyped in Figma and code written with Claude.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/arigami-web-accessibility) | [GitHub](https://github.com/yassinabdelal-ipynb/access)

### BrainSync  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Most Technically Complex Hack [unknown]  (tier: track_winner)
- **Pitch:** Brain-computer interface where users pick flickering on-screen options by gaze (SSVEP via EEG), including a mode that proposes Claude-written replies spoken in the user's voice.
- **Problem / user:** People with Parkinson's, ALS or locked-in syndrome lose the ability to type, point or speak clearly. / people with severe motor or speech impairment
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; Swift; JavaScript; HTML; Shell; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Claude (ai_model, core); Cartesia (ai_model, supporting); OpenBCI / Cerelog X8 EEG (hardware_part, core); CCA SSVEP decoder (other, core)
- **Sponsor APIs:**  | fit: Event-run Most Technically Complex Hack prize, not a sponsor challenge; page shows real-time EEG decoding with custom hardware as the technically complex element.
- **Repo:** public, commits 218 (before/in/after event: 0/218/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Uses an 8-channel EEG headset with a training-free CCA decoder on occipital channels and 11-17 Hz flicker targets; replies drafted by Claude and voiced via Cartesia; long technical writeup with math.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; platforms; stack_languages
- **Links:** [Devpost](https://devpost.com/software/brainsync) | [GitHub](https://github.com/1thing2say/BrainSync)

### Drigil  (Cal Hacks 13.0 (2026))

- **Prizes:** [Anthropic] Claude for Public Benefit [unknown]  (tier: sponsor_winner)
- **Pitch:** Wearable-camera job coach for workers with intellectual or developmental disabilities: Claude turns a supervisor's narrated video into steps, then gives live spoken guidance and corrections.
- **Problem / user:** Few people with disabilities are employed, and job-coach support in the first weeks of a new job is scarce. / workers with intellectual or developmental disabilities, supervisors
- **Domain / idea type:** accessibility + productivity_workplace / social_good
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend React; React Router; backend FastAPI; WebSockets; db SpacetimeDB; hosting Vercel
- **Tech/APIs:** Anthropic Claude (ai_model, core, sponsor); Cartesia (ai_model, core); MediaPipe (framework, core); OpenCV (framework, supporting); Gemini (ai_model, supporting); OpenAI API (ai_model, supporting); SpacetimeDB (database, supporting); Raspberry Pi / Arduino (hardware_part, supporting); Moss (other, unclear)
- **Sponsor APIs:** Anthropic Claude | fit: Targeted Claude for Public Benefit by using Claude to convert a supervisor's narrated task video into coaching steps and corrections for workers with developmental disabilities.
- **Repo:** public, commits 31 (before/in/after event: 0/31/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 34, writeup long, impact claims True (Cites US BLS figures: 22.7% employment for people with disabilities in 2024 versus 65.5% without.)
- **Notes:** Privacy design blurs faces and runs MediaPipe hand tracking in the browser before frames leave the device; supervisor voice cloned via Cartesia with consent; page has a Real vs. simulated section and a wristband; 34 gallery images.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/drigil) | [GitHub](https://github.com/shraddha11-408/CalHacks-13.0)

### Eve: event finances handled  (Cal Hacks 13.0 (2026))

- **Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance [unknown]  (tier: sponsor_winner)
- **Pitch:** Permission-limited AI agent that processes hackathon travel claims, prizes, tax forms and sponsor-portal paperwork, leaving payment release to a human controller.
- **Problem / user:** Hackathon organizers lack tooling for reimbursements and prize payouts, causing months-long delays and missed tax-form requirements for winners. / hackathon and event organizers
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind CSS; shadcn/ui; backend Next.js server actions; Drizzle; Better Auth; Vercel Workflow; db PostgreSQL (PlanetScale); hosting Vercel
- **Tech/APIs:** Claude (Anthropic SDK, computer use) (ai_model, core); Vercel AI SDK (framework, supporting); E2B desktop sandbox (cloud, core); Vercel Workflow (cloud, supporting); PlanetScale Postgres (database, core); Better Auth (auth, supporting); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted the Hyphenate autonomous-finance challenge with an agent that prepares payouts, tax withholding and ledger entries under role-limited permissions.
- **Repo:** public, commits 184 (before/in/after event: 0/183/1), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Reports catching all 40 planted problems in a seeded 300-person event with 160 claims and 25 prizes.)
- **Notes:** Claude computer use on an E2B desktop fills university finance portals but stops before Submit; amounts and tax math are deterministic code; tested on seeded event with 40 planted problems, all caught; money movement simulated.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; event_start; event_end; sponsor_apis_used; team_size
- **Links:** [Devpost](https://devpost.com/software/eve-event-finances-handled) | [GitHub](https://github.com/uijincho/eve)

### FortWatch  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Best Hardware Hack [unknown]  (tier: track_winner)
- **Pitch:** Low-cost ESP32-S3 wristband that classifies nearby sounds on-device and shows and vibrates alerts for deaf users, with a live event dashboard.
- **Problem / user:** Deaf people lack an affordable alternative to smartwatches for noticing important sounds like doorbells and car horns when out alone. / deaf and hard-of-hearing people
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / predictive_ml
- **Stack:** langs C++; Python; TypeScript; frontend Arduino GFX; backend Node.js; SpacetimeDB; db SpacetimeDB; hosting Mana
- **Tech/APIs:** ESP32-S3 (Waveshare touch LCD) (hardware_part, core); YAMNet / TensorFlow (ai_model, core); ESC-50 dataset (data_source, supporting); SpacetimeDB (database, supporting); Mana (cloud, supporting); Claude Code (ai_model, supporting); OpenSCAD 3D case (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 67 (before/in/after event: 0/58/9), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (States Claude Code wrote over 85% of the code and parts could cost as little as $10.)
- **Notes:** YAMNet-based classifier runs on the ESP32-S3 twice a second with audio never leaving the device; 10 sound classes tuned on ESC-50; urgency-coded vibration; SpacetimeDB dashboard on Mana; writeup says Claude Code wrote over 85% of code.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/fortwatch) | [GitHub](http://github.com/joaquinGiorgis/calhack/)

### GovTok  (Cal Hacks 13.0 (2026))

- **Prizes:** Winner Cal Hacks Most Creative Hack [unknown]  (tier: track_winner)
- **Pitch:** TikTok-style feed where residents film neighborhood problems, reports are pinned to location, and followers watch each issue go from reported to fixed.
- **Problem / user:** Cities have a communication gap on infrastructure issues like potholes, and form-based reporting lacks context and visibility. / city residents and municipal agencies
- **Domain / idea type:** civic_legal + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind; backend Node.js; Convex; db Convex; hosting Vercel
- **Tech/APIs:** Claude (ai_model, core); Whisper (ai_model, supporting); Groq (ai_model, supporting); Google Maps / Geocoding (maps_geo, core); Convex (database, core); Playwright (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 88 (before/in/after event: 0/88/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims False
- **Notes:** Claude (Opus) vision moderates uploads with no human review queue, checking for faces and plates, and transcripts are treated as untrusted input against prompt injection; duplicate check within 50 m before posting.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/govtok) | [GitHub](https://github.com/StreetLamp05/GovTok)

### GroundTruth  (Cal Hacks 13.0 (2026))

- **Prizes:** [Hyphenate] The Hyphenated Enterprise: Autonomous Systems for Finance [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous agent that settles satellite ground-station SLA credit disputes by weighing pass logs, space weather, maintenance notices and contract terms, escalating to a controller when needed.
- **Problem / user:** Ground-station operators settle dropped-pass billing disputes by hand across conflicting sources, which is slow at the volume of contacts they handle. / ground-station operators' dispute analysts and controllers
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml
- **Stack:** langs Python; Rust; TypeScript; frontend React; backend Python; Rust; Cedar; db SpacetimeDB; hosting AWS; Vercel
- **Tech/APIs:** Cedar policy language (framework, core); SpacetimeDB (database, core); AWS (cloud, supporting); CelesTrak / SGP4 (data_source, core); SHAP (framework, supporting); LLM (unspecified) (ai_model, core)
- **Sponsor APIs:**  | fit: Targeted Hyphenate's autonomous-finance challenge with an agent that settles SLA credit disputes under least-privilege Cedar policies, an audit trail and controller escalation; sponsor tools not named on page.
- **Repo:** public, commits 177 (before/in/after event: 0/175/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims True (Cites KSAT revenue of NOK 2.361B (about USD 234M) across about 2.1 million contacts on about 375 antennas.)
- **Notes:** Writeup is structured as questions (real enough, would you hire it) with simulated company data, Cedar authorization policy, SHAP explanations, CelesTrak/SGP4 orbit data and SpacetimeDB; agent that proposes a credit cannot approve it.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/groundtruth-k3g5v6) | [GitHub](https://github.com/AamirAbatiyow/CalHacks26)

### half full  (Cal Hacks 13.0 (2026))

- **Prizes:** Winner Cal Hacks Third Overall [3rd]  (tier: overall_top3)
- **Pitch:** Mobile-first PWA delivering a small daily edition of hopeful news with AI illustrations, narration, source receipts and a reaction jar.
- **Problem / user:** Doom-framed news and chopped-up social clips overwhelm young people, who stop following current events. / Gen Z news readers
- **Domain / idea type:** creative_media + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; generative_media; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; React; Motion; GSAP; PWA; backend Node.js; Apify Actor; db Firestore; hosting Vercel
- **Tech/APIs:** Anthropic Claude (ai_model, core, sponsor); Apify (data_source, core, sponsor); Recraft (ai_model, core); Cartesia (ai_model, core, sponsor); Firebase Auth and Firestore (auth, supporting); Runway (ai_model, supporting); Vercel (cloud, supporting); Next.js (framework, core)
- **Sponsor APIs:** Anthropic Claude; Apify; Cartesia
- **Repo:** public, commits 50 (before/in/after event: 0/50/0), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 10, writeup long, impact claims False
- **Notes:** Custom Apify Actor gathers evidence per story and the pipeline can reject under-supported stories; finite 3-5 story edition ends with a 'caught up' screen, plus crossword and illustrated reactions.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates
- **Links:** [Devpost](https://devpost.com/software/half-full) | [GitHub](https://github.com/rainazab/half-full)

### muselet  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Best Solo Hack [unknown]  (tier: track_winner)
- **Pitch:** Voice-triggered Mac agent that runs entirely on Apple Silicon, using a fast fine-tuned router and a local planner to click, type and verify outcomes.
- **Problem / user:** Cloud computer-use agents are slow and send the whole screen off the machine, a privacy and cost problem. / Mac power users and people who find mouse and keyboard hard to use
- **Domain / idea type:** ai_agents_infra + accessibility / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / llm_chat; agent_or_tool_use; speech_or_voice; vision
- **Stack:** langs Swift; Python; frontend SwiftUI; backend Python; WebSocket; db ; hosting local Apple Silicon
- **Tech/APIs:** Qwen3.5-4B + LoRA (MLX) (ai_model, core); Parakeet TDT v2 / FluidAudio (ai_model, core); Tinker (training) (cloud, supporting); macOS Accessibility API (framework, core); eyes-4b vision model (ai_model, supporting); SwiftUI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 481 (before/in/after event: 0/481/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims True (Reports 94.5% router accuracy, ~60 ms median latency, under $150 training cost and zoom grounding gain from 36.0% to 63.5%.)
- **Notes:** Router is Qwen3.5-4B with a self-trained LoRA scoring 43 actions in one pass (reports ~60 ms, 94.5% on route_v2); local planner, speech and OCR; ghost cursor shows intent; risky actions need spoken confirmation.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/museles) | [GitHub](http://github.com/ardahk/muselet)

### Orbit Health  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Best Planet-First Social Impact Hack [unknown]  (tier: track_winner)
- **Pitch:** Village pod with camera, mic and pulse oximeter runs a nurse-style voice triage, then a satellite-aware planner ships medicines to rural Zambian clinics before roads flood.
- **Problem / user:** Rural Zambian villages cannot signal what medicine they need and stock does not reach clinics before rainy-season road closures. / rural villagers in Zambia, clinic staff, health logistics planners
- **Domain / idea type:** health_wellness + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; speech_or_voice; vision; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js 15; backend SpacetimeDB reducers; Next.js API routes; TensorFlow; db SpacetimeDB; hosting local laptop
- **Tech/APIs:** SpacetimeDB (database, core, sponsor); Grok Voice (xAI) (ai_model, core); Jev (TypeSafe) (ai_model, core); Claude (ai_model, supporting, sponsor); NASA and Copernicus satellite data (data_source, core); OpenStreetMap / OSRM (maps_geo, core); Seeed XIAO nRF52840 with MAX30101 and Grove Vision AI V2 (hardware_part, core); HumBug mosquito models (ai_model, supporting)
- **Sponsor APIs:** SpacetimeDB; Claude | fit: Planet-First track win; the only sponsor mentions are SpacetimeDB as the full backend and Claude for wording and second-opinion camera checks.
- **Repo:** public, commits 86 (before/in/after event: 0/86/0), README solid
- **Demo/writeup:** video None, live none, screenshots 3, writeup long, impact claims True (Cites Zambia malaria cases and clinic stockout statistics, and simulated planner savings of 833 to 83 movements and 112,849 km.)
- **Notes:** Solo build; maps 23,206 villages from satellite roof counts, uses keyless satellite data, SpacetimeDB reducers as the whole backend, firmware on real boards, mosquito wingbeat classifier.
- **Team size:** 1 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates
- **Links:** [Devpost](https://devpost.com/software/orbit-health) | [GitHub](https://github.com/philiprmocanu-cell/triage-pod)

### Rouge - Sees Your Screen and Points the Way  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Hacker's Choice [unknown]  (tier: track_winner)
- **Pitch:** Windows desktop assistant drawn as an animated ribbon that points at on-screen controls, performs browser tasks, explains errors and answers from local documents.
- **Problem / user:** Voice assistants talk about your work rather than working with you on the screen you are looking at. / Windows desktop users
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / llm_chat; agent_or_tool_use; rag_or_search; vision; speech_or_voice
- **Stack:** langs JavaScript; C#; PowerShell; frontend Electron; WebGL; Canvas; backend Node.js; db ; hosting 
- **Tech/APIs:** Anthropic Claude (Haiku/Sonnet/Opus) (ai_model, core); Windows UI Automation (C#/PowerShell) (framework, core); Electron (framework, core); Qwen3.5 (local) (ai_model, supporting); BM25 local search (other, supporting); Serper API (data_source, supporting); WebGL (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 65 (before/in/after event: 0/63/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims True (Reports idle CPU drop from about 34% to 7% of a core and window lookups 35x faster (71ms to 2ms).)
- **Notes:** Reads Windows UI Automation controls instead of screenshots; routes between Haiku, Sonnet and Opus per request; user-supplied API keys encrypted locally; reports idle CPU cut from about 34% to 7%.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/rouge-cm8jig) | [GitHub](https://github.com/RithikGobinath/rouge)

### Silent Voice  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Second Overall [2nd]; [Cartesia] Best Use of Cartesia [unknown]  (tier: overall_top3)
- **Pitch:** Reads silent mouthing via camera lip reading and face EMG, uses Claude to predict dialogue, and speaks in the user's cloned voice over a live phone call.
- **Problem / user:** People who lose their voice box after laryngectomy cannot speak in their own voice; existing devices give robotic sound. / laryngectomy patients and their families
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / llm_chat; speech_or_voice; vision; predictive_ml
- **Stack:** langs Python; frontend dashboard; backend PyTorch; MediaPipe; KenLM; ZeroMQ; Twilio; db ; hosting local laptop with RTX 5060
- **Tech/APIs:** Cartesia Sonic and Ink (ai_model, core, sponsor); Claude (Haiku and Opus) (ai_model, core, sponsor); Auto-AVSR (ai_model, core); EMG sensor pads with Arduino (hardware_part, core); Twilio (telecom, core); PyTorch (framework, supporting); MediaPipe (framework, supporting)
- **Sponsor APIs:** Cartesia; Claude | fit: Used Cartesia Sonic for streaming cloned-voice output with emotion and Cartesia Ink for caller transcription over a live phone call.
- **Repo:** public, commits 129 (before/in/after event: 0/125/4), README detailed
- **Demo/writeup:** video None, live none, screenshots 6, writeup long, impact claims True (Cites ~190,000 yearly voice-box cancer cases and measured error rates, latency and accuracy figures from its own tests.)
- **Notes:** Fuses a retrained lip reader, a custom EMG model on four face pads, and Claude next-word prediction every 100 ms; claims 9.8% word error on a new session and ~0.7 s latency; runs on one laptop with Twilio call demo.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates
- **Links:** [Devpost](https://devpost.com/software/silent-voice-s1f74p) | [GitHub](https://github.com/thaimtl/Silent-Voice)

### Sophi - The Physical Augmentation Walker  (Cal Hacks 13.0 (2026))

- **Prizes:** Winner Cal Hacks First Overall [1st]  (tier: overall_top3)
- **Pitch:** Walker with a voice agent, distance-sensing haptics, robotic arms, lift and GPS, plus a caregiver companion app.
- **Problem / user:** Falls and mobility limits threaten independence of elderly and disabled people, and caregivers lack ways to check in. / elderly and mobility-impaired people, blind users, caregivers
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; mobile_cross / True / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; Python; C++; frontend Next.js; React; Leaflet.js; backend Node.js; Zod; PlatformIO; db PostgreSQL; Supabase; SpacetimeDB; hosting Render
- **Tech/APIs:** Claude (Anthropic) (ai_model, core, sponsor); Cartesia (ai_model, core, sponsor); SpacetimeDB (database, core, sponsor); Raspberry Pi 5 and ESP32 modules (hardware_part, core); SO-101 robot arms (hardware_part, core); Supabase (database, supporting); OpenStreetMap / Leaflet (maps_geo, supporting); Stripe (payments, token); Piper TTS (ai_model, unclear)
- **Sponsor APIs:** Claude; Cartesia; SpacetimeDB
- **Repo:** public, commits 331 (before/in/after event: 0/331/0), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 14, writeup long, impact claims True (Cites 340 million blind or low-vision people and 1.7 billion people with mobility restrictions as the addressable population.)
- **Notes:** Raspberry Pi 5 plus three ESP32s, four soldered boards and 30+ 3D-printed parts; SO-101 arms driven by a custom iPhone-based harness after other control options proved unreliable.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates
- **Links:** [Devpost](https://devpost.com/software/sophi) | [GitHub](https://github.com/mzhao1599/sophi)

### Standard Response  (Cal Hacks 13.0 (2026))

- **Prizes:** Cal Hacks Best People-First Social Impact Hack [unknown]; [Microsoft] Built for the Real World (1st), Customer Impact Award (2nd) [unknown]; [Convex] Best use of Convex [unknown]; [Apify] Best Use of Apify [unknown]; [Moss] Best Use of Moss [unknown]; [Anthropic] Claude for Public Benefit [unknown]  (tier: track_winner)
- **Pitch:** Voice agent phones every home in a wildfire evacuation zone, triages who cannot leave, and dispatches accessible vehicles or neighbors, promising help only once a driver accepts.
- **Problem / user:** Disabled residents were left behind in the Eaton Fire because no one had staff to call everyone and coordinate available vans. / paratransit agencies, dispatchers, disabled and elderly residents, neighbors
- **Domain / idea type:** safety_security + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; speech_or_voice; rag_or_search; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind CSS; backend Node.js; Convex; OR-Tools; SimPy; OSMnx; Twilio; WebSockets; db Convex; hosting Fly.io; DigitalOcean; Vercel
- **Tech/APIs:** Claude (Haiku, Sonnet, Opus) (ai_model, core, sponsor); Cartesia Ink and Sonic (ai_model, core, sponsor); Moss (data_source, core, sponsor); Convex (database, core, sponsor); Apify Actor (data_source, core, sponsor); Twilio (telecom, core); Mana (other, supporting, sponsor); OR-Tools and custom ALNS solver (other, core); OSMnx / OpenStreetMap (maps_geo, core); DigitalOcean (cloud, supporting); Fly.io (cloud, supporting)
- **Sponsor APIs:** Claude; Cartesia; Moss; Convex; Apify; Mana | fit: Social impact track win; writeup has a per-sponsor section describing Claude, Cartesia, Moss, Convex, Apify and Mana each doing a specific job.
- **Repo:** public, commits 300 (before/in/after event: 0/436/4), README detailed
- **Demo/writeup:** video None, live not_checked, screenshots 16, writeup long, impact claims True (Simulation results on Eaton Fire night (641 of 662 on time vs 39), voice-exam scores, 0.86 s median turn latency, and firefighter quotes.)
- **Notes:** Eaton Fire night simulation over real records (claims 641 of 662 households out on time vs 39 modeled today); promise guard enforced in code; custom Apify Actor; Mana-written tests; team visited fire stations.
- **Team size:** 4 | **Confidence:** medium | unverified: has_demo_video; ui_polish; is_sponsor flags; event dates
- **Links:** [Devpost](https://devpost.com/software/standard-response) | [GitHub](https://github.com/Imhaohao/calhacks)

### TouchSpace  (Cal Hacks 13.0 (2026))

- **Prizes:** [Anthropic] Claude for Public Benefit [unknown]  (tier: sponsor_winner)
- **Pitch:** Scans indoor spaces with an iPhone LiDAR, builds a floor plan and route graph, and conveys it to blind users via voice and a tactile hardware display.
- **Problem / user:** Blind and visually impaired people cannot easily learn the layout of unfamiliar buildings, which turn-by-turn apps do not convey. / blind and visually impaired people
- **Domain / idea type:** accessibility + mobility_transport / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; web; hardware / True / llm_chat; speech_or_voice
- **Stack:** langs Swift; Python; TypeScript; frontend SwiftUI; React; Vite; Tailwind; backend FastAPI; Pydantic; Uvicorn; Shapely; db SQLite; hosting 
- **Tech/APIs:** Claude (ai_model, core, sponsor); Apple RoomPlan / ARKit / LiDAR (hardware_part, core); Web Speech API (framework, supporting); Web Audio API (framework, supporting); FastAPI (framework, core); SwiftUI (framework, core)
- **Sponsor APIs:** Claude | fit: Targeted Claude for Public Benefit as an accessibility tool; Claude is listed in the stack for the conversational layer, though the page excerpt read does not detail exactly how.
- **Repo:** public, commits 71 (before/in/after event: 0/71/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 40, writeup long, impact claims False
- **Notes:** Combines Apple RoomPlan/LiDAR scanning in a SwiftUI app, shareable .touchspacemap bundles via a community drive, a web app and a tactile hardware display; 40 gallery images.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/touchspace) | [GitHub](https://github.com/holokcheung/touchspace)
