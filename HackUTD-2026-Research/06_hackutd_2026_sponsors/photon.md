# Photon - HackUTD 2026 brief

Event facts (verified, https://zeroday.hackutd.co via WebFetch): HackUTD 2026 "Zero Day", Nov 7-8 2026, ECSW at UT Dallas. It is a 24-hour hackathon (hacking Sat 12:00pm; submissions due Sun 12:00pm; judging Sun 1-4pm; closing 5pm), not 36 hours. Page says challenge tracks "will be announced once hacking starts" -> no challenge text public. Sponsor tiers there: Silver = StateFarm, CBRE, Nvidia, Capital One, Spacetime; Other = AT&T, Photon. Caution: hackutd-redesign.pages.dev (unofficial/placeholder-looking) lists different tiers (NVIDIA as Title, Capital One Platinum) and six generic tracks (AI/ML, Healthcare, Sustainability, Cybersecurity, Education, FinTech); treat as unverified/stale.

## 1. Who they are
Photon (photon.codes): messaging infrastructure for AI agents, so agents live in iMessage, WhatsApp, Telegram, Slack, Discord, voice, email, SMS rather than separate apps. Core product "Spectrum" (aka Photon 2.0). Claims SOC 2 Type II and HIPAA-capable support (verified from photon.codes fetch; claims are the company's own). Reported $4.5M raise (unverified, ecosystemastartup.com / dealroom headlines in search).

## 2. HackUTD 2026 prize/challenge
Not public. Listed only under "Other" sponsors with no event (verified, zeroday.hackutd.co). Photon also appears at HackPrinceton 2026 (notion page "photon hackprinceton 26s" did not render; contents unknown).

## 3. Products / access
- SDK: spectrum-ts, https://github.com/photon-hq/spectrum-ts ; TypeScript, onMessage/send API; providers: iMessage, WhatsApp Business, Telegram, Terminal, voice; custom via definePlatform; @spectrum-ts/imessage-local for a local Mac (verified, photon.codes and /docs).
- Docs: https://photon.codes/docs ; pricing: https://photon.codes/pricing (not read). Dashboard: app.photon.codes. Beta docs are separate from v1 (project IDs starting pho_prj_ likely beta) (verified).
- Credits: RuntimeWire reports Photon 2.0 public beta with $100 credits for builders (unverified, single secondary source: runtimewire.com/article/photon-messaging-agent-beta-100-credits). A free plan with an iMessage number was claimed by a third party (unverified).
- Contact shown in docs: a company email (ryan@photon.codes) for signup/plan questions (verified from docs fetch; do not mass-contact).
- Note: iMessage needs their hosted number or a Mac; plan setup before the event.

## 4. Prior hackathon sponsorships
HackPrinceton 2026 (page unrendered, unverified). Photon HackerNoon company profile and weekly updates exist (photon.codes/weekly-update/...), not read. No past HackUTD sponsorship found (inference: first-time).

## 5. Likely judging values (INFERENCE)
Evidence: product pitch is "agents in the conversations people already use". Likely rewards working agents reachable by real text/iMessage in a live demo, multi-channel use, and real user value.
Directions (inference):
1. Campus assistant over iMessage (UTD events, deadlines, dining) with LLM backend.
2. Group-chat agent (split bills, plan outings) using Spectrum multi-user threads.
3. Voice+text healthcare or accessibility check-in agent, leveraging their HIPAA positioning.
Pairs well with NVIDIA Nemotron as the model backend (inference).

## 6. Booth questions
- Is there a Photon prize and criteria? Required use of Spectrum?
- Hackathon credits, test iMessage numbers, rate limits, v1 vs beta recommendation?
- Can teams demo via real iMessage on stage; any reserved lines for judges?

## Sources
- https://photon.codes (verified)
- https://photon.codes/docs (verified)
- https://github.com/photon-hq/spectrum-ts (referenced, not opened)
- https://runtimewire.com/article/photon-messaging-agent-beta-100-credits (unverified)
- https://zeroday.hackutd.co (verified)
- https://somethingreat.notion.site/photon-hackprinceton-26s (unrendered)
