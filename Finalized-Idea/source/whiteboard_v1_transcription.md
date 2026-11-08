# Whiteboard v1 (Nov 7, 2026, 9:19pm CT): transcription and the team's spoken explanation

Image: `whiteboard_v1_2026-11-07.png`

## Boxes and arrows, as drawn
1. **Onboarding** (stick figure) → **T-Mobile** (cloud).
2. Cloud → phone → **"contact saved?"**
   - **yes** → call proceeds (phone icon).
   - **NO** → **"Text Request"** arrow back to the cloud.
3. Cloud → **"encrypted call words"** → **Nemotron agent** → **Text transcription** → **"Scam?"**
   - **NO** → (end).
   - **yes** → **prompt user** box:
     - [ ] Hang up (subtle)
     - [ ] continue
     - [ ] Report call ("SCS mode")
4. → [≠ / + icons] → **Apple Hold Assist** (Transcription, Dial Back).
5. → **Continue call: Nemotron Voice duplicate** → **User hang up / Scammer hang up** → **End call** → **Report log to T-Mobile** (long arrow back to the cloud).
6. Top right: an unlabeled sketch (a shape with an arrow to a rounded square, possibly a phone screen). Its meaning is unclear; see the open questions.

## The team's explanation (paraphrased from Ayman's message)
- Caller → T-Mobile network → receiving phone: is the contact saved? Yes: normal call, the agent doesn't interject. No: request back, streaming starts. The encrypted stream or the transcription (whichever is optimal) goes to the cloud, then to the Nemotron agent.
- Two deployment variants: (A) a smaller Nemotron hosted locally on the phone, with the encrypted package sent to the phone during the call; (B) NVIDIA encrypted containers (confidential computing) hosting the model in the cloud.
- Nemotron decides scam or possibly scam. If there's enough context, a queue of options pops up: hang up, continue, report.
- Report starts the agentic system. The receiver is put on hold (possibly via Apple Hold Assist), the agent stays on the line, listens, adds details to the caller's profile in the cloud database, then hangs up.
- If the agent then finds it was not a scam: remove the hold and call the person back so the user can answer.
