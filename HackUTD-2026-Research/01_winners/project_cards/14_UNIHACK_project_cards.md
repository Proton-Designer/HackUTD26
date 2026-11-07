# UNIHACK: project cards (21 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## UNIHACK 2025

### Crevo  (UNIHACK 2025)

- **Prizes:** First Timers' Prize [unknown]  (tier: track_winner)
- **Pitch:** AI video editor that detects who is speaking, auto-frames the video on them and adds live captions and translation.
- **Problem / user:** Manually editing speaker framing, cuts and subtitles takes creators hours. / podcasters, creators, educators
- **Domain / idea type:** creative_media + accessibility / creative_tool
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; Figma; backend Flask; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); PyAnnote (ai_model, core); Vosk / Kaldi (ai_model, core); MoviePy (framework, supporting); Flask (framework, core)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Combines MediaPipe mouth-movement detection with PyAnnote speaker labels to cut false speaker detections; Vosk/Kaldi for real-time subtitles; exports mp4 plus .srt. Page link slot shows Figma, no live site.
- **Team size:** 5 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); tech_items.is_sponsor; prize placement n/a; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/ocuvid)

### Growth Garden  (UNIHACK 2025)

- **Prizes:** First place [1st]  (tier: overall_top3)
- **Pitch:** Habit app where an AI assistant sets personal routines and finished tasks grow items in a 3D planet garden.
- **Problem / user:** Habit tools are siloed by domain or just block bad habits; users lack a personalised plan toward their own goals. / people building personal habits
- **Domain / idea type:** mental_health + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; three.js; backend Langflow (DataStax); db ; hosting Jenkins CI/CD
- **Tech/APIs:** Langflow / DataStax (ai_model, core); Next.js (framework, core); three.js (framework, core); Jenkins (other, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup long, impact claims True (Cites a fivefold rise in mental illness among preteen girls since Snapchat as motivation.)
- **Notes:** Three.js planet garden with items snapping to the surface using hand-written vector maths, dynamic ambient audio mixing, Langflow (DataStax) backend; half the team first-timers.
- **Team size:** 6 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); ai_types; domain_secondary; tech_items.is_sponsor; event dates from Monash/DigitalReviews articles; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/growth-garden)

### Shuffl  (UNIHACK 2025)

- **Prizes:** Second place [2nd]  (tier: overall_top3)
- **Pitch:** Smart card-game table mixing in-person and online players, with Arduino NFC card scanning, voice input and an AI strategy advisor, built accessibility-first.
- **Problem / user:** Friends can't always play together, beginners feel intimidated, and visually impaired players are poorly served by card games. / card-game players incl. visually impaired
- **Domain / idea type:** accessibility + entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; speech_or_voice
- **Stack:** langs Java; TypeScript; C; frontend Next.js 14; Tailwind CSS; ShadCN; backend Spring Boot; WebSocket/STOMP; db ; hosting Azure Container Apps; Docker; GitHub Actions
- **Tech/APIs:** Azure Speech Recognition (ai_model, core); GPT-4o mini (ai_model, core); Arduino Uno (hardware_part, core); PN532 NFC module (hardware_part, core); Spring Boot (framework, core); Azure (cloud, supporting); Docker (other, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** Arduino Uno with PN532 NFC readers mapping card UIDs; Azure custom speech; Spring Boot WebSocket backend; tested screen reader support with a visually impaired friend. Monash article lists Weave as 2nd and Shuffl 3rd; Devpost badge says Second.
- **Team size:** 6 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); tech_items.is_sponsor; placement order conflicts with Monash article; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/shuffl-4rzu3c)

### Weave  (UNIHACK 2025)

- **Prizes:** Third place [3rd]  (tier: overall_top3)
- **Pitch:** Upload your wardrobe and see outfits on a mannequin or your own photo via AI virtual try-on, then save and share looks.
- **Problem / user:** Trying on clothes is a hassle, especially for people with mobility limits, and picking outfits causes decision fatigue. / people planning outfits, incl. those with mobility limits
- **Domain / idea type:** retail_consumer + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** web / False / generative_media; vision
- **Stack:** langs Go; TypeScript; frontend Next.js; Tailwind CSS; ShadCN; backend Go; db Amazon S3; hosting Coolify; Docker; AWS Lambda
- **Tech/APIs:** FashnAI virtual try-on API (ai_model, core); AWS Lambda (cloud, supporting); Amazon S3 (cloud, supporting); CloudFormation (cloud, token); Coolify (cloud, supporting); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 8, writeup long, impact claims False
- **Notes:** FashnAI handles one garment per call, so team chained calls to layer a full outfit; AWS Lambda strips backgrounds from uploads; Go backend; self-hosted on Coolify. Monash article lists it 2nd; Devpost says Third.
- **Team size:** 6 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); tech_items.is_sponsor; placement order conflicts with Monash article; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/weave-vn2xdk)


## UNIHACK 2026

### Anchor (Monash)  (UNIHACK 2026)

- **Prizes:** THE EU SHARED FUTURE PRIZE (by the European Union) [unknown]  (tier: sponsor_winner)
- **Pitch:** Natural-disaster alert app that gives personalised warnings, evacuation plans and a GPT-4o explanation of why the user is at risk.
- **Problem / user:** People under stress during bushfires and similar disasters need clear, location-specific warnings rather than raw satellite and weather data. / Australian residents in disaster-prone areas
- **Domain / idea type:** safety_security + sustainability_climate / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat
- **Stack:** langs JavaScript; frontend React Native; Expo; HTML; CSS; backend Node.js; db ; hosting Netlify
- **Tech/APIs:** OpenAI GPT-4o (ai_model, core); NASA FIRMS (data_source, core); OpenWeatherMap (data_source, core); Australian Bureau of Meteorology (data_source, supporting); Expo / React Native (framework, core); Claude (ai_model, unclear)
- **Sponsor APIs:**  | fit: EU Shared Future Prize: the page does not state how it targets the EU theme beyond disaster safety and a future plan to expand to the EU.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Built by first-time hackathon first-years; uses NASA FIRMS fire data, OpenWeatherMap and BoM; phone demo dropped for a computer-run mobile demo; page redirected to a fire-tracker slug.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_fit_note; edition_url_redirect
- **Links:** [Devpost](https://unihack2026.devpost.com/submissions/967079-anchor) | [GitHub](https://github.com/jamie-pham/EmergencyAlert--anchor)

### Antrum MK 1  (UNIHACK 2026)

- **Prizes:** FIRST PLACE [1st]  (tier: overall_top3)
- **Pitch:** Pair of leg-worn ESP32 devices that track cave partners by dead reckoning, show partner direction by LED and guide the way back; paths shown on a web dashboard.
- **Problem / user:** Cavers and miners get lost or separated in low-visibility, low-comms underground environments. / cave explorers and miners
- **Domain / idea type:** safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs C; C++; TypeScript; frontend Angular; backend Hono; db MongoDB; hosting Google Cloud VM; Vercel
- **Tech/APIs:** ESP32 (hardware_part, core); ICM20948 IMU (hardware_part, core); XC4508 2.4GHz radio (hardware_part, core); PlatformIO (other, supporting); Angular (framework, core); Hono (framework, core); MongoDB (database, supporting); Google Cloud (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Custom PCB and 3D-printed enclosures; IMU dead reckoning with ZUPT; 2.4 GHz RF24-style radio master-slave exchange; Angular dashboard and Hono API; team drove for 3D prints at 3am.
- **Team size:** 4 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); tech_items.is_sponsor; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/antrum-mk-1)

### BeeSafe (Monash)  (UNIHACK 2026)

- **Prizes:** SOCIAL IMPACT PRIZE, 4th [unknown]  (tier: track_winner)
- **Pitch:** Smartphone driving-safety platform combining on-device computer vision, automatic emergency detection and blockchain-backed records.
- **Problem / user:** Road crashes affect thousands of Australians daily and a phone could provide driver monitoring and emergency response. / Australian drivers
- **Domain / idea type:** safety_security + mobility_transport / new_category
- **Platforms / hardware / AI:** web; mobile_ios / False / vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; frontend TanStack Start; React; Tailwind CSS; shadcn/ui; Framer Motion; backend oRPC; Better Auth; Prisma; db PostgreSQL; Supabase; hosting Vercel; AWS; Docker
- **Tech/APIs:** YOLOv8 + ONNX Runtime Web (ai_model, core); MediaPipe (ai_model, core); AWS Polly (ai_model, supporting); Anthropic SDK (ai_model, unclear); Google Generative AI (ai_model, unclear); Base Sepolia / viem / MetaMask (other, supporting); LocationIQ + OpenStreetMap (maps_geo, supporting)
- **Sponsor APIs:**  | fit: Won the Social Impact Prize, listed as 4th in the prize name; the project targets road-safety and emergency response.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 25, writeup long, impact claims False
- **Notes:** YOLOv8 and MediaPipe run in-browser through ONNX Runtime/WebGPU; AWS Polly voice, Base Sepolia and MetaMask via viem listed; team hit trouble getting an iOS app to judges.
- **Team size:** 6 | **Confidence:** high | unverified: ui_polish; github_url; placement; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/beesafe-njd4hi)

### Cowdar  (UNIHACK 2026)

- **Prizes:** THIRD PLACE [3rd]  (tier: overall_top3)
- **Pitch:** iPhone app estimating a cow's weight from a LiDAR scan plus photo, using a custom pose model and a livestock weight formula.
- **Problem / user:** Livestock weighing tools are expensive, subscription-based or poor; small farmers need a free option on phones they own. / small-scale cattle farmers
- **Domain / idea type:** other / data_or_analytics
- **Platforms / hardware / AI:** mobile_ios / False / vision; predictive_ml
- **Stack:** langs Swift; Python; frontend Swift; ARKit; backend FastAPI; db ; hosting 
- **Tech/APIs:** YOLOv8 pose (ai_model, core); ARKit LiDAR (hardware_part, core); Roboflow (data_source, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Custom YOLOv8m-pose trained on 1042 labelled cow images; LiDAR points projected to 2D to get body distances; Schaeffer-style formula; open source; team notes dark Angus hides were hard.
- **Team size:** 5 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); domain_primary (agriculture not in list); team_size (one private member counted); demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/cowdar)

### Echo (UNSW/USYD)  (UNIHACK 2026)

- **Prizes:** BEST DESIGN [unknown]  (tier: track_winner)
- **Pitch:** Anonymous app where you type an unspoken thought and learn how many others have felt similarly, using embeddings while never storing raw text.
- **Problem / user:** People feel isolated by thoughts they are ashamed of and believe they are alone in having them. / people carrying private emotional thoughts
- **Domain / idea type:** mental_health + social_community / new_category
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind CSS; backend FastAPI; db PostgreSQL; Elasticsearch; hosting Vercel; Docker
- **Tech/APIs:** Ollama (Qwen small model) (ai_model, core); sentence-transformers (ai_model, core); Elasticsearch (database, core); NanoGPT API (ai_model, supporting); FastAPI (framework, core)
- **Sponsor APIs:**  | fit: Won Best Design per the page award list; no sponsor technology identified.
- **Repo:** public, commits 148 (before/in/after event: 0/148/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 25, writeup long, impact claims False
- **Notes:** Three-stage AI pipeline enforcing that raw thought text never persists; local Ollama Qwen small model, sentence-transformers, Elasticsearch matching; a Google Drive file is also linked.
- **Team size:** 6 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/echo-107u6c) | [GitHub](https://github.com/petmav/echo-unihack-2026)

### Guardia  (UNIHACK 2026)

- **Prizes:** SOCIAL IMPACT PRIZE, 3rd [3rd]  (tier: track_winner)
- **Pitch:** Safety-first walking navigation for women at night: scores routes against crime incidents, voice-alerts near hotspots, adds AI companion call and SOS.
- **Problem / user:** Navigation apps show the fastest route, not the safest, leaving women walking alone at night anxious. / women walking home alone at night (Melbourne)
- **Domain / idea type:** safety_security + mobility_transport / social_good
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Mapbox; backend FastAPI; db Elasticsearch; hosting AWS App Runner; Vercel
- **Tech/APIs:** Elasticsearch (database, core, sponsor); Elastic Web Crawler (data_source, core, sponsor); HeyGen (ai_model, supporting); Mapbox (maps_geo, core); FastAPI (framework, core); AWS App Runner (cloud, supporting)
- **Sponsor APIs:** Elastic
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Elastic web crawler gathered over 10,000 incident records into Elasticsearch; FastAPI route scorer on AWS App Runner; HeyGen AI companion; Mapbox map.
- **Team size:** 6 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); ai_types; prize not shown as badge on Devpost page; confirmed via UNIHACK Medium winners list; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/guardia-9ghij1)

### HABITMON  (UNIHACK 2026)

- **Prizes:** BEST DESIGN, 2nd [2nd]  (tier: track_winner)
- **Pitch:** Skill-learning app where an AI fairy gives small tasks, and each completion yields a gacha monster that roams a field and quizzes you.
- **Problem / user:** New learners get overwhelmed, fall into tutorial hell and lose motivation; productivity apps feel like chores. / people learning a new skill
- **Domain / idea type:** education + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; backend Flask; db Elasticsearch; hosting 
- **Tech/APIs:** Elasticsearch (database, core, sponsor); OpenAI ChatGPT API (ai_model, core); React (framework, core); Flask (framework, core)
- **Sponsor APIs:** Elastic
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Pixel-art monsters as GIFs, CSS gacha reel, localStorage game state; Elasticsearch retrieves roadmaps and ChatGPT API writes quiz questions; most members first-time hackers. No Winner badge on page.
- **Team size:** 5 | **Confidence:** high | unverified: prize not shown as badge on Devpost page; confirmed via UNIHACK Medium winners list; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/habit-habitat)

### Hooked (UTS)  (UNIHACK 2026)

- **Prizes:** BEST USE OF ELASTIC TECHNOLOGY (by Elastic) [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified Australian fishing app with a Gemini-powered FishDex for species ID and Elastic dashboards for fisheries tracking invasive and endangered fish.
- **Problem / user:** Invasive fish harm Australian waterways, beginner anglers face a steep learning curve, and local actionable catch data is scarce. / anglers and fisheries agencies
- **Domain / idea type:** sustainability_climate + entertainment_games / social_good
- **Platforms / hardware / AI:** mobile_cross / False / vision; llm_chat; generative_media
- **Stack:** langs C#; HTML; CSS; JavaScript; frontend .NET MAUI; backend C#; db Supabase; Elasticsearch; hosting 
- **Tech/APIs:** Elasticsearch / Elastic dashboards (database, core, sponsor); Google Gemini (ai_model, core); Leonardo AI (ai_model, supporting); Supabase (database, core); .NET MAUI (framework, core); Mapbox (maps_geo, supporting)
- **Sponsor APIs:** Elastic | fit: Uses Elasticsearch for geospatial map queries and FishDex search and to aggregate catch data into dashboards for fisheries and environmental agencies.
- **Repo:** public, commits 124 (before/in/after event: 0/124/0), README solid
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Built in .NET MAUI; Elasticsearch handles geospatial and full-text search and feeds agency dashboards; Leonardo AI generates badges and assets; Supabase backend; insights and Mapbox endpoints.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://unihack2026.devpost.com/submissions/969724-hooked) | [GitHub](https://github.com/Valin-K/Hooked/)

### MeshMap (UNSW)  (UNIHACK 2026)

- **Prizes:** SOCIAL IMPACT PRIZE [unknown]  (tier: track_winner)
- **Pitch:** Bluetooth Low Energy mesh-network phone app for offline messaging, map-based event sharing and SOS alerts during internet blackouts.
- **Problem / user:** Authorities or outages can cut internet access, leaving people unable to reach help, locate family or avoid danger. / civilians in internet-shutdown crises
- **Domain / idea type:** telecom_networking + safety_security / social_good
- **Platforms / hardware / AI:** mobile_ios; mobile_android; web / False / llm_chat
- **Stack:** langs Swift; Kotlin; TypeScript; frontend SwiftUI; Next.js; backend Next.js; db Supabase; GRDB; hosting Vercel
- **Tech/APIs:** CoreBluetooth BLE mesh (other, core); X25519 / HKDF / AES-GCM (other, core); Claude API (ai_model, supporting); Twilio (telecom, supporting); Supabase (database, supporting); MapKit (maps_geo, core); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 73 (before/in/after event: 0/71/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 14, writeup long, impact claims True (Cites Iran's near-total internet shutdown and BLE range and Tehran density estimates to argue mesh viability.)
- **Notes:** Native iOS (Swift, CoreBluetooth) and Android (Kotlin) apps with up-to-7-hop relaying, E2E-encrypted DMs, chunked image transfer, web-of-trust alert scoring and a Claude-written news site.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier
- **Links:** [Devpost](https://devpost.com/software/meshnet) | [GitHub](https://github.com/RuoHan-Chen/MeshMap)

### Peersuade  (UNIHACK 2026)

- **Prizes:** BEST DESIGN, 3rd [3rd]; MOST FUN IDEA [unknown]  (tier: track_winner)
- **Pitch:** Jackbox-style 1v1 voice debate game on political topics, judged by five AI voters with personalities, including an OBJECTION button.
- **Problem / user:** Young voters are politically disengaged and traditional debates feel boring and jargon-heavy. / young Australians and friends playing party games
- **Domain / idea type:** entertainment_games + civic_legal / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js 15; React 19; Tailwind v4; backend Express.js; Socket.io; db ; hosting Vercel
- **Tech/APIs:** Gemini Flash (ai_model, core); Groq Whisper (ai_model, core); Agora RTC (other, core); Socket.io (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 8, writeup long, impact claims True (Cites Gen Z disengagement stats: 55% globally and about 47% of Australian Gen Z voting mainly to avoid a fine.)
- **Notes:** Server-authoritative Socket.io game state; Agora RTC voice with parallel-chunk Groq Whisper transcription; Gemini Flash voter personas; reconnect state sync.
- **Team size:** 6 | **Confidence:** high | unverified: demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/peersuade)

### Safe Trace (UQ/Monash)  (UNIHACK 2026)

- **Prizes:** AI SOLUTIONS PRIZE (by Quantium) [unknown]  (tier: sponsor_winner)
- **Pitch:** Raspberry Pi camera stream analyzed by a custom-trained vision model to check PPE use at work sites and compute a safety score.
- **Problem / user:** Many workplace accidents are avoidable if correct protective equipment use were monitored automatically. / workplace safety managers
- **Domain / idea type:** safety_security + productivity_workplace / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision
- **Stack:** langs Python; frontend ; backend FastAPI; Flask; Node.js; db ; hosting 
- **Tech/APIs:** Ultralytics YOLO (ai_model, core); Raspberry Pi + camera (hardware_part, core); Claude (ai_model, unclear); Gemini (ai_model, unclear)
- **Sponsor APIs:**  | fit: Won the AI Solutions Prize (by Quantium) with a custom-trained PPE-detection model; the page does not mention Quantium tools.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Team trained its own YOLO model for PPE detection, streaming from a Pi camera over WiFi to a home server; first time training a model; Claude and Gemini also in tags.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://unihack2026.devpost.com/submissions/969368-safe-trace)

### Sentinel AI  (UNIHACK 2026)

- **Prizes:** SECOND PLACE [2nd]  (tier: overall_top3)
- **Pitch:** Web app that turns a DJI drone into a natural-language agent via an Android bridge, with live telemetry, vision models and footage analysis.
- **Problem / user:** Flying drones takes skill or paid operators; users want to describe tasks in plain language instead. / landowners, industry and government drone users
- **Domain / idea type:** ai_agents_infra + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_android; hardware / True / agent_or_tool_use; vision; speech_or_voice; rag_or_search
- **Stack:** langs Kotlin; TypeScript; frontend Next.js; React; backend Express.js; WebSockets; db Elastic; hosting Vercel; RunPod
- **Tech/APIs:** OpenAI API (ai_model, core); DJI Mobile SDK (hardware_part, core); YOLO (ai_model, supporting); Elastic (database, supporting, sponsor); FFmpeg (other, supporting); RunPod (cloud, token); Arduino (hardware_part, supporting)
- **Sponsor APIs:** Elastic
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Kotlin app on DJI MSDK streams RTMP video via FFmpeg; OpenAI agent loop with GPS/telemetry tools; Arduino telemetry bridge; Elastic stores video-analysis timestamps; simulated Android test environment.
- **Team size:** 4 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); ai_types; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/sentinel-ai-rzp29l)

### SlothMotion  (UNIHACK 2026)

- **Prizes:** SOCIAL IMPACT PRIZE, 2nd [2nd]  (tier: track_winner)
- **Pitch:** Webcam exercise coach for people 65+ that compares live pose to a reference routine and gives real-time feedback, with large high-contrast UI.
- **Problem / user:** Most Australians over 65 miss activity guidelines; mobility limits and gym discomfort block exercise. / older adults in Australia
- **Domain / idea type:** health_wellness + accessibility / social_good
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs TypeScript; frontend React; Vite; backend Supabase; db Supabase; hosting 
- **Tech/APIs:** MediaPipe Pose (ai_model, core); React (framework, core); Supabase (database, supporting)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 5, writeup long, impact claims True (States 57% of Australians aged 65+ do not meet physical activity guidelines.)
- **Notes:** MediaPipe Pose landmarks normalised and compared to a recorded reference with tolerance thresholds; routines personalised to ailments; no team member had prior computer vision experience.
- **Team size:** 6 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); prize not shown as badge on Devpost page; confirmed via UNIHACK Medium winners list; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/slothmotion)

### StepFlow  (UNIHACK 2026)

- **Prizes:** FIRST TIMERS PRIZE (by Atlassian) [unknown]  (tier: track_winner)
- **Pitch:** Gamified study scheduler: tasks as shooting targets or a spin wheel, RAG-generated quizzes, and Q-learning to time revision.
- **Problem / user:** Students struggle with task indecision, self-pressure and knowing when to revise. / university students
- **Domain / idea type:** education + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind; backend FastAPI; LangChain; db ChromaDB; SQLite; Firebase; hosting 
- **Tech/APIs:** Ollama / Llama 3 (ai_model, core); ChromaDB (database, core); LangChain (framework, supporting); FastAPI (framework, core); Firebase (cloud, supporting); Cursor (other, token)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Ebbinghaus forgetting-curve scheduler tuned by Q-learning on simulated schedules; local Llama 3 via Ollama for quizzes; end-of-day reflection step.
- **Team size:** 5 | **Confidence:** high | unverified: github_url (page lists a repo but URL not captured); placement n/a; Firebase role; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/stepflow)

### ToiletGO (Monash/UniMelb)  (UNIHACK 2026)

- **Prizes:** MOST ENTERTAINING PITCH [unknown]  (tier: track_winner)
- **Pitch:** Public toilet finder with community reviews, Google image analysis to estimate cleanliness of unreviewed toilets, and a Subway Surfers-style toilet game.
- **Problem / user:** People often face unpleasant public toilets and lack reliable information to choose a good one nearby. / general public
- **Domain / idea type:** retail_consumer + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision
- **Stack:** langs TypeScript; Python; frontend React; Vite; backend Express; db localStorage; hosting 
- **Tech/APIs:** Google Gemini / image analysis (ai_model, supporting); Google Maps (maps_geo, supporting); National Public Toilet Map data (data_source, core); React / Vite (framework, core); Express (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 13 (before/in/after event: 0/13/0), README thin
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Won the most entertaining pitch; pivoted after a tennis-analysis idea failed; uses Toilet Map Australia data (personal-use only), localStorage reviews and an Express game leaderboard.
- **Team size:** 6 | **Confidence:** high | unverified: ui_polish; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/orion-15qdnf) | [GitHub](https://github.com/shiimee/UNIHACK-2026-TOILETGO-)

### Tracksync (UNSW)  (UNIHACK 2026)

- **Prizes:** MOST CREATIVE IDEA [unknown]  (tier: track_winner)
- **Pitch:** Git-style version control for music co-production that tracks audio project changes across collaborators.
- **Problem / user:** Remote music co-production relies on file swapping, with no history or merge workflow like software teams have. / music producers collaborating remotely
- **Domain / idea type:** creative_media + dev_tools / creative_tool
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; wavesurfer.js; backend FastAPI; GitPython; db PostgreSQL; Supabase; hosting 
- **Tech/APIs:** GitPython (framework, core); FFmpeg (other, core); LMMS (other, supporting); wavesurfer.js (framework, supporting); Supabase (database, supporting)
- **Sponsor APIs:**  | fit: Won Most Creative Idea per the page award list; no sponsor technology involved.
- **Repo:** public, commits 25 (before/in/after event: 0/18/7), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup medium, impact claims False
- **Notes:** Applies git concepts to non-text audio project files; uses GitPython, FFmpeg, wavesurfer.js and the open-source LMMS (C++) in the stack; team wrote a detailed PRD first.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/tracksync) | [GitHub](https://github.com/andrew-c105/UNIHACK-2026-Hackathon)

### UniAid (Monash)  (UNIHACK 2026)

- **Prizes:** PEOPLE'S CHOICE [unknown]  (tier: track_winner)
- **Pitch:** Mentor-matching platform where students and parents describe needs in free text and an embedding plus learning-to-rank model recommends mentors.
- **Problem / user:** New university students and their parents struggle to find reliable, consolidated guidance on visas, housing, culture and career. / new university students and parents
- **Domain / idea type:** education + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / recommendation; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; Vite; backend FastAPI; db PostgreSQL; hosting Netlify; EC2/GCP VM
- **Tech/APIs:** sentence-transformers (ai_model, core); Learning-to-rank (ai_model, core); FastAPI (framework, core); PostgreSQL (database, core); React / Vite (framework, core); Elasticsearch (database, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 176 (before/in/after event: 0/176/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** Sentence-transformer embeddings combined with learning-to-rank and explicit requirement checks (visa, language); CPU-only ML on a single cloud VM; People's Choice winner.
- **Team size:** 5 | **Confidence:** high | unverified: ui_polish; n_screenshots; team_size
- **Links:** [Devpost](https://devpost.com/software/uniaid-tvojlk) | [GitHub](https://github.com/bhattrahul525/UniAid)
