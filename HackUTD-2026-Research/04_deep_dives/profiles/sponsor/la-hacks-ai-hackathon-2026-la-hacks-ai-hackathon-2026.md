# LA Hacks (AI Hackathon 2026) — LA Hacks AI Hackathon 2026 (3 projects)

### BetterBill
*LA Hacks (AI Hackathon 2026) LA Hacks AI Hackathon 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: Best Voice Agent (also Visa prize)

**What it is:** A patient-side hospital bill checker: snap a photo, the app reads each line, flags suspect charges with sources, screens for financial assistance, drafts a dispute letter and has an AI advocate phone billing after the patient approves.
**Problem / user:** Patients, especially insured adults, who receive hospital bills they may not owe and cannot decode billing codes, price files or charity-care rules; cites 45% getting a bill they thought insurance should cover.

**Features**
- Bill photo or text reading — StepFun vision model transcribes lines; patient confirms and corrects each line and marks care not received. *[shown_working]*
- Deterministic error checks — TypeScript rules engine in integer cents checks duplicates, CMS unit limits, bill-versus-statement mismatches and published cash prices, with a source per amount. *[shown_working]*
- Financial assistance screening — Matches hospital policy, federal rules and state charity-care laws; Browser Use fetches missing policies live. *[shown_working]*
- Dispute letter drafting — Gemini drafts; claim checker rejects dollar figures not in the evidence; patient approves exact text. *[shown_working]*
- AI advocate phone call — ElevenLabs agent over a Photon line calls billing after approval; 3-way call prototype with patient on the line. *[claimed]*
- Redacted evidence packet and Prices tab — Shareable packet of findings and published hospital prices. *[claimed]*

**Flow:** Snap or paste the bill → Confirm lines and fix misreads → Review flagged charges with proof → See assistance eligibility → Approve letter then advocate calls billing → Share redacted evidence packet

**Prompt:** Photon track at LA Hacks 2026: build an iMessage-native agent on Photon; separate prize for the best voice agent. Judged on technical depth, product thinking and impact. Visa prize text not found.
**Fit (explicit):** AI voice advocate calls hospital billing over a Photon phone line using an ElevenLabs agent, with the patient approving first.  *(targeted: Photon Best Voice Agent, Visa The Future of Shopping)*
**Sponsor tools:** Photon (phone line for advocate calls, supporting); ElevenLabs (billing-call voice agent, supporting); Browser Use (capturing hospital price files and policies, supporting); StepFun, Sentry, Tiger Data (bill reading, tracing, database, supporting)
**AI:** AI transcribes bills (StepFun), drafts letters (Gemini) and voices calls (ElevenLabs); all dollar math is deterministic code, with guards rejecting ungrounded figures or unmatched quotes.
**Architecture:** Expo/React Native and TanStack Start front ends, Bun/oRPC/Drizzle/Postgres backend on Tiger Data, rules engine, LiveKit Python voice controller, Browser Use scrapers, Vercel hosting, Sentry traces.
**Novelty:** Separates AI reading/writing from code-computed numbers with sourced findings and evaluates against synthetic bills with known seeded errors; ships a monorepo across web, iOS and Android.
**Scope:** large · working: Live app, demo video, tests, Docker and CI; about 93k LOC across 903 files. · polish: Trailer, sourced works-cited README, design folder, eval results and pricing model.
**Claims:** 22 of 22 seeded errors caught on 11 synthetic bills, 0 false flags on 3 clean bills | 88.8% line recall on 35 phone photos | 1 of 3 in-scope findings caught on 5 recreated real cases | Saved reads return in under 1 second (from 26)
**Gaps:** Visa prompt not found; phone call not shown working
Sources: https://devpost.com/software/betterbill, https://github.com/matmanna/betterbill

---

### Henomaly
*LA Hacks (AI Hackathon 2026) LA Hacks AI Hackathon 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: iMessage Track Winner (also QNX prize)

**What it is:** A poultry-pen early-warning system: a camera on a QNX Raspberry Pi 5 watches hens and droppings with on-device YOLO models, scores each pen against its own baseline and texts farmers an iMessage alert with evidence, without diagnosing disease.
**Problem / user:** Commercial poultry farmers and their vets, since avian flu can kill huge flocks before anyone notices; needs to work with unreliable internet.

**Features**
- Edge camera pipeline on QNX — Nine prioritized processes using message passing and shared-memory frames; ONNX Runtime via a C bridge; a supervisor restarts killed stages in 20-33 ms. *[shown_working]*
- Chicken detection and behavior classifiers — YOLO11n detector and YOLO11-cls models flag inactivity, panting, eating, drinking, movement. *[shown_working]*
- Droppings appearance model — YOLO11n trained on public fecal photos (mAP50 0.854); fails on distant barn footage so demo simulates the close-up path. *[claimed]*
- Per-pen baselines and persistence alerting — Scores each pen against its own hourly baseline; alert only when anomaly persists across windows. *[shown_working]*
- Farmer iMessage alerts and chat — Photon sends pen, time, evidence image and explanation; farmer can ask questions, request images and decide on vet sharing. *[shown_working]*
- Dashboard and monitor display — Next.js dashboard at aremyhens.fit reads analysed clips. *[shown_working]*
- Paper on cross-collection accuracy — Benchmark shows ~99% farm-test accuracy falls to 75-78% on a PCR-labelled collection. *[shown_working]*

**Flow:** Pi camera captures pen frames → System scores pen against its hourly baseline → Persistent anomaly creates an alert with evidence → Farmer gets iMessage alert → Farmer asks follow-ups and decides whether to share with vet

**Prompt:** Photon iMessage track at LA Hacks 2026: build an iMessage-native agent on Photon, judged on technical depth, product thinking and impact. QNX prize text not found.
**Fit (explicit):** Farmer alert and chat loop runs over iMessage through Photon; the whole edge pipeline runs on QNX on a Raspberry Pi 5.  *(targeted: Photon iMessage Track, QNX track)*
**Sponsor tools:** Photon / iMessage (farmer alerts and chat, supporting); QNX 8.0 on Raspberry Pi 5 (real-time process-isolated edge pipeline, core); Veri training platform (multi-GPU model training on AWS, supporting)
**AI:** Open-source YOLO11 detector and classifiers trained on public poultry data (Big Broiler video, Machuve droppings) and exported to ONNX for on-device inference; statistical per-pen baselining decides alerts.
**Architecture:** Camera Module 3 to QNX C capture, still-spot finder and ONNX detector, behavior and droppings stages, alert logic, Photon iMessage and chat; Next.js dashboard on Vercel; training on Veri/AWS GPUs.
**Novelty:** Combines a real-time OS with fault-injection demo, a written cross-collection benchmark paper and honest reporting that droppings detection failed on real distant frames.
**Scope:** large · working: Live site, hardware photos, tests and CI; 990 files and 46k LOC; metrics reported on held-out data. · polish: Full paper with verification report, mermaid diagrams, dashboard and hardware photos.
**Claims:** Chicken detector mAP50 0.927 | Behavior classifier top-1 accuracy 0.701 | Detector 168 ms at 320 px on the Pi 5 (3.7x faster than 640 px) | Killed stage relaunched within 20-33 ms
**Gaps:** QNX prompt not found; no video
Sources: https://devpost.com/software/holy-crap, https://github.com/RishitRai/Henomaly

---

### SproutPass
*LA Hacks (AI Hackathon 2026) LA Hacks AI Hackathon 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: iMessage Runner-Up (also Visa prize)

**What it is:** A Base44-hosted app and iMessage flow where parents pass outgrown children's clothes to nearby families: photos become inventory, shared needs are matched, the seller shares a listing and only the buyer approves a trade, settled with a simulated Visa receipt.
**Problem / user:** Parents of young children who outgrow clothes quickly and find listing, searching and arranging exchanges too much effort.

**Features**
- Photo or chat intake — Base44 LLM suggests garment details from photos and parents confirm; also accepted through a private iMessage thread via Photon. *[shown_working]*
- Need capture — AI extracts sizes, categories and budgets from messages and asks for confirmation before saving. *[shown_working]*
- Nearby-encounter matching — Shared listings checked against confirmed needs by size, category, budget and fit rules; location is simulated in demo. *[shown_working]*
- Seller authorize, buyer approve — Sharing a listing authorizes the seller; buyer's approval alone triggers ownership update. *[shown_working]*
- Simulated Visa receipt — Labeled simulation records an authorization reference and receipt; no real card or Visa API. *[shown_working]*
- Pixel companions and celebration — Playful layer with companions, flowers and sounds that dramatize encounters and approvals. *[shown_working]*

**Flow:** Parent sends clothing photos by iMessage or app → Confirms garment details and needs → Families meet nearby and companions find a fit → Seller shares listing; buyer reviews offer → Buyer approves; ownership moves and a simulated receipt appears

**Prompt:** Photon iMessage track at LA Hacks 2026: build an iMessage-native agent on Photon, judged on technical depth, product thinking and impact. Visa prize text not found.
**Fit (explicit):** Intake and offers flow through iMessage conversations linked by Photon; a resale checkout with simulated Visa payment answers the shopping prize.  *(targeted: Photon iMessage Runner-Up, Visa The Future of Shopping)*
**Sponsor tools:** Photon (link iMessage conversations to offers and receipts, supporting); Visa (simulated) (labeled payment simulation receipt, token); Base44 (hosting, data store, backend functions, LLM calls, core)
**AI:** Base44 InvokeLLM extracts garment details and structured needs from photos and messages; application code, not the model, validates matches and approvals.
**Architecture:** React/Vite front end with Leaflet and Zustand on Base44, which stores garments, needs, listings, proposals and ownership history with backend functions; Photon agent worker bridges iMessage.
**Novelty:** Buyer-only final approval with explicit simulated payment; proximity-based matching with game-like companions; unusually candid README on what is staged versus real.
**Scope:** medium · working: Live Base44 app and demo script; 456 files, 43k LOC, tests; README says AI, location, payment and iMessage delivery are partly staged. · polish: 40-second portrait demo video, phone-view screenshots, submission docs, feedback form.
**Claims:** Connected prototype covering inventory, needs, matching, offers, approval and ownership update | Team states tests do not show parents want the product
**Gaps:** Visa prompt not found; Devpost lists no video; GitHub README has one
Sources: https://devpost.com/software/sproutpass, https://github.com/96528025/SproutPass

---

