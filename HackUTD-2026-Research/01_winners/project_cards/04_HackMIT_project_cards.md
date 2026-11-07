# HackMIT: project cards (35 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackMIT 2024

### Get Away  (HackMIT 2024)

- **Prizes:** First place, "Best Beginner Hack" category [1st]  (tier: track_winner)
- **Pitch:** None
- **Problem / user:** None / None
- **Domain / idea type:** other / other
- **Platforms / hardware / AI:**  / None / None
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots None, writeup None, impact claims None
- **Notes:** No Devpost or Plume page could be located; only the queue prize entry (HackMIT 2024 Best Beginner Hack) is known.
- **Team size:** None | **Confidence:** low | unverified: page_not_found; domain_primary; idea_type; all idea/tech fields; github_url; devpost_url; event dates from memory
- **Links:** [Devpost](None)


## HackMIT 2025

### EyeCraft  (HackMIT 2025)

- **Prizes:** First place, entertainment track [1st]  (tier: track_winner)
- **Pitch:** Minecraft accessibility mod that maps head movement, facial expressions, winks and voice commands to in-game controls for players with severe mobility limits.
- **Problem / user:** Traditional controllers block players with severe mobility or visual impairments from playing games like Minecraft. / gamers with severe mobility impairments
- **Domain / idea type:** accessibility + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / vision; speech_or_voice; predictive_ml
- **Stack:** langs Python; Java; frontend ; backend MediaPipe; OpenCV; JAX; Flax; Fabric API; db ; hosting 
- **Tech/APIs:** MediaPipe (framework, core); OpenCV (framework, core); JAX/Flax expression classifier (ai_model, core); Fabric API (Minecraft modding) (framework, core)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Python vision process runs alongside a Java Fabric mod; JAX/Flax expression classifier plus custom head-movement model; team built no front end; page is on HackMIT's Plume gallery, no Devpost page found.
- **Team size:** 4 | **Confidence:** medium | unverified: github_url; n_screenshots; ui_polish; event dates from memory; duplicate queue prize 'novelty prize check' ignored
- **Links:** [Devpost](None)

### Griddy  (HackMIT 2025)

- **Prizes:** First place, sustainability track (novelty prize check) [1st]; First place, sustainability track [1st]  (tier: track_winner)
- **Pitch:** Hardware-backed power grid orchestrator using an optimization algorithm, ESP32 grid model and iron-air batteries, with a metrics dashboard.
- **Problem / user:** Existing power grid routing is inefficient and renewables lack incentive; team wanted rare-earth-free local storage. / grid operators and infrastructure developers
- **Domain / idea type:** energy_utilities + sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / agent_or_tool_use; predictive_ml
- **Stack:** langs TypeScript; C; Python; C/C++; CSS; frontend Next.js; backend websocket backend; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Next.js (framework, core); Cerebras API (ai_model, supporting, sponsor); Integer linear programming + FFT (other, core)
- **Sponsor APIs:** Cerebras
- **Repo:** public, commits 40 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims True (Claims the routing outperforms the US grid and known private solar grids; one battery powered an LED about 4 hours.)
- **Notes:** Homemade iron-air battery from fertilizer and pencil lead powered an LED for hours; routing runs at 24 Hz using integer linear programming plus FFT demand prediction.
- **Team size:** 3 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; ui_polish; stack_backend
- **Links:** [Devpost](https://plume.hackmit.org/project/kmips-kavlf-auvtc-ymtmn) | [GitHub](https://github.com/Tetraslam/hackmit25)

### Kava  (HackMIT 2025)

- **Prizes:** First place, EigenCloud Sponsor Prize Side Track [1st]; HackMIT EigenCloud Sponsor Prize Side Track (first place) [1st]  (tier: sponsor_winner)
- **Pitch:** AI claims agent that helps wildfire-affected people assemble complete insurance claim packets, auto-fixing gaps and fetching missing receipts.
- **Problem / user:** Wildfire victims lose months to claim rejections caused by scattered, incomplete documentation. / wildfire-affected renters and homeowners
- **Domain / idea type:** fintech_finance + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; vision
- **Stack:** langs TypeScript; Python; CSS; frontend ; backend ; db ; hosting 
- **Tech/APIs:** EigenCloud (cloud, unclear, sponsor); Knot TransactionLink (data_source, core, sponsor); OCR (ai_model, core)
- **Sponsor APIs:** Knot TransactionLink; EigenCloud | fit: Built an AI judge loop (EigenCloud domain-specific judge challenge) and used Knot TransactionLink to auto-fetch missing receipts into claim packets.
- **Repo:** public, commits 2 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Claims scores improve from about 42% to 85%+ through the enhancement loop; no external market numbers.)
- **Notes:** AI judge scores claims against a 47-rule rubric and loops improvements; Knot TransactionLink fetches receipts; output PDF carries a signed proof card.
- **Team size:** None | **Confidence:** medium | unverified: team_size; stack_*; tech_items; event_start; event_end; n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/acarj-euukc-rblna-lfviq) | [GitHub](https://github.com/arav06/kava-hackmit)


## HackMIT 2026

### btw  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: META - 3RD PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI [3rd]  (tier: sponsor_winner)
- **Pitch:** Family game app where members complete shared daily challenges and the family progresses only when everyone responds, nudging calls to parents and grandparents.
- **Problem / user:** Busy students keep postponing calls and messages to distant family; a shared prompt can supply the nudge. / families spanning generations
- **Domain / idea type:** social_community + entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** mobile_cross; web / False / llm_chat; vision; speech_or_voice
- **Stack:** langs TypeScript; frontend React Native; Expo; backend Supabase; db Supabase; hosting Vercel
- **Tech/APIs:** Meta AI model (ai_model, supporting, sponsor); OpenAI (ai_model, token, sponsor); Supabase (database, core); Expo (framework, core); Vercel (cloud, supporting)
- **Sponsor APIs:** Meta; OpenAI | fit: Meta 3rd place; a Meta model analyses family photos, text and voice messages to generate personalized challenge prompts.
- **Repo:** public, commits 304 (before/in/after event: 0/304/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** UI, icons and animations hand-drawn in Procreate; designed to be simple for grandparents; streaks and levels; Meta model used to craft prompts from shared photos, text and voice.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; has_live_demo
- **Links:** [Devpost](https://plume.hackmit.org/project/eelwb-vsngo-fgsei-tovgv) | [GitHub](https://github.com/trishz1230/hackmit-2026)

### Burrow  (HackMIT 2026)

- **Prizes:** WINNER: EDUCATION TRACK WINNER [unknown]  (tier: track_winner)
- **Pitch:** Animated rabbit browser extension that watches the student's page, teaches Socratically without giving answers, and remembers the learner across sessions.
- **Problem / user:** AI tutors are separate tabs that hand over answers and do not track long-term, personalized learning. / students (and parents via a dashboard)
- **Domain / idea type:** education + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** browser_extension; web; hardware / True / llm_chat; agent_or_tool_use; speech_or_voice; vision
- **Stack:** langs TypeScript; HTML; Python; CSS; JavaScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Deepgram (STT/TTS) (ai_model, core, sponsor); OpenAI model (ai_model, core, sponsor); Chrome extension / debugger protocol (framework, core); Raspberry Pi + 7-inch display (hardware_part, supporting)
- **Sponsor APIs:** Deepgram; OpenAI
- **Repo:** public, commits 251 (before/in/after event: 0/251/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Chrome extension runs an observe-decide-act agent loop over about 25 actions; server-side check blocks answer leaks; per-student concept graph; Raspberry Pi display monitors handwritten work.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_languages
- **Links:** [Devpost](https://plume.hackmit.org/project/iecbs-pgvcb-vklxe-bfbtl) | [GitHub](https://github.com/jerryjlwang/Human-eval)

### camp  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: RAMP - 1ST PLACE - SAVE TIME. SAVE MONEY [1st]  (tier: sponsor_winner)
- **Pitch:** Native Mac notch and iPhone Live Activity apps that recommend lunch from preferences and calendar and batch coworkers' orders to split delivery fees.
- **Problem / user:** Ordering food at work means long lines or interruptions, and coworkers ordering from the same place each pay separate delivery fees. / office workers
- **Domain / idea type:** food_nutrition + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** desktop; mobile_ios / False / recommendation; llm_chat; rag_or_search
- **Stack:** langs Swift; Python; frontend AppKit; ActivityKit; backend FastAPI; db ; hosting 
- **Tech/APIs:** Ramp sandbox (payments, supporting, sponsor); OpenAI API (ai_model, supporting, sponsor); FastAPI (framework, core); ActivityKit (framework, core)
- **Sponsor APIs:** Ramp; OpenAI | fit: Ramp 1st; integrates a Ramp sandbox to help manage spending and saves money via shared delivery fees.
- **Repo:** public, commits 62 (before/in/after event: 0/62/0), README solid
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Swift AppKit panel in the Mac notch and ActivityKit Live Activities; recommender works without an LLM key; Ramp sandbox integration; restaurant data simulated since delivery APIs need partner access.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; ui_polish; team_size; stack_database
- **Links:** [Devpost](https://plume.hackmit.org/project/froib-urbmc-nphhn-ugmor) | [GitHub](https://github.com/harryyuncheng/camp)

### CareChair  (HackMIT 2026)

- **Prizes:** WINNER: OVERALL TRACK 3RD PLACE; SPONSOR WINNER: OPENAI - 1ST PLACE - THE FIFTH TEAMMATE; SPONSOR WINNER: DIMENSIONAL - WINNER - BEST USE OF DIMENSIONAL; SPONSOR WINNER: ASUS - 1ST PLACE - ASUS / ZENNI CLAW CHALLENGE [3rd]  (tier: overall_top3)
- **Pitch:** Wheelchair-mounted robotic caregiver with arms, depth vision, voice control and a care dashboard for bathing, feeding and medication help.
- **Problem / user:** Aging and disability need physical care that families and facilities cannot scale, costing independence and money. / elderly and disabled people and their caregivers
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; vision; speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend browser JavaScript; backend Node.js; db ; hosting 
- **Tech/APIs:** Deepgram Nova-3 / Aura-2 (ai_model, core, sponsor); Anvil Robotics arms (hardware_part, core); Intel RealSense D455 (hardware_part, core); MediaPipe (ai_model, core); Arduino (hardware_part, supporting, sponsor); OpenAI (ai_model, supporting, sponsor); Meta AI (ai_model, supporting, sponsor); The Token Company (other, supporting, sponsor); Dimensional (framework, unclear, sponsor); ASUS Ascent GX10 (hardware_part, supporting, sponsor)
- **Sponsor APIs:** Deepgram; Arduino; OpenAI; Meta; The Token Company; Dimensional; ASUS | fit: Used ASUS hardware for local compute, OpenAI for higher-level agent reasoning, and Dimensional-style bounded robot skills for safe actuation.
- **Repo:** public, commits 44 (before/in/after event: 0/44/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Cites aging, disability and caregiver statistics plus annual home-care and nursing-home costs as market context.)
- **Notes:** Two Anvil robotic arms plus RealSense depth camera build a 3D body model via MediaPipe and RANSAC to plan bathing motions; commands are validated before reaching the robots.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/yjrfb-ddfqs-evmsq-zfhgi) | [GitHub](https://github.com/25tyler/Wheelgentic)

### CFO-Sabbatical  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: MAXIMOR AI - 2ND PLACE - OFFICE OF THE CFO AGENT CHALLENGE [2nd]  (tier: sponsor_winner)
- **Pitch:** A system of 15 AI agents handling Office-of-the-CFO work: invoice payment prioritization, debt collection, reconciliation and a 13-week cash forecast.
- **Problem / user:** Finance teams manually triage invoices, chase customer debts, reconcile books and forecast cash. / company finance teams and CFOs
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; Shell; CSS; HTML; frontend ; backend ; db ; hosting Vercel
- **Tech/APIs:** Grok (ai_model, core, sponsor); Stripe (payments, supporting); Gmail (data_source, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** Grok (SpaceXAI) | fit: Built a multi-agent Office of the CFO system (AP, collections, reconciliation, 13-week forecast) matching the Maximor challenge theme.
- **Repo:** public, commits 52 (before/in/after event: 0/52/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Consolidated from 43 agents down to 15; includes an observability harness visualizing agent-to-agent communication; tested on self-made sample invoices; pulls from Gmail and Stripe.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_languages
- **Links:** [Devpost](https://plume.hackmit.org/project/zwjij-edzdv-vmitm-apwhq) | [GitHub](https://github.com/rohan9314/hackmit26)

### ClashMIT  (HackMIT 2026)

- **Prizes:** WINNER: ENTERTAINMENT TRACK WINNER [unknown]  (tier: track_winner)
- **Pitch:** Mobile-browser AR game where players lock cameras onto each other's faces and shout spells like Fireball to battle in real life.
- **Problem / user:** Hackathons keep people glued to laptops; the team wanted a game that gets hackers moving and meeting each other. / hackathon attendees
- **Domain / idea type:** entertainment_games + social_community / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice
- **Stack:** langs JavaScript; frontend Three.js; Web Audio; Web Speech API; backend Node.js; WebSocket; db ; hosting 
- **Tech/APIs:** ONNX Runtime Web (SCRFD, ArcFace) (ai_model, core); Three.js (framework, core); Web Speech API (other, core); WebSocket game server (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 72 (before/in/after event: 0/72/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** On-device face recognition (SCRFD plus ArcFace via ONNX Runtime Web) with a second eyes-only signature; voice-cast spells; live leaderboard on a big screen.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/knges-yhnky-svuti-xmpdm) | [GitHub](https://github.com/spycoderyt/clashmit)

### ClubHub  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: DROPBOX - 2ND PLACE - TURN DIGITAL CHAOS INTO SOMETHING USEFUL [2nd]  (tier: sponsor_winner)
- **Pitch:** Matches students' stated goals to campus clubs in an interactive graph and turns uploaded event posters into structured, up-to-date listings.
- **Problem / user:** Campus club and event info is scattered across posters, PDFs and word of mouth, so students cannot find fitting communities. / university students and student clubs
- **Domain / idea type:** education + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; recommendation; vision
- **Stack:** langs JavaScript; Python; HTML; CSS; SQL; frontend React; Vite; backend FastAPI; db SQLite; ChromaDB; hosting 
- **Tech/APIs:** Claude (ai_model, core); Voyage AI embeddings (ai_model, core); Dropbox (cloud, core, sponsor); ChromaDB (database, core); U of T Student Organization Portal (data_source, supporting)
- **Sponsor APIs:** Dropbox | fit: Dropbox powers the live update flow: club uploads a poster, backend extracts and stores structured event data linked to the source file.
- **Repo:** public, commits 122 (before/in/after event: 0/122/0), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Pulls club data from a University of Toronto portal; Claude extracts event details from posters or PDFs; Voyage embeddings match goals; Dropbox upload flow keeps events fresh with source links.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_languages; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/caruu-rcnjn-yzrse-akiwz) | [GitHub](https://github.com/hdave07/ClubHub)

### DonoRex  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: GIVECAMPUS - 1ST PLACE + GRAND PRIZE - FUNDRAISING / CONSTITUENT INTELLIGENCE CHALLENGE [1st]  (tier: sponsor_winner)
- **Pitch:** Scores alumni donors and builds a ranked weekly outreach queue under a staff time budget, with approval-gated Microsoft 365 drafting.
- **Problem / user:** University fundraisers can only make about 149 contacts a week and choose whom to contact mostly by gut feel. / university advancement and major gift officers
- **Domain / idea type:** productivity_workplace + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs TypeScript; frontend Next.js; backend ; db ; hosting 
- **Tech/APIs:** Next.js (framework, core); Microsoft Graph (M365) (other, supporting); GiveCampus constituent data (data_source, core, sponsor)
- **Sponsor APIs:** GiveCampus data | fit: Built a donor-prioritization engine with explainable weekly action queue directly for the GiveCampus fundraising challenge.
- **Repo:** public, commits 16 (before/in/after event: 0/16/0), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup medium, impact claims True (States about 149 meaningful contacts per 40-hour week and about 20,000 constituents processed.)
- **Notes:** Deterministic scoring and explanations over about 20,000 constituents; Tuesday Autopilot uses Microsoft Graph to draft mail and tasks but stops at human approval; links to a slide deck.
- **Team size:** 2 | **Confidence:** high | unverified: ai_used; n_screenshots; ui_polish; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/cxnvv-kmhmt-hktyj-zuygs) | [GitHub](https://github.com/latoriaa13/HackMIT_Dropbox)

### Elute  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: OPENAI - 2ND PLACE - THE FIFTH TEAMMATE; SPONSOR WINNER: REGENERON - GRAND PRIZE - MAKE CLINICAL TRIALS AND BIOSTATISTICS BETTER! [unknown]  (tier: sponsor_winner)
- **Pitch:** Agentic system that stress-tests drug-disease hypotheses by orchestrating biomedical tools, surfacing weakest links and the next question to answer.
- **Problem / user:** Drug programs can rest on chains of weak or untested assumptions across papers, discovered only after huge spending. / drug development researchers
- **Domain / idea type:** health_wellness + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; CSS; JavaScript; HTML; frontend ; backend ; db ; hosting 
- **Tech/APIs:** OpenAI models (ai_model, core, sponsor); Harvard ToolUniverse (framework, core); Open Targets (data_source, core); ClinicalTrials.gov (data_source, core); PubMed / NCBI E-utilities / Europe PMC (data_source, core)
- **Sponsor APIs:** OpenAI | fit: Orchestrated multi-step biomedical tool calls with a visible reasoning trace for the Regeneron clinical-trials challenge; OpenAI used for extraction and explanation.
- **Repo:** public, commits 35 (before/in/after event: 0/35/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Frames drug programs as costing years and hundreds of millions of dollars; no measured results reported.)
- **Notes:** Uses Harvard ToolUniverse (Open Targets, ClinicalTrials.gov, PubMed) with API fallbacks; deterministic claim-status engine decides evidence, LLM only extracts and explains; supports historical cutoff runs.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_languages; stack_frontend; stack_backend
- **Links:** [Devpost](https://plume.hackmit.org/project/afzbr-ptgza-tcorl-mrobb) | [GitHub](https://github.com/IvanRatushnyy/HackMIT)

### Erbgut  (HackMIT 2026)

- **Prizes:** WINNER: SUSTAINABILITY TRACK WINNER [unknown]  (tier: track_winner)
- **Pitch:** Simulator and tuner for DNA data-storage codecs that measures which coding rules pay off per sequencing channel and learns where decoding fails.
- **Problem / user:** DNA storage relies on generic encoding rules and heavy redundancy that waste lab resources and density across different sequencing methods. / DNA data-storage researchers
- **Domain / idea type:** sustainability_climate + other / data_or_analytics
- **Platforms / hardware / AI:** web / None / predictive_ml
- **Stack:** langs Python; JavaScript; C/C++; C++; HTML; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Fountain code encoder / channel simulator (other, core); CNN decoder corrector (0.8M params) (ai_model, core); Public Nanopore and Illumina datasets (data_source, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 311 (before/in/after event: 0/298/13), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots None, writeup long, impact claims True (Reports Nanopore reads per strand falling from 19.5 to 5.5 and 31 percent more data per DNA letter on Illumina; decoder exact-recovery 88 vs 67 percent.)
- **Notes:** Fountain-code encoder, channel simulator calibrated on two public sequencing datasets, and a classic decoder plus small CNN corrector; reports held-out measurements; says it runs on a microcontroller.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; has_hardware; stack_languages
- **Links:** [Devpost](https://plume.hackmit.org/project/mwrat-butaa-qmvaa-aebuw) | [GitHub](https://github.com/timarnoldev/hackmit2026)

### FRIDAY  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: OPENAI - 3RD PLACE - THE FIFTH TEAMMATE [3rd]  (tier: sponsor_winner)
- **Pitch:** Furniture shopping where the room is the filter: describe or speak what you want and see constraint-checked items placed in a 3D scene.
- **Problem / user:** Product pages ignore your actual space, so shoppers measure by hand and risk returns when furniture does not fit. / furniture shoppers
- **Domain / idea type:** retail_consumer + housing_real_estate / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice; vision
- **Stack:** langs TypeScript; Python; frontend React; Vite; PlayCanvas; three.js; backend Django; db Elasticsearch; hosting 
- **Tech/APIs:** Elasticsearch (database, core, sponsor); Deepgram (ai_model, core, sponsor); Visa sandbox checkout (payments, supporting, sponsor); OpenAI Codex (ai_model, supporting, sponsor); PlayCanvas (framework, core); Gaussian splatting (other, supporting)
- **Sponsor APIs:** Elastic; Deepgram; Visa; OpenAI Codex
- **Repo:** public, commits 386 (before/in/after event: 0/384/2), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Voice requests compile into 13 schema-validated constraint types run against an Elasticsearch catalogue; 5 cm grid solver with rotations; Gaussian-splat room capture; writeup claims 85 PRs and 351 commits via parallel agents.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/fkbzo-xqhff-jgchs-azula) | [GitHub](https://github.com/LeeSinLiang/hackmit2026)

### GPU (Graphics Processing Unit (GPU))  (HackMIT 2026)

- **Prizes:** WINNER: OVERALL TRACK 2ND PLACE [2nd]  (tier: overall_top3)
- **Pitch:** Custom GPU design with warp scheduler and vector lanes on a RISC-V base, run on an FPGA with graphics, physics and LLM demos.
- **Problem / user:** GPUs and RAM are expensive and opaque; team wanted to build and fully understand their own accelerator. / hardware and architecture enthusiasts
- **Domain / idea type:** dev_tools / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / llm_chat
- **Stack:** langs Chisel; C; frontend ; backend ; db ; hosting 
- **Tech/APIs:** FPGA (Vivado) (hardware_part, core); Chisel (framework, core); RISC-V (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 46 (before/in/after event: 0/41/5), README thin
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Chisel-described GPU synthesized with Vivado onto an FPGA at 2.5 GOPS, extends RISC-V with custom parallelism instructions; demos include DOOM, fluid sim and LLM inference.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/xxomh-wwztg-ooipq-hzzbb) | [GitHub](https://github.com/arghunter/gpu)

### Keiko  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: HACKSTER - 2ND PLACE - CREATE WHAT'S NEXT; SPONSOR WINNER: ARDUINO - 1ST PLACE - TOUCH GRASS: BUILD SOMETHING THAT UNDERSTANDS THE REAL WORLD [unknown]  (tier: sponsor_winner)
- **Pitch:** Buoy with a DIY piezo hydrophone and Arduino that streams underwater audio to a cloud model to detect whales and publish sightings.
- **Problem / user:** Most whale deaths come from ship strikes and entanglement, and whale locations are hard to know in time. / marine conservationists and researchers
- **Domain / idea type:** sustainability_climate + other / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / predictive_ml
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Arduino UNO Q 4GB (hardware_part, core, sponsor); Piezo disc transducer hydrophone (hardware_part, core); Custom ensemble audio model (ai_model, core); Watkins / Cornell / Orcasound whale audio datasets (data_source, core)
- **Sponsor APIs:** Arduino | fit: Used an Arduino UNO Q board in a field-style buoy sensing real-world underwater sound for the Arduino real-world challenge.
- **Repo:** public, commits 97 (before/in/after event: 0/97/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims True (States about two-thirds of whale deaths come from human interactions; model AUROC 0.9816 on 5-fold cross-validation.)
- **Notes:** Hydrophone built from piezo disc and custom op-amp; SLA-printed buoy; custom 1D+2D ensemble model with reported AUROC 0.9816; detections written to a public open database.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_frontend; stack_backend; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/hyfdu-oilyy-yixkb-mlauw) | [GitHub](https://github.com/2900xt/keiko-hackMIT)

### Klick  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: META - 1ST PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI; SPONSOR WINNER: ESPRESSIF - WINNER - BEST USE OF ESPRESSIF HARDWARE & SOLUTIONS (IN AIOT) [unknown]  (tier: sponsor_winner)
- **Pitch:** Phone-and-badge system where AI twins of two nearby people negotiate over Bluetooth proximity and both are told when a meeting is worthwhile.
- **Problem / user:** At large events people walk past ideal contacts with no way to know, and networking apps are ignored. / hackathon and event attendees
- **Domain / idea type:** social_community / new_category
- **Platforms / hardware / AI:** mobile_android; hardware; web / True / llm_chat; agent_or_tool_use; speech_or_voice; recommendation
- **Stack:** langs Kotlin; TypeScript; C; frontend Jetpack Compose; LVGL; backend Firebase Cloud Functions v2; db Firestore; hosting Firebase
- **Tech/APIs:** Meta Muse Spark (Meta Model API) (ai_model, core, sponsor); ESP32-S3-BOX-3 / Waveshare ESP32-S3 AMOLED (hardware_part, core, sponsor); Deepgram STT/TTS (ai_model, supporting, sponsor); Firebase (Firestore, Functions, FCM) (cloud, core); Bluetooth LE (other, core)
- **Sponsor APIs:** Meta Muse Spark; Espressif ESP32-S3; Deepgram | fit: Twin-to-twin negotiation on Meta Muse Spark to connect nearby people, plus ESP-IDF firmware on ESP32-S3 badges for the Espressif AIoT prize.
- **Repo:** public, commits 88 (before/in/after event: 0/88/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Android BLE advertise-and-scan with 8-byte tokens; twin conversation on Meta Muse Spark via Anthropic SDK pointed at Meta API; ESP32-S3 lanyard badges change colour on a match; BLE direction guessed via body shielding.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/rwqwq-hqecj-bfxns-lyqyc) | [GitHub](https://github.com/dylankainth/blades/)

### Lil-Vro Model  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: HACKSTER - 3RD PLACE - CREATE WHAT'S NEXT [3rd]  (tier: sponsor_winner)
- **Pitch:** Voice-only Socratic study buddy for kids 8-14 that runs on an ESP32-S3-BOX-3, with a parent dashboard of streaks and mastery.
- **Problem / user:** Kids copy chatbot answers or get distracted by screens instead of reasoning through homework themselves. / children aged 8 to 14 and their parents
- **Domain / idea type:** education + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / llm_chat; speech_or_voice; recommendation
- **Stack:** langs Python; TypeScript; frontend Next.js 15; React 19; Tailwind; backend Python; db Supabase Postgres; hosting 
- **Tech/APIs:** OpenAI model and TTS (ai_model, core, sponsor); Deepgram (ai_model, core, sponsor); faster-whisper (ai_model, core); ESP32-S3-BOX-3 (hardware_part, core, sponsor); Supabase (database, core)
- **Sponsor APIs:** OpenAI; Deepgram; Espressif ESP32-S3
- **Repo:** public, commits 82 (before/in/after event: 0/79/3), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Custom 99-symbol spoken-math normalizer and math-to-speech renderer; local faster-whisper; fail-closed kid-safety filter; three tutoring modes including hidden-error mistake mode; BOX-3 streams 16 kHz audio over Wi-Fi.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/teywu-cadwe-dcfzg-zgcgt) | [GitHub](https://github.com/Chaitanya-purohit/lilvro)

### MathMatch  (HackMIT 2026)

- **Prizes:** WINNER: BEGINNER TRACK WINNER [unknown]  (tier: track_winner)
- **Pitch:** Gamified proof-based math app with a swipe feed and timed 1v1 duels where solutions are typed or spoken and AI-graded, with ELO ratings.
- **Problem / user:** Students lean on AI for answers and lose math reasoning; the team wanted rigor-focused, competitive proof practice. / students practicing competition-style math
- **Domain / idea type:** education + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; recommendation
- **Stack:** langs TypeScript; Python; CSS; frontend ; backend ; db ; hosting Vercel
- **Tech/APIs:** Devin (ai_model, core, sponsor); OpenAI models (grading) (ai_model, core, sponsor); Deepgram (ai_model, supporting, sponsor); AMC/AIME/USAMO benchmark dataset (data_source, core); Vercel (cloud, supporting)
- **Sponsor APIs:** Cognition Devin; OpenAI; Deepgram
- **Repo:** public, commits 115 (before/in/after event: 0/115/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims True (Cites a UCSD study that 1 in 8 students lack basic high school math proficiency.)
- **Notes:** Per-topic ELO ratings for users and problems; grading rewards methodology over answers; spoken proofs via speech-to-text; app largely built by Devin agents; uses AMC/AIME/USAMO problem set.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_languages
- **Links:** [Devpost](https://plume.hackmit.org/project/givtb-jfvaz-amjmc-dtcuf) | [GitHub](https://github.com/BoomydayCoder/HackMIT-2)

### Memory Palace  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: META - 2ND PLACE - BRINGING PEOPLE CLOSER TOGETHER WITH AI [2nd]  (tier: sponsor_winner)
- **Pitch:** EEG spike detection triggers 30-second camera captures that are described by Muse Spark, indexed in Elastic and searchable with an agent.
- **Problem / user:** People lose track of confusing or notable moments, and dementia care relies on hand-assembled memory cues. / general users, dementia patients and their caregivers
- **Domain / idea type:** health_wellness + mental_health / new_category
- **Platforms / hardware / AI:** web; mobile_android; hardware / True / vision; rag_or_search; agent_or_tool_use; predictive_ml; llm_chat
- **Stack:** langs Python; frontend Next.js; React; backend Python; db ; hosting 
- **Tech/APIs:** Meta Muse Spark (ai_model, core, sponsor); Elastic (BM25 + vector, Inference Service) (database, core, sponsor); Jina v5 Omni embeddings (ai_model, core); Grok (Memory Guard option) (ai_model, supporting); Emotiv EPOC X EEG (hardware_part, core); ESP camera module (hardware_part, core, sponsor)
- **Sponsor APIs:** Meta Muse Spark; Elastic | fit: Muse Spark describes captured clips and an agent plus Elastic search returns them as evidence, framed as bringing people closer via shared moments.
- **Repo:** public, commits 39 (before/in/after event: 0/39/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Spike detector adapts per user with a 30-second baseline calibration; capture rig is an ESP camera and Android phone since Meta glasses were not obtained; hybrid BM25 plus Jina vector retrieval in Elastic.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/ekkeo-uldro-ffuzo-fsegk) | [GitHub](https://github.com/NamaiBest/MemoryPalace)

### Money Maxer  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: RAMP - 3RD PLACE - SAVE TIME. SAVE MONEY; SPONSOR WINNER: MAXIMOR AI - 4TH PLACE - OFFICE OF THE CFO AGENT CHALLENGE [unknown]  (tier: sponsor_winner)
- **Pitch:** Agent finance team that investigates payment discrepancies, gathers evidence across systems, asks humans when stuck, and posts verified accounting entries.
- **Problem / user:** Finance staff spend time investigating short payments and missing context before books can be closed. / finance teams and CFO offices
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml; rag_or_search
- **Stack:** langs TypeScript; frontend ; backend ; db SQLite; hosting 
- **Tech/APIs:** Claude Agent SDK (ai_model, core); SQLite ledger (database, core); Gmail / Slack / CRM connectors (data_source, supporting); QuickBooks mirroring (other, supporting); ASUS GX10 (LoRA fine-tune) (hardware_part, supporting, sponsor)
- **Sponsor APIs:** ASUS GX10 | fit: Built an office-of-the-CFO agent system with verification and memory for the Maximor challenge; also targeted Ramp save-time-save-money theme.
- **Repo:** public, commits 241 (before/in/after event: 0/239/2), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Reports fine-tuned reader at 0.972 field F1 vs 0.958 and 70.0% vs 66.7% exact match against Claude on own benchmark.)
- **Notes:** Deterministic verification gate before posting; scoped, expiring human-answer memory; historical replay turns decisions into backtested rules; LoRA-tuned document reader on an ASUS GX10 reports 0.972 field F1 versus 0.958 for Claude.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_frontend; stack_hosting
- **Links:** [Devpost](https://plume.hackmit.org/project/nlhtb-gqmiu-yvcyw-pibeg) | [GitHub](https://github.com/AthM23/money-maxing)

### Newton's Playground  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: ASUS - 3RD PLACE - ASUS / ZENNI CLAW CHALLENGE [3rd]  (tier: sponsor_winner)
- **Pitch:** Offline physics tutor rig: photograph a textbook problem, watch it simulate, then grab and throw objects with hand tracking.
- **Problem / user:** Intro physics uses static diagrams and mouse input, which builds little physical intuition. / intro physics students
- **Domain / idea type:** education / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; llm_chat; speech_or_voice; rag_or_search
- **Stack:** langs TypeScript; Python; frontend Vite; Matter.js; KaTeX; backend Python service; Ollama; db ; hosting 
- **Tech/APIs:** ASUS Ascent GX10 (hardware_part, core, sponsor); Ollama (local qwen and nemotron models) (ai_model, core); MediaPipe hand tracking (ai_model, core); Deepgram STT (ai_model, supporting, sponsor); ESP32-S3 + NeoPixel ring (MQTT) (hardware_part, supporting, sponsor); Matter.js (framework, core); OpenStax University Physics (BM25 index) (data_source, supporting)
- **Sponsor APIs:** ASUS GX10; Deepgram; Espressif ESP32-S3 | fit: Ran all models on the ASUS Ascent GX10 so the full photo-to-simulation demo works offline except speech-to-text.
- **Repo:** public, commits 69 (before/in/after event: 0/69/0), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims True (Reports simulation agreement with closed-form derivations within 0.58 percent and structured generation sped from 31 s to 5.5 s.)
- **Notes:** All models run locally on an ASUS Ascent GX10 via Ollama; two-display setup; MediaPipe hand tracking drives launch velocity; ESP32-S3 NeoPixel ring light over MQTT; physics checked against closed-form solutions to 0.58%.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/khvue-bewru-gqjrh-xgwpv) | [GitHub](https://github.com/ethannsie/hackMIT26.git)

### nullMap  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: ELASTIC - 2ND PLACE - FIND THE SIGNAL [2nd]  (tier: sponsor_winner)
- **Pitch:** Search tool that takes a research proposal, finds similar past papers and trials including null results, and shows stats, a topic map and funnel plots.
- **Problem / user:** Null results are underreported, causing publication bias, wasted lab effort and painful literature review. / medical researchers
- **Domain / idea type:** health_wellness + dev_tools / data_or_analytics
- **Platforms / hardware / AI:** web / False / rag_or_search; llm_chat
- **Stack:** langs Python; frontend ; backend Elasticsearch; Docker; db Elasticsearch; hosting Vercel; AWS EC2
- **Tech/APIs:** Elastic Cloud / Elasticsearch (database, core, sponsor); OpenAlex (data_source, core); ClinicalTrials.gov (data_source, core); AWS EC2 (cloud, supporting, sponsor); Cursor (other, supporting, sponsor); Devin (ai_model, supporting, sponsor); Vercel (cloud, supporting)
- **Sponsor APIs:** Elastic; Voloridge EC2; Devin; Cursor | fit: Elastic 2nd; used Elastic Cloud with Elasticsearch to store and vector-search embedded paper titles and abstracts.
- **Repo:** public, commits 129 (before/in/after event: 0/129/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots None, writeup long, impact claims True (Says the circulatory and renal subset has about 2 million records; publication bias causes large wasted spending.)
- **Notes:** Subset of OpenAlex and ClinicalTrials.gov (renal and circulatory) indexed in Elastic Cloud with vector search; LLM classifies each report's outcome as positive, negative or null; first hackathon for the team.
- **Team size:** None | **Confidence:** high | unverified: n_screenshots; ui_polish; team_size; demo_video_url; platforms
- **Links:** [Devpost](https://plume.hackmit.org/project/cuqqq-zpzje-qzyls-tmbjd) | [GitHub](https://github.com/conrad204/NullMap/tree/main)

### Paw Patrol  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: ASUS - 2ND PLACE - ASUS / ZENNI CLAW CHALLENGE [2nd]  (tier: sponsor_winner)
- **Pitch:** Streams police officers' live video, audio and heart rate to dispatch and hospital dashboards with AI analysis that issues alerts and suspect details.
- **Problem / user:** Officers under threat must radio dispatch manually, delaying communication with dispatch and emergency medical responders. / police officers, dispatchers and emergency healthcare responders
- **Domain / idea type:** safety_security + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_ios / True / vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Mapbox; Three.js; CSS Modules; backend Next.js API routes; FastAPI; WebRTC; db SQLite; Vercel Blob; hosting Vercel
- **Tech/APIs:** YOLO (ai_model, core); Whisper (ai_model, core); OpenAI / Claude / Ollama (ai_model, supporting, sponsor); Mapbox (maps_geo, supporting); Apple Watch heart rate (hardware_part, core); Vercel (cloud, supporting)
- **Sponsor APIs:** OpenAI
- **Repo:** public, commits 139 (before/in/after event: 0/137/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup medium, impact claims False
- **Notes:** Planned custom hardware was dropped due to shipping delays; used iPhone and Apple Watch instead; YOLO and Whisper pipeline with LLM transcript assessment for human review; three dashboards.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/zznsi-rdjii-twguh-prtfz) | [GitHub](https://github.com/alex-nyan/hackmit_2026)

### Peel - The tiny lab technician  (HackMIT 2026)

- **Prizes:** WINNER: OVERALL TRACK 1ST PLACE; SPONSOR WINNER: ELASTIC - 1ST PLACE - FIND THE SIGNAL [1st]  (tier: overall_top3)
- **Pitch:** Phone-connected low-cost optical dissolution tester paired with an AI evidence engine to check whether a medicine is genuine.
- **Problem / user:** Counterfeit and substandard medicines are common, and real lab dissolution tests are expensive and distant. / pharmacists, clinics and NGOs in low-resource settings
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** mobile_android; hardware; web / True / vision; rag_or_search; agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs Dart; Python; frontend Flutter; Rive; three.js; backend FastAPI; db Elasticsearch; hosting Runpod; Elastic Cloud Serverless
- **Tech/APIs:** Elasticsearch / Agent Builder (database, core, sponsor); ESP32-S3 / ESP32-S3-BOX-3 (hardware_part, core, sponsor); Deepgram Voice Agent (ai_model, supporting, sponsor); Devin (other, supporting, sponsor); Firecrawl (data_source, supporting); Arduino (framework, core, sponsor); Flutter (framework, core); Runpod (cloud, supporting); openFDA / NDC / RxNav (data_source, core)
- **Sponsor APIs:** Elastic; Espressif; Deepgram; Cognition Devin; Arduino | fit: Elasticsearch served as the entire database with hybrid semantic search and an Agent Builder agent over regulator recall data.
- **Repo:** public, commits 99 (before/in/after event: 0/99/0), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims True (Cites 100,000 yearly antimalarial deaths and 1 in 10 substandard products; device about $100 in parts; 22k recalls, 84k pills indexed.)
- **Notes:** ESP32-S3 rig with six LEDs and two light sensors streams to a Flutter Android app; Elasticsearch holds about 245k recall, product and pill documents; Devin built the app.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/qxodw-wgjqk-lidau-dxrpe) | [GitHub](https://github.com/viktorinkov/HackMIT-2026)

### Recall  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: DROPBOX - 1ST PLACE - TURN DIGITAL CHAOS INTO SOMETHING USEFUL [1st]  (tier: sponsor_winner)
- **Pitch:** Voice companion phones people with dementia for gentle reminiscence-based recall sessions and builds a family-visible memory graph of people, events and memories.
- **Problem / user:** People with dementia lose memories and families lose shared history; reminiscence therapy is expensive and not proactive or longitudinal. / people with dementia and their families
- **Domain / idea type:** health_wellness + mental_health / new_category
- **Platforms / hardware / AI:** web / False / speech_or_voice; llm_chat; rag_or_search; vision
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; backend Next.js; db SQLite; LadybugDB; hosting Railway
- **Tech/APIs:** Deepgram (ai_model, core, sponsor); OpenAI (ai_model, supporting, sponsor); Meta Muse Spark (ai_model, supporting, sponsor); LadybugDB (database, core); SQLite (database, core); Linq iMessage (telecom, supporting); Vitest (framework, supporting)
- **Sponsor APIs:** Deepgram; OpenAI; Meta Muse Spark | fit: Dropbox track win; the writeup describes uploaded family photo collections organized into the memory graph, with no Dropbox API named.
- **Repo:** public, commits 92 (before/in/after event: 0/92/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Conversation state machine requires confirmation before saving words; graph keeps relatives' accounts separate from the patient's confirmed memories; iMessage via Linq; sessions grounded in reminiscence-therapy research.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://plume.hackmit.org/project/cocds-fxbwj-czmjd-uzpbs) | [GitHub](https://github.com/jeffreyzhou-harvard/Recall)

### Rumi  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: RAMP - 2ND PLACE - SAVE TIME. SAVE MONEY [2nd]; SPONSOR WINNER: LONG LAKE - WINNER - CONVINCE A NON-BELIEVER [unknown]  (tier: sponsor_winner)
- **Pitch:** AI interior design shopping agent that scans a room with LiDAR, takes taste and budget, and fills an editable 3D plan with real purchasable products.
- **Problem / user:** Furnishing a room piecemeal means items fit alone but not together, and measuring, layout and budgeting are done in isolation. / renters and students furnishing a room on a budget
- **Domain / idea type:** retail_consumer + housing_real_estate / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_ios / False / agent_or_tool_use; vision; llm_chat; rag_or_search; generative_media
- **Stack:** langs TypeScript; Swift; frontend React; React Three Fiber; Drei; backend Convex; db Convex; hosting 
- **Tech/APIs:** Apple RoomPlan (hardware_part, core); React Three Fiber (framework, core); Convex (database, core); Clerk (auth, supporting); Exa (data_source, core); OpenAI (ai_model, core, sponsor); Zod (framework, supporting); Devin (ai_model, supporting, sponsor); Codex (ai_model, supporting, sponsor)
- **Sponsor APIs:** OpenAI; Devin | fit: Ramp 2nd (save time/money) and Long Lake wins; the budget-constrained shopping plan fits the Ramp theme, but no Ramp API is named in the writeup.
- **Repo:** public, commits 169 (before/in/after event: 0/106/63), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** iOS app uses Apple RoomPlan LiDAR scan transferred to a browser 3D editor; budget math, collisions and placement enforced by deterministic code with tests; listed vs estimated dimensions kept distinct. Demo video is a Drive link plus YouTube.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; sponsor_fit_note; has_live_demo
- **Links:** [Devpost](https://plume.hackmit.org/project/aajnp-oqnis-ttafi-kbgks) | [GitHub](https://github.com/IBS27/rumi)

### Scenar.io  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: ELEVENLABS - 3RD PLACE - ELEVENLABS CHALLENGE [3rd]  (tier: sponsor_winner)
- **Pitch:** Language-learning game where you walk through an AI-generated 3D world and speak with voiced NPCs toward goals generated from your own scenario prompt.
- **Problem / user:** Classroom language study teaches translation but not live conversation, so learners freeze when they must answer on the spot. / language learners
- **Domain / idea type:** education + entertainment_games / new_category
- **Platforms / hardware / AI:** desktop / False / speech_or_voice; llm_chat; generative_media; agent_or_tool_use
- **Stack:** langs C#; Python; frontend Unity; backend FastAPI; db ; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, core, sponsor); World Labs (ai_model, core); Nano Banana (ai_model, supporting); OpenAI Responses API (ai_model, core, sponsor); Unity (framework, core); FastAPI (framework, core); Microsoft Rocketbox (other, supporting)
- **Sponsor APIs:** ElevenLabs; OpenAI | fit: ElevenLabs speech-to-text and text-to-speech drive the spoken conversation with characters and on-screen subtitles.
- **Repo:** public, commits 64 (before/in/after event: 0/63/1), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Reference image from Nano Banana expanded into a World Labs Gaussian-splat world inside Unity; scenarios generated via OpenAI structured outputs; two-way ElevenLabs voice with lip-sync and subtitles.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; platforms
- **Links:** [Devpost](https://plume.hackmit.org/project/rpbsx-etzty-tttwk-fhnlt) | [GitHub](https://github.com/ZackMurry/hackmit-2026)

### Sherlock  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: MAXIMOR AI - 3RD PLACE - OFFICE OF THE CFO AGENT CHALLENGE [3rd]  (tier: sponsor_winner)
- **Pitch:** Multi-agent AI finance office of 22 roles that investigates uploaded financial records, reconciles transactions and produces evidence-linked reports with human review.
- **Problem / user:** Financial records are scattered across spreadsheets and systems, so discrepancies go unnoticed until audit; school boards often fail audits. / finance teams, school districts
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; rag_or_search; vision
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; LangGraph; db SQLite; hosting 
- **Tech/APIs:** LangGraph (framework, core); OpenAI (ai_model, core, sponsor); Supabase (auth, supporting); SQLite (database, core); Fine-tuned local extraction model (ai_model, supporting); FastAPI (framework, core)
- **Sponsor APIs:** OpenAI | fit: Built an AI office-of-the-CFO with Treasury, Controllership, FP&A and Audit leads, matching Maximor's challenge theme.
- **Repo:** public, commits 230 (before/in/after event: 0/230/0), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims False
- **Notes:** Exact-cents deterministic accounting code separated from LLM reasoning; LangGraph checkpoints let investigations pause for human answers; human decisions become precedents rechecked later; local fine-tuned model for document extraction.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; sponsor_fit_note
- **Links:** [Devpost](https://plume.hackmit.org/project/cxwit-mchwb-zrdld-pegqj) | [GitHub](https://github.com/Nityasav/hackmit)

### SignalHound  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: HACKSTER - 1ST PLACE - CREATE WHAT'S NEXT [1st]  (tier: sponsor_winner)
- **Pitch:** Unitree Go2 robot dog finds a person by climbing Bluetooth signal strength measured by a Nordic nRF7002-DK, with no camera, map or GPS.
- **Problem / user:** Finding people by camera fails around corners and occlusions, while phones already broadcast Bluetooth that could guide search. / search-and-rescue and pet-tracking use cases
- **Domain / idea type:** safety_security + telecom_networking / hardware_gadget
- **Platforms / hardware / AI:** hardware; cli / True / other
- **Stack:** langs Python; C; frontend ; backend Zephyr; bleak; db ; hosting 
- **Tech/APIs:** Nordic nRF7002-DK (hardware_part, core, sponsor); Unitree Go2 (hardware_part, core); Zephyr RTOS (framework, core); bleak (framework, supporting); Unitree WebRTC (other, core)
- **Sponsor APIs:** Nordic nRF7002-DK | fit: Hackster win; a Nordic DK acts as the actual sensor on the robot dog, running untethered on a power bank.
- **Repo:** public, commits 31 (before/in/after event: 0/30/1), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Direction inferred by stepping and re-measuring RSSI, fitting a gradient plane; built a 2D radio simulator with multipath to tune; safety layer caps speed; BLE rebroadcast from DK avoids cables. Latest run closed in at -51 dBm.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; ui_polish; ai_used; ai_types; sponsor_apis_used; team_size
- **Links:** [Devpost](https://plume.hackmit.org/project/osnma-ymnqm-azajt-sywdc) | [GitHub](https://github.com/ary4nraj/hackmit)

### Spidey Sense  (HackMIT 2026)

- **Prizes:** WINNER: HEALTHCARE TRACK WINNER [unknown]  (tier: track_winner)
- **Pitch:** Four-microphone array and head-tracking hat that plays only the person you face, while still alerting on your name or alarms.
- **Problem / user:** Deaf, hard-of-hearing and ADHD users struggle to isolate one voice in loud rooms; hearing aids amplify everything. / deaf, hard-of-hearing and ADHD listeners
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** desktop; hardware; web / True / speech_or_voice; llm_chat; predictive_ml
- **Stack:** langs Python; Rust; MicroPython; JavaScript; frontend vanilla JS; d3; backend Python http.server; server-sent events; db ; hosting 
- **Tech/APIs:** faster-whisper (ai_model, core); DeepFilterNet3 (ai_model, core); ESP32-S3 + Arduino Modulino Movement (hardware_part, core, sponsor); Zoom AMS-44 USB interface and 4 mics (hardware_part, core); Claude CLI (summaries) (ai_model, supporting); pyannote / ReDimNet2 diarizer (ai_model, supporting); Higgs Audio v3 (ai_model, supporting)
- **Sponsor APIs:** Espressif ESP32-S3; Arduino Modulino
- **Repo:** public, commits 4 (before/in/after event: 0/0/4), README detailed
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims True (Reports measured separation up to 18 dB between voices, bearing error 1-5 degrees, and 14.7 percent diarization error on AMI.)
- **Notes:** Mic geometry calibrated with sound; SRP-PHAT direction finding with MVDR beamformer, per-bin mask and DeepFilterNet; IMU hat on ESP32-S3; everything runs offline on one laptop.
- **Team size:** 2 | **Confidence:** high | unverified: n_screenshots; ui_polish
- **Links:** [Devpost](https://plume.hackmit.org/project/bvbun-rvjwe-dwtmj-ljtag) | [GitHub](https://github.com/tomasdavola/spideysense)

### Stewardship Sam  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: GIVECAMPUS - 2ND PLACE + MOST PRODUCTION READY - FUNDRAISING / CONSTITUENT INTELLIGENCE CHALLENGE [2nd]  (tier: sponsor_winner)
- **Pitch:** Relationship-intelligence agent for GiveCampus fundraisers that builds a graph of donor communities and surfaces who needs attention and why.
- **Problem / user:** CRMs flatten alumni and donors into rows, hiding the clubs and communities that connect them and signals like lapsed thanks or contact fatigue. / university advancement and fundraising teams
- **Domain / idea type:** productivity_workplace + social_community / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; React; backend FastAPI; db ; hosting 
- **Tech/APIs:** NetworkX (framework, core); OpenAI (ai_model, supporting, sponsor); pandas (framework, supporting); GiveCampus dataset (data_source, core, sponsor); FastAPI (framework, core)
- **Sponsor APIs:** GiveCampus dataset | fit: Built on GiveCampus's provided constituent dataset (gifts, interactions, affiliations, events), addressing its fundraising/constituent intelligence challenge; also won Most Production Ready.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots None, writeup long, impact claims False
- **Notes:** Solo build; six relationship use cases derived from exploring the sponsor dataset; NetworkX community graph plus deterministic signal detection, with OpenAI only for explanations and natural-language questions.
- **Team size:** 1 | **Confidence:** high | unverified: n_screenshots; ui_polish; repo_clone_failed
- **Links:** [Devpost](https://plume.hackmit.org/project/alqmf-ljbou-vlpzr-ujkfk) | [GitHub](https://github.com/marcosarnold/stewardship-sam)

### The PenPal  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: ARDUINO - 2ND PLACE - TOUCH GRASS: BUILD SOMETHING THAT UNDERSTANDS THE REAL WORLD [2nd]  (tier: sponsor_winner)
- **Pitch:** Camera and MediaPipe hand tracking detects when a child is struggling to write, with a pulse oximeter stress signal, streaming to a teacher dashboard.
- **Problem / user:** Children who stay silent when struggling, such as with selective mutism, get delayed help because teachers miss non-verbal signs of distress. / children with neurodevelopmental difficulties and their teachers
- **Domain / idea type:** education + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision; predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; backend Python; WebSocket; db Firebase; hosting Firebase
- **Tech/APIs:** MediaPipe (ai_model, core); OpenCV (framework, core); Arduino pulse oximeter (hardware_part, core, sponsor); Firebase (database, supporting); WebSockets (framework, core)
- **Sponsor APIs:** Arduino | fit: Arduino-connected pulse and oximetry sensing was used to detect stress alongside the camera pipeline (Touch Grass real-world theme).
- **Repo:** public, commits 39 (before/in/after event: 0/39/0), README solid
- **Demo/writeup:** video True, live none, screenshots None, writeup medium, impact claims False
- **Notes:** Planned IMU unavailable so team pivoted to phone camera plus Arduino pulse oximeter; collected own baseline-vs-stress readings to train a calm/stressed model; 21 hand landmarks analysed for stalls and posture.
- **Team size:** 4 | **Confidence:** high | unverified: n_screenshots; ui_polish; stack_hosting; stack_languages
- **Links:** [Devpost](https://plume.hackmit.org/project/gxcea-qehmz-xnldy-yifsj) | [GitHub](https://github.com/sabrasX/hackmit2026-4s)

### VistaAI  (HackMIT 2026)

- **Prizes:** SPONSOR WINNER: MAXIMOR AI - 1ST PLACE - OFFICE OF THE CFO AGENT CHALLENGE [1st]  (tier: sponsor_winner)
- **Pitch:** AI-native operating layer that ingests messy data from acquired companies into a shared backend and surfaces evidence-backed integration opportunities for PE roll-ups.
- **Problem / user:** Acquired portfolio companies have fragmented systems and manual workflows, making integration and back-office consolidation slow and spreadsheet-driven. / private equity firms and portfolio operators
- **Domain / idea type:** fintech_finance + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend ; backend FastAPI; db Postgres; hosting AWS
- **Tech/APIs:** FastAPI (framework, core); Postgres (database, core); AWS object storage (cloud, supporting)
- **Sponsor APIs:**  | fit: Maximor 1st; cross-company finance and operations data standardized into records with traceable calculations, matching the office-of-the-CFO agent theme.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots None, writeup long, impact claims False
- **Notes:** Schema detection and field-mapping proposals with human review of ambiguous cases; provenance back to file and row; AI interpretation separated from deterministic calculations; multi-tenant Postgres on AWS.
- **Team size:** 3 | **Confidence:** high | unverified: n_screenshots; ui_polish; live_demo_url; ai_types; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://plume.hackmit.org/project/cslzr-pathl-qrbxv-xahcq) | [GitHub](https://github.com/emiliano800/vista)
