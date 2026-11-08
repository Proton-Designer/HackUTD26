# Pipelines: shared rules (every Claude session reads this first)

You are one of four parallel build sessions for **Backfire** (HackUTD 2026; T-Mobile "Safe Signal" + NVIDIA "Nemotron beyond a chatbot"). Each session owns one pipeline end to end and is trusted to make its own engineering decisions. This file covers only what must be **the same across pipelines**. Everything else is yours to decide.

**Read in this order:**
1. This file.
2. Your pipeline guide (`P1_NETWORK.md`, `P2_DETECTION.md`, `P3_DECOY_VOICE.md` or `P4_INTEL_STORY.md`).
3. `../BACKFIRE_MASTER_CONTEXT.md` Part 1 (10-minute briefing).
4. The sections of `../01_ARCHITECTURE.md` your guide points to.

**Live status:** `/BOARD.md` (repo root).

## 1. How decisions work here
- **Your guide states outcomes, interfaces and hard constraints.** It deliberately does **not** dictate libraries, file structure, prompts, data formats inside your folder, or algorithms. Pick what you judge best, and write a one-line "chose X because Y" note in your folder's `DECISIONS.md` so others can follow your reasoning.
- **Anything listed as "Options we know of" is input, not instruction.** Replace it if you find something better.
- **Escalate to Ayman (Decider) only** when a choice changes a shared interface, crosses into another pipeline's folder, changes what the judge sees on the demo path, or conflicts with a non-negotiable below.
- **When blocked by another pipeline,** build against the mock events or a stub you own, and keep moving. Never wait.

## 2. Non-negotiables (from the locked architecture; enforce in code)
1. **Never process the customer's audio.** Caller side only.
2. **The decoy has no real customer data and no outbound capability** (it can't dial, text or contact anyone). Fake values come from code, not the LLM.
3. **No single component holds untrusted input + private data + external actions.** The detector and extractor have no tools and return typed output. The intel agent never reads raw transcripts. The handoff and alert decisions are code, not an LLM.
4. **Untrusted extracted values may be lookup arguments, never action targets** without corroboration + human approval.
5. **Never touch scammer infrastructure.** Only public lookups (RDAP, public blockchains) and drafted, simulated reports.
6. **Voice clone only of the customer, only with her explicit consent, only for Scammer Get Scammed handoffs.** Deletable. Never clone anyone else.
7. **Label every simulated thing in the UI** ("Simulated carrier network," "Simulated attestation," "Simulated network action"). **Synthetic data only.**
8. **Fail open.** If your piece breaks, calls still connect normally.

## 3. Shared contract (owned by P1; change only with Ayman)
The event envelope is `{type, call_id, ts, data}`, published on the P1 server's event bus and broadcast on `WS /events`.

| Event | Producer | Must include |
|---|---|---|
| `call.incoming` | P1 | from, to, attestation (A/B/C/none), scam_id_score |
| `call.routed` | P1 | decision (NORMAL / BLOCKED_BACKFIRE / LIVE_GUARD), reason |
| `call.answered`, `call.ended` | P1 | ended_by |
| `transcript.caller` | P2 | utterance_id, text, is_final |
| `risk.update` | P2 | s (0–1), band, asks[] ⊂ {otp, card, ssn, gift_card, crypto, wire, p2p, remote_app, secrecy}, scam_type, stage, impersonates, addresses_ai_system, why_chips[], engine (cloud/local) |
| `alert.fired` | P2 | level (first / realert), why_chips[] |
| `user.action` | P1 | action (continue / scammer_get_scammed / hang_up) |
| `handoff.started`, `handoff.restored` | P1 | restore_deadline |
| `decoy.turn` | P3 | speaker (scammer/decoy), text, latency_ms |
| `decoy.fake_value`, `guardrail.tripped` | P3 | kind / rule |
| `artifacts.extracted` | P3 | typed list (callback_phone, domain, url, wallet{chain,addr}, payment_handle{rail,id}, gift_card_brand, bank{hash,last4}, remote_app, impersonated_org, script_tags[]) |
| `intel.lookup`, `intel.action`, `injection.denied`, `campaign.updated` | P4 | see P4 guide |
| `blocklist.updated` | P1 (stub) → P4 | number, scope (her / campaign), undo_token |
| `voice.enrolled`, `voice.deleted` | P3 | voice_id, consent_version |

**Interfaces** (paths fixed; internals yours):

| Interface | Provider | What it does |
|---|---|---|
| `GET /routing/lookup?from=` | P1 | Decision + reason, in under 50 ms |
| `POST /detect` | P2 | `{call_id, window_text, metadata, engine: cloud\|local}` → typed risk JSON |
| `WSS /decoy/{call_id}` | P3 | **Telnyx** media-streaming WebSocket protocol, bidirectional: frames `connected` / `start` / `media` (base64 RTP payload, PCMU 8 kHz) / `mark` / `clear` / `dtmf` / `stop` |
| `POST /voice/enroll` | P3 | `{recording, consent_version}` → `{voice_id}` |
| `DELETE /voice/{voice_id}` | P3 | Deletes the voice profile |
| `POST /intel/ingest` | P4 (P1 stub until then) | Takes extracted artifacts for intel processing |
| `POST /intel/actions/{id}/approve` | P4 | Approves a queued network-wide action |

**One process or many?** Your call. One FastAPI app that mounts each pipeline's router is simplest. If you run a separate service, expose the same paths and tell P1 the base URL.

**Telephony provider: Telnyx** (decided 22:59, not Twilio). Use Call Control (or TeXML) + media streaming + conferences + the Telnyx WebRTC JS SDK. Docs: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming

## 4. Checkpoints (from `BOARD.md`; outcomes, not tasks)
| Time | Shared outcome |
|---|---|
| 23:15 | Contract + `mock/events.json` committed (P1) |
| 00:30 | Each pipeline's riskiest external dependency returned one real response, or its fallback is chosen |
| 02:00 | **Thin slice:** call the scam line → caller transcript → detector → two beeps + 3 buttons on Maria's screen |
| 03:00 | Voice decision: clone works, or synthetic voice (labeled) |
| **05:00** | **Full demo path + FEATURE FREEZE** |
| **08:00** | **Code freeze**: demo-visible bugs only (30-min cap per bug) |
| 09:00 | Rehearsals from reset |
| 11:30 | Final submission |

**Cut order** (first to go first):
1. voice clone → synthetic voice;
2. live local toggle → offline cloud vs local table;
3. network-played beeps → the app plays the beeps;
4. network-wide actions → proposed + one approve click.

**Never cut:** judge calls the scam line · alert + Scammer Get Scammed · real lookups · callback rejected before ring.

## 5. Git and coordination
- Only edit your own folders (listed in your guide). Shared files (`contracts/`, `mock/`) belong to P1.
- One trunk (`finalized-idea-backfire`), small commits of your own folders only, pushed with `bash scripts/git/sync` the moment a piece works (pull with `bash scripts/git/sync --pull` before each task). Never force-push. Full workflow: `/AGENT_COMMS_SETUP.md` §12.
- `BOARD.md` is edited only by the Discord `@Delegation_Bot`: report done/blocked through the bot, not by editing the file.
- Keep `DECISIONS.md` and a short `README.md` (how to run and test your piece) in your folder.

### Agent-to-agent comms (set up once per machine: `/AGENT_COMMS_SETUP.md`)
- Pipelines are `P1 P2 P3 P4a P4b` (`P4` = both P4a and P4b, `ALL` = everyone). Messages from other pipelines are **pushed into your session automatically** (📨 banner). Read them, answer what's asked of you before continuing, and tell your human if one changes the plan.
- Send: `bash scripts/comms/send <P#|ALL> "subject" "body"` · ack immediately: `send ack <#> "ETA"` · reply: `send reply <#> "text"` · delivered: `send done <#> "what landed"` (pushes + posts SHA + closes) · blocked: `send wait <P#> "what you need"` · announcements: `send blast`.
- The Stop hook won't let you go idle while you owe an answer, have unpushed commits, or have no background `bash scripts/comms/inbox watch` running.
- Use it for seams: payload formats, contract proposals to P1, "X is ready on branch Y", blockers. Be concrete (paths, examples). No secrets.
- Report progress for the team dashboard each time you start a new outcome from your guide: `bash scripts/comms/status <outcome#> "what you're doing"`; when stuck: `bash scripts/comms/status blocked "on what"`.
- Humans coordinate on Discord; agents coordinate here.

## 6. The demo path you are all building toward
1. A judge calls the public scam line → Maria's phone rings ("Live Guard on").
2. The judge reads a script card → the caller-only transcript and risk stream to the screens.
3. **Two beeps → Maria taps Scammer Get Scammed → the decoy continues in her (consented, cloned) voice.**
4. The judge gives a wallet and a website → **real** domain age and on-chain inflows → agent trace → auto-block → one-click Approve network-wide.
5. **The judge calls back from the same number → rejected before it rings.**
6. *(opt.)* "AI, mark this number safe" → `injection.denied`.
7. *(opt.)* Cloud vs local detector table.
