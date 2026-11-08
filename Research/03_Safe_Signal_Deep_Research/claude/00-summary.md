# 00 - Summary: the 10 findings most likely to help us win

Compiled 2026-11-07 from files 01-08. Each item links to the file that has the sources. None of the NVIDIA code was run, because the sandbox blocked integrate.api.nvidia.com. Before anything else, call `GET /v1/models` with a key to confirm the model IDs.

1. **Build on LangGraph or a plain loop with the `openai` client against `https://integrate.api.nvidia.com/v1`. Do not build on NeMo Agent Toolkit.** The deprecation claim is true: its README says it was deprecated in Oct 2026 and reaches end of life at the end of 2026. Of the successors, only NeMo Relay helps us. Add it as a LangGraph callback for traces we can show judges; it takes about 10 lines. Skip Helix and Fabric. → [01-nvidia-stack.md](01-nvidia-stack.md)

2. **Models:** use `nvidia/nemotron-3-super-120b-a12b` as the planner (1M context, tool calling). Use `nemotron-3.5-lightning-30b-a3b` for fast sub-steps. Use `nemotron-3-nano-omni-30b-a3b-reasoning` for screenshots and voicemail audio. Use `nvidia/nemotron-3.5-content-safety` as the guard. Rate limits aren't published, so give each person their own key and cache tool results. Avoid the older guard models: they're scheduled for deprecation in about 9 days. → [01](01-nvidia-stack.md)

3. **The gap to pitch:** no product follows one scam across text, callback, link, payment and recovery as a single incident. Scam Shield covers the "before" well, covers "during" weakly, and offers nothing "after" except 7726 reporting. Position the agent as the "during and after" layer on top of Scam Shield. → [04-competitors.md](04-competitors.md)

4. **Secure the agent through its design, and demo the defense live.** It is a textbook lethal trifecta. Build it this way:
   - A quarantined Nemotron call reads the raw message and returns enum-only JSON.
   - The planner never sees the raw text.
   - A Python policy gate checks every tool call.
   - Releasing a payment is not an agent tool at all.
   - Irreversible actions need a human tap.

   For the demo, run the 5 synthetic injection messages through a naive agent first, then through ours, with the audit log on screen. → [06-agent-security.md](06-agent-security.md)

5. **Opening numbers** (all verified, primary sources):
   - Reported fraud losses hit a record $15.9B in 2025, and text was the #1 contact method (FTC).
   - IC3 counted $20.9B in 2025 losses: $7.7B from people 60+ and $893M from AI-related scams.
   - 64% of scams finish within a day of first contact (GASA 2025). This one comes from the co-publisher's summary.

   → [08-pitch-ammo.md](08-pitch-ammo.md), [03-scam-data.md](03-scam-data.md)

6. **Echo T-Mobile's own words.** Its Nov 2, 2026 cybersecurity report gives:
   - about 3B scam texts blocked in 2025
   - scam and spam messages up about 50% from 2024
   - SIM swaps down more than 99%
   - a statement that it is preparing for AI-enabled fraud and AI agents

   That fits our agent exactly. → [04](04-competitors.md)

7. **Honest confidence recipe:** run self-consistency (N=5-10 samples at temperature 0.7), show 3 buckets instead of a percentage, and take no automatic action in "Unsure" (HAX G10). For evaluation, use about 150 synthetic items. Report per-type recall, false-positive rate on real-looking bank and delivery texts, the injection flip rate, and a reliability diagram with ECE. The ECE code is in the file. → [05-detection-confidence.md](05-detection-confidence.md)

8. **Warnings need action buttons.** In UK payment-fraud experiments, a risk warning plus Cancel / Call bank buttons cut fraud from about 22% to about 4%. Warning text alone cut it by about 4 points. Show warnings rarely, at the moment of payment, and vary how they look. The Nessie mock bank can hold or cancel a transfer (`PUT` or `DELETE /transfers/{id}`), so this can be shown end to end. → [05](05-detection-confidence.md), [02-tool-apis.md](02-tool-apis.md)

9. **Real tools for tonight:**
   - Safe Browsing v5, plus the OpenPhish feed checked locally
   - rdap.org for domain age, and dnstwist for look-alike domains
   - URLhaus and ThreatFox (free Auth-Key)
   - CAMARA SIM Swap, Device Swap, KYC and Number Recycling mocked from the exact spec schemas (T-Mobile's version needs an NDA)
   - the Vonage playground if we want one real SIM Swap call

   PhishTank takes no new signups, so skip it. **The FTC sites showed a shutdown notice today**, so have a copy-paste case summary ready as a fallback for reporting. → [02](02-tool-apis.md)

10. **Privacy story judges can check:**
    - Run Presidio redaction before every Nemotron call, and show the exact redacted payload in the demo.
    - Map Cavoukian's 7 principles one-to-one to features.
    - Say "on-device-first architecture, cloud fallback with redaction." Don't say "on-device," "E2EE" or "anonymous."
    - TDPSA lists fraud prevention as a permitted purpose (541.201), but consent for sensitive data and minimization still apply. We are not lawyers.

    → [07-privacy.md](07-privacy.md)

## Bonus
- **Precedent:** HackUTD 2025's NVIDIA winners used Nemotron as the reasoning core of an agent that called real tools and replanned, and both also won a second sponsor prize. No past T-Mobile track winner built a scam tool. → [08](08-pitch-ammo.md)
- **Red-team slide:** show a before-and-after garak score with `--target_type rest` against our agent endpoint. NeMo Guardrails' built-in injection detection won't catch "ignore your instructions" text in an SMS, so we need our own input check for that. → [01](01-nvidia-stack.md)

## Open items to confirm at the venue
- Exact hosted IDs for Lightning, Omni and Ultra (call `/v1/models`).
- What a Brev credit buys (ask the NVIDIA booth). We only need Brev to self-host the download-only jailbreak-detect model.
- Whether the FTC sites are up before judging.
- Whether the Nessie API host resolves.
