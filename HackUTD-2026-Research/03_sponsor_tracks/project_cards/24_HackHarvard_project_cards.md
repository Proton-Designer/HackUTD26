# HackHarvard: project cards (8 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackHarvard 2025

### C2Pay  (HackHarvard 2025)

- **Prizes:** Winner Best Financial Hack by Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile SDK for risk-based adaptive multi-factor authentication of payments, scoring device, behavior and biometric signals and prompting extra auth only above a threshold.
- **Problem / user:** Fixed multi-factor checks add friction to every payment while fraud still slips through. / payment app developers and shoppers
- **Domain / idea type:** fintech_finance + safety_security / dev_tool
- **Platforms / hardware / AI:** mobile_cross / False / False
- **Stack:** langs TypeScript; frontend React Native; Expo; backend ; db ; hosting 
- **Tech/APIs:** React Native / Expo (framework, core); Stripe test API (payments, supporting); C2PA (other, unclear); Device behavioral and biometric signals (other, core)
- **Sponsor APIs:**  | fit: Won Capital One's Best Financial Hack with a payments-security SDK; the page lists Stripe test payments and no Capital One API.
- **Repo:** public, commits 18 (before/in/after event: 0/16/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Demo is a React Native Expo shopping app showing the SDK, with mock payments via Stripe test API and motion and tap-pattern signals; mentions C2PA, hashing and TEE concepts.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; ai_used; ui_polish
- **Links:** [Devpost](https://devpost.com/software/c2pay) | [GitHub](https://github.com/sofiaal1/C2Pay)


## HackHarvard 2026

### Concord  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Turns a clinical-trial protocol into a site budget priced from public Medicare fee schedules, with coverage analysis, site comparison and portfolio overlap views.
- **Problem / user:** Hospitals and trial sponsors negotiate trial budgets without shared public benchmarks, so numbers are hard to verify. / hospital research offices and trial sponsors
- **Domain / idea type:** health_wellness + fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; TypeScript; frontend React; Vite; Leaflet.js; backend FastAPI; Uvicorn; Pydantic; db SQLite; hosting GitHub Pages
- **Tech/APIs:** ClinicalTrials.gov API (data_source, core); CMS Physician Fee Schedule (data_source, core); CMS Clinical Laboratory Fee Schedule (data_source, core); FastAPI (framework, supporting); React (framework, supporting); Leaflet.js (maps_geo, supporting)
- **Sponsor APIs:**  | fit: Queue lists a Photon sponsor prize (unconfirmed, no badge on page); the page text shows no Photon or iMessage use, so how it targeted Photon is unknown.
- **Repo:** public, commits 293 (before/in/after event: 0/293/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 37, writeup long, impact claims True (Illustrative budget split: about 20% of per-participant sponsor budget from public CMS rates, 60% from a proposed standard.)
- **Notes:** Labels every figure as public source or assumption; uses CMS fee schedules and ClinicalTrials.gov data; worked example on a Regeneron lung trial. Photon use not visible in the page text I read.
- **Team size:** 3 | **Confidence:** medium | unverified: prizes; sponsor_apis_used; sponsor_fit_note; writeup_sections; writeup_length
- **Links:** [Devpost](https://devpost.com/software/concord-17as0b) | [GitHub](https://github.com/CosmicOdyssey/concord)

### Elfie  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** One phone number you text to manage a move: four coordinating AI agents find an apartment, sell furniture and settle roommate bills over iMessage, SMS and voice.
- **Problem / user:** Moving, especially on Boston's September 1 lease turnover, wastes time and money on logistics, furniture disposal and chasing roommates for shares. / renters moving apartments, esp. Boston students
- **Domain / idea type:** housing_real_estate + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; frontend ; backend Bun; db Postgres (Supabase); hosting Railway; Vercel
- **Tech/APIs:** Photon 2.0 (telecom, core, sponsor); Claude (ai_model, core); Retell (ai_model, supporting); Browserbase / Stagehand (other, supporting); Nessie (Capital One) (payments, supporting, sponsor); Supabase (database, supporting); Railway (cloud, supporting)
- **Sponsor APIs:** Photon 2.0; Nessie (Capital One mock banking API) | fit: Built the whole product on Photon 2.0 as an iMessage/SMS/voice multi-agent assistant, targeting the Photon agent track; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** public, commits 107 (before/in/after event: 0/107/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 16, writeup long, impact claims True (Cites 5,000+ mattresses collected in a week and surge moving prices above $2,000 as context.)
- **Notes:** Four named agents (crew lead, home, stuff, money) behind one thread; draws ledger and plan as images because Photon 2.0 lacks app cards; page also describes fighting Photon version changes.
- **Team size:** 4 | **Confidence:** medium | unverified: prizes; sponsor_apis_used depth; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/n-a-okr0vf) | [GitHub](https://github.com/arshiyasharma/hackharvard/)

### Keepsake  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Phone-camera memory assistant for people with dementia that detects everyday items, remembers where last seen, saves a photo and answers 'where is it' by voice.
- **Problem / user:** People with dementia repeatedly lose glasses, keys and pills; tags and smart glasses depend on them remembering to use a device. / people living with dementia and their families
- **Domain / idea type:** health_wellness + accessibility / new_category
- **Platforms / hardware / AI:** mobile_cross / False / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; frontend React Native; Expo; backend FastAPI; db ; hosting 
- **Tech/APIs:** YOLO-World / Ultralytics (ai_model, core); CLIP (ai_model, supporting); MediaPipe (ai_model, supporting); OpenCV (framework, supporting); OpenAI (ai_model, unclear); xAI Grok (ai_model, unclear); Photon (telecom, unclear, sponsor); Expo / React Native (framework, core); FastAPI (framework, supporting)
- **Sponsor APIs:** Photon | fit: Lists Photon in its Built With tags, but the writeup text I read does not describe how it was used; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** public, commits 119 (before/in/after event: 1/115/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims True (Opens with a statistic on the number of Americans living with dementia (about 7 million).)
- **Notes:** Uses open-vocabulary detection (YOLO-World, CLIP) on a phone camera and returns a photo with the item highlighted. Photon appears only as a Built With tag in what I read.
- **Team size:** 4 | **Confidence:** medium | unverified: prizes; sponsor_apis_used depth; sponsor_fit_note; tech_items depth; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/keepsake-df0gmw) | [GitHub](https://github.com/rayhanrinzan/keepsake)

### Mirage  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Security watcher between an AI agent and its tools that silently swaps out-of-scope calls for a fake environment, logs them forensically and alerts a defender by text and voice.
- **Problem / user:** Hard-blocking a misbehaving AI agent gives no information and tips it off; teams need to contain agents that exceed their scope. / security teams deploying AI agents
- **Domain / idea type:** safety_security + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; JavaScript; frontend HTML5; CSS3; backend Node.js; Express.js; WebSockets; db ; hosting ngrok
- **Tech/APIs:** Photon (spectrum-ts, iMessage) (telecom, supporting, sponsor); ElevenLabs (ai_model, supporting); Factory Droid (ai_model, core); Model Context Protocol (other, core); Daytona (cloud, supporting); OpenAI (ai_model, unclear); Express.js (framework, supporting)
- **Sponsor APIs:** Photon; spectrum-ts; ElevenLabs | fit: Used Photon to text the on-call defender when a call is flagged, followed by an ElevenLabs voice briefing; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** public, commits 101 (before/in/after event: 0/101/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Reports results from a 25-agent rehearsal run with counts of caught out-of-scope attempts.)
- **Notes:** Tool-call interception with decoy responses; evaluated in a 25-agent rehearsal (24 live agents plus one scripted rogue); defender gets Photon text, then ElevenLabs voice call with one-time code.
- **Team size:** 4 | **Confidence:** medium | unverified: prizes; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/team-b-0ydafx) | [GitHub](https://github.com/MrFiscus/Mirage)

### SiteLine  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Reviews site-specific redlines on clinical trial agreements against precedents and rules, auto-accepting safe changes and escalating the rest to legal, finance and privacy approvers via iMessage.
- **Problem / user:** Contract staff manually review every tracked change when sponsors send the same trial agreement to dozens of hospital sites. / clinical trial contracting teams at sponsors and hospitals
- **Domain / idea type:** civic_legal + health_wellness / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; TypeScript; JavaScript; frontend HTML5; CSS; backend ; db Supabase Postgres; S3; hosting Daytona
- **Tech/APIs:** Photon 2.0 (iMessage + voice) (telecom, core, sponsor); Daytona (cloud, supporting); Supabase Postgres (database, supporting); S3 (cloud, supporting)
- **Sponsor APIs:** Photon 2.0 | fit: Used Photon 2.0 as the approval channel: each escalation goes as one iMessage to the right approver with a phone-call fallback; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** public, commits 213 (before/in/after event: 0/213/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 55, writeup long, impact claims False
- **Notes:** Approvers reply 1/2/3 (approve, counter, reject) in iMessage with a phone-call fallback; unclear cases are never auto-accepted; precedents stored in Supabase Postgres and S3.
- **Team size:** 4 | **Confidence:** medium | unverified: prizes; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/siteline-90rxwp) | [GitHub](https://github.com/duna-akin/hackharvard-2026)

### Swarm  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Tracks breaking changes in third-party APIs and uses coding agents to open and merge fix PRs, with approval by replying yes in an iMessage thread.
- **Problem / user:** Teams lose engineering time to API vendors shipping breaking changes that nobody notices until users report breakage. / software teams depending on many third-party APIs
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; JavaScript; frontend HTML; SVG; backend FastAPI; Server-Sent Events; db SQLite; hosting Daytona; GitHub Actions
- **Tech/APIs:** Photon (iMessage) (telecom, core, sponsor); Factory Droid SDK (ai_model, core); Anthropic (ai_model, supporting); OpenAI (ai_model, supporting); Daytona (cloud, supporting); GitHub / GitHub Actions (other, supporting); FastAPI (framework, supporting); SQLite (database, supporting)
- **Sponsor APIs:** Photon | fit: Used Photon so the agent texts the developer a real iMessage alert about a broken dependency and takes yes replies to open and merge the fix PR; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims True (States dataset of 386 breaking changes from 8 vendors, 2009 to present.)
- **Notes:** Maintains a database of 386 breaking changes across 8 vendors refreshed daily; human approves PR opening and merging by texting yes over Photon.
- **Team size:** 1 | **Confidence:** medium | unverified: prizes; writeup_sections; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/swarm-1e527i) | [GitHub](https://github.com/shubangowda/swarm)

### TekKEY  (HackHarvard 2026)

- **Prizes:** UNCONFIRMED: appears in winners=true gallery AND project text mentions Photon; Devpost page shows no prize badge yet (Photon 2.0 messaging agent track: winner/runner-up/best voice) [unknown]  (tier: sponsor_winner)
- **Pitch:** Trading-key layer that bounds the maximum loss an AI agent can cause, verifies agent programs, and alerts the owner by iMessage with a freeze command.
- **Problem / user:** Exchanges only check whether a caller may send orders, but owners need a hard cap on what an LLM trading agent can cost them. / owners of AI trading agents
- **Domain / idea type:** fintech_finance + safety_security / dev_tool
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs C++20; Python; frontend ; backend FastAPI; db SQLite; hosting Vercel; Daytona
- **Tech/APIs:** Photon 2.0 (telecom, supporting, sponsor); Capital One Nessie (payments, supporting, sponsor); Factory Droid SDK (ai_model, supporting); Anthropic and xAI models (ai_model, core); Coinbase market data (data_source, supporting); Chalk model gateway (ai_model, supporting); Daytona (cloud, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Photon 2.0; Capital One Nessie | fit: Used Photon 2.0 as the owner's phone: every program end and budget alarm is a real iMessage and replying freeze stops new programs; Photon prize on queue is unconfirmed (no badge on page).
- **Repo:** public, commits 12 (before/in/after event: 0/12/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Rejected agent programs return counterexamples that feed a repair loop; core written in C++20 with a Python 3.12 FastAPI layer; uses Coinbase market data and Capital One Nessie.
- **Team size:** 2 | **Confidence:** medium | unverified: prizes; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/tekkey) | [GitHub](https://github.com/JoshuaA1292/TekKEY)
