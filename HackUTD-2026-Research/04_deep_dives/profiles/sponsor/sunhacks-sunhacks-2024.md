# SunHacks — SunHacks 2024 (1 projects)

### LockItUp
*SunHacks SunHacks 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner State Farm - Best Hack for Social Good

**What it is:** A concept for QR-code bike locks built into campus bike stands, with a proof-of-concept Arduino stepper-motor lock and a Django web app on AWS (EC2, SQS, DynamoDB).
**Problem / user:** ASU students whose bikes get stolen; the page claims about 300 thefts per semester.

**Features**
- QR unlock at bike stands — Student scans a code to release the built-in lock *[claimed]*
- Web app — Django site as one place to lock bikes on campus *[claimed]*
- AWS backend — EC2 hosting, SQS messaging, DynamoDB for credentials, CDK for infra *[claimed]*
- Stepper-motor lock prototype — Arduino 101 with stepper and scrap materials *[claimed]*

**Flow:** Scan the QR code on a stand → Web app authenticates the student → Lock mechanism engages or releases

**Prompt:** State Farm SunHacks 2024 Best Hack for Social Good: technical solution to a local or global social issue.
**Fit (implied):** Addresses campus bike theft with shared secure lock infrastructure; page names the win but not the prompt.  *(targeted: State Farm - Best Hack for Social Good)*
**AI:** none
**Architecture:** Django app on EC2 communicates with the Arduino lock via SQS; DynamoDB holds users and credentials.
**Novelty:** Infrastructure-embedded lock instead of a personal lock; hardware prototype plus cloud.
**Scope:** small · working: Proof-of-concept prototype claimed; no video or demo; repo README empty. · polish: Little; large repo size likely from generated or vendored code.
**Claims:** 300 bikes stolen from ASU each semester (unsourced)
**Gaps:** no demo; prototype not shown
Sources: https://devpost.com/software/lockitup, https://github.com/risratna/lockitup (evidence README), sponsor_prompts_*.jsonl (SunHacks 2024)

---

