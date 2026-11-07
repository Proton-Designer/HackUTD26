# SunHacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## SunHacks 2024

### LockItUp  (SunHacks 2024)

- **Prizes:** Winner State Farm - Best Hack for Social Good [unknown]  (tier: sponsor_winner)
- **Pitch:** QR-enabled bike lock built into bike stands for campus, with an Arduino stepper-motor prototype and an AWS-backed web app.
- **Problem / user:** Bikes are frequently stolen on the ASU campus and students lack a convenient secure locking option. / university students who bike
- **Domain / idea type:** safety_security + mobility_transport / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs Python; frontend ; backend Django; AWS CDK; db DynamoDB; hosting AWS EC2
- **Tech/APIs:** Arduino 101 with stepper motor (hardware_part, core); AWS EC2 (cloud, supporting); AWS SQS (cloud, supporting); DynamoDB (database, supporting); Django (framework, supporting)
- **Sponsor APIs:**  | fit: Won State Farm's Best Hack for Social Good with a campus bike-theft prevention lock prototype; no State Farm API or dataset is mentioned.
- **Repo:** public, commits 9 (before/in/after event: 0/9/0), README thin
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Proof-of-concept built from scrap material; switched from Raspberry Pi to Arduino 101 after power problems; AWS SQS used for inter-process messaging.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/lockitup) | [GitHub](https://github.com/risratna/lockitup)


## SunHacks 2025

### Crises.ai  (SunHacks 2025)

- **Prizes:** Winner State Farm - Best Hack for Safety [unknown]  (tier: sponsor_winner)
- **Pitch:** Insurance-carrier disaster dashboard that merges live quake, wildfire, FEMA, 911 and social-chatter feeds into one map with claim forecasts and customer exposure overlays.
- **Problem / user:** Carriers struggle to unify disaster intelligence fast enough to protect policyholders. / insurance carriers and claims teams
- **Domain / idea type:** safety_security + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js; Tailwind CSS; backend Node.js; Socket.IO; Drizzle; db Postgres; hosting 
- **Tech/APIs:** Gemini (ai_model, supporting); USGS earthquake feed (data_source, core); NASA FIRMS (data_source, core); FEMA declarations (data_source, core); Kontur hazards (data_source, supporting); Next.js (framework, supporting); Socket.IO (framework, supporting)
- **Sponsor APIs:**  | fit: Won State Farm's Best Hack for Safety with an insurer-facing disaster-monitoring and claim-forecast map built from public hazard feeds; no State Farm API or dataset is mentioned.
- **Repo:** public, commits 25 (before/in/after event: 0/21/4), README solid
- **Demo/writeup:** video False, live none, screenshots 10, writeup short, impact claims False
- **Notes:** Integrates USGS, NASA FIRMS, FEMA, Kontur and 911 clusters with Gemini-scored social posts; customer-density polygons over 18+ metros use seeded persona data.
- **Team size:** 3 | **Confidence:** high | unverified: writeup_sections; demo_video_url
- **Links:** [Devpost](https://devpost.com/software/crises-ai) | [GitHub](https://github.com/SankrityaT/Crises.ai)
