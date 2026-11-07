# DubHacks — DubHacks 2026 (2 projects)

### Fluffy
*DubHacks DubHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: Best Voice Agent

**What it is:** A camera- and voice-driven home assistant aimed at elderly care. A vision-language model labels people and objects in a room, infers what the person needs from what they say and do, and fires tool calls such as dimming lights, playing music or texting a caretaker.
**Problem / user:** Elderly people living at home and their caretakers; the page frames it as a daily-life concern rather than a formal problem statement.

**Features**
- Scene labeling with ownership and relative position — Perceptron Mk 1.5 VLM labels objects and people against a reference frame (right door, left wall) and assigns who owns what. *[claimed]*
- Need inference from speech plus vision — Combines transcript and visual context, e.g. coughing and throat scratching implies the person wants water. *[claimed]*
- Tool-call execution from a fixed set — Chosen tools include text, play song, dim lights, open windows, notify caretaker; then waits for user reaction. *[shown_working]*
- Consent-gated plan harness — Executor validates plans; comfort actions need a consent source, notify and safety actions run pre-agreed; undecided plans expire after 30 seconds. *[shown_working]*
- Emergency texts to caretaker — Photon API sends the message to a configured caregiver destination; caregiver can acknowledge alerts. *[claimed]*
- Music via Spotify and ElevenLabs voice — Spotify OAuth playback; ElevenLabs synthesis configured as optional provider. *[claimed]*
- Simulated living room — Mock home service and 3D room (React Three Fiber) show lights and windows changing over websockets. *[shown_working]*

**Flow:** Camera and microphone stream continuously → VLM labels people and objects relative to a reference frame → Ownership and positions are assigned → System infers the next needed action from words and visuals → Plan is checked for consent and a tool call is made → Action executes in the mock home or via Photon/Spotify → System waits for the person's response

**Prompt:** Build a messaging agent on Photon reachable on real channels; voice agents on a Photon phone number count for the Best Voice Agent prize.
**Fit (explicit):** Page says Photon API was used for emergency texts to caretakers; the assistant is voice-driven, though most of the voice pipeline uses Chrome speech-to-text and ElevenLabs rather than Photon.  *(targeted: Photon: Best Voice Agent)*
**Sponsor tools:** Photon API (Emergency texts to a caretaker as one tool call, supporting); Perceptron Mk 1.5 (Vision-language scene labeling and inference, core)
**AI:** Perceptron Mk 1.5 VLM labels the scene and infers need; planned Grok voice reasoning was dropped for lack of credits; Chrome speech-to-text replaced slow Mk 1.5 transcription. Code largely written with parallel Cursor agents.
**Architecture:** Frontend (Next.js, 3D room) talks over websockets to a FastAPI harness that validates plans and consent, an executor, and a mock-home service; external providers are Perceptron, ElevenLabs, Spotify, Photon.
**Novelty:** Explicit consent model separating comfort from pre-agreed safety actions, and a schema-validated plan layer between inference and actuation; simulated home instead of hardware.
**Scope:** large · working: Repo has about 36k LOC, tests and a runnable harness with mock room; no live demo or video. · polish: 3D room UI, schemas, docs and env bootstrap; only three screenshots on Devpost.
**Claims:** Entire codebase written with up to 8 Cursor agents at once
**Gaps:** No video; No quantitative results; Voice pipeline details thin
Sources: https://devpost.com/software/fluffy-xq8lgp, https://github.com/edwinthemathman/dubhacks26-Fluffy

---

### restock
*DubHacks DubHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Photon: Runner Up

**What it is:** An iMessage agent for shared households. Roommates text what they ran out of, get three live-priced options ranked by unit price, mark items shared or personal, and one 'order now' text places a demo order and splits charges per person via Stripe test mode.
**Problem / user:** Roommates and groups who juggle a chat, a store app and a payment app, with one person fronting cash and chasing repayment.

**Features**
- Natural-language restock requests — Claude parses casual texts and matches them to catalog items; deterministic commands like 'add dish soap' work as fallback. *[shown_working]*
- Live-price options ranked by unit price — SerpApi Google Shopping results filtered to major retailers and ranked in code; model only picks listing numbers. *[shown_working]*
- Shared vs personal classification — Items auto-classified, user replies 'personal' to flip; expensive personal items need an approver's yes. *[shown_working]*
- Order and bill split — 'order now' authorizes each member's share via off-session Stripe PaymentIntents, capturing only when all succeed; cardless members are covered by the owner. *[shown_working]*
- Per-person Restock numbers with relay — Photon shared lines give each member a number; household news is relayed to every thread. *[shown_working]*
- Web signup and OTP dashboard — Mobile-first pages for start, join, pay-back and a dashboard logged in by texted 6-digit code. *[shown_working]*
- Safety guards — Luhn check drops pasted card numbers, idempotent charges and webhooks, redaction of personal data, AI disclosure on request. *[claimed]*
- Group chat and real checkout — Bind household to a real iMessage group; real merchant ordering and Stripe Connect payouts. *[planned]*

**Flow:** Owner starts a household on the website and gets a Restock number → Owner texts hi, invites roommates by link → Owner adds a card via Stripe link → Member texts 'we're out of dish soap' → Restock replies with three ranked options; member picks one → Anyone texts 'order now' and confirms with yes → Each person gets a private receipt or pay-back link

**Prompt:** Build a messaging agent on Photon reachable on real channels such as iMessage; track winner, runner-up and best voice agent prizes.
**Fit (explicit):** README lists Photon Messaging Agent as a target; the whole product is an iMessage agent running on Photon 2.0 with real numbers, built on shared lines after dropping the group-chat design for plan cost.  *(targeted: Photon: Messaging Agent, Visa: Reimagine Shopping, VEYZL: Best Use of VEYZL, Best Startup Idea)*
**Sponsor tools:** Photon 2.0 (All messaging: iMessage numbers per member, inbound parsing, relays, core); VEYZL (Security audit on every pull request, fixes logged, supporting)
**AI:** Claude API for intent parsing, item matching, Q&A and choosing among listings; model output is schema-validated, listings treated as untrusted, and only listing numbers are returned.
**Architecture:** Photon inbound webhook into a Node/TypeScript Express server with SQLite; Claude for intents, SerpApi for prices, Stripe for cards and charges; deployed on Railway with a web dashboard.
**Novelty:** Payment logic covers cardless members, idempotent retries and all-or-nothing capture; documented pivot from group chat to per-person lines; security audit trail kept in docs.
**Scope:** large · working: Live site restock.select, about 19k LOC, tests including idempotency across restarts, CI; orders are demo only. · polish: Detailed README with sample transcripts and FAQ, privacy page, health check, dashboard.
**Claims:** Charges and webhooks are idempotent, tested across server restarts | All shares are captured only after every share authorizes
**Gaps:** No video; No usage metrics
Sources: https://devpost.com/software/restock-n5hxgo, https://github.com/aknotwell/restock

---

