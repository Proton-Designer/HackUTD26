# Hack the North: project cards (30 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Hack the North 2024

### ChatGPMe  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Overcooked-style Unity game where you play ChatGPT answering a stream of human requests, scored by how AI-like your replies are.
- **Problem / user:** Flips the AI hype: the player must answer queries quickly under time pressure as the AI. / casual gamers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / llm_chat
- **Stack:** langs C#; JavaScript; frontend Unity; backend ; db ; hosting Google Cloud
- **Tech/APIs:** Cohere API (ai_model, core, sponsor); Unity (framework, core); Defang (cloud, supporting, sponsor); Google Cloud (cloud, unclear)
- **Sponsor APIs:** Cohere; Defang
- **Repo:** public, commits 31 (before/in/after event: 0/31/0), README none
- **Demo/writeup:** video None, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** Typed answers are scored by Cohere on similarity to an AI response; Defang used to generate a template and sanitise input; hand-drawn Procreate sprites.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/chatgpme) | [GitHub](https://github.com/r-chong/HTN-2024/)

### ConArt AI  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Gamified team brainstorming app: players sketch and prompt against a timer, sketches become concept images, and teammates vote.
- **Problem / user:** Teams stall at the start of design and need a fast, fun way to turn rough ideas into concept art. / design teams and artists in early ideation
- **Domain / idea type:** creative_media + productivity_workplace / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media
- **Stack:** langs JavaScript; CSS; frontend React; Vite; Tailwind; backend Convex; db Convex; hosting Vercel
- **Tech/APIs:** Convex (database, core, sponsor); Replicate API (ai_model, core); ControlNet / Stable Diffusion (ai_model, core); Vercel (cloud, supporting)
- **Sponsor APIs:** Convex
- **Repo:** public, commits 63 (before/in/after event: 0/62/1), README thin
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Convex handles real-time game state while actions call Replicate (ControlNet plus Stable Diffusion); deployed on Vercel with a custom domain listed.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/conart-ai) | [GitHub](https://github.com/benjamindrussell/conartAI)

### Flashback  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists; Winner Intuit: Win a VR Headset! [unknown]  (tier: honorable_or_finalist)
- **Pitch:** VR museum of personal memories: upload photos, video and audio on a web app and walk through them as exhibits on a Quest.
- **Problem / user:** Fleeting meaningful moments are easily forgotten; the team wanted a private, immersive way to revisit them. / individuals wanting to relive personal memories
- **Domain / idea type:** creative_media + mental_health / new_category
- **Platforms / hardware / AI:** web; other / True / False
- **Stack:** langs JavaScript; C#; frontend React; Material UI; Unity; backend Node.js; Express.js; db Convex; hosting 
- **Tech/APIs:** Unity + Meta Quest (hardware_part, core); Convex (database, core, sponsor); Spotify API (data_source, supporting); Figma (other, supporting)
- **Sponsor APIs:** Convex | fit: Intuit prize is a VR headset giveaway prize; the page does not describe an Intuit product use.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Two-part system: React/Convex web uploader plus Unity C# VR gallery tested on Meta Quest; exhibits trigger audio and captions on approach; Figma hi-fi mockups; Spotify API.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor; has_demo_video; github_url (queue gave org listing; not a repo, so null); live_demo_url (only a Figma link listed, not recorded); repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/flashback-q3kzg9) | [GitHub](https://github.com/orgs/htn-2024/repositories)

### LureLore  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Photo-based fishing log: Gemini identifies each catch, which appears in a 3D aquarium and on a shared map with achievements.
- **Problem / user:** Fishing memories are poorly captured by photos alone; anglers want to track catches and share spots. / recreational anglers
- **Domain / idea type:** entertainment_games + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs JavaScript; frontend React; Three.js; Leaflet; backend Node.js; Express; db MongoDB Atlas; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Three.js (framework, core); Leaflet.js (maps_geo, supporting); MongoDB Atlas (database, core)
- **Sponsor APIs:** MongoDB Atlas
- **Repo:** public, commits 73 (before/in/after event: 0/70/3), README detailed
- **Demo/writeup:** video None, live none, screenshots 8, writeup medium, impact claims False
- **Notes:** Three.js interactive aquarium of past catches plus Leaflet community map of catch locations and achievements unlocked by fish size or first catch.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/lurelore) | [GitHub](https://github.com/danielh-hong/hackthenorth2024)

### PathSense  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists; Winner Cohere: Best Use of Cohere [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Voice-driven indoor navigation for visually impaired users, combining camera object detection, scene description and MappedIn routing.
- **Problem / user:** Outdoor navigation is well served but visually impaired people lack real-time guidance inside buildings. / visually impaired people navigating indoor venues
- **Domain / idea type:** accessibility + mobility_transport / new_category
- **Platforms / hardware / AI:** hardware; web / True / vision; speech_or_voice; agent_or_tool_use; rag_or_search; llm_chat
- **Stack:** langs Python; JavaScript; TypeScript; frontend React; Tailwind CSS; backend Node.js; db Convex; hosting Vercel; ngrok
- **Tech/APIs:** MappedIn SDK (maps_geo, core, sponsor); Voiceflow (other, core, sponsor); Cohere Rerank (ai_model, core, sponsor); Convex (database, supporting, sponsor); Groq Whisper (ai_model, supporting, sponsor); GPT-4 Vision mini (ai_model, core); Detectron2 (ai_model, core); DPT depth estimation (ai_model, supporting); Unreal Engine TTS (other, supporting); TAPO cameras (hardware_part, core); Auth0 (auth, token, sponsor)
- **Sponsor APIs:** Cohere; MappedIn; Voiceflow; Convex; Groq; Auth0 | fit: Cohere Rerank API does semantic search over computer-vision tags and mapping data in response to user queries.
- **Repo:** public, commits 87 (before/in/after event: 0/83/4), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Pipeline of Detectron, DPT depth and GPT-4 Vision on TAPO camera streams, Cohere Rerank over stored tags, Voiceflow dialogue, MappedIn routes, Groq Whisper STT and Unreal TTS.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video; live_demo_url (ngrok tunnel link not recorded)
- **Links:** [Devpost](https://devpost.com/software/pathsense-athy2r) | [GitHub](https://github.com/akjadhav/hackthenorth-2024)

### TinkerFlow  (Hack the North 2024)

- **Prizes:** Winner Hack the North 2024 Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Photo or text list of electronic parts goes in; an LLM returns a project idea, wiring schematic and step-by-step instructions.
- **Problem / user:** Beginners struggle to know how components wire together and what to build with the parts they have. / beginner electronics tinkerers
- **Domain / idea type:** education + dev_tools / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; vision; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; React Flow; backend Flask; LangChain; db ; hosting 
- **Tech/APIs:** Cohere LLM (ai_model, core, sponsor); Groq LLM (ai_model, supporting, sponsor); Google Vision AI (ai_model, core); LangChain (framework, supporting); React Flow (framework, core)
- **Sponsor APIs:** Cohere; Groq
- **Repo:** public, commits 63 (before/in/after event: 0/60/3), README thin
- **Demo/writeup:** video None, live none, screenshots 3, writeup medium, impact claims True (Cites workforce survey percentages on learning new skills and 80% component classification accuracy.)
- **Notes:** Custom React Flow based schematic drawer because existing libraries were deprecated; selectable Cohere (default, RAG and preamble) or Groq LLM; Google Vision identifies parts at about 80% accuracy.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/tinkerflow) | [GitHub](https://github.com/wilsonchenghy/TinkerFlow)


## Hack the North 2025

### ChessMate  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Robotic chessboard with a two-axis magnetic gantry that moves pieces for a remote opponent, with voice commands and AI coaching.
- **Problem / user:** Distance and mobility or vision limits make it hard to play physical chess with family or friends. / chess players, remote families, people with mobility or vision limits
- **Domain / idea type:** accessibility + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / agent_or_tool_use; vision; speech_or_voice; llm_chat
- **Stack:** langs Python; frontend Next.js; React; backend Raspberry Pi; Arduino; db ; hosting 
- **Tech/APIs:** Raspberry Pi 5 (hardware_part, core); Arduino (hardware_part, core); NEMA 17 steppers + gantry (hardware_part, core); Groq (ai_model, supporting, sponsor); Computer vision piece detection (other, core)
- **Sponsor APIs:** Groq
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README none
- **Demo/writeup:** video None, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Dual NEMA17 gantry with electromagnet moves magnetised pieces; Pi 5 runs webcam piece detection, chess engine and collision-free pathfinding, Arduino drives motors; voice agent via web app.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; team_size; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/chessmate-nwygvq) | [GitHub](https://github.com/o-bm/ChessMate)

### Coach Bob!  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** AR warm-up game: XReal glasses overlay punch/kick targets on a punching bag while a voiced Coach Bob taunts, with force sensing on impact.
- **Problem / user:** Athletes skip proper warm-ups, causing injuries; the build makes warming up engaging. / martial arts athletes and people training on a bag
- **Domain / idea type:** health_wellness + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / speech_or_voice; vision; llm_chat
- **Stack:** langs C++; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** XReal AR glasses (hardware_part, core); OAK-1 AF camera (hardware_part, core); OpenCV (framework, core); MPU-6050 IMU (hardware_part, core); Gemini (ai_model, supporting, sponsor); ElevenLabs (ai_model, supporting)
- **Sponsor APIs:** Gemini
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README solid
- **Demo/writeup:** video True, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Registers hits by reading the bag's wobble with an IMU instead of a force sensor; team says it started late and hardware needed reinforcing.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/coach-bob) | [GitHub](https://github.com/ultratrikx/oak_camera_project)

### DUM-E  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Voice-controlled 5-DOF robotic arm that uses a camera, homography and a multimodal LLM to pick and place objects on a workspace.
- **Problem / user:** Robot arms usually run fixed routines; the team wanted one that understands natural language and its surroundings. / makers and workspace users wanting a robotic assistant
- **Domain / idea type:** ai_agents_infra + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / llm_chat; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; C++; frontend ; backend Flask; Raspberry Pi; Arduino; db ; hosting 
- **Tech/APIs:** Llama 4 Maverick via Groq (ai_model, core, sponsor); Whisper Large V3 (ai_model, core); OpenCV (framework, core); Raspberry Pi (hardware_part, core); Arduino Uno (hardware_part, core); Servo motors (hardware_part, core)
- **Sponsor APIs:** Groq
- **Repo:** public, commits 141 (before/in/after event: 0/139/2), README thin
- **Demo/writeup:** video None, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Skips vision-language-action models: OpenCV segmentation on a warped top-down frame plus coordinates fed to a multimodal LLM, with inverse kinematics on Pi/Arduino and a feedback loop.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/dum-e-kgx6at) | [GitHub](https://github.com/pekachoo/htn-DUM-E)

### Lattice  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Live holographic capture: three Kinect v2 sensors merged into one 3D point cloud viewed in a HoloLens at about 20+ FPS.
- **Problem / user:** Real-world objects and people are hard to scan and share live in 3D with cheap hardware. / remote collaboration, medical training and live entertainment users
- **Domain / idea type:** creative_media + telecom_networking / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware / True / False
- **Stack:** langs C++; C#; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Xbox Kinect v2 (hardware_part, core); Microsoft HoloLens (hardware_part, core); Kinect for Windows SDK (framework, core); OpenCV (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 12 (before/in/after event: 0/12/0), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Three laptops each run a Kinect client feeding a central server; calibration via marker plus ICP; reports 23 FPS; used discontinued HoloLens over a phone hotspot.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/lattice-flck7q) | [GitHub](https://github.com/KenC2006/Lattice)

### Maatchaa  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Matches Shopify products with trending YouTube Shorts via embeddings and lets brands swipe through creator partnerships.
- **Problem / user:** Short-form creators and sponsors struggle to find each other and set up sponsored product placements. / Shopify merchants and YouTube Shorts creators
- **Domain / idea type:** retail_consumer + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** web / False / rag_or_search; recommendation; generative_media; vision; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; backend Python; BlackSheep; db Supabase; Pinecone; hosting 
- **Tech/APIs:** Cohere multimodal embeddings (ai_model, core, sponsor); Pinecone (database, core); Gemini (ai_model, core); Nano Banana image gen (ai_model, supporting); Shopify API (data_source, core); YouTube API (data_source, core); Supabase (database, supporting)
- **Sponsor APIs:** Cohere
- **Repo:** public, commits 201 (before/in/after event: 0/70/131), README detailed
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Tinder-style approval dashboard; Cohere multimodal embeddings in Pinecone, Gemini picks products, Nano Banana generates product sets, and YouTube Studio API updates descriptions.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; live_demo_url (maatchaa.co listed but not recorded; http link seen only via page script); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/maatchaa) | [GitHub](https://github.com/StockerMC/Maatchaa)

### Puppeteer  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists; Winner Warp: Best Developer Tool by Warp [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Terminal tool that probes a running app, lets an LLM tamper with variables and simulate backend data so frontends are not blocked.
- **Problem / user:** Frontend developers stall when the backend is unavailable and cannot test traffic or data realistically. / frontend developers
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** cli / False / agent_or_tool_use; llm_chat; generative_media
- **Stack:** langs Python; frontend React; backend ; db SQLite; hosting 
- **Tech/APIs:** Martian LLM router (ai_model, core, sponsor); Cohere (ai_model, supporting, sponsor); Gemini (ai_model, supporting); SQLite (database, supporting)
- **Sponsor APIs:** Martian; Cohere; Warp | fit: Entered for Warp developer-tool prize; the page does not describe Warp use, only a terminal UI dev tool.
- **Repo:** public, commits 61 (before/in/after event: 0/45/16), README solid
- **Demo/writeup:** video None, live none, screenshots 6, writeup short, impact claims False
- **Notes:** LLM-chosen runtime probes feed changed values to a Martian router that picks among text and image models by rule; terminal UI with natural-language notifications.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor; sponsor_fit_note; has_demo_video; github_url (tree/main link as listed)
- **Links:** [Devpost](https://devpost.com/software/puppeteer-7429qv) | [GitHub](https://github.com/BrianLi23/puppeteer/tree/main)

### ROSS - Remote Operated Semantic Sketching  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Turns paintings into touch experiences: a two-axis robot draws warm and cold lines on a blind user's palm with narration.
- **Problem / user:** Visual art is inaccessible to blind people; the project adds touch, temperature and sound to convey it. / blind and visually impaired art lovers
- **Domain / idea type:** accessibility + creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; generative_media; speech_or_voice
- **Stack:** langs Python; frontend ; backend Arduino; db ; hosting 
- **Tech/APIs:** Meta Segment Anything (ai_model, core); Arduino + stepper motors (hardware_part, core); Hugging Face Bob Ross XTTS voice (ai_model, supporting); Cohere (ai_model, unclear, sponsor); Gemini (ai_model, unclear)
- **Sponsor APIs:** Cohere
- **Repo:** public, commits 69 (before/in/after event: 0/69/0), README none
- **Demo/writeup:** video None, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Meta SAM segmentation to stroke graphs and curves, Arduino cartesian robot with alcohol brush and resistor-heated brush; warm/cold colour coding was not fully working so demo used one brush.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video; Cohere/Gemini depth (listed in Built With only)
- **Links:** [Devpost](https://devpost.com/software/ross-42pnvi) | [GitHub](https://github.com/FowlFarmer/HTN2025)

### S-KBD67  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Modded Nerf blasters with microcontrollers and gyros that drive a PC first-person shooter over Wi-Fi as mouse and keyboard input.
- **Problem / user:** Make FPS gameplay physical and immersive using a toy gun instead of mouse and keyboard. / gamers
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / False
- **Stack:** langs C++; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP8266 (hardware_part, core); ESP32 (hardware_part, core); MPU-6050 gyroscope (hardware_part, core); HW-504 joystick (hardware_part, supporting); UDP networking (other, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 40 (before/in/after event: 0/40/0), README none
- **Demo/writeup:** video True, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Sensor data sent as UDP packets to a Python app mapped to input events; moved from ESP8266 to ESP32 in places; team mentions working around game anticheat.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/s-kbd67) | [GitHub](https://github.com/Amelia1110/Valorant-Nerf-Gun)

### Sauron  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Investigation platform that stores device movement over time, maps trajectories, and lets police query who was near a place via a Cohere-powered chatbot.
- **Problem / user:** Low crime clearance rates; investigators lack tools to reconstruct who was where and when. / law enforcement and private investigators
- **Domain / idea type:** safety_security + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Mapbox GL JS; Tailwind CSS; shadcn/ui; backend Flask; db PostgreSQL; PostGIS; Supabase; hosting Supabase
- **Tech/APIs:** Cohere (ai_model, core, sponsor); Mapbox GL JS (maps_geo, core); PostGIS (database, core); Supabase (database, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Cohere
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims True (Cites roughly 50% violent-crime clearance rate and aims for 10x more efficient investigations; no measured results.)
- **Notes:** Team recorded live location data of hundreds of devices during the event, reportedly via reverse-engineered undocumented APIs; chatbot uses Cohere tool use against a PostGIS database.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/sauron-zvo2je) | [GitHub](https://github.com/alangrewco/sauron)

### SpeakEasy  (Hack the North 2025)

- **Prizes:** Winner Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Behavioural interview practice site that records answers and scores both verbal content and body language with AI.
- **Problem / user:** Video interview analysis tools target recruiters; applicants lack practice tools with real-time verbal and non-verbal feedback. / job seekers preparing for behavioural interviews
- **Domain / idea type:** education + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; vision
- **Stack:** langs JavaScript; Python; frontend ; backend Node.js; Express.js; FastAPI; db PostgreSQL; Firebase; hosting 
- **Tech/APIs:** Martian LLM router (gpt-4.1-nano) (ai_model, core, sponsor); AssemblyAI (ai_model, core); MediaPipe (ai_model, core); spaCy (framework, supporting); Firebase (cloud, supporting); PostgreSQL (database, supporting)
- **Sponsor APIs:** Martian
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Routes LLM calls through Martian router, transcribes with AssemblyAI, scores filler words/vocabulary with spaCy, and uses three MediaPipe models for facial, eye and hand analysis.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; team_size; has_demo_video; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/speakeasy-vdkc9n) | [GitHub](https://github.com/Dante-Capobianco/speakeasy-HTN-25)

### Stu3dio  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Collaborative 3D studio where AI director, scriptwriter and character artist agents help users build and generate an AI movie.
- **Problem / user:** Making a film with generative AI needs coordinated ideation, scripts, characters, scenes and video; the tool organises this as a regenerating node tree. / aspiring filmmakers and creators
- **Domain / idea type:** creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media; agent_or_tool_use
- **Stack:** langs TypeScript; SQL; HTML; JavaScript; CSS; frontend Next.js; React; backend Fastify; Redis; db Supabase; hosting 
- **Tech/APIs:** Supabase (database, supporting); Redis job queue (database, core); LLM / image / video providers (unnamed) (ai_model, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 45 (before/in/after event: 0/43/2), README thin
- **Demo/writeup:** video None, live none, screenshots 8, writeup short, impact claims False
- **Notes:** Project is a tree of nodes whose edits mark descendants stale; every AI action is a Redis-queued job with artifacts in blob storage; scribble-to-edit on characters and frames.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor; AI providers not named on page; has_demo_video; stack_languages
- **Links:** [Devpost](https://devpost.com/software/vibe-director) | [GitHub](https://github.com/Jeff15321/Stu3dio-HackTheNorth2025)

### Tango  (Hack the North 2025)

- **Prizes:** Hack the North 2025: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** macOS voice assistant that watches the clipboard and acts on spoken commands: captions memes, makes CSVs, rewrites text, answers coding questions.
- **Problem / user:** Copying text into an LLM and pasting answers back interrupts workflow. / knowledge workers and developers on macOS
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** desktop / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core, sponsor); Groq (ai_model, core, sponsor); OpenAI (ai_model, supporting); WebRTC VAD (other, core); Graphite (other, supporting, sponsor)
- **Sponsor APIs:** Gemini; Groq; Graphite
- **Repo:** public, commits 45 (before/in/after event: 0/45/0), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Also won the Graphite Engineering Dream Team sponsor prize per the page (not in queue prizes). Uses always-on wake-word and voice-activity detection with fast LLM providers.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/tango-q37d4z) | [GitHub](https://github.com/demanr/tango)


## Hack the North 2026

### bingbong  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Rhythm party game for up to four players that uses the Hack the North PCB badges as wireless controllers.
- **Problem / user:** Team wanted to hack the event hardware badges into a multiplayer experience. / hackathon attendees with event badges
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs TypeScript; Svelte; C; C/C++; Shell; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP32-C6 ESP-NOW bridge (hardware_part, core); Hack the North PCB badge firmware (hardware_part, core, sponsor)
- **Sponsor APIs:** 
- **Repo:** public, commits 54 (before/in/after event: 0/54/0), README thin
- **Demo/writeup:** video None, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Custom firmware on badges talks ESP-NOW to an ESP32-C6 USB bridge feeding a web game server; debugging included badge brownouts caused by the power-hungry LCD.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor; stack_* (page lists only generic tags); team_size (page shows 4 profiles); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/bing-bong-z7rsny) | [GitHub](https://github.com/sophiayduan/bingbong)

### Bricked  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Turns a sentence into a buildable 3D LEGO model using planner, builder, inspector and vision-critic agents with live streaming and steering.
- **Problem / user:** LLMs generate poor 3D structures (floating bricks); users want to redesign builds from existing bricks. / LEGO hobbyists
- **Domain / idea type:** creative_media + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; vision; generative_media
- **Stack:** langs Python; TypeScript; frontend Next.js; Three.js; LDraw; backend Python; SSE; db ; hosting 
- **Tech/APIs:** Claude Sonnet and Opus (via CLI) (ai_model, core); BrickGPT grammar (framework, core); LDraw renderer (framework, supporting); Three.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 109 (before/in/after event: 0/109/0), README none
- **Demo/writeup:** video None, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Bottom-up layered multi-agent loop with a lintable BrickGPT-style grammar, deterministic force/torque stability check and Claude vision critic; exports a link to buy parts.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/a-feuvb1) | [GitHub](https://github.com/GuyOnWifi/hack-the-north)

### CADEX  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Prompt plus reference photos in, measured and validated parametric CAD out, with STEP/STL/G-code, drawings and IKEA-style assembly guide.
- **Problem / user:** People with a clear physical idea lack CAD skills; models guess dimensions poorly from photos. / makers and non-CAD users repairing or designing physical parts
- **Domain / idea type:** creative_media + dev_tools / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; Python; frontend React; Vite; Tailwind; Three.js; backend Node.js; Hono; CadQuery; db ; hosting 
- **Tech/APIs:** OpenAI Responses API + Structured Outputs (ai_model, core, sponsor); Codex CLI as CAD agent (ai_model, core, sponsor); CadQuery (framework, core); Three.js (framework, supporting)
- **Sponsor APIs:** OpenAI; Codex
- **Repo:** public, commits 29 (before/in/after event: 0/29/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 2, writeup long, impact claims False
- **Notes:** Asks user for caliper measurements via annotated photo callouts, drives Codex CLI to write CadQuery, runs an automated geometry checker loop; demoed with a printed badge case that fit.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/cadex) | [GitHub](https://github.com/justinbaduaa/htn2026)

### Combadge  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]; Winner QNX: Create an Embedded System with QNX that Uses AI [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Wearable Star Trek combadge: chest touch sensor wired by conductive thread to a Pi 5 running QNX, giving a voice AI that sees, browses and shops.
- **Problem / user:** Wants always-available computing that does not pull attention to a screen. / general consumers wanting hands-free AI assistance
- **Domain / idea type:** ai_agents_infra + retail_consumer / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / speech_or_voice; agent_or_tool_use; vision; llm_chat
- **Stack:** langs C; Python; frontend ; backend QNX 8.0; WebSockets; GraphQL; db ; hosting 
- **Tech/APIs:** QNX 8.0 (framework, core, sponsor); OpenAI voice/reasoning models (ai_model, core, sponsor); Raspberry Pi 5 (hardware_part, core); MPR121 touch sensor (hardware_part, core); Browserbase (other, supporting); Composio (other, supporting); Shopify (data_source, supporting); Twilio (telecom, supporting); Codex (other, supporting, sponsor)
- **Sponsor APIs:** QNX; OpenAI; Codex | fit: Embedded QNX 8.0 on a Raspberry Pi 5 runs the audio, camera and network stack for the AI voice assistant.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** Shirt itself acts as circuit via conductive thread; QNX lacked Bluetooth audio drivers so team streamed PCM through custom driver; agent tools include Browserbase, Composio (Gmail, Calendar, Shopify), phone handoff.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video; github_url (queue gave org page, not a repo; null); repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/combadge) | [GitHub](https://github.com/orgs/Combadge-HTN)

### Composition  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]; Winner MLH: Best Use of Gemini API [unknown]  (tier: honorable_or_finalist)
- **Pitch:** AI filmmaking studio where you physically move a phone through a virtual scene to frame shots while an AI director generates footage.
- **Problem / user:** Creatives who can visualise an idea do not want to spend hours prompting; they want creative control. / independent filmmakers and creatives
- **Domain / idea type:** creative_media / creative_tool
- **Platforms / hardware / AI:** web; mobile_cross / False / generative_media; agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend React; Three.js; backend Node.js; db ; hosting 
- **Tech/APIs:** Gemini / Gemini Live (ai_model, core, sponsor); Three.js (framework, core); OpenAI Codex (other, supporting, sponsor); Zod (framework, token)
- **Sponsor APIs:** Gemini | fit: Gemini and Gemini Live listed as the AI components for direction and cinematic generation; page gives no detail.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Solo project built with Codex; phone motion captures camera movement inside a Three.js scene, Gemini Live used for AI direction; writeup is high-level with few technical details.
- **Team size:** 1 | **Confidence:** medium | unverified: is_sponsor; has_demo_video; platforms (phone use inferred); repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/composition) | [GitHub](https://github.com/justinlam747/Composition)

### Concerto  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Turns a concert crowd's phones into a distributed orchestra, locating each phone by camera-decoded screen patterns and assigning musical parts.
- **Problem / user:** Audience participation at concerts is limited to watching or flashlights; phones could be a spatial sound system. / concert organisers and audiences
- **Domain / idea type:** entertainment_games + creative_media / new_category
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; Python; frontend Next.js; React; backend Bun; Hono; OpenCV; PyAV; NumPy; db ; hosting 
- **Tech/APIs:** OpenCV optical localization (framework, core); Web Audio API (framework, core); Bun + Hono (framework, core); Codex (other, unclear, sponsor)
- **Sponsor APIs:** 
- **Repo:** public, commits 93 (before/in/after event: 0/82/11), README detailed
- **Demo/writeup:** video None, live none, screenshots None, writeup long, impact claims False
- **Notes:** Each phone flashes an 11-bit Hamming-coded red/blue ID decoded by an OpenCV worker; NTP-style clock sync with scheduled playback; tested with 1,500 simulated WebSocket clients; solid error handling.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; n_screenshots (no numbered gallery in page text); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/concerto-0wd9zs) | [GitHub](https://github.com/nicholasching/HackTheNorth)

### Keymaeleon  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Mechanical keyboard with an OLED in each keycap whose labels and actions change with the active app and VS Code state.
- **Problem / user:** Fixed keyboards force users to memorise shortcuts that differ per app and situation. / developers using VS Code
- **Domain / idea type:** dev_tools + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** hardware; desktop / True / llm_chat; recommendation
- **Stack:** langs C++; Python; frontend ; backend Python service; VS Code extension; db ; hosting 
- **Tech/APIs:** Arduino Nano ESP32 (hardware_part, core); OLED keycaps (hardware_part, core); VS Code extension (framework, core); OpenAI API (ai_model, supporting, sponsor); SolidWorks (other, supporting)
- **Sponsor APIs:** OpenAI
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 6, writeup long, impact claims False
- **Notes:** VS Code extension feeds git, test and debug state to a Python bridge that drives an Arduino Nano ESP32 HID keyboard; OpenAI generates profiles for unsupported apps.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; team_size (page shows 3 profiles); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/keymaeleon) | [GitHub](https://github.com/macto2024/Keymealeon)

### Orbis Engine  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]; Winner OpenAI: API Prizes [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Converts ordinary video into an explorable 3D/4D Gaussian-splat world you can walk through in a VR headset with talking characters.
- **Problem / user:** Existing footage is flat; the team wanted to step inside movies and phone videos in first person. / VR users and viewers of films, sports clips or workout videos
- **Domain / idea type:** creative_media + entertainment_games / new_category
- **Platforms / hardware / AI:** web; other / True / generative_media; vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Three.js; WebXR; Spark; backend Modal; PyTorch; db ; hosting AWS; Modal
- **Tech/APIs:** World Labs Marble (ai_model, core); OpenAI API (GPT vision, Realtime) (ai_model, core, sponsor); Pi3X camera pose (ai_model, core); LHM avatars (ai_model, core); LaMa inpainting (ai_model, supporting); Modal GPU (cloud, core); Devin (other, supporting, sponsor); Codex (other, supporting, sponsor); WebXR / Meta Quest (hardware_part, core)
- **Sponsor APIs:** OpenAI; Codex; Devin | fit: OpenAI API used in four places: scene prompt writing, output checking, scale estimation and Realtime voice chat; Codex and Devin used as dev agents.
- **Repo:** public, commits 30 (before/in/after event: 30/0/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Writeup documents failed approaches (V0 to V2) before shipping Pi3X poses, Marble room splats, LHM avatars; Devin built front end, Codex ran long GPU research jobs; trace observability admin panel.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video; github_url (page-linked repo is a third-party model repo, Depth-Anything-3; project repo not linked)
- **Links:** [Devpost](https://devpost.com/software/temp-jcyltx) | [GitHub](https://github.com/ByteDance-Seed/Depth-Anything-3)

### punching-face  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]; Winner Sentry: Best Use of Sentry [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Scans a face from video or webcam into a 3D head and lets players punch it with hand tracking and soft-tissue physics, with live multi-phone sparring.
- **Problem / user:** Joke premise: the team wanted to punch a teammate, so built a physics-based 3D scan-and-punch toy with a coaching voice layer. / hackathon demo audience / players
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision; generative_media; llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Vite; Three.js; MediaPipe; backend Python servers; Newton/Warp; LiveKit; db ; hosting 
- **Tech/APIs:** Sentry (other, core, sponsor); OpenAI (gpt-6-astra) (ai_model, supporting, sponsor); Qwen3.5 Omni (ai_model, supporting); Meshy API (ai_model, supporting); Newton / Warp physics (framework, core); COLMAP (framework, core); MediaPipe (ai_model, core); LiveKit (other, supporting)
- **Sponsor APIs:** Sentry; OpenAI | fit: Sentry used as end-to-end tracing: one trace from browser through HTTP handler and pipeline subprocess stages, gen_ai spans, session replay and profiling.
- **Repo:** public, commits 20 (before/in/after event: 0/20/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 3, writeup long, impact claims True (Quantified latency, speed-up and test-count claims (under 50 ms reaction, 309 s to 122 s pipeline, 55 JS tests).)
- **Notes:** COLMAP/MakeHuman local reconstruction with Meshy alternative, CPU tetrahedral FEM via Newton/Warp, under 50 ms hit response, LiveKit arena, heavy Sentry tracing across subprocesses; writeup also lists repo-level tests.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; team_size (page lists 4 profiles); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/punchface) | [GitHub](https://github.com/akashngb/punching-face)

### Reflex  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Robotic exoskeleton glove that Claude can drive over MCP or that learns hand motions from teleoperation via a fine-tuned VLA.
- **Problem / user:** Physical skills are taught hand-over-hand one learner at a time; the team wanted to record and replay that guidance with AI. / rehab patients (Parkinson's/stroke), learners of physical skills
- **Domain / idea type:** health_wellness + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / agent_or_tool_use; llm_chat; vision; predictive_ml; speech_or_voice
- **Stack:** langs Python; TypeScript; C; frontend Next.js; React; Three.js; Tailwind; backend FastAPI; ROS 2; rosbridge; db ; hosting Docker
- **Tech/APIs:** Anthropic API / Claude via MCP (ai_model, core); SmolVLA / LeRobot (ai_model, core); ROS 2 + Gazebo (framework, core); Feetech ST3215 servos (hardware_part, core); Intel RealSense D435i (hardware_part, supporting); MediaPipe (ai_model, supporting); Qwen Omni (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 151 (before/in/after event: 0/149/2), README detailed
- **Demo/writeup:** video None, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Claude controls servos through MCP alongside a live 3D URDF web console; SmolVLA fine-tuned on about 50 teleop demos; shared sim/real HAL; compliance tuning designed but not demoed.
- **Team size:** 4 | **Confidence:** high | unverified: is_sponsor; has_demo_video; team_size (page lists 4 profiles)
- **Links:** [Devpost](https://devpost.com/software/reflex-e0jkih) | [GitHub](https://github.com/ZechariahWang/htn-2026)

### Settlers of Solana  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]; Winner Solana: Best Use of Solana and Badge Hack [unknown]  (tier: honorable_or_finalist)
- **Pitch:** A swarm of 100+ LLM agents runs a free-market village economy settled on Solana, with on-chain auctions, lending and foreclosure.
- **Problem / user:** RL economy sims cannot explain behaviour or adapt to rule changes; the team wanted an LLM-agent economy others can analyse on-chain. / researchers and builders studying agent economies
- **Domain / idea type:** fintech_finance + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml
- **Stack:** langs Rust; JavaScript; frontend React; Vite; Three.js; backend Node.js; Anchor; Solana; db ; hosting 
- **Tech/APIs:** Solana / Anchor program (other, core, sponsor); SPL token (other, core, sponsor); Baseten model APIs (cloud, core, sponsor); OpenAI API (tool calling) (ai_model, core, sponsor); Claude / Anthropic API (ai_model, supporting); Codex (other, supporting, sponsor); Three.js (framework, supporting)
- **Sponsor APIs:** Solana; Baseten; OpenAI; Codex | fit: Core ledger, order-book auctions, minting and burning for loans run in a Solana Anchor program with a real SPL token.
- **Repo:** public, commits 74 (before/in/after event: 0/71/3), README detailed
- **Demo/writeup:** video None, live none, screenshots 10, writeup long, impact claims True (Cites cost figures (about $1.33 for six minutes at 30 agents, roughly $20 for 1,000 agents) and an x402 volume share.)
- **Notes:** Anchor program in Rust clears up to 100 orders per atomic auction, mints coins only through borrowing, supply-equals-purses invariant; 55 config dials, Three.js island, agents on Baseten, OpenAI or Claude models.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/_solanasim) | [GitHub](https://github.com/leakyhose/agent-economy)

### TakeOne  (Hack the North 2026)

- **Prizes:** Hack the North 2026: Finalists [unknown]  (tier: honorable_or_finalist)
- **Pitch:** Robotic film studio: an RC-truck cart with camera and light arms, AI director, 3D rehearsal simulator and built-in editor from idea to finished video.
- **Problem / user:** Small teams can imagine cinematic shots but lack the crew and gear to physically film them. / solo creators and small film teams
- **Domain / idea type:** creative_media + ai_agents_infra / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / agent_or_tool_use; llm_chat; vision; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React; Three.js; backend Python; WebSockets; SQLite; FFmpeg; db SQLite; hosting 
- **Tech/APIs:** OpenAI Responses API + GPT-Live (ai_model, core, sponsor); MuJoCo (framework, core); SO-101 arms / LeRobot (hardware_part, core); MediaPipe + OpenCV tracking (ai_model, core); ESP32 + CAN bus (hardware_part, core); FFmpeg (framework, supporting); Blackmagic Camera (other, supporting); Google Maps Platform (maps_geo, token)
- **Sponsor APIs:** OpenAI
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README detailed
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Two SO-101 arms on a reinforced RC truck with CAN-bus drivetrain and 42V to 12V power; MuJoCo plus Three.js rehearsal; 39 movement presets; performer tracking with PID; operator approval before motion.
- **Team size:** 3 | **Confidence:** high | unverified: is_sponsor; team_size (page lists 3 profiles); has_demo_video
- **Links:** [Devpost](https://devpost.com/software/takeone-erqv3l) | [GitHub](https://github.com/3-rt/TakeOne)
