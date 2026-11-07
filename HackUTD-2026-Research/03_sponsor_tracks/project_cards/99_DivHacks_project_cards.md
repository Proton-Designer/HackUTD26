# DivHacks: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DivHacks 2025

### PayPark  (DivHacks 2025)

- **Prizes:** Winner Sponsor Challenge: Capital One [Best Financial Hack] [unknown]  (tier: sponsor_winner)
- **Pitch:** Real-time parking payment platform where users start a session in one click and pay automatically in XRP over the XRP Ledger, with a map of spots.
- **Problem / user:** Parking meters need coins or cards and are clunky; drivers want seamless real-time pay-per-use payments. / drivers and parking operators
- **Domain / idea type:** fintech_finance + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / other
- **Stack:** langs TypeScript; Python; frontend Next.js; React; Tailwind CSS; Framer Motion; backend FastAPI; db ; hosting 
- **Tech/APIs:** XRP Ledger / Ripple (payments, core); TomTom Maps API (maps_geo, supporting); Echo AI (ai_model, unclear); FastAPI (framework, supporting); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Entered for Capital One's Best Financial Hack as a parking payments product; the page shows XRP Ledger payments and does not mention Capital One or Nessie.
- **Repo:** public, commits 39 (before/in/after event: 0/35/4), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Blockchain payments (XRP Ledger/Ripple) with TomTom maps and Socket.io live updates; two Loom videos instead of YouTube; Echo AI listed in the tags.
- **Team size:** 3 | **Confidence:** high | unverified: event_end; ai_used; sponsor_fit_note; ui_polish
- **Links:** [Devpost](https://devpost.com/software/paypark) | [GitHub](https://github.com/kkanda0/ParkPay)


## DivHacks 2026

### RentEscrow  (DivHacks 2026)

- **Prizes:** Winner Sponsor Challenge: Capital One [The Best Use of Nessie] [unknown]  (tier: sponsor_winner)
- **Pitch:** Tenant and landlord platform for tracking repairs, sharing evidence, messaging, and managing simulated rent escrow with Nessie sandbox money and an XRPL testnet.
- **Problem / user:** Tenant-landlord repair disputes lack shared evidence and trustworthy handling of held rent. / tenants and landlords
- **Domain / idea type:** housing_real_estate + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; Python; frontend Next.js; backend Next.js; db MongoDB; hosting Railway
- **Tech/APIs:** Capital One Nessie sandbox (payments, core, sponsor); Photon messaging (telecom, supporting, sponsor); Google Gemini (ai_model, supporting); NYC Open Data (data_source, supporting); XRPL Testnet (payments, supporting); MongoDB (database, supporting)
- **Sponsor APIs:** Capital One Nessie API; Photon | fit: Won Best Use of Nessie by running simulated rent escrow against Nessie's banking sandbox, alongside Photon messaging between tenant and landlord.
- **Repo:** public, commits 43 (before/in/after event: 0/43/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup short, impact claims False
- **Notes:** Combines NYC Open Data records, Gemini, Photon messaging, Nessie sandbox banking and XRPL Testnet escrow; short writeup but a hosted Railway deployment.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; nessie depth; ui_polish
- **Links:** [Devpost](https://devpost.com/software/rentescrow-nthfwb) | [GitHub](https://github.com/mujtaba-atif/divhacks1)

### unsaid  (DivHacks 2026)

- **Prizes:** Winner Sponsor Challenge: Capital One [The Best Use of Nessie] [unknown]  (tier: sponsor_winner)
- **Pitch:** Group-planning agent you text like a friend: it collects constraints, pulls typical spend from Nessie, scores venues and negotiates a plan across everyone via messaging.
- **Problem / user:** Coordinating a group outing means endless back-and-forth over time, distance, diet and budget. / friend groups planning outings
- **Domain / idea type:** social_community + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / llm_chat; agent_or_tool_use; recommendation
- **Stack:** langs TypeScript; frontend ; backend Node.js; db MongoDB; hosting 
- **Tech/APIs:** Capital One Nessie API (data_source, core, sponsor); Photon Spectrum (telecom, core, sponsor); Grok (ai_model, core); Claude (ai_model, supporting); MongoDB (database, supporting)
- **Sponsor APIs:** Capital One Nessie API; Photon Spectrum | fit: Won Best Use of Nessie by proposing each person's budget from their usual spend pulled via the Nessie API rather than asking for a number, inside a Photon Spectrum texting flow.
- **Repo:** public, commits 58 (before/in/after event: 0/58/0), README solid
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Messaging-first product built on Photon Spectrum with join codes and fan-out; Grok extracts and scores preferences, plus a negotiation engine and a venue catalogue; built with Claude and Cursor.
- **Team size:** 2 | **Confidence:** high | unverified: event_end; writeup sections; ui_polish
- **Links:** [Devpost](https://devpost.com/software/unsaid-zm8w5v) | [GitHub](https://github.com/argsdio/unsaid)
