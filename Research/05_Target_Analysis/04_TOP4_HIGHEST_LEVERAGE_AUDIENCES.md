# The 4 highest-leverage audiences for Safe Signal

Nov 7, 2026. Built from three independent research passes (victim data, T-Mobile's own customer base, gaps and real complaints; full files in `audience_research/`) plus the team's earlier research. I kept only audiences that showed up in **at least two** of the three passes, and re-checked the headline numbers myself.

**Tags:** **[V]** re-checked at the source by me · **[A]** sourced by a research agent with a URL in `audience_research/` · **(calc.)** arithmetic from sourced numbers · **(est.)** estimate · **(anecdote)** real complaint, shows *how* it fails, not *how often*.

## What we're scoring against
**Our goal (locked):** customers are protected, and feel protected, before, during and after a scam. That trust keeps them with T-Mobile.

**T-Mobile's prompt (verbatim):** *Safe Signal: Protect customers from scams and fraud in ways we haven't thought of yet.* Any approach: prevention, real-time protection, education, new security features. Scam detection is a core piece, not the whole product. Go beyond classification: safeguards and customer-facing experiences. Clear next steps, honest confidence, privacy by design. Synthetic data only. **Judges:** creativity, impact, usability, security and privacy, detection quality. **Big unlock:** customers feel protected before, during and after a threat.

**Leverage score (1–5 each):** Harm · Vulnerability · Channel (runs through T-Mobile's calls, texts, account or brand) · Gap (existing tools fail) · Value to T-Mobile · Demo-able in 24h.

## At a glance

| # | Audience | Who exactly | Phase where it's won | Found by | Score /30 |
|---|---|---|---|---|---|
| 1 | **The Coached Elder + Family Helper** | 75+ customer on a family plan with an adult child on the account | During → After | All 3 passes (#1 in each) | **29** |
| 2 | **"Fake T-Mobile" code-relay targets** | Account holders (skew 50+) hit by fake T-Mobile / bank alerts that push a callback or a code read-back | Before → During | All 3 passes | **27** |
| 3 | **The First-72-Hours Victim** | Any customer (worst for 60+) in the hours after they paid, shared a code or gave remote access | After | 2 passes | **25** |
| 4 | **Recruiter-text job seekers, 18–34** | Students, new grads and gig seekers who get "remote job / task" texts | Before | 2 passes | **21** |

They're distinct by **situation**, not just age: #1 is defined by family structure, #2 by a T-Mobile-specific attack pattern, #3 by a moment in time, #4 by a younger life stage and a different channel. Two other audiences came up and were rejected (see end).

---

## Audience 1: The Coached Elder + Family Helper

**Definition.** A T-Mobile customer aged about 75+, still answering unknown calls, who sits on a family plan where an adult child is the account holder or an authorized user, and who gets a real-looking alert, then a live call, then is coached into moving their own money.

**Prompt lines it serves:** *"Customers feel protected before, during and after"* (all three phases) · *"Go beyond classification: safeguards and customer-facing experiences"* (a consented family loop, hold-and-verify) · *"Clear next steps, honest confidence"* · *"Privacy by design"* (the elder opts in; the helper sees a flag, never the call) · judges' **impact** and **usability**.

### Why this is the highest-leverage niche (the numbers)
- **Biggest and fastest-growing pool of losses:** people 60+ reported **$3B+** lost to the FTC in 2025 (≈ **$600M** in 2020, ≈ **$2.4B** in 2024), across ~**123,000** loss reports **[V]**. The FBI puts 60+ losses at **$7.7B** in 2025, **~60% up** on 2024 **[V]**.
- **Loss per victim climbs with age:** median loss **$640** (60s), **$1,000** (70s), **$2,000** (80+, **up 21%** in a year), vs **$305** for people in their 20s **[V]**.
- **A few cases do the damage:** six-figure losses are **6%** of older adults' loss reports but **70%** of their dollars **[V]**.
- **It runs on T-Mobile's channel:** **80+ is the only age group where phone calls lead on both dollars and number of reports** **[V]**. Older adults lost **$578M** via calls and **$296M** via texts (texts **+61%** in a year) **[V]**. Phone-started scams have a median loss of **$3,000** vs **$599** for social-media-started ones **[A, FTC report re-read by agent]**.
- **The family lever is measurable:** **17%** of 80+ loss reports are filed by someone else (vs **3.8%** at 60–69), and those reports carry a median of **$6,500** (80+), more than 3x the overall 80+ median **[A]**. When family finds out, it's already late; looping them in earlier is the opportunity.
- **Value to T-Mobile:** postpaid ARPA **$155.73**; 1 basis point of postpaid account churn ≈ **$78M/yr** in revenue (est.) **[A]**.

### 3 problems this audience faces
| Phase | Problem | Data | Source |
|---|---|---|---|
| **Before** | The call looks legitimate, so number-reputation filters pass it. Scammers spoof the bank's real number; the victim checks the call log and it matches. | **41%** of older adults' $10K+ business/government-impostor losses started with a phone call; banks found **40%** of calls appearing to come from their own numbers were spoofed **[A]**. T-Mobile itself says scammers "sometimes still find a way around" its filters **[A]**. | FTC Data Spotlight (Aug 2025); Bank Policy Institute (Jul 2026); see `audience_research/lens1`, `lens3` |
| **During** | The coached payment: the scammer keeps the victim on the line for hours, scripts what to tell the bank, and forbids calling family. Nobody sees the whole call-plus-payment picture. | FTC: scammers "coach people on what to say to bank employees and tell people not to speak to friends or family." Older adults' $10K+ impostor losses were paid by **crypto 33%**, **bank transfer 20%**, **cash 16%** **[A]**. In-call detection exists only on some Pixel/Samsung phones, is **off by default**, and the victim can dismiss it alone; **16%** of 65+ don't have a smartphone at all **[A]**. | FTC Older Adults report (Oct 2026); Pew 2025; Google support |
| **After** | Family learns late and recovery is thin. Elder tools (EverSafe, Carefull) only alert after money posts and need a linked bank account. | Third-party-filed 80+ median **$6,500** **[A]**; only ~**4.8%** of mass-market fraud victims report to a BBB or government agency **[A]**. | FTC Older Adults report; EverSafe pricing |

**Biggest risk:** it's the "obvious" senior pick, so it must be pitched as the narrow pair (75+ elder plus adult child on the plan), with consent at the center. Elder financial abuse is sometimes committed by family, so the elder must opt in. T-Mobile doesn't publish how many 75+ customers it has.

---

## Audience 2: "Fake T-Mobile" code-relay targets

**Definition.** T-Mobile account holders (skewing 50+ and primary account holders) who get a text or call pretending to be T-Mobile, or their bank, and are pushed to call back a fake number or read back a one-time code, which hands over the account or the bank login.

**Prompt lines it serves:** *"Protect customers in ways we haven't thought of yet"* (only T-Mobile can check this) · *"Prevention, real-time protection, new security features"* · judges' **detection quality** (multi-signal: text plus callback plus code) and **security and privacy** · *"honest confidence"* (show why it was flagged).

### Why this is a high-leverage niche (the numbers)
- **Only T-Mobile can catch it.** T-Mobile knows whether it really called you, knows it just sent you a code, and can see a live call from a non-T-Mobile number on the same line. No bank or phone OS knows all three (lens 2).
- **T-Mobile says this is the gap.** Its Nov 2026 cybersecurity report says fraudsters "trick customers, typically those in the most vulnerable groups, into placing calls themselves" through fake customer service numbers and urgent financial alerts, and that its Scam Callback Protection covers only calls the customer places **[A, T-Mobile report PDF]**.
- **It's growing in T-Mobile's channel:** T-Mobile saw nearly **50% more** scam/spam messages in 2025 and blocked ~**3B** scam texts **[V]**. Banks report text- and call-originated bank-impersonation scams **up 124%** from 2024 to 2025 **[A]**. Impostor scams cost **$3.5B** in 2025, and the costliest start with a fake bank security alert **[A]**.
- **High loss per case:** FBI account-takeover complaints average about **$76,500** each in 2025 (calc.) **[A]**. A Senate committee wrote to T-Mobile in May 2026 citing median losses of **$1,835** per phone-started and **$1,000** per text-started scam **[A]**.
- **Value to T-Mobile:** one hijacked primary account exposes every line and every financed device. One SIM-swap case cost T-Mobile a **$33M** arbitration award **[A]**.

### 3 problems this audience faces
| Phase | Problem | Data | Source |
|---|---|---|---|
| **Before** | Fake T-Mobile texts are running at scale, and a T-Mobile-branded text is more believable to a T-Mobile customer. | A fake "T-Mobile rewards points expiring" campaign tracked since **early May 2026** used **1,000+** message variants and at least **81** lookalike domains **[V]**. Older adults' business-impersonation texts are **31%** of their text-loss reports **[A]**. | Malwarebytes (Sep 2026); FTC Older Adults report |
| **During** | The code-relay call: a scammer calls from a spoofed T-Mobile number, triggers a **real** T-Mobile reset text, and asks the victim to reply YES and read back the code. Scam Shield judges the number, and here the number looks like T-Mobile. | r/tmobile: three calls from a spoofed T-Mobile 1-800 number, a genuine reset text from short code 462, and an iPhone 15 Pro Max ordered on the account (anecdote). A 2025 KnowBe4 account: the caller knew the account number, bill amounts and spouse's line **[A]**. | reddit.com/r/tmobile/comments/1bzfcee; blog.knowbe4.com |
| **After** | Cleanup after a takeover is slow and the protections were opt-in. | FCC: hundreds of complaints describe store and care staff who "do not know how to address" fraudulent SIM swaps **[A]**. T-Mobile's SIM Protection is a toggle the customer must turn on, doesn't block Apple eSIM transfers, and T-Mobile's own pages disagree on whether prepaid lines get it **[A]**. | FCC fact sheet (DOC-397990A1); t-mobile.com/support/plans-features/sim-protection |

**Biggest risk:** there's no published count or dollar total for "fake T-Mobile" scams specifically; the evidence is T-Mobile's own statement plus anecdotes. Don't pitch SIM swap as a crisis, since T-Mobile says successful swaps are down **99%+** since 2022 **[V]**. Pitch the code-relay pattern instead.

---

## Audience 3: The First-72-Hours Victim

**Definition.** Any T-Mobile customer, hit hardest at 60+, in the first hours and days after they paid a scammer, read out a code or gave remote access: the window when money can still be frozen, a second "recovery" scam is coming, and nobody owns the case.

**Prompt lines it serves:** this is the **"after"** half of the big unlock, the phase every existing tool skips · *"Clear next steps"* · *"honest confidence"* (don't promise money back) · *"customer-facing experiences"* · our proof metric (scams resolved without a care call) · the NVIDIA **multi-step agent** requirement (a case agent that runs recovery steps with tools).

### Why this is a high-leverage niche (the numbers)
- **"After" is close to empty:** Scam Shield offers nothing after the fact; the FTC's IdentityTheft.gov states the FTC "does not resolve individual consumer reports"; Zelle's impostor reimbursement is voluntary and "may be discontinued at any time" **[A]**.
- **Speed is the lever:** under the FBI's Financial Fraud Kill Chain, about **$32.9M of $65.4M** reported by 60+ victims was frozen, roughly half, when reported fast **[A, check exact figure before quoting]**.
- **Most victims never report, so they never get help:** only **21%** of fraud victims told local police and **14%** told the FBI or FTC; only **43%** warned family or friends (AARP 2025) **[A]**. About **1 in 3** victims never reported to a bank, police or government (CFP Board 2026) **[A]**.
- **Value to T-Mobile:** this is where trust is won or lost, and where care calls pile up; T-Mobile is targeting digital/AI savings (~**$3B** extra profit by 2027) and has cut care calls **50%+** since 2021 **[V]**.

### 3 problems this audience faces
| Phase | Problem | Data | Source |
|---|---|---|---|
| **After** | Recovery scams target people who just lost money. | The FBI received **100+** reports (Dec 2023–Feb 2025) of scammers impersonating the IC3 to "recover" funds, and warned of fake "crypto recovery law firms" that cite the victim's exact transfer amounts **[A]**. Victims in their 70s and 80s have a **9%** higher risk of being scammed again than victims in their 50s **[A]**. | ic3.gov PSA250418, PSA250813 |
| **After** | The money rules put everything on the victim, and the window is hours. | Authorized payments fall outside Reg E protection; Zelle reimbursement is voluntary with unpublished criteria; the FBI kill chain acted on only **200 of 680** FTC referrals in 2025 **[A]**. | Zelle/Chase FAQs; FTC Older Adults report |
| **After** | Victims stay silent or feel blamed, so they stop asking for help. | **23.7%** of under-35 victims felt blamed by institutions (Aspen/UAS, n=3,812) **[A]**; about **1 in 4** non-reporters stayed silent out of embarrassment or shame (CFP Board) **[A]**. | aspeninstitute.org 2025 report |

**Biggest risk:** it's a moment, not a stable group, so judges may ask "who exactly is the customer?" The answer is to pair it with Audience 1 or 2 as their "after" half. T-Mobile also can't see the money; it only knows someone is a victim if they tell it (care, 7726) or an agent notices the pattern.

---

## Audience 4: Recruiter-text job seekers, 18–34

**Definition.** Students, new grads and gig or side-income seekers who get an unsolicited "remote job / rate-and-boost task" text, get moved to WhatsApp or Telegram, and are then asked to pay to "unlock" earnings.

**Prompt lines it serves:** *"Prevention, education"* (catch the first text) · *"ways we haven't thought of yet"* (a different persona from the seniors most teams will pick) · judges' **creativity** and **usability** (a "is this offer real?" flow for a young user).

### Why this is a high-leverage niche (the numbers)
- **The scam starts on T-Mobile's channel:** in 2025, **half** of all BBB employment-scam reports came by text, and reports **doubled** over 2024 **[V]**.
- **Fast-growing losses:** FTC job-scam losses went from **$90M** (2020) to **$501M** (2024) **[A]**; BBB task-scam median loss **$2,300** **[A]**; FTC saw a **400%** rise in task scams in 2024 **[A]**.
- **Hit most often:** **44%** of people in their 20s who reported a scam lost money, vs **24%** of people in their 70s (2024) **[A]**. Consumer Reports: the share of 18–29 scam attempts starting by text or messaging app rose from **13% to 40%** in a year **[A]**.
- **Value to T-Mobile:** lower ARPA, but these are the customers T-Mobile needs to win and keep for decades.

### 3 problems this audience faces
| Phase | Problem | Data | Source |
|---|---|---|---|
| **Before** | Job offers arrive by SMS from numbers that pass spam filters and look like real recruiters or brands. | Half of BBB employment-scam reports came by text in 2025 **[V]**; BBB says the public was "inundated with SMS, WhatsApp and other text-based messages about work opportunities" **[A]**. | BBB Employment Scams 2026 update |
| **During** | "Pay to get paid": small early payouts build trust, then deposits grow; the conversation moves off T-Mobile's network. | BBB task-scam median **$2,300**, one victim sent **$65,000** **[A]**. | BBB Employment Scams 2026 update |
| **After** | Young victims feel blamed and crypto is unrecoverable. | **23.7%** of under-35 victims felt blamed by institutions vs **8.7%** of 75+ **[A]**; BBB: "no path to recovery" **[A]**. | Aspen/UAS 2025; BBB |

**Biggest risk:** smaller losses per person (median ~**$305** for 20s **[V]**), and the scam leaves T-Mobile's channel within a message or two, so T-Mobile can mostly act **before**, not during or after. FTC 2025 job-scam totals aren't published yet.

---

## Recommendation
- **Lead with Audience 1.** It's #1 in all three passes and the only one strong on harm, vulnerability, channel and gap at once.
- **Audience 2 is our "only T-Mobile can do this" edge.** It's the signal that answers "ways we haven't thought of yet". It works as the detection layer protecting Audience 1, or as a standalone audience.
- **Audience 3 is the "after" half** every competitor skips. It's where our proof metric (resolved without a care call) and the NVIDIA multi-step agent live.
- **Audience 4 is the genuine alternative** if the team wants to avoid the senior space entirely, at the cost of smaller per-victim impact.

1, 2 and 3 stack into one story: **one family, one scam, before → during → after.** That's a team decision for the solution step, not this one.

## Considered and rejected
- **Metro / prepaid customers (25.9M):** a real product gap (T-Life doesn't support Scam Shield on prepaid) but no prepaid-specific fraud loss data. Use "works without the app" as a design constraint instead.
- **Breach-notified customers:** highest value to T-Mobile, but T-Mobile is sensitive about the 2021–23 breaches and the link to scam losses is inferred.
- **Small-business owners:** their biggest losses come via email (BEC), and T-Mobile-specific evidence is thin.
- **Crypto/investment, romance/bereaved:** big dollars, but they start mostly on social media, outside T-Mobile's channel.
- **Limited-English, disability, military:** real vulnerability, but no usable loss data. Use multilingual support as an add-on.

## Key sources (re-checked)
- FTC, Protecting Older Consumers 2025–2026: https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf (figures via https://ppc.land/older-americans-lost-3-billion-to-fraud-in-2025-ftc-tells-congress/)
- FBI IC3 2025 and FTC 2025 totals: https://www.aarp.org/money/scams-fraud/fbi-ftc-report-2025-losses.html
- T-Mobile, Advancing Cybersecurity (Nov 2, 2026): https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile
- Fake T-Mobile rewards campaign: https://www.malwarebytes.com/blog/news/2026/09/t-mobile-rewards-points-expiry-texts-are-a-phishing-scam
- BBB employment scams 2025: https://www.wibw.com/2026/05/31/bbb-reports-employment-scams-doubled-2025-task-based-schemes-surge/
- All other figures: URLs in `audience_research/lens1_victim_harm.md`, `lens2_tmobile_base.md`, `lens3_gaps_pain.md`.
