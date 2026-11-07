# HackHarvard: project cards (8 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackHarvard 2024

### Diabeteasy  (HackHarvard 2024)

- **Prizes:** 3rd Place Overall Hack [3rd]  (tier: overall_top3)
- **Pitch:** Smart insole with pressure sensors that streams foot data, alerts patient and doctor, and drives a shape-changing sole to correct gait for type 2 diabetics.
- **Problem / user:** Diabetic neuropathy patients lose foot sensation and need frequent insole replacements to avoid complications. / type 2 diabetes patients with peripheral neuropathy and their doctors
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / None
- **Stack:** langs C++; TypeScript; frontend Next.js; React; Three.js; Tailwind; backend Node.js; WebSockets; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Arduino (hardware_part, core); Servo motors (hardware_part, core); Pressure sensors (hardware_part, core); WebSockets (framework, supporting); Three.js (framework, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Custom three-sensor insole built on ESP32/Arduino with servos driving a cardboard shape-changing model sole; data streamed over WebSockets to a Three.js dashboard.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; n_screenshots; is_sponsor flags; ui_polish; impact claims not fully scanned; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/diabeteasy)

### Garuda  (HackHarvard 2024)

- **Prizes:** 2nd Place Overall Hack [2nd]  (tier: overall_top3)
- **Pitch:** Disaster-response dashboard that analyzes drone footage for damage with a vision-language model, maps hot zones live and generates green rebuild plans.
- **Problem / user:** Responders need fast damage assessment and recovery planning after disasters, ideally sustainable rebuilding. / disaster recovery teams and emergency responders
- **Domain / idea type:** safety_security + sustainability_climate / automation_or_agent
- **Platforms / hardware / AI:** web / True / vision; llm_chat; predictive_ml
- **Stack:** langs Python; frontend Next.js; backend Flask; OpenCV; TensorFlow; db Firebase; hosting 
- **Tech/APIs:** LLaVA (ai_model, core); Google Maps API (maps_geo, core); Flask (framework, supporting); Next.js (framework, supporting); OpenCV (framework, supporting); TensorFlow (framework, supporting); Firebase (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 17 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Drone video uploads feed a Flask API that records hot zones; LLaVA annotates damage types; heatmap updated via a peer-to-peer network claim.
- **Team size:** 4 | **Confidence:** medium | unverified: has_hardware; is_sponsor flags; ui_polish; impact claims not fully scanned; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/garuda-pb7qtf) | [GitHub](https://github.com/TheSacredJump/garuda)

### MediGuide  (HackHarvard 2024)

- **Prizes:** Best first-time hack [unknown]  (tier: track_winner)
- **Pitch:** AI medication-adherence system that reads prescriptions, sets reminders and follows up with patients, including by voice calls.
- **Problem / user:** Many patients fail to take medications as prescribed, creating safety risks. / patients on medication regimens and their care providers
- **Domain / idea type:** health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; Python; frontend Next.js; React; shadcn; backend Flask; db Prisma; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); Vapi (ai_model, core); Next.js (framework, supporting); Flask (framework, supporting); Prisma (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 28 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims True (Quotes a study that 40-75% of adults do not take medications as prescribed.)
- **Notes:** Patients onboarded through a consultation flow; OpenAI parses prescriptions and Vapi handles voice interaction; cites adherence statistics.
- **Team size:** 3 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; placement_tier; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/mediguide-c9qn3t) | [GitHub](https://github.com/MediGuideApp/MediGuide)

### Sustain-ify  (HackHarvard 2024)

- **Prizes:** 1st Best Overall Hack [1st]  (tier: overall_top3)
- **Pitch:** Multi-agent app that helps people live sustainably through an eco-shopping assistant, DIY project ideas and personal health reports.
- **Problem / user:** Environmental decline and worsening personal health call for everyday tools that make sustainable choices easy. / eco-conscious consumers
- **Domain / idea type:** sustainability_climate + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; Dart; JavaScript; HTML; CSS; frontend Flutter; Streamlit; backend FastAPI; CrewAI; LangChain; LlamaIndex; db MongoDB; Firebase; hosting 
- **Tech/APIs:** GPT-4o (ai_model, core); Gemini 1.5 Pro (ai_model, supporting); Groq (ai_model, supporting); CrewAI (framework, core); LangChain (framework, supporting); LlamaIndex (framework, supporting); Tavily (data_source, supporting); Serper (data_source, supporting); MongoDB (database, supporting); Firebase (database, supporting); Flutter (framework, core); Streamlit (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 47 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 8, writeup long, impact claims False
- **Notes:** Combines several LLM providers and agent frameworks (CrewAI, LangChain, LlamaIndex) with web-search tools behind Flutter and Streamlit front ends.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; demo_video_url; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/sustain-ify) | [GitHub](https://github.com/SrikarVamsi/Sustain-ify)


## HackHarvard 2025

### Post Surgery Pillow (PSP)  (HackHarvard 2025)

- **Prizes:** 1st Best Overall Hack [1st]  (tier: overall_top3)
- **Pitch:** Hospital pillow with embedded sensors that monitors patients and uses Gemini to rank who needs nurse attention and what clinical action to take.
- **Problem / user:** Nurses juggling many critical patients lack prioritized, actionable information on who needs help first. / nurses and hospital care teams
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; predictive_ml
- **Stack:** langs Java; Python; frontend ; backend Node.js; db MongoDB; hosting 
- **Tech/APIs:** Arduino sensors (hardware_part, core); Google Gemini (ai_model, core); MongoDB (database, supporting); Node.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims True (Reports 100% edge-case detection accuracy from its own test readings.)
- **Notes:** Weighted scoring formula over sensor parameters plus edge-case detection, then Gemini-generated diagnosis; writeup frames pillow as smart hospital pillow, page title says post surgery.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; ai_types; event_start; event_end; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/post-surgery-pillow-psp) | [GitHub](https://github.com/quynhanh726/PSP-Post-Surgery-Pillow-)

### ResQme  (HackHarvard 2025)

- **Prizes:** 2nd Best Overall Hack [2nd]  (tier: overall_top3)
- **Pitch:** Offline ESP32 mesh network that lets people in disaster zones send messages and status updates without cell or internet infrastructure.
- **Problem / user:** Disasters knock out communication infrastructure, leaving victims unable to signal for help. / disaster victims and rescue coordinators
- **Domain / idea type:** safety_security + telecom_networking / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; mobile_cross / True / False
- **Stack:** langs C++; Python; frontend Next.js; React; Expo; React Native; Tailwind; Leaflet.js; backend Node.js; db Supabase; PostgreSQL; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); PainlessMesh (framework, core); GPS module (hardware_part, supporting); Supabase (database, supporting); Leaflet.js (maps_geo, supporting); Expo / React Native (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 33 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** PainlessMesh network on ESP32 nodes with GPS and OLED feedback; master node hosts a Wi-Fi access point web page and can mirror logs to the cloud; Expo mobile and Next.js dashboard also listed.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used; is_sponsor flags; ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/resqme-jq52al) | [GitHub](https://github.com/lordoftheseas/ResQme)

### ScrewYouIKEA.com  (HackHarvard 2025)

- **Prizes:** Best First-Time Hack [unknown]  (tier: track_winner)
- **Pitch:** Upload a furniture assembly manual PDF and get an interactive step-by-step 3D guide, with a public library of converted IKEA manuals.
- **Problem / user:** Printed assembly manuals are confusing and hard to follow. / people assembling flat-pack furniture
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; React; Three.js; Tailwind; pdfjs-dist; backend Express.js; db ; hosting Vercel
- **Tech/APIs:** Gemini 2.5 Flash/Pro (ai_model, core); Three.js (framework, core); pdf.js (framework, supporting); Web Speech API (other, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 31 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Gemini extracts parts and steps from manual PDFs (pdfjs) and renders them as Three.js 3D visualizations; voice input via Web Speech API; library of pre-converted manuals.
- **Team size:** 3 | **Confidence:** medium | unverified: writeup_sections; has_impact_claims; is_sponsor flags; ui_polish; event_start; event_end; placement_tier
- **Links:** [Devpost](https://devpost.com/software/screwyouikea) | [GitHub](https://github.com/donaragalstyan/ScrewYouIkea)

### Yumi  (HackHarvard 2025)

- **Prizes:** 3rd Best Overall Hack [3rd]  (tier: overall_top3)
- **Pitch:** Agentic social network where natural-language restaurant reviews build taste profiles, and AI agents help groups pick where to eat and coordinate.
- **Problem / user:** Choosing a restaurant for a group is hard because everyone's tastes and constraints differ. / friend groups deciding where to eat
- **Domain / idea type:** social_community + food_nutrition / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios; web / False / llm_chat; agent_or_tool_use; recommendation; speech_or_voice
- **Stack:** langs Python; TypeScript; Swift; frontend SwiftUI; Next.js; React; Tailwind; backend FastAPI; sentence-transformers; db Supabase; hosting Netlify; Render
- **Tech/APIs:** Google Gemini (ai_model, core); ElevenLabs (ai_model, supporting); Twilio (telecom, supporting); Google Places (maps_geo, supporting); sentence-transformers (ai_model, supporting); Supabase (database, supporting); SwiftUI (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 227 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims True (States image resizing cut upload time by 70%.)
- **Notes:** Gemini extracts flavor, atmosphere and price preferences from casual reviews; Twilio and ElevenLabs listed for agent calls/voice; native SwiftUI app plus Next.js web; image upload resizing claimed to cut upload time 70%.
- **Team size:** 4 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; depth of Twilio/ElevenLabs; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/yumi) | [GitHub](https://github.com/scrappydevs/Yummy)
