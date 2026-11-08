# Lens 2: T-Mobile's own customer base and channels (Safe Signal audience candidates)

Nov 7, 2026. Read first: brief_for_agents.md, T/agent1-3, T/00_TARGET_ANALYSIS_SYNTHESIS.md, TMobile_Strategic_Intelligence_Report.md. New primary checks this pass: T-Mobile support pages, T-Mobile newsroom cybersecurity report (Nov 2, 2026), FTC 2025-2026 older adults report, BakerHostetler on the Washington AG ruling, r/tmobile threads, BBB 2025 Risk Report, FCC.
Tags: (est.) = my estimate or inference, not a published number. UNVERIFIED = could not confirm.

## What I looked for
Audiences where (a) the scam runs through a T-Mobile product, plan, number or the T-Mobile brand, and (b) T-Mobile can see or do something no bank or phone OS can. Seven "T-Mobile-only" signals kept coming up:
1. T-Mobile knows it did NOT call you (it knows its own care outbound calls and numbers).
2. T-Mobile knows it just sent you a one-time code or "reply YES" text.
3. T-Mobile can see a live inbound call from a non-T-Mobile number on the same line at the same moment.
4. T-Mobile knows who is on the account (primary holder, authorized users, dependent lines).
5. T-Mobile has government-ID-verified age/status for 55+, military and first-responder plan holders (support page: age verified in store with photo ID within 45 days) https://www.t-mobile.com/support/plans-features/55-plus-verification
6. T-Mobile knows exactly who was in which breach and what data (SSN or not).
7. T-Mobile controls the network-level layer (Scam ID/Scam Block/Callback Protection) for ALL customers including prepaid, even where the app does not reach.

---

## AUDIENCE 1 (best): 55+ Billing Responsible Parties hit by "fake T-Mobile" calls and texts

**Definition.** The verified-55+ person who owns a multi-line T-Mobile account (T-Mobile calls them the Billing Responsible Party) and is contacted by someone pretending to be T-Mobile care, T-Mobile "fraud department" or T-Mobile rewards, with the goal of relaying a one-time code, taking over the account, and then using the number to drain a bank account.

**Why highest leverage**
- Size: NOT disclosed. T-Mobile has 142.4M customers (Dec 2025) but never publishes 55+ account counts; the 10-K only names 55+ as a discount plan. Do not put a count on a slide. https://www.stocktitan.net/sec-filings/TMUS/10-k-t-mobile-us-inc-files-annual-report-2bc151edc363.html
- Harm: people 60+ reported about $3B lost to fraud in 2025, about 5x 2020; 80+ median loss $2,000; frauds that started with a phone call keep the highest median losses. https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf FBI IC3: 60+ filed 201,266 complaints, $7.748B lost, average $38,500. https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf JEC letter to T-Mobile/AT&T/Verizon cites median losses of $1,835 for call-initiated and $1,000 for text-initiated scams (2025). https://www.jec.senate.gov/public/index.cfm/republicans/newsroom?id=3B11E394-A8C9-4CF2-BC81-6B7F424F293C
- Why T-Mobile specifically: T-Mobile itself says fraudsters "trick customers, typically those in the most vulnerable groups, into placing calls themselves" through fake customer service numbers and urgent financial alerts, and that Scam Callback Protection covers only calls the customer places. https://www.t-mobile.com/news/_admin/uploads/2026/11/Advancing-Cybersecurity-at-T-Mobile.pdf
- Value to T-Mobile: one hijacked primary account exposes every line and every financed device. One SIM-swap case cost a $33M arbitration award (agent2). 1 basis point of postpaid account churn is about $78M annualized (est., agent2, arithmetic from 34.97M accounts and $155.73 ARPA). Churn is already rising to 1.09% in Q3 2026. https://www.sec.gov/Archives/edgar/data/1283699/000128369926000129/tmus-20260930.htm
- Unique leverage: only T-Mobile can show that "T-Mobile is not calling you right now" and can match "code just sent" to "live call from a stranger."

**3 problems**
1. (BEFORE) Fake T-Mobile rewards-expiry texts are running at scale. A campaign tracked since early May 2026 used 1,000+ message variants and at least 81 domains, with fake point balances and 1-2 day deadlines; a local-news account says T-Mobile has no points program. These land on real T-Mobile customers, who find a T-Mobile-branded text more believable. Sources: https://cybersecuritynews.com/fake-t-mobile-rewards ; https://undercodenews.com/t-mobile-customers-targeted-by-a-massive-rewards-scam-as-1000-phishing-messages-flood-phones ; https://q985online.com/t-mobile-rewards-text-scam-illinois/ (secondary sources; T-Mobile's own community post not retrieved)
2. (DURING) The code-relay call. Scammer calls from a spoofed T-Mobile number, then triggers a REAL T-Mobile "reply YES / read back the code" text; the victim relays it. Documented in r/tmobile (c. 2024, 105 upvotes) https://www.reddit.com/r/tmobile/comments/1bzfcee/fraudscam_alert_inbound_call_from_spoofed_tmobile and in a 2025 KnowBe4 account where the caller already knew account number, bill amounts and the spouse's line and offered "a 30% discount." https://blog.knowbe4.com/sneaky-t-mobile-scam-and-lessons-learned Scam calls are built to keep the victim on the line so no calmer person can step in. https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2025/08/false-alarm-real-scam-how-scammers-are-stealing-older-adults-life-savings 41% of 60+ victims who lost $10K+ to business/government imposters said it began with a phone call (2024). Same FTC source.
3. (AFTER) Takeover cleanup is slow and unresolved. A r/tmobile user (recent) reports 2FA disabled, password changed and a new authorized user added online with no SMS code, then over an hour on 611 to remove the user and a request for a fraud investigation they expected to go nowhere. https://www.reddit.com/r/tmobile/comments/1x2jjou/account_hacked_2fa_disabled_password_changed (single anecdote; no volume data exists). T-Mobile's own SIM Protection page says it does not stop Apple eSIM transfers. https://www.t-mobile.com/support/plans-features/sim-protection

**Prompt lines served.** "Protect customers... in ways we haven't thought of yet" (a check no bank can run); "Go beyond classification: safeguards and customer-facing experiences, clear next steps, honest confidence, privacy by design" (on-network signals, no message content); "before, during and after a threat" (all three: pre-bunk, live interrupt, guided recovery).

**Scores (1-5):** Harm 5 | Vulnerability 4 | Channel 5 | Gap 5 | Value to T-Mobile 4 | Demo-able 5 = **28/30**

**Biggest weakness.** The T-Mobile-impersonation evidence is anecdotal (Reddit, one blog, security-news write-ups); no one publishes a count or dollar loss for "fake T-Mobile" scams, and FTC numbers are not carrier-specific. Also it is "seniors" narrowed by one sharp mechanism, so we must lead with the mechanism (code-relay signature), not the age.

---

## AUDIENCE 2 (tie): Older parent line plus the adult-child "second pair of eyes" on the same account

**Definition.** A multi-generation T-Mobile account where an older person's line (often 55+) sits next to an adult child or other family member who is the primary holder or an authorized user, so T-Mobile can see the family relationship that a bank and a phone OS cannot.

**Why highest leverage**
- Size: not disclosed (est. only: family plans drive ARPA per agent2, no multi-generation count exists).
- The scam design is to isolate: FTC says staying on the phone is meant to keep the victim from "a friend or family member in a calmer state of mind who might see through the lies." https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2025/08/false-alarm-real-scam-how-scammers-are-stealing-older-adults-life-savings
- Harm: 60+ reports of $100K+ losses were 5% of loss reports but 68% of aggregate losses (2024); older adults 53% more likely to report a friend/family-impersonation loss (2023 data). https://www.ftc.gov/system/files/ftc_gov/pdf/P144400-OlderAdultsReportDec2025.pdf ; https://www.ftc.gov/news-events/news/press-releases/2024/10/ftc-issues-annual-report-congress-agencys-actions-protect-older-adults
- Value: family accounts hold the ARPA; the 2025-26 legacy-plan migration added $50-78 bill jumps for some family plans and a lot of anger (intel report), so trust-building features on the family account have retention value (est.).

**3 problems**
1. (BEFORE) Account roles are all-or-nothing. On T-Mobile's pages, an authorized user can add Port Out Protection but only the primary holder can remove it; a 2025-26 complaint shows a second line bought an add-on the account holder says she was told it could not. https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud ; https://www.complaintsboard.com/t-mobile-st-joseph-missouri-unauthorized-charge-c2020284 I did not find a documented "alert-only trusted contact" role on T-Mobile's pages (UNVERIFIED that none exists; check T-Life).
2. (DURING) Phone-start scams are where older people lose the most per incident, and the victim is alone. FTC: median loss highest for phone-start frauds; 80+ median $2,000. https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf T-Mobile can see a long call from a non-contact number, but nothing in the support pages shows it tells a family member.
3. (AFTER) Late discovery and no recovery path. FBI froze funds in only a small share of cases: IC3 RAT initiated the Financial Fraud Kill Chain for 3,900 incidents in 2025 (FTC older adults report; the dollar figure in my excerpt was cut off, check before quoting). https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf Family often learns days later.

**Prompt lines served.** "Customer-facing experiences" and "clear next steps" (family co-pilot); "during" (live loop-in); "after" (shared recovery checklist); "privacy by design" (consent, alert shares only a flag, not call content).

**Scores:** Harm 4 | Vulnerability 5 | Channel 3 | Gap 4 | Value 3 | Demo-able 5 = **24/30**

**Biggest weakness.** Real risk of harm: elder financial exploitation is often committed by family and caregivers (FinCEN advisory https://www.fincen.gov/system/files/advisory/2022-06-15/FinCEN%20Advisory%20Elder%20Financial%20Exploitation%20FINAL%20508.pdf), so "tell the family" needs opt-in by the older person. Also evidence on the actual loop-in effect is thin, and it overlaps heavily with Audience 1 (best presented as a feature of 1).

---

## AUDIENCE 3 (tie): Customers notified of T-Mobile breaches, especially those with SSN exposed

**Definition.** Current customers whose data was in a T-Mobile breach (2021: 76M records, about 47M with SSNs per BakerHostetler) who received a T-Mobile text notice and now face lookalike phishing and a notice they could not tell from a scam.

**Why highest leverage**
- Only T-Mobile knows who was in which breach and which fields were exposed. The Washington AG alleges customers with SSNs exposed received no information about it, while those without SSN exposure were told. https://www.atg.wa.gov/news/news-releases/ag-ferguson-files-lawsuit-against-t-mobile-massive-data-breach
- July 2026: King County court granted summary judgment, finding two violations per notice for 361,030 Washington residents (722,060 total); statutory max $7,500 each; $72M at $100 each (illustrative, not a ruling); T-Mobile moved for reconsideration; AG opposed Sept 2026; trial on penalties next year. https://www.bakerlaw.com/insights/close-enough-data-breach-notifications-create-exposure ; https://communicationsdaily.com/article/2026/09/16/washington-ag-objects-to-tmobiles-attempt-to-dismiss-data-breach-judgment-2609150048
- Value: documented direct breach costs about $525M (agent2 reconciliation) plus open Washington exposure. This is the one audience where fixing the experience is also reducing legal exposure.

**3 problems**
1. (BEFORE) A notice that looks like phishing. The 2021 notice was a short text with a link; the court found both the delivery method and the content non-compliant. Customers are also told "never click links in texts" by T-Mobile's own guidance. https://mslawgroup.com/july-2026-regulatory-roundup ; https://www.t-mobile.com/dialed-in/tips-tricks/avoid-phone-scams
2. (DURING) Post-breach lures use real exposed data to sound credible. Javelin: 71% of scam losers also shared personal information with the criminals; account takeover victims rose 18% to 6.0M and new-account fraud victims 31% to 5.4M in 2025 (all consumers, not T-Mobile). https://www.aarp.org/money/scams-fraud/javelin-identity-theft-report-2024 ; https://javelinstrategy.com/whitepapers/2026-identity-fraud-study-illusion-progress I found no source on scams that specifically exploit the T-Mobile breach (UNVERIFIED; do not claim it).
3. (AFTER) Years later, customers still cannot easily see what T-Mobile knows about their exposure. FCC consent decree required security changes and $31.5M (agent2, row B2; carried not re-verified). https://www.fcc.gov/document/t-mobile-required-change-business-practices-after-data-breaches

**Prompt lines served.** "Customers feel protected... after a threat" (verifiable in-app breach status); "privacy by design" (show the customer their own exposure, no new data collection); "honest confidence."

**Scores:** Harm 3 | Vulnerability 3 | Channel 5 | Gap 4 | Value 5 | Demo-able 4 = **24/30**

**Biggest weakness.** Our own T-Mobile intel report says strategic talks with T-Mobile "must strictly avoid" the 2021-2023 breaches, class actions and Price Lock. A judge from T-Mobile may not want a pitch built on it. It is also not a niche (tens of millions) and the scam-harm link is inferred.

---

## AUDIENCE 4: Metro by T-Mobile and T-Mobile Prepaid customers (no T-Life Scam Shield)

**Definition.** Prepaid and Metro customers, who get network-level Scam ID and Scam Block but not the T-Life app version of Scam Shield, and whose account-takeover protections are described inconsistently on T-Mobile's own pages.

**Why highest leverage**
- Size: 25.9M prepaid customers (Dec 2025), 15% of service revenue, prepaid ARPU $33.33, prepaid churn 2.72% (agent2, from the 10-K and Q4 2025 release). https://s29.q4cdn.com/310188824/files/doc_financials/2025/q4/Q4-2025-Earnings-Release.pdf
- Gap is verifiable on T-Mobile's pages: "The T-Life app does not support Scam Shield with Prepaid accounts"; Scam Block turned on by dialing #662#. https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud
- Value: lower ARPU, but a huge base and high churn; a visible "protected" promise matters for a customer who can leave in a day (est.).

**3 problems**
1. (BEFORE) Protection depends on dial codes. Scam Block on prepaid is opt-in via #662#; Caller ID via #436#; nothing proactively nudges the customer. Same source as above. https://prepaid.t-mobile.com/
2. (DURING) Pages disagree on SIM Protection. The SIM Protection page says "Not available to T-Mobile for Business, T-Mobile Prepaid, or Metro" https://www.t-mobile.com/support/plans-features/sim-protection ; the account-fraud page has a Prepaid SIM Protection section https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud ; Metro says SIM Change Protection is free to all Metro customers. https://www.metrobyt-mobile.com/support/security/how-to-avoid-account-takeover-fraud A customer mid-incident cannot tell what protects them.
3. (AFTER) Weak recovery path. EPIC and CDT told the FCC prepaid plans, more used by low-income customers, "may be more vulnerable" to SIM swap and that victims have largely been unable to recover damages. https://epic.org/documents/in-re-protecting-consumers-from-sim-swap-and-port-out-fraud-fnprm (advocacy filing, "may be" language)

**Prompt lines served.** "Any approach: prevention, real-time protection... new security features" (SMS/voice-only, no app); "clear next steps" (works on a basic phone); "before/during/after" via network-level prompts.

**Scores:** Harm 3 | Vulnerability 4 | Channel 4 | Gap 5 | Value 3 | Demo-able 4 = **23/30**

**Biggest weakness.** No Metro- or prepaid-specific fraud loss data found; "low-income customers lose more" is an inference. ARPU and prepaid revenue are falling ($2.43B Q3 vs $2.63B), which weakens the value case. Metro review sites use "scam" for billing complaints, so do not count those as fraud.

---

## Considered and rejected
- **Small businesses on T-Mobile for Business** (18/30 est.): SIM Protection excluded per support page and BBB business median loss $931, but the top scams (fake invoice, BEC median $5,175) run through email, not T-Mobile channels. https://bbbmarketplacetrust.org/wp-content/uploads/2026/08/Risk-Report-2025-US.pdf
- **Military and first-responder plan holders**: T-Mobile has verified status, and FTC says military community lost $584M in 2024 (AARP summary), but I found no T-Mobile-specific scam evidence; treat as a sub-slice of Audience 1 or 2. https://www.aarp.org/money/scams-fraud/older-adults-ftc-fraud-report
- **SIM-swap/port-out victims**: T-Mobile says successful SIM swaps are down more than 99% since 2022; severe but rare (agent2). Not a scalable audience for a 24-hour demo.
- **Legacy-plan bill-shock customers** (forced July 13, 2026 migration, bill jumps up to $78): a perfect scam pretext ("call to lower your bill"), but I found no evidence yet of scams riding it, only the older "30% discount" anecdote. Use as a trigger inside Audience 1, not its own audience.
- **Kids' lines (SyncUP) and families with minors**: Javelin shows mobile numbers and logins are misused after child ID fraud, but the loss is not a scam through T-Mobile channels and per-victim data is old. https://landing.escalent.co/hubfs/24-5014J-CS-2024%20Child%20%26%20Family%20Cybersecurity%20Study.pdf
- **Recent port-ins / recycled-number holders**: Princeton found 35M US numbers disconnected yearly and reassigned, creating privacy risk for new owners, but it is a data-leak issue, not a scam-loss one. https://recyclednumbers.cs.princeton.edu/
- **5G Home Internet and T-Satellite users**: no scam evidence found; no phone-number takeover angle.

## My ranking and note to the synthesizer
1. Audience 1 (28). 2. Audiences 2 and 3 tie (24). 4. Audience 4 (23).
If the team wants one pitch: Audience 1 as the headline, with Audience 2's family loop-in as a feature (opt-in) and Audience 4's "works without the app" as the design constraint. Audience 3 is high value for T-Mobile but carries a stated brand sensitivity.
Open checks before quoting: 55+ account count (undisclosed); whether T-Life has an alert-only trusted contact; the FBI Recovery Asset Team dollar figure; the exact FCC SIM-swap compliance date; and Washington penalty (not yet set).
