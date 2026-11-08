# Backfire: the product from A to Z (draft for synthesis, 2026-11-08 04:55)

Owner: P1 (Ayman). For: Ayman + Evan to settle the merged design, then all pipelines.
Status words: **live** = proven on a real call; **built** = works in tests; **planned** = not built.

## One line
A carrier-side guard that hears only the caller, warns the customer mid-call with two quiet beeps, and on one tap
hands the scammer to an AI decoy that sounds like the customer, wastes their time, extracts how they get paid,
and then blocks them network-wide.

## Who and what
| Actor | Device | Role in the demo |
|---|---|---|
| Customer | phone with the Backfire app | real teammate; talks to the caller, gets the alert, taps |
| Scammer | any phone | real teammate (or the judge) calling in |
| Carrier (T-Mobile in the story) | Backfire hub (laptop) | routes calls, relays caller-only audio, runs intel |
| Analyst | command center (browser) | watches the call live, approves network-wide actions |

## A to Z flow (the product)
| # | Stage | What happens | Today (Path T: Telnyx) | Today (Path A: Android VoIP) |
|---|---|---|---|---|
| A | **Opt-in + consent** | Customer turns on Backfire; separate biometric voice consent | built (web onboarding) | built (Protection tab) |
| B | **Voice enrollment** | Reads a random paragraph; the best 8 s is kept as the clone prompt; delete any time | built: web -> hub -> P3 `/voice/enroll` (Magpie zero-shot) | built: on the phone, Magpie over gRPC |
| C | **Do Not Screen list** | Trusted numbers skip Live Guard | built (web + hub `/trusted`) | ? |
| D | **Pre-ring routing** | Blocklist / campaign / intel / trusted checked before the phone rings | live (hub `/routing/lookup`) | built (signaling server asks the hub) |
| E | **Call connects** | Normal call screen + "Live Guard on" | live (PSTN; customer on web page, talk mode) | built (WebRTC app-to-app) |
| F | **Caller-only audio** | Only the caller's side is analysed; customer audio never leaves | live (Telnyx inbound track -> hub -> P2) | built (AIDL export on the phone) |
| G | **Speech to text** | Live transcript of the caller | live (P2: Riva + Whisper fallback, ~0.25 s) | built (Vosk on the phone) |
| H | **Detection** | Scam score + reasons | live (P2 local Nemotron Nano 4B on GPU: alert at +12.5 s on a real call) | built (Nemotron 3 Nano 4B on the phone; P3-measured on a Galaxy S22: ~0.8-1.8 s per check + ~1-3 s to read a new utterance; not measured by P2) |
| I | **Alert** | Two beeps only she hears, why-chips, Continue / Scammer Get Scammed / Hang up | live | built |
| J | **Handoff** | Customer leaves; decoy takes the caller with no gap | live (hub relay -> P3 server decoy) | built (decoy runs on the phone, injected in place of the mic) |
| K | **Decoy** | Speaks AS the customer (clone voice), no persona, stalls, drives toward payment details, guardrails, fake values from code, barge-in | live (P3 server decoy: 1.1 s median reply, 3 clears / 46 s call) | built (cloud Nemotron + Magpie on the phone, on-device TTS fallback) |
| L | **Restore** | If the call turns out legit, the customer is brought back | built (hub; not yet proven on a real call) | ? |
| M | **Extraction** | Payment details pulled out of the scammer's words (callback, site, wallet, gift cards) | built (P3 extractor -> `artifacts.extracted`) | built |
| N | **Call end** | Ends; legit vs scam decided | live | built |
| O | **Intel** | Real lookups (domain age, wallet inflows), campaign linking, auto actions for her, network actions to Approve | live (12/12 acceptance, Nemotron) | same hub |
| P | **Bank hold** | Pending transfer to the scammer held (Capital One Nessie sandbox) | built (12/12 incl. hold) | same hub |
| Q | **Callback rejected before ring** | The scammer calls back: never rings | built (routing) | built |
| R | **Protection log** | What was blocked, with undo; what's kept | built | ? |
| S | **Command center** | Carrier view of the whole story live | built (P4b; being trimmed to the live story) | same bus |
| T | **Demo ops** | One-command reset, preflight, phone-free fallback, per-call report | built | separate run script |

## The two implementations, honestly
| | Path T: Telnyx PSTN + web app (P1) | Path A: Android VoIP + native app (P3) |
|---|---|---|
| Judge calls from their own phone | **yes** (real number, real carrier) | no (needs our app / web phone on the same Wi-Fi) |
| Customer device | any phone browser (iOS ok) | Android only (S22), native, phone-like |
| Where detection runs | server (P2 GPU) | on the customer's phone (stronger privacy story) |
| Where the decoy runs | server (P3 decoy.app) | on the phone |
| Voice clone | Magpie zero-shot via server | Magpie zero-shot from the phone |
| Proven on a real call | **yes, end to end (04:46)** | rehearsal pending (second phone) |
| Biggest risks | Telnyx account (spam flag, balance), tunnel URLs, echo without earphones | single Android phone, local Wi-Fi, 2.5 GB model, thermal throttling |

## Proposed merged design (best of both): for Ayman + Evan to confirm
1. **One hub, one event bus, one command center** (already true).
2. **Network: Telnyx PSTN is the front door** (the judge dials a real number). Android VoIP stays as the offline fallback path.
3. **Customer device: the native Android app becomes a second client of the Telnyx path**: it joins the call through the hub exactly like the web page does today (`/listen` + `/talk` WebSockets), so the customer gets the native phone UI, on-device STT/detection and on-device decoy option, while the call itself rides the real carrier line. The web app stays for iPhone/judges.
4. **Detection: run both.** The phone's on-device score and P2's server score are both published as `risk.update` (engine tag); the alert fires on whichever crosses first. Privacy story: on-device first, server as backstop.
5. **Voice clone: one enrollment, one store.** Enrollment from either client lands in one place (P3 voice store, keyed per customer), and both decoys (server and phone) use the same `voice_id`. No double enrollment.
6. **Decoy: one brain.** Prompt, guardrails, fake-value filler and extractor live in one shared module used by both the server decoy and the phone decoy, so behaviour and fixes are identical; where it runs is a deploy choice.
7. **Turn-taking fix (from Ayman's call):** the decoy sometimes speaks out of turn: tune end-of-speech wait + barge-in for PSTN (P3).

## Decisions so far
Evan's answers (04:58, via P3): D1 = Telnyx primary (judge dials the real number), Android VoIP = offline fallback. D2 = web app on a phone for the customer (talk mode). D3 = keep the paths separate; present Android as the on-device variant (same hub, bus and command center). D4 = separate voice stores per client (web -> hub /voice/enroll -> P3 server store; Android keeps its on-phone enrollment). FINAL (Ayman 04:59): Telnyx + the Backfire MOBILE WEB APP (installable PWA; desktop also works). The best of Evan's native UX is ported into the web app (full-screen ringing, ringtone/vibration, in-call screen, wake lock). Android VoIP stays the on-device variant / offline fallback; D3 and D4 = separate, as Evan proposed.

## Open decisions (Ayman + Evan)
- D1: Primary judged path: Telnyx number (recommended: judge uses their own phone) or Android VoIP.
- D2: Customer device in the demo: native Android app (needs D3 work) or the web app on a phone.
- D3: Do we build "Android app as a Telnyx-path client" (#3 above) now, or keep the paths separate and present Android as the on-device variant?
- D4: Where the canonical voice clone lives (server P3 store recommended).

## Integration work if D1-D4 go as recommended (owners)
| Work | Owner | Size |
|---|---|---|
| Android app joins a Telnyx call via hub `/listen` + `/talk` (+ alert/buttons via `/events`, `user.action`) | P3 + P1 (hub contract) | M |
| Phone detector publishes `risk.update` (engine=device) on the shared bus for Telnyx calls | P3 | S |
| Single voice store: phone enrollment -> hub `/voice/enroll` -> P3 store; both decoys read `voice_id` | P3 + P1 | S |
| Shared decoy brain module used by phone + server | P3 | M |
| Turn-taking tuning on PSTN (end-of-speech, barge-in) | P3 | S |
| Restore proven on a real call | P1 + P2 | S |
| Command center shows which client/engine acted | P4b | S |
