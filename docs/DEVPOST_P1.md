# Devpost draft: P1 (the call path, the hub, the customer app)

Draft for the lead to merge into the team Devpost. Tags: **[live]** real phone call; **[sim]** phone-free simulated run; **[built]** tested, not proven live; **[design]** idea only. Numbers are from 2026-11-08; see `docs/P1_JUDGE_QA.md` for sources.

## What P1 built
The part of Backfire you can pick up and use: a real phone number, the server that sits in the call path, and the customer's app.
- **A real scam line.** A Telnyx number whose webhooks hit our hub. Anyone can call it from any phone **[live]**.
- **The hub** (one Python/FastAPI process): pre-ring routing (confirmed-scammer callers are rejected before the phone rings; trusted contacts skip screening), an event bus every other piece plugs into, caller-only audio relay to detection and the decoy, and demo ops (reset, preflight, safe restart, per-call report) **[live]**.
- **The customer app**: a mobile web app (installable, any phone browser). The call rings full screen with **Answer / Decline**; in **talk mode** the customer speaks to the caller through the hub; when detection fires she gets two private beeps, a red alert with why-chips, and three buttons: Continue, **Fire Back**, Hang up. Onboarding includes a separate biometric-voice consent and a graded voice enrollment, a Do Not Screen list and a protection log with undo **[live]**.
- **Fail-open design**: if any Backfire part breaks, the call still connects.
- **A phone-free fallback** (`SIM_MODE`): the same stack with a simulated caller, clearly labeled, for when phones or Telnyx fail **[sim]**.

## How a call flows
1. A scammer dials the number. The hub checks the blocklist, campaigns, trusted list and emergency numbers in ~0.1 ms **[live]**.
2. The customer's phone rings in the app. She taps Answer; the call connects with **one media stream carrying only the caller's audio** **[live]**.
3. Detection (P2: Riva speech-to-text, a local Nemotron-Nano scam model) scores what the caller says. At **12-18 s** the app beeps twice and shows the alert **[live]**.
4. She taps **Fire Back**. The hub starts the decoy first and mutes her mic. The decoy (P3) answers **in her cloned voice** (NVIDIA Magpie zero-shot from a ~8 s enrolled sample), median reply **~1.1-1.4 s**, and steers the scammer toward saying how he gets paid **[live]**.
5. When the scammer hangs up, the intel agent (P4, Nemotron) reads what the decoy extracted, runs real domain and blockchain lookups, **holds her pending transfer in the Capital One Nessie sandbox**, blocks the number, and queues bank-wide and network-wide actions for one analyst click. On the real call the block appeared within about 2 s of hang-up; allow up to ~45 s **[live]**.
6. If the number calls back, it is rejected before ringing **[built]**. If the call was actually legit, risk stays low and the customer is brought back instead **[built]**.

## What is real and what is simulated
- **Real:** the phone call, the Telnyx number and signed webhooks, ringing and talking through the app, caller-only audio, detection, the cloned-voice decoy, the intel agent's lookups, the Nessie sandbox hold **[live]**.
- **Simulated:** the carrier. We are not inside T-Mobile, so network-wide blocks and indicator sharing are queued approvals that send nothing; the bank is a mock sandbox with synthetic accounts; the "scammer" is a teammate or a synthetic voice reading a script; caller-ID attestation never reaches our webhook, so we treat callers as unverified **[sim]**.
- **Privacy rule we enforce in code:** the customer's audio is never analysed or sent to the decoy; only the caller's side is **[live]**.

## Honest limits
- A prototype of the call path on a rented SIP network, **not a carrier deployment**; a carrier would run it in its own core, with real attestation, enforcement and a pre-ring score **[design]**.
- Detection needs the scammer to say enough words first, so the alert is 12-18 s in, not instant **[live]**.
- The cloned voice is close, not perfect; phone-quality enrollment audio gives a clearly worse clone, which is why the app grades the recording and offers a re-record **[live]**.
- Tested one call at a time; concurrency and rate limits exist in code but were not load-tested **[design]**. Restore-to-customer after a legit call is built but not re-proven on the current build **[built]**.
- iOS needs the page open with the screen on, and a phone mic can echo without earphones.
- Shared NVIDIA quota: heavy rehearsals can degrade to rules-only detection and canned decoy lines.
- The talk-mode phone-free path has a known gap: use `SIM_MODE=1 MARIA_LEG=sip` for the fallback (`docs/DEMO_DAY_RUNBOOK.md` §3).
- Security is demo-grade: device PIN pairing, signed webhooks, pipeline token and a dial guard are in, but secrets are env vars on a laptop and event redaction is off.

## Built with
Telnyx (Call Control, media streaming), FastAPI, WebSockets, NVIDIA Nemotron (detection, decoy, intel), NVIDIA Riva speech-to-text, NVIDIA Magpie TTS (zero-shot voice cloning), Capital One Nessie sandbox, Cloudflare quick tunnels, a vanilla-JS installable web app.
