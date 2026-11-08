# T-Mobile Safe Signal Threat Map: Attacks on T-Mobile and Comparable Carriers, 2018–2026

T-Mobile is hurt most when an attacker takes control of a customer's phone number or account by working through T-Mobile's own people, tools, APIs and vendors, and when the scams that follow a breach reach the customer. The largest documented losses fall in that window: SIM swaps, port-outs and post-breach follow-on fraud. T-Mobile's own products (Scam Shield, SIM Protection, Port-Out/Account Takeover Protection) are strong at blocking known-bad calls and locking accounts in advance. They are weak at connecting the signals that show a takeover is happening and at guiding customers after a breach.

## TL;DR
- T-Mobile has publicly confirmed at least seven customer-data incidents from 2021 to 2026. The two largest were the August 2021 breach (76.6 million people, including SSNs and driver's license data) and the January 2023 API abuse (about 37 million accounts). Together they cost $350 million in class-action payments, a $150 million security spending commitment, and a $31.5 million FCC consent decree. Nearly every incident fed SIM-swap and account-takeover risk.
- The attack that shows up again and again at T-Mobile and its peers is human-channel takeover. Attackers phish employees, bribe them, or exploit stolen internal tools, then use that access to move a customer's number (Lapsus$ inside the Atlas tool in 2022; SIM-swap crews claiming internal T-Mobile access 100 times in seven months of 2022; $300-per-swap bribe texts in 2024). The same playbook moved into vishing of SaaS and CRM systems at carriers in 2025–2026: Salesforce campaigns, Charter, Odido and TELUS.
- The best pitch position is an agent that works during the attack. It would correlate carrier signals (SIM change, port-out, device swap, care contact, new login) with the customer's own context, step in in real time, and run a recovery playbook personalized to each breach. That covers before, during and after, which is exactly where T-Mobile's current tools stop.

---

## research/tmo-00-summary.md — One-page brief

### 10 most important findings
1. **The 2021 breach is the anchor case.** T-Mobile confirmed it on August 16–17, 2021.\[1\] It exposed data on about 76.6 million current, former and prospective customers, including SSNs and driver's license numbers for many of them.\[2\]\[3\] Account PINs were exposed for 850,000 prepaid customers.\[4\] The attacker, John Binns, told the WSJ he got in through an unprotected router.\[2\] The class settlement was $350M plus $150M in security spending; payments began in May 2025.\[5\]
2. **The January 2023 API abuse ran for about six weeks before anyone noticed.** Data pulls began around November 25, 2022, T-Mobile detected them on January 5, 2023, and disclosed them in an 8-K on January 19, 2023. About 37M postpaid and prepaid accounts were affected.\[6\]\[7\] Google Fi customers were caught up in it, and at least one Fi customer reports a SIM swap on January 1, 2023 that lasted 1 hour 48 minutes.\[8\]
3. **Internal tools are the crown jewels.** In March 2022, Lapsus$ used employee VPN credentials bought on a criminal market to get into T-Mobile's Atlas account-management tool, which can perform SIM swaps. Extra verification blocked their attempts on FBI and DoD-linked accounts.\[9\] They then downloaded about 30,000 source-code repositories (Krebs, April 22, 2022).\[10\]\[11\]
4. **SIM-swap crews treated T-Mobile employee access as a renewable resource.** Telegram logs from Star Fraud and two other crews show they claimed internal T-Mobile access on 100 separate occasions over seven months in 2022, mostly by phishing employees (Krebs, February 2023).\[12\]
5. **Insider bribery is now done openly.** In April 2024, current and former T-Mobile and Verizon staff received texts offering "up to $300 per sim swap." T-Mobile said it "did not have a systems breach."\[13\]\[14\] In March 2026, T-Mobile reported a single-customer incident to the Maine AG caused by a vendor employee's improper access, exposing SSN, driver's license and account PIN.\[15\]\[16\]
6. **A single SIM swap can cost a carrier more than an FCC fine.** An arbitrator ordered T-Mobile to pay $33M (made public March 20, 2025) over a February 21, 2020 SIM swap in which a T-Mobile employee moved Josh Jones's number and roughly $38M in crypto was stolen.\[17\]\[18\]
7. **Regulators are pushing toward zero trust and phishing-resistant MFA.** The FCC's $31.5M T-Mobile consent decree (September 30, 2024) covers incidents in 2021, 2022 and 2023, splits into a $15.75M penalty and $15.75M in security investment, and requires "zero trust and phishing-resistant multi-factor authentication."\[19\]\[20\]
8. **Salt Typhoon reached T-Mobile only at the edge.** T-Mobile says the attackers came in through a connected wireline provider's network and reached only edge routing gear, not customer data (Jeff Simon, November 27, 2024; Bloomberg account, August 2026).\[21\]\[22\] The FBI and CISA said PRC actors stole call records at other carriers (November 13, 2024).\[23\] The August 27, 2025 joint advisory cites about 200 US organizations and more than 80 countries.\[24\]
9. **Carrier data now leaks through cloud and SaaS vendors.** AT&T's 2024 Snowflake theft took call and text records for nearly all its wireless and MVNO customers (taken April 14–25, disclosed July 12, 2024).\[25\]\[26\] The 2025–2026 Salesforce vishing and OAuth campaigns reached Verizon (claimed), Charter (April 2026), Odido (6.2M customers, February 2026) and TELUS Digital.\[27\]\[28\]\[29\]
10. **SIM-swap losses reported to the FBI are falling, but scam-text losses are rising.** IC3 SIM-swap losses went from $72.65M in 2022 to $48.8M in 2023, $25.98M in 2024 and $17.37M in 2025.\[30\] FTC-reported text-scam losses hit $470M in 2024, five times the 2020 level,\[31\] and T-Mobile says it saw nearly 50% more scam and spam messages in 2025 than in 2024.\[32\] Fraud is moving from taking over a number toward deceiving the customer.

### Top 3 positioning angles
1. **"Catch the takeover while it's happening, not after the bank account is empty."** Every major T-Mobile loss started with a phone number changing hands: Jones ($38M), Google Fi (1h48m), Lapsus$ in Atlas. SIM Protection only helps customers who turned it on in advance; our agent watches the SIM-change, port-out and care-contact sequence in real time and holds high-risk changes until the real owner confirms.
2. **"After the breach letter, we become the customer's bodyguard."** T-Mobile has sent breach notices to tens of millions of people, and Washington's attorney general sued partly because those notices were unclear.\[33\] Our agent reads what was exposed for that specific customer, rotates what can be rotated, and flags any call or text that quotes the leaked data back to them.
3. **"Trust the person, verify the action, even when it's our own rep."** Bribery texts ($300 per swap), phished employee credentials, and a 2026 vendor-employee insider case all show that the weakest link is a legitimate tool used for an illegitimate reason. Our agent scores each care or retail action against the customer's risk profile and the employee's normal behavior, then asks for step-up proof before it executes.

### 5 most citable facts
1. Approximately 37 million current postpaid and prepaid customer accounts had data taken through a single API, starting on or around November 25, 2022 (T-Mobile Form 8-K, January 19, 2023, sec.gov).\[6\]
2. The $31.5M FCC settlement splits into a $15.75M penalty and $15.75M in cybersecurity investment, covering breaches in 2021, 2022 and 2023, including an API incident and a sales-application breach (FCC, September 30, 2024, as reported by Reuters and BleepingComputer).\[19\]
3. Josh Jones won a $33M arbitration award against T-Mobile over a February 21, 2020 SIM swap that stole about $38M in crypto (Greenberg Glusker, March 20, 2025; SecurityWeek).\[17\]\[34\]\[35\]
4. T-Mobile says it has reduced successful SIM-swap attacks "by more than 99% since 2022" and blocked "nearly 3 billion scam and spam texts" in 2025 (T-Mobile Newsroom, November 2, 2026).\[36\]
5. FTC: consumers reported losing $470 million to text-message scams in 2024, more than five times the 2020 figure (FTC Data Spotlight, April 2025).\[37\]

---

## research/tmo-01-incidents.md — Part 1: T-Mobile incident history

### Chronological table

| # | Incident | Discovered → Disclosed (gap) | Actor / motive | Initial access | Taxonomy | Scale / cost |
|---|---|---|---|---|---|---|
| 1 | 2018 customer data exposure | Detected Aug 20, 2018 → disclosed Aug 23, 2018 (3 days) | "An international group" (per T-Mobile) / UNVERIFIED motive | API | Bulk data theft | ~2M (about 3% of 77M customers, per T-Mobile spokesperson via CyberScoop/Motherboard, Aug 24, 2018) |
| 2 | 2019 prepaid exposure | UNVERIFIED (Nov 2019) | Unknown | UNVERIFIED | Bulk data theft | ~1M prepaid (UNVERIFIED) |
| 3 | 2020 email-account compromise and Dec 2020 CPNI exposure | UNVERIFIED (Mar 2020, Dec 2020) | Unknown | Employee email phishing (UNVERIFIED) | Data / CPNI theft | ~200K CPNI (UNVERIFIED) |
| 4 | Feb 21, 2020 SIM swap of Josh Jones | Feb 2020 → award public Mar 20, 2025 | Criminal / financial | T-Mobile employee performed swap; 8-digit PIN bypassed | SIM swap, insider/care | ~$38M crypto stolen; $33M award |
| 5 | Mint Mobile port-outs | Jun 8–10, 2021 → Jul 10, 2021 (~1 month) | Unknown / financial | Account access, likely care tool (UNVERIFIED) | Unauthorized port-out | "very small number" |
| 6 | August 2021 breach | Unit221B tip Aug 13 → confirmed Aug 16–17, 2021 (days, but WA AG alleges T-Mobile learned only from an outside source) | John Binns / notoriety, grievance, data sale | Exposed router / testing gateway, then brute-force | Bulk data theft | 76.6M people; $350M class + $150M security spend |
| 7 | March 2022 Lapsus$ intrusions | Mar 2022 → Apr 22, 2022 (via Krebs; ~weeks) | Lapsus$ / notoriety, SIM-swap profit | Stolen employee VPN creds bought on Russian Market | Internal tool abuse, source-code theft | ~30,000 repos; no customer data per T-Mobile |
| 8 | 2022 SIM-swap crew access (Star Fraud et al.) | 2022 → Krebs Feb 2023 | Com SIM-swap crews / financial | Employee phishing of internal tools | SIM swap via insider tools | 100 claimed access events in 7 months |
| 9 | January 2023 API abuse | Activity from ~Nov 25, 2022; detected Jan 5, 2023; 8-K Jan 19, 2023 (~6 weeks undetected + 14 days to disclose) | Unknown / financial | Abused single API "without authorization" | API abuse/enumeration | ~37M accounts; part of FCC $31.5M |
| 10 | Google Fi spillover from #9 | Jan 2023 → Fi notices ~Jan 31, 2023 | Same as #9 | Same as #9 | Downstream SIM swap | Count undisclosed |
| 11 | Feb–Mar 2023 PIN/SSN exposure | Intrusion Feb 24–Mar 30; discovered Mar 27; notices Apr 28, 2023 | Unknown | Not disclosed (secondary sources: sales application) | Account data theft (PINs) | 836 customers |
| 12 | Kroll employee SIM swap | Aug 2023 (UNVERIFIED date) | SIM-swap actor / financial | T-Mobile account of Kroll employee swapped | Downstream SIM swap | FTX/BlockFi/Genesis claimant data |
| 13 | Mint Mobile 2023 breach | Data reportedly taken ~Mar 2023 → notices Dec 22, 2023 (~9 months, per secondary source) | Unknown / data sale | Not disclosed | Bulk data theft | Undisclosed count |
| 14 | April 2024 SIM-swap bribe texts | Apr 15–16, 2024 | Unknown SIM-swap buyers / financial | Texts to employees' personal/work phones | Insider bribery | Industry-wide (T-Mobile, Verizon, Charter staff) |
| 15 | Salt Typhoon attempt | Fall 2024 → Nov 27, 2024 blog; Aug 2026 Bloomberg detail | PRC MSS-linked / espionage | Via interconnected wireline provider; spoofed router | Nation-state edge persistence | No customer data per T-Mobile |
| 16 | March 2026 vendor-insider incident | Discovered Mar 5, 2026 → notice Mar 31, 2026 (26 days) | Vendor employee / unknown | Insider misuse of vendor access | Insider/vendor data access | 1 customer (Maine AG filing) |
| 17 | Oct 2026 BYOD extortion claim | Claimed Oct 7, 2026 | BYOD gang / extortion | UNVERIFIED | Extortion claim | UNVERIFIED; no samples |

### Per-incident detail

**#4 Josh Jones SIM swap (Feb 21, 2020; award public March 20, 2025)**
- **Who was targeted.** Company: a T-Mobile employee carried out the swap; the attacker also got into T-Mobile systems by unknown means.\[35\] Customer: a high-value crypto holder. Downstream: exchange and wallet accounts that relied on SMS recovery.
- **What was taken.** About 1,500 BTC and roughly 60,000 BCH, worth about $38M at the time. The attacker got past his 8-digit PIN.\[35\]
- **Cost and outcome.** $33M award, including more than $6.5M in fees, after a 12-day arbitration in fall 2023. The arbitrator found violations of the Federal Communications Act; T-Mobile paid and has moved to seal the findings, per Greenberg Glusker.\[38\]\[39\]
- **Remaining gap.** A PIN alone does not stop an insider or someone with tool access.

**#5 Mint Mobile port-outs (June 8–10, 2021; disclosed July 10, 2021)**
- An unauthorized person viewed subscriber account information and ported numbers to another carrier.\[40\]\[41\] Harmed: prepaid MVNO customers and any accounts using those numbers for SMS 2FA. Vector undisclosed (UNVERIFIED).
- Mint has been a T-Mobile subsidiary since 2023 and can use T-Mobile's SIM Protection in T-Life (secondary source: efani.com).\[42\]\[43\]

**#6 August 2021 breach**
- **Timeline.** Unit221B told T-Mobile on August 13, 2021 that its data was for sale on a forum (Wikipedia summary). T-Mobile confirmed the breach on August 16–17.\[1\]\[44\]
- **Actor and access.** John Binns, then 21 and living in Turkey, told the WSJ (August 26, 2021) he found an unprotected router and called T-Mobile's security "awful."\[2\]\[45\] He was indicted in the Western District of Washington (reported January 2024) and was reported to be in Turkey awaiting extradition as of December 2024.\[1\]
- **What was taken.** About 7.8M current postpaid customers (name, DOB, SSN, driver's license/ID); about 40M+ former or prospective credit applicants; 850,000 prepaid customers (names, numbers, account PINs);\[46\]\[47\] IMEI/IMSI for some; business name, federal tax ID and contacts for business customers. Total later put at about 76.6M people.\[48\]
- **Downstream.** Leaked SSNs enable identity theft at lenders.
- **Cost.** $350M class fund plus $150M in 2022–2023 security spending\[1\] (approximately $400M pre-tax charge in Q2 2022).\[48\]\[49\] Final approval June 29, 2023; Eighth Circuit affirmed July 29, 2024 (secondary source); payments began May 2025 (Keller Rohrback).\[5\]\[49\] Payouts: $25 per person, $100 for Californians, up to $25,000 for documented losses.\[50\]
- **What T-Mobile changed.** Reset exposed PINs, offered two years of ID protection,\[1\] and promoted Scam Shield and Account Takeover Protection (press release, August 17, 2021).\[4\]\[51\]
- **Criticism.** Washington AG Bob Ferguson sued under the Consumer Protection Act on January 6, 2025 in King County Superior Court, covering 2,025,634 Washingtonians, 183,406 of whom had SSNs exposed (GeekWire, January 6, 2025). The suit alleges T-Mobile learned of the breach from an outside source, sent "brief" texts that omitted legally required information, and was "downplaying its severity and sending notices to affected consumers that did not disclose all the information that had been compromised." T-Mobile called the suit "a surprise."

**#7 Lapsus$ (March 2022)**
- **Access.** Employee VPN credentials bought on Russian Market. T-Mobile said "monitoring tools detected a bad actor using stolen credentials to access internal systems that house operational tools software" (Krebs, April 22, 2022).\[9\]\[52\]
- **Reached.** Atlas (can perform SIM swaps); FBI/DoD-linked accounts blocked by additional verification; Slack and Bitbucket, about 30,000 repositories downloaded.\[9\]\[52\]
- **Lesson.** Extra verification on government accounts worked, which supports a "VIP step-up" for every high-risk customer.

**#8 SIM-swap crews (2022)**
- Star Fraud and two other groups claimed internal T-Mobile access 100 times in seven months of 2022 by phishing employees through fake SSO and VPN pages sent by text.\[53\] Targets: retail and care staff; end victims mostly crypto holders.
- Five alleged Scattered Spider members were charged in November 2024; Noah Urban was sentenced to 10 years (August 2025) over at least $800K stolen from five SIM-swap victims.\[53\]

**#9 January 2023 API abuse**
- **Taken.** Name, billing address, email, phone, DOB, account number, number of lines and plan features from a single API. No SSNs, PINs or payment data (8-K).\[6\]
- **Gap.** About 41 days of undetected bulk extraction, then 14 days to the 8-K.\[54\]
- **Downstream.** Google Fi customers had phone number, SIM serial, plan, activation date and account status exposed; at least one reported SIM swap followed.\[55\] The data makes follow-on phishing look legitimate.\[56\]
- **Remaining gap.** No rate-limiting or anomaly detection on the API (UNVERIFIED root cause; analysts' inference). Included in the FCC $31.5M decree.\[19\]

**#11 Feb–Mar 2023 incident (836 customers)**
- Exposed name, contact details, account number, account PIN, SSN, government ID, DOB, balance, internal rate-plan codes and number of lines. T-Mobile reset PINs and offered two years of credit monitoring (Maine AG notice).\[57\]\[58\]
- Small in scale but maximal for takeover: PIN plus SSN is everything needed to impersonate a customer to care.

**#13 Mint Mobile 2023**
- Exposed name, phone, email, SIM serial, IMEI and plan description; notices December 22, 2023 said no immediate action was needed.\[42\]\[59\]\[60\] BleepingComputer noted the data is enough to support SIM-swap attempts.\[40\]\[61\]

**#14 Bribery texts (April 2024)**
- "I'm looking to pay someone up to $300 per sim swap done." Senders pointed to Telegram and claimed the "T-Mo employee directory"; former employees also received them, suggesting stale data.\[13\]\[62\]\[63\]
- PhoneArena later reported a $500-per-swap offer and a customer told a 2024 swap was an "inside job" (dates UNVERIFIED).\[64\]
- Reps enter a dealer code for each swap, so every swap is attributable (The Register), which is a built-in detection signal.\[63\]

**#15 Salt Typhoon**
- **2024 statement.** T-Mobile saw "attempts to infiltrate" its network through a third-party wireline provider, "quickly severed connectivity," and no calls, voicemails or texts were accessed (Jeff Simon, November 27, 2024, via Infosecurity Magazine).\[22\]
- **August 2026 Bloomberg account.** A suspicious router in a California data center was traced to a router in Chicago belonging to another telecom, disguised to impersonate the T-Mobile device; staff cut the cable with scissors; attackers reached only edge routing.\[21\]\[65\]
- **Conflict.** Some outlets place the cable cut in Bellevue, WA; Mobile World Live, closer to the Bloomberg text, says the team drove to the data center housing the compromised device.\[21\]\[66\] The location is unsettled, and the "no customer data" substance is T-Mobile's own unverified claim.

**#16 March 2026 vendor-insider incident**
- Discovered March 5, 2026; Maine AG filing March 31, 2026. One customer's name, address, email, account and phone numbers, account PIN, driver's license number, DOB and SSN exposed.\[15\]\[16\] T-Mobile told SecurityWeek (April 3, 2026) it was an isolated vendor insider incident, reset the PIN and notified law enforcement.\[67\] BPO and vendor reps remain a live access path.

**#17 BYOD claim (October 7, 2026)**
- The gang listed T-Mobile on its leak site without samples (Cybernews); UNVERIFIED.\[68\] Separately, Security Boulevard republished the 2021 breach (47.8M) in March 2026 as if new;\[47\] recycled breach news is itself fuel for "your account was breached" scams.

**Company-level changes (cumulative)**
- **Products.** Scam Shield (Scam ID and Scam Block, dial #662#); Account Takeover Protection (offered by August 2021; six-digit port-out PIN from the app added March 2022); SIM Protection (blocks SIM changes until removed with two-factor confirmation; only the Primary Account Holder can remove it);\[4\]\[69\]\[70\]\[71\]\[72\] biometric ID verification.
- **Claimed results (November 2, 2026).** Successful SIM swaps down "more than 99% since 2022"; 160B+ unwanted calls blocked since 2017; nearly 3B scam texts blocked in 2025; attempted intrusions up 37% while credential-based attempts fell 35%.\[36\]
- **Self-service.** T-Life restored self-service SIM changes in June 2025 after disabling them in November 2022 (tmo.report),\[73\]\[74\] making the app account itself a takeover target.
- **CFIUS.** CFIUS disclosed a $60M penalty against T-Mobile on August 14, 2024, finding that "between August 2020 and June 2021…T-Mobile failed to take appropriate measures to prevent unauthorized access to certain sensitive data and failed to report some incidents…promptly" (Hunton Andrews Kurth, August 16, 2024). It is the largest CFIUS penalty disclosed to date and the first to name the company.

---

## research/tmo-02-parallels.md — Part 2: Parallel companies and threat groups

### US carriers and MVNOs

**AT&T — Snowflake call-record theft (2024)**
- **Timeline.** Taken April 14–25, 2024; AT&T learned April 19; DOJ twice allowed delayed disclosure; 8-K July 12, 2024.\[26\]\[75\]
- **Taken.** Call and text records for May 1–October 31, 2022 and January 2, 2023 for "nearly all" wireless customers and MVNO customers on AT&T's network (Cricket, Boost and others), about 109M accounts: numbers contacted, counts, durations, and cell-site IDs for a subset. No content, names or SSNs.\[26\]\[76\]\[77\]
- **Actor and access.** UNC5537 used infostealer-harvested credentials on Snowflake accounts without MFA (Mandiant).\[26\]\[78\] AT&T reportedly paid $370K to have the data deleted (Wired).\[77\]
- **Downstream.** Customers of other carriers, including T-Mobile, appear as counterparties.\[25\]
- **Applies to T-Mobile because** T-Mobile also keeps CDR and analytics data in cloud warehouses, and a stolen analyst credential without phishing-resistant MFA, the exact control the FCC decree demands, would expose the same metadata.

**AT&T — 73M dataset (2024) and FCC $13M (September 2024)**
- A dataset of 73M current and former account holders, with 2019-era passcodes and SSNs, surfaced in March 2024 and was reported by AT&T in early April 2024;\[75\] ShinyHunters had advertised AT&T data of this size in 2021. The FCC's $13M resolved a January 2023 cloud-vendor breach affecting 8.9M wireless customers.\[79\]
- **Applies to T-Mobile because** leaked passcodes and SSNs help attackers pass care verification at any carrier, and customers reuse PINs.

**Verizon / TracFone**
- FCC fine of $16M (July 2024) over TracFone breaches; Verizon staff got the same $300 bribe texts in April 2024;\[19\]\[80\] ShinyHunters claimed Verizon among November 2025 Gainsight-Salesforce victims (UNVERIFIED by Verizon); reported Salt Typhoon victim.
- **Applies to T-Mobile because** the same prepaid brands, bribery campaigns and CRM integrations exist at T-Mobile (Metro, Mint).

**Charter / Spectrum (April 2026)**
- **How.** ShinyHunters says it vished an employee's Microsoft Entra SSO account on April 1, 2026, then got into Charter's Salesforce instance.\[27\]
- **Scale, in conflicting counts.** ShinyHunters claims 42M records; Have I Been Pwned counts 4.9M accounts plus about 85K staff-directory records; Cybernews says at least 13M people, mostly Spectrum Enterprise. Charter says only business-customer sales tools were hit and no CPNI was released (SecurityWeek, May 29, 2026);\[81\]\[82\]\[83\] Charter's statement is more authoritative on scope.
- **Applies to T-Mobile because** T-Mobile for Business sales tools sit in the same SaaS/SSO pattern, and the FCC decree already cites a T-Mobile "sales application breach."\[19\]

**Comcast / Xfinity — Citrix Bleed (2023)**
- Attackers got in through Citrix Bleed (unpatched Citrix NetScaler, CVE-2023-4966) between October 16–19, 2023; Comcast disclosed on December 18, 2023, and its Maine AG filing lists 35,879,455 people affected (BankInfoSecurity, December 20, 2023; Cybersecurity Dive).
- **Applies to T-Mobile because** edge-device exploitation is the same entry class as Salt Typhoon and the 2021 router.

**Other US carriers.** Dish/Boost (February 2023 ransomware), Lumen (reported Salt Typhoon victim), UScellular (acquired by T-Mobile in 2025) and Cricket/Visible: not verified in this pass (UNVERIFIED). Cricket and Boost customers were inside AT&T's Snowflake data.\[77\]

### Shared vendors and platforms

**Twilio (August 2022).** Employees were smished with fake "password expired" or "schedule change" texts leading to Okta-lookalike pages,\[84\] part of 0ktapus, which hit more than 130 organizations\[85\] (Group-IB). **Applies to T-Mobile because** the same texts went to carrier staff, and T-Mobile was named among companies Scattered Spider hit in 2021–2023 (DOJ charges; Krebs, November 2024).\[86\]

**Snowflake customer campaign (2024).** UNC5537 used infostealer credentials on accounts without MFA;\[26\] John Binns, the 2021 T-Mobile attacker, was named in connection with it.\[1\] **Applies to T-Mobile because** any analytics tenant protected only by a password is exposed the same way.

**Salesforce-connected apps (2025–2026)**
- UNC6040 called staff posing as IT and talked them into approving a fake "Data Loader" connected app (FBI FLASH, September 12, 2025). Salesloft Drift OAuth tokens were abused and revoked August 20, 2025; Gainsight tokens were abused in November 2025 (about 285 instances claimed);\[87\]\[88\] Experience Cloud guest-access abuse (the "Aura" campaign) was disclosed in March 2026.\[89\] Microsoft grouped these into three intrusion paths (July 13, 2026).\[90\]
- **Telecom victims.** Odido (Netherlands): 6.2M customers taken from its CRM on February 7–8, 2026 via phishing and IT impersonation; on February 27 ShinyHunters leaked 649K customers and more than 340K IBANs.\[28\]\[91\] TELUS Digital: confirmed March 2026; ShinyHunters claims about 1 PB via Google Cloud credentials from the Drift loot and a $65M demand (UNVERIFIED).\[92\]\[93\]
- **Applies to T-Mobile because** care and sales staff are exactly who UNC6040 calls, and T-Mobile runs large consumer and business CRM estates.

**BPO and call-center outsourcers.** Group-IB says Scattered Spider deliberately targeted carriers' BPOs for SIM-swap access;\[94\] T-Mobile's 2026 vendor-insider case shows the path is live.\[15\] **Applies to T-Mobile because** vendor reps have tool access but sit outside T-Mobile's direct HR and monitoring.

**Signaling (SS7/Diameter) and lawful intercept.** Salt Typhoon compromised systems tied to CALEA wiretap capability and took call records (FBI/CISA, November 13, 2024).\[23\]\[24\] No SS7-specific incident verified (UNVERIFIED). **Applies to T-Mobile because** its wireline interconnects were Salt Typhoon's actual path in.

### International carriers

**SK Telecom (2025)**
- **Timeline.** Reported around April 19–22, 2025; malware present since 2022 (an abnormal reboot on February 23, 2022 was never reported).
- **Taken.** 25 categories of USIM data, 9.82 GB, about 26.96M IMSI records (MSIT).\[95\] PIPC counts about 23.24M people after deduplication;\[96\] MSIT counts records and PIPC counts people, and both are authoritative for their own unit.
- **Root causes.** Plaintext Ki/OPc keys for 26.1M SIMs; management servers linked to the HSS.\[97\]
- **Cost.** PIPC fine of KRW 134.79B, about $97M (August 27–28, 2025), its largest ever; SKT pledged KRW 700B over five years.\[97\]\[98\] MSIT said the leaked data "can enable SIM-cloning."\[95\]
- **Applies to T-Mobile because** HSS/UDM and SIM-key stores are the T-Mobile equivalent, and a theft there allows SIM cloning invisible to port-out and SIM-lock controls.

**Other carriers.** Optus (September 2022) said up to 9.8M records were affected; the Australian Information Commissioner's August 2025 civil-penalty case counts about 9.5M people, alleges one breach of the law for each of them (Reuters, August 2025), and alleges an "unauthenticated, internet-facing API" (iTnews). It is a direct analog to T-Mobile's 2023 API abuse. Rogers, Telstra, Orange, Vodafone, Telefonica, Bouygues Telecom (2025) and KT (2025 rogue-femtocell micropayment fraud) were not re-verified (UNVERIFIED); check primary sources before use.

**Deutsche Telekom (parent).** Per Cybernews, DT appeared on the LockBit leak site in 2024 and has denied repeated hacker claims (UNVERIFIED).\[68\] No DT security incident touching T-Mobile US customers was found.

### Threat groups and their carrier playbooks
- **Lapsus$ (2021–2022).** Bought employee credentials, recruited insiders via social media, used MFA fatigue, abused internal tools (Atlas) for SIM swaps, extorted with source code. Members arrested in 2022;\[10\]\[99\] re-emerged in the 2025 "Scattered Lapsus$ Hunters" coalition (at least 16 Telegram channels since August 8, 2025).\[99\]
- **Scattered Spider / UNC3944 / 0ktapus / Star Fraud (2022–).** SMS phishing of carrier and BPO staff with fake SSO pages, help-desk vishing, SIM swapping, theft of phones from carrier stores; crypto holders are the main end victims (Group-IB).\[94\] Five charged November 2024; Urban sentenced to 10 years August 2025.
- **ShinyHunters / UNC6040 / UNC6240.** Data-theft and extortion brand since 2020 (including the 2021 AT&T sale).\[100\] Since 2025: vishing to approve OAuth apps, SaaS token theft, leak-site extortion.\[90\] Telecom victims: Odido, Charter, TELUS (claimed), Verizon (claimed).
- **Salt Typhoon (PRC MSS-linked).** Exploits known CVEs in edge routers, firewalls and VPNs; persists through configuration changes; pivots between interconnected carriers;\[24\]\[65\] targets lawful-intercept systems and call records of senior US political figures.\[101\] FBI said in February 2026 it remains active (CyberScoop, via Vectra).\[102\]
- **The Com / SIM-swap-for-hire on Telegram.** Bribery solicitations ($300–$500 per swap), "panel" access sold on Telegram, leaked employee directories used to target staff.

---

## research/tmo-03-taxonomy.md — Part 3: Attack-type taxonomy

**Data note.** Frequency figures come from FBI IC3, the FTC, T-Mobile and court records. IC3 counts only complaints filed, so true volumes are higher. Where no number exists, the entry says so.

### A. Account and identity

**A1. SIM swap (care, retail, or self-service)**
- **How it works.** The attacker gathers PII from breaches, gets past care verification or bribes or phishes an employee, and moves the number to an attacker SIM or eSIM. The victim's phone loses service; the attacker receives SMS one-time codes and resets email, bank and exchange accounts.
- **Target.** Company: care, retail and BPO staff and tools. Customers: high-value and crypto holders, older adults. Downstream: banks, exchanges, email providers.
- **Frequency and trend.** IC3 complaints: 2,026 (2022), 1,075 (2023), 982 (2024), 971 (2025). Losses: $72.65M, $48.8M, $25.98M, $17.37M.\[30\]\[103\] T-Mobile reports successful swaps down more than 99% since 2022.\[104\] Falling, but harm is concentrated.
- **Harm per victim.** IC3 average about $26K in 2024;\[30\] the tail is enormous (Jones, $38M).
- **Defenses and gaps.** SIM Protection and biometric verification are opt-in. FCC rules require secure authentication and notification, but compliance is not yet required as of October 2026 (UNVERIFIED; FCC waiver DA 24-649 deferred it pending a Federal Register notice).\[105\]\[106\] Insiders and stolen tool access get around customer-side locks.
- **Early signals.** SIM or eSIM change, especially off-hours; care contact followed by a SIM change within minutes; device "no service" while the account shows activity; new IMEI; password-reset texts after the swap; a rep's dealer code tied to unusual volume.
- **Timeline.** Before (lock), during (hold and verify), after (restore, notify banks).

**A2. Unauthorized port-out**
- **How it works.** A leaked account number and PIN (like the 850K prepaid PINs exposed in 2021) is used to request a port to another carrier, bypassing SIM-change controls.
- **Target.** Prepaid and MVNO customers (Mint 2021). Frequency not separately reported.
- **Defenses and gaps.** Port-Out / Account Takeover Protection and the 2022 port-out PIN;\[71\]\[107\] gap is a leaked PIN plus reused credentials.
- **Signals.** Port-out PIN generated, port request from a new carrier, recent PIN view or reset, new-device app login. **Timeline.** Before and during.

**A3. eSIM transfer abuse**
- **How it works.** The attacker takes over the T-Life or app account by credential stuffing or phishing, then uses self-service eSIM transfer (restored June 2025)\[73\] to move the line with no human involved. No public data; emerging risk (inference).
- **Signals.** New-device login followed by eSIM transfer within minutes, MFA method change, impossible-travel login. **Timeline.** During.

**A4. Care and retail social engineering.** The attacker calls care or visits a store with stolen PII and a fake ID to get a PIN reset, an added authorized user, or a device upgrade. Signals: repeated failed verification, contact from a new number or distant store, account change followed by an order. Before and during.

**A5. Insider bribery and vendor reps.** Recruiters reach employees by text or Telegram ($300–$500 per swap); the rep swaps under their own dealer code. Industry-wide campaigns in April 2024; single-customer vendor case in March 2026. Detection relies on after-the-fact audit. Signals: rep actions outside assigned queue or geography, swaps on high-value accounts, action bursts. During (company side).

**A6. Employee credential phishing and stolen tool access.** Smishing to fake SSO or VPN pages (0ktapus) or infostealer-market credentials (Lapsus$) give attackers the internal SIM-swap tools; at least 100 access events in seven months of 2022 at T-Mobile (Krebs).\[12\] Defense: phishing-resistant MFA, which the FCC decree mandates.\[108\] Signals: tool session from a new device or ASN; SIM changes with no matching customer contact.

**A7. Credential stuffing on carrier accounts.** Reused passwords unlock My T-Mobile or T-Life, exposing PINs and plan data and allowing eSIM changes. T-Mobile says credential-based attempts fell 35% even as overall intrusion attempts rose 37% (November 2026).\[32\] Signals: login velocity, new device fingerprints, failed-login bursts.

**A8. Synthetic identity, new-account and device-financing fraud.** Leaked SSN, DOB and driver's license data (2021 breach) is used to open lines and finance phones in a victim's name or a synthetic identity; targets former and prospective customers whose SSNs leaked. No public carrier figure (UNVERIFIED). Signals: credit application SSN matching a breach list, new address, ship-to differing from billing. After the breach, for years.

**A9. Subscription and premium fraud.** Charges added to the line; low priority, no data in this pass.

### B. Data
- **B1. Bulk customer data theft.** T-Mobile 2021 (76.6M), SK Telecom 2025 (26.96M records). Company-side; the customer-side value is the after-breach response.
- **B2. API abuse and enumeration.** An API returns account data for any identifier without proper authorization and the attacker walks the ID space. T-Mobile 2023 (37M, about 41 days undetected);\[54\] Optus 2022 (about 9.5M people per the Australian Information Commissioner's 2025 case, which alleges an "unauthenticated, internet-facing API"). Signal: per-client request volume and sequential IDs.
- **B3. CPNI and call-record theft.** AT&T Snowflake (about 109M) and Salt Typhoon.\[23\]\[25\] Harm: social-graph mapping that enables targeted scams ("I'm calling about your call with your bank").
- **B4. Cloud and SaaS data theft.** Snowflake 2024, Salesforce 2025–2026, Charter, Odido; vector is vishing of staff and stolen OAuth tokens.
- **B5. Vendor and BPO compromise.** Twilio 2022, TELUS Digital 2026, T-Mobile's 2026 vendor insider.

### C. Network
- **C1. SS7/Diameter tracking and SMS interception.** No 2022–2026 carrier incident verified (UNVERIFIED); bypasses every account-level control.
- **C2. Lawful-intercept abuse.** Salt Typhoon (FBI/CISA, November 13, 2024);\[23\] victims are government and political targets.
- **C3. Router and edge-device exploits.** Salt Typhoon (known CVEs, AA25-239A),\[24\] the 2021 T-Mobile router, Comcast Citrix Bleed (35,879,455 people per Comcast's Maine AG filing, December 2023).
- **C4. Nation-state persistence.** SKT malware dormant 2022–2025; Salt Typhoon active since at least 2019.\[102\]
- **C5. SIM cloning from stolen keys.** SKT's plaintext Ki/OPc keys. Signal: the same IMSI attaching from two locations at once.

### D. Customer-facing scams over the carrier channel

**D1. Smishing, including fake T-Mobile texts**
- **How it works.** A link text (package redelivery, toll, fake bank fraud alert, fake carrier bill or rewards) leads to a page that harvests card data or credentials.
- **Frequency.** FTC: $470M reported lost in 2024, five times 2020; top lures were package delivery, job, fake fraud alert, unpaid toll and wrong number.\[109\] T-Mobile blocked about 3B scam texts in 2025 and saw 50% more scam messages than in 2024.\[36\]
- **Defenses and gaps.** Scam Shield network filtering, OS filters, 7726 reporting; gaps are personalized lures and new domains.
- **Signals.** Newly registered domains, sender bursts, links in first-contact texts, lures referencing recent breach data.

**D2. Robocalls and spoofed caller ID.** Scam Shield identified or blocked 19.8B calls in 2023 and 160B+ since 2017;\[36\]\[70\] STIR/SHAKEN applies. Gap: spoofed numbers of real banks and of T-Mobile care itself.

**D3. Voice-clone and AI calls.** No carrier dataset in this pass (UNVERIFIED). Vishing by Scattered Spider and UNC6040 shows the human-voice channel is the dominant enterprise vector. Signals: unknown caller claiming to be family or a bank, urgency script, request to move money or read a code.

**D4–D8. Other channel scams (all UNVERIFIED for frequency in this pass).** Wangiri/IRSF (signal: single-ring calls from high-cost international ranges); SIM-farm bulk texting (signal: high-volume new prepaid lines with identical templates); fake carrier support numbers (search results leading to lines that ask for PINs); fake "your account was breached" follow-ons, fueled by real notices and recycled breach news like the March 2026 republication (signal: inbound contact referencing the breach and asking for a PIN, code or payment); RCS and iMessage spam, which travel over data and partly bypass SMS filters.

### E. Post-breach exploitation
- **E1. Phishing using leaked data.** Data from the 2023 API abuse (name, DOB, plan, number of lines)\[6\] makes fake T-Mobile messages convincing.
- **E2. Extortion.** ShinyHunters leak sites target companies; no verified direct-to-customer carrier extortion found (UNVERIFIED).
- **E3. Identity theft from leaked SSNs and driver's licenses.** 2021 breach (7.8M current postpaid plus 40M+ former and prospective)\[47\] and the 836-customer 2023 incident; long-tail new-account fraud; the settlement allowed up to $25,000 in documented losses.\[50\]

---

## research/tmo-04-matrix.md — Part 4: Target-audience matrix

| Attack type | Company target | Customer target | Downstream target | B/D/A | Frequency (source) | Severity per victim | T-Mobile product coverage | Gap |
|---|---|---|---|---|---|---|---|---|
| SIM swap (care/retail) | Care, retail, BPO reps; Atlas-type tools | Crypto holders, high-value, older adults | Banks, exchanges, email | B/D/A | Med, falling (IC3 982 in 2024; T-Mobile −99%) | Very high (avg ~$26K; up to $38M) | SIM Protection, biometric ID — Partial (opt-in) | Medium |
| Unauthorized port-out | Port-out systems, care | Prepaid/MVNO (Mint) | Same as above | B/D | Low–Med (no separate data) | Very high | Port-Out / Account Takeover Protection — Partial | Medium |
| eSIM self-service abuse | T-Life app, account login | App-heavy postpaid | Banks, email | D | Unknown, emerging (inference) | Very high | SIM Protection — Partial | Large |
| Care/retail social engineering | Care agents, store reps | All; older adults | Employers (business lines) | B/D | Med (Krebs 2022–23) | High | Biometric ID — Partial | Medium |
| Insider bribery / vendor rep | Reps, BPO staff | High-value | Banks, exchanges | D | Med (Apr 2024 campaign; Mar 2026 case) | Very high | None customer-facing — No | Large |
| Employee credential phishing | SSO/VPN, internal tools | All via tool abuse | All | B | High in 2022 (100 events / 7 months) | High | Internal controls (not a product) — Partial | Medium |
| Credential stuffing on accounts | My T-Mobile / T-Life | Postpaid with reused passwords | — | B/D | Med (attempts −35% per T-Mobile 2026) | Med–High | Biometric/2FA — Partial | Medium |
| Synthetic / new-account / device-finance fraud | Credit, activation | Former/prospective (SSN leaked) | Lenders, credit bureaus | A | UNVERIFIED | High (credit damage) | ID protection offered after 2021 — Partial | Large |
| Bulk data theft | Core IT, test environments | All, incl. former/prospective | Everyone using that data | A | Low (several major events) | Med per person, huge in aggregate | Notification + ID monitoring — Partial | Large (after) |
| API abuse | Customer APIs | Postpaid/prepaid, MVNO (Fi) | MVNO partners | A | Low (2023) | Med | None — No | Large (after) |
| CPNI / call-record theft | Cloud warehouse, LI systems | All; VIPs | Contacts in records | A | Low (AT&T 2024; Salt Typhoon) | Med (privacy, targeting) | None — No | Medium |
| SaaS/CRM vishing (Salesforce) | Sales/care staff, CRM | Business and consumer | Partners | A | Med–High 2025–26 (FBI FLASH Sept 2025) | Med | None — No | Large (after) |
| Vendor/BPO compromise | Vendors | All | — | A | Med | High | None — No | Large |
| SS7/Diameter interception | Signaling | VIPs | Banks (SMS OTP) | D | UNVERIFIED | High | Network-side — Partial | Medium |
| Lawful-intercept abuse / nation-state | Edge routers, LI | Government, political | National security | D | Low frequency, extreme severity (AA25-239A) | Extreme for targets | Network-side — Partial | Small (out of agent scope) |
| SIM cloning (stolen keys) | HSS/UDM | All | Banks | D | Low (SKT 2025) | High | None — No | Medium |
| Smishing (incl. fake T-Mobile) | Brand | All; older adults, job seekers | Banks, card issuers | B/D | High ($470M 2024, FTC; +50% 2025 per T-Mobile) | Low–High (median small, tail large) | Scam Shield — Partial | Large |
| Robocalls / spoofed caller ID | Network | All; older adults | Banks | B/D | High (19.8B flagged 2023) | Variable | Scam Shield (Scam ID/Block) — Yes/Partial | Small–Medium |
| Voice-clone / AI calls | — | Older adults, families, executives | Banks, employers | D | Rising, UNVERIFIED | Very high | None specific — No | Large |
| Wangiri / IRSF | Billing | All | — | D | UNVERIFIED | Low | Partial (network) | Small |
| SIM-farm bulk texting | Prepaid activation | — | Everyone receiving texts | B | UNVERIFIED | Indirect | Partial | Medium |
| Fake carrier support numbers | Brand | All | — | D | UNVERIFIED | High (PIN theft → swap) | None — No | Medium |
| Fake breach-follow-on scams | Brand | Breach-notified customers | — | A | UNVERIFIED but structurally constant | High | None — No | Large |
| RCS/iMessage spam | — | All | — | B/D | UNVERIFIED | Low–Med | OS filters — Partial | Medium |
| Identity theft from leaked SSN/DL | — | 2021 breach population | Lenders | A | UNVERIFIED (long tail) | High | 2-year ID protection (expired) — Partial | Large |

---

## research/tmo-05-opportunities.md — Part 5: Opportunity map

### Gap 1 — Takeover-chain interceptor (top priority)
- **Problem.** Each takeover signal (care call, PIN reset, SIM change, new device, OTP texts) is checked on its own, so no one sees the chain until the money is gone.
- **Protects.** Postpaid and prepaid customers, especially crypto holders and older adults; downstream banks and exchanges. **Moment.** During.
- **Signals and tools (mocked).** CAMARA SIM Swap (time since last SIM change), CAMARA Device Swap, port-out event feed, care-interaction log, T-Life login and device fingerprint, inbound OTP and reset text count.
- **Action.** Score the chain; if high risk, hold the SIM/eSIM change or port for a short verification window, push a biometric challenge to the existing device or a trusted contact, send a SIM-swap risk flag to the linked bank, and write a case summary for fraud ops.
- **Pitch incident.** A Google Fi customer's number moved for 1 hour 48 minutes on January 1, 2023, and their email, a financial account and Authy were accessed (SecurityWeek).\[110\] Or Jones, $38M.
- **False positives.** Legitimate upgrades look identical. Show calibrated confidence ("3 of 5 signals; legitimate upgrade probability X"), default to a soft hold and step-up rather than a block, and log every decision.

### Gap 2 — Breach-aftermath concierge
- **Problem.** Breach notices are generic, and the WA AG alleged T-Mobile's were misleading;\[33\] customers don't know what their own exposure means or which scams will follow.
- **Protects.** Current, former and prospective customers in a breach population. **Moment.** After.
- **Tools.** Field-level parser for the breach notice (synthetic); account actions (PIN rotation, turning on SIM Protection and Port-Out Protection); credit-freeze checklist; watchlist flagging texts or calls that quote the leaked fields.
- **Action.** Produce a personal risk plan ("your PIN and SSN leaked, so here are 4 steps, 2 done for you"), run it with consent, monitor for 90 days.
- **Pitch incident.** The 836-customer 2023 incident exposed PIN, SSN and government ID together; the 37M API abuse fields make phishing look legitimate.
- **False positives.** Low risk since it advises rather than blocks. Be honest that it cannot verify credit-bureau state, and show confirmed versus recommended steps.

### Gap 3 — Personalized smishing and fake-T-Mobile triage
- **Problem.** Network filters catch bulk spam, but personalized lures and new domains slip through, and text-scam losses are rising.
- **Protects.** All customers, especially older adults and job seekers. **Moment.** Before and during.
- **Tools.** URL and domain-age lookup, sender reputation, breach-field match, official T-Mobile short code and domain lookup, Nemotron reasoning on message intent.
- **Action.** Label with an explanation, defang the link, offer one-tap 7726 reporting, and show "T-Mobile will never ask for your PIN by text."
- **Pitch fact.** $470M reported lost to text scams in 2024 (FTC); T-Mobile saw 50% more scam messages in 2025.\[32\]
- **False positives.** Real delivery and bank texts. Show the confidence score and reasons, never delete, and offer a "verify with official app" path.

### Gap 4 — Rep-action guardian (company side)
- **Problem.** Bribed, phished or vendor reps use legitimate tools, and customer-side locks can't stop them.
- **Protects.** High-value customers, and T-Mobile from arbitration exposure like the $33M Jones award. **Moment.** During.
- **Tools.** Synthetic care and retail action log, dealer-code behavior baselines, customer risk tier, store or queue geography.
- **Action.** Require customer-side confirmation (push to the current device) before any SIM, port or PIN action on high-risk accounts; flag anomalous reps to security.
- **Pitch incident.** The $300-per-swap texts (April 2024), Lapsus$ in Atlas, the March 2026 vendor insider.
- **False positives.** Busy store reps can look anomalous. Use peer-group baselines, route to review rather than automatic discipline, and monitor actions, not employees' personal data.

### Gap 5 — Number-trust broker for downstream apps
- **Problem.** Banks and exchanges still trust SMS OTP without knowing the SIM changed an hour ago.
- **Protects.** Downstream financial accounts. **Moment.** During.
- **Tools.** CAMARA SIM Swap, Device Swap and Number Verification (mocked), plus a consent ledger.
- **Action.** When a partner app asks "is this number safe to send an OTP?", answer with a risk level and reason, and trigger the customer's own confirmation.
- **Pitch incident.** Google Fi Authy takeover; the Kroll SIM swap that exposed FTX, BlockFi and Genesis claimant data.\[111\]
- **False positives.** Recent legitimate SIM changes. Return a level ("changed 2h ago, verified by biometric") instead of yes or no.

### Gap 6 — Live scam-call coach and family guardian
- **Problem.** Voice-clone, bank-impersonation and fake-T-Mobile-care calls get past call labeling when the number is spoofed or new.
- **Protects.** Older adults and families. **Moment.** During.
- **Tools.** Call metadata (STIR/SHAKEN attestation, first-contact status), on-device transcript (synthetic), Nemotron scam-script detection.
- **Action.** Whisper a warning ("they're asking for a code; T-Mobile never does"), offer to hang up and call back the verified number, alert a designated family member.
- **Pitch fact.** IC3 2025: complainants aged 60 and over reported $7.748B in losses (IC3 2025 report, via Wikipedia summary).\[112\]
- **False positives.** A real bank calling. The agent only advises, explains the cue, and never blocks the call.

### Top 3 positioning angles (ranked)
1. **Takeover-chain interceptor.** "Your customers' numbers get stolen through your own care, retail and app channels, and today each signal is judged on its own. Our agent sees the care call, PIN reset, SIM change and OTP burst as one attack and holds the change until the real owner says yes."
2. **Breach-aftermath concierge.** "After 76.6 million and then 37 million breach notices, customers were left to work out their own risk while scammers used the leaked data against them. Our agent turns each notice into a personal, partly automated recovery plan and catches the scams that quote the leaked data back."
3. **Rep-action guardian.** "Bribery texts offer your reps $300 to $500 per swap, and a single swap cost T-Mobile $33 million in arbitration. Our agent requires the customer's own device to approve high-risk actions, so a compromised rep or vendor cannot complete a swap alone."

---

## Caveats
- **Unverified items.** The 2019–2020 T-Mobile incidents, Rogers, Telstra, Orange, Vodafone, Telefonica, Bouygues, KT, Dish, Lumen and SS7 specifics were not re-verified in this pass; check primary sources before quoting them.
- **Claims from interested parties.** T-Mobile's Salt Typhoon account and its "more than 99%" SIM-swap reduction are the company's own claims. ShinyHunters' counts for Charter, TELUS and Verizon are attacker claims.
- **FCC SIM-swap rule status.** The FCC waiver (DA 24-649) deferred compliance until a Federal Register notice; a compliance vendor says that as of October 2026 none of the rules are yet required.\[105\]\[106\] Not confirmed on an FCC page.
- **Interpreting IC3 trends.** IC3 figures are complaint-based. The decline in SIM-swap complaints may reflect better carrier controls (T-Mobile's claim) or underreporting; both readings are plausible.

## Sources

1. [T-Mobile data breach](https://en.wikipedia.org/wiki/T-Mobile_data_breach)
2. [T-Mobile to Pay \$350 Million in Settlement Over Massive Hacking](https://www.insurancejournal.com/news/national/2022/07/25/677094.htm)
3. [T-Mobile Data Breach Lawsuit: The \$350 Million Settlement](https://lawsuitwatch.org/data-privacy-tech/tmobile-data-breach-lawsuit)
4. [T Mobile Shares Additional Information Regarding Ongoing Cyberattack Investigation](https://www.businesswire.com/news/home/20210817005964/en/T-Mobile-Shares-Additional-Information-Regarding-Ongoing-Cyberattack-Investigation)
5. [T-Mobile 2021 Data Breach](https://www.kellerrohrback.com/currentcases/t-mobile-2021-data-breach)
6. [T-Mobile US, Inc. - Form 8-K - FY2023](https://www.sec.gov/Archives/edgar/data/1283699/000119312523010949/d641142d8k.htm)
7. [T-Mobile hacked to steal data of 37 million accounts in API data breach](https://www.bleepingcomputer.com/news/security/t-mobile-hacked-to-steal-data-of-37-million-accounts-in-api-data-breach/)
8. [Google Fi Breach & SIM-Swapping Attacks: What You Need to Know](https://my-cpe.com/blogs/google-fi-breach--sim-swapping-attacks)
9. [Hackers From Lapsus\$ Now Target T-Mobile! - Cyber News Group](https://www.cybernewsgroup.co.uk/2022/04/25/hackers-from-lapsus-now-target-t-mobile/)
10. [Leaked Chats Show LAPSUS\$ Stole T-Mobile Source Code](https://krebsonsecurity.com/2022/04/leaked-chats-show-lapsus-stole-t-mobile-source-code/)
11. [Lapsus\$ Hackers Gained Access to T-Mobile Systems, Source Code - SecurityWeek](https://www.securityweek.com/lapsus-hackers-gained-access-t-mobile-systems-source-code/)
12. [Fla. Man Charged in SIM-Swapping Spree is Key Suspect in Hacker Groups Oktapus, Scattered Spider](https://krebsonsecurity.com/2024/01/fla-man-charged-in-sim-swapping-spree-is-key-suspect-in-hacker-groups-oktapus-scattered-spider/)
13. [T-Mobile, Verizon workers get texts offering \$300 for SIM swaps](https://www.bleepingcomputer.com/news/security/t-mobile-verizon-workers-get-texts-offering-300-for-sim-swaps/)
14. [T-Mobile employees report being lured into scamming customers (Update: T-Mobile statement)](https://www.androidauthority.com/t-mobile-sim-swapping-scam-3434272/)
15. [T-Mobile data breach: what happened and what's at risk](https://www.upguard.com/news/t-mobile-data-breach-2026-04-07)
16. [T-Mobile Data Breach Exposes Sensitive Personal Info](https://www.claimdepot.com/data-breach/t-mobile-2026)
17. [News](https://www.greenbergglusker.com/news/greenberg-glusker-secures-landmark-33m-arbitration-award-against-t-mobile-for-sim-swap-security-failures)
18. [Law firm says it "humbled" T-Mobile for not preventing SIM swap attack](https://www.phonearena.com/news/Law-firm-says-it-humbled-T-Mobile-for-not-preventing-SIM-swap-attack_id168942)
19. [T-Mobile pays \$31.5 million FCC settlement over 4 data breaches](https://www.bleepingcomputer.com/news/security/t-mobile-pays-315-million-fcc-settlement-over-4-data-breaches/)
20. [US reaches \$31.5 million settlement with T-Mobile over data breaches](https://www.rappler.com/technology/t-mobile-fcc-settlement-data-breaches/)
21. [T-Mobile US CIO recounts hunt for Sal... - Mobile World Live](https://www.mobileworldlive.com/t-mobile-us/t-mobile-us-cio-recounts-hunt-for-salt-typhoon-hackers/)
22. [T-Mobile Claims Salt Typhoon Did Not Access Customer Data - Infosecurity Magazine](https://www.infosecurity-magazine.com/news/tmobile-salt-typhoon-did-not/)
23. [Salt Typhoon: threat group profile - Brandefense](https://brandefense.io/knowledge-hub/apt-groups/salt-typhoon/)
24. [Salt Typhoon: What It Is, How It Works & 2026 Status](https://blog.corenexis.com/salt-typhoon)
25. [Massive AT&T data breach exposes call logs of 109 million customers](https://www.bleepingcomputer.com/news/security/massive-atandt-data-breach-exposes-call-logs-of-109-million-customers/)
26. [AT&T discloses theft of call and text records for nearly…](https://www.enterprotect.com/resource-center/att-snowflake-call-text-records-breach)
27. [Charter Communications confirms data breach — ShinyHunters blamed after threat to leak user info online](https://www.techradar.com/pro/security/charter-communications-confirms-data-breach-shinyhunters-blamed-after-threat-to-leak-user-info-online)
28. [Odido data breach escalates into criminal probe](https://cybernews.com/security/why-odidos-crisis-only-getting-bigger-criminal-investigation/)
29. [Telus Digital confirms security incident as ShinyHunters claims 1PB data theft](https://cyberinsider.com/telus-digital-confirms-security-incident-as-shinyhunters-claims-1pb-data-theft/)
30. [SIM Swap Fraud Statistics 2026: FBI Losses, Scattered Spider](https://www.stingrai.io/blog/sim-swap-statistics-2026)
31. [FTC: Text scam losses hit \$470M in 2024](https://salinapost.com/posts/bc17fad3-b5a5-486b-92b3-46af82cd4473)
32. [Nearly 3 billion scam and spam texts were blocked before reaching T-Mobile customers in 2025.](https://stocktitan.net/news/TMUS/t-mobile-opens-up-on-its-cybersecurity-transformation-in-new-egkg47ye964i.html)
33. [AG Ferguson files lawsuit against T-Mobile for massive data breach](https://www.atg.wa.gov/news/news-releases/ag-ferguson-files-lawsuit-against-t-mobile-massive-data-breach)
34. [T-Mobile Coughed Up \$33 Million in SIM Swap Lawsuit - SecurityWeek](https://www.securityweek.com/t-mobile-coughed-up-33-million-in-sim-swap-lawsuit/)
35. [T-Mobile to Pay \$33 Million in SIM Swap Lawsuit Linked to a 2020 Bitcoin Theft](https://tmo.report/2025/03/t-mobile-to-pay-33-million-in-sim-swap-lawsuit-linked-to-a-2020-bitcoin-theft/)
36. [T‑Mobile Opens Up on Its Cybersecurity Transformation in New Report - T‑Mobile Newsroom](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile)
37. [New FTC Data Spotlight highlights text scams that may target your business](https://www.ftc.gov/business-guidance/blog/2025/04/new-ftc-data-spotlight-highlights-text-scams-may-target-your-business)
38. [Greenberg Glusker secures \$33M award from T-Mobile in SIM swap](https://www.dailyjournal.com/article/384493-greenberg-glusker-secures-33m-award-from-t-mobile-in-sim-swap)
39. [T-Mobile Hit With \$33M SIM Swap Award Over Crypto Theft - AiCoin](https://www.aicoin.com/en/article/450907)
40. [Mint Mobile discloses new data breach exposing customer data](https://www.bleepingcomputer.com/news/security/mint-mobile-discloses-new-data-breach-exposing-customer-data/)
41. [Mint Mobile data breach allowed attacker to port phone numbers](https://appleinsider.com/articles/21/07/10/mint-mobile-data-breach-allowed-attacker-to-port-phone-numbers)
42. [Mobile virtual network operator Mint Mobile discloses a data breach](https://securityaffairs.com/156295/data-breach/mint-mobile-data-breach-2.html)
43. [Mint Mobile Explained: Is It Actually Secure?](https://www.efani.com/blog/what-is-mint-mobile-and-how-secure-is-it)
44. [The Cyberattack Against T-Mobile and Our Customers: What happened, and what we are doing about it. - T-Mobile Newsroom](https://www.t-mobile.com/news/network/cyberattack-against-tmobile-and-our-customers)
45. [T-Mobile Data Breach: Why One Carrier Keeps Getting Hacked](https://www.breachsense.com/blog/t-mobile-data-breach-case-study/)
46. [T-Mobile Data Breach: Full History, Settlements, and What to Do](https://www.security.org/identity-theft/breach/t-mobile/)
47. [T-Mobile Confirms Data Breach Affecting 47.8 Million Current, Former and Prospective Customers - Security Boulevard](https://securityboulevard.com/2026/03/t-mobile-confirms-data-breach-affecting-47-8-million-current-former-and-prospective-customers/)
48. [T-Mobile settles suit over massive hacking for \$350M](https://www.foxbusiness.com/markets/t-mobile-settles-suit-massive-hacking-350m)
49. [T-Mobile Data Breach - 76.6M SSNs Exposed (2026 Update)](https://www.harmreport.com/lawsuits/data-breach/t-mobile/)
50. [T-Mobile to Shell Out \$350 Million to Customers in Wake of Massive Data Breach](https://finance.yahoo.com/news/t-mobile-shell-350-million-193036758.html)
51. [T-Mobile says that 48 million subscribers were victimized in data breach, offers free ID protection](https://www.phonearena.com/news/t-mobile-offering-customers-free-id-theft-protection_id134426)
52. [T-Mobile breached by cybercrime group LAPSUS\$ through compromised employee accounts - 9to5Mac](https://9to5mac.com/2022/04/22/t-mobile-breach-lapsus/)
53. [SIM-Swapper, Scattered Spider Hacker Gets 10 Years](https://cybersecurity.fullcoll.edu/2025/08/20/sim-swapper-scattered-spider-hacker-gets-10-years/)
54. [Security: How 37 Million T-Mobile Customers Got Hacked — And Why It Wasn’t Even Complicated](https://sgopalanbtg.substack.com/p/security-how-37-million-t-mobile)
55. [Google Fi Data Breach - Hackers May Carry Out SIM Swap Attacks](https://cybersecuritynews.com/google-fi-data-breach/)
56. [T-Mobile Data Breach Includes Massive Compromise of Google Fi Service, Unknown Quantity of Customer Records Exposed - CPO Magazine](https://www.cpomagazine.com/cyber-security/t-mobile-data-breach-includes-massive-compromise-of-google-fi-service-unknown-quantity-of-customer-records-exposed/)
57. [T-Mobile Discloses 2nd Data Breach of 2023, This One Leaking Account PINs and More - Slashdot](https://it.slashdot.org/story/23/05/02/1312245/t-mobile-discloses-2nd-data-breach-of-2023-this-one-leaking-account-pins-and-more)
58. [T-Mobile sees another data breach - 9to5Mac](https://9to5mac.com/2023/05/02/t-mobile-sees-another-data-breach/)
59. [Mint Mobile virtual operator reports data breach exposing customer data](https://beyondmachines.net/event_details/mint-mobile-virtual-operator-reports-data-breach-exposing-customer-data-e-6-p-l-k)
60. [Mint Mobile discloses new Customer Data Breach](https://www.androidheadlines.com/2023/12/mint-mobile-new-customer-information-breach.html)
61. [Mint Mobile Breach: Customers May Face SIM Swap Attacks](https://www.vpnmentor.com/news/mint-mobile-breach-sim-swap-attacks/)
62. [Scammers offer cash to phone carrier staff to swap SIM cards](https://www.scworld.com/news/scammers-offer-cash-to-phone-carrier-staff-to-swap-sim-cards)
63. [SIM swappers texting telco employees, offer cash for crime • The Register](https://www.theregister.com/AMP/2024/04/16/sim_swap_scam_tmobile/)
64. [T-Mobile rep receives shocking request in a text message - PhoneArena](https://www.phonearena.com/news/t-mobile-rep-rejects-shocking-request-made-via-text-message_id179605)
65. [T-Mobile Cut Cable to Eject Salt Typhoon Hackers - Cyber Kendra](https://www.cyberkendra.com/2026/08/t-mobile-cut-cable-to-eject-salt.html)
66. [T-Mobile Sent Four People With Scissors to Stop Chinese Hackers](https://www.yahoo.com/news/us/articles/t-mobile-sent-four-people-183411081.html)
67. [T-Mobile Sets the Record Straight on Latest Data Breach Filing - SecurityWeek](https://www.securityweek.com/t-mobile-sets-the-record-straight-on-latest-data-breach-filing/)
68. [T-Mobile threatened by hackers behind Trump Mobile breach](https://cybernews.com/security/trump-mobile-hackers-claim-t-mobile-data-breach/)
69. [Protect your T-Mobile account from fraud](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud)
70. [T-Mobile Report: Un-carrier Customers Protected from Over 19 Billion Scam Calls in 2023 - T-Mobile Newsroom](https://www.t-mobile.com/news/un-carrier/t-mobile-report-customers-protected-from-over-19-billion-scam-calls-in-2023)
71. [T-Mobile adds extra security to port-out process - 9to5Mac](https://9to5mac.com/2022/03/18/t-mobile-adds-extra-security-port-out-process/)
72. <https://www.phonearena.com/news/t-mobile-sim-protection-is-live_id144370>
73. [Huge T-Mobile App Update Finally Adds Self-Service SIM Changes And Business Account Support](https://tmo.report/2025/06/huge-t-mobile-app-update-finally-adds-self-service-sim-changes-and-business-account-support/)
74. [T Life App Finally Lets You Switch SIM Cards on Your Own - TmoNews](https://www.tmonews.com/2025/06/t-life-app-finally-lets-you-switch-sim-cards-on-your-own/)
75. [AT&T breach sees an estimated 109 million customers’ call logs leaked - Tech Monitor](https://www.techmonitor.ai/technology/cybersecurity/att-breach-sees-an-estimated-109-million-customers-call-logs-leaked)
76. [AT&T/Snowflake Breach Hits Most of US - Vendor Exposure Strikes Again](https://foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2024/july/at-t-snowflake-breach-hits-most-of-us-vendor-exposure-strikes-again/)
77. [AT&T in the crosshairs after a massive breach of customer data](https://finance.yahoo.com/news/t-crosshairs-massive-breach-customer-063505101.html)
78. [AT&T Data Breach 2024: 73M Records](https://www.cloudskope.com/breaches/att-breach-2024)
79. [US reaches \$31.5 million settlement with T-Mobile over data breaches](https://finance.yahoo.com/news/us-reaches-31-5-million-164416755.html)
80. [T-Mobile and Verizon workers offered \$300 bribes for SIM swaps](https://9to5mac.com/2024/04/17/sim-swaps-using-bribes/)
81. [ShinyHunters adds Charter to trophy shelf after 4.9M customer records leak](https://www.theregister.com/cyber-crime/2026/05/29/shinyhunters-adds-charter-to-trophy-shelf-after-49m-customer-records-leak/5248281)
82. [Charter Communications Data Breach Could Impact Nearly 5 Million - SecurityWeek](https://www.securityweek.com/charter-communications-data-breach-could-impact-nearly-5-million/)
83. [Inside the Charter data breach: hackers leak 13M+ customer data](https://cybernews.com/security/charter-spectrum-data-breach-millions-exposed/)
84. [Twilio Smishing Breach 2022](https://www.cloudskope.com/breaches/twilio-breach-2022)
85. [12 Questions and Answers About Scattered Spider (G1015)](https://www.securityscientist.net/blog/12-questions-and-answers-about-scattered-spider-g1015/)
86. [Feds Charge Five Men in ‘Scattered Spider’ Roundup](https://krebsonsecurity.com/2024/11/feds-charge-five-men-in-scattered-spider-roundup/)
87. [ShinyHunters Threat Actor Profile: TTPs, IoCs & Attacks](https://www.huntress.com/threat-library/threat-actors/shinyhunters)
88. [Cyber Criminal Groups UNC6040 and UNC6395 ...](https://www.ic3.gov/CSA/2025/250912.pdf)
89. [Aura data breach](https://en.wikipedia.org/wiki/Aura_data_breach)
90. [Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity](https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html)
91. [Overview: Odido & Ben Data Breach](https://www.upguard.com/news/odido-nl-data-breach-2026-03-02)
92. [Telus Digital data breach confirmed: ShinyHunters claims 1PB theft](https://www.bitdefender.com/en-us/blog/hotforsecurity/telus-digital-data-breach)
93. [Telus Digital confirms breach - hackers allegedly stole 'almost 1 petabyte of data'](https://www.techradar.com/pro/security/telus-digital-confirms-breach-hackers-allegedly-stole-almost-1-petabyte-of-data)
94. [Connecting Scattered Spider: Defining A Cybercrime Collective Through Shared TTPs](https://www.group-ib.com/blog/connecting-scattered-spider/)
95. [MSIT Releases Final Investigation Results on SK Telecom ...](https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&nttSeqNo=1139)
96. [SK Telecom USIM data breach: incident profile - Brandefense](https://brandefense.io/knowledge-hub/incidents/sk-telecom-2025/)
97. [SK Telecom hit with record privacy fine after massive data leak - The Korea Herald](https://www.koreaherald.com/article/10563945)
98. [South Korean Government Fines 'Negligent' SK Telecom](https://cybersecurityasia.net/south-korea-fines-negligent-sk-telecom/)
99. [Lapsus\$](https://en.wikipedia.org/wiki/Lapsus$)
100. [What are ShinyHunters, the hackers that attacked Google? Should we all be worried?](https://theconversation.com/what-are-shinyhunters-the-hackers-that-attacked-google-should-we-all-be-worried-264271)
101. [Salt Typhoon hackers targeted over 80 countries, FBI says - Nextgov/FCW](https://www.nextgov.com/cybersecurity/2025/08/salt-typhoon-hackers-targeted-over-80-countries-fbi-says/407719/)
102. [Salt Typhoon: TTPs, detection, and defense](https://www.vectra.ai/resources/vectra-ai-threat-briefing-salt-typhoon)
103. [SIM Swap Fraud Statistics 2026: Reported Losses, Attack Volume, And Who Gets Targeted](https://www.efani.com/blog/sim-swap-fraud-statistics-2026)
104. [T-Mobile says it's winning the fight against SIM swap attacks after years of trouble](https://androidauthority.com/t-mobile-sim-swap-attacks-security-report-3730775)
105. [United States Telecom & Mobile Services Compliance Guide](https://www.identomat.com/compliance-guide/guide/telecom-mobile-services-compliance-in-the-united-states)
106. [Compliance Date Set for FCC Rules to Secure Cellphones](https://www.vitallaw.com/news/compliance-date-set-for-fcc-rules-to-secure-cellphones/cspd01e62ee93303974150815d5752b0746f13)
107. [The best SIM swap protection services in 2026 - Artisan AI](https://www.artisan.co/blog/best-sim-swap-protection)
108. [T-Mobile to pay \$31.5M in settlement with FCC over cybersecurity data breaches](https://www.geekwire.com/2024/t-mobile-to-pay-31-5m-in-settlement-with-fcc-over-cybersecurity-data-breaches/)
109. [FTC Highlights \$470M in Text Message Scams](https://natlawreview.com/article/privacy-tip-440-text-scam-proceeds-surpass-470m-2024)
110. [Google Fi Data Breach Reportedly Led to SIM Swapping - SecurityWeek](https://www.securityweek.com/google-fi-data-breach-reportedly-led-to-sim-swapping/)
111. [T-Mobile slapped with \$33 million bill for a SIM swap it didn't stop - Android Authority](https://www.androidauthority.com/tmobile-sim-swap-payout-3539652/)
112. [Internet Crime Complaint Center](https://en.wikipedia.org/wiki/Internet_Crime_Complaint_Center)
