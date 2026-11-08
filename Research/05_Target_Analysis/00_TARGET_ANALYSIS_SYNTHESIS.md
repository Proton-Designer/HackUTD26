> **PRELIMINARY (superseded).** Written before the goal was locked. Final audience work: `04_TOP4_HIGHEST_LEVERAGE_AUDIENCES.md`.

# Who to protect: value × vulnerability (Safe Signal, Step 1 → 2)

Nov 7, 2026. Built from three research passes (files in this folder: `agent1_segment_harm.md`, `agent2_cost_to_tmobile.md`, `agent3_solution_gaps.md`) plus my own checks of the anchor numbers against the FTC, FBI and T-Mobile sources. Tags: **[V]** = I re-checked the source myself, **[A]** = agent-sourced with URL in its file, **[U]** = unverified, don't put on a slide yet.

## The question we're answering
Scams hit almost every T-Mobile customer, so the leading edge is the group where **high value** (money lost, cost to T-Mobile) overlaps with **most vulnerable** (can't spot it, can't recover), **inside a channel T-Mobile controls** (calls and texts), **where existing tools fail**.

## Scorecard (1 = low, 5 = high)

| Segment | Loss per victim | Volume / frequency | T-Mobile channel (calls/texts) | Value to T-Mobile | Vulnerability | Gap in existing tools | **Total /30** |
|---|---|---|---|---|---|---|---|
| **Older adults 70+ (esp. 80+), postpaid, often on a family plan** | 5 | 4 | 5 | 4 | 5 | 5 | **28** |
| Job seekers / young adults 18–29 | 2 | 5 | 4 | 3 | 3 | 4 | **21** |
| Account-takeover / SIM-swap victims | 5 | 1 | 5 | 4 | 3 | 3 | **21** |
| Prepaid / Metro, lower-income | 3 | 4 | 4 | 2 | 4 | 4 | **21** |
| Small-business owners | 5 | 2 | 2 | 3 | 2 | 3 | **17** |
| Limited-English / immigrants | 3 | 3 | 4 | 2 | 4 | 4 | **20** (low data confidence) |
| Military / veterans | 3 | 2 | 3 | 2 | 3 | 2 | **15** |

## Why older adults win (the evidence)
- **Most money lost:** FTC: people 60+ reported **$3B+** lost in 2025, up from ~$2.4B in 2024 and ~$600M in 2020; **~123,000** loss reports, up 78% since 2020 **[V]**. FBI IC3: **$7.7B** lost by 60+ in 2025, ~60% more than 2024 **[V]**.
- **Loss per victim rises with age:** FTC median loss: 60s **$640**, 70s **$1,000**, 80+ **$2,000** (up 21%), vs **$305** for people in their 20s **[V]**.
- **A few cases do most of the damage:** 6% of older adults' loss reports were six-figure losses, and they were 70% of all dollars lost **[V]**.
- **The channels are T-Mobile's:** older adults lost **$578M via phone calls** (+15%) and **$296M via texts** (+61%). **For 80+, phone calls lead on both dollars and number of reports** **[V]**. Phone-originated scams have a much higher median loss than social media ones (~$3,000 vs $599) **[A/U]**.
- **The scam types are impersonation-heavy:** government impersonation $448M, business impersonation $422M, tech support (324% more likely for older adults than younger ones) **[V]**. These are scripted, live-call, coached-payment scams, which is exactly what a carrier can see.
- **They under-report and recover least:** older adults file fewer loss reports. FTC estimates true older-adult losses at **$13.3B–$119.5B** after adjusting for under-reporting **[V]**.
- **A family member is the lever:** reports filed by someone else for the victim have far higher medians (80+: **$6,500**). Losses are bigger and found later when family isn't looped in **[A]**.
- **Value to T-Mobile:** postpaid ARPA **$155.73**, account churn rising to **1.09%**. One basis point of postpaid churn ≈ **$78M/yr** in revenue (estimate) **[A]**. 55+ plans exist ($75 for 1 line, $110 for 2). T-Mobile doesn't publish 55+ counts **[A]**.
- **The tools fail at the moment that matters:** Scam Shield judges numbers and URLs, not conversations. It's strong *before* a call, weak *during*, and offers nothing *after*. In-call detection exists only on some Pixel/Samsung phones and is off by default, and the victim can dismiss it alone. Elder tools (EverSafe, Carefull) only see bank transactions after they post. Recovery (Zelle reimbursement, IdentityTheft.gov) is voluntary or do-it-yourself **[A]**.

## Runner-up, and why not first
- **Job seekers / young adults:** most frequent losers (44% of 20–29 reports show a loss vs 24% for 70–79) and scams often start by text (BBB: half of 23,000+ job-scam reports in 2025) **[A]**. But losses are small per case (median ~$305) and the scam moves to WhatsApp/Telegram quickly, so T-Mobile sees only the opening. Good second persona or demo variation.
- **SIM swap / account takeover:** this is where T-Mobile's biggest payouts were ($33M Jones award, $350M breach settlement) **[A]**, but T-Mobile says successful swaps are down >99% since 2022 **[V]**. Pitching it as a current crisis contradicts their own report. Use it as a supporting layer (verify the number is still yours before acting), not the lead.

## Ranked list of main issues (for Step 1 write-up)
1. **Live, coached payment scams on phone calls against older adults:** impersonation of bank, government, tech support or T-Mobile; biggest dollars; T-Mobile's own channel; no one intervenes *during* the call.
2. **Nothing happens after the money leaves:** reimbursement is voluntary, reporting is DIY, victims rarely report, families find out late.
3. **Scam texts are growing fast and are the opening move:** T-Mobile saw nearly 50% more scam/spam messages in 2025 and blocked ~3B texts **[V]**; older adults' text losses are up 61% **[V]**; job scams start by text.
4. **Family members can't help in time:** caregiver-filed cases show the largest losses; no consented, phone-channel loop exists.
5. **Takeover chain (SIM swap, port-out, breach follow-on):** rare now but catastrophic per victim and T-Mobile-liable.
6. **Protection gaps by plan type:** prepaid/Metro and business lines have weaker or contradictory SIM-protection coverage (T-Mobile's own pages disagree) **[A]**.

## Draft foundation sentence (Step 2)
> "**Older adults on T-Mobile** experience **life-savings losses and isolation** from **live phone and text scams that coach them into paying**, and **nothing steps in during the call or after the money is gone**, which is why we are building **[solution]**."

Secondary user: the **adult child or caregiver** on the same family plan, who gets looped in with consent.

## Check with the team before locking
- "Older adults" is a big group. Narrowing to **75+ on a family plan with an adult child on the account** fits the data (80+ highest median, caregiver lever) and is easy to demo.
- Is NVIDIA in scope? This persona fits "beyond a chatbot" well: a multi-step agent (detect → verify independently → loop in family → hold/recover) with real tool calls.
- **Unverified, keep off slides:** T-Mobile naming "most vulnerable groups" and a 75% care-call goal (not on the newsroom page); the $3,000 phone median (agent-sourced, FTC PDF not re-opened); the Washington AG $72M/$5.4B figures.

## Sources (re-checked)
- FTC, Protecting Older Consumers 2025–2026 (summary): https://ppc.land/older-americans-lost-3-billion-to-fraud-in-2025-ftc-tells-congress/ ; report PDF: https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf
- AARP on FBI IC3 2025 + FTC 2025: https://www.aarp.org/money/scams-fraud/fbi-ftc-report-2025-losses.html
- T-Mobile, Advancing Cybersecurity at T-Mobile (Nov 2, 2026): https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile
- All other figures: URLs in the three agent files in this folder.
