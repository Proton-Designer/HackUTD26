# LA Hacks: project cards (40 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## LA Hacks 2025

### AERIS  (LA Hacks 2025)

- **Prizes:** Best of Groq [unknown]  (tier: sponsor_winner)
- **Pitch:** Drone-based disaster response: YOLOv8 spots victims and hazards in DJI video, Groq Llama triages them, and agents find hospitals and place Twilio calls.
- **Problem / user:** Disasters knock out phone service and rescuers search blindly, wasting time. / search-and-rescue teams and first responders
- **Domain / idea type:** safety_security + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind CSS; shadcn/ui; Leaflet; backend FastAPI; Docker; NGINX RTMP; FFmpeg; db Supabase; hosting 
- **Tech/APIs:** Groq (Llama) (ai_model, core, sponsor); YOLOv8 (Ultralytics) (ai_model, core); Dain agents (framework, supporting); Twilio (telecom, supporting); Supabase (database, supporting); DJI drone (hardware_part, core)
- **Sponsor APIs:** Groq | fit: Used Groq-hosted Llama in the computer-vision pipeline to triage victims detected in drone frames.
- **Repo:** public, commits 49 (before/in/after event: 0/0/49), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup medium, impact claims True (States that over 60% of disaster victims lose phone service.)
- **Notes:** RTMP/FFmpeg ingest of a DJI drone feed into a FastAPI pipeline running custom YOLOv8 detection, Groq Llama triage and Supabase logging; Dain agents coordinate hospital lookup and Twilio calls.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/aeris-ej7d9k) | [GitHub](https://github.com/Jeffuz/AERIS)

### AI Escape, UncBlox, Bloom.AI, Kindness Maxxing  (LA Hacks 2025)

- **Prizes:** ROBLOX Civility Challenge: Building A Better Digital World [unknown]  (tier: sponsor_winner)
- **Pitch:** Roblox escape-room game where players solve puzzles and quizzes on AI literacy, data privacy and algorithmic bias to unlock keys.
- **Problem / user:** People need accessible education on responsible AI use, misinformation and data safety. / Roblox players of all ages
- **Domain / idea type:** education + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** other / False / False
- **Stack:** langs Lua; frontend Roblox Studio; backend ; db ; hosting Roblox
- **Tech/APIs:** Roblox Studio (framework, core, sponsor); Lua (framework, core, sponsor)
- **Sponsor APIs:** Roblox Studio | fit: Targeted the Roblox civility challenge with an educational Roblox escape game on AI literacy and cybersecurity.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup medium, impact claims False
- **Notes:** Queue entry bundles four Roblox-challenge winners (AI Escape, UncBlox, Bloom AI, Kindness Maxxing); only AI Escape's page was read, built in Roblox Studio/Lua by a two-person team new to both.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; bundled_projects_not_read; github_url
- **Links:** [Devpost](https://devpost.com/software/ai-escape)

### Alto  (LA Hacks 2025)

- **Prizes:** Overall: 1st Place [1st]; Track: AI Agents League (Fetch.ai) [unknown]  (tier: overall_top3)
- **Pitch:** Multi-agent pipeline that ingests mobile bug reports, analyzes repo code with Gemini, drafts Maestro replication scripts and posts results to Slack.
- **Problem / user:** Mobile developers lose much time debugging; existing monitoring and AI coding tools lack an integrated agent workflow from report to replication. / mobile app developers
- **Domain / idea type:** dev_tools + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend React Native; backend Flask; uAgents; db ; hosting Vercel
- **Tech/APIs:** Fetch.ai uAgents/Agentverse (framework, core, sponsor); ASI-1 Mini (ai_model, supporting, sponsor); Google Gemini 2.5 Pro (ai_model, core); Instabug (data_source, supporting); gitingest (other, core); Maestro (other, supporting); Slack webhooks (other, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; Agentverse; ASI-1 Mini | fit: Built the whole workflow as cooperating uAgents registered with Agentverse, with ASI-1 Mini driving the extraction step.
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** Wraps local gitingest inside a uAgent and bridges a Flask gateway to the async agent loop; Maestro script generation is labeled experimental.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; n_screenshots; team_size; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/alto) | [GitHub](https://github.com/NLNHSR/AgentAlto)

### Bandaid Maps  (LA Hacks 2025)

- **Prizes:** Winner Melissa Data Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Location-based tool that scores a user's emergency healthcare readiness from nearby trauma centers, urgent cares and pharmacies, and generates a Gemini action plan.
- **Problem / user:** People lack a quick read on how prepared their location is for medical emergencies. / general public in emergencies
- **Domain / idea type:** health_wellness + mobility_transport / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs JavaScript; CSS; Python; HTML; frontend React; Leaflet.js; backend FastAPI; db MongoDB; hosting 
- **Tech/APIs:** Melissa data APIs (data_source, core, sponsor); Gemini (ai_model, core); Leaflet.js (maps_geo, supporting); MongoDB (database, supporting); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** Melissa | fit: Targeted the Melissa Data Challenge by using Melissa location data to find nearby healthcare services and compute a readiness score.
- **Repo:** public, commits 8 (before/in/after event: 0/0/8), README solid
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Health Readiness Score from 0 to 100 using Melissa location data; optional symptom-aware recommendations and 24/7 emergency filter; README text mentions Streamlit while tags list React and FastAPI.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; stack_languages; platforms
- **Links:** [Devpost](https://devpost.com/software/bandaid-maps) | [GitHub](https://github.com/GovindKurapati/bandaid-maps)

### Cena Can See  (LA Hacks 2025)

- **Prizes:** Google Gemini: Chase the Future! [unknown]  (tier: sponsor_winner)
- **Pitch:** A Nao humanoid robot uses Gemini vision, spatial reasoning and function calling to plan and carry out tasks like cleaning a spill without task-specific training.
- **Problem / user:** Training robots for everyday tasks through reinforcement or imitation learning is expensive and compute-heavy. / robotics developers and household-assistance users
- **Domain / idea type:** ai_agents_infra + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; C++; JavaScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Google Gemini API (vision, function calling) (ai_model, core, sponsor); Nao humanoid robot (hardware_part, core); Custom controller and inverse kinematics (framework, core)
- **Sponsor APIs:** Google Gemini API | fit: Targeted the Gemini challenge by using Gemini multimodal input and function calling as the planner that drives a Nao robot's perception and actions.
- **Repo:** public, commits 2 (before/in/after event: 0/0/2), README thin
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Runs on an aging Nao robot needing Python 2.7; firmware was bricked and reflashed; inverse kinematics maps camera pixels to joint angles; Gemini function calls trigger low-level motions.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/cena-can-see) | [GitHub](https://github.com/mahanthesh0r/Cena_Humanoid_Robot)

### Delphi  (LA Hacks 2025)

- **Prizes:** Track: Heart of The Matter [unknown]  (tier: track_winner)
- **Pitch:** Voice-driven web browsing for blind users via four cooperating agents: voice, orchestrator, vision and browser action.
- **Problem / user:** Blind users navigate sites through screen readers and shortcuts, which is slow and frustrating. / visually impaired web users
- **Domain / idea type:** accessibility + ai_agents_infra / social_good
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; JavaScript; CSS; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents/Agentverse (framework, core, sponsor); Gemini 2.0 Flash (incl. Live) (ai_model, core); Browser-use (framework, core); Text-to-speech (other, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; Agentverse
- **Repo:** public, commits 33 (before/in/after event: 0/0/33), README solid
- **Demo/writeup:** video False, live not_checked, screenshots 2, writeup medium, impact claims False
- **Notes:** Four named agents on Fetch.ai Agentverse; vision agent analyzes screenshots while a browser-use agent executes clicks and keystrokes.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; team_size; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/delphi-lxes1j) | [GitHub](https://github.com/brennenho/delphi)

### Devin & Kevin  (LA Hacks 2025)

- **Prizes:** Track: hack2school [unknown]; DAIN Challenge: AI Agent Excellence & Innovation Awards [unknown]  (tier: track_winner)
- **Pitch:** Multi-agent product manager that scopes a project technically, assigns people, runs standups and allocates budgets.
- **Problem / user:** Product managers spend effort on scoping, staffing, budgets and standups that could be automated. / product managers and engineering teams
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** other / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Dain (framework, core, sponsor)
- **Sponsor APIs:** Dain | fit: Built the multi-agent system on the Dain platform.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Solo build on TypeScript and Dain; also creates and solves GitHub issues via agents. Page lists no repo link.
- **Team size:** 1 | **Confidence:** high | unverified: event_start; event_end; platforms
- **Links:** [Devpost](https://devpost.com/software/kevin-4m6rbf)

### Embers  (LA Hacks 2025)

- **Prizes:** Track: Cold Hard Cache [unknown]; Google Gemini: Chase the Future! [unknown]  (tier: track_winner)
- **Pitch:** Upload a home walkthrough video; YOLO detects valuables, Gemini estimates replacement values, and a voice assistant answers queries, for insurance documentation before wildfires.
- **Problem / user:** People rarely inventory belongings before disasters, leading to insurance disputes and underpayment after wildfires. / homeowners and renters in disaster-prone areas
- **Domain / idea type:** fintech_finance + safety_security / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind; backend Python; REST API; db Supabase; hosting 
- **Tech/APIs:** Ultralytics YOLO v11 (ai_model, core); Google Gemini 2.0/2.5 (ai_model, core, sponsor); Supabase (database, core); Whisper (ai_model, supporting)
- **Sponsor APIs:** Google Gemini | fit: Used Gemini multimodal reasoning to value each detected item from images and context.
- **Repo:** public, commits 67 (before/in/after event: 0/0/67), README detailed
- **Demo/writeup:** video False, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Uses multi-frame deduplication with non-max suppression across video frames; stores items and image paths in normalized Supabase tables.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; team_size; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/insurefire) | [GitHub](https://github.com/twistyyb/insurefire)

### Fynd  (LA Hacks 2025)

- **Prizes:** Track: AI Agents League (Fetch.ai) [unknown]  (tier: track_winner)
- **Pitch:** Swipe-style shopping app where agents crawl Shopify, Amazon and Etsy, learn likes, recommend products, with a Snap Spectacles AR preview.
- **Problem / user:** Shoppers face decision fatigue from endless scrolling across e-commerce sites. / online shoppers
- **Domain / idea type:** retail_consumer + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web; other / True / agent_or_tool_use; recommendation
- **Stack:** langs Python; JavaScript; TypeScript; frontend React; Next.js; backend ; db ; hosting 
- **Tech/APIs:** Fetch.ai (framework, core, sponsor); Dain (framework, supporting, sponsor); Butterfly (other, supporting); Snap Spectacles (hardware_part, supporting); Gemini (ai_model, unclear); TensorFlow (framework, unclear); Shopify/Amazon/Etsy connectors (data_source, supporting)
- **Sponsor APIs:** Fetch.ai; Dain; Snap Spectacles | fit: Used Fetch.ai agents to crawl e-commerce data and drive recommendation logic.
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Dating-app swipe UI across web, mobile and AR; Spectacles gesture swiping fell back to buttons. Linked repo is an event org page, not a project repo.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; team_size; n_screenshots; tech_items.is_sponsor; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/fynd-myi2jc) | [GitHub](https://github.com/orgs/LAHacks-2025/repositories)

### Ghostface Cookah  (LA Hacks 2025)

- **Prizes:** Winner Snap Inc. Challenge: Dream it. Build it. [unknown]  (tier: sponsor_winner)
- **Pitch:** Snapchat Spectacles AR cooking assistant that overlays a recipe video, timestamped steps and a timer that follow the cook's head movements.
- **Problem / user:** Cooks with messy hands cannot easily touch a phone or flip through a recipe while following a video. / home cooks
- **Domain / idea type:** food_nutrition + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** other / True / speech_or_voice; llm_chat
- **Stack:** langs TypeScript; frontend Lens Studio; backend yt-dlp; db ; hosting 
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); OpenAI Whisper via Groq (ai_model, core); Gemini (ai_model, supporting); OpenAI (ai_model, supporting); yt-dlp (other, supporting)
- **Sponsor APIs:** Snap Spectacles; Lens Studio | fit: Targeted the Snap challenge by building the AR experience in Lens Studio for Snapchat Spectacles with a head-following video player, steps and timer.
- **Repo:** public, commits 11 (before/in/after event: 0/0/11), README none
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Recipe steps and timestamps are generated from a cooking video by downloading it with yt-dlp and transcribing with Whisper through Groq; AR layer built in Lens Studio for Spectacles.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/ghostface-cookah) | [GitHub](https://github.com/joycechen721/lahacks25-spectacles)

### GMax  (LA Hacks 2025)

- **Prizes:** MSI Lucky's Hackening [unknown]  (tier: sponsor_winner)
- **Pitch:** Gmail Chrome extension and FastAPI backend that classify incoming mail with Gemini, draft replies in the user's own style and ask for approval by SMS.
- **Problem / user:** Professionals lose hours daily to email, and routine replies could be handled by AI with human oversight. / professionals with heavy email load
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** browser_extension; web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React; Chrome extension; backend FastAPI; WebSockets; Pydantic; db Supabase; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Gmail API + Cloud Pub/Sub (cloud, core); Supabase (database, supporting); Textbelt SMS (telecom, supporting); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Won the MSI Lucky's Hackening prize; the page lists no MSI hardware or product and does not say what the prize required.
- **Repo:** public, commits 92 (before/in/after event: 0/0/92), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims True (Cites professionals spending 28% of the workday (2.6 hours daily) on email.)
- **Notes:** Gmail push notifications via Cloud Pub/Sub feed a Gemini pipeline for spam, phishing and reply decisions; builds a style persona from sent mail; SMS (Textbelt) confirmation before sending.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; is_sponsor; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/gmax) | [GitHub](https://github.com/aroy23/GMax)

### Leadify; Brew  (LA Hacks 2025)

- **Prizes:** Linkd Challenge: Best Use of Linkd People Search [unknown]  (tier: sponsor_winner)
- **Pitch:** Leadify: Gemini-driven pipeline that turns event details into ranked sponsor and speaker leads from Linkd people search, with personalized outreach drafts; Brew is a cold-outreach app.
- **Problem / user:** Organizers and students spend long hours finding the right people on LinkedIn and writing cold outreach by hand. / small event organizers and internship seekers
- **Domain / idea type:** productivity_workplace + social_community / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; React; backend Python asyncio; Node.js; db ; hosting Fetch.ai Agentverse
- **Tech/APIs:** Linkd People Search API (data_source, core, sponsor); Google Gemini (ai_model, core); Fetch.ai (framework, supporting); Stagehand (Brew) (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** Linkd API | fit: Targeted the Linkd challenge by using the Linkd people-search API to discover real LinkedIn profiles as sponsor/speaker leads, then ranking them with Gemini.
- **Repo:** public, commits 23 (before/in/after event: 0/0/23), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Queue combines two Linkd-challenge winners; Leadify was read in full (solo, approval-first agent flow on Fetch.ai), Brew only for tags and links (Gemini, Linkd, Stagehand, Next.js). Github link is Brew's.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; brew_details; team_size
- **Links:** [Devpost](https://devpost.com/software/momentum-94wfd6) | [GitHub](https://github.com/EvanAd7/la-hacks)

### LingoBuddy  (LA Hacks 2025)

- **Prizes:** Winner Google Gemini: Chase the Future! [unknown]  (tier: sponsor_winner)
- **Pitch:** Gemini-powered language-learning platform that generates custom lessons, exercises and grammar explanations from chat and gives pronunciation help on vocabulary cards.
- **Problem / user:** Busy learners struggle to find quick, speech- and pronunciation-focused language tools that balance immersion with vocabulary. / busy language learners
- **Domain / idea type:** education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; generative_media
- **Stack:** langs Python; CSS; frontend Next.js; backend FastAPI; Uvicorn; db Supabase; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core, sponsor); Supabase (database, supporting); Next.js (framework, core); FastAPI (framework, core)
- **Sponsor APIs:** Google Gemini | fit: Targeted the Google Gemini prize by using Gemini as the backend model for lesson generation, grammar explanations and pronunciation help.
- **Repo:** public, commits 112 (before/in/after event: 0/0/112), README solid
- **Demo/writeup:** video True, live none, screenshots 58, writeup medium, impact claims False
- **Notes:** Lessons are generated from chat input in English or the target language; uses Gemini multimodal plus speech-to-text and text-to-speech for pronunciation; 58 gallery images.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; ai_types
- **Links:** [Devpost](https://devpost.com/software/lingobuddy-fkj4g0) | [GitHub](https://github.com/sebomaniac/lingobuddy)

### Lumos  (LA Hacks 2025)

- **Prizes:** Overall: 2nd Place [2nd]; Track: AI Agents League (Fetch.ai) [unknown]  (tier: overall_top3)
- **Pitch:** Alzheimer's memory aid: Snap Spectacles AR names familiar faces while agents and a caregiver mobile app handle reminders, safe zones and alerts.
- **Problem / user:** Alzheimer's patients lose recall of people and routines, and caregivers need non-invasive ways to assist and monitor them. / Alzheimer's patients and their caregivers
- **Domain / idea type:** health_wellness + accessibility / new_category
- **Platforms / hardware / AI:** mobile_cross; other / True / vision; agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs JavaScript; TypeScript; Python; frontend React Native; Expo; React; backend Node.js; Express; Flask; db MongoDB Atlas; hosting 
- **Tech/APIs:** Snap Spectacles (hardware_part, core); Fetch.ai (framework, core, sponsor); Dain (framework, supporting, sponsor); Gemini 2.5 (ai_model, supporting); MongoDB Atlas (database, supporting); Melissa API (data_source, supporting); Butterfly (other, unclear)
- **Sponsor APIs:** Fetch.ai; Dain; Melissa; MongoDB Atlas; Snap Spectacles | fit: Used Fetch.ai agents for recognition, reminders, safety monitoring and journaling prompts.
- **Repo:** public, commits 46 (before/in/after event: 0/0/46), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Runs face recognition overlays on Snapchat Spectacles; combines agents from Fetch.ai and Dain with geofenced safe zones and Melissa API hospital lookup.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; n_screenshots; team_size; is_sponsor_flags
- **Links:** [Devpost](https://devpost.com/software/lumos-f8h0mn) | [GitHub](https://github.com/pb2323/Lumos)

### Magic Mirror  (LA Hacks 2025)

- **Prizes:** Track: Clean Code [unknown]  (tier: track_winner)
- **Pitch:** Voice-controlled virtual clothing try-on studio using segmentation and an open-source try-on model to show users wearing garments.
- **Problem / user:** Online clothing shoppers struggle with fit and look, driving costly returns and emissions. / online clothing shoppers
- **Domain / idea type:** retail_consumer + sustainability_climate / creative_tool
- **Platforms / hardware / AI:** web / False / generative_media; vision; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React; Next.js; Tailwind; backend Flask; PyTorch; db ; hosting H100 GPUs
- **Tech/APIs:** FitDiT (ai_model, core); FastSAM (ai_model, core); YOLO (ai_model, core); LiveKit (other, core); OpenAI image generation (ai_model, supporting); PyTorch (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 73 (before/in/after event: 0/0/73), README solid
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims True (Cites online apparel share, 30-40% return rates and roughly 40 billion dollars of yearly returns, plus extra emissions.)
- **Notes:** Custom pipeline of FastSAM and YOLO segmentation feeding FitDiT, run on rented H100 GPUs, with a LiveKit voice agent controlling the UI.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; team_size
- **Links:** [Devpost](https://devpost.com/software/magic-mirror-muya4w) | [GitHub](https://github.com/KevinWu098/magic-mirror)

### OpenSesame.Work  (LA Hacks 2025)

- **Prizes:** Overall: 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Job-search automation: upload a resume, set preferences, and browser agents auto-apply and send AI-personalized LinkedIn connection requests to recruiters.
- **Problem / user:** Job hunting is repetitive: filling applications and cold-messaging recruiters consumes time that could go to interviews. / job seekers
- **Domain / idea type:** productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; JavaScript; TypeScript; frontend React; HTML; CSS; backend Flask; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); Browser-Use (framework, core); Flask (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 22 (before/in/after event: 0/0/22), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Runs multiple Gemini-driven Browser-Use sessions in parallel with retry/fallback logic to submit real applications and LinkedIn requests.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; team_size; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/opensesame-work) | [GitHub](https://github.com/rahut-tae/LAHACKS2025)

### Pulse  (LA Hacks 2025)

- **Prizes:** Snap Inc. Challenge: Dream it. Build it. [unknown]  (tier: sponsor_winner)
- **Pitch:** Snap Spectacles AR app that guides bystanders through CPR with hand-placement overlays and rhythm cues, and maps nearby AEDs with voice control.
- **Problem / user:** Few Americans are current on CPR training and many freeze during cardiac arrest, so step-by-step guidance in view could help. / bystanders in cardiac emergencies
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** other; hardware / True / vision; speech_or_voice
- **Stack:** langs TypeScript; frontend Lens Studio; backend ; db ; hosting 
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); Spectacles Interaction Kit (framework, supporting, sponsor); VoiceML (ai_model, supporting, sponsor); Pose detection (ai_model, supporting); MSI (hardware_part, token)
- **Sponsor APIs:** Snap Spectacles; Lens Studio; VoiceML | fit: Targeted Snap's challenge by building an AR CPR coach and AED finder for Spectacles in Lens Studio.
- **Repo:** public, commits 1 (before/in/after event: 0/0/1), README none
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims True (States only 20% of Americans are current with CPR training.)
- **Notes:** Built in Lens Studio for Spectacles with pose detection, Spectacles Interaction Kit and VoiceML; AED locations precise only inside Pauley Pavilion; the writeup left a placeholder note unfilled.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/pulse-n06ij9) | [GitHub](https://github.com/jackyydai/LAHack2025-Pulse)

### SnapDrobe  (LA Hacks 2025)

- **Prizes:** Winner Snap Inc. Challenge: Dream it. Build it. [unknown]  (tier: sponsor_winner)
- **Pitch:** Snap Spectacles app where a voice command captures a clothing item, AI describes it for a digital wardrobe, and the system helps build outfits.
- **Problem / user:** People who struggle with fashion find it hard to remember and match clothing they like. / everyday shoppers wanting outfit help
- **Domain / idea type:** retail_consumer + creative_media / new_category
- **Platforms / hardware / AI:** other / True / vision; llm_chat; recommendation; speech_or_voice
- **Stack:** langs TypeScript; Python; frontend Lens Studio; Spectacles Interaction Kit; backend Python; Render; db Amazon DynamoDB; hosting Render
- **Tech/APIs:** Snap Spectacles / Lens Studio (hardware_part, core, sponsor); Gemini API (ai_model, core, sponsor); Fetch.ai (other, supporting, sponsor); Amazon DynamoDB (database, supporting); OpenWeather (data_source, supporting); Render (cloud, supporting)
- **Sponsor APIs:** Snap Spectacles; Lens Studio; Gemini; Fetch.ai | fit: Targeted the Snap challenge by building a voice-driven wardrobe capture experience in Lens Studio on Spectacles using the Interaction Kit.
- **Repo:** public, commits 20 (before/in/after event: 0/0/20), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Stores AI-generated text descriptions instead of images; built on Lens Studio and the Spectacles Interaction Kit by a team new to Spectacles; Fetch.ai, Gemini, DynamoDB and OpenWeather listed in stack.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; platforms; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/snapdrobe) | [GitHub](https://github.com/venkatnikhilm/SnapDrobeAPI)

### stackwise  (LA Hacks 2025)

- **Prizes:** Winner Warp Challenge: Best Developer Tool [unknown]  (tier: sponsor_winner)
- **Pitch:** Describe a project in plain English and get a Gemini-generated tech stack as an editable graph, plus generated project scaffolds.
- **Problem / user:** Choosing a tech stack is overwhelming for junior developers and time-consuming even for seniors. / software developers
- **Domain / idea type:** dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Vite; backend Flask; db ; hosting Vercel; Railway
- **Tech/APIs:** Google Gemini (ai_model, core, sponsor); Next.js (framework, core); Flask (framework, supporting); Vercel (cloud, supporting); Railway (cloud, supporting)
- **Sponsor APIs:** Google Gemini | fit: Targeted Warp's Best Developer Tool prize as a stack-planning tool; the page does not show use of Warp's own product.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 28, writeup medium, impact claims False
- **Notes:** Stack recommendations appear as a graph where users edit technologies and connections, with a chat interface and scaffold generation; no GitHub link on the page; 28 gallery images.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/stackwise)

### StartNOW  (LA Hacks 2025)

- **Prizes:** Track: AI Agents League (Fetch.ai) [unknown]  (tier: track_winner)
- **Pitch:** Pitch a startup idea to a boardroom of personality-driven AI agents that debate it, accept your input, and output a pitch deck, report and mood board.
- **Problem / user:** Founders find startup building overwhelming and miss angles a diverse team would raise. / aspiring founders
- **Domain / idea type:** productivity_workplace + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs Python; JavaScript; frontend React; backend Flask; uAgents; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents (framework, core, sponsor); ASI:One Mini (ai_model, core, sponsor); Gemini (ai_model, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; ASI:One Mini | fit: ASI:One Mini powered each personality agent built on uAgents.
- **Repo:** public, commits 19 (before/in/after event: 0/0/19), README solid
- **Demo/writeup:** video False, live none, screenshots 6, writeup medium, impact claims False
- **Notes:** Agents with role archetypes (intern, CTO, PM) argue with each other via event-driven messages; Gemini summarizes the session into a report.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; team_size; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/startnow) | [GitHub](https://github.com/c00lme/startup-sim)


## LA Hacks 2026

### Accent  (LA Hacks 2026)

- **Prizes:** Winner Track: Light The Way; Winner Figma Make Challenge [unknown]; Track: Light The Way [unknown]  (tier: track_winner)
- **Pitch:** macOS menu-bar assistant that hears a spoken request, detects on-screen UI elements, and highlights what to click with spoken directions.
- **Problem / user:** Older adults and non-technical users struggle to find the right controls in complex apps such as video calls. / older adults and non-technical computer users
- **Domain / idea type:** accessibility + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** desktop / False / llm_chat; vision; speech_or_voice
- **Stack:** langs Swift; Python; frontend AppKit; Gradio; backend Node; LangChain; pydantic; db ; hosting local
- **Tech/APIs:** Gemini 3.1 (ai_model, core); ElevenLabs STT/TTS (ai_model, core, sponsor); RF-DETR UI element detector (Hugging Face) (ai_model, core); Figma Make (other, supporting, sponsor); LangChain (framework, supporting); Ollama Gemma (ai_model, token, sponsor); Windsurf (other, token, sponsor)
- **Sponsor APIs:** ElevenLabs; Figma Make; Windsurf | fit: Used Figma Make to generate the animated mascot shown while the assistant is thinking.
- **Repo:** public, commits 16 (before/in/after event: 0/11/5), README detailed
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Cropsheet trick: each detected UI element cropped into a labeled grid so the LLM maps labels correctly; Swift app plus Python backend; local Gemma tried but dropped for speed.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/accent-cdw2qi) | [GitHub](https://github.com/RyloRiz/accent)

### Autopsy  (LA Hacks 2026)

- **Prizes:** Winner 3rd Overall; Winner Cognition Company Challenge [3rd]; 3rd Overall [3rd]  (tier: overall_top3)
- **Pitch:** Failure-memory layer for coding agents that records rejected runs, builds a failure graph, and injects warnings into future prompts.
- **Problem / user:** Coding agents repeat the same mistakes each session because nothing learned from rejected runs carries over. / developers using AI coding agents
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** cli; web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind; Three.js; backend FastAPI; SQLAlchemy; db Postgres; pgvector; hosting Docker; Cloudflare
- **Tech/APIs:** opencode (framework, core); Gemma (ai_model, supporting, sponsor); Gemini embedding-001 (ai_model, core); Postgres + pgvector (database, core); Devin (other, token, sponsor); GoDaddy Registry domain (other, token, sponsor)
- **Sponsor APIs:** Gemma; GoDaddy Registry | fit: Built a tool that makes AI coding agents learn from past failures, matching the Cognition challenge brief on agent tooling.
- **Repo:** public, commits 157 (before/in/after event: 0/157/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Plugin for opencode with one-line curl install; graph stored as two Postgres tables with pgvector; preflight lookup has 800ms fail-open timeout; 3D graph dashboard.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/autopsy-zq5d84) | [GitHub](https://github.com/balebbae/Autopsy)

### beehyv  (LA Hacks 2026)

- **Prizes:** Winner Organizers' Choice [unknown]  (tier: track_winner)
- **Pitch:** Maps about 100k arXiv papers into a 2D semantic graph, finds empty regions as research gaps, and uses an agent swarm to explore them.
- **Problem / user:** AI research is expanding quickly with hallucinations, jargon and non-replicable code, making it hard to see where real gaps lie. / AI researchers
- **Domain / idea type:** education + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / True / agent_or_tool_use; llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend ; backend PyTorch; FastMCP; Ollama; db SQLite; hosting ASUS GX10
- **Tech/APIs:** OpenRouter Nemotron 3 Super (ai_model, core); ASUS GX10 / Gemma (hardware_part, core, sponsor); Ollama (framework, supporting); FastMCP (framework, supporting); UMAP / MiniBatchKMeans (framework, core); SQLite (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup long, impact claims True (States the sample covers about 100k arXiv papers.)
- **Notes:** Clusters precomputed embeddings with MiniBatchKMeans, flattens with UMAP, then finds voids via Voronoi diagrams and alpha shapes; agents use OpenRouter Nemotron and Gemma on an ASUS GX10; full writeup in an external Google Doc.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; platforms; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/beehyv) | [GitHub](https://github.com/justanotherinternetguy/Beehyv)

### Bridge  (LA Hacks 2026)

- **Prizes:** Best Hardware Hack [unknown]  (tier: track_winner)
- **Pitch:** Affordable refreshable braille device that transcribes images or audio and raises pins with a 3D-printed rotating cylinder and stepper motors.
- **Problem / user:** Deafblind students depend on scarce human interpreters and braille displays costing thousands of dollars that cannot read handwritten notes or lectures. / deafblind students
- **Domain / idea type:** accessibility + education / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / speech_or_voice; vision; llm_chat
- **Stack:** langs Python; JavaScript; frontend HTML; CSS; JavaScript; backend FastAPI; Uvicorn; db ; hosting 
- **Tech/APIs:** ESP32 + stepper motors (hardware_part, core); Whisper (ai_model, core); Claude API (ai_model, core); 3D-printed braille pin mechanism (hardware_part, core); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims True (Cites about 160 million deafblind people worldwide and braille displays costing $3,000-$15,000.)
- **Notes:** Pin display driven by a CAD-designed rotating cylinder with bumps; computer runs Whisper transcription and Claude text extraction via FastAPI, then sends braille patterns to an ESP32; improvised around part shortages.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/bridge-4euwyt) | [GitHub](https://github.com/lozlrc/Bridge/)

### codebreaker  (LA Hacks 2026)

- **Prizes:** Winner 1st Overall [1st]; Winner Cognition Company Challenge [unknown]  (tier: overall_top3)
- **Pitch:** Security platform with a CVE benchmark curated by Devin, a specialized agent harness, and an autonomous loop that reproduces vulnerabilities and opens fix PRs.
- **Problem / user:** Open-source supply-chain attacks are rising and existing tools and benchmarks are not built for agents or modern ecosystems. / software and security teams
- **Domain / idea type:** safety_security + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend React 19; Vite; Tailwind; shadcn; backend Cloudflare Workers; Hono; Vercel AI SDK; db Cloudflare D1; Drizzle; hosting Cloudflare; Modal
- **Tech/APIs:** Devin (ai_model, core, sponsor); Cloudflare Workers/AI Gateway (cloud, core); Modal sandboxes (cloud, core); GitHub Advisory Database (data_source, core); Vercel AI SDK (framework, supporting); GitHub PRs (other, core); DeepWiki (other, supporting)
- **Sponsor APIs:** Devin | fit: Used Devin sessions to curate the benchmark, build the system, and generate reproduction, tests and patch PRs.
- **Repo:** public, commits 300 (before/in/after event: 0/1286/1), README thin
- **Demo/writeup:** video False, live not_checked, screenshots 6, writeup long, impact claims True (Claims over 60% of US businesses hit by supply-chain attacks and reports benchmark scores across models over 280 million tokens.)
- **Notes:** Reports ECVE-Bench results (GPT-5 about 24%, Kimi K2.6 35% to 47% in harness); Devin curated the dataset, built much of the stack, and drives patching.
- **Team size:** 2 | **Confidence:** high | unverified: team_size; n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/codebreaker-la) | [GitHub](https://github.com/KevinWu098/codebreaker)

### Conjure  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Agentverse multi-agent pipeline that turns a text prompt into a walkable 3D interior rendered in the browser.
- **Problem / user:** Most people can describe a space they want but cannot model it in 3D. / people wanting quick 3D spaces (designers, creators)
- **Domain / idea type:** creative_media + ai_agents_infra / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs Python; TypeScript; frontend Next.js; React; React Three Fiber; Three.js; Tailwind; backend FastAPI; pydantic; WebSockets; db ; hosting Agentverse
- **Tech/APIs:** Fetch.ai Agentverse (other, core, sponsor); Google Gemini API (ai_model, core); Three.js / React Three Fiber (framework, core)
- **Sponsor APIs:** Fetch.ai Agentverse | fit: Described as a staged pipeline of about 29 Agentverse agents coordinating a shared world spec.
- **Repo:** public, commits 116 (before/in/after event: 0/116/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims False
- **Notes:** All agents read and update one shared WorldSpec; WebSocket streams agent progress live; geometric validators; procedural assets replaced unreliable external furniture catalog links; repo name is WorldEdit.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; event_start; event_end; live_demo_url
- **Links:** [Devpost](https://devpost.com/software/conjure-m960jz) | [GitHub](https://github.com/pauligwe/WorldEdit)

### Dots  (LA Hacks 2026)

- **Prizes:** Winner Track: Catalyst For Care; Winner Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Turns a floorplan into a tactile-style map plus a QR link that lets users ask text or voice questions about the layout.
- **Problem / user:** Blind and low-vision visitors get little usable orientation from visual floor plans and signage in large venues. / blind and low-vision visitors, venue operators
- **Domain / idea type:** accessibility + civic_legal / social_good
- **Platforms / hardware / AI:** web; mobile_ios / False / llm_chat; vision; speech_or_voice; generative_media
- **Stack:** langs Python; Swift; frontend ; backend FastAPI; Uvicorn; db SQLite; hosting Vercel
- **Tech/APIs:** Gemini (ai_model, core); Fetch.ai ASI:One (ai_model, core, sponsor); ElevenLabs Conversational AI (ai_model, core, sponsor); SQLite (database, supporting)
- **Sponsor APIs:** Fetch.ai ASI:One; ElevenLabs | fit: Used ASI:One for text Q&A over per-map context, listed against the Agentverse track; ElevenLabs powers the voice agent.
- **Repo:** public, commits 27 (before/in/after event: 0/27/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Per-map isolated Q&A by map_id; short-lived server-minted ElevenLabs tokens for voice; produces ADA-style compliance summary; Swift appears in stack list.
- **Team size:** 4 | **Confidence:** medium | unverified: team_size; n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/dots-y5r21j) | [GitHub](https://github.com/aryanmudgal-tech/dots)

### Drip  (LA Hacks 2026)

- **Prizes:** Winner Track: Sustain The Spark [unknown]  (tier: track_winner)
- **Pitch:** Raspberry Pi edge node whose processor waste heat drives a homemade membrane distillation chamber that desalinates seawater, plus a one-click agent deployer.
- **Problem / user:** Data center cooling consumes fresh water in drought regions; waste heat from AI compute could instead produce clean water. / data center operators and edge AI hosts
- **Domain / idea type:** sustainability_climate + energy_utilities / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; agent_or_tool_use
- **Stack:** langs Go; Python; TypeScript; JavaScript; frontend Next.js; React; backend Go; Docker; ngrok; Tailscale; db ; hosting Vercel; Raspberry Pi 5; ASUS Ascent GX10
- **Tech/APIs:** Raspberry Pi 5 (hardware_part, core); ASUS Ascent GX10 (hardware_part, core, sponsor); Ollama Gemma 4 E4B (ai_model, core, sponsor); Tailscale (other, supporting); ngrok (other, supporting); Cloudinary (other, supporting, sponsor); Peltier module and membrane chamber (hardware_part, core); Arista challenge (networking) (other, unclear, sponsor)
- **Sponsor APIs:** ASUS Ascent GX10; Gemma; Cloudinary
- **Repo:** public, commits 102 (before/in/after event: 0/102/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims False (States the distillation prototype was tested and produced water; no quantified yield or market numbers.)
- **Notes:** Physical build: liquid-cooled Pi 5, thermos hot chamber, Peltier cold side, polycarbonate membrane chamber; Go server runs per-user Ollama Gemma instances; map of US data centers; saltwater from Santa Monica.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/drip-6ao9m2) | [GitHub](https://github.com/Lewin-B/lahacks2026)

### Jarvis  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Proactive Chrome extension that briefs you on Gmail, detects meeting requests, writes calendar events, and recommends restaurants via an Agentverse agent.
- **Problem / user:** AI assistants are reactive chat tabs; users want one that already knows their context and acts ahead of time. / busy individuals with heavy email and calendar load
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** browser_extension / False / llm_chat; agent_or_tool_use; recommendation
- **Stack:** langs JavaScript; Python; HTML; CSS; frontend Chrome MV3 extension; Shadow DOM; backend FastAPI; Agentverse; db chrome.storage.local; hosting Agentverse
- **Tech/APIs:** Fetch.ai ASI:One (asi1-mini) (ai_model, core, sponsor); Agentverse (other, core, sponsor); Gmail API (data_source, core); Google Calendar API (data_source, core); Google OAuth (auth, supporting)
- **Sponsor APIs:** Fetch.ai ASI:One; Agentverse | fit: Inference runs through ASI:One and a restaurant recommendation agent is deployed on Agentverse.
- **Repo:** public, commits 16 (before/in/after event: 0/16/0), README none
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Shadow DOM overlay on every page; regex fallback alongside LLM for meeting detection; state kept in chrome.storage for MV3 service worker restarts; restaurant agent on Agentverse.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/jarvis-eifsyq) | [GitHub](https://github.com/saigudisa6/jarvis/tree/restaurant-agent)

### MultiEval  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Platform for tracing, A/B comparing and autonomously evolving multi-agent orchestration harnesses, built on Inspect AI and OpenHands.
- **Problem / user:** Existing observability tools treat traces as linear, so teams cannot see or measure coordination failures between sibling agents. / teams building multi-agent coding systems
- **Domain / idea type:** ai_agents_infra + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend Inspect AI; OpenHands; MCP; db ; hosting 
- **Tech/APIs:** Inspect AI (framework, core); OpenHands (framework, core); Claude Opus (ai_model, core); Gemini 3.1 Pro (ai_model, supporting); Fetch.ai Agentverse / ASI:One (other, supporting, sponsor); Devin (other, token, sponsor); Windsurf (other, token, sponsor); MCP (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; ASI:One; Devin; Windsurf | fit: Evaluation tooling for agent harnesses, with one harness deploying Agentverse economic-simulation agents over ASI:One.
- **Repo:** public, commits 3 (before/in/after event: 0/1/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims True (Reports pass rate rising from 0.79 to 0.87 with the structured-delegation harness on its own benchmark.)
- **Notes:** Graph and Gantt trace viewers; Wilson-bound A/B compare; budget-capped meta-agent that evolved a Fetch.ai harness which then simulated a 50-agent economy; five custom harnesses.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/multival) | [GitHub](https://github.com/AlfredSjoqvist/multieval)

### NeighborFridge  (LA Hacks 2026)

- **Prizes:** Best UI/UX [unknown]; Figma Make Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Web marketplace where students scan grocery receipts, get expiry reminders and list surplus food for neighbors to claim through shared pickup lockers.
- **Problem / user:** Groceries get forgotten and thrown out, wasting money and resources while neighbors could use them. / students and local households
- **Domain / idea type:** food_nutrition + sustainability_climate / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; backend Django; Django REST Framework; SimpleJWT; db SQLite; hosting AWS
- **Tech/APIs:** Figma Make (other, core, sponsor); Tesseract / pytesseract OCR (other, core); Veryfi (other, token); Ollama Gemma 2 (ai_model, supporting); OpenStreetMap Nominatim (maps_geo, supporting); Django REST Framework (framework, core); AWS (cloud, supporting)
- **Sponsor APIs:** Figma Make | fit: Targeted the Figma Make challenge by prototyping and generating the React UI with Figma Make plus ChatGPT Codex.
- **Repo:** public, commits 160 (before/in/after event: 0/160/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims False
- **Notes:** Receipt OCR using Tesseract with optional Veryfi; Gemini free-tier limits led to a local Gemma 2 on Ollama; UI prototyped with Figma Make and ChatGPT Codex; locker pickup simulated in an MVP.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/neighborfridge) | [GitHub](https://www.github.com/sinaghadimi9081/LaHacks2026)

### NeuralLens  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Multi-agent Agentverse system that predicts gaze and brain response to a marketing image, scores it, and auto-optimizes image and copy.
- **Problem / user:** Small businesses cannot afford neuromarketing studies that large brands use to tune their visuals. / small business owners and marketers
- **Domain / idea type:** retail_consumer + creative_media / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / vision; agent_or_tool_use; generative_media; predictive_ml; llm_chat
- **Stack:** langs Python; frontend React; backend Fetch.ai uAgents; Playwright; db ; hosting Google Colab A100; RunPod; Replicate; ngrok
- **Tech/APIs:** Meta TRIBE v2 (ai_model, core); DeepGaze IIE (ai_model, core); Fetch.ai Agentverse / uAgents (other, core, sponsor); ASI:One (ai_model, core, sponsor); Cloudinary generative AI (other, core, sponsor); Stripe / Fetch Payment Protocol (payments, supporting); Playwright (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; ASI:One; Cloudinary | fit: Built a six-agent pipeline registered on Agentverse and invoked through ASI:One chat.
- **Repo:** public, commits 21 (before/in/after event: 0/20/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 2, writeup long, impact claims True (Cites small-business statistics, studies on purchase prediction and menu revenue lift, and a planned $99/month SaaS price.)
- **Notes:** Applies Meta TRIBE v2 brain-response model with DeepGaze saliency; six-agent pipeline on Agentverse with FET/Stripe payment agent; GPU inference on Colab/RunPod; served via ASI:One chat without custom frontend.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/neurolens-2qgdm8) | [GitHub](https://github.com/anirudhmazumder/NeuralLens)

### Nimbus  (LA Hacks 2026)

- **Prizes:** Winner Arista Networks: Connect the Dots Challenge [unknown]; Winner High Quality Sponsormaxxing [unknown]  (tier: sponsor_winner)
- **Pitch:** Open-source VM provisioning platform that gives an EC2-like experience on self-owned Proxmox hardware, with static IPs and instant HTTPS subdomains via a reverse-tunnel gateway.
- **Problem / user:** A student club paid about $3,600 a year to AWS for infrastructure that could run on roughly $300 of owned hardware. / student clubs, startups and hobbyists with spare hardware
- **Domain / idea type:** dev_tools + telecom_networking / dev_tool
- **Platforms / hardware / AI:** web; cli / True / False
- **Stack:** langs Go; Bash; TypeScript; frontend React; Vite; backend Go; Proxmox API; Caddy; db SQLite; hosting Proxmox cluster
- **Tech/APIs:** Proxmox (cloud, core); Go (framework, core); React (framework, supporting); Caddy (framework, supporting); Gopher tunnel gateway (other, supporting); ASUS GX10 (hardware_part, supporting, sponsor)
- **Sponsor APIs:**  | fit: Entered Arista Networks' Connect the Dots Challenge with a platform that provisions VMs on owned hardware and exposes them through routed networking and tunnels; the page does not name Arista products.
- **Repo:** public, commits 433 (before/in/after event: 0/172/261), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 67, writeup long, impact claims True (Claims a 12x cost premium ($3,600 vs $300) and 30-second two-click VM provisioning.)
- **Notes:** Single Go binary with embedded React SPA and one SQLite file; 9-step provisioning over the Proxmox API; demoed on 5 repurposed laptops, a router and a GX10; integrates the team's Gopher tunnel gateway and Caddy TLS; 67 gallery images.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note; platforms
- **Links:** [Devpost](https://devpost.com/software/nimbus-q025jc) | [GitHub](https://github.com/smalex-z/nimbus)

### Northstar  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Hiking safety app that detects falls, runs on-device voice triage, reads vitals with the phone camera, and phones an emergency contact.
- **Problem / user:** Injured hikers on trails with no mobile signal struggle to get help or relay their condition. / hikers
- **Domain / idea type:** safety_security + health_wellness / new_category
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; speech_or_voice; agent_or_tool_use; predictive_ml
- **Stack:** langs JavaScript; Swift; frontend React Native; Expo; backend Fetch.ai Agentverse; Twilio; db ; hosting 
- **Tech/APIs:** ZETIC Melange (Qwen 3.5-4B, YAMNet) (ai_model, core, sponsor); Fetch.ai Agentverse agents (other, core, sponsor); ElevenLabs voice (ai_model, core, sponsor); Twilio (telecom, core); Expo / React Native (framework, core)
- **Sponsor APIs:** Zetic Melange; Fetch.ai Agentverse; ElevenLabs | fit: Ran triage and sound-classification models fully on-device through Melange, and used an Agentverse agent swarm to look up care information.
- **Repo:** public, commits 109 (before/in/after event: 0/109/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (States that over half of hiking injuries are slips and falls; no sourcing given.)
- **Notes:** Local Qwen 3.5-4B and YAMNet via Zetic on phone; camera-and-flash PPG for heart rate and blood pressure; Twilio plus ElevenLabs outbound call; satellite connectivity claimed.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; event_start; event_end; live_demo_url
- **Links:** [Devpost](https://devpost.com/software/northstar-7lcg45) | [GitHub](https://github.com/continuitylabs/lahacks26)

### Polaris  (LA Hacks 2026)

- **Prizes:** Winner Best Social Impact Hack [unknown]  (tier: track_winner)
- **Pitch:** Hospital paging system where agents classify urgency, pick the right on-call clinician using EHR context, and send an accept/decline page with a short SBAR brief.
- **Problem / user:** Hospital paging is slow and guesswork, with nurses unsure who is on call, available or already overpaged. / nurses, clinicians and hospital operators
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; speech_or_voice; rag_or_search
- **Stack:** langs Python; TypeScript; JavaScript; Bash; frontend Next.js; React; Tailwind; shadcn/ui; backend FastAPI; Flask; Socket.IO; uAgents; nginx; Gunicorn; db TinyDB; hosting AWS; systemd
- **Tech/APIs:** Fetch.ai uAgents (framework, core, sponsor); ASI:One (ai_model, core, sponsor); AWS (cloud, supporting); FastAPI (framework, core); Flask / Socket.IO (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; ASI:One
- **Repo:** public, commits 59 (before/in/after event: 0/59/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Fetch.ai uAgents pipeline with ASI:One reasoning, P1-P4 priority classification, Socket.IO live queue, voice input and SBAR brief under 100 words; deployed on AWS behind nginx.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; tech_items.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/polaris-mh7rd8) | [GitHub](https://github.com/angelinawwu/lahacks26)

### Pols 15  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Twelve-agent Fetch.ai system that simulates voter reactions to a policy across seven demographics, then drafts and posts to social media after a $1 payment.
- **Problem / user:** Local candidates cannot afford polling to test positions before announcing them. / first-time and local political candidates
- **Domain / idea type:** civic_legal + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; generative_media
- **Stack:** langs Python; JavaScript; frontend Vite; React; Tailwind; Mapbox; D3; backend Fetch.ai uAgents; FastAPI; httpx; db ; hosting Agentverse
- **Tech/APIs:** Fetch.ai Agentverse / uAgents (other, core, sponsor); ASI:1 (ai_model, core, sponsor); Stripe payment protocol (payments, core); Composio (other, core); Mapbox (maps_geo, supporting); D3 (framework, supporting)
- **Sponsor APIs:** Fetch.ai Agentverse; ASI:One | fit: Registered twelve chat-enabled agents on Agentverse, with ASI:1 as the only LLM and the orchestrator reachable through ASI:One chat.
- **Repo:** public, commits 1 (before/in/after event: 0/1/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims True (Cites $50k+ per polling cycle for Senate races and 60-120 second end-to-end run time.)
- **Notes:** Solo entry; inter-agent calls moved from Agentverse mailbox to direct HTTP for speed; Stripe-gated Composio posting to real accounts; comparison agent checks predicted vs real replies; 3D Mapbox globe.
- **Team size:** 1 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/pols-15) | [GitHub](https://github.com/PranAD-dev/pols-15)

### Residue  (LA Hacks 2026)

- **Prizes:** Track: Agentverse - Search & Discovery of Agents [unknown]  (tier: track_winner)
- **Pitch:** Study app that measures room sound and screen activity to learn a personal focus profile, then plays generated soundscapes and matches study partners.
- **Problem / user:** Study tools only time sessions and do not reveal which acoustic environment helps each student focus. / college students
- **Domain / idea type:** education + productivity_workplace / new_category
- **Platforms / hardware / AI:** web; mobile_ios / False / agent_or_tool_use; llm_chat; generative_media; recommendation; predictive_ml
- **Stack:** langs TypeScript; Python; Swift; frontend Next.js; React; Tailwind; backend Next.js API routes; Fetch.ai uAgents; db MongoDB Atlas; hosting 
- **Tech/APIs:** Fetch.ai uAgents / ASI1-Mini (ai_model, core, sponsor); ElevenLabs sound generation (ai_model, supporting, sponsor); MongoDB Atlas Vector Search (database, supporting, sponsor); ZETIC Melange (on-device Qwen) (ai_model, supporting, sponsor); Web Audio API (framework, core); Screen Capture API (framework, core)
- **Sponsor APIs:** Fetch.ai ASI:One; ElevenLabs; MongoDB Atlas; Zetic Melange | fit: Orchestrator and matching agents built with Fetch.ai uAgents plus ASI1-Mini calls for perception and intervention, with a fallback when agents are down.
- **Repo:** public, commits 124 (before/in/after event: 0/124/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Browser Web Audio analysis stays local; screen-diff productivity score; iOS companion with on-device Qwen via Zetic; MongoDB vector matching of acoustic profiles; team pivoted mid-event.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/residue) | [GitHub](https://github.com/MaanPatel2005/Residue)

### RIIS  (LA Hacks 2026)

- **Prizes:** Winner 2nd Overall [2nd]; Winner Fetch.ai: Best Use of ASI:One [unknown]  (tier: overall_top3)
- **Pitch:** Rover enters collapsed buildings, detects survivors with pose estimation, triggers agent triage and multilingual voice contact, and builds a VR Gaussian-splat scene.
- **Problem / user:** Survivors of structural collapse die before care reaches them; responders cannot safely enter immediately. / first responders and incident commanders
- **Domain / idea type:** safety_security + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware; other / True / vision; agent_or_tool_use; llm_chat; speech_or_voice; generative_media
- **Stack:** langs Python; JavaScript; frontend Vanilla HTML/CSS/JS; Unity; backend FastAPI; db ; hosting 
- **Tech/APIs:** Fetch.ai uAgents/Agentverse (framework, core, sponsor); ASI-1 Mini (ai_model, core, sponsor); ElevenLabs Multilingual v2 (ai_model, supporting, sponsor); YOLOv8-pose (ai_model, core); MASt3R (ai_model, supporting); InstantSplat (ai_model, supporting); PiCar-X / Raspberry Pi 5 (hardware_part, core); Meta Quest 2 (hardware_part, supporting)
- **Sponsor APIs:** Fetch.ai uAgents; ASI-1 Mini; ElevenLabs | fit: Four uAgents (Scout, Triage, Comms, Mapping) with ASI-1 Mini generating SBAR triage reports.
- **Repo:** public, commits 17 (before/in/after event: 0/17/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Combines PiCar-X rover, on-laptop YOLOv8-pose, four Fetch.ai agents, ElevenLabs Spanish voice, and MASt3R plus InstantSplat reconstruction viewed in Meta Quest 2.
- **Team size:** 4 | **Confidence:** high | unverified: team_size; n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/riis) | [GitHub](https://github.com/srinisriram/RIIS)

### SPECTRA  (LA Hacks 2026)

- **Prizes:** Track: Flicker To Flow [unknown]  (tier: track_winner)
- **Pitch:** Small RGB-guided neural network that upsamples iPhone LiDAR depth maps to dense metric depth in real time on-device, with an iOS app.
- **Problem / user:** Consumer LiDAR depth is too sparse and blurry at camera resolution for robotics or AR planning. / robotics, AR and accessibility developers
- **Domain / idea type:** ai_agents_infra + accessibility / data_or_analytics
- **Platforms / hardware / AI:** mobile_ios; web / True / vision; predictive_ml
- **Stack:** langs Python; Swift; JavaScript; frontend SwiftUI; ARKit; HTML; CSS; backend FastAPI; PyTorch; db ; hosting Vercel; ASUS GX10
- **Tech/APIs:** PyTorch (framework, core); ASUS Ascent GX10 (hardware_part, core, sponsor); ZeticMLange (other, core, sponsor); CoreML (framework, core); ARKitScenes dataset (data_source, core); iPhone LiDAR/ARKit (hardware_part, core)
- **Sponsor APIs:** ASUS Ascent GX10; Zetic Melange | fit: Used Zetic Melange for on-device deployment and the ASUS GX10 for training and as an optional inference server.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup long, impact claims True (Compares LiDAR sensor price ranges ($3-$25 vs $8,000-$75,000) and states model size of about 2 MB.)
- **Notes:** Trained a custom 2 MB MobileNetV2-based model on ARKitScenes using an ASUS GX10; runs via CoreML/Zetic on phone or via GX10 server; A/B demo mode. Page also shows a Zetic Company Challenge win not in queue.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/spectra-qbj2gf)

### YES? or YES!  (LA Hacks 2026)

- **Prizes:** Most Questionable Use of 36 Hours [unknown]  (tier: track_winner)
- **Pitch:** Phone-call gag where an AI fish offers two bad options and three real guppies in a tank vote by position, after which a MacBook carries out the choice.
- **Problem / user:** No real problem; the team set out to build the most unhinged use of 36 hours with fish making real-life decisions. / hackathon audience and demo viewers
- **Domain / idea type:** entertainment_games + ai_agents_infra / entertainment_or_game
- **Platforms / hardware / AI:** hardware; web; bot_or_chat / True / llm_chat; agent_or_tool_use; speech_or_voice; vision
- **Stack:** langs TypeScript; JavaScript; Python; frontend Next.js; backend Node.js; Pusher; Playwright; db Redis; hosting Fly.io; Vercel
- **Tech/APIs:** Claude Haiku 4.5 (ai_model, core); Twilio Media Streams (telecom, core); Deepgram (ai_model, core); ElevenLabs (ai_model, core); OpenCV fish tracking (framework, core); Pusher (framework, supporting); Playwright (framework, supporting); Redis (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 72 (before/in/after event: 0/72/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Twilio call streamed through Deepgram, Claude Haiku 4.5 and ElevenLabs; OpenCV counts fish per tank side at 30 Hz with 1-second rolling-majority vote; Playwright/osascript runners replaced slow computer use.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/yes-or-yes) | [GitHub](https://github.com/lukietee/YESorYES)
