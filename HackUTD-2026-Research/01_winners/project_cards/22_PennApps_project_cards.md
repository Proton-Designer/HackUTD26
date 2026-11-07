# PennApps: project cards (7 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## PennApps XXV (Fall 2024)

### Rally AI  (PennApps XXV (Fall 2024))

- **Prizes:** Best Overall 2nd [2nd]; Best Design [unknown]; The Wolfram Award [unknown]  (tier: overall_top3)
- **Pitch:** Multi-agent web app that generates personalised, state-compliant campaign ads where a politician's cloned voice and lip-synced video address a voter's local issues.
- **Problem / user:** Voters feel disconnected from politicians and campaigns lack tools to show how policies affect individual voters. / political campaign teams and voters
- **Domain / idea type:** civic_legal + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; generative_media; speech_or_voice; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind CSS; backend ; db Supabase PostgreSQL; hosting Vercel
- **Tech/APIs:** OpenAI GPT-4o-mini (ai_model, core); Cartesia Sonic (ai_model, core); Sync Labs (ai_model, core); Firecrawl (data_source, core); Perplexity API (data_source, supporting); Pexels (data_source, supporting); FFmpeg (framework, supporting); Supabase (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 83 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims True (Cites talks with 70+ campaigns and 40+ ad teams; calls customized campaign material a massive market.)
- **Notes:** Pipeline: Firecrawl and Perplexity research, GPT-4o-mini script, Cartesia voice, Sync Labs lipsync, Pexels b-roll, FFmpeg; compliance LLM chain using NCSL and OpenFEC data plus a database of AI political ad bills.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/rally-8sxi2t) | [GitHub](https://github.com/pr28416/rally)

### SoundSheild  (PennApps XXV (Fall 2024))

- **Prizes:** Best Overall 1st [1st]; The Wolfram Award [unknown]  (tier: overall_top3)
- **Pitch:** Wearable on a Raspberry Pi Zero that filters noise, plays calming audio when sound gets overwhelming and alerts the user to people behind them using a camera.
- **Problem / user:** People with sensory hypersensitivity, common in autism, are overwhelmed by everyday noise. / people with sound sensitivity
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi Zero (hardware_part, core); OpenCV (framework, core); librosa (framework, core); SciPy / NumPy (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 8, writeup medium, impact claims True (Cites that 50 to 70 percent of autistic people have sound hypersensitivity.)
- **Notes:** Spectral subtraction and dynamic range compression on a Pi Zero; leaves speech unfiltered; OpenCV person detection behind the wearer.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/soundsheild) | [GitHub](https://github.com/arijitchakma79/PennApps2024)

### SurgeVue  (PennApps XXV (Fall 2024))

- **Prizes:** Best Overall 3rd [3rd]; Best AR/VR Hack [unknown]  (tier: overall_top3)
- **Pitch:** AR neurosurgery assistant that outlines tumors and foreign objects via ML, tracks hand motion with an Arduino gyroscope and sweat sensor, secured by face and RFID login.
- **Problem / user:** Brain surgery margins for error are tiny and emergency neurosurgery mortality is high. / neurosurgeons
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; hardware / True / vision; predictive_ml
- **Stack:** langs Python; Swift; C++; JavaScript; frontend SceneKit; HTML/CSS; backend Flask; db ; hosting 
- **Tech/APIs:** PyTorch (ai_model, core); OpenCV (framework, core); SceneKit (framework, core); Arduino gyroscope (hardware_part, core); Sweat sensor (hardware_part, supporting); RFID (hardware_part, supporting); PropelAuth (auth, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 41 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup medium, impact claims True (Cites a 15-fold mortality increase for non-elective neurosurgery.)
- **Notes:** Swift/SceneKit iOS AR overlay, PyTorch tumor classifier behind Flask, Arduino gyroscope and sweat sensor, PropelAuth with face recognition and RFID; page also links a slide deck and Drive file.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/surgikalai) | [GitHub](https://github.com/jeet-dekivadia/SurgeVue)


## PennApps XXVI (Fall 2025)

### Dispatch  (PennApps XXVI (Fall 2025))

- **Prizes:** 2nd Place Overall [2nd]  (tier: overall_top3)
- **Pitch:** AI copilot for 911 dispatchers that transcribes calls live, detects urgency and stress, writes incident briefs, suggests protocol questions and ranks a triage queue.
- **Problem / user:** Dispatchers must listen, type and recall protocols under stress, slowing emergency response. / 911 dispatchers
- **Domain / idea type:** safety_security + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs JavaScript; HTML; CSS; frontend Next.js; React; Tailwind CSS; backend ; db ; hosting Vercel
- **Tech/APIs:** Ollama (ai_model, core); Open 911 datasets (data_source, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 30 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup short, impact claims False
- **Notes:** Local LLM inference with Ollama; priority scoring grounded in open 911 datasets (Seattle, NYC); multilingual and stress detection claimed; short writeup with no section headings beyond the story.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/dispatch-evf2sq) | [GitHub](https://github.com/us-abdullah/dispatch10)

### Intention.ai  (PennApps XXVI (Fall 2025))

- **Prizes:** Best Beginner Hack (>2 members first time) [unknown]  (tier: track_winner)
- **Pitch:** Chrome extension and dashboard that uses webcam face-landmark emotion cues to tell when a student is focused, tired or stressed and has Gemini suggest study adjustments.
- **Problem / user:** Workers and students lose many hours to poor focus and lack feedback on their focus patterns. / students
- **Domain / idea type:** productivity_workplace + education / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension; web / False / vision; llm_chat; recommendation
- **Stack:** langs TypeScript; JavaScript; Python; frontend React; Next.js; Tailwind CSS; backend TypeScript; db MongoDB; hosting 
- **Tech/APIs:** face-api.js (ai_model, core); Google Gemini API (ai_model, core); MongoDB (database, supporting); JWT (auth, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims True (Cites workers losing over 500 hours a year to disruptions.)
- **Notes:** Beginner-track winner. face-api.js on-device emotion detection plus slouch, blink and head-tilt heuristics feeding Gemini recommendations; JWT auth; Chrome extension toggle.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/pennapps-f2k83a)

### kinemo  (PennApps XXVI (Fall 2025))

- **Prizes:** 1st Place Overall [1st]  (tier: overall_top3)
- **Pitch:** Webcam-only motion-controlled two-player game console with gesture menu and three games: Boxing, Flying Fruits and Reaction Time.
- **Problem / user:** No stated problem; began as a boxing motion tracker and grew into a multi-game platform. / casual players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / vision
- **Stack:** langs Python; frontend Pygame; backend ; db ; hosting 
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); Pygame (framework, core); NumPy (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 73 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Pose estimation with MediaPipe drives punch, kick and weave rules with cooldowns and stuns; hand-gesture menu; team toured it around the venue for feedback; 9 gallery photos with real play sessions.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/kinemo) | [GitHub](https://github.com/arvinmefsha/kinemo)

### OverSEA  (PennApps XXVI (Fall 2025))

- **Prizes:** 3rd Place Overall [3rd]  (tier: overall_top3)
- **Pitch:** Detects untracked illegal fishing vessels by comparing satellite radar detections with AIS, shows hotspots on a 3D globe, with a Gemini agent and Exa maritime-law research.
- **Problem / user:** Coast guards cannot patrol huge exclusive economic zones, and many industrial fishing vessels go untracked. / coast guards and marine conservation analysts
- **Domain / idea type:** sustainability_climate + safety_security / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml; rag_or_search
- **Stack:** langs Python; frontend Next.js; Tailwind CSS; Recharts; Mapbox; backend Python; db MongoDB; hosting 
- **Tech/APIs:** Global Fishing Watch API (data_source, core); MongoDB (database, core, sponsor); Auth0 (auth, core, sponsor); Google Gemini (ai_model, core, sponsor); Exa (data_source, supporting); Mapbox (maps_geo, core); SciPy clustering (other, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 185 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (Cites fish-stock overfishing and untracked vessel percentages from published papers.)
- **Notes:** Global Fishing Watch Sentinel-1 SAR and AIS data in MongoDB; SciPy density clustering for hotspots; Auth0 clearance levels gate features; Mapbox 3D globe; writeup cites papers.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/oversear) | [GitHub](https://github.com/spicybigmac/pennapps)
