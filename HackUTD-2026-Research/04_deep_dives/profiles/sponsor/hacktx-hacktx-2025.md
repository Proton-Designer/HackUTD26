# HackTX — HackTX 2025 (1 projects)

### EcoFin Carbon
*HackTX HackTX 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best Capital One Hack

**What it is:** A web app that estimates the CO2 footprint of each bank transaction pulled from Nessie, shows emissions by category on a dashboard with an eco score, and offers a Gemini chat coach for greener spending suggestions.
**Problem / user:** Consumers who want to be greener but cannot see the environmental impact of their spending in finance tools.

**Features**
- Nessie transaction sync — Backend pulls purchase history, normalizes merchants and categorizes them. *[claimed]*
- Hybrid carbon estimation — Amount times per-category kgCO2e factor, with unit-based logic for fuel, utilities, flights and a confidence score. *[claimed]*
- Analytics dashboard — Circular CarbonOrbit chart by category, animated metrics, trends and A-F eco score. *[claimed]*
- Gemini eco coach — Chat with spending-aware recommendations and impact estimates, history saved. *[claimed]*
- Auth0 login and secured API — JWT-verified Express routes with helmet, CORS and rate limiting. *[claimed]*
- Offsets, leaderboards, goals — Verified offset programs and sustainability goals. *[planned]*

**Flow:** Sign in through Auth0 → Sync transactions from Nessie → Emissions computed per transaction → View dashboard by category and eco score → Ask the coach for ways to cut emissions

**Prompt:** Broad fintech track: boldest idea in action, such as payments, smarter shopping, accessible financing or financial literacy; intentionally open-ended.
**Fit (implied):** Adds a carbon-impact lens to personal finance built on Nessie transaction data; README states it won the Capital One hack.  *(targeted: Best Capital One Hack)*
**Sponsor tools:** Capital One Nessie API (Source of user transaction data, core)
**AI:** Google Gemini powers the eco coach using spending context; emissions are rule-based lookups and multiplication by category factors, not learned models.
**Architecture:** React/Vite/TypeScript client and Express/TypeScript server with MongoDB (Mongoose models for user, transaction, emission, chat), Auth0 JWT, Nessie and Gemini calls.
**Novelty:** Reframes bank transactions as carbon estimates with confidence scores; common sustainability-plus-finance concept.
**Scope:** medium · working: About 10.7k LOC with documented API endpoints; no demo or video; Devpost says MongoDB planned while README says it is used. · polish: Animated glass-style UI described, detailed README with setup; no tests.
**Claims:** Functional prototype tracks and visualizes transaction-based carbon data
**Gaps:** No demo or video; README and Devpost disagree on MongoDB and Carbon Interface use
Sources: https://devpost.com/software/ecofin-carbon, https://github.com/arnavvalvekar/hacktx

---

