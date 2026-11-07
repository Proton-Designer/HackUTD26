# HooHacks: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HooHacks 2025

### Dr. Andy - The Deployable Surgeon  (HooHacks 2025)

- **Prizes:** Best Overall - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Remote surgery rig: a surgeon in any OpenXR VR headset controls robotic arms with a stereo camera via hand tracking and ROS.
- **Problem / user:** Surgical expertise is unavailable in war zones, disaster areas and remote regions. / surgeons and remote patients
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; other / True / None
- **Stack:** langs C; C#; C++; Python; HLSL; frontend Unity; backend ROS; db ; hosting 
- **Tech/APIs:** Meta Quest 3 hand tracking / OpenXR (hardware_part, core); ROS (framework, core); Unity (framework, core); Arduino (hardware_part, core); Stereo camera system (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 55 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup medium, impact claims True (Claims sub-50ms control latency in the demo.)
- **Notes:** Built the robot from scratch; Meta Quest 3 hand tracking through Unity mapped to ROS commands; page claims sub-50ms latency and a suture-tying demo; ML stabilization described as planned or used inconsistently.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/y-u9oxsk) | [GitHub](https://github.com/paris-phan/and-e)

### Show Me A Sign  (HooHacks 2025)

- **Prizes:** Best Overall - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Duolingo-style ASL learning site that checks fingerspelled letters from webcam video with a custom CNN combined with geometric hand-shape detection.
- **Problem / user:** Mainstream language apps overlook American Sign Language practice with feedback. / ASL learners
- **Domain / idea type:** education + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind CSS; shadcn/ui; backend Flask; Socket.IO; db Supabase; hosting 
- **Tech/APIs:** TensorFlow CNN (ai_model, core); MediaPipe (ai_model, supporting); OpenCV (framework, core); Supabase (database, supporting); Socket.IO (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 63 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup long, impact claims False
- **Notes:** CNN trained on about 25,000 wireframe-style hand images to reduce skin-tone bias, fused with OpenCV finger geometry; WebSocket frame streaming at controlled frame rate.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/show-me-a-sign) | [GitHub](https://github.com/itskevinshi/lingo-sign-explorer)

### wearit  (HooHacks 2025)

- **Prizes:** Best Overall - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Mobile app that takes a photo of a wardrobe item and generates weather-aware outfit ideas, avatar try-on and shopping links via a chain of APIs.
- **Problem / user:** People own clothes but struggle to style them into outfits. / fashion-conscious shoppers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / vision; llm_chat; recommendation
- **Stack:** langs JavaScript; frontend React Native; Expo; React Navigation; backend ; db ; hosting AWS S3
- **Tech/APIs:** Google Cloud Vision (ai_model, core); Together AI Mistral-7B (ai_model, core); Open-Meteo (data_source, supporting); Pexels API (data_source, core); SerpAPI Google Shopping (data_source, supporting); ReadyPlayerMe (other, supporting); AWS S3 (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 49 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Chained pipeline: Google Cloud Vision, Together AI Mistral-7B to build queries, Open-Meteo weather, Pexels images, SerpAPI shopping, ReadyPlayerMe avatars, S3 uploads.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/wearit-a5nw62) | [GitHub](https://github.com/athiraponneth/HooHacks25)


## HooHacks 2026

### Agent Gauntlet  (HooHacks 2026)

- **Prizes:** Best Overall - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Local benchmark where a task browser agent and a red-team agent duel live, testing resistance to prompt injection, fake UI, redirects and credential-harvesting forms.
- **Problem / user:** Browser agents can be tricked by malicious page content, so capability alone does not mean safety. / AI safety researchers and agent developers
- **Domain / idea type:** ai_agents_infra + safety_security / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend Next.js 16; React; Tailwind CSS; Recharts; backend Playwright; Convex; db Convex; hosting 
- **Tech/APIs:** Playwright (framework, core); OpenAI API (GPT-4o judge) (ai_model, core); Anthropic API (ai_model, core); Convex (database, supporting); Vitest (framework, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 18 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup long, impact claims False
- **Notes:** Playwright injects attacks as the page loads; agents run rule-based or LLM-backed (OpenAI/Anthropic); GPT-4o judge plus canary leak check; exports JSON, CSV and ShareGPT JSONL; Wild West themed hand-drawn SVG UI.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/agent-gauntlet) | [GitHub](https://github.com/abhimaddi/agent-gauntlet)

### ScamShield  (HooHacks 2026)

- **Prizes:** Best Overall - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Raspberry Pi device that listens to speakerphone calls, scores scam likelihood with Gemini plus keywords, warns the user via Nest/LEDs and alerts family with a dashboard.
- **Problem / user:** Older adults on scam calls are pressured and isolated before family can intervene. / older adults and their families
- **Domain / idea type:** safety_security + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; db SQLite; Railway Postgres; hosting Vercel; ngrok
- **Tech/APIs:** Gemini API (ai_model, core); ElevenLabs (ai_model, core); Raspberry Pi (hardware_part, core); Google Nest (hardware_part, supporting); Twilio (telecom, supporting); Auth0 (auth, supporting); SenseCAP Indicator (hardware_part, token)
- **Sponsor APIs:** 
- **Repo:** public, commits 53 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Local speech-to-text on Pi, Gemini risk score with keyword fallback, ElevenLabs spoken warning cast to Google Nest, Twilio/WhatsApp alerts, Auth0 Next.js dashboard; SenseCAP unit was dead on arrival.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/scamshield-87rbxe) | [GitHub](https://github.com/TristanGru/ScamShield)

### Search and Rescue  (HooHacks 2026)

- **Prizes:** Best Overall - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Emergency-response simulator where users design multi-floor buildings in 2D/3D, place responders and victims, and run routed rescue simulations with hazards.
- **Problem / user:** Planning how responders move and hazards spread in complex buildings is hard to test before a real disaster. / emergency planners and building designers
- **Domain / idea type:** safety_security / data_or_analytics
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs Python; JavaScript; HTML; frontend React; Three.js; backend FastAPI; db ; hosting 
- **Tech/APIs:** A* pathfinding (other, core); Hungarian algorithm (other, core); Three.js (framework, core); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 44 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Uses A* pathfinding and Hungarian-algorithm assignment rather than ML despite the AI-powered label; JSON import/export workflow between editor, simulation and replay; Three.js renderer.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish; ai_used
- **Links:** [Devpost](https://devpost.com/software/search-and-rescue-2pwlkf) | [GitHub](https://github.com/Imranbilal268/Search_and_Rescue)
