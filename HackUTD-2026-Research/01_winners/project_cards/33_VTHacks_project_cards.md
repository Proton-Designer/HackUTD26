# VTHacks: project cards (12 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## VTHacks - 13

### Cognita  (VTHacks - 13)

- **Prizes:** VTHacks - 2nd Place Prize [2nd]  (tier: overall_top3)
- **Pitch:** Intern-onboarding assistant that turns PDFs, manuals and policy documents into personalized interactive learning using retrieval and Gemini.
- **Problem / user:** New hires are handed hundreds of pages of static documents, which is slow for HR and ineffective for learning. / interns, new hires and HR teams
- **Domain / idea type:** productivity_workplace + education / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React; Tailwind CSS; backend Flask; LangChain; db ChromaDB; MongoDB; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); ChromaDB (database, core); LangChain (framework, supporting); MongoDB (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 57 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Document-grounded retrieval pipeline (ChromaDB with LangChain) over company documents; Flask backend with React/TypeScript frontend.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/cognito-at5gu8) | [GitHub](https://github.com/Scotchex/Cognita)

### Fire Guard  (VTHacks - 13)

- **Prizes:** VTHacks - 3rd Place Prize [3rd]  (tier: overall_top3)
- **Pitch:** Helmet-mounted tactical system for firefighters combining camera, LiDAR and radar sensing with on-device AI, mapping and team communication.
- **Problem / user:** Firefighters lose visibility and orientation in smoke and lack reliable location sharing and communication inside buildings. / Firefighters and incident commanders
- **Domain / idea type:** safety_security + sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; JavaScript; frontend Next.js; React; Tailwind CSS; Three.js; Leaflet.js; Chart.js; backend FastAPI; WebSockets; db ; hosting 
- **Tech/APIs:** YOLOv5 (ai_model, core); DistilGPT-2 (ai_model, supporting); Whisper (ai_model, supporting); MediaPipe (framework, supporting); OpenCV (framework, supporting); Jetson TX2 (hardware_part, core); ESP32 (hardware_part, supporting); RPLidar (hardware_part, core); 24GHz FMCW radar (hardware_part, supporting); Arduino (hardware_part, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 33 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Multi-sensor helmet fusing camera, LiDAR, radar and IMU, with on-device YOLOv5 detection and DistilGPT-2 room labelling; team admits photos are limited and points to slideshow.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/fire-guard) | [GitHub](https://github.com/JohnRankin5/VTHack2025)

### SpeakEasy  (VTHacks - 13)

- **Prizes:** VTHacks - Best First Time Hack [unknown]  (tier: track_winner)
- **Pitch:** Web app that transcribes an uploaded talk video and uses Gemini to grade speech and delivery and suggest coaching.
- **Problem / user:** People practicing public speaking lack structured feedback on content, delivery and audio quality. / Students and aspiring public speakers
- **Domain / idea type:** education + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; rag_or_search; vision
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; backend Flask; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); Whisper (ai_model, core); ffmpeg (other, core); PyTorch (framework, supporting); librosa (framework, supporting); OpenCV (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 47 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Pipeline combines ffmpeg, Whisper transcription, Gemini text grading and audio analysis with retrieval of example talks; very long dependency list.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/speakeasy-49nuf1) | [GitHub](https://github.com/dsahero/speak_easy)

### StoryVue  (VTHacks - 13)

- **Prizes:** VTHacks - 1st Place Prize [1st]  (tier: overall_top3)
- **Pitch:** Hands-free voice reading assistant that uses OCR and an OpenAI model to read printed text aloud and explain or summarize it for visually impaired children.
- **Problem / user:** Visually impaired children cannot read printed material independently. / visually impaired children
- **Domain / idea type:** accessibility + education / social_good
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs JavaScript; frontend HTML; CSS; backend Node.js; Express.js; db ; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); Tesseract OCR (ai_model, core); TensorFlow (framework, unclear); Express.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 29 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Tesseract OCR plus OpenAI language model, fully voice-controlled; Figma slide deck linked from the page.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/storyvue) | [GitHub](https://github.com/JoshuaEssandoh/VTHacks13)


## VTHacks - 14

### aftercare.  (VTHacks - 14)

- **Prizes:** VTHacks - 3rd Place Prize; [MLH] Best Use of Vultr [3rd]  (tier: overall_top3)
- **Pitch:** Post-discharge follow-up system that checks in with patients by voice or text in English or Spanish, flags worrying answers and escalates to a physician.
- **Problem / user:** Patients lose clinical support after hospital discharge and deterioration may go unnoticed. / Discharged patients and their physicians
- **Domain / idea type:** health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; Vite; backend Node.js; Express.js; db SQLite; hosting Vultr; GoDaddy ANS
- **Tech/APIs:** Gemini (ai_model, core); ElevenLabs (ai_model, core); LiveKit (other, core); WebRTC (other, supporting); Vultr (cloud, supporting, sponsor); GoDaddy ANS (other, unclear, sponsor)
- **Sponsor APIs:** Vultr; GoDaddy ANS | fit: Prize is MLH Best Use of Vultr; Vultr and ANS appear in the built-with list, hosting detail not read in depth.
- **Repo:** public, commits 14 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Deterministic rules, not the model, decide clinical severity; supports voice (WebRTC/LiveKit) and bilingual check-ins with secure escalation.
- **Team size:** 3 | **Confidence:** medium | unverified: event_start; event_end; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/aftercare-b9di1l) | [GitHub](https://github.com/ksadiora/aftercare/tree/integrate-callsign)

### Bubu-Dins  (VTHacks - 14)

- **Prizes:** VTHacks - 2nd Place Prize; [Cloudforce] Most Interesting Use of HokieAI [2nd]  (tier: overall_top3)
- **Pitch:** Game-style financial literacy app where learners move through a map, practice housing and investing topics, and chat with a fictional banker character.
- **Problem / user:** Personal finance concepts like housing and investing are hard for young people to learn from dry material. / Young learners new to personal finance
- **Domain / idea type:** education + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; frontend React; backend Bun; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, supporting); OpenAI (ai_model, supporting); HokieAI (ai_model, supporting, sponsor); Figma (other, supporting)
- **Sponsor APIs:** HokieAI | fit: Prize is for most interesting use of HokieAI; page lists hockieai among tools but writeup detail on use was not reviewed in depth.
- **Repo:** public, commits 14 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 28, writeup medium, impact claims False
- **Notes:** Narrative learning map with an AI banker character who asks about tradeoffs rather than selling products; also placed in the Cloudforce HokieAI prize.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/bubu-dins) | [GitHub](https://github.com/Tramle26/Bubu-Dins)

### CuraVox  (VTHacks - 14)

- **Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 2nd Place [2nd]  (tier: sponsor_winner)
- **Pitch:** Physician hands a patient a QR code that opens a multilingual voice medication companion, Cora, configured with the drug, language and visit notes.
- **Problem / user:** Patients forget or misunderstand medication instructions after visits, especially across language barriers. / Physicians and patients on a new medication
- **Domain / idea type:** health_wellness + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind CSS; backend Node.js; db ; hosting 
- **Tech/APIs:** Claude (ai_model, core); Gemini (ai_model, supporting); Deepgram (ai_model, core)
- **Sponsor APIs:**  | fit: Built for the Impiricus HCP engagement challenge; gives physicians a way to extend engagement to patients via a voice companion.
- **Repo:** public, commits 2 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video False, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Setup takes about thirty seconds via QR; the patient talks to a voice companion in Spanish, French or English.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/curavox) | [GitHub](https://github.com/Moustapha110/curavox)

### Deadbolt  (VTHacks - 14)

- **Prizes:** VTHacks - 1st Place Prize [1st]  (tier: overall_top3)
- **Pitch:** Chrome extension that scans prompts before they are sent to AI chatbots and blocks or warns when they contain sensitive or controlled information.
- **Problem / user:** Employees may paste classified or sensitive data into AI tools, leaking it before anyone can intervene. / Staff at organizations handling controlled or sensitive data
- **Domain / idea type:** safety_security + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** browser_extension / False / predictive_ml; llm_chat
- **Stack:** langs TypeScript; frontend Vite; backend ; db ; hosting 
- **Tech/APIs:** Claude (ai_model, supporting); HokieAI (ai_model, supporting, sponsor); Manifest V3 (framework, core); NER classifier (ai_model, core)
- **Sponsor APIs:** HokieAI
- **Repo:** public, commits 42 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Intercepts the Enter keypress client-side and applies tiered block/warn rules, with controlled-marking detection that cannot be overridden; uses NER and a classifier.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/deadbolt-vs2xlp) | [GitHub](https://github.com/srikarb-jpg/VTHACKS14.git)

### FalsePay  (VTHacks - 14)

- **Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** Platform that audits Open Payments records for questionable physician payments, enriches physician data from the live NPPES registry and gives physicians a low-friction audit flow.
- **Problem / user:** Pharma-to-physician payment records can be inaccurate or questionable and hard to audit and engage physicians about. / Pharma compliance teams and physicians
- **Domain / idea type:** health_wellness + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs Python; TypeScript; frontend Next.js; Tailwind CSS; backend FastAPI; db PostgreSQL; pgvector; TimescaleDB; hosting 
- **Tech/APIs:** CMS Open Payments (data_source, core); NPPES registry (data_source, core); pgvector (database, supporting); TimescaleDB (database, supporting); FastAPI (framework, core); Docker (other, supporting)
- **Sponsor APIs:**  | fit: Built for the Impiricus HCP engagement challenge; used public Open Payments and NPPES data to build an audit and physician-engagement flow.
- **Repo:** public, commits 11 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims None
- **Notes:** Combines CMS Open Payments data with live NPPES registry lookups, pgvector and TimescaleDB; has a hosted site.
- **Team size:** 2 | **Confidence:** medium | unverified: event_start; event_end; ai_used; has_impact_claims
- **Links:** [Devpost](https://devpost.com/software/falsepay) | [GitHub](https://github.com/sudip-manchare/hcp-outbound)

### HireWire  (VTHacks - 14)

- **Prizes:** [GoDaddy] Best Use of ANS — 3rd Place; [MLH] Best Use of Presage [3rd]  (tier: track_winner)
- **Pitch:** Voice-first job application agent where each application is an agent-to-agent handshake that verifies employer identity with certificates before sharing private data.
- **Problem / user:** Job seekers share private data with unverified employers and automated postings. / Job seekers and employers
- **Domain / idea type:** productivity_workplace + safety_security / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Python; frontend Next.js; React; backend Python; db MongoDB; hosting 
- **Tech/APIs:** Gemini (ai_model, core); ElevenLabs (ai_model, supporting); Databricks (cloud, unclear); MongoDB (database, supporting); GoDaddy ANS (other, unclear, sponsor)
- **Sponsor APIs:** GoDaddy ANS | fit: Placed 3rd in GoDaddy ANS prize; the agent identity handshake matches the ANS theme, but ANS use is not named in the page tags.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live not_checked, screenshots 1, writeup short, impact claims False
- **Notes:** Agent-to-agent identity verification using domain-anchored certificates before data is exchanged; page text is short and has one screenshot.
- **Team size:** 3 | **Confidence:** medium | unverified: event_start; event_end; sponsor_apis_used; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/hirewire) | [GitHub](https://github.com/vijayvanapalli96/vthacks_2026/)

### Persist Health  (VTHacks - 14)

- **Prizes:** [Impiricus] Build the Next HCP Engagement Tool — 3rd Place [3rd]  (tier: sponsor_winner)
- **Pitch:** AI tool that helps doctors understand patients better and supports patients between appointments, funded by pharma rather than charging patients or doctors.
- **Problem / user:** Doctors lack insight into patients between visits and patients get little in-between support. / Doctors and patients
- **Domain / idea type:** health_wellness / new_category
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; frontend React; backend Express.js; db MySQL; hosting Vultr; GoDaddy
- **Tech/APIs:** OpenRouter (ai_model, core); Vultr (cloud, supporting, sponsor); GoDaddy (other, supporting, sponsor); MySQL (database, supporting)
- **Sponsor APIs:** Vultr; GoDaddy | fit: Built for the Impiricus HCP engagement challenge; positions pharma funding as the sustaining model.
- **Repo:** public, commits 6 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 31, writeup long, impact claims False
- **Notes:** Business model has pharma pay while the tool is free to doctors and patients; 31 screenshots and a hosted site.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/pied-piper-test) | [GitHub](https://github.com/wasdthedebugger/vthacks)

### Radar  (VTHacks - 14)

- **Prizes:** VTHacks - Best UI/UX Hack; [GoDaddy] Best Use of ANS — 2nd Place [unknown]  (tier: track_winner)
- **Pitch:** iOS home-emergency system where AI agents analyze camera events, assess threats, call or alert contacts and assemble an incident record.
- **Problem / user:** Home emergencies such as intruders leave people without fast situational awareness, response and documentation. / Homeowners and their emergency contacts
- **Domain / idea type:** safety_security / automation_or_agent
- **Platforms / hardware / AI:** mobile_ios / False / vision; agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Swift; Python; frontend SwiftUI; backend Python; db MongoDB; hosting Vultr
- **Tech/APIs:** Gemini API (ai_model, core); ElevenLabs (ai_model, supporting); Retell AI (ai_model, supporting); MongoDB (database, supporting); Resend (other, supporting); Vultr (cloud, unclear, sponsor)
- **Sponsor APIs:** Vultr; GoDaddy ANS | fit: Placed 2nd in GoDaddy Best Use of ANS; ANS itself not listed in built-with tags, so how it was used was not confirmed.
- **Repo:** public, commits 333 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Multi-agent design (camera agent plus voice and notification agents) with native Swift iOS client; won UI/UX prize and GoDaddy ANS 2nd.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; sponsor_apis_used; sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/boom-hmsdki) | [GitHub](https://github.com/cayden-h/VTHacks)
