# 04 — Competitive landscape and product white space
**Research date: 2026-11-07 | Avoid saying incumbents lack features they actually ship.**

## TL;DR — use first
1. T-Mobile **already protects calls, texts and websites**; never pitch your app as their first text scam detector.
2. Google Pixel's on-device real-time scam alerts now extend across calls and messaging, including Gboard; plain real-time detection is **not unique**.
3. Compete on a **consented cross-channel action workflow**: collect corroborating signals, prevent a risky next step, document evidence and walk through recovery.
4. Make unsupported integrations visibly **simulated**, not “a T-Mobile network action” or “a real bank transfer blocked.”
5. Cite T-Mobile's **Nov 2026 cybersecurity report** to align the pitch with its latest stated security priorities.

## A. T-Mobile's existing feature baseline: do not underestimate it

- **Scam Shield / ScamShield free** — [official features](https://www.t-mobile.com/benefits/scam-shield), [support details](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud). Already includes **Scam Likely/Scam ID**, Scam Block (`#662#` on supported service), potential-spam identification, number blocking, spam calls routed to voicemail, *Callback Protection*, **Safe Web Browsing**, and automatic network protection for suspicious texts and websites. Experience is managed in **T-Life** on eligible accounts. **Use:** position your product as a layer of explanation, verified next actions and recovery, not replacement call-blocking.
- **Scam Shield Premium** — [T-Mobile support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud). Premium offers category call blocks, per-number call/text blocking lists that may persist on the network, reverse number lookup, and voicemail-to-text. Specific price and availability depend on plan/account; **current exact universal price UNVERIFIED**. **Use:** demonstrate interventions beyond a category or phone-number block; do not suggest Premium never filters texts.
- **Coverage caveat** — T-Life Scam Shield management has restrictions for prepaid customers (some free network features still work). [T-Mobile support](https://www.t-mobile.com/support/plans-features/help-with-scams-spam-and-fraud). **Use:** consider a universally understandable, lightweight safety flow instead of relying on a particular carrier app entitlement.
- **Customer complaints** — User-app reviews can reflect missed detections, false positives, UI friction or price, but **no systematically verified complaint counts or quotations obtained**. **UNVERIFIED**; do not tell judges a quantified gap exists without app-store link and sample methodology.

### T-Mobile's very recent public position

- **“Advancing Cybersecurity at T-Mobile”** — [T-Mobile newsroom, Nov 2026](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile). T-Mobile says it identifies **hundreds of millions of scam/spam calls weekly**, saw **nearly 50% more scam/spam messages in 2025 than 2024**, and describes substantial progress on preventing SIM-swap and phishing-related compromise. **Use in pitch:** “T-Mobile already stops enormous volume. The remaining opportunity is the *customer journey when a convincing scam gets through*.” Do not imply this project is affiliated with T-Mobile.

## B. Other existing products, from primary sources

| Product / primary URL | Verified coverage / differentiation | Limitation for *this hackathon's* gap (not proof feature does not exist) | Use in pitch |
|---|---|---|---|
| **AT&T ActiveArmor** — [official](https://www.att.com/security/), [terms](https://www.att.com/legal/terms.activeArmorMobileSecurity) | Fraud/spam-call identification and blocking; plan-dependent advanced identity and security features. | No verified public documentation of a unified *scam -> contextual risk evidence -> consented transfer hold -> tailored recovery* sequence in one customer flow. | Carrier competitors already filter calls; action orchestration is the differentiator. |
| **Verizon Call Filter** — [FAQ](https://www.verizon.com/support/call-filter-faqs/) | Call spam detection, filter/block, spam reporting; paid upgrades for enhanced caller ID/categories. | Primarily call-centric experience in cited materials. | Show cross-channel evidence (message + URL + network signal + payment). |
| **Google Pixel Scam Detection** — [Google Store](https://store.google.com/intl/en/ideas/articles/pixel-safety-features), [Pixel Help](https://support.google.com/pixelphone/answer/16704479?hl=en), [Sep 2026 Pixel Drop](https://support.google.com/pixelphone/thread/466181739/september-2026-pixel-drop) | On-device AI detects suspicious patterns in live calls/texts; Google added on-device messaging/Gboard warnings on supported Pixels in 2026. | Sophisticated before/during warning already exists; a bank/FTC recovery workflow is **not documented by these references**. | **Competitive threat:** avoid claiming first multimodal warning; emphasize next-step protection. |
| **Apple iOS 26 call screening** — [Apple support](https://support.apple.com/en-us/111106), [iOS 26 overview](https://apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26) | Can screen unknown calls and show caller purpose, silence/filter unknown numbers. | This is caller handling and filtering rather than proven financial safety workflow. | Compare your customer-facing “explain + verify + act” after contact. |
| **Apple Messages filtering** — [Apple Support](https://support.apple.com/en-us/125068) | Unknown-sender handling, transaction/promotion categories and third-party filters for SMS/MMS/RCS. | For iMessage vs SMS/RCS, behavior and app extension capabilities vary; avoid broad universal claims. | Show a UI that works from pasted/shared screenshots and synthetic call transcripts. |
| **Samsung Smart Call / AI scam detection** — [Samsung support, Jun 2026](https://samsung.com/us/support/answer/ANS10003438) | Samsung lists caller-ID/spam blocking and real-time AI scam-warning on eligible Galaxy software/models. | Regional and device availability may vary; payment intervention **not confirmed**. | Warn against “no competitor uses AI to detect calls.” |
| **Hiya** — [product](https://www.hiya.com/products/hiya-protect) | Spam/fraud call intelligence and protection used in carrier/device ecosystems. | Payment-recovery toolchain not established in cited materials. | Explain telecom-number reputation as *one input*, not a definitive decision. |
| **Truecaller** — [official](https://www.truecaller.com/) | Caller ID, spam calls, blocking and messaging spam tools (varies by platform/plan). | End-to-end recover-after-fraud flow not verified. | Position as differentiated intervention, not “better caller ID.” |
| **Robokiller** — [SMS documentation](https://support.robokiller.com/hc/en-us/articles/360018939911-How-does-Robokiller-block-Spam-Text-Messages), [official](https://robokiller.com/spam-blocker-app) | Blocks/categorizes unwanted calls and SMS using sender reputation, lists and content patterns. | Does more than call filtering; payment action is **not documented** in these sources. | Do not claim text-content scanning is new. |
| **Norton Genie** — [official product](https://ca.norton.com/products/genie-scam-detector), [Norton blog](https://us.norton.com/blog/online-scams/norton-genie) | Users submit screenshot/text/email/social posts/URLs for AI assessment and advice; Norton has scam-protection integrations. | Detect/advice is not the same as a visible *user-authorized multi-tool action receipt*. | Direct “not another paste-in chatbot” contrast. |
| **UK banks / Confirmation of Payee** — [Pay.UK service](https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/) | Checks whether recipient account name matches intended payee as a payment-flow control. | A genuine matching recipient can still receive funds obtained through persuasion; CoP is not an all-purpose APP scam detector. | Reinforce layered checks rather than claiming we invented payment confirmation. |

## C. Gap table — before / during / after and channels
**Legend:** `●` confirmed substantive coverage in cited materials, `◐` partial or indirect coverage, `—` no verified claim from sources checked; **“—” does NOT mean confirmed absent**. Columns C=call, S=SMS/MMS, M=RCS/iMessage/chat, E=email, W=web link, P=payments.

| Product | Before | During | After | C | S | M | E | W | P |
|---|---|---|---|---|---|---|---|---|---|
| T-Mobile Scam Shield | ● | ● | ◐ | ● | ● | ◐ | — | ● | — |
| AT&T ActiveArmor | ● | ● | ◐ | ● | ◐ | — | — | ◐ | — |
| Verizon Call Filter | ● | ● | ◐ | ● | — | — | — | — | — |
| Google Pixel Scam Detection | ● | ● | ◐ | ● | ● | ● | — | ◐ | — |
| Apple iOS call/message screening | ● | ● | ◐ | ● | ● | ● | — | ◐ | — |
| Samsung Smart Call | ● | ● | ◐ | ● | — | — | — | — | — |
| Hiya / Truecaller | ● | ● | ◐ | ● | ◐ | ◐ | — | — | — |
| Robokiller | ● | ● | ◐ | ● | ● | ◐ | — | — | — |
| Norton Genie | ● | ◐ | ◐ | ◐ | ● | ● | ● | ● | — |
| UK bank payee-confirmation controls | ● | ● | ◐ | — | — | — | — | — | ● |
| **Proposed Safe Signal Agent (demo)** | **●** | **●** | **●** | **◐ simulated** | **●** | **◐ paste/share** | **◐ paste/share** | **●** | **◐ simulated** |

**Column-source basis:** T-Mobile [benefits](https://www.t-mobile.com/benefits/scam-shield), Google [Pixel Help](https://support.google.com/pixelphone/answer/16704479?hl=en), Apple [Messages](https://support.apple.com/en-us/125068), Samsung [support](https://samsung.com/us/support/answer/ANS10003438), Robokiller [SMS](https://support.robokiller.com/hc/en-us/articles/360018939911-How-does-Robokiller-block-Spam-Text-Messages), Norton [Genie](https://ca.norton.com/products/genie-scam-detector), bank [Pay.UK](https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/). Entire matrix is a **research interpretation**, not exhaustive independent product testing; feature coverage changes with region, app version and subscription.

## D. Exact product claim to make (and avoid)

**Make:** “Scam Shield already blocks and filters huge volumes of suspicious communications. Our Nemotron agent closes the **last-mile decision gap**: independent evidence, consented safeguards, and guided recovery across messages, links, telecom signals and simulated bank actions.” Supported background: [T-Mobile 2026 security statement](https://www.t-mobile.com/news/un-carrier/advancing-cybersecurity-at-t-mobile), [Scam Shield](https://www.t-mobile.com/benefits/scam-shield).

**Do not make:** “T-Mobile protects calls but has no text security”; “Only our app detects AI voice clones”; “We can freeze real customer bank funds”; “Google has no messaging scam detection”; “A verified caller ID guarantees caller legitimacy.” These would contradict or overrun the source evidence.

## E. A practical differentiator judges can see

**Moment 1 — before:** user receives a synthetic bank text. App identifies urgency/OTP request, extracts link, checks URL + sender with cited tools, and offers verified bank callback.

**Moment 2 — during:** simulated bank transfer is initiated; independent `policy_engine` pauses the *simulated transaction* only after opt-in, displaying the evidence and explicit “confirm hold” button.

**Moment 3 — after:** app generates incident timeline, 7726 instructions, FTC report guidance, IdentityTheft.gov recovery link and a copyable fraud-claim narrative (nothing automatically sent).

This is both an agentic multi-step workflow for NVIDIA and a before/during/after customer protection story for T-Mobile.
