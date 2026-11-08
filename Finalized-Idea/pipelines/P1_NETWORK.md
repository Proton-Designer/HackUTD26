# P1: Network & call control (Ayman, machine A)

**You are the "carrier network" and the integration hub.** You own the shared contract, the server everyone plugs into, Maria's app (including **onboarding**), and everything **Telnyx** does. In production this is T-Mobile's IMS call server and media server (architecture §3, §4, §15). In the demo it's **Telnyx** + your server, labeled "Simulated carrier network." (Architecture §15 says Twilio; the team switched to Telnyx at 22:59. The mapping is below.)

**Your folders:** `contracts/`, `mock/`, `server/`, `voip/`, `web/customer/` (+ merges to the main branch)
**Read:** `00_SHARED_RULES.md`; architecture §0, §3, §4, §6, §7, §9, §12, §15.

## Outcomes you own
1. **Contract first (23:15).** `contracts/` reflects shared rules §3. `mock/events.json` replays at least 3 believable calls (an IRS gift-card scam, a legitimate bank-fraud-department call, a crypto scam), so the other screens and pipelines can build without telephony.
2. **The hub.** A server with the event bus + `WS /events`, the routing store (her confirmed scammers, campaign numbers, trusted numbers with attestation), and a public URL Telnyx can reach.
3. **A public scam line (a Telnyx number).** Anyone can call it. Calls are routed **before ringing**:
   - confirmed or campaign-linked numbers → rejected;
   - trusted + verified caller ID → normal;
   - everything else (incl. "Scam Likely") → Live Guard.

   Abuse-safe: per-caller limits and a call cap.
4. **Caller-only audio** reaches P2's speech-to-text. Maria's audio is never sent anywhere.
5. **Maria's app** (`web/customer/`), a standalone mobile-web app that *is* her phone:
   - **Onboarding:**
     - Backfire opt-in.
     - Separate voice consent (biometric, clearly worded).
     - A **random paragraph** to read aloud, recorded and sent to P3's `POST /voice/enroll`.
     - A delete-my-voice control.
   - **Call screen:** feels like a normal incoming/active call, plus a "Live Guard on" label. On `alert.fired`: **two beeps only she hears**, why chips, and **Continue / Scammer Get Scammed / Hang up**.
   - **Protection log:** blocked numbers with **undo**, calls handled, what's kept.
6. **The handoff.** On Scammer Get Scammed, Maria leaves the call and P3's decoy takes over the caller's side, with no audible gap or hold music. A restore path brings her back if P2 signals a legitimacy restore. Restore is below the cut line.
7. **Callback rejection without P4 (stub).** When a decoy session ends, add the caller to her confirmed list and emit `blocklist.updated`. The judge's callback is then rejected before ring. P4 replaces this with the policy gate later.
8. **Demo operations:** a one-command reset, a `DEMO_MODE` cached replay for when live telephony fails, and a latency log. Ten clean runs from reset by 08:00.

## Decisions that are yours
How you do all of the above:
- server framework;
- the Telnyx pattern for both call halves and the swap (Call Control vs TeXML);
- the WebRTC client vs dial-out approach for Maria;
- tunnel vs hosted deploy;
- UI stack and design;
- how the beeps reach only her;
- how you store state.

**Options we know of (Telnyx; not instructions):**
- **Caller-only audio:** Call Control `streaming_start` with `stream_track=inbound_track` on the caller's leg (or TeXML `<Start><Stream>`).
- **Decoy audio into the call:** bidirectional streaming (`stream_bidirectional_mode=rtp`, codec PCMU 8 kHz; `stream_bidirectional_target_legs` picks which leg hears it), pointed at P3's `/decoy/{call_id}`.
  - **Note:** only **one bidirectional stream per call**, and starting a new stream may replace the existing one. Test whether the caller-only detection stream and the decoy stream can coexist, or move detection to the decoy stream after handoff.
- **Swapping Maria out:** Telnyx conference commands (join/leave participants), or Call Control bridge/unbridge of the two legs.
- **Maria's app as the phone:** the Telnyx WebRTC JS SDK, so the web app is a real endpoint.
- **Rejecting before ring:** Call Control `reject` on `call.initiated` (or TeXML `<Reject>`).
- **Caller-ID verification:** check the `call.initiated` webhook payload for SHAKEN/STIR attestation fields; fall back to a demo toggle.
- **Beeps:** local playback in the app (simplest; only she hears them), or the network plays audio to her leg only.
- **Security:** verify webhooks and stream connections with Telnyx's Ed25519 signature headers.
- **Tunnel:** cloudflared or ngrok.
- Docs: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming · https://developers.telnyx.com/api-reference/call-commands/streaming-start

## Seams to agree on early
- **With P2:** how audio frames or partial transcripts get to them (in-process call vs websocket vs queue), and the cadence of `/detect` calls (P2 owns the cadence; you own the frames). Confirm the sample rate and encoding together.
- **With P3:** the decoy WebSocket handshake (Telnyx `connected` / `start` frames, `stream_id`, `mark` / `clear`), and the `call_id` you pass (e.g., as a custom stream parameter or in the URL). **Get P3's echo bot working on a real call by 00:30**: it's the riskiest seam in the whole build.
- **With P4 (from 02:00):** P4 takes over writing the blocklist, and your routing lookup reads what they write.

## Done = acceptance tests
- [ ] A listed number calling the scam line hears a rejection; Maria's phone never rings
- [ ] An unlisted number rings Maria's app with "Live Guard on"
- [ ] Caller speech shows up as `transcript.caller`; Maria's speech never does
- [ ] Mock `alert.fired` → two beeps + 3 buttons; each button emits `user.action`
- [ ] Scammer Get Scammed → the caller keeps talking to the decoy with no audible break
- [ ] After the decoy ends, the same number calling again is rejected before ring
- [ ] Onboarding records a paragraph and stores the returned `voice_id`; delete works
- [ ] Reset → a clean demo in under 30 seconds

## Risks to manage (your call how)
- Conference swap latency or audio gaps.
- The venue Wi-Fi and the tunnel.
- Phone browsers blocking autoplay of the beeps.
- Telnyx account verification and number purchase: do it first, it can take time.
- Being the merge bottleneck: merge on a schedule, not on demand.
