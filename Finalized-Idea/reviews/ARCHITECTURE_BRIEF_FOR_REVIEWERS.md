# Brief: proposed Safe Signal / "Backfire" architecture (team whiteboard, Nov 7 2026, 9:19pm CT)

## The challenge (T-Mobile "Safe Signal", HackUTD 2026) and NVIDIA track
- T-Mobile: "Protect customers from scams and fraud in ways we haven't thought of yet." Any approach (prevention, real-time protection, education, new security features). Scam detection is a core piece, not the whole product. Go beyond classification: safeguards and customer-facing experiences. Clear next steps, honest confidence, privacy by design. Synthetic data only (no real customer data). Judges: creativity, impact, usability, security and privacy, detection quality. Big unlock: customers feel protected before, during and after a threat.
- NVIDIA: use Nemotron beyond a chatbot: multi-step workflows, agents that plan and execute, tool integration, real-world applicability.

## Whiteboard (transcribed; image at /mnt/user-data/attachments/8c1c987d-074d-51ce-9b23-94847e35d26b/f76a44bb-image.png)
1. Onboarding (customer opts in) → T-Mobile network (cloud).
2. Incoming call → network asks the receiving phone: "contact saved?"
   - YES → call proceeds normally, agent does not interject.
   - NO → phone sends a "text request" back to the network → network starts streaming "encrypted call words" (encrypted audio stream or transcription, whichever is optimal) to the Nemotron agent.
3. Nemotron agent → text transcription → "Scam?"
   - NO → nothing.
   - YES → prompt user with options: [ ] Hang up (subtle), [ ] Continue, [ ] Report call ("SCS mode").
4. Report → the receiver is put on hold; uses **Apple Hold Assist** (transcription, dial back). The agent "continues call" using a **Nemotron voice duplicate** (decoy voice, possibly cloned to sound like the user), listens to the scammer, extracts details and adds them to a scammer-profile database in the cloud, then hangs up.
5. End: user hangs up / scammer hangs up → end call → report log to T-Mobile (fed back into the network).
6. If the agent later decides the call was NOT a scam: remove hold and "call back" the person so the user can answer.

## Two deployment variants the team wants
- **A: Local.** Smaller Nemotron model on the phone; the network sends the encrypted package directly to the phone during the call; phone decrypts and runs detection.
- **B: Cloud confidential computing.** Nemotron hosted in NVIDIA confidential-computing (encrypted, attested) containers; network sends encrypted package there.

## What we already established (treat as findings, verify if you doubt them)
- iOS gives NO third-party app access to cellular call audio, transcripts or call logs, even for calls labeled spam. CallKit covers only an app's own VoIP calls. Call Directory / Live Caller ID Lookup only supply labels by number. Message Filter extension can classify SMS. Android also blocks call-audio capture (system-only permission) but allows foreground services.
- iOS suspends background apps during a normal cellular call; no allowed background mode covers "analyze someone else's call".
- Current Nemotron 3 Nano is ~30B total / ~3B active params (MoE) — too big for iPhone RAM (8–12GB). Older ~4B Nemotron variants may exist (UNVERIFIED).
- So all call audio access must happen in the carrier network. Demo stand-in: Twilio programmable voice (Media Streams over websocket, Conferences for leg add/remove) or Vapi/Retell with Nemotron as custom LLM via OpenAI-compatible endpoint integrate.api.nvidia.com/v1.
- T-Mobile today (see /home/claude/tmobile_existing_scam_features.md): all call protection is number/pattern-based (Scam ID "Scam Likely", Scam Block #662#, Caller Verified STIR/SHAKEN, Callback Protection for outgoing calls). ~29B calls tagged scam/spam in 2025. NO content-based call analysis. T-Mobile runs in-network AI Live Translation (beta, per-call opt-in via *87*) and publicly said "AI isn't listening in on calls that aren't being translated", "We do not save call recordings or transcripts", CTO: "We don't listen to customers' calls." AT&T piloted a network AI receptionist (Sep 2025). Analytics vendor: First Orion. T-Mobile runs a honeypot program for network attackers.
- FCC 24-84 flags privacy risks of real-time call content analysis; must comply with ECPA/wiretap laws. Texas is one-party consent; some states require all-party consent.
- Prior recommendation (to evaluate, not assume): Tier 1 = decoy answers calls ALREADY flagged "Scam Likely" by metadata (customer never on line, no customer audio). Tier 2 = opt-in screening of unknown/unverified callers, caller leg only, ephemeral, keep only extracted scammer artifacts. Saved contacts whose caller ID fails STIR/SHAKEN verification should be treated as unknown (spoofed-family-member voice clones). Don't prompt at ring time; one-time setting plus a mid-call "Bring in Backfire" button. Confidential computing ("open the letter in a locked room") preferred over local model.
- Backfire concept doc (decoy + extract + burn + legal Do/Don't): /mnt/user-data/attachments/8c1c987d-074d-51ce-9b23-94847e35d26b/a070326a-attachment.txt
- Cost estimate: self-hosted ASR+Nemotron ≈ $0.0005–0.001 per screened minute; ≈ $0.02 per opted-in user/month.

## Supporting files (read what's relevant)
- /mnt/user-data/uploads/HackUTD-26/Research/00_HackUTD2026_Challenge_Briefs.md
- /mnt/user-data/uploads/HackUTD-26/Research/03_Safe_Signal_Deep_Research/claude/ (01-nvidia-stack, 02-tool-apis, 05-detection-confidence, 06-agent-security, 07-privacy)
- /mnt/user-data/uploads/HackUTD-26/Research/05_Target_Analysis/ (00c_GOAL_DECISION, 04_Top4_Audiences)
- /mnt/user-data/uploads/HackUTD-26/HackUTD-2026-Kit/ (decisions/architecture.md, domains/13-architecture-tradeoffs.md, domains/15-ai-app-design-eval.md, decisions/pitch-demo.md, domains/01-judging.md)
- /home/claude/tmobile_existing_scam_features.md
