# Open questions for the team (product and design decisions only)

These are the product, framework and design calls the architecture **does not** make for you. Technical choices (models, thresholds, data flow, routing, stand-ins) are already decided in `01_ARCHITECTURE.md`. Each question has options, what it affects, and a **suggested default** in case you want to move fast. Record answers in the "Decision" line so this file becomes the decision log.

---

## A. Core product shape

**Q1. What should happen with calls from unknown numbers?**
- (a) **Answer-first:** T-Mobile's AI picks up, asks who's calling and why, then rings you with a label. Scammers never reach you.
- (b) **Live guard:** your phone rings normally; the AI quietly listens to the caller's side and warns you if it turns scammy.
- (c) Both, with the customer choosing in settings.
- *Affects:* the demo's magic moment (b has the "hidden switch"; a looks like AT&T's receptionist), privacy optics, and how often legitimate callers get delayed.
- *Suggested:* (c), with (b) shown in the demo.
- **Decision:** B (live guard), with the caveat that once a caller is a confirmed scammer they can never contact the customer again. Implemented as a personal block if the caller ID was verified; otherwise future calls go to the decoy, plus automatic decoy routing for the same campaign from new numbers (see 01 v1.1).

**Q2. What's the hero of the pitch?**
- (a) Mode D: "Scam Likely calls get answered by our AI instead of blocked." Cleanest privacy story; no customer on the line.
- (b) Mode G: the live handoff from a real customer to the decoy mid-call. Most dramatic.
- (c) The intelligence loop: "one scam call makes everyone immune."
- *Suggested:* open with (b) as the moment, explain (a) as the default, and close on (c) as the "why only T-Mobile can do this."
- **Decision:** Suggested: open with the live handoff (Mode G), explain Mode D as the default, close on immunity.

**Q3. When the customer doesn't respond to a warning, what's the default?**
- (a) "Ask me": keep the call; re-alert once only at very high confidence.
- (b) "Protect me automatically": hand off without input, at ≥0.95 confidence plus a hard red flag (gift card, crypto, code request).
- (c) No default; force the choice at setup.
- *Affects:* safety for vulnerable users vs the risk of handing a real caller to the AI.
- *Suggested:* (c), with (a) pre-highlighted.
- **Decision:** Beep (only the customer hears it) until she picks one of three: Continue / Scammer Get Scammed / Hang up. After Continue, alert once more only if very likely a scam. No-response fallback still open → N1.

**Q4. Who does the decoy pretend to be after a handoff?** (Both reviewers recommend against cloning the customer's voice, for biometric-law and abuse reasons. Confirm you agree.)
- (a) A relative who "picked up the phone": "Hi, this is her grandson, she asked me to help." The voice change is explained naturally.
- (b) The same persona in a synthetic voice with a cover line: "Sorry, switched to my headset."
- (c) A neutral persona (e.g., "assistant") that stalls.
- *For Mode D* (the customer never answered), the decoy can be any invented persona. Do you want a fixed character, like O2's "Daisy"?
- *Suggested:* (a) for handoffs; one memorable named persona for Mode D.
- **Decision:** After handoff the decoy says nothing, or 'Sorry, I lost you there for a second.' No voice cloning (confirmed by default). Voice choice → N2. Mode D persona → N3.

**Q5. If a scammer asks "Am I talking to a robot?", what does the decoy do?**
- (a) Deflect in persona.
- (b) Admit it and end the call.
- *Affects:* the biggest reputational risk is a *legitimate* caller caught by a false positive; the legal position is unclear.
- *Suggested:* (a) in Mode D (confirmed scammer); (b) if the confidence has dropped.
- **Decision:** A, deflect in persona.

**Q6. Should screening announce itself to the caller?** (A short tone or "this call may be screened for fraud" at the start; it matters in all-party-consent states.)
- (a) Always. (b) Only in all-party-consent states. (c) Never.
- *Trade-off:* a disclosure may tip off scammers, but it protects T-Mobile legally and builds public trust.
- *Suggested:* (a), a neutral tone, framed as a trust feature.
- **Decision:** C, never announce. ⚠️ Accepted legal risk in all-party-consent states; ask the booth.

**Q7. Should "Backfire answers Scam Likely calls" be on by default for Scam Block users, or opt-in for everyone?**
- *Suggested:* opt-in for the pitch (safer). Mention default-on as a future option, since no customer audio is involved.
- **Decision:** Opt-in.

## B. Audience and scope

**Q8. Who is the named demo persona?**
- (a) Maria, 34, Spanish-speaking, on Metro: AI-fluent Spanish scams, English-first tools (from our audience research).
- (b) A family-plan account holder whose 80+ parent gets a cloned-voice call.
- (c) A college job seeker.
- *Also decide:* is Spanish support in scope for the demo (detector + decoy in Spanish)?
- *Suggested:* (a), with Spanish in at least the detector and after-card.
- **Decision:** Older woman (elderly persona).

**Q9. Are caregiver features in scope?** (The account holder proposes settings; the line user confirms; optional after-alerts to the caregiver. Also: are minors' lines excluded?)
- *Suggested:* in scope as one setup screen; exclude minors' lines.
- **Decision:** No caregiver features.

**Q10. Calls only, or texts too?** Scam texts often contain the callback number. Feeding text-scam callback numbers into the same intel loop is cheap and high-value.
- *Suggested:* calls are the product; text callback numbers feed the intel loop as a stretch.
- **Decision:** Calls only for now.

**Q11. Is the "you already shared something" recovery flow in scope?** (After-card button: secure accounts, one-tap SIM and Port-Out Protection, report.)
- *Suggested:* yes. It's the strongest "after," and it's cheap.
- **Decision:** Out of scope for now; later.

## C. Positioning and business

**Q12. Name and family:** is the product "Backfire"? The concept doc mentions **"Live Wire"** as the detection layer with Backfire as the add-on. Is Live Wire still a thing? One name or two?
- **Decision:** Keep it Backfire (single name).

**Q13. Where does it live for the customer?**
- (a) Inside T-Life → Scam Shield (a new Scam Shield feature).
- (b) A standalone app.
- *Suggested:* (a). It builds on what T-Mobile already runs and matches the "position on top of Scam Shield" finding.
- **Decision:** Inside T-Life in production; standalone app for the demo.

**Q14. Business model**
- (a) Free for everyone.
- (b) Part of Scam Shield Premium ($4/line).
- (c) Included in Experience More/Beyond plans.
- (d) Tier 1 free, live guard premium.
- *Note:* charging for protection can read as "monetizing fear" (our goal-review concern).
- *Suggested:* (d), or keep it unstated in the pitch.
- **Decision:** Keep it unstated.

**Q15. How "instant" should the burn look in the demo?** The honest design has a human analyst approve network-wide blocks and freeze requests.
- (a) Show "pending analyst review" honestly, with one-click approval in the demo.
- (b) Show the burn as instant.
- *Suggested:* (a). Lookups are instant and real; enforcement is "approved in 1 click." It earns "honest confidence" and "security."
- **Decision:** Pending; explained in chat (see N4).

## D. Whiteboard clarifications

**Q16.** What is the sketch in the **top-right corner** of the whiteboard (a shape with an arrow to a rounded square)?
- **Decision:** Irrelevant: a drawing explaining the NVIDIA container.
**Q17.** What does **"SCS mode"** under "Report call" stand for?
- **Decision:** SCS = Scammer Get Scammed (the handoff option).
**Q18.** Both reviewers say **Variant A (local Nemotron on the phone) isn't physically feasible** for this product (no app access to call audio, app suspended mid-call, model too large, decoy needs the network). Drop it entirely, or keep one slide as "future on-device warnings with phone makers"?
- *Suggested:* one line in Q&A prep, not a slide.
- **Decision:** Evan: Nemotron 3 Nano 4B at 4-bit should work. Confirmed: the model fits (~2.5GB; Bolt E4B 4GB is another option). OS limits remain, so on-device = detection on Android only → N8.

**Q19.** The whiteboard had the customer pick "Hang up (subtle)." What did "subtle" mean: hang up without alerting the scammer, or quietly in the background? The new design: key 9 ends the call, and the scammer just hears the call drop.
- **Decision:** Same layout as a typical phone call screen, plus two extra buttons: Continue and Scammer Get Scammed.

---

## Round 2: new questions raised by the round-1 answers (Nov 7, 10pm)

**N1. If she never answers the beeps, what happens?** An older user may not understand the tone, or may have the phone on speaker. Beeping forever over a call makes it hard to hear.
- (a) Keep a soft tone every ~5 s for the rest of the call.
- (b) After ~20 s without an answer **and** very high confidence + a red flag (gift card, crypto, code request), hand off to the decoy automatically.
- (c) Stop after ~20 s and send an after-card.
- *Suggested:* (b). It protects the person least able to respond, and the bar for acting alone stays very high.
- **Decision:** Two beeps, then stop. Two more only if the alert fires again or the likelihood rises.

**N2. What voice does the decoy use after handoff?** "Sorry, I lost you" covers a pause, but not a different-sounding voice.
- (a) A stock older-woman synthetic voice chosen to roughly match the customer's profile (age and gender set at onboarding). Not a clone, so no voiceprint.
- (b) Whatever stock voice, and accept the mismatch (scammers often push through anyway).
- (c) A different person ("her grandson picked up"), which explains the voice change.
- *Suggested:* (a), with the "lost you" line.
- **Decision:** Clone the customer's own voice from a random paragraph read at onboarding. Implemented with safeguards (separate biometric consent, enclave-only storage, live-guard handoffs only, never Mode D, watermark, delete on opt-out).

**N3. In Mode D (flagged calls the decoy answers directly), who is the decoy?** She never picked up, so it can be anyone. One recurring named character gives the product a memorable "face" (like O2's "Daisy").
- *Suggested:* one named older-woman character, plus a name for her.
- **Decision:** Asked which calls get answered directly; explained in chat. Persona name still open → N11.

**N4. The burn (Q15): fully instant, or honest approval steps?** (Explained in chat.)
- (a) Everything instant.
- (b) Split: instant and automatic for actions that only affect *this customer* or are low-harm and reversible (her personal block, decoy routing, adding the callback number to the Callback Protection warning list); **one-click analyst approval** for network-wide blocks, website takedowns and freeze requests.
- (c) Everything waits for a human.
- *Suggested:* (b).
- **Decision:** Optimal = split: automatic for customer-scoped and low-harm actions; one-click analyst approval for network-wide and external actions.

**N5. How often should she be told about intercepted calls?** With "never contact you again" plus Mode D, she may get many silent interceptions.
- (a) A notification every time.
- (b) A daily or weekly "Your shield" summary.
- (c) Notify only for live-guard calls; summarize the rest.
- *Suggested:* (c).
- **Decision:** Explained in chat (Mode D triggers). Notification cadence follows N10 (nothing per call) → digest question N12.

**N6. Can she undo a "never contact again" block?** (e.g., it turns out it was her pharmacy)
- *Suggested:* yes, from the protection log, with one confirmation.
- **Decision:** Yes.

**N7. Is there a second screen in the demo?** The customer app is one. A **T-Mobile-side "command center"** would show campaigns forming, artifacts burned, the analyst approve button and the immunity counter.
- *Suggested:* yes. It's where the intelligence loop and the NVIDIA agent trace become visible.
- **Decision:** Yes.

**N8. On-device detection (Evan's 4B model): in the demo or not?** It's real only as Android on-device detection, with the decoy still in the network. Showing it costs build time but adds a "privacy mode" story.
- (a) Cloud only (confidential-computing story).
- (b) Cloud + an "on-device detection" toggle running Nemotron 3 Nano 4B / Bolt E4B locally (Android phone or laptop stand-in).
- (c) Mention it in Q&A only.
- *Suggested:* (c) unless someone is free after the core flow works; then (b).
- **Decision:** Build both: (1) NVIDIA confidential-computing cloud container; (2) local Nemotron 4B model doing detection.

**N9. Who plays the scammer in the live demo?** A judge reading a script card (most memorable; riskier) or a teammate (safer)?
- *Suggested:* a judge, with a teammate as backup.
- **Decision:** Yes. Anyone can call a specific public number and play the scammer.

**N10. What does she see after a live-guard call: the scammer's words, or just a summary?**
- *Suggested:* summary + why chips by default; "show what they said" one tap away (caller side only).
- **Decision:** Nothing shown per call; the agent handles confirmed scams automatically.

## E. To ask the T-Mobile booth (theirs to answer, not ours)
See `01_ARCHITECTURE.md` §17. The top three:
1. Is a fake-persona decoy OK for your brand?
2. Would opt-in + caller-side-only + no-retention enclave fit your "we don't listen" commitment?
3. Is anything in this flow out of bounds?

---

## Round 3 (Nov 7, 10:15pm)

**N11. The Mode D decoy character.** On calls the decoy answers directly, she never picked up, and her clone isn't used there (safeguard). So the decoy needs its own persona. One recurring named older-woman character?
- *Suggested:* yes. Give her a name, which doubles as the brand moment (e.g., "Scammers keep getting Grandma ___").
- **Decision:** Moot after round 4: the AI never answers calls directly. (If she skipped voice consent, the decoy uses a synthetic older-woman voice.)

**N12. "Feel protected after" without per-call notices.** T-Mobile's brief rewards customers *feeling* protected after a threat. If she never sees anything, judges may ask where the "after" is.
- (a) Nothing at all.
- (b) A quiet weekly "Your shield" summary she can ignore ("4 scam calls handled for you this week").
- (c) Visible only in the app's protection log when she opens it.
- *Suggested:* (b) + (c).
- **Decision:**

---

## Round 4 (Nov 7, 10:25pm): routing locked
- **"Scam Likely" calls:** follow the normal workflow (ring with Live Guard on; the label still shows). No AI-answers-first mode at all.
- **Confirmed scammer number:** automatically blocked (for her; undo in the protection log).
- **Number from the same scam network/campaign:** automatically blocked before ringing.
- Implemented in `01_ARCHITECTURE.md` v2 §3 and §10. Network-wide blocking for all customers still needs one-click analyst approval and a verified caller ID.

**Still open:** N12 (weekly summary vs log only).
