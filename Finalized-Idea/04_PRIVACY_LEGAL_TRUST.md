# Privacy, legal and trust design

General guidance, not legal advice. Ask the T-Mobile booth: "Is anything in this flow out of bounds for you?"

## The constraint we design around
- T-Mobile publicly says: "AI isn't listening in on calls that aren't being translated," "We do not save call recordings or transcripts," and (CTO) "We don't listen to customers' calls." Source: `03_TMOBILE_EXISTING_PROTECTIONS.md`.
- The FCC (24-84) says real-time call-content analysis "pose[s] significant privacy risks" and must comply with ECPA and wiretap law. https://docs.fcc.gov/public/attachments/FCC-24-84A1_Rcd.pdf
- Only 32% of Americans feel confident their personal data is private (Consumer Reports, Oct 2026).

## Principle: Backfire never analyzes *you*. It only analyzes and talks to *scammers*.
(v2: there is no "AI answers first" mode. Decided Nov 7.)
| What | When | Customer audio processed? | Consent |
|---|---|---|---|
| **Pre-ring blocking** | The number is a confirmed scammer for her, or linked to a confirmed campaign | **None.** The phone never rings | Backfire opt-in; undo in the protection log |
| **Live Guard** | Unknown, "Scam Likely" or caller-ID-unverified callers | **No.** Only the caller's side, in memory, never stored (cloud enclave or on-device model) | One-time opt-in, like T-Mobile's `*87*` Live Translation model |
| **Scammer Get Scammed** (decoy) | Only when **she** presses it after an alert | Her **voice profile** is used to speak; her live audio is not analyzed | Separate biometric consent for the voice profile |

## Hard promises (put them on screen)
1. Visible indicator whenever Backfire is active; one tap turns it off.
2. **Receipts** after every event: what was analyzed, what was kept, what was deleted.
3. No audio stored. No transcript of the customer stored. Only **scammer artifacts** are kept (numbers, domains, wallets, payment handles, script fingerprints).
4. No ad use, no training on customer calls. Only scammer artifacts go to the FTC, FBI IC3, registrars or exchanges.
5. Each line's user consents for their own line. The account holder can't switch it on for another adult.
6. Built so it can't spy: the service that hears calls can't send data out, and the service that files reports never sees audio.
7. Confidential computing: the call is decrypted only inside attested NVIDIA GPU enclaves. Verify Brev support before claiming we run it.

## The decoy: legal line (from the Backfire concept)
| Do | Don't |
|---|---|
| Talk only on calls the scammer started | Call, text or spam scammer numbers |
| Give fake details | Hack, scan, crash or flood their sites |
| Look up public data (domain records, public blockchains) | Publish personal information or shame anyone |
| Report to companies that can act | Pretend to be police, the FBI or a bank |
| Use synthetic data only | Threaten, or move or "steal back" money |
| Keep a human in the loop for anything that freezes accounts | Let the decoy engage before detection is confident |

## Recording and consent
- Texas is a one-party consent state; some states require all-party consent. Storing transcripts or extracted artifacts instead of audio reduces exposure but doesn't remove the question.
- Google's Pixel Scam Detection beeps to all parties and processes audio ephemerally. That's a sign big companies treat notice seriously.
- **Customer voice clone (team decision, Nov 7):** the customer reads a random paragraph at onboarding. Required safeguards:
  - a **separate, explicit biometric consent** (Texas CUBI requires informed consent before capturing a voiceprint, no sale, and destruction once the purpose ends; Illinois BIPA requires a written release);
  - stored encrypted, only in the enclave or secure store;
  - deleted on opt-out;
  - used only for Scammer Get Scammed handoffs, where the scammer already heard her voice (the AI never answers calls on its own in v2);
  - audio watermark on every output;
  - never exported or used for anything else.
- Residual risks to own in Q&A: (1) a central store of customer voice profiles is a high-value breach target; (2) a "T-Mobile clones your voice" headline, given T-Mobile itself names deepfake voice scams as a threat. Answer: consent, enclave-only storage, watermarking, live-guard-only use.

## Trust numbers for the pitch
- 69% would trade some privacy for stronger AI protection (Harris Poll for Alloy, 2025; asked about banks).
- 70% say automatic call screening would be useful (2024 consumer survey).
- 80% ignore important calls out of fear of scams (Truecaller, 2026).
- 99% of Scam Block users keep it on (T-Mobile).
