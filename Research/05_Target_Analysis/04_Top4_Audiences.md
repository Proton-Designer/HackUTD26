# Safe Signal: the 4 highest-leverage niche audiences

Nov 7, 2026. Built on `00_TARGET_ANALYSIS_SYNTHESIS.md`, `01_segment_harm.md`, `02_cost_to_tmobile.md`, `03_solution_gaps.md`, the goal lock (`00c_GOAL_DECISION.md`), the past-winner dataset (`HackUTD-2026-Research/`) and the kit (`HackUTD-2026-Kit/`). Fresh web checks were added for caregivers, language and job scams (sources at the bottom).
Tags: **[V]** primary or checked source · **[A]** from our agent research files (URL there) · **[E]** our arithmetic, method shown · **[J]** our judgment.

---

## 0. The prompt we're scoring against (T-Mobile "Safe Signal", opening ceremony slide)

> **"Protect customers from scams and fraud in ways we haven't thought of yet."**
> - Any approach: prevention, real-time protection, education, new security features
> - Scam detection is a core piece, **not the whole product**
> - Go beyond classification: **safeguards and customer-facing experiences**
> - **Clear next steps, honest confidence, privacy by design**
> - You create the data: synthetic scam messages and scenarios, no real customer data
> - Judges look for: **creativity, impact, usability, security and privacy, detection quality**
> - The big unlock: customers **feel protected before, during and after** a threat

Our locked goal (`00c`): **Goal 6, customer trust and security** is what we design for. Retention (Goal 2) is the business "why" and care-call deflection (Goal 4) is the proof metric.

### What "highest leverage" means here
An audience is high leverage when it does all four of these:
1. **Real harm, with numbers.** That gives us **impact**.
2. **The scam runs through calls, texts or the account**, which T-Mobile controls. That makes our **detection** something T-Mobile could actually ship.
3. **Existing tools fail in the "during" or "after" phase.** That gives us room for **creativity** ("ways we haven't thought of yet").
4. **Few other teams will pick it**, while it still matters to T-Mobile. That is how we get noticed.

### Why "unique" matters, from the past-winner data
- Most scam winners in our dataset built for **older adults plus a family alert**: ScamShield (HooHacks '26, top 3), Kill-Switch (DubHacks '26, **T-Mobile 3rd**), Guardo, Trustline, Guardião, and Hey Buddy (older immigrants). Our own pitch-ammo file says scam winners "protect older adults [and] alert a trusted family member." Expect many teams in the room to do the same.
- **Zero** scam winners in the dataset targeted job seekers or breach-exposed customers. **One** (Hey Buddy, HackGT 13) targeted language barriers, and it won. That tells us judges value the angle and that it is still open on a T-Mobile track.
- Kit finding 4.2 / sponsor card: T-Mobile winners solved the stated problem for a **named persona**. Kit finding 0.9: "execution of a familiar idea" is *less* common among winners (39% W vs 52–60% non-winners).
- At HackUTD 2025 the T-Mobile track was "crowded with near-identical sentiment dashboards" (sponsor card). Differentiating on persona matters more than polish.

---

## 1. Summary

| # | Audience | One-line why | Leverage score /40 [J] | Crowding risk |
|---|---|---|---|---|
| 1 | **The family-plan account holder protecting an aging (80+) parent** | Biggest dollars per victim, phone-led, and the paying T-Mobile customer already holds the line controls | **35** | Medium (we reframe away from the crowded "grandma app") |
| 2 | **Spanish-speaking / limited-English households, often on Metro or prepaid (DFW)** | English-first tools, T-Mobile's weakest published protection tier, highest churn, and in our backyard | **33** | Low |
| 3 | **Job seekers and new grads (18–29)** | The fastest-growing scam whose opener lands in T-Mobile's SMS channel, and judges and testers are this persona | **26** | Very low |
| 4 | **Customers whose data already leaked (breach-notified)** | Leaked fields make the next scam convincing. It's T-Mobile's largest realized cost, and "after" is empty in every tool | **31** | Very low |

Score = 8 criteria from `00_TMobile_Goals.md`, each scored 1–5: harm, vulnerability, value to T-Mobile, churn risk, care cost, channel control, tool gap, demo/NVIDIA fit. Full grid in §6.

---

## 2. Audience 1: The family-plan account holder protecting an aging parent

**Who exactly:** an adult child, usually 40–60, who is the **Primary Account Holder** on a T-Mobile family plan that includes a parent aged 75–80+. The parent is the one who gets scammed. The account holder is the one who can act.

**Why the reframe:** the elder data is the strongest in the whole research set, but "app for grandma" is the most-built scam idea. Building for the **account holder** makes T-Mobile's paying customer the user. It also uses controls only the carrier has, which no bank or caregiver app can copy.

### Problem 1: The biggest losses are found late, and by someone else
- FTC 2025: median loss for **80+ is $2,000**, up 21%, vs **$305** for people in their 20s **[V]**.
- When **someone else files the report** for the victim, the 80+ median jumps to **$6,500**, which is **3.25×** the overall 80+ median [E]. **17%** of 80+ reports are filed by someone else **[A, FTC Older Adults report]**.
- **6%** of older adults' loss reports are $100K+, and they account for **70% of all dollars** **[V]**.
- Read: the family finds out after the money is gone, and the cases they find are the catastrophic ones.

### Problem 2: The weapon is a phone call, and only the victim is on it
- For 80+, **phone calls lead on both dollars and number of reports**. Older adults lost **$578M via calls (+15%)** and **$296M via texts (+61%)** in 2025 **[V]**.
- Median loss when the scam starts by phone: **$3,000**, vs **$599** on social media, about 5× [A].
- Older adults who lost $100K+ to government/business impersonation: **$55M (2020) to $445M (2024)**. The script is "move your money to protect it" **[V]**.
- The only live-call detectors (Pixel/Galaxy S26) are **off by default**, and the victim alone can dismiss them ("Not a scam"). Nobody else is told **[A]**.

### Problem 3: Caregiver tools only see the money after it moves
- **51.3M** Americans care for an adult 50+, and **56%** of them manage that person's finances. That is about **28.7M people** [E: 51.3M × 56%] **[V, AARP/NAC 2025]**.
- Caregiver products (EverSafe $16.99–$26.99/mo, Carefull) alert **after a transaction posts**, and they're blind to the call that coached it **[A]**.
- Recovery is thin: the FBI freeze path acted on **200 of 680** FTC referrals and froze **$10.8M** in 2025, against **$7.7B** lost by people 60+ **[V]**.

### Why this is the highest-leverage audience (the numbers)
- **Harm pool:** FTC 60+ reported losses were **$3B** in 2025 (5× 2020). The FTC estimates the true figure at **$13.3B–$119.5B** after under-reporting. FBI IC3 counted **$7.748B** from 60+, which is **37% of all IC3 dollars from 20% of complaints** **[V]**.
- **Value to T-Mobile:** the account holder pays the **$155.73 postpaid ARPA**, and ARPA is per account, so family accounts drive it. **1 basis point of postpaid account churn ≈ $78M/yr** [E, `02`]. Churn is already **1.09% and rising** **[V]**.
- **T-Mobile already gave this person the levers:** only the Primary Account Holder can remove Port-Out Protection. SIM Protection, line controls and the T-Life pop-up exist **[A]**. We would be the first to wire them to a live scam signal.
- **T-Mobile's own words:** fraudsters trick "those in the most vulnerable groups" into calling fake care numbers (Advancing Cybersecurity, Nov 2, 2026) **[V]**.
- **Prompt fit:** **before** = consented guardian rules on the parent's line. **During** = a live-call risk signal reaches the account holder, with a "call back the real bank" step. **After** = a case file plus a bank freeze request within the hour. **Privacy by design** = the parent opts in and sees exactly what is shared.

---

## 3. Audience 2: Spanish-speaking / limited-English households (heavy on Metro and prepaid, DFW)

**Who exactly:** Spanish-dominant adults, often on Metro by T-Mobile or prepaid, frequently with a bilingual family member who translates. The DFW angle is literal: Dallas County is the venue.

### Problem 1: The protection is English-first, and their plan tier gets less of it
- The FTC says anti-fraud tools "are often **less effective for languages other than English**" **[V]**. Pixel call detection launched English-only, and Apple call screening supports a limited set of languages **[A]**.
- T-Mobile's own support pages say **SIM Protection is "not available to T-Mobile Prepaid or Metro"**, and the Scam Shield app doesn't support Prepaid. Metro's page says the opposite. The pages **contradict each other**, so say "pages disagree" on stage, never "no protection" **[A]**.

### Problem 2: When targeted, they're less equipped and lose more
- Pew: only **59% of Hispanic adults** say they know how to avoid scams, vs **75% of White adults** **[A]**.
- Consumer Reports 2025: **29% of the lowest-income** people who met a scam lost money vs **10%** at $100K+. **37% of Black** vs **15% of White** respondents lost money. Prepaid skews lower-income and Latino **[A]**.
- AARP: Latino adults are most targeted by **government-impostor, utility and grandparent** scams, which are call-heavy and sit in T-Mobile's channel **[A]**.

### Problem 3: Authority-impersonation scams are surging, and victims don't report
- FTC immigration-scam complaints: about **960/yr (2021–2024) to nearly 2,000 in 2025** (about 2×), with **$94.4M** reported stolen over five years, "certainly an undercount" **[V, ProPublica on FTC data]**.
- Researchers found **4,000+ fraudulent immigration-service messages** in Spanish-language WhatsApp groups (Jan–Sep 2025), reaching **31,000+ users**. Impersonating authority is the top threat Spanish-language fact-checkers flag **[V, DDIA]**.
- The FTC says Latino communities **report at lower rates** (barriers: not knowing where to report, distrust of government). Reports often arrive through **relatives who translate** **[V/A]**.

### Why this is high leverage (the numbers)
- **Size, local:** Texas has **8.27M Spanish speakers**, **3.21M** of them limited-English (39%) **[V, MPI 2024 ACS]**. **34.4%** of Dallas County speaks Spanish at home, and there are **67,000+ Spanish limited-English households** **[V]**. **41.2%** of Dallas city residents speak a non-English language at home **[V]**.
- **Value to T-Mobile:** prepaid is **25.9M customers** and **15% of service revenue**. Its churn is **2.72%/month**, about 2.7× postpaid phone **[V]**. **1 bp of prepaid churn ≈ $12.4M/yr** [E: 25.9M × 0.0001 × 12 × $33.33 ARPU × 12]. Prepaid revenue is **falling** ($2.63B to $2.43B per quarter), so retention matters here **[V]**.
- **Care cost:** each assisted care contact costs a **$13.50 median** vs $1.84 self-service (Gartner) **[A]**. Non-English cases are the hardest to resolve without a human.
- **Tool gap:** every "during" tool in our competitor table is weak or missing for non-English users **[A, `03` matrix]**.
- **Prompt fit:** **creativity** (nobody on a T-Mobile track has done it), **usability** (native-language explanations), **honest confidence** (detection quality reported per language). Nemotron's multilingual ability is the NVIDIA hook, but **check the model card before claiming it**.
- **Validated by judges elsewhere:** Hey Buddy (HackGT 13 winner) protected older immigrants on English calls.
- **Caveat:** there is no US dollar-loss figure by language. Pitch the gap and the population, not a made-up loss number.

---

## 4. Audience 3: Job seekers and new grads (18–29)

**Who exactly:** college students and recent grads hunting for internships and first jobs. That is literally the people at HackUTD.

### Problem 1: The scam opens in the text inbox, T-Mobile's channel
- BBB: employment-scam reports **doubled, from 11,748 (2024) to 23,234 (2025)**, and **half began by text message** **[V]**.
- Consumer Reports: the share of 18–29 scam attempts that start by **text/messaging rose from 13% to 40%** (2024 to 2025) **[A]**.
- "Fake job / task" is one of the FTC's **top 5 text scams**. Together the top 5 are about half of all text fraud reports **[V]**.

### Problem 2: Losses are climbing fast, through a stepwise "deposit to unlock" trap
- FTC job-scam losses: **$90M (2020) to $501M (2024)**, a 5.6× rise **[V]**. FBI IC3 counted **$363M** in employment losses in 2025 (24,688 complaints) **[V]**.
- Task scams pay small "commissions," then demand crypto deposits to unlock earnings. BBB's task-scam median loss is **$2,300**, and the median across all job scams is **$1,000** (2025) **[V/A]**.
- Students also get **fake-check** jobs sent to their student email (FTC alert, May 2025) **[V]**.

### Problem 3: The group most likely to lose, and least likely to say so
- **44%** of fraud reports from people in their 20s show a money loss, vs **24%** for 70–79 **[V]**.
- **23.7% of under-35s felt blamed** after a scam vs **8.7% of 75+** (Aspen/UAS) **[A]**. Shame suppresses reporting.
- **46%** of rental-scam loss reports come from 18–29, a second, housing-season hit **[A]**.

### Why this is high leverage (the numbers)
- **Channel control:** this is the highest share of **text-originated** loss of any segment in our research. T-Mobile blocked about **3B scam texts** in 2025 with messages **up about 50%**, so the opener goes straight through T-Mobile's network **[V]**.
- **Growth:** reports **×2 in one year (BBB)**, losses **×5.6 in four years (FTC)**.
- **Evidence we can gather tonight:** the kit says "who you asked beats how many" and "a segment at UT Dallas or the venue lets you test in person." That gives us 5 real target users in 30 minutes and verbatim quotes for the pitch, which no other audience offers.
- **Value to T-Mobile:** first-plan customers are long-lifetime accounts (no published 18–29 ARPU, so don't invent one).
- **Prompt fit:** **education** (the brief lists it) at the exact moment the offer arrives. **Before** (score the recruiter text). **During** (the "pay to unlock" step). **After** (shame-free reporting plus a bank call script).
- **Weakness to own:** losses per victim are smaller, and the conversation moves to WhatsApp/Telegram, so T-Mobile sees only the opener. Design for the opener and the hand-off moment.

---

## 5. Audience 4: Customers whose data already leaked (breach-notified)

**Who exactly:** anyone who got a breach notice in the past year, from any company. Frame it as T-Mobile protecting you from **everyone's** leaks, so the pitch isn't a dig at T-Mobile's own breaches.

### Problem 1: Leaked data makes the next scam convincing
- ITRC: **80%** of consumers got a breach notice in the past year, and **88%** of them had a negative consequence. **53.7%** saw **more phishing** afterward (the ITRC press release says 40%, so cite the range) **[A]**.
- The 2023 API leak exposed **name, DOB, plan and number of lines** for about 37M accounts. Those are exactly the fields needed to fake a convincing carrier text **[A]**.
- T-Mobile's own security report names **"AI-enabled fraud"** and **"deepfake voice scams on an industrial scale"** as priorities **[V]**.

### Problem 2: Breach notices are generic, and how they're written is now a legal liability
- Washington AG v. T-Mobile: in **July 2026** a court found **2 violations for each of 361,030** residents (722,060), over the quality of text-message breach notices. That's about **$72M at $100 per violation**, with a theoretical ceiling of about **$5.4B** [E, law-firm illustration, not a court figure] **[A]**.
- Documented direct breach-related cost to T-Mobile over five years is about **$525M**: $350M settlement plus charges, $31.5M FCC, $60M CFIUS, and the $33M Jones SIM-swap award [E, `02`].

### Problem 3: Recovery is do-it-yourself, and takeover signals are judged one at a time
- IdentityTheft.gov: "The FTC **does not resolve individual consumer reports**." The victim does all the calling **[A]**.
- IC3 2025: **67,456** personal-data-breach complaints, **$1.315B** lost. Losses for 60+ rose **$110M to $254M to $324M** **[A]**. Javelin: account-takeover victims **+18%** in 2025 **[A]**.
- SIM Protection and Port-Out Protection are **opt-in toggles**, and SIM Protection does **not** block Apple eSIM transfers. The 2-year ID protection after 2021 has **expired** **[A]**.

### Why this is high leverage (the numbers)
- **Population:** the 2021 breach hit **76.6M** people and 2023 about **37M** accounts. Industry-wide, **80%** of consumers got a notice last year **[A]**.
- **Where T-Mobile actually loses money:** breach aftermath is T-Mobile's **largest realized fraud-related cost** (about $525M), and the WA case shows post-incident communication itself is a loss driver **[A]**.
- **Tool gap:** the "after" column in our solutions table is empty or partial for every product **[A, `03`]**.
- **Prompt fit:** strongest on **"ways we haven't thought of yet"**. Examples: a personal exposure map ("your DOB and plan leaked, so here are the 3 scams that will quote them back to you"), a watchlist that flags incoming texts quoting leaked fields, and one-tap PIN rotation plus SIM/Port-Out lock. **Clear next steps** is literally the product.
- **Risks:** touchy in front of T-Mobile judges, so lead with "any breach" and the customer. Don't pitch SIM swap as a current crisis, since T-Mobile reports it is **down >99%** since 2022 **[V]**.

---

## 6. Full scoring grid [J]

| Criterion (from `00_TMobile_Goals`) | 1 Account holder + aging parent | 2 Spanish/LEP, Metro/prepaid | 3 Job seekers / new grads | 4 Breach-exposed |
|---|---|---|---|---|
| Harm (loss × frequency) | 5 | 3 | 3 | 4 |
| Vulnerability (spot / report / recover) | 5 | 5 | 3 | 3 |
| Value to T-Mobile (ARPA, growth) | 5 | 3 | 3 | 4 |
| Churn risk after an incident | 3 | 5 | 3 | 4 |
| Care / support cost | 3 | 4 | 2 | 4 |
| T-Mobile channel control (calls, texts, account) | 5 | 4 | 4 | 4 |
| Gap in existing tools | 5 | 5 | 4 | 5 |
| Demo in 24h + NVIDIA multi-step fit | 4 | 4 | 4 | 3 |
| **Total /40** | **35** | **33** | **26** | **31** |
| Uniqueness vs past winners | 2 | 4 | 5 | 5 |

Scores are our judgment, made to compare these four. They are not judge scores. #3 scores lowest on value but is the easiest to validate with real users at the venue.

## 7. Recommendation
- **Highest harm:** #1, but only with the account-holder reframe. Without it we're the eighth "grandma scam app."
- **Best balance of value and uniqueness:** **#1 + #2 combined** as one persona: *a bilingual adult child who holds the family plan for a Spanish-speaking parent.* That keeps the elder loss data, adds a gap nobody has filled on a T-Mobile track, matches the FTC/AARP finding that relatives translate and report, and is local to DFW.
- **Most "haven't thought of yet":** #4. Keep it as the creative second flow (the leaked-field watchlist) if we have time.
- **Fastest real evidence:** #3. Use it for hour 1–3 interviews even if it isn't the lead persona.

## 8. Considered and dropped
- **Small-business owners:** BEC is $3.05B, but it's email-driven, so T-Mobile has weak channel control and the data is thin **[A]**.
- **SIM-swap / crypto holders:** severe, but leading with it contradicts T-Mobile's own −99% claim **[V]**.
- **Romance / bereaved:** about 60% start on social media, outside T-Mobile's channel **[A]**.
- **Military / veterans:** no T-Mobile-relevant fraud data **[A]**.

## Sources (new in this file; everything else is in `01`/`02`/`03`)
- FTC, Protecting Older Consumers 2025–2026: https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf
- FTC imposter release, Jun 2026: https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025
- AARP/NAC, Caregiving in the US 2025 (50+ companion): https://www.caregivingintheus.org/wp-content/uploads/2026/07/family-caregivers-of-adults-age-50-plus-caregiving-in-us-2025-series.doi_.10.26419-2fppi.00412.001.pdf
- ProPublica, immigration scam complaints doubled (Apr 2026): https://www.propublica.org/article/trump-immigration-scams-complaints-doubled-ice
- DDIA, WhatsApp Weaponized Part 2 (Dec 2025): https://ddia.org/en/whatsapp-weaponized-how-scammers-target-us-latinos-part2
- Migration Policy Institute, Texas language data (2024 ACS): https://www.migrationpolicy.org/data/state-profiles/state/language/TX
- Dallas Morning News on ACS household language (Dec 2023): https://www.dallasnews.com/news/2023/12/07/almost-half-of-dallas-households-speak-languages-other-than-english
- BorderReport/KXAN, Texas county language shares: https://www.borderreport.com/news/census-bureau-estimates-1-in-3-texans-speak-a-language-other-than-english-at-home
- Census QuickFacts, Dallas city: https://www.census.gov/quickfacts/fact/table/dallascitytexas/LND110210
- BBB employment scams 2026 update (via Daily Herald summary): https://www.dailyherald.com/20260528/business/bbb-investigation-reveals-reports-of-job-scams-have-doubled-from-last-year/
- FTC consumer alert, college students and job scams (May 2025): https://consumer.ftc.gov/consumer-alerts/2025/05/college-students-avoid-scammers-while-you-job-hunt
- CNBC on IC3 2025 employment losses: https://www.cnbc.com/make-it/2026/11/06/binance-hack-fake-job-interview-scams.html
- T-Mobile, Advancing Cybersecurity (Nov 2, 2026): https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile
- Past-winner evidence: `HackUTD-2026-Research/04_deep_dives/data/deepdive_all.jsonl`, `outputs/sponsor_cards.md`, `outputs/findings.md`; pitch-ammo `Research/03_Safe_Signal_Deep_Research/claude/08-pitch-ammo.md`
