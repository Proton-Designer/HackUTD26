# HackTX: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2026

### ARcher  (2026)

- **Prizes:** [Best Hardware Hack] Brick House (prize: Nvidia 5080 per member; NVIDIA is the prize, not a confirmed sponsor challenge) [unknown]  (tier: sponsor_winner)
- **Pitch:** iPhone AR tower-defense game where players place a castle in their room and draw and release a bow using a custom flex-sensor glove.
- **Problem / user:** Tower defense stays on-screen; the team wanted physical, room-scale play with a wearable controller. / mobile AR gamers
- **Domain / idea type:** entertainment_games / hardware_gadget
- **Platforms / hardware / AI:** mobile_ios; hardware / True / False
- **Stack:** langs C#; C++ (Arduino); Python; frontend Unity; backend ; db ; hosting 
- **Tech/APIs:** Unity (framework, core); Seeed XIAO ESP32 (hardware_part, core); Flex sensor + LSM6DSO32 IMU (hardware_part, core); NVIDIA GeForce RTX 5080 (prize only) (hardware_part, token, sponsor)
- **Sponsor APIs:**  | fit: No NVIDIA tool was used; the prize came from the Best Hardware Hack (Brick House) category, where an NVIDIA 5080 GPU was the reward, so this is not an NVIDIA challenge win.
- **Repo:** public, commits 21 (before/in/after event: 0/21/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Custom glove with Seeed XIAO ESP32, flex sensor and IMU sends UDP over the phone hotspot to Unity; each release is sent three times to survive packet loss; two gloves built.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; sponsor_challenge_link
- **Links:** [Devpost](https://devpost.com/software/overworked-archers) | [GitHub](https://github.com/Mohammad-R-Rashid/ARcher)


## HackTX 2025

### HackTX 2025  (HackTX 2025)

- **Prizes:** Winner Best Capital One Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** App that estimates the carbon footprint of a user's bank and card transactions by category and visualizes emissions, using Nessie data.
- **Problem / user:** People cannot see the environmental impact of everyday spending. / environmentally minded consumers
- **Domain / idea type:** sustainability_climate + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat
- **Stack:** langs JavaScript; TypeScript; frontend React; Vite; Tailwind CSS; backend Node.js; Express; db Nessie API; hosting 
- **Tech/APIs:** Capital One Nessie API (data_source, core, sponsor); Auth0 (auth, supporting); Google Gemini (ai_model, supporting); React (framework, core); MongoDB (database, token)
- **Sponsor APIs:** Capital One Nessie API | fit: Won Best Capital One Hack by using Nessie as the source of user accounts and transactions for per-category carbon estimates; the roadmap mentions partnering with banks such as Capital One.
- **Repo:** public, commits 20 (before/in/after event: 0/16/4), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Devpost page title is the event name, but the app is EcoFin Carbon; Nessie serves as the transaction and user-store layer with Auth0 login and an emissions model; CI/CD listed.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; project_name (page title is event name); ui_polish
- **Links:** [Devpost](https://devpost.com/software/ecofin-carbon) | [GitHub](https://github.com/arnavvalvekar/hacktx)


## HackTX 2026

### BreakingPoint  (HackTX 2026)

- **Prizes:** Winner [Capital One] The Best Use of Nessie [unknown]  (tier: sponsor_winner)
- **Pitch:** Simulator that shows how a surprise cost such as repairs affects a user's finances over 30 days, as an interactive consequence graph grounded in bank data.
- **Problem / user:** People cannot see how an unexpected expense will ripple through their next month of finances. / everyday bank customers facing unexpected costs
- **Domain / idea type:** fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js; React; React Flow; Tailwind CSS; backend FastAPI; db ; hosting 
- **Tech/APIs:** Capital One Nessie sandbox API (data_source, core, sponsor); SerpApi (data_source, supporting); Google Gemini (ai_model, supporting); React Flow (framework, core)
- **Sponsor APIs:** Capital One Nessie API | fit: Won Best Use of Nessie by using the sandbox API to supply a fictional customer's accounts and transactions as the financial context that grounds each 30-day cost scenario.
- **Repo:** public, commits 17 (before/in/after event: 0/17/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Scenario simulation over a fictional Nessie customer with React Flow graph; SerpApi finds resources that could offset the cost; Gemini used for reasoning.
- **Team size:** 3 | **Confidence:** high | unverified: event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/breakingpoint) | [GitHub](https://github.com/MMehta45/hacktx26)
