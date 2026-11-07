# HackNC: project cards (16 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackNC 2025

### Carolina Capital: OS Game About Youth Finance Management  (HackNC 2025)

- **Prizes:** HackNC Beginner - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Financial-literacy game styled as a retro desktop OS where players run a virtual student's weekly life through banking, jobs, housing and education apps.
- **Problem / user:** Young people get little hands-on practice with money concepts like loans, APRs and investing. / teens and students learning personal finance
- **Domain / idea type:** education + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; HTML; CSS; frontend ARIA; backend ; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 7 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Windows-98-style interface with a simulated stock market and credit-score-based loan rates; Gemini is used inside the game; page has only one image.
- **Team size:** 3 | **Confidence:** high | unverified: Gemini depth guessed
- **Links:** [Devpost](https://devpost.com/software/carolina-capital-os-game-about-youth-finance-management) | [GitHub](https://github.com/j3ffreyl1u/HackNC-2025)

### CuratePlate  (HackNC 2025)

- **Prizes:** HackNC Beginner - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** App that photographs a restaurant menu and recommends dishes fitting the user's estimated nutritional needs and dietary restrictions.
- **Problem / user:** Eating out is hard when you must match meals to personal nutrition goals and restrictions. / health-conscious diners and people with dietary restrictions
- **Domain / idea type:** food_nutrition + health_wellness / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat; recommendation; speech_or_voice
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Nutritionix API (data_source, core); ElevenLabs (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 12 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Profile (height, weight, age, sex) drives a daily-needs estimate; Gemini reads menu photos and Nutritionix supplies nutrition data; ElevenLabs adds voice.
- **Team size:** 4 | **Confidence:** high | unverified: platforms guessed; Python-only stack listed
- **Links:** [Devpost](https://devpost.com/software/curateplate) | [GitHub](https://github.com/b-314/menu-vision)

### EyeCode: Speak With Your Eyes!  (HackNC 2025)

- **Prizes:** HackNC Beginner - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Webcam blink detector that turns short and long blinks into Morse code, converts it to text and speaks it aloud with text-to-speech.
- **Problem / user:** People who cannot speak or use their hands need low-cost, easy-setup communication. / people with severe motor or speech impairments
- **Domain / idea type:** accessibility + health_wellness / social_good
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice
- **Stack:** langs Python; frontend ; backend Flask; db ; hosting 
- **Tech/APIs:** MediaPipe FaceMesh (framework, core); OpenCV (framework, core); ElevenLabs (ai_model, core); Flask (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 2 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Needs only a webcam; blink timing via MediaPipe FaceMesh and OpenCV decodes Morse, with ElevenLabs voicing the output.
- **Team size:** 4 | **Confidence:** high | unverified: platforms (web vs desktop) guessed from Flask
- **Links:** [Devpost](https://devpost.com/software/eyecode-speak-with-your-eyes) | [GitHub](https://github.com/THEpranavsomalraju/eyecode)

### InterviewArcade  (HackNC 2025)

- **Prizes:** HackNC General - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Technical-interview simulator where students talk through and code a solution, then Gemini evaluates both and returns case-by-case feedback.
- **Problem / user:** Students lack realistic, spoken practice for technical interviews. / CS students preparing for technical interviews
- **Domain / idea type:** education + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; backend FastAPI; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); ElevenLabs (ai_model, core); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 155 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup medium, impact claims False
- **Notes:** Evaluates the spoken approach plus the code together, with company-specific question selection; ElevenLabs provides the interviewer voice.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/interview-arcade) | [GitHub](https://github.com/coopersizemore/InterviewArcade)

### Localized  (HackNC 2025)

- **Prizes:** HackNC General - 2nd Place [2nd]; Capital One Best Personal Finance Hack [unknown]  (tier: overall_top3)
- **Pitch:** iOS app giving students a weekly rotating lineup of local-business deals, one free coupon per week with another unlocked by sharing.
- **Problem / user:** Local businesses struggle to reach students, and students want affordable local options. / college students and local small businesses
- **Domain / idea type:** retail_consumer + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / False
- **Stack:** langs Swift; Python; frontend SwiftUI; backend FastAPI; JWT; db Amazon RDS; hosting AWS; Vercel
- **Tech/APIs:** SwiftUI (framework, core); FastAPI (framework, core); Amazon RDS (database, core); AWS (cloud, supporting); JWT (auth, supporting)
- **Sponsor APIs:**  | fit: Capital One personal-finance prize; page does not describe any Capital One API, so the link to the prize is only thematic (student savings).
- **Repo:** public, commits 67 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Gamified credit-free coupon system with a business-side dashboard to publish offers; backend deployed as a FastAPI service on AWS RDS with a public API docs page.
- **Team size:** 4 | **Confidence:** high | unverified: sponsor_fit_note
- **Links:** [Devpost](https://devpost.com/software/localized) | [GitHub](https://github.com/alexandramarum/localized/)

### SentiFrame  (HackNC 2025)

- **Prizes:** HackNC General - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Real-time emotion-aware AI that streams video and audio from Ray-Ban Meta glasses to a backend to analyze emotional tone and respond.
- **Problem / user:** Communication lacks awareness of emotional tone, and smart glasses have no developer APIs for live video or audio. / wearable users and people interested in emotional-context assistance
- **Domain / idea type:** ai_agents_infra + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; speech_or_voice; llm_chat; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind CSS; Framer Motion; Recharts; backend ; db Firebase; hosting 
- **Tech/APIs:** Ray-Ban Meta glasses (hardware_part, core); Google Gemini (ai_model, core); PyTorch (framework, supporting); ElevenLabs (ai_model, supporting); Firebase (database, supporting); Speech-to-text (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Team built its own pipeline to pull live video and audio off Ray-Ban Meta glasses, since no official API exists; multimodal emotion analysis with a Recharts dashboard.
- **Team size:** 3 | **Confidence:** medium | unverified: exact emotion model unclear; section headings partially read
- **Links:** [Devpost](https://devpost.com/software/smartframe-m4695z)


## HackNC 2026

### aerodance.  (HackNC 2026)

- **Prizes:** HackNC Frutiger Aero - 1st Place [1st]; [MLH] Best Use of Solana [unknown]  (tier: track_winner)
- **Pitch:** Motion-tracked Frutiger Aero dance game for one or two players who copy on-screen dancers for points, with optional Solana-connected battles and QR-code join.
- **Problem / user:** Dance games usually need dedicated hardware or consoles. / casual players and party groups
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs JavaScript; C/C++; Kotlin; TypeScript; HTML; frontend Three.js; backend ; db ; hosting 
- **Tech/APIs:** Three.js (framework, core); Solana (payments, supporting, sponsor); Photon (other, unclear, sponsor)
- **Sponsor APIs:** Solana; Photon | fit: MLH Solana prize; page says players can connect through Solana for dance battles.
- **Repo:** public, commits 232 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup short, impact claims False
- **Notes:** Players and crowd join by scanning a QR code; body-motion matching scores dance accuracy; Photon and Solana listed in Built With.
- **Team size:** 4 | **Confidence:** medium | unverified: pose-tracking method not named; ai_used; Photon use
- **Links:** [Devpost](https://devpost.com/software/aerodance) | [GitHub](https://github.com/IsaacThoman/aerodance-hacknc)

### Batman  (HackNC 2026)

- **Prizes:** [Photon] Best iMessage Agent - 1st Place [1st]  (tier: sponsor_winner)
- **Pitch:** iMessage safety agent: text it a date plan, it monitors your Find My location only for that window, checks in discreetly and alerts a chosen friend if you do not answer.
- **Problem / user:** People meeting someone, such as on a date, want a discreet safety net without sharing location constantly. / people going on dates or meeting strangers
- **Domain / idea type:** safety_security + social_community / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; mobile_ios / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Vite; backend Node.js; gRPC; db SQLite; hosting Fly.io; Vercel
- **Tech/APIs:** Photon (spectrum-ts) (other, core, sponsor); Claude (ai_model, core); iMessage / Apple Find My (other, core); LiveKit (other, supporting); OpenStreetMap (maps_geo, supporting); SQLite / Drizzle ORM (database, supporting)
- **Sponsor APIs:** Photon | fit: Photon iMessage agent track; the whole product is delivered as an iMessage conversation agent via Photon's spectrum-ts.
- **Repo:** public, commits 8 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup medium, impact claims False
- **Notes:** Two secret code words give a silent way out; location is watched only for the planned window; built over Photon's Spectrum iMessage layer with Claude and LiveKit.
- **Team size:** 2 | **Confidence:** high | unverified: github_url on page points to a landing-page repo tree/main
- **Links:** [Devpost](https://devpost.com/software/batman-cjer91) | [GitHub](https://github.com/markandeyay/batmanlandingpage)

### Bazaarly  (HackNC 2026)

- **Prizes:** HackNC General - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** Dashboard for pop-up apparel events where vendors organize inventory and sales per event, with a Solana Pay devnet checkout that records sales after payment.
- **Problem / user:** Pop-up clothing vendors lack a simple way to track inventory and sales across events. / pop-up apparel vendors and event shoppers
- **Domain / idea type:** retail_consumer + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat; recommendation
- **Stack:** langs TypeScript; Python; frontend React; Vite; backend Node.js; Express.js; FastAPI; db Firestore; Snowflake; hosting Firebase
- **Tech/APIs:** Solana Pay (payments, core, sponsor); Firebase / Firestore (database, core); Google Gemini (ai_model, supporting); CLIP (ai_model, supporting); rembg / OpenCV (framework, supporting); Snowflake Cortex (ai_model, unclear); Capital One Nessie (data_source, unclear, sponsor)
- **Sponsor APIs:** Solana; Snowflake; Capital One Nessie
- **Repo:** public, commits 57 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 31, writeup long, impact claims False
- **Notes:** Sale is recorded only after Solana Pay confirmation on Devnet; image tooling (CLIP, rembg, OpenCV) for garments; Capital One Nessie and Snowflake Cortex also listed.
- **Team size:** 5 | **Confidence:** medium | unverified: depth of Snowflake and Nessie; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/bazaarly) | [GitHub](https://github.com/joysudo/bazaarly)

### Call me Maybe  (HackNC 2026)

- **Prizes:** HackNC Frutiger Aero - 2nd Place [2nd]  (tier: track_winner)
- **Pitch:** Web project with a 3D model (GLB from Sketchfab) hosted on Vercel; the Devpost writeup contains almost no description.
- **Problem / user:** Not stated; the writeup is a joke placeholder. / not stated
- **Domain / idea type:** entertainment_games / other
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs Python; TypeScript; JavaScript; CSS; HTML; frontend ; backend ; db ; hosting Vercel
- **Tech/APIs:** Sketchfab / GLB models (other, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 66 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Devpost text is essentially empty (a short joke line); only Built With (glb, sketchfab), video, repo and a Vercel demo are given, so purpose is unverified.
- **Team size:** 4 | **Confidence:** low | unverified: one_line_pitch; problem_statement; target_user; domain_primary; idea_type; ai_used; platforms
- **Links:** [Devpost](https://devpost.com/software/call-me-maybe-3da9ky) | [GitHub](https://github.com/arjbarber/hacknc2026)

### CampusSync  (HackNC 2026)

- **Prizes:** HackNC Beginner - 3rd Place [3rd]  (tier: overall_top3)
- **Pitch:** iOS campus app that finds mutual free time among friends, tracks course schedules and helps students discover clubs, meeting times and dues.
- **Problem / user:** College life is scattered across posters, chats and calendars, so students miss events and hangouts. / college students, especially first-years
- **Domain / idea type:** social_community + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios / False / llm_chat
- **Stack:** langs Swift; frontend SwiftUI; backend ; db ; hosting 
- **Tech/APIs:** SwiftUI (framework, core); Claude (ai_model, supporting); RateMyProfessor (data_source, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 24 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 25, writeup medium, impact claims False
- **Notes:** Native SwiftUI app with MVVM; pulls RateMyProfessor data and uses Claude.
- **Team size:** 2 | **Confidence:** high | unverified: how Claude and RateMyProfessor are used
- **Links:** [Devpost](https://devpost.com/software/campussync-orcwq3) | [GitHub](https://github.com/tringuye122/CampusSync)

### Ebb  (HackNC 2026)

- **Prizes:** HackNC Beginner - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Smartwatch, iPhone app and website that sense rising stress in children with special needs from movement and room loudness, help them calm down and inform parents and teachers.
- **Problem / user:** Kids with special needs can have meltdowns that caregivers see too late. / children with special needs, parents and teachers
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; web; hardware / True / predictive_ml; llm_chat
- **Stack:** langs Python; frontend Lovable; backend ; db Supabase; hosting 
- **Tech/APIs:** Supabase (database, supporting); Claude (ai_model, supporting); Lovable (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 56 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Compares movement and loudness to the child's own baseline and stores loudness levels only, never audio; spans watch, phone and web surfaces. Page lists Claude, Lovable and Supabase.
- **Team size:** 2 | **Confidence:** medium | unverified: watch hardware model not identified; ai_types inferred
- **Links:** [Devpost](https://devpost.com/software/ebb-36zbl2) | [GitHub](https://github.com/jzps333/ebb)

### Klane  (HackNC 2026)

- **Prizes:** HackNC General - 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** Lead-finding agent for tradespeople that researches public news, permits, procurement notices and announcements to surface upcoming work matched to a trade and territory.
- **Problem / user:** Contractors spend evenings hunting permit portals and notices to find future jobs before they are posted. / small contractors and tradespeople such as roofers
- **Domain / idea type:** productivity_workplace + retail_consumer / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; speech_or_voice
- **Stack:** langs TypeScript; JavaScript; SQL; frontend React; backend Node.js; db PostgreSQL; Snowflake; Tiger Data; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); ElevenLabs (ai_model, supporting); Photon (other, unclear, sponsor); Snowflake (database, unclear, sponsor); Tiger Data / PostgreSQL (database, supporting, sponsor); React (framework, supporting)
- **Sponsor APIs:** Photon; Snowflake; Tiger Data
- **Repo:** public, commits 5 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Bounded batch research with streaming partial results and relevance/currentness filtering; ships a demo-data mode and a live mode; saved profiles; Photon, Snowflake and Tiger Data listed.
- **Team size:** 1 | **Confidence:** medium | unverified: sponsor flags for Photon/Snowflake/Tiger assumed from sponsor tracks; depth of Photon/Snowflake
- **Links:** [Devpost](https://devpost.com/software/klane) | [GitHub](https://github.com/am7t/klane)

### Phish Finder  (HackNC 2026)

- **Prizes:** [Photon] Best iMessage Agent - 2nd Place [2nd]  (tier: sponsor_winner)
- **Pitch:** iMessage agent that opens a forwarded suspicious link in an isolated sandbox, inspects the page, domain, redirects and threat intel, and reports back.
- **Problem / user:** People cannot safely tell whether a suspicious link is a phishing attempt without opening it. / everyday phone users receiving suspicious links
- **Domain / idea type:** safety_security / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; Vite; TanStack Query; backend Node.js; db ; hosting 
- **Tech/APIs:** Photon (other, core, sponsor); Playwright (framework, core); Claude Code (ai_model, supporting); Codex (ai_model, supporting); Zod (framework, token)
- **Sponsor APIs:** Photon | fit: Photon iMessage agent track; the user interacts entirely by forwarding links in iMessage via Photon.
- **Repo:** public, commits 34 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** User never opens the link; a Playwright sandbox visits it and results return over iMessage via Photon. Repo is named Tripwired.
- **Team size:** 3 | **Confidence:** high | unverified: threat-intel sources not read; Claude Code/Codex listed as dev tools
- **Links:** [Devpost](https://devpost.com/software/phish-finder) | [GitHub](https://github.com/Joewuliu/Tripwired)

### Scrub+  (HackNC 2026)

- **Prizes:** HackNC General - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Touchless spatial interface for exploring 3D CT scans with webcam hand gestures and voice, including cutting planes, measurement and surgical-plan comparison.
- **Problem / user:** Surgeons and clinicians need to manipulate medical imaging without touching devices. / surgeons and clinicians viewing CT scans
- **Domain / idea type:** health_wellness / new_category
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; GLSL; frontend Three.js; Vite; WebGL; backend ; db ; hosting Vercel
- **Tech/APIs:** MediaPipe (framework, core); Three.js / WebGL (framework, core); Google Gemini (ai_model, supporting); Google Web Speech API (ai_model, supporting); SciPy (framework, supporting); TotalSegmentator (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 67 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup long, impact claims False
- **Notes:** Solo build; hand tracking and speech run on a laptop webcam with WebGL/GLSL volume rendering. Queue github (TotalSegmentator) is a cited reference; the page's own repo is avidnerd/hack-nc.
- **Team size:** 1 | **Confidence:** high | unverified: TotalSegmentator use depth
- **Links:** [Devpost](https://devpost.com/software/scrub-d67fm5) | [GitHub](https://github.com/avidnerd/hack-nc)

### Speak Up  (HackNC 2026)

- **Prizes:** HackNC Beginner - 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Gamified impromptu-speaking trainer: pick a debate prompt and side, speak aloud, and get a score with targeted feedback.
- **Problem / user:** People need low-pressure practice at making arguments out loud. / students and anyone practicing public speaking or debate
- **Domain / idea type:** education + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat
- **Stack:** langs TypeScript; Python; JavaScript; PL/pgSQL; frontend ; backend ; db PostgreSQL; hosting Fly.io
- **Tech/APIs:** Fly.io (cloud, supporting); PostgreSQL (database, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup short, impact claims False
- **Notes:** Built with help from AI coding agents; distinct visual style; deployed on Fly.io with a Postgres (PL/pgSQL) backend.
- **Team size:** 4 | **Confidence:** medium | unverified: ai_used and ai_types inferred from scoring feedback; model not named
- **Links:** [Devpost](https://devpost.com/software/speak-up-4ofanr)
