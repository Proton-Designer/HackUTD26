# HackIllinois — HackIllinois 2026 (1 projects)

### Velum
*HackIllinois HackIllinois 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best Use of Capital One Nessie (Hackathon API)

**What it is:** A document-protection platform that processes PDFs and images so humans can read them but AI extraction fails, syncs through Google Drive, and commits document-state hashes to Solana. A workflow canvas can also trigger Nessie bank deposits or withdrawals.
**Problem / user:** People protecting documents against AI scraping and trust in centralized key holders; also users wanting verifiable financial workflows.

**Features**
- Adversarial document hardening — Python pipeline adds pixel noise, decoy text, prompt-injection overlays, perturbations and EXIF poisoning, seeded by chain entropy. *[claimed]*
- Google Drive sync — OAuth sign-in; hardened files re-uploaded to the same folder with per-folder settings and sync history. *[claimed]*
- On-chain entropy oracle — Every 5 seconds hashes Solana token state plus document IDs with SHA3-256 and commits via SPL Memo. *[claimed]*
- Verifier CLI and public Wall — CLI checks a commit by transaction signature; /wall shows live token state grid. *[claimed]*
- Workflow engine with banking block — Visual canvas of four block types run in topological order; banking block reads or moves money through Nessie. *[claimed]*
- Dashboard — Next.js app for wallets, Nessie accounts, workflows and activity with Explorer links. *[claimed]*

**Flow:** Sign in with Google and connect Drive folders → Harden documents → Sync hardened files back → Oracle anchors state on Solana → Build a workflow mixing document validation and Nessie events → Verify any commit with the CLI

**Prompt:** Track for projects making good use of Capital One's Nessie hackathon API; page details were sparse.
**Fit (explicit):** Nessie appears as a banking event block in the workflow engine that reads balances and executes deposits or withdrawals when conditions pass, tied to an on-chain commit. It is one module of a larger project.  *(targeted: Best Use of Capital One Nessie (Hackathon API))*
**Sponsor tools:** Capital One Nessie API (Banking event workflow block: balances, transactions, deposits, withdrawals, supporting)
**AI:** Adversarial ML hardening against AI extraction (optional PGD attacks with PyTorch); no model named; no LLM features described.
**Architecture:** Next.js frontend with Supabase auth, Express/Drive backend, Python hardening scripts, and Node oracle writing to Solana devnet via SPL Memo; Nessie called from the workflow layer.
**Novelty:** Unusual combination of anti-AI document poisoning, blockchain entropy commits and a banking workflow canvas; scope far from a typical finance app.
**Scope:** large · working: About 17k LOC, Vercel demo link and YouTube video on Devpost; no tests. · polish: Public wall page, verifier CLI, multi-service architecture; README short.
**Claims:** Hardened documents look identical to humans but are unreadable to AI systems | Workflows validate live banking data and commit on-chain in one atomic-like flow
**Gaps:** No measured hardening effectiveness; Official track text sparse; Video not viewed
Sources: https://devpost.com/software/velum, https://github.com/MarcDasilva/HackIllinois

---

