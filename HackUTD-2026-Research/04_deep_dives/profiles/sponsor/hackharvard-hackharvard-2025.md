# HackHarvard — HackHarvard 2025 (1 projects)

### C2Pay
*HackHarvard HackHarvard 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best Financial Hack by Capital One

**What it is:** C2Pay is a mobile SDK for payment fraud: it scores risk from device, motion/tap and biometric signals and only escalates to stronger verification, a TEE-key-signed C2PA manifest, when risk crosses a threshold. A React Native demo shop shows it.
**Problem / user:** Developers adding checkout flows, merchants needing proof of transactions, and shoppers who want little friction.

**Features**
- Risk-based adaptive MFA — Device, behavioral and biometric signals produce a score; only high scores trigger extra verification. *[shown_working]*
- C2PA manifests signed with TEE-backed keys — Escalated payments get a provenance manifest signed with hardware-backed device keys. *[claimed]*
- Merchant verification view — Merchant screen checks a transaction's proof. *[shown_working]*
- Mock shopping app with Stripe test payments — Expo app simulates checkout at various risk levels with a receipt. *[shown_working]*
- User analytics dashboard — In-app screen showing activity. *[shown_working]*

**Flow:** Shop in the mock app → Start payment; SDK collects signals → Risk score computed → Low risk passes; high risk gets signed manifest → Merchant view verifies; receipt issued

**Prompt:** Capital One's HackHarvard 2025 prize asking for an open-ended fintech project that rethinks banking; no tools named.
**Fit (implied):** Fintech security layer that makes online payments verifiable while keeping checkout low-friction; page also mentions Visa's secure-payments focus.  *(targeted: Best Financial Hack by Capital One)*
**AI:** none
**Architecture:** React Native/Expo TypeScript app embeds SDK modules for signal collection, risk scoring, hashing, secure storage and C2PA signing; Stripe test API mocks payments.
**Novelty:** Brings content-provenance (C2PA) and device attestation, from AI-image authenticity, into payment authentication.
**Scope:** small · working: Repo with 33 files and demo flows described; ML risk models listed as future. · polish: Video, mock shop UI and receipt screens.
**Claims:** Verifiable proofs for merchants | Only escalates when needed
**Gaps:** Risk scoring logic opaque
Sources: https://devpost.com/software/c2pay, https://github.com/sofiaal1/C2Pay

---

