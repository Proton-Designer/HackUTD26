# HackUTD 2026 — Safe Signal × NVIDIA Nemotron research summary
**Prepared 2026-11-07 for Sunday 2026-11-08 judging**  
**Tracks:** T-Mobile Safe Signal (protect before/during/after) + NVIDIA Nemotron Beyond a Chatbot (multi-step autonomous tool workflows).  
**Research scope:** Eight Markdown sections in this folder, with source URLs, build applications and uncertainty flags. The project uses **synthetic data only**.

## Top 10 findings ranked by impact on winning

| Rank | Finding | Decision / why it wins | Research file |
|---:|---|---|---|
| **1** | **The product must act, not just classify.** An approved `SIMULATED` bank hold and recovery receipt make protection tangible. | Build **detect -> independent verification -> explain -> approve -> simulated protective action -> recover** as the central demo, not a chat UI. [FTC evidence](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud). | [04 Competitors](04-competitive-landscape-ChatGPT.md), [08 Pitch](08-pitch-ammo-ChatGPT.md) |
| **2** | **The NVIDIA track requires visible Nemotron plus multi-tool execution.** NVIDIA-hosted inference exposes an OpenAI-compatible API; some endpoints have conflicting availability. | Test `nvidia/nemotron-3-super-120b-a12b` and Omni, then show actual agent tool calls. Cache truthful offline replay fallback. [NVIDIA](https://build.nvidia.com/). | [01 Stack](01-nvidia-stack-ChatGPT.md) |
| **3** | **Avoid a deprecated integration time sink.** NeMo Agent Toolkit was deprecated in **October 2026**, EOL by year-end; Relay/Helix/Fabric are successors. | Lightweight Python controller with tool schema and policy engine; only copy toolkit architecture/examples. [NVIDIA migration guide](https://docs.nvidia.com/nemo/agent-toolkit/1.9/resources/migration-guide.html). | [01 Stack](01-nvidia-stack-ChatGPT.md) |
| **4** | **T-Mobile already protects calls, texts and websites; Pixel now has on-device scam warnings in messaging.** | Explicitly claim the next-step intervention and recovery orchestration, not “first text scam detection.” [T-Mobile](https://www.t-mobile.com/benefits/scam-shield), [Google](https://support.google.com/pixelphone/thread/466181739/september-2026-pixel-drop). | [04 Competitors](04-competitive-landscape-ChatGPT.md) |
| **5** | **Telecom trust APIs are open as specs, not public operator data.** SIM Swap/Device Swap/Number Verification/KYC/Tenure/Recycling can be mocked faithfully. | Use release-tagged CAMARA JSON schemas and label `MOCK` prominently; don't promise T-Mobile/Aduna access. [CAMARA](https://camaraproject.org/resources), [SIM Swap YAML](https://github.com/camaraproject/SimSwap/blob/r3.3/code/API_definitions/sim-swap.yaml). | [02 APIs](02-tool-apis-ChatGPT.md) |
| **6** | **Privacy and authorization are a product advantage.** Scam text itself is untrusted and can attack AI agents; data minimization removes the “lethal trifecta.” | Keep secrets outside context, forbid arbitrary network calls, redact locally, require human approval for simulated effects. [Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), [CaMeL](https://arxiv.org/html/2503.18813). | [06 Agent security](06-agent-security-ChatGPT.md), [07 Privacy](07-privacy-ChatGPT.md) |
| **7** | **Free threat APIs come with limits; clean lookups do not prove safety.** Safe Browsing, VirusTotal, abuse.ch and RDAP are enough for a credible evidence chain. | Start with **one tested** URL API and RDAP; make all other integrations optional, handle 429/timeouts and do not burn hours on paid/approval gates. [Safe Browsing](https://developers.google.com/safe-browsing/reference), [VirusTotal](https://docs.virustotal.com/reference/public-vs-premium-api). | [02 APIs](02-tool-apis-ChatGPT.md) |
| **8** | **The best pitches use verified losses and current sponsor context.** FTC: ~$15.9B reported 2025 fraud losses; T-Mobile says 2025 scam/spam messages rose nearly 50% versus 2024. | Cite *both* in problem slide with denominators and years, never add FTC and FBI totals. [FTC](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud), [T-Mobile](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile). | [03 Landscape](03-scam-landscape-ChatGPT.md), [08 Pitch](08-pitch-ammo-ChatGPT.md) |
| **9** | **Show detection quality without inventing calibrated certainty.** LLM verbalized confidence is not an empirically calibrated scam probability. | Evaluate 12 scenario families and benign lookalikes; report per-type recall, benign FPR, and abstention; show evidence-based risk label. [2026 research](https://arxiv.org/html/2606.22179). | [05 Confidence](05-detection-confidence-ChatGPT.md) |
| **10** | **A contextual pause is a defensible security UX.** Warning design and reflection can affect user behavior, but real-world effect size for this specific prototype is not yet established. | Show a single salient “Pause and verify in your bank app” step before a mock transaction, not alarm spam. [USENIX](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/akhawe), [2026 mobile-payment study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13024239/). | [05 Confidence](05-detection-confidence-ChatGPT.md), [08 Pitch](08-pitch-ammo-ChatGPT.md) |

## Immediate build plan — four people, one demo

**Person A — Agent:** Get an actual NVIDIA API response and a successful function call. Create a Nemotron analyst plus controller adapter. Keep a prerecorded fixture mode if endpoint is rate-limited. [01](01-nvidia-stack-ChatGPT.md).

**Person B — APIs / backend:** Wire one live reputation checker and RDAP. Use typed schemas for CAMARA `sim-swap` and bank `hold` simulations; hardcode no real banking access. Record provenance and evidence-receipt logs. [02](02-tool-apis-ChatGPT.md), [06](06-agent-security-ChatGPT.md).

**Person C — frontend/privacy:** Build 3 stages (**before** suspicious message, **during** consented simulated protection, **after** FTC/7726/IdentityTheft recovery); use “MOCK” badges and evidence-derived nonnumeric risk levels. [04](04-competitive-landscape-ChatGPT.md), [07](07-privacy-ChatGPT.md).

**Person D — evaluation/pitch:** Generate 12 scam types + benign lookalikes + injection variations, calculate genuine metrics on holdout, make one slide with FTC/T-Mobile dated numbers, rehearse 90-second demo. [03](03-scam-landscape-ChatGPT.md), [05](05-detection-confidence-ChatGPT.md), [08](08-pitch-ammo-ChatGPT.md).

### Proposed demo state machine

```text
SYNTHETIC_MESSAGE
  -> PII_REDACTED
  -> NEMOTRON_ANALYZED
  -> REPUTATION_CHECKED
  -> TELECOM_SIGNAL_MOCKED
  -> EXPLAINED_TO_USER (with uncertainty)
  -> USER_APPROVED / USER_DECLINED
  -> BANK_HOLD_SIMULATED (only if approved)
  -> INCIDENT_RECEIPT
  -> RECOVERY_OPTIONS
```

## Three claims that must not be made

1. **“We integrated T-Mobile's real SIM-swap data / froze a real bank transfer.”** There is no authenticated operator/bank account access verified; these are synthetic fixtures and simulations. [CAMARA](https://camaraproject.org/resources), [Nessie](https://api.reimaginebanking.com/).
2. **“Our Nemotron model is 97% accurate / calibrated.”** No completed live test set or statistical calibration is provided by this research report. Generate measured results and explicitly label synthetic benchmarks. [Confidence paper](https://arxiv.org/html/2606.22179).
3. **“We keep everything on-device.”** Hosted Nemotron calls send redacted synthetic data to NVIDIA; on-device processing is limited to your implemented local parts. [API docs](https://docs.api.nvidia.com/), [Google on-device comparison](https://store.google.com/intl/en/ideas/articles/pixel-safety-features).

## Most important unverified or blocked items

| Item | Status / fallback |
|---|---|
| Exact NVIDIA account-level model endpoint success and free rate limits | **UNVERIFIED / potentially RATE-LIMITED**. Test with actual API key and use visible fixture mode if absent. [01](01-nvidia-stack-ChatGPT.md). |
| Public, immediately available T-Mobile US / Aduna CAMARA sandbox | **UNVERIFIED; likely approval >1 h**. OpenAPI-based mock only. [02](02-tool-apis-ChatGPT.md). |
| Real-time Capital One Nessie hold/cancel payment endpoint | **NOT VERIFIED**. Mock our own hold, never say real money is held. [02](02-tool-apis-ChatGPT.md). |
| Latest full FTC 2025 Consumer Sentinel Data Book with all detailed tables | **UNVERIFIED at official FTC index**. Use official 2025 FTC press/testimony data instead. [03](03-scam-landscape-ChatGPT.md). |
| Exact free-tier/terms for PhishTank, Nazario corpus and unspecified Kaggle datasets | **UNVERIFIED**. Prefer original synthetic messages and explicitly licensed corpora. [03](03-scam-landscape-ChatGPT.md). |
| Benign FPR/scam recall and “approval gate 0 failures” | **NOT MEASURED**. Must run tests before reporting any percentages. [05](05-detection-confidence-ChatGPT.md). |
| Brev GPU promo/credits | **UNVERIFIED / possible signup >1 h**. No GPU required with hosted NIM API. [01](01-nvidia-stack-ChatGPT.md). |

## Source and file navigation

- [01 — NVIDIA / Nemotron stack, orchestration, guardrails, garak, Brev](01-nvidia-stack-ChatGPT.md)
- [02 — Tool APIs: URL, domain, phone, CAMARA, banking, reporting, PII](02-tool-apis-ChatGPT.md)
- [03 — Scam landscape, 12 script families, statistics and datasets](03-scam-landscape-ChatGPT.md)
- [04 — Competitors and before/during/after channel gap table](04-competitive-landscape-ChatGPT.md)
- [05 — Honest confidence, synthetic benchmark, HAX/PAIR warning UX](05-detection-confidence-ChatGPT.md)
- [06 — Agent prompt-injection defense, CaMeL, lethal trifecta, MCP](06-agent-security-ChatGPT.md)
- [07 — Cavoukian, NIST, Texas privacy law, on-device vs cloud](07-privacy-ChatGPT.md)
- [08 — Pitch stats, real incidents, NVIDIA hackathon winners, demo script](08-pitch-ammo-ChatGPT.md)

**Provenance:** Primary official docs, government resources, developer specification repositories and scholarly papers searched on November 7, 2026. API examples are labeled illustrative, model calls were not authenticated in this research pass, and all implementation outcomes should be independently tested. Some demanded exact details remain explicitly **UNVERIFIED**, not guessed. The status of online pages, API entitlements and links can change.
