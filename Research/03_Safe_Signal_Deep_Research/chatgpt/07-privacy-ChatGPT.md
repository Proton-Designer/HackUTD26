# 07 — Privacy by design for Safe Signal
**Research date: 2026-11-07 | This is product design research, not legal advice.**

## TL;DR — use first
1. Build the demo with **100% synthetic text, audio, identities and transactions**; no live carrier or bank accounts.
2. Keep ingestion, URL extraction, PII masking and policy decisions local; **only send minimized, redacted content to Nemotron**.
3. Default to **no history retention**, with optional incident export/deletion; never auto-report a customer to third parties.
4. Clearly distinguish your **cloud-hosted Nemotron** from the **on-device Google Pixel** models; do not borrow their privacy claims.
5. Implement opt-in at every risky transition and describe the Texas Data Privacy and Security Act cautiously.

## A. Ann Cavoukian's 7 foundational principles -> actual features

Primary text: **Ann Cavoukian, “Privacy by Design — The 7 Foundational Principles”** — [Duke-hosted original](https://oarc.duke.edu/sites/default/files/Privacy%20by%20Design%20-%207%20Foundational%20Principles.pdf), [archived IPC original](https://web.archive.org/web/20221020132403/https:/www.ipc.on.ca/wp-content/uploads/Resources/pbd-implement-7found-principles.pdf).

| Principle | Implementation for the weekend | What to say to judges |
|---|---|---|
| **1. Proactive not reactive, preventive not remedial** | Identify suspicious requests **before** a link click or simulated transfer; offer a deliberate verification pause. | “We prevent the bad next step, not just label past messages.” |
| **2. Privacy as the default** | Default memory/off, no third-party submissions, only synthetic data, shortest possible retention. | “Safety is on by design; personal-data upload is not.” |
| **3. Privacy embedded into design** | PII masking is inside the data flow before the model, with a reject-on-sensitive-content policy. | “Redaction is architectural, not a checkbox added later.” |
| **4. Full functionality: positive-sum, not zero-sum** | Domain-risk check using minimized hostname; explicit evidence, useful advice even if user declines cloud use. | “Safe verification without having to share every conversation.” |
| **5. End-to-end security, full-lifecycle protection** | TLS for API transport; no real secrets in frontend; redact logs; in-memory ephemeral incident state; manual delete/export. | “Incident data do not become a permanent risk database by default.” |
| **6. Visibility and transparency** | Show data destination (local vs NVIDIA endpoint), sources used, mock badges, evidence confidence, side-effect consent log. | “Users can tell exactly what the agent did and did not do.” |
| **7. Respect for user privacy, user-centric** | Concise opt-in, revoke/delete, accessible language, nonjudgmental warning, review before reporting. | “The user stays in control even when AI finds a risk.” |

## B. NIST Privacy Framework — the one-page summary to use

- **NIST Privacy Framework** — [official hub](https://www.nist.gov/privacy-framework), [Getting Started guide](https://nist.gov/system/files/documents/2021/01/13/Getting-Started-NIST-Privacy-Framework-Guide.pdf). Five functions: **Identify-P**, **Govern-P**, **Control-P**, **Communicate-P**, **Protect-P**. The framework is flexible, voluntary and intended for managing *privacy risk arising from data processing*. **Use:** map five demo controls rather than claim “NIST certified.”
- **NIST brief overview/one-page source** — [Privacy Framework one-page executive graphic/presentation](https://nist.gov/system/files/documents/2019/10/15/1-5-nist-privacy-fw-lefkovitz.pdf), [full core](https://nist.gov/document/nist-privacy-framework-version-1-core-pdf). A currently published **official one-page consumer-oriented PDF** under exactly that name was **UNVERIFIED**; the short NIST briefing and framework overview are reliable substitutes. **Use in pitch:** five icon labels, one protection mechanism each.

| NIST function | Safe Signal implementation |
|---|---|
| **Identify-P** | Inventory inputs: synthetic SMS/audio, URLs, case ID, tool responses, incident receipt; forbid real customer data. |
| **Govern-P** | Rules for default retention, allowed integrations, consent, vendor access and incident deletion. |
| **Control-P** | User chooses cloud analysis, can stop workflow, remove incident and veto all side effects. |
| **Communicate-P** | Data-flow disclosure, explanation of risk and confidence limits, independent evidence citations, clear simulated badges. |
| **Protect-P** | Local masking, HTTPS, server-only key, origin-scoped session state, no arbitrary outbound tool calls, sanitized logs. |

## C. Texas Data Privacy and Security Act (TDPSA)

- **Texas Attorney General consumer privacy rights page** — [official](https://texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act). Effective **July 1, 2024**. Protects Texas residents' rights for relevant covered processing and defines personal and sensitive data; includes rights like access, correction, deletion and opting out in applicable cases. Generally exempts qualifying small businesses but has particular treatment for sales of sensitive data. **Use:** show edit/delete/export and disclosure controls now, irrespective of whether student prototype legally falls within a statutory exemption.
- **What matters in design:** a phone number, contact details, precise location, text containing identities, financial details and inferred risk profiles are potentially personal or sensitive information. Minimize collection and avoid sale/sharing, indefinite retention, or use in AI training. Whether the law applies to a specific hackathon team/business depends on status and processing; **LEGAL APPLICABILITY UNVERIFIED; not legal advice**. [Texas AG](https://texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act).
- **No deceptive privacy claim:** a cloud Nemotron inference call transmits data to a remote provider; it is **not “fully on-device”** merely because prescreening happens locally. Check NVIDIA's applicable API data terms before sending live personal data. [NVIDIA API](https://docs.api.nvidia.com/), [NVIDIA build](https://build.nvidia.com/).

## D. On-device versus cloud: what competitors really do

| Architecture | Primary reference | Honest interpretation | Reusable design |
|---|---|---|---|
| **Google Pixel Scam Detection, calls** | [Google Pixel safety](https://store.google.com/intl/en/ideas/articles/pixel-safety-features), [Gemini Nano on Pixel](https://store.google.com/us/magazine/gemini-nano-offline?hl=en-US) | Supported Pixel call Scam Detection can run *on-device*, using local model and hardware; feature off by default/depends on device. | Compare to your **local rules and masking**, not your hosted inference. |
| **Google Pixel messages/keyboard** | [Sep 2026 Pixel Drop](https://support.google.com/pixelphone/thread/466181739/september-2026-pixel-drop) | Google announced on-device Gboard suspicious-message warnings across supported messaging apps in the US. | Acknowledge the competitor already does in-the-moment local detection. |
| **Apple iOS call screening** | [Apple support](https://support.apple.com/en-us/111106) | Screens unknown calls and collects caller purpose on supported configurations. Underlying processing details for each variant **not confirmed here**. | Copy user control and simple caller explanation; never claim all processing stays local. |
| **Apple Messages** | [Apple support](https://support.apple.com/en-us/125068) | Unknown senders and SMS/MMS/RCS filter options are available; third-party extensions/platform constraints apply. | Give a user-controlled share/paste workflow rather than unpermitted access to iMessage/SMS inbox. |
| **Your demo** | [NVIDIA hosted API docs](https://docs.api.nvidia.com/) | **Hybrid:** local regex/PII masking; *redacted synthetic data* sent to hosted Nemotron for inference; local deterministic permission checker. | Put a tiny data-flow diagram directly in the pitch. |

## E. Minimal privacy-safe data flow and audit checklist

```text
[SYNTHETIC incident fixture]
         | (locally strip contact/account IDs; don't paste secrets)
         v
[redacted scenario + minimal parsed hostname]
         |---> reputation API: hostname only / third-party call disclosed
         |---> NVIDIA hosted Nemotron: synthetic redacted text only
         v
[local policy, no real account access]
         v
[proposal + explicit human consent]
         v
[SIMULATED effect + redacted receipt]
         v
[optional user export; wipe in-memory session]
```

- [ ] Toggle `use_cloud_model` off by default in a non-demo consumer design; for live judging with synthetic fixtures it can be preenabled with clear banner.
- [ ] Display `synthetic_demo_data = true`, `carrier_api = mocked`, `bank_actions = simulated` on screens.
- [ ] Use regex/Presidio locally before remote calls. [Presidio](https://microsoft.github.io/presidio/).
- [ ] Prompt logs scrubbed; model calls must not carry contact book, GPS or account passwords.
- [ ] No passive real SMS/iMessage/email ingestion; input only explicit paste/share sample.
- [ ] Consent is granular: analyze, check reputation, simulate hold, prepare report, open official website; each independent.
- [ ] Clicking “report” only prepares copy; actual filing is the user's separate action at [FTC ReportFraud](https://reportfraud.ftc.gov/).
- [ ] Retention and deletion status visible, with a clear explanation if demo backend logs fixture metadata.

## F. Two sentences ready for the pitch

> “We designed Safe Signal to protect the person, not collect their life. Local preprocessing minimizes the evidence, Nemotron reasons over synthetic redacted content, and every consequential intervention requires explicit user approval.”

This is a **prototype implementation claim only if your code actually follows the described data flow**, not a blanket security certification.
