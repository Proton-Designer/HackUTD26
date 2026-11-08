# Lens 3: Unserved gaps and real pain (Safe Signal, T-Mobile customers)

Nov 7, 2026. Lens: where do existing protections demonstrably fail, especially DURING and AFTER a scam. I read the team files first (`agent1_segment_harm.md`, `agent3_solution_gaps.md`, `00_TARGET_ANALYSIS_SYNTHESIS.md`) and added new web evidence. Tags: **[new]** = fetched this pass; **[team]** = carried from the team files (URL in that file); **(est.)** / **(calc.)** = my arithmetic or inference. Phase tags: B = before, D = during, A = after.

## Reliability warnings (read first)
- **Reddit/BBB/GetHuman stories are anecdotes.** They show HOW tools fail, not how often. I pair each with a data point where one exists.
- **ITRC 2026 Consumer Impact Report numbers are not usable as prevalence.** Its "general consumer" panel reports 80.5% suicidal ideation, 87.9% "asked for help, never heard back", 78.9% "paid a recovery scammer", and 77.9% of scam victims in $100K+ households. That sample is clearly self-selected and non-representative (n=1,111 online, 312-409 scam victims; it also contradicts FTC/IC3 on age and income). I use it only as directional evidence on the after-scam experience, and I say so each time. https://www.idtheftcenter.org/wp-content/uploads/2026/10/ITRC-2026-Consumer-Impact-Report.pdf
- Phone/text is a minority of loss REPORTS overall (phone 11%, text 7% of 2025 FTC loss reports; but phone $1.1B and text $639M in dollars) [team]. So the audience must be one where the call/text channel is the main path.
- The $3,000 phone-origin median for 60+ is agent-sourced and the FTC PDF was not re-opened [team, flagged U in synthesis]. Do not put it on a slide until checked.

---

## RANKING (by my 6-criterion total)

| # | Audience | Total /30 |
|---|---|---|
| 1 | **Coached-payment seniors 75+ with an adult child on the plan** (narrowed "older adults") | **28** |
| 2 | **The first-72-hours victim** (any T-Mobile customer who just paid or shared a code; the "after" window) | **26** |
| 3 | **Number-as-key customers** (phone number is the root of their bank/crypto 2FA; OTP-relay and SIM-swap targets) | **24** |
| 4 | **One-phone micro-business owners** (published number, mixed personal/business line) | **21** |

Recommendation from this lens: pick #1 as the persona and build #2 as its "after" half, because #1 alone is what every team will pick and its real unserved gaps are the family loop and the post-loss window, not the first warning. If the team wants something un-obvious that still has hard data, #2 is the strongest standalone "gap" story. #3 is the best T-Mobile-specific angle but is small and partly contradicts T-Mobile's own 99% claim.

---

## 1. Coached-payment seniors 75+ with an adult child on the plan

**One sentence:** T-Mobile postpaid customers aged about 75+ (many on a 55+ or family plan, many with a non-smartphone or an iPhone) who get a real-looking bank/T-Mobile/tech-support text then call and are coached to move their own money, while an adult child who pays or manages the plan hears nothing until it is over.

**Why highest leverage**
- Biggest dollars in the best-documented group: 60+ lost $3B+ per the FTC in 2025 (about $600M in 2020) and $7.748B per IC3 (average about $38,500; 12,000+ lost over $100K) [team: ftc.gov older-adults report Oct 2026; ic3.gov 2025 report].
- It is concentrated: 6% of 60+ loss reports are six-figure and make up 70% of dollars [team, synthesis marked V]. For 80+, phone calls lead on both dollars and report counts [team V].
- Imposter scams hit $3.5B in 2025 and the costliest start with a fake bank security alert [team: ftc.gov 2026/06 press release]. That is the exact "legit text, then call, then payment" chain.
- The family lever is measurable: 17% of 80+ loss reports were filed by someone else, and those third-party reports have a median of $6,500 for 80+ (vs about $2,000 overall) [team, FTC older-adults report]. Losses found late are bigger.
- Existing tools cover the first warning (Scam Shield is strong before) and almost nothing during or after: see problems below.

**3 problems**

1. **[D] The scam looks legitimate at every step, so number/URL filters pass it.** A real bank text asks "do you recognize this charge?", the victim replies NO, and the scammer calls spoofing the bank's own fraud number; the victim checks the call log and it matches. AARP's testimony describes this chain ending with the "fake bank investigator" helping the target "transfer their assets to keep them safe", and Reddit victims describe identical caller ID. T-Mobile itself says scammers "sometimes still find a way around" filters [team].
   - Sources: https://www.congress.gov/119/meeting/house/118056/witnesses/HHRG-119-BA10-Wstate-StokesK-20250401.pdf [new]; https://www.reddit.com/r/Scams/comments/1weozci/most_involved_bank_scam_to_date/ [new, anecdote: spoofed fraud line, victim checks call log, number matches]; https://www.reddit.com/r/Scams/comments/1af50sx/zelle_scam [new, anecdote: Bank of America caller ID, "case number", Zelle "code" trick]; https://www.fcc.gov/consumers/scam-alert/bank-impersonation-scams [new: FCC says bank impersonation scams are the highest-loss impersonation category].

2. **[B/D] The protections assume a smartphone, an app, and an opt-in the person does not have.** Pew 2025: 78% of 65+ own a smartphone and 16% of 65+ have a cellphone that is not a smartphone. AARP 2025 (50+ sample): smartphone ownership drops to 76% among 80+ (so about a quarter of 80+ do not own one, calc.). Google's in-call detector is Pixel/S26-only and off by default; Apple call screening is opt-in and language-limited; T-Mobile's Scam Shield management runs through T-Life, which does not support Scam Shield on Prepaid [team]. A r/tmobile user reports a store that "could not sell me a phone without the T-Life app" and asks what older adults with flip phones do.
   - Sources: https://assistivelisteningknowledgebase.org/evidence/pew-2025-mobile (summary of Pew 2025 Mobile Fact Sheet, https://www.pewresearch.org/internet/fact-sheet/mobile/) [new]; https://www.aarp.org/content/dam/aarp/research/topics/technology/internet-media-devices/2025-technology-trends-older-adults-age-differences.doi.10.26419-2fres.00891.005.pdf [new]; https://www.reddit.com/r/tmobile/comments/1toor3q/the_tmobile_store_literally_could_not_sell_me_a [new, anecdote]; https://support.google.com/phoneapp/answer/15654065?hl=en [team].

3. **[D/A] Nobody who could help is told in time, and the freeze window is narrow.** Elder tools (EverSafe $16.99-$26.99/mo, Carefull) alert after transactions post and are bank-linked [team]. The FBI kill chain froze $10.8M across 200 actionable cases out of 680 FTC referrals, and $32.9M of $65.4M for 60+ victims, and only when reported fast [team: IC3 2025 report; FTC older-adults report]. In the AARP testimony, a bank fraud investigator intervening and "convincing her to speak to her family" was what stopped a retirement-fund theft: a human loop, not a tool.
   - Sources: https://www.eversafe.com/pricing.html [team]; https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf [team]; AARP testimony above [new].

**Prompt lines served:** "real-time protection" (during-call), "customer-facing experiences" and "clear next steps" (family hand-off), "privacy by design" (opt-in consent from the senior), "feel protected before, during and after". Weakly serves "prevention" (Scam Shield already owns that).

**Scores (1-5):** Harm 5 | Vulnerability 5 | Channel 5 | Gap 4 | Value to T-Mobile 4 | Demo-ability 5 = **28**

**Biggest weakness / risk:** It is the obvious pick; judges will have seen "seniors" many times, so the pitch must lead with the sharp slice (75+, non-app device, family-plan adult child, text-then-call-then-pay chain) and the family loop, not "detect scams for seniors". Also: monitoring a parent's calls raises consent and privacy questions; the design must be senior-opt-in and metadata-only. And Scam Shield is strong BEFORE, so claiming a "before" gap would be wrong.

---

## 2. The first-72-hours victim (the "after" window)

**One sentence:** Any T-Mobile customer, most severely 60+, in the first hours and days after they paid, read out a code, or gave remote access, when the money can still be frozen, a second scam is about to arrive, and no one owns the case.

**Why highest leverage**
- "After" is the phase where current coverage is closest to zero and where the locked goal (trust, plus "scams resolved without a care call") is won or lost. Scam Shield: after = N [team]. IdentityTheft.gov: "The FTC does not resolve individual consumer reports" [team].
- Speed is the lever and is measurable: FBI kill-chain froze about half of dollars for 60+ victims when reported ($32.9M of $65.4M) [team]; banks tell victims to report within the hour [team: banrox.com].
- Most victims never report: AARP 2025 survey found only 21% of fraud victims told local police and 14% told the FBI or FTC; only 43% warned family or friends [new]. CFP Board 2026: about 1 in 3 victims never reported to a bank, law enforcement or a government agency, and 1 in 4 of those who did not contact law enforcement stayed silent from embarrassment or shame [new].
- Repeat victimization is documented with scammer data (not self-report): victims in their 70s and 80s have a 9% greater risk of another victimization than victims in their 50s (1.33M mail-scam victims) [new].
- A T-Mobile angle exists: recovery scammers arrive by call, text and WhatsApp, which T-Mobile carries, and 7726 / care are the only places the victim already talks to the carrier.

**3 problems**

1. **[A] Institutions go silent or blame the victim, so victims stop asking.** Directional only (self-selected panel, see warning): ITRC 2026 reports 87.9% of its general-consumer scam victims asked an organization for help and never heard back, and 67.2% felt blamed. The independent Aspen/UAS analysis (n=3,812) is more reliable on blame: 23.7% of under-35 and 28.7% of Black victims felt blamed by institutions, vs 8.7% of 75+ [team: S20]. A r/personalfinance victim after Wells Fargo denied a Zelle fraud claim: "they said there's nothing they can do, no appeals process."
   - Sources: https://www.idtheftcenter.org/wp-content/uploads/2026/10/ITRC-2026-Consumer-Impact-Report.pdf [new, directional]; https://www.aspeninstitute.org/wp-content/uploads/2025/12/2025_Fraud-and-Scams-Analysis_Report_FINAL.pdf [new/team]; https://www.reddit.com/r/personalfinance/comments/s6jq5l/wells_fargo_denied_my_fraud_claim_my_life_savings [new, anecdote, 2022].

2. **[A] Recovery scams re-victimize people who just lost money.** The FBI has more than 100 reports (Dec 2023-Feb 2025) of scammers impersonating the IC3 and offering to "recover" funds, and a 2025 PSA warns of fake "crypto recovery law firms" that cite the victim's exact transfer amounts and dates and target the elderly. The IC3 2025 annual report lists recovery scams as part of the investment-fraud pattern. ITRC's 78.9% "paid a recovery scammer" is not a prevalence estimate, but it matches the FBI's description of the mechanism.
   - Sources: https://www.ic3.gov/PSA/2025/PSA250418 [new]; https://www.ic3.gov/PSA/2025/PSA250813 [new]; https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf [new/team]; https://www.idtheftcenter.org/wp-content/uploads/2026/10/ITRC-2026-Consumer-Impact-Report.pdf [new, directional].

3. **[A/D] The money-recovery rules push everything onto the victim, and the window is hours.** Authorized pushes fall outside Reg E; Zelle's imposter reimbursement is a voluntary, revocable network program with unpublished criteria [team: zelle.com; chase.com FAQ]. Banks see the transaction but not the call coaching it [team]. Reddit victims show the pattern: told to "send a support ticket through a transfer", a victim moves their own money and only later asks the real bank. FFKC acted on 200 of 680 FTC referrals in 2025 [team].
   - Sources: https://www.reddit.com/r/Scams/comments/15zq22c/just_fell_for_a_bank_scam_devastated [new, anecdote]; https://www.zelle.com/understanding-fraud-scams [team]; https://www.chase.com/personal/personal-account/faqs/send-and-receive-money [team]; https://www.ftc.gov/system/files/ftc_gov/pdf/2026-older-adults-report-10192026.pdf [team].

**Prompt lines served:** "customers feel protected ... after a threat" (this is the "after" half of the big unlock), "go beyond classification: safeguards and customer-facing experiences", "clear next steps", "honest confidence" (do not promise recovery), and the NVIDIA multi-step agent track (a case agent that runs steps with tools).

**Scores (1-5):** Harm 4 | Vulnerability 5 | Channel 3 | Gap 5 | Value to T-Mobile 4 | Demo-ability 5 = **26**

**Biggest weakness / risk:** The carrier cannot see the money, and it only knows someone is a victim if they tell it (7726, care, or an agent that notices a post-call pattern). "First-72-hours victim" is a moment, not a stable customer segment, so judges may ask "who exactly is the customer?" Fix: pair it with #1 (senior plus caregiver is who the post-loss agent serves). Also: no firm US data on how many victims T-Mobile could reach, and liability around telling someone "freeze your account now" needs careful, non-legal wording.

---

## 3. Number-as-key customers (phone number is the root of their bank/crypto 2FA)

**One sentence:** T-Mobile customers, postpaid or prepaid, whose number is the recovery/2FA key to bank, brokerage or crypto accounts, who are hit by calls that spoof T-Mobile or their bank to relay OTP codes, or by SIM swap and port-out.

**Why highest leverage**
- Direct T-Mobile exposure: the team files record a $350M breach settlement and a $33M SIM-swap award [team: threat map]; this is the one scam type that runs through T-Mobile's own systems and brand.
- Per-victim harm is high: IC3 2025 account takeover about 4,700 complaints, $359.7M (about $76,500 each, calc.) [new: IC3 2025 report]. SIM swap itself is small: 971 complaints, $17.4M [team].
- Controls exist but are opt-in and leaky: SIM Protection excludes Apple eSIM transfers; Port-Out Protection is a per-line checkbox; T-Mobile pages conflict on Prepaid/Business eligibility [team].

**3 problems**

1. **[B] The protection was not actually on.** A r/tmobile victim of a SIM swap says care told him afterward that a swap lock (72-hour delay) was added, and that he "felt kind of betrayed" because he had been assured it was already enabled and it "was never setup." Official T-Mobile pages show SIM Protection as a toggle the customer must find and keep on [team]. This is 2022, so treat as anecdote of a design pattern, not current rate.
   - Sources: https://www.reddit.com/r/tmobile/comments/tvss9e/guys_i_too_am_a_victim_of_a_sim_card_swap_today [new, 2022]; https://www.t-mobile.com/support/plans-features/sim-protection [team].

2. **[D] The attacker calls from a number that looks like T-Mobile and uses T-Mobile's own real security text as a prop.** A r/tmobile user got three back-to-back calls from "T-Mobile / 1-800-375-1126" about "phones purchased on your account", asked him to reply YES to a genuine T-Mobile password-reset text (short code 462) and read back the code; an iPhone 15 Pro Max had been ordered on his account. Scam Shield judges the number and URL, and here the number looked legitimate [team].
   - Source: https://www.reddit.com/r/tmobile/comments/1bzfcee/fraudscam_alert_inbound_call_from_spoofed_tmobile [new, 2024 anecdote]. Also FDIC OIG on spoofed bank numbers hitting business customers: https://www.fdicoig.gov/call-spoofing-scams [new].

3. **[A] After a takeover, frontline staff cannot fix it and the money is gone in minutes.** FCC fact sheet: hundreds of FCC/FTC complaints describe "customer service representatives and store employees who do not know how to address instances of fraudulent SIM swaps or port-outs", victims spending many hours on the phone and at stores, and some complaints alleging store employees were involved. EPIC/NCLC: accounts drained "within minutes", providers decline to document, victims rarely recover [team].
   - Sources: https://docs.fcc.gov/public/attachments/DOC-397990A1.pdf [new/team]; https://epic.org/documents/in-re-protecting-consumers-from-sim-swap-and-port-out-fraud-fnprm [team]; https://www.nclc.org/fcc-must-increase-accountability-in-fight-to-end-sim-swap-and-port-out-fraud [team].

**Prompt lines served:** "new security features", "privacy by design", "real-time protection" (live OTP-relay warning), "security and privacy" and "usability" judging criteria; mock CAMARA-style signals only (no real data).

**Scores (1-5):** Harm 4 | Vulnerability 3 | Channel 5 | Gap 3 | Value to T-Mobile 5 | Demo-ability 4 = **24**

**Biggest weakness / risk:** T-Mobile's own Nov 2026 report claims a 99%+ drop in successful swaps since 2022 [team], so pitching it as a current crisis contradicts the sponsor. Volume is small (971 SIM-swap complaints). Best used as a supporting layer of #1 or #2 (e.g., "verify the number is still yours before acting"), not the lead.

---

## 4. One-phone micro-business owners (published number, mixed personal and business line)

**One sentence:** Owners of salons, bars, contractors, shops and one-person firms whose personal T-Mobile number is also the business number, who cannot follow the standard advice to ignore unknown callers.

**Why highest leverage (honest version: medium)**
- Root-level reason existing tools fail: the core defense (screen unknown numbers) is unusable when the number is on cards, signs and Google and a new customer or vendor is exactly an unknown caller. FTC and FCC tell people "don't answer calls from unknown numbers" [new: fcc.gov spoofing guide]; a Wichita owner says her number is on "T-shirts, business cards, Google"; she lost hours and hundreds of dollars when her number was taken over (Verizon, not T-Mobile) [new].
- Harm per case is moderate, not huge: BBB business scam reports 1,796 in 2024 with a median loss of $1,200 (2025 through May: 505 reports, $838 median) [new]. The big dollars (IC3 BEC $3.05B in 2025) are mostly email invoice fraud, which T-Mobile does not carry [team].
- Business lines are a high-value account for T-Mobile (team value file), and takeover also destroys business income.

**3 problems**

1. **[B/D] Cannot screen unknown callers, and blocking changing numbers fails.** A BBB case: a business paid nearly $24,000 over 2.5 years to a fake trademark-protection company; after realizing, the owner blocked the numbers, but "the phone numbers continuously change." Mixed personal/business use also creates false positives on iPhone call screening [team: macobserver].
   - Sources: https://www.bbb.org/all/scamstudies/Business_scam_study/full-scam-study [new]; https://www.fcc.gov/consumers/guides/spoofing [new].

2. **[D] Spoofed bank and vendor calls target business accounts.** FDIC OIG warns that fraudsters spoof the bank's number to business customers, sometimes using real employee names, and one supervised bank reported $5M in recent attempts. BBB logged 300+ impersonation reports, many vendor fraud.
   - Sources: https://www.fdicoig.gov/call-spoofing-scams [new]; https://www.bbb.org/all/scamstudies/Business_scam_study/full-scam-study [new].

3. **[A] Number hijack means lost income and no business-specific remedy.** In the TracFone/Straight Talk port-out class action, plaintiffs describe losing a business-tied number, $200 and $360 of lost business income, and compromised accounts over the holidays; the Wichita owner reports hundreds of dollars lost. FCC rules now require lock options, but the complaints show staff still struggle [team/new].
   - Sources: https://www.classaction.org/media/barcomb-et-al-v-tracfone-wireless-inc-complaint_1.pdf [new]; https://foxkansas.com/news/local/wichita-small-business-owner-warns-of-number-takeover-scam-after-losing-access-to-line [new, other carrier]; https://docs.fcc.gov/public/attachments/DOC-397990A1.pdf [new/team].

**Prompt lines served:** "new security features", "customer-facing experiences" (call-by-call context for a line that must answer strangers), "usability". Weak on "before, during and after" for a mass-market demo.

**Scores (1-5):** Harm 3 | Vulnerability 3 | Channel 4 | Gap 4 | Value to T-Mobile 4 | Demo-ability 3 = **21**

**Biggest weakness / risk:** Evidence is thin on T-Mobile specifically (my best cases are other carriers or BBB anecdotes), per-victim loss is modest, the biggest-dollar business fraud is email, and no source tags "small business" in IC3 [team: agent1 rated segment confidence Med-Low]. A judge may find it less emotionally clear than #1 or #2.

---

## Audiences considered and rejected
- **Job seekers / 18-29 students:** high frequency and half of 23,000+ BBB job-scam reports start by text [team], but median loss about $305 and the scam jumps to WhatsApp/Telegram, so the carrier sees only the opener. Good secondary demo variant, not the lead.
- **Investment / crypto-exposed adults:** biggest dollars (IC3 investment $8.65B) but social-media-first and no source defines "crypto/HNW" as a measurable customer segment [team].
- **Romance / bereaved:** large 60+ losses ($584M IC3) but about 60% start on social media, bereavement not measured in 2025 data, and Javelin shows romance victims down 41% [team].
- **Limited-English / Spanish-first / prepaid-Metro:** real gap (FTC says tools "are often less effective for languages other than English"; Hiya/Google/Apple language limits) but evidence is qualitative and 2021-2022 [team]. Better as a modifier on #1 or #2 (multilingual explanations) than a standalone audience. It would be my next pick if the team wants an equity angle.
- **Working-age "high-income" scam victims (ITRC claim 86% aged 30-60):** contradicts FTC/IC3 age data and comes from a self-selected panel; rejected as an artifact.
- **People with cognitive decline or disability:** vulnerability 5 but no US quantitative data found [team: agent1 row 10]; cannot be defended with numbers.

## Cross-cutting gap findings worth using in the pitch (any audience)
1. Scam Shield answers "is this number bad?", but the costliest scams use a legitimate-looking number plus a real bank text; the unserved question is "is this call asking me to move money right now?" [team + new Reddit/AARP evidence].
2. "After" has no owner: banks see transactions, the FTC does not resolve individual reports, the carrier fraud team sees only the line. Victims then fall to recovery scammers (FBI PSAs, 2025).
3. The family or caregiver is the cheapest, most effective intervention on record (AARP testimony; 80+ third-party reports are the biggest losses) and no carrier tool supports a consented loop.

## Not verified / open
- The 80+ phone-origin median ($3,000) and exact 60+ channel dollar splits (FTC PDF not re-opened).
- Share of T-Mobile postpaid 55+ customers on non-smartphones (T-Mobile does not publish; Pew/AARP are national, not carrier-specific).
- Whether SIM Protection is default-on for new postpaid lines (support excerpt truncated).
- Current T-Mobile Scam Shield behavior on feature phones (management via T-Life is documented; network blocking likely works without an app, but I did not confirm).
- The Reddit posts date from 2022-2026; none establish prevalence.
