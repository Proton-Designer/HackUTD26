# Agent context: Backfire (read this before working on the project)

You are helping a HackUTD 2026 team (UT Dallas, Nov 7–8, 2026) build **Backfire** for two tracks:
- **T-Mobile "Safe Signal":** "Protect customers from scams and fraud in ways we haven't thought of yet." Judged on creativity, impact, usability, security and privacy, and detection quality. Customers should feel protected before, during and after. **Synthetic data only.**
- **NVIDIA:** Nemotron "beyond a chatbot": multi-step agents, tool use, real-world applicability.

## Source of truth
1. `01_ARCHITECTURE.md`: the system design. Follow it; don't redesign silently.
2. `06_OPEN_QUESTIONS_FOR_TEAM.md`: product decisions. **Do not assume answers to open questions.** If a task depends on one, ask, or use the "Suggested" default and say so.
3. `04_PRIVACY_LEGAL_TRUST.md`: hard rules the code must respect.
4. `pipelines/00_SHARED_RULES.md` + your pipeline guide in `pipelines/` (you decide implementation details within them), `07_EXECUTION_PLAN.md` + the root `BOARD.md` (board wins): your lane, steps, the contract in `contracts/events.md` + `mock/events.json`, and the checkpoints. Only edit your own folders; only Ayman changes contracts.

## Non-negotiables (enforce in code and in reviews)
- Never process the **customer's** audio. Caller side only (Telnyx `stream_track=inbound_track` on the caller's leg in the demo).
- **Voice cloning only of the customer, only with explicit separate consent at onboarding, only when she presses Scammer Get Scammed.** The voice profile lives only in the enclave/secure store, is watermarked on output, and is deleted on opt-out. Never clone anyone else. If she has no voice consent, use a synthetic voice.
- The AI never answers calls on its own. Pre-ring: block confirmed and campaign-linked numbers; otherwise ring with Live Guard. Customer-scoped actions are automatic; network-wide and external actions need one-click analyst approval.
- Two implementations: cloud (NVIDIA confidential container) and local (Nemotron 3 Nano 4B / Bolt E4B detector on the device). Both must exist.
- The decoy has **no real customer data and no outbound tools**. It can never dial, text or contact anyone. Fake values come from code, not the LLM.
- No agent holds untrusted input + private data + external actions at once. The detector and extractor have no tools and return typed JSON only. The planner never reads raw transcripts. The handoff decision is **code**, not an LLM.
- Untrusted extracted values may be **lookup** arguments, never **action** targets without corroboration plus human approval (policy gate).
- Never hack, scan, flood or contact scammer infrastructure. Only public lookups (RDAP, public blockchains) and drafted reports.
- Store artifacts, not audio. Label every simulated component in the UI ("Simulated carrier network", "Simulated attestation").
- Fail open: if any piece breaks, the call continues normally.

## Demo stack (from `01_ARCHITECTURE.md` §15)
- **Telnyx** (decided 22:59): Call Control/TeXML; caller-only `streaming_start` with `stream_track=inbound_track`; bidirectional streaming (PCMU 8 kHz) for the decoy; conferences or bridge/unbridge for the swap; Telnyx WebRTC JS SDK for Maria's app; beeps played locally in the app.
- NVIDIA hosted endpoint `https://integrate.api.nvidia.com/v1` (OpenAI-compatible, key in `NVIDIA_API_KEY`). Detector/decoy: Nemotron 3.5 Lightning; planner/verifier: Nemotron 3 Super. Confirm exact model IDs with `GET /v1/models`. Expect rate limits, so call the detector per utterance, not per audio chunk.
- Streaming speech-to-text: Nemotron Speech Streaming / Parakeet if GPU available; else a vendor (labeled).
- SQLite/Postgres for policy, history and intel; real RDAP and blockchain lookups; simulated Scam ID, Callback Protection, DNS and traceback (CAMARA-style JSON).
- Web/PWA "T-Life" screen: live transcript, confidence bucket + why chips, buttons, after-card, protection log.

## Team context
- Repo: https://github.com/Proton-Designer/HackUTD26 · local folder `HackUTD-26/`
- Kit for process decisions: `HackUTD-2026-Kit/` (judging, architecture, pitch-demo, AI app eval)
- Research: `Research/` (T-Mobile intel, scam data, NVIDIA stack, tool APIs, privacy, agent security)
