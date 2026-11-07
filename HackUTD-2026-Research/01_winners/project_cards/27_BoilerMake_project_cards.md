# BoilerMake: project cards (4 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## BoilerMake XI - included as the second most recent edition on Devpost because BoilerMake XIII has no Devpost page

### PromoteAI  (BoilerMake XI - included as the second most recent edition on Devpost because BoilerMake XIII has no Devpost page)

- **Prizes:** Klaviyo always puts our customers first [unknown]  (tier: sponsor_winner)
- **Pitch:** Generates platform-tailored social media posts and images from a company description and target audience, with direct posting integrations.
- **Problem / user:** Small companies struggle to produce consistent, optimized social media content across several platforms. / small businesses and marketers
- **Domain / idea type:** productivity_workplace + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; generative_media
- **Stack:** langs Python; JavaScript; frontend React; Tailwind; backend Django; db SQL; hosting 
- **Tech/APIs:** OpenAI GPT-4 (ai_model, core); DALL-E (ai_model, core); Twitter/LinkedIn/Facebook APIs (other, supporting); Django (framework, supporting)
- **Sponsor APIs:**  | fit: Awarded Klaviyo's customer-first prize; page does not list Klaviyo, project is a marketing content tool.
- **Repo:** public, commits 30 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** GPT-4 writes posts and DALL-E makes images per platform (Twitter, LinkedIn, Facebook, Instagram); integrates with social accounts for posting; Django backend with SQL store.
- **Team size:** 2 | **Confidence:** medium | unverified: is_sponsor flags; ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/promoteai) | [GitHub](https://github.com/aryanmathur2003/promoteAI)


## BoilerMake XII

### Fluention  (BoilerMake XII)

- **Prizes:** 3rd Place Prize: JBL Speaker [3rd]  (tier: overall_top3)
- **Pitch:** AI speech-pathology assistant that trains pronunciation and articulation with lip-movement tracking, speech recognition and guided exercises, plus a communication aid module.
- **Problem / user:** People with speech difficulties lack accessible, structured speech-therapy practice. / people with speech or pronunciation difficulties
- **Domain / idea type:** health_wellness + accessibility / other
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; frontend Next.js; HTML; CSS; backend FastAPI; db ; hosting Google Cloud
- **Tech/APIs:** MediaPipe (framework, core); OpenCV (framework, core); TensorFlow (framework, supporting); OpenAI GPT-4 (ai_model, supporting); Groq (ai_model, supporting); Lipsync API (ai_model, supporting); Google Cloud (cloud, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 105 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 31, writeup long, impact claims False
- **Notes:** Uses webcam lip and tongue tracking (MediaPipe) with timed lip-shape holds and breath-control exercises modeled on clinical speech therapy; includes a lip-sync API.
- **Team size:** 4 | **Confidence:** medium | unverified: n_screenshots; second module details only partly read
- **Links:** [Devpost](https://devpost.com/software/fluention) | [GitHub](https://github.com/jihwimin/fluention)

### MockMade  (BoilerMake XII)

- **Prizes:** 2nd Place Prize: Sony Headphone [2nd]; Cartesia: Best Use of Sonic [unknown]; Caterpillar: Best Cloud Implementation [unknown]  (tier: overall_top3)
- **Pitch:** AI mock-interview platform running real-time behavioral phone-style and technical coding interviews, then grading the session.
- **Problem / user:** Job seekers lack realistic interview practice in a competitive market. / CS students and job seekers
- **Domain / idea type:** productivity_workplace + education / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; Magic UI; backend ; db MongoDB; hosting Vercel; Render
- **Tech/APIs:** OpenAI (ai_model, core); Cartesia Sonic (ai_model, core, sponsor); Retell (ai_model, core); Auth0 (auth, supporting); MongoDB (database, supporting); Cloudinary (other, supporting); Render (cloud, supporting); Vercel (cloud, supporting); sync (ai_model, supporting)
- **Sponsor APIs:** Cartesia | fit: Used Cartesia text-to-speech voice for the AI interviewer (listed in Built With).
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims False
- **Notes:** Behavioral interview is a simulated phone call with video replay; technical round pairs a LeetCode-style editor with an AI interviewer giving hints.
- **Team size:** 4 | **Confidence:** medium | unverified: sponsor_fit_note; Caterpillar cloud use not described; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/mockmate) | [GitHub](https://github.com/danielxies/bmakebackend)

### REMI  (BoilerMake XII)

- **Prizes:** 1st Place Prize: iPad [1st]; College of Engineering: Most Consequential Project [unknown]  (tier: overall_top3)
- **Pitch:** Smart bike lock with encrypted NFC keys plus a mobile app that lets owners list bikes and renters find and unlock them nearby.
- **Problem / user:** Students need cheap, flexible short-term transportation, and bike owners lack a secure way to lend bikes out. / students and bike owners/renters
- **Domain / idea type:** mobility_transport + retail_consumer / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross / True / False
- **Stack:** langs Dart; Java; C++; frontend Flutter; backend Firebase; db Firebase; hosting 
- **Tech/APIs:** Arduino Nano (hardware_part, core); NFC reader (hardware_part, core); Bluetooth Low Energy (other, core); Servo motor (hardware_part, core); Flutter (framework, core); Firebase (database, supporting); Google Maps (maps_geo, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 109 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims True (Claims improving quality of life for millions of students (unquantified beyond that).)
- **Notes:** Custom lock hardware (Arduino Nano, servo, NFC reader) paired over BLE with a Flutter app; Firebase auth/database and Google Maps for finding bikes.
- **Team size:** 3 | **Confidence:** medium | unverified: ai_used; is_sponsor flags; ui_polish; event_start; event_end; placement_tier
- **Links:** [Devpost](https://devpost.com/software/remi-hbkrzs) | [GitHub](https://github.com/mihir-chauhan/REMI)
