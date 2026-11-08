# 07 Privacy by Design

## TL;DR
1. Build these first: Presidio-style PII redaction before any Nemotron cloud call, scan opt-in per channel (SMS / calls / links), raw text discarded after the verdict, and a user-visible "what we saw, what we sent, what we kept" audit log with retention timers.
2. Pitch frame: Cavoukian's 7 principles (ipc.on.ca) with one feature each (table below). Judges can tick through it in 30 seconds.
3. NIST Privacy Framework: v1.0 (2020) is still the only final version. v1.1 is an Initial Public Draft (Apr 2025, comments closed Jun 2025). Cite "aligned to NIST PF 1.0 functions, tracking the 1.1 draft."
4. Texas TDPSA (Tex. Bus. & Com. Code ch. 541): fraud prevention is a permitted purpose (541.201), but consent for sensitive data (541.101), data minimization, and data protection assessments (541.105) still shape the design. AG-only enforcement, 30-day cure, up to $7,500 per violation. We are not lawyers.
5. Be honest: Google and Apple do scam detection on-device. Our prototype is a cloud LLM (Nemotron on build.nvidia.com) with redaction. Claim "on-device-first architecture, cloud fallback with redaction," and demo the split. Don't claim on-device inference unless we actually run a small model locally.

---

## 1. Cavoukian's 7 Foundational Principles mapped to features

Source for the principles: Ann Cavoukian, *Operationalizing Privacy by Design: A Guide to Implementing Strong Privacy Practices*, IPC Ontario, Dec 2012. https://www.ipc.on.ca/en/media/1769/download (also a shorter original "7 Foundational Principles" PDF mirrored at https://student.cs.uwaterloo.ca/~cs492/papers/7foundationalprinciples_longer.pdf).

| # | Principle (paraphrased) | Concrete feature we can build in 24h | Pitch line |
|---|---|---|---|
| 1 | **Proactive not reactive; preventative not remedial.** Stop privacy harms before they happen. | Threat model + data-flow diagram drawn before coding. Redaction is in the pipeline before the LLM call, not bolted on after. Prompt-injection guard (see 06) so a scam text can't make the agent leak data. | "Privacy controls run before the model sees anything." |
| 2 | **Privacy as the default.** Users are protected with no action needed. | Every channel starts with minimal data: only unknown senders scanned (mirrors Google and Apple), raw message text not stored by default, cloud analysis gets redacted text only, audit-log retention defaults to 24h for raw snippets. | "Out of the box we keep nothing but the verdict." |
| 3 | **Privacy embedded into design.** A core part of the system, not an add-on. | A single `privacy_gateway()` that every tool call and LLM call must go through (redact, then log, then send). Tool calls get only the fields they need (URL checker gets the URL, phone lookup gets the number, never the whole thread). | "One choke point, enforced in code." |
| 4 | **Full functionality, positive-sum.** No false choice between privacy and security. | Show detection quality on redacted vs unredacted synthetic data side by side. If recall barely moves, that proves the positive-sum claim with numbers. Placeholders keep type information (`<PERSON>`, `<PHONE_NUMBER>`, `<URL>`) so the model can still reason. | "We measured it: redaction costs X points of recall." |
| 5 | **End-to-end security, full lifecycle.** Protect from collection to secure destruction. | Retention timers: raw snippet TTL (e.g. 24h), verdict + evidence hashes kept 30 days, then auto-delete. TLS to APIs, secrets in env vars, encrypted local store (SQLite + key). "Delete everything now" button that really wipes. | "Every record has an expiry date shown in the UI." |
| 6 | **Visibility and transparency.** Practices are open and verifiable. | User-visible audit log per event: what was scanned, what was redacted, what was sent to which service (Nemotron, Safe Browsing, etc.), what action the agent took, and when it will be deleted. Exportable JSON (doubles as a TDPSA access-request answer). | "Tap any alert to see exactly what left your phone." |
| 7 | **Respect for user privacy, user-centric.** Strong defaults, clear notice, easy choices. | Opt-in per channel with plain-language toggles (no dark patterns; this also matters legally, see TDPSA 541.001(6)). Agent asks before high-impact actions (blocking a contact, alerting a family member, freezing a payment). Trusted-contact sharing is opt-in and shows exactly what is shared. | "You stay in control. The agent proposes, you approve." |

Implementation notes:
- PII redaction: Microsoft Presidio (analyzer + anonymizer, also an image redactor). Note: Presidio is now a community-owned project. Docs moved to https://presidio.dataprivacystack.org/, repo https://github.com/data-privacy-stack/presidio/. The docs warn that it won't find all sensitive data, so say "reduces" exposure, not "eliminates." The old microsoft.github.io/presidio URL now redirects. Specific operator names (replace/mask/hash/encrypt) and deanonymize support: UNVERIFIED in this pass, check the docs before relying on reversible redaction.
- Scam-specific caveat: we must NOT redact the signals the detector needs (the URL, the callback number, the payment amount, the urgency language). Redact the *victim's* PII (names, account numbers, SSNs, addresses, OTP codes). Send the URL/number only to the matching reputation tool. (Team design suggestion, not from a source.)

---

## 2. NIST Privacy Framework

- **Current status:** Version 1.0 (Jan 2020) is the published, final version. https://www.nist.gov/privacy-framework (PDF: https://doi.org/10.6028/NIST.CSWP.01162020).
- **v1.1:** NIST CSWP 40, *Initial Public Draft*, published Apr 14, 2025. Comments closed Jun 13, 2025. It realigns with CSF 2.0 and adds a 1.0-to-1.1 Core mapping. https://csrc.nist.gov/pubs/cswp/40/nist-privacy-framework-11/ipd , PDF https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.40.ipd.pdf . NIST's April 2025 news release said a final version would come later that year (https://www.nist.gov/news-events/news/2025/04/nist-updates-privacy-framework-tying-it-recent-cybersecurity-guidelines). As of our check (Nov 2026), the nist.gov framework page still lists 1.1 only as the IPD. **A final 1.1 release is UNVERIFIED.** Law-firm summaries say 1.1 adds AI privacy-risk content (e.g. https://www.jonesday.com/en/insights/2025/05/nist-updates-its-privacy-framework-to-address-ai). That comes from secondary sources, not confirmed on the NIST page.
- **Closest thing to a 1-page version:** there is no official one-pager. Use the *Quick Start Guide*, "Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses" (PF 1.0). https://www.nist.gov/document/getting-started-nist-privacy-framework-guide-small-and-medium-businesses . It is organized as "Ready, Set, Go." Learning Center with translations: https://www.nist.gov/privacy-framework/getting-started-0/learning-center

**Core functions** (paraphrased from the Quick Start Guide above; PF 1.0 names them with a "-P" suffix):

| Function | What it means | Our feature |
|---|---|---|
| Identify-P | Inventory the personal data and its lifecycle. Assess privacy risk to individuals. Vet vendors and tools. | Data-flow diagram + data inventory table in the README (message text, phone numbers, URLs, verdicts, which API sees what). |
| Govern-P | Set privacy policies and roles. Track legal duties. Reassess when products or laws change. | One-page privacy policy + "privacy owner" on the team. TDPSA notes below. |
| Control-P | Limit collection and retention. Let individuals manage their data. Use de-identification. | Redaction gateway, per-channel opt-in, TTLs, delete-all button. |
| Communicate-P | Clear notices and choices. Collect preferences. Plan breach response. | Plain-language onboarding, per-alert "why and what was shared" panel, audit log. |
| Protect-P | Access control, encryption, updates, secure disposal. | Encrypted local store, secrets management, scoped API keys, secure wipe. |

---

## 3. Texas Data Privacy and Security Act (TDPSA)

Not legal advice. We are not lawyers. Official text is Tex. Bus. & Com. Code ch. 541 (https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm). Our sandbox couldn't reach that host, so section text below was read from the texas.public.law mirror and the Texas AG page. Effective **July 1, 2024**.

AG overview: https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/enforcing-privacy-and-data-security-laws-protect-texans/texas-data-privacy-and-security-act

**What matters for a scam-protection feature**

- **Applicability / small-business carve-out (541.002).** Applies to entities doing business in Texas or offering products used by Texans, that process or sell personal data, and that are not an SBA-defined small business. Exempt entities include state agencies, GLBA financial institutions/data, HIPAA entities, nonprofits, higher ed, and certain electric utilities. https://texas.public.law/statutes/tex._bus._&_com._code_section_541.002 . A hackathon team is likely exempt, but **T-Mobile is not**, so design as if the law applies.
- **Small businesses still can't sell sensitive data without consent (541.107).** https://texas.public.law/statutes/tex._bus._&_com._code_section_541.107 (confirmed by the AG page).
- **Key definitions (541.001)** https://texas.public.law/statutes/tex._bus._&_com._code_section_541.001
  - Consent (subdiv. 6): a clear affirmative act that is freely given, specific, informed and unambiguous. It does NOT include accepting broad terms of use, hovering/muting/closing content, or agreement obtained through dark patterns (subdiv. 10). Design implication: per-channel opt-in toggles, no pre-checked boxes.
  - Sensitive data (subdiv. 29): data revealing race/ethnicity, religion, mental/physical health diagnosis, sexuality, citizenship/immigration status; biometric/genetic data used to identify someone; data from a known child; precise geolocation. Scanned message content can *incidentally* reveal these (e.g. a fake "pharmacy" or immigration-office scam). That is our inference, not settled law, so treat scanned content as possibly sensitive.
  - Personal data (subdiv. 19) includes pseudonymous data that can be re-linked. It excludes deidentified data (subdiv. 12). Redacted text with re-linkable tokens is probably still personal data.
- **Controller duties (541.101).** Data minimization (adequate, relevant, reasonably necessary for disclosed purposes). No secondary use without consent. Reasonable security scaled to the data. No processing of sensitive data without consent. No retaliation for exercising rights. https://texas.public.law/statutes/tex._bus._&_com._code_section_541.101
- **Data protection assessments (541.105).** Required for targeted ads, sale, risky profiling, **processing sensitive data**, and other heightened-risk processing. Must weigh benefits against risks and safeguards. Must be produced to the AG on a civil investigative demand (541.153), and stays confidential. https://texas.public.law/statutes/tex._bus._&_com._code_section_541.105 . Pitch move: include a 1-page mini-DPA in the repo.
- **Fraud/security exception (541.201(a)).** The chapter doesn't stop processing to detect, prevent, protect against, or respond to security incidents, identity theft, fraud, harassment, malicious or deceptive activity, or to keep systems secure. https://texas.public.law/statutes/tex._bus._&_com._code_section_541.201 . Whether this exception removes the consent requirement for sensitive data in a consumer scam-scanning product is a legal question. **UNVERIFIED / ask a lawyer.** Safe design: rely on the exception for core detection AND still get opt-in consent.
- **Consumer rights (541.051) and response duties (541.052).** Rights: confirm and access, correct, delete, portable copy, and opt out of targeted ads, sale, and significant-decision profiling. The AG page lists these. Controller must respond within 45 days, extendable once by 45 days with notice. Free at least twice a year. Appeal process required (541.053). https://texas.public.law/statutes/tex._bus._&_com._code_section_541.052 . Build: "Export my data" and "Delete my data" buttons.
- **Enforcement.** AG has exclusive authority (541.151) and investigative authority/CIDs (541.153). Written notice plus a **30-day cure** period before suit (541.154). Civil penalty **up to $7,500 per violation** (541.155, amount per AG page). **No private right of action** (541.156). https://texas.public.law/statutes/tex._bus._&_com._code_section_541.154
- **Enforcement precedent.** Jan 13, 2025: the Texas AG sued Allstate and its subsidiary Arity in the first suit under a state comprehensive privacy law. Allegations include collecting and selling driving and location data through an SDK in third-party apps without notice or affirmative consent. https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law . Lesson for the pitch: background data collection through a phone SDK, without clear consent, is what Texas is enforcing against. Our consent UX is a feature.

---

## 4. On-device vs cloud scanning

### Google (Android / Pixel)
Source: Google blog, "New AI-powered scam detection features to help protect you on Android" (Nov 2024): https://blog.google/security/new-ai-powered-scam-detection-features/
- **Google Messages Scam Detection:** on-device AI. On by default as part of Spam Protection, only for non-contacts. Nothing leaves the device unless the user reports the conversation. A report sends sender details and recent messages from that sender to Google and the carrier. Launched in English in the US, UK and Canada.
- **Phone app Scam Detection (calls):** on-device models analyze the conversation in real time. Gemini Nano on Pixel 9+, smaller on-device models on Pixel 6+. Audio is processed ephemerally and is not recorded, stored, or sent to Google. **Off by default (opt-in).** Never runs on calls with contacts. Beeps to signal it's active. Can be turned off per call.
- **Feb 25, 2026 update:** Messages Scam Detection now uses an on-device Gemini model for longer conversational scams (job, romance / "pig butchering") on Pixel 10 and Galaxy S26 in the US, Canada and UK. Call Scam Detection is coming to the Samsung Phone app on the S26 in the US. https://9to5google.com/2026/02/25/google-messages-scam-detection-gemini/ (secondary source). The article doesn't name "Gemini Nano" for Messages, so treat the exact model name as UNVERIFIED.
- An Oct 2026 report of a further Gemini-powered Messages upgrade: https://www.droid-life.com/2026/10/14/google-messages-is-getting-a-massive-gemini-powered-scam-defense-upgrade/ . **UNVERIFIED, not read.** Check it before citing.

### Apple (iOS 26)
Source: Apple Newsroom, Oct 10, 2025, "Apple helps safeguard users from scams and fraud while protecting personal data": https://www.apple.com/sg/newsroom/2025/10/apple-helps-safeguard-users-from-scams-and-fraud-while-protecting-personal-data/ (the US URL failed to load; the SG mirror has the same article path).
- **Call Screening:** asks unknown callers for a name and reason before the phone rings. Builds on Live Voicemail. Apple calls it an on-device feature.
- **Messages:** opt-in screening of unknown senders into a separate folder. Spam goes to its own folder, and links in spam-filtered messages are disabled. Apple says categorization and filtering happen on device. iMessage has been end-to-end encrypted since 2011. Reporting a message sends it to Apple, but what data is sent isn't described.
- **Support doc:** "Screen Unknown Callers" options are Never / Ask Reason for Calling / Silence. Before iOS 17, call screening also needed Live Voicemail. https://support.apple.com/111106
- **Third-party SMS filter extension (IdentityLookup):** a developer's filter can defer a query to its own server only through a declared domain (`ILMessageFilterExtensionNetworkURL` + Associated Domains). https://developer.apple.com/documentation/identitylookup/creating-a-message-filter-app-extension . Claims that it applies only to unknown senders and that the extension can't export data: **UNVERIFIED** (couldn't load the full Apple text).

### What we can honestly claim
- Our prototype: Nemotron through a cloud endpoint (build.nvidia.com), tools called over the internet, synthetic data only. **We do NOT do on-device inference** unless we actually run a small model locally.
- Honest claims: "Privacy-preserving cloud analysis. PII is redacted before it leaves the device, only unknown senders are scanned, raw content isn't kept, every outbound call is logged and visible to the user, and nothing is used for training." Plus: "The architecture is on-device-first. On a T-Mobile phone the first-pass filter would run locally, like Google and Apple do today."
- Avoid: "end-to-end encrypted," "we never see your messages," "fully on-device," "anonymous" (redacted text with re-linkable tokens is pseudonymous, not deidentified under TDPSA 541.001).

### Suggested architecture split (team design, not sourced)
```
[Phone / client]                             [Cloud]
 1. Channel opt-in check (SMS/call/link)
 2. Contact allowlist: skip known contacts
 3. Cheap local triage: regex + URL extract
    + small classifier (optional local model)
    -> benign: drop, keep nothing
    -> suspicious:
 4. privacy_gateway(): Presidio redact the
    victim's PII, keep scam signals,
    write audit-log entry  ───────────────▶  5. Nemotron agent (redacted text only)
                                               - tools get minimal fields:
                                                 URL -> Safe Browsing / urlscan
                                                 number -> carrier lookup
                                                 CAMARA SIM-swap (mock)
                                               - no storage, no training
 7. Show verdict + confidence + actions  ◀──  6. Verdict, evidence, proposed actions
 8. User approves high-impact actions
 9. TTL deletes raw snippet (24h);
    verdict + hashes kept 30d; export/delete
```
Demo tip: show the exact redacted payload that went to Nemotron in the UI. That is the most convincing privacy proof for judges.

---

## Unverified / gaps
- Whether NIST PF 1.1 is final as of Nov 2026 (nist.gov still showed the IPD).
- Whether the TDPSA 541.201 fraud exception overrides the sensitive-data consent rule for consumer scanning (legal question).
- Exact Presidio operator names and deanonymize support after the move to community ownership.
- Apple IdentityLookup restrictions (unknown senders only, no data export).
- Exact on-device model name for the 2026 Google Messages upgrade. The Oct 2026 droid-life story wasn't read.
- 541.155 penalty amount comes from the AG page. The section text itself wasn't fetched.
