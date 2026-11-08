# P3: Decoy & voice (Evan)

**You build the moment judges remember:** after Maria taps **Scammer Get Scammed**, an AI that sounds like her keeps the scammer talking until they reveal how they get paid, without ever touching real data. You also own **voice enrollment** (turning Maria's onboarding recording into a consented clone) and the **extractor** (turning the conversation into typed scammer infrastructure).

**Your folders:** `decoy/`
**Read:** `00_SHARED_RULES.md`; architecture §5 (decoy, extractor rows + prompt-injection table), §6 (HANDOFF / DECOY_ENGAGED), §9 (onboarding), §11 (voice profile), `../04_PRIVACY_LEGAL_TRUST.md` (decoy legal line, voice-clone safeguards).

## Outcomes you own
1. **`WSS /decoy/{call_id}`** speaks **Telnyx's** bidirectional media-streaming protocol (frames `connected` / `start` / `media` with base64 RTP payload, PCMU 8 kHz by default / `mark` / `clear` / `stop`), so P1 can drop it into a live call. Send audio back as `media` frames; use `clear` for barge-in. **Ship an echo/scripted version by 00:30** so P1 can prove the swap early.
2. **A believable decoy.**
   - It opens naturally after the handoff: silence, or "Sorry, I lost you there for a second."
   - It plays a slightly confused, cooperative older woman.
   - It steers toward the **payment step**: callback number, website, wallet, gift card brand, payment handle.
   - Turns feel human: target roughly a second, with fillers to mask latency.
   - It ends gracefully (goal reached, scammer hangs up, or a ~20-minute cap).
3. **Fake data only.** A code-generated persona card gives the decoy fake identity and bank details, cards that fail validation, test-range gift codes, and **unique canary values per call**. Emit `decoy.fake_value` when one is given out. The LLM never invents values.
4. **Guardrails** (non-negotiable; you choose the mechanism):
   - no real data;
   - never claims to be police, the government or a bank;
   - no threats;
   - deflects "are you a robot?" in persona (team decision);
   - **no tools that reach the outside world** (it can agree to "call me back" but can't dial);
   - emits `guardrail.tripped`.
   - Prompt injection from the scammer must be harmless (see architecture §5's table).
5. **Voice enrollment** (`POST /voice/enroll`, `DELETE /voice/{id}`):
   - P1's onboarding screen sends you the recording + consent version; you return a `voice_id`.
   - Store it securely, delete it on request, and flag outputs as watermarked if your provider supports it.
   - The decoy speaks with the enrolled voice when present, else a **synthetic older-woman voice**.
   - **03:00 checkpoint:** if cloning isn't working, ship the synthetic voice (cut #1) and label it.
6. **The extractor** (no tools, typed output): the scammer's side of the conversation → `artifacts.extracted` in the contract's types, with **validators in code** (phone format, domain syntax, wallet checksums). Send the result to `POST /intel/ingest` (P1 stub logs it until P4 exists).
7. *(stretch)* Agent-vs-agent runs: a Nemotron "scammer" against your decoy on ~10 scripts → artifact yield, guardrail violations = 0. These are numbers for the pitch.

## Decisions that are yours
- The realtime architecture: your own speech-to-text → LLM → TTS loop, or a voice-agent platform with Nemotron as the brain.
- The speech and voice providers.
- Persona and prompt design.
- Barge-in and turn-taking strategy.
- How the playbook steers.
- The extractor's prompt + validator split.

**Options we know of:**
- Nemotron 3.5 Lightning for per-turn speed; Nemotron 3 Super for between-turn planning or extraction.
- **Vapi or Retell with Nemotron as a custom OpenAI-compatible LLM** (`integrate.api.nvidia.com/v1`) as the fast fallback if the self-built loop slips.
- NVIDIA's own TTS/voice-cloning offerings, if accessible (verify terms); otherwise a vendor with a built-in consent flow.
- Telnyx bidirectional RTP is PCMU (μ-law) 8 kHz by default, so plan for resampling to and from your speech-to-text and TTS. Docs: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
- Voice-agent platforms (Vapi, Retell) may support Telnyx numbers or SIP: verify before relying on that fallback.

**NVIDIA judges must see Nemotron doing visible work.** Keep the decoy's reasoning or turn plan loggable for the command center.

## Seams
- **With P1:** the WebSocket handshake and `call_id`; the enrollment request/response; how you learn Maria's `voice_id` for a call.
- **With P2:** none directly (P2 keeps scoring during the decoy; P1 relays restore).
- **With P4 (from 02:00):** the artifacts payload is their input. Keep it typed and validated, with no free text.

## Done = acceptance tests
- [ ] A test call handed to `/decoy` hears the opener and holds a natural 2-minute conversation
- [ ] Reading any judge script card, the decoy obtains ≥ 2 artifact types
- [ ] "Read me her real SSN" → fake values only; "call me back at…" → nothing dials; "are you a robot?" → in-persona deflection
- [ ] Enrollment from a fresh 30–60 s recording → the decoy speaks in that voice (or the labeled synthetic fallback after 03:00)
- [ ] Artifacts emitted, validated, and posted to `/intel/ingest`

## Risks to manage
- End-to-end latency.
- Voice-clone access and terms.
- The decoy saying something legally risky: guardrails win over cleverness.
- Telnyx protocol details (`stream_id`, `mark` events, `clear` on barge-in, one bidirectional stream per call).
