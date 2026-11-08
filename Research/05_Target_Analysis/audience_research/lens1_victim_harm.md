# Lens 1: Victim harm data. Top 4 candidate audiences (Safe Signal)

Compiled 2026-11-07. Builds on `/mnt/user-data/outputs/T/agent1_segment_harm.md`, `agent3_solution_gaps.md`, `agent2_cost_to_tmobile.md`; primary numbers re-checked this pass against the FTC 2025-26 older-adults report, IC3 2025 report/PSA, FTC spotlights, BBB, FCC, BPI.

Tags: **[V]** = re-read at the primary source this pass. **[T]** = carried from team files (URL in that file, not re-opened). **(calc.)** = my arithmetic. **(est.)** = my inference. No carrier-level victim data exists publicly, so "T-Mobile customers" is always inferred from national data.

Source key (used below):
- FTC-OA = FTC, Protecting Older Consumers 2025-2026 (Oct 19 2026): https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf
- FTC-IMP = FTC Data Spotlight "False alarm, real scam" (Aug 2025): https://www.ftc.gov/system/files/ftc_gov/pdf/Imposter-Data-Spotlight-August-2025.pdf
- FTC-SOC = FTC Data Spotlight, social media losses (Apr 2026): https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2026/04/reported-losses-scams-social-media-eight-times-higher-2020
- FTC-TXT24 = FTC Top text scams of 2024: https://www.ftc.gov/system/files/ftc_gov/pdf/spotlight-top-text-scams.pdf
- FTC-BTM = FTC Bitcoin ATMs spotlight (2024): https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/09/bitcoin-atms-payment-portal-scammers
- IC3-25 = FBI IC3 2025 report: https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf
- IC3-BTM = IC3 crypto kiosk PSA (May 2026): https://www.ic3.gov/PSA/2026/PSA260515-2
- BBB-EMP = BBB Employment scams 2026 update: https://www.bbb.org/all/scamstudies/jobscams/employment-scams-2026-update
- BPI = Bank Policy Institute, impersonation survey (Jul 2026): https://bpi.com/impersonation
- JEC = Senate JEC letter to carriers (May 2026): https://www.jec.senate.gov/public/index.cfm/democrats/press-releases?ID=A7EF0129-3DF5-46E3-B2FE-40FA561BC81C

---

## Ranking at a glance

| Rank | Audience | H | V | C | G | $ | D | Total /30 |
|---|---|---|---|---|---|---|---|---|
| 1 | **The Coached Elder and their Helper**: 75+ postpaid phone-first customer with an adult child on the plan | 5 | 5 | 5 | 5 | 4 | 5 | **29** |
| 2 | **Fake-alert responders**: 50+ customers who reply to or call back a "fraud alert" text (bank/Amazon/Apple) | 4 | 3 | 5 | 4 | 4 | 5 | **25** |
| 3 | **Breach-notice and takeover-aftermath customers** (T-Mobile's own breach population) | 3 | 3 | 4 | 4 | 5 | 4 | **23** |
| 4 | **Recruiter-text job seekers, 18-34** (task/gig scams) | 3 | 3 | 4 | 4 | 3 | 4 | **21** |

H=Harm, V=Vulnerability, C=Channel (T-Mobile controls), G=Gap in existing tools, $=Value to T-Mobile, D=Demo-able in 24h. Scores are my judgment (est.), anchored on the numbers below.

---

## 1. The Coached Elder and their Helper (score 29)

**Definition.** A T-Mobile postpaid customer aged about 75+ who still takes unknown calls and lives alone or semi-independently, plus the adult child who pays or co-manages the family plan and would help if they knew. T-Mobile tie: the scam is a live voice call (and often a text before it) on a T-Mobile line, and the helper is already a T-Mobile account holder.

**Why highest leverage (numbers).**
- Largest and fastest-growing pool of dollars: FTC 60+ reported losses about $600M (2020) to over $3B (2025), about 123,000 loss reports. [V] FTC-OA. IC3 60+: 201,266 complaints, $7.7B, average about $38,000, 12,444 victims lost over $100K. [V] IC3-25 / https://www.fbi.gov/news/stories/scammers-target-older-adult-victims
- Per-victim harm climbs with age: median loss about $900 for 60+, **$2,000 for 80+ (+21% in a year)**, far above any other age group. [V] FTC-OA. Phone-started fraud median **$3,000** vs $599 for social-media-started. [V] FTC-OA.
- **80+ is the one age group where phone calls lead both dollars and number of loss reports** (every other age band is social-media first). [V] FTC-OA; FTC-SOC footnote 7.
- Loss is concentrated: only 6% of older adults' loss reports are $100K+, but they are 70% of dollars; $100K+ reports went from 1,136 (2020) to 6,769 (2025), +496%. [V] FTC-OA. Older adults who lost $100K+ to government/business impostors: $55M (2020) to $445M (2024). [V] https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-data-show-more-four-fold-increase-reports-impersonation-scammers-stealing-tens-even-hundreds
- **The helper lever is measurable**: 17.0% of reports for people 80+ were filed by someone else (adult child, spouse, caretaker), vs 3.8% at 60-69. Those third-party reports have median losses of **$6,500 (80+) and $5,994 (70-79)** vs about $2,000 and $1,000 overall. [V] FTC-OA footnotes 77-78. Read: by the time family is involved, the loss is already big, so earlier looping-in is the opportunity.
- Texas is a heavy market: #3 state for 60+ losses ($678.6M, IC3 2025). [T] agent1 S4.
- Trend is up while the "obvious" tools are not moving: 60+ text-scam dollars +61% in 2025. [V] FTC-OA.

**3 specific problems.**

| # | Phase | Problem | Data | Source |
|---|---|---|---|---|
| 1 | Before | Number-reputation filters do not stop a spoofed or fresh number that is then used for a personalized "your account is compromised" call. 80+ customers lose mainly on calls. | 41% of older adults' $10K+ business/government imposter losses (2024) started with a phone call; 80+ phone losses dominate. Imposter calls are usually a spoofed "bank" or "agency" number. Two surveyed banks found 40% of calls appearing to come from their own numbers were spoofed. | https://www.ftc.gov/system/files/ftc_gov/pdf/Imposter-Data-Spotlight-August-2025.pdf ; https://bpi.com/impersonation |
| 2 | During | The call is a coached payment: scammer keeps victim on the line for hours, scripts what to tell bank staff, forbids calling family, and sends them to the bank, a Bitcoin ATM, or a courier. Nobody on the carrier or bank side sees the whole call-plus-payment picture. | FTC: scammers "coach people on what to say to bank employees and tell people not to speak to friends or family"; "harrowing" extended calls. Payment methods for older adults' $10K+ imposter losses (2024): crypto 33%, bank transfer 20%, cash 16%. | https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf ; https://www.ftc.gov/system/files/ftc_gov/pdf/Imposter-Data-Spotlight-August-2025.pdf |
| 3 | After | Families learn late, and recovery is thin. Elders under-report (FTC cites 4.8% report to a BBB or a government entity); freeze-and-recover only works when reported fast. | Third-party-filed medians $6,500 (80+). IC3 Financial Fraud Kill Chain: 3,900 incidents in 2025; for 60+ victims, about $32.9M frozen of $65.4M reported (IC3 report, via agent1). FTC referred only about 700 reports to the IC3 recovery team. | https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf ; https://www.ftc.gov/system/files/ftc_gov/pdf/ftc-testimony-jec-hearing-on-the-rising-scam-economy.pdf ; [T] agent1 S4 for the $32.9M/$65.4M split |

**Serves which prompt lines.** "Customers feel protected before, during and after" (all three phases, the core unlock). "Go beyond classification: safeguards and customer-facing experiences" (helper loop, hold-and-verify). "Clear next steps, honest confidence" (plain-language, one action). "Privacy by design" (opt-in consent from the elder; the helper sees an alert, not the call). Judges' "impact" and "usability".

**Score.** Harm 5, Vulnerability 5, Channel 5, Gap 5, Value 4, Demo 5 = **29/30**.
- Gap evidence: Pixel in-call detection is opt-in and the victim can tap "Not a scam"; Android bank-app warning needs screen-share plus a participating app; caregiver tools (EverSafe, Carefull) watch money after it posts. [T] agent3 sections 1-3.
- Value: postpaid ARPA $155.73, 1 bp of churn about $78M/yr (est.). [T] agent2.

**Biggest weakness / risk.** It is the "obvious" pick (seniors), so it must be defended as a narrow dyad (75+ with an adult child), not "seniors". Also: (a) T-Mobile does not publish 55+ or 75+ customer counts [T] agent2; (b) a helper-alert feature can look like surveillance, so consent and "who sees what" must be the centerpiece; (c) FTC medians ($2,000) look modest because dollars sit in rare whale losses, so lead with the 6% / 70% stat; (d) FTC ages are only on about 46% of reports. [V] FTC-OA.

---

## 2. Fake-alert responders: 50+ customers who reply to or call back a "fraud alert" text (score 25)

**Definition.** A customer, skewing 50+, who receives a text posing as their bank, Amazon or Apple ("did you just spend $1,249?" / "call this number"), and either replies YES/NO or calls back, which hands them to a fake "fraud department" and starts the move-your-money chain. T-Mobile tie: both legs, the text and the callback, ride T-Mobile's network, and T-Mobile can see the SMS-then-call pattern.

**Why highest leverage (numbers).**
- This is the opening move of the costliest scam family: FTC imposter losses were $3.5B in 2025, and the costliest imposter scams start with a fake bank security alert. [T] agent3 sec 0 (https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025). Bank impersonation has the highest losses of any imposter category. [V] FCC https://www.fcc.gov/consumers/scam-alert/bank-impersonation-scams
- Text channel is where growth is: older-adult text-scam dollars **+61%** in 2025; the largest share (31%) of older adults' text-scam loss reports were texts impersonating well-known businesses, "particularly Amazon, Apple, and banks", styled as account-security alerts. [V] FTC-OA. All-ages text losses $470M (2024) to about $639M (2025, secondary). [T] agent1.
- Bank-alert texts historically had a **$3,000 median loss** (2022, reports up about 20x since 2019). [V] https://search.ftc.gov/business-guidance/blog/2023/06/can-your-staff-spot-five-most-common-text-message-scams
- Telecom is the main vector: banks report text/call-originated bank-impersonation scams **up 124% from 2024 to 2025**. [V] BPI.
- Older adults see these but still lose: they filed no-loss reports on text scams (32%) and phone scams (29%) most, i.e. many are spotted, some are not. [V] FTC-OA footnote 79. Honest read: this audience is not "can't spot scams", it is "gets caught on the one that is personalized and urgent".
- Congress is pressing carriers on exactly this: JEC cited FTC 2025 medians of $1,835 (phone-initiated) and $1,000 (text-initiated) per victim and asked AT&T, T-Mobile, Verizon for anti-scam plans. [V] JEC.

**3 specific problems.**

| # | Phase | Problem | Data | Source |
|---|---|---|---|---|
| 1 | Before | The lure text looks like a legitimate bank/Amazon/Apple alert with a call-back number or a YES/NO reply, so it contains no obviously bad link for URL filters to catch. | Texts impersonating businesses are 31% of older adults' text-loss reports; 51% of all text-fraud reports are business imposters (2022). Top five text scams are about half of all FTC text fraud: fake fraud alerts, wrong-number, job, fake "gifts"/delivery, Amazon-style alerts. | https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf ; https://www.ftc.gov/system/files/ftc_gov/pdf/spotlight-top-text-scams.pdf |
| 2 | During | The moment of reply or callback hands the victim to a live human on the phone. The call can show a spoofed bank or "T-Mobile" number, and the victim is told to also read back a one-time code. | Example in FTC report: spoofed Apple text, then call, then "FBI investigation", then a $52,000 wire plus Bitcoin ATM deposits. Reddit r/tmobile: customer got three back-to-back calls from a spoofed T-Mobile number, a real-looking 462 reset text, and was pushed to reply YES and read back a code (anecdote, 2024). | https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf ; https://www.reddit.com/r/tmobile/comments/1bzfcee/fraudscam_alert_inbound_call_from_spoofed_tmobile |
| 3 | After | Money leaves by bank wire or cash-to-crypto-ATM, which is hard to reverse and where victims are coached. | IC3 2025: 13,400+ complaints involving crypto kiosks, **$388M lost (+58% vs 2024)**, over half from people 50+ ($302M); about $29K per complaint (calc.). FTC (H1 2024): 86% of BTM losses were on gov/business impersonation or tech-support scams; about two of every three BTM dollars were lost by older adults. | https://www.ic3.gov/PSA/2026/PSA260515-2 ; https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/09/bitcoin-atms-payment-portal-scammers |

**Serves which prompt lines.** "Prevention + real-time protection" (the text-to-call handoff is the detectable chain). "Detection quality" (multi-signal: text content, callback within minutes, caller-ID mismatch). "Honest confidence" (show why flagged, not just "Scam Likely"). "Before, during, after."

**Score.** Harm 4, Vulnerability 3, Channel 5, Gap 4, Value 4, Demo 5 = **25/30**.
- Gap: Scam Shield judges number/URL, not the conversation; Apple call screening only collects what the caller says and is opt-in. [T] agent3.

**Biggest weakness / risk.** Heavy overlap with Audience 1 (same older victims, same chain); it is a scenario more than a group, so judges may read it as "the product" rather than "the audience". Also, vulnerability is moderate (many in this group do spot scams), and data on how many victims entered via text vs call is not split cleanly by age in public FTC tables. Phone is 11% and text 7% of all 2025 FTC loss reports by count (website/app 31%, social 28%), so this is a high-dollar slice, not the volume leader. [V] FTC-SOC.

---

## 3. Breach-notice and takeover-aftermath customers (score 23)

**Definition.** Existing T-Mobile customers whose data was in one of the company's breaches (2021: 76.6M people; 2023: about 37M accounts) or who have had a SIM swap, port-out or account takeover, and who now get "T-Mobile" calls and texts that use real details about them. T-Mobile tie: T-Mobile's own incident, own notices, own liability, own SIM Protection.

**Why highest leverage (numbers).**
- Harm is real but spread thin: IC3 personal-data-breach complaints 67,456 and $1.315B in 2025; average about $19.5K (calc.); 60+ share rising ($110M in 2023 to $324M). [T] agent1 S4.
- Follow-on phishing is the common outcome: in the ITRC survey, 53.7% saw more phishing/scam attempts after a notice (the ITRC press release says 40% for the same item; conflict). 80% of consumers got a breach notice in the prior year. Self-selected survey. [T] agent1 S22 https://www.idtheftcenter.org/wp-content/uploads/2026/01/2025-ITRC-Annual-Data-Breach-Report.pdf
- SIM swap itself is small and falling: IC3 971 complaints, **$17.4M** in 2025 vs $72.7M and 2,026 complaints in 2022; T-Mobile says successful swaps are down more than 99% since 2022 (company claim). [V] https://www.stingrai.io/blog/sim-swap-statistics-2026 (quoting IC3-25); [T] agent2. Do not pitch SIM swap as a current crisis; pitch the aftermath chain.
- Highest value to T-Mobile of any group here: breach cost about $400M charge plus $31.5M FCC plus $60M CFIUS plus $33M Jones award, about $525M documented (est.); Washington AG won summary judgment (July 2026) on 722,060 notice violations, with $72M at $100 each (illustrative) and a $5.4B statutory ceiling (theoretical). [T] agent2 rows B1-B3, A1 (B3 from a law-firm summary, not primary).
- Churn: postpaid account churn 1.09% and rising; carrier switching jumped 77% after SK Telecom's 2025 SIM breach (Korea). [T] agent2.

**3 specific problems.**

| # | Phase | Problem | Data | Source |
|---|---|---|---|---|
| 1 | Before | Breach notices are generic and often a text, so customers cannot tell a real notice from a lure, and the people who were exposed get targeted with accurate personal details. | Washington court found breach text-message notices deficient for 361,030 residents (2 violations each); 53.7% of notice recipients saw more phishing (ITRC, conflicting 40%). | https://www.jdsupra.com/legalnews/close-enough-data-breach-notifications-6919478 (via [T] agent2 B3); https://www.idtheftcenter.org/wp-content/uploads/2026/01/2025-ITRC-Annual-Data-Breach-Report.pdf |
| 2 | During | Takeover chain: spoofed "T-Mobile" call about "phones ordered on your account", password reset text, and OTP read-back. Protections are opt-in toggles with gaps. | Reddit r/tmobile spoofed-T-Mobile call (anecdote). T-Mobile support page says SIM Protection is "Not available to T-Mobile for Business, T-Mobile Prepaid, or Metro" while Metro's page says it is free to all Metro customers; SIM Protection does not block Apple eSIM transfer. | https://www.t-mobile.com/support/plans-features/sim-protection ; [T] agent2 sec 0 item 5 |
| 3 | After | Recovery is a do-it-yourself checklist; care staff are described as untrained on SIM-swap cases, and victims are drained "within minutes". | FCC/FTC complaints describe staff who "do not know how to address" fraudulent swaps; EPIC: losses happen before the carrier can act; IdentityTheft.gov: "The FTC does not resolve individual consumer reports." | https://docs.fcc.gov/public/attachments/DOC-397990A1.pdf ; https://epic.org/documents/in-re-protecting-consumers-from-sim-swap-and-port-out-fraud-fnprm ; https://www.identitytheft.gov/report |

**Serves which prompt lines.** "Customers feel protected after a threat" (the strongest "after" story). "Privacy by design" (breach-aware, minimal data). "New security features" (verified-notice channel, one-tap lock). Judges' "security and privacy".

**Score.** Harm 3, Vulnerability 3, Channel 4, Gap 4, Value 5, Demo 4 = **23/30**.

**Biggest weakness / risk.** Per-victim harm is the least proven of the four: SIM swap is $17.4M nationally and T-Mobile itself says it is down over 99%, so judges from T-Mobile may bristle at a pitch built on their breach. Breach population is huge but "breach victim" is not a measurable loss segment (agent1 flags this). Several figures here are company claims or secondary sources.

---

## 4. Recruiter-text job seekers, 18-34 (score 21)

**Definition.** Younger customers (students, new grads, gig and side-income seekers, aged about 18-34) who receive an unsolicited "recruiter" or "rate and boost" text offering remote or task work, and who are asked to move to WhatsApp or Telegram and then pay to "unlock" earnings. T-Mobile tie: the scam begins as an SMS to a T-Mobile number, the one segment where carrier visibility at the first contact is highest.

**Why highest leverage (numbers).**
- **Origin is the carrier's channel**: in 2025, half of the 23,000+ employment-scam reports to BBB Scam Tracker listed text messages as the delivery method. [V] BBB-EMP. Task-based scams (rating apps, liking videos) "became unavoidable in 2025", and BBB task reports roughly doubled over the tracking period; median loss $2,300. [V] BBB-EMP. FTC saw a 400% rise in task scams in 2024. [V] BBB-EMP quoting FTC.
- Volume and rate: FTC job-scam losses $90M (2020) to **$501M (2024)**. [T] agent1 S14-S15. 44% of 20-29 reports showed a loss vs 24% of 70-79 (2024). [T] agent1 S3. IC3 20-29: 112,069 complaints, $563.1M. [V] IC3-25.
- Telco share rising: Consumer Reports found the share of 18-29 scam attempts starting in text/messaging apps rose from 13% to 40% (2024 to 2025). [T] agent1 S19. BBB text scams rose from 9.8% to 14.9% of all Scam Tracker reports. [V] https://bbbmarketplacetrust.org/wp-content/uploads/2026/08/Risk-Report-2025-US.pdf
- Per-victim dollars are lower: FTC median for 20-29 about $305 (2025); BBB task median $2,300; IC3 employment average about $14.7K (calc.). [T] agent1.

**3 specific problems.**

| # | Phase | Problem | Data | Source |
|---|---|---|---|---|
| 1 | Before | Job offers arrive by SMS and WhatsApp from numbers that pass spam filters, impersonating recruiters, YouTube or movie studios, and look like legitimate hiring. | Half of 23,000+ BBB employment reports began by text; BBB: the public "was inundated with SMS, WhatsApp and other text-based messages about work opportunities" in 2025. | https://www.bbb.org/all/scamstudies/jobscams/employment-scams-2026-update |
| 2 | During | "Pay to get paid": small early payouts build trust, then victims deposit crypto to unlock bigger pay; sunk cost keeps them paying. The conversation moves off-network (WhatsApp/Telegram), where T-Mobile loses sight. | BBB task-scam median $2,300 (2025), victim example $65,000 sent; FTC +400% task scams (2024). | https://www.bbb.org/all/scamstudies/jobscams/employment-scams-2026-update ; https://www.ftc.gov/system/files/ftc_gov/pdf/spotlight-top-text-scams.pdf |
| 3 | After | Young victims under-report and feel blamed, and crypto sent is unrecoverable. | Only 4.8% of mass-market fraud victims report to BBB or a government entity; 23.7% of under-35 victims felt blamed vs 8.7% of 75+ (UAS, via agent1); BBB: "no path to recovery". | https://www.bbb.org/all/scamstudies/jobscams/employment-scams-2026-update ; https://www.aspeninstitute.org/wp-content/uploads/2025/12/2025_Fraud-and-Scams-Analysis_Report_FINAL.pdf |

**Serves which prompt lines.** "Prevention / education" (first-contact SMS triage). "Usability" (a student-friendly "is this offer real?" flow). "Creativity" (a different persona than the seniors every team will pick).

**Score.** Harm 3, Vulnerability 3, Channel 4, Gap 4, Value 3, Demo 4 = **21/30**.

**Biggest weakness / risk.** Smaller losses per person ($305 FTC median for 20-29; BBB $2,300) and the scam leaves T-Mobile's channel within one or two messages, so "during" and "after" protection is thin. FTC 2025 job-scam dollar totals were not found. Younger customers skew prepaid and price-sensitive, so value to T-Mobile is lower (est.).

---

## Audiences considered and rejected

1. **Crypto / investment (pig-butchering) victims**: biggest dollars (IC3 crypto-nexus $11.37B, FTC investment over $7.9B, about half of all FTC losses), but contact is overwhelmingly social media ($1.1B of the $2.1B social-media losses was investment); T-Mobile sees only the edge (wrong-number text, WhatsApp handoff). No source defines "crypto holders" as a segment. [V] FTC-SOC; [T] agent1.
2. **Romance / recently widowed**: IC3 60+ romance $584M (+50%), but about 60% of FTC romance losers say it began on social media, and bereavement is only measured in a 2017 BJS survey (widowed 22% of 60+ fraud victims) with no 2025 data; Javelin shows romance victims down 41%. [V] FTC-SOC; [T] agent1 S24, S28.
3. **Small-business owners (BEC)**: IC3 BEC $3.05B, about $123K per complaint (calc.), but the vector is email/invoice fraud, IC3 does not tag "small business", and carrier leverage is low. [T] agent1.
4. **Prepaid / Metro, immigrants, limited-English, disabled**: strong qualitative gaps (FTC says detection tools are less effective outside English; CR shows 37% of Black Americans who met a scam lost money vs 15% of White), but no per-victim loss data and no prepaid-specific harm data found; treat as hypotheses and a UX modifier (multilingual), not a lead audience. [T] agent1 rows 8, 10; agent3 gap 4.
5. **Home buyers / car sellers (mid-transaction)**: wire-fraud and fake-check scams are real, but I found no 2025 primary figure that ties them to calls/texts; the vector is email and online marketplaces, and IC3 "Real Estate" is a small category in the tables I could read. Not supported by data this pass.
6. **Military / veterans**: FTC 2024 median $700 vs $497 all, $584M total; no 2025 data and no telco-specific angle. [T] agent1 row 9.

---

## Notes for the main session
- Folding rule: "coached cash-out at a Bitcoin ATM" is a strong, definable moment (IC3 $388M, +58%, over half 50+) but it is the same victims as Audiences 1 and 2 and T-Mobile cannot see the ATM; I kept it as a problem inside #2, not a separate audience. If the team wants one memorable demo moment, it is the best candidate.
- Data cautions: FTC 2025 age tables cover only about 46% of reports; FTC (median of loss reports) and IC3 (mean of all complaints) are not comparable; the ITRC breach figure has a 53.7% vs 40% conflict; the Washington AG exposure numbers are law-firm math, not accruals.
- Items I did not re-open: agent1's S19 (Consumer Reports 13%-40%) and S20 (UAS 23.7% blamed) and agent2's cost figures are tagged [T].
