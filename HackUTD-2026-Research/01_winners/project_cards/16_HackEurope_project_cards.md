# HackEurope: project cards (1 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackEurope 2026

### ZeroStrike  (HackEurope 2026)

- **Prizes:** Overall winner / top prize (per TCD article; which city not stated) [unknown]; HackEurope: Grand Winner (hackeurope.com testimonial; Julian Lewandowski's site: Overall winner, HackEurope 2026) [unknown]  (tier: overall_top3)
- **Pitch:** Platform predicting dry-lightning wildfire risk and using Claude agents to dispatch a DJI drone that releases cloud-seeding payload over threatened terrain.
- **Problem / user:** Dry lightning ignites many wildfires while response budgets shrink and firefighters arrive late; team wants prevention before ignition. / wildfire agencies and emergency planners
- **Domain / idea type:** sustainability_climate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_android; hardware / True / agent_or_tool_use; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; Tailwind; Mapbox GL; backend Flask; Firebase Cloud Functions; db Firestore; hosting Firebase
- **Tech/APIs:** Claude API (ai_model, core); XGBoost (ai_model, core); ERA5 reanalysis (data_source, core); NASA / ESA data (data_source, supporting); DJI Mobile SDK v5 (hardware_part, core); ESP32 (hardware_part, core); Firestore (database, core); Mapbox GL (maps_geo, core)
- **Sponsor APIs:** 
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video None, live not_checked, screenshots 6, writeup long, impact claims True (Cites 225 billion euro wildfire damage and a cut in EU wildfire response budget from 1.7 to 1.2 billion euro.)
- **Notes:** XGBoost trained on 28,000 ignitions with ERA5 data; 6-hour storm-cell projection; custom Android app over DJI MSDK v5 plus ESP32 servo payload; Firestore as cross-network command bus; Devpost shows no Winner badge.
- **Team size:** 4 | **Confidence:** medium | unverified: github_url (page lists a repo but URL not captured); tech_items.is_sponsor; HackEurope city; Claude API listed as built-with; sponsor status unknown; winner status from TCD article and queue, not Devpost badge; demo_video_url; has_demo_video
- **Links:** [Devpost](https://devpost.com/software/zerostrike)
