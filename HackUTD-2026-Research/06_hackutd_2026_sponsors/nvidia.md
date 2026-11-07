# NVIDIA - HackUTD 2026 brief

Event facts (verified, https://zeroday.hackutd.co via WebFetch): HackUTD 2026 "Zero Day", Nov 7-8 2026, ECSW at UT Dallas. It is a 24-hour hackathon (hacking Sat 12:00pm; submissions due Sun 12:00pm; judging Sun 1-4pm; closing 5pm), not 36 hours. Page says challenge tracks "will be announced once hacking starts" -> no challenge text public. Sponsor tiers there: Silver = StateFarm, CBRE, Nvidia, Capital One, Spacetime; Other = AT&T, Photon. Caution: hackutd-redesign.pages.dev (unofficial/placeholder-looking) lists different tiers (NVIDIA as Title, Capital One Platinum) and six generic tracks (AI/ML, Healthcare, Sustainability, Cybersecurity, Education, FinTech); treat as unverified/stale.

## 1. Who they are
NVIDIA: GPU/accelerated-computing and AI platform company. Sells GPUs, CUDA stack, DGX/cloud inference, NIM microservices, and the open Nemotron model family. (Verified: build.nvidia.com lists Nemotron models.)

## 2. HackUTD 2026 prize/challenge
Not public. zeroday.hackutd.co lists NVIDIA only as a Silver sponsor with no event or challenge (verified). Do not assume a prize. Previous HackUTD IX Devpost page did not mention NVIDIA (verified via hackutd-ix.devpost.com fetch).

## 3. Products / access for a 24-hour build
- build.nvidia.com "Use Inference Endpoints: Free inference with leading models". Models shown on page at fetch time: Nemotron 3.5 Super VL (120B-A12B), Nemotron 3.5 Lightning (30B-A3B), Nemotron 3 Ultra (550B-A55B), DeepSeek V4.1 Flash (verified, build.nvidia.com). Full catalog behind "More Models".
- API docs: https://docs.api.nvidia.com ; base URL https://integrate.api.nvidia.com/v1 is OpenAI-compatible (unverified: third-party blog klymentiev.com/blog/nvidia-nim-free-credits).
- Access: free NVIDIA Developer account, pick a model, "Get API Key"; no credit card (unverified, third-party). Reported ~1,000 monthly credits and ~40 RPM, 429s on exceed (unverified, third-party; NVIDIA publishes no universal limits). Free tier is prototyping-only; production needs AI Enterprise (unverified).
- Hackathon-specific credits for HackUTD 2026: none found (unverified; ask booth). Other hackathons have offered NVIDIA-provided access pages (e.g., hackthelaw.notion.site Nemotron page; content did not render).
- Also relevant: NIM containers, NeMo, Riva (speech), Cosmos, Isaac; only usable if given GPU/cloud time.

## 4. Prior hackathon sponsorships
HackUTD: NVIDIA appears under "Past Sponsors" on hackutd.co (verified). Prior prize structure/winners not re-researched per instructions; HackUTD IX Devpost (https://hackutd-ix.devpost.com) has no NVIDIA prize (verified). Other 2026 hackathons show NVIDIA DGX Spark hackathons on Luma (e.g., https://luma.com/aitx-dgx-hackathon) - listing only seen in search, unverified detail.

## 5. Likely judging values (INFERENCE)
Evidence: NVIDIA pushes Nemotron/NIM open models and agentic AI on build.nvidia.com (verified). Likely rewards real use of Nemotron/NIM endpoints, agentic workflows, working demo, and technical depth.
Project directions (inference):
1. Multi-step agent using Nemotron with tool calling and a clear eval/guardrail story.
2. Vision-language app on Nemotron VL (document/photo understanding for a concrete domain).
3. Latency/cost comparison tool routing between Nemotron sizes (Lightning vs Ultra).

## 6. Questions for booth
- Is there a dedicated NVIDIA prize and its exact criteria? Required to use Nemotron/NIM?
- Hackathon credits or raised rate limits (team of 4 sharing keys)? GPU/cloud time (e.g., via Northmark Compute & Cloud, a Gold sponsor - unverified link)?
- Preferred models/endpoints; any NeMo Guardrails/Agent Toolkit expectations?

## Sources
- https://zeroday.hackutd.co (verified)
- https://hackutd.co (verified)
- https://build.nvidia.com/ (verified)
- https://klymentiev.com/blog/nvidia-nim-free-credits (unverified third party)
- https://hackutd-ix.devpost.com (verified)
- https://hackutd-redesign.pages.dev/ (unverified)
