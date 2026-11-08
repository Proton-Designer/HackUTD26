# Problem, audience and positioning

Nov 7, 2026. Condensed from `Research/05_Target_Analysis/` (goal lock, top-4 audiences), the AI-outlook analysis, and `03_TMOBILE_EXISTING_PROTECTIONS.md`. Tags: **[V]** checked primary source, **[A]** from our research files (URLs there), **[E]** our estimate.

## The prompt (T-Mobile "Safe Signal")
> "Protect customers from scams and fraud in ways we haven't thought of yet."
- Scam detection is a core piece, **not the whole product**. Go **beyond classification**: safeguards and customer-facing experiences.
- **Clear next steps, honest confidence, privacy by design.** Synthetic data only.
- Judges: **creativity, impact, usability, security and privacy, detection quality.**
- Big unlock: customers **feel protected before, during and after** a threat.

NVIDIA track: Nemotron **beyond a chatbot**: multi-step workflows, planning agents, tool integration, real-world applicability.

Locked goal (`00c_GOAL_DECISION.md`): **customer trust and security** is the design goal. Retention is the business "why." Care-call deflection is the proof metric.

## The insight
Everyone else will build "detect the scam, warn the user." Number blocklists fail because **scammers rotate cheap phone numbers**. The things they **can't cheaply change** are their script, callback numbers, phishing domains and the wallet, gift card or bank account the money goes to.

> **Follow the scam, not the number.** When a scammer gets through, the customer presses one button and our AI takes over in her own voice. It keeps the scammer talking until they reveal how they get paid, and every scam call makes every other customer safer.

## Why this is a T-Mobile problem (and not just the bank's)
- The scam call and text travel over T-Mobile's network. The bank only sees the final step, when money moves.
- The phone number is the key to bank and email resets. T-Mobile guards that key. FCC SIM-swap rules (2023) and the $33M Jones arbitration award make it T-Mobile's responsibility.
- Scammers impersonate T-Mobile itself ("those in the most vulnerable groups" calling fake care numbers, in T-Mobile's own words) **[V]**.
- Congress is asking carriers, not banks: the Senate JEC wrote to T-Mobile, AT&T and Verizon in May 2026 for their anti-scam strategies, citing median losses of $1,835 for scams that start with a call and $1,000 for ones that start with a text **[A]**.

## Key numbers
| Fact | Figure | Tag |
|---|---|---|
| US reported fraud losses 2025 (FTC) | $15.9B, ~3M reports | [V] |
| FBI IC3 losses 2025 / people 60+ | $20.9B / $7.7B | [V] |
| AI-related losses (IC3 2025) | $893M; ~$352M of it from people 60+ | [A] |
| Calls T-Mobile tagged as scam/spam in 2025 | ~29B; 800+ scam calls identified or blocked per second | [V] |
| Scam texts T-Mobile blocked in 2025 | ~3B; scam messages up about 50% vs 2024 | [V] |
| Scam Block retention | ~99% of users who turn it on keep it on | [V] |
| Median loss when a scam starts by phone vs on social media (60+) | $3,000 vs $599 | [A] |
| Personalized scam attempts | 20% of scam attempts were personalized; 32% of phone-started ones (CR, Oct 2026) | [V] |
| AI spear-phishing (peer-reviewed) | 54% click rate vs 12% control, 92% lower cost | [V] |
| AI voice phishing compliance (N=4,100) | 16.5% | [V] |
| Gen-AI fraud forecast (Deloitte) | $12.3B (2023) → $40B (2027) | [V, projection] |
| Value of 0.01 point of monthly postpaid churn | ≈ $78M/yr | [E] |
| Cost per assisted care contact | $13.50 median | [A] |
| Willing to trade some privacy for AI scam protection | 69% (Harris Poll for Alloy, 2025; asked about banks) | [V] |
| Say automatic call screening would be useful / would pay extra | 70% / 40% | [V] |
| Confident their personal data is private | 32% (CR, Oct 2026) | [V] |

## What T-Mobile does NOT do today (our space)
From `03_TMOBILE_EXISTING_PROTECTIONS.md`:
- No analysis of call content for scams. All call protection is based on the number and calling patterns.
- No AI that answers or engages scam calls.
- No warning during an incoming call that gets through.
- No consumer deepfake or voice-clone detection, even though T-Mobile's own report names deepfake voice scams as a threat.
- No extraction of scammer infrastructure from conversations.
- Reports give no feedback: customers never hear an outcome.
- No guided recovery for victims.
- Strongest protections are off by default.

Competitors: AT&T has piloted a network AI receptionist since Sep 2025, so "AI screens calls" isn't new. **No carrier turns scam conversations into intelligence about the scammers.**

## Demo persona (one named user, per the kit and the past-winner data)
**Decided: an older woman** (name TBD, e.g., "Maria", 78, a T-Mobile customer). This matches the highest loss per victim: a $2,000 median loss for 80+, phone calls as the #1 channel for 80+, and $7.7B lost by people 60+ in 2025 (FBI).
- **Pitch caution:** "seniors get scammed" is the crowded default. Open with the *moment* (the scammer realizing he's talking to an AI in her voice), not with the demographic. The creativity is in the mechanism (live handoff, voice continuity, campaign immunity), not in the audience.

## Pitch lines
- "Everyone else warns you about scams. We let you hand the scammer to an AI that sounds like you, and turn the call against them."
- "Never your voice analyzed: only the caller's side, inside a sealed NVIDIA container (or on your own phone)."
- "Scammers change numbers for pennies. They can't change where the money goes."
- "One scam attempt makes every T-Mobile customer immune to that script."
