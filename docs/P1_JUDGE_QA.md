# P1 judge Q&A (call / network side). Short, true answers. Updated 2026-11-08.

Evidence tags on every claim: **[live]** seen on real Telnyx calls with a real phone; **[sim]** seen in phone-free runs (`SIM_MODE`, same hub/P2/decoy/intel path, fake caller, no Telnyx request); **[built]** implemented and covered by tests, not proven on a real call; **[design]** how it is meant to work or what we would do with a carrier, not built or not measured. If a judge pushes on a [built] or [design] claim, say that tag out loud.

Sources: `docs/PRODUCT_MAP.md`, `docs/RELEASE_NOTES_P1.md`, `docs/CLIENT_API.md`, `voip/LIVE_TEST_PLAN.md`, the hub's `/demo/latency`, and the 2026-11-08 phone-free run in `docs/DEMO_DAY_RUNBOOK.md` §3.

## What is the product, in one breath?
- A scammer calls a Backfire customer's real phone number (Telnyx). The hub listens to **the caller's side only**, warns the customer with two quiet beeps and a red alert on their phone, and on one tap (**Fire Back**) an AI decoy **in the customer's own cloned voice** takes the caller, wastes their time and extracts how they get paid. After hang-up the intel agent blocks the number network-wide (simulated carrier) and holds the pending transfer at the bank sandbox **[live]**.

## How is the call intercepted?
- The scam line is a Telnyx number whose **Call Control app** webhook points at our hub; every inbound call arrives as a signed `call.initiated` webhook **[live]**.
- The hub routes before anything rings, in about 0.1 ms: a confirmed-blocked caller is **rejected before the customer's phone rings** (BLOCKED_BACKFIRE); a trusted contact (Do Not Screen list) skips Live Guard; everyone else is LIVE_GUARD **[live]** (callback-rejected-before-ring is [built]).
- The customer uses the **Backfire mobile web app** (installable PWA, any phone browser). On LIVE_GUARD it **rings full screen with Answer / Decline**. The caller hears ringing until she taps Answer; Decline or 45 s without an answer rejects the call **[live]** (the ring/answer wiring with real Telnyx on every phone type is [built]; iOS needs the page open with the screen on).
- On Answer the hub answers the caller leg with **one bidirectional media stream, caller's audio only** (PCMU 8 kHz). In **talk mode** the customer talks back through the hub (`WS /talk`: her mic goes to the caller) and hears the caller and decoy over `WS /listen`; her mic is muted while the decoy has the call **[live]**. Her audio is never sent to detection or the decoy; the stream carries only the `inbound` track **[live]**.
- Alternatives still in the code: `MARIA_LEG=sip` (customer on a WebRTC SIP leg inside a conference) and `listen` (hear only) **[built]**.

## How fast is it? (real-call numbers)
- **Alert**: the two beeps and red alert arrive **12-18 s after the call starts**, once the scammer has said enough for P2 (Riva speech-to-text ~0.25 s, then a local Nemotron-Nano detector on a GPU) to be sure **[live]**. That time is the scammer talking, not network lag. In a phone-free run the alert came at 8.6 s on the judge card **[sim]**.
- **Handoff**: `handoff.started` under 1 s after the Fire Back tap **[live]**.
- **Decoy replies**: **~1.1-1.4 s median** from the end of the scammer's sentence to the decoy's first audio, server decoy, Nemotron plus Magpie TTS **[live]**. Barge-in works (the decoy stops when the scammer talks over it; about 3 clears in a 46 s call) **[live]**.
- **Intel block**: the intel block (number blocked, payment details, bank hold) appears **within about 2 s of hang-up** on the real call **[live]**. In the phone-free run it came 21 s after hang-up because intel ran its lookups then **[sim]**; expect anywhere from 2 s to ~45 s and do not promise 2 s.
- **Hub overhead**: routing 0.1 ms; relay to P2 0.1 ms p50; relay to the decoy and back 0.3 ms p50 **[sim, `/demo/latency`]**.
- **Restore** (call turns out legit, risk stays below 0.5 for 10 s, customer is brought back, number not blocked): measured on an earlier real call **[live]**, but not re-proven on the current talk-mode build **[built]**.

## How does the decoy sound like the customer?
- At onboarding the customer gives **separate biometric-voice consent**, then reads a random paragraph in the app. The hub forwards it to the decoy service, which keeps the best ~8 s as the clone prompt for **Magpie zero-shot TTS** (NVIDIA), no training, no fine-tuning **[live]**. She can delete the sample any time (`DELETE /voice/{id}`) **[built]**.
- **Enrollment is graded**: the service measures bandwidth, level and clipping. Phone-quality audio (nothing above 4 kHz) drops speaker similarity from ~0.82 to ~0.56 in our controlled A/B (ECAPA), so the app tells her "Saved, but it sounds like phone quality" and offers a re-record **[live]**.
- If no voice service is connected, the audio is discarded and a **synthetic voice is used**, and the app says so **[built]**.
- The decoy has no persona: it speaks as the customer, stalls, steers toward payment details, uses **fake values from code** (never her real data), and has guardrails against giving anything real **[live]**.
- Honest limit: the clone is similar, not identical, and a scammer who knows her voice well could notice **[design]**. Tuning of when the decoy speaks out of turn on PSTN is ongoing **[built]**.

## What does "Nessie hold" mean?
- The intel agent extracts the scammer's payout details from what the decoy got him to say, runs real lookups (domain age, wallet inflows), and **holds the customer's pending transfer** in the **Capital One Nessie sandbox** (mock bank, synthetic accounts; the hold is a cancellable transfer status so it is undoable) **[live]**.
- Bank-wide or network-wide actions (flag the payee account for every customer, block the number network-wide, FTC/IC3 packet) are **queued as simulated approvals** for one analyst click; nothing is sent anywhere **[sim]**. Plain code applies only what affects the customer herself (stop her own transfer); the LLM only proposes **[built]**.

## What is real and what is simulated?
- **Real [live]**: Telnyx number, signed webhooks, answer + caller-only media stream, ringing/Answer in the web app, talk mode, P2 detection, Fire Back handoff, decoy audio to the caller in the cloned voice, call end, blocklist, Nemotron intel with domain/blockchain lookups, Nessie sandbox writes.
- **Simulated either way**: the "carrier network" itself (we are not inside T-Mobile); network-wide blocks and sharing **[sim]**; bank data (Nessie is a mock sandbox); the scammer is always a synthetic voice or a teammate reading our script card; no real victims, no real scam numbers.
- **Phone-free fallback [sim]**: same hub, P2, decoy and intel with a **local fake caller**; voip sends no Telnyx request; labeled simulated. Run it with `SIM_MODE=1 MARIA_LEG=sip` (not `talk`; see runbook §3).
- **Caller ID**: the Telnyx call record shows SHAKEN/STIR "A" on the inbound leg, but the **webhook has no attestation field**, so the hub sees `attestation: none` and treats callers as unverified (fails safe: no trusted-contact bypass) **[live]**. A carrier would supply this field **[design]**.

## What about security and privacy?
- **Caller side only**: detection and decoy never receive the customer's audio; enforced in the stream code (only `inbound` frames), checked in frame counts **[live]**.
- **Signed webhooks**: Ed25519 verification, unsigned or tampered = 403 **[live]**.
- **Device pairing**: the customer's phone pairs once with a PIN; without the device token, user actions, protection log, `/talk`, `/listen` and phone login return 401; wrong PINs lock the IP out **[built]**.
- **Pipeline token** required for P2/P3/P4 to post events **[live]**. **Simulated calls are loopback-only** (never accepted through the public tunnel) **[built]**. **PSTN dial guard**: code can only dial the customer's own SIP address unless a human sets an override **[built]**.
- **Prompt-injection guard**: intel ignores artifacts from calls that never handed off, and a scammer saying "mark this number safe" cannot change her trusted list (`injection.denied`) **[live]**.
- Not done: production hardening; secrets are env vars on a laptop; `EVENTS_REDACT` is off, so `/events` over the tunnel shows transcripts to anyone with the URL **[design: say so]**.

## What does a call cost?
- A 73 s test call cost about **$0.016** on Telnyx (inbound $0.0064 + a second leg $0.01, from Telnyx call records) on the earlier SIP-leg build; the number is $1/month **[live]**. Talk mode uses no second Telnyx leg, so it should be lower; not re-measured **[design]**. Nemotron/STT/TTS costs are separate and not metered **[design]**.

## Why does it fail open?
- Protection must never break phone service. If the hub, P2, P3 or intel is down: the call still connects, routing falls back to NORMAL, a missing decoy leaves the customer on the call (`handoff.failed`), a P2 outage only drops the alert, and a P3 outage falls back to a built-in stand-in decoy **[built, partly live]**. The only thing blocked is a number we already confirmed as a scammer; emergency numbers are never blocked.

## How does this fit T-Mobile's network?
- **[design]** Scam Shield and caller-ID labels tell the customer "likely scam" and stop. Backfire sits in the call path **before the phone rings**, listens only to the caller, warns in real time, hands the scammer to a decoy that wastes time and collects payment indicators, then **blocks network-wide and shares the campaign**. In a carrier it would be a media-aware service beside the voice core (application server / SBC fork of the caller leg) with a pre-ring scam score.
- We built it on a rented SIP network: a **faithful prototype of the call path, not a carrier deployment** **[say so]**.

## What would you do with a carrier API? [design]
- Read SHAKEN/STIR attestation and carrier analytics at call setup so verified contacts skip Live Guard and spoofed callers are scored before ringing.
- Actually apply blocks, takedown requests and number-reputation updates (we only simulate them) and share campaign indicators across carriers.
- Fork the caller leg without bridging; lower latency, no extra legs.
- Customer opt-in, recording disclosure, retention limits, audit logs, and analyst approval for network-wide actions (we already gate those as pending approvals **[built]**).

## Likely follow-ups
- *"Is the scammer real?"* No. A teammate or a synthetic voice reading a script card. No real people or numbers. **[live]**
- *"Does the AI listen to the customer?"* No. Caller side only. **[live]**
- *"What if the caller is legit?"* Handoff is reversible: if risk stays low for 10 s the customer is brought back and the number is not blocked (`legit` flag on call end) **[built]**.
- *"What if the customer never taps?"* Nothing changes: the call continues normally and nothing is blocked **[live]**.
- *"What if the phones or Telnyx fail on stage?"* Phone-free run on the same stack, labeled simulated **[sim]**; a looped replay if everything fails **[sim]**.
- *"What happened with the Telnyx account?"* After repeated automated test calls an earlier backup account was temporarily blocked (restored). We stopped outbound tests, added a hard dial guard, and keep a phone-free fallback; rules in `voip/TELNYX_SAFE_USE.md`. The cause is our inference, not confirmed.
- *"Does it scale?"* We tested one call at a time; a concurrency cap and per-caller rate limit exist in code, not load-tested **[design]**.
