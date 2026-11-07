# HackNC — HackNC 2026 (1 projects)

### RxSolve
*HackNC HackNC 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [Capital One] The Best Use of Nessie

**What it is:** A simulated payments layer for independent pharmacies: it catches prescription claims paid below acquisition cost, assembles evidence from the pharmacy's invoices, files appeals through portal, email or fax, and settles recoveries on a Nessie sandbox ledger. A PBM simulator and dashboard demo the loop.
**Problem / user:** Independent pharmacies that PBMs underpay and that lack the leverage of big chains to contest.

**Features**
- Underpayment detection — Compares paid claim against acquisition cost via invoice data at claim time. *[shown_working]*
- Multi-channel appeals — Routes appeals through simulated portal, email or fax depending on what the PBM accepts. *[shown_working]*
- Evidence gathering with guardrails — Gemini extracts evidence; rules block filing with missing facts and ask a human (e.g. wholesaler detail). *[shown_working]*
- PBM simulator — Standalone service that mimics PBM adjudication, denials and settlement for testing. *[shown_working]*
- Dashboard — Shows claim journey, evidence, communications, ledger activity and recovery chart. *[shown_working]*
- Nessie ledger settlement — Recoveries recorded as transfers in Capital One's Nessie sandbox. *[shown_working]*
- Recovery opportunity scan — Upload a historical claims CSV, measure shortfalls, and queue ready claims for auto-file under a dollar limit. *[shown_working]*
- Unfamiliar PBM form support — Constrained form filling for new PBM forms. *[planned]*

**Flow:** Claim arrives from mock pharmacy system → Underpayment flagged → Evidence assembled; missing wholesaler info requested and supplied → Appeal filed via portal/email/fax → PBM sim responds and claim is refiled/settled → Dashboard shows recovery and ledger

**Prompt:** Capital One prize for the best project built with its Nessie hackathon banking API; the Devpost listing gives no further brief.
**Fit (explicit):** Uses Nessie as the settlement ledger for recovered claim money, with logical transfers adapted to the sandbox's behavior. The writeup describes this explicitly.  *(targeted: [Capital One] The Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (Ledger for claim settlement transfers, core); Photon (Listed in built-with; role not described, unclear)
**AI:** Gemini extracts evidence from documents and drives negotiation; deterministic rules decide underpayment and PBM outcomes, with human-in-the-loop stops when facts are missing.
**Architecture:** Bun/TypeScript monorepo: API orchestrator, PBM simulator, dashboard, plus a mock pharmacy PMS; claims/events in TigerData, Gemini for extraction, Nessie for ledger; local doubles when keys absent.
**Novelty:** Targets a niche, real pharmacy-reimbursement workflow with a full simulated counterparty and fail-closed rules; unusually large repo with design docs and tickets.
**Scope:** large · working: README run steps, seed replay, end-to-end tests over HTTP, YouTube demo, 14 screenshots. · polish: Docs folder (design, plan, demo, status), scan page with six scenarios, dashboard.
**Claims:** End-to-end demo recovers an underpaid claim across three appeal channels
**Gaps:** Video not watched; No quantified results; ElevenLabs/Photon roles unexplained
Sources: https://devpost.com/software/rxsolve, evidence/sponsor-hacknc-hacknc-2026-rxsolve.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

