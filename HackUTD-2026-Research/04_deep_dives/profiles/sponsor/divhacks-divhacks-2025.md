# DivHacks — DivHacks 2025 (1 projects)

### PayPark
*DivHacks DivHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Sponsor Challenge: Capital One [Best Financial Hack]

**What it is:** A usage-based parking web app: pick a spot on a TomTom map, start a live session, watch cost accrue, then settle the exact amount in RLUSD on the XRP Ledger testnet. Echo AI by Merit supplies pricing, explanations and login.
**Problem / user:** Drivers who must prepay fixed parking blocks, overpay or risk tickets, and deal with meters and card fees.

**Features**
- Live parking sessions — Start/stop session with elapsed time and per-second cost updated over Socket.io. *[claimed]*
- RLUSD settlement on XRPL — Payment with trustline handling and ledger verification; testnet only. *[claimed]*
- Map discovery — Interactive TomTom map of parking locations. *[claimed]*
- AI dynamic pricing and explanations — Echo AI by Merit prices by location, time and demand and explains in plain language. *[claimed]*
- Wallet connection and history — Connect XRPL wallet, fund it, review sessions and transactions. *[claimed]*
- Provider dashboard, mobile apps — Next steps. *[planned]*

**Flow:** Sign in with Echo → Connect and fund an XRPL wallet → Pick a spot on the map → Start session and watch live billing → End session → Pay exact amount in RLUSD

**Prompt:** Open fintech track: payments, smarter shopping, accessible financing, financial literacy; Nessie API optional.
**Fit (implied):** Reinvents payment for parking as pay-for-what-you-use with on-chain settlement; no Nessie use mentioned. Also entered Ripple XRPL challenge.  *(targeted: Capital One Best Financial Hack)*
**AI:** Echo AI by Merit used for dynamic pricing, pricing explanations, recommendations, auth and chat; details of model not given.
**Architecture:** Next.js frontend and Express/Prisma/SQLite API; Socket.io for live state; XRPL.js to testnet for RLUSD; TomTom Maps.
**Novelty:** Changes the unit of parking from prepaid block to metered session, paid by stablecoin on a public ledger.
**Scope:** medium · working: Two Loom demo videos linked on Devpost; monorepo with api and web apps plus docs; repo includes a vendored Node binary inflating size. · polish: README with architecture diagram, setup docs, testnet disclaimer; README demo GIF placeholder unfilled.
**Claims:** Sub-second billing precision with XRPL micropayments | 3rd place overall and Most Popular Hack
**Gaps:** videos not watchable
Sources: https://devpost.com/software/paypark, https://github.com/kkanda0/ParkPay (evidence README), sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl (DivHacks 2025)

---

