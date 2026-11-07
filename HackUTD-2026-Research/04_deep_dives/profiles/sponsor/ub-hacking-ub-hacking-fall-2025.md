# UB Hacking — UB Hacking Fall 2025 (1 projects)

### EAS&E
*UB Hacking UB Hacking Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best AI/ML Hack (prize: NVIDIA Orion Jetson Nano per team member; low confidence, no NVIDIA challenge)

**What it is:** A web app for people with arthritis that uses the camera and MediaPipe to track hands and pose while they trace exercise shapes, with a voice assistant for arthritis questions and a Gemini-written session report.
**Problem / user:** People with arthritis who struggle to keep up therapeutic hand, wrist and posture exercises and need simple, low-typing interfaces.

**Features**
- Hand-tracing exercises — MediaPipe hand model tracks wrist and fingers while the user traces on-screen shapes *[claimed]*
- Posture exercises — MediaPipe pose model for posture movements *[claimed]*
- Fine motor exercises — Camera-based finger precision tasks *[claimed]*
- Custom exercise shapes — User draws shapes targeting a pain region; saved in Firebase *[claimed]*
- Eva voice assistant — ElevenLabs conversational agent with RAG answers arthritis questions and guides site use *[claimed]*
- Speech-to-text input — Voice input to reduce typing *[claimed]*
- Gemini session report — Gemini summarizes the exercise session *[claimed]*
- Accessible layout — Large buttons, simple instructions, minimal typing *[claimed]*

**Flow:** Open the web app and allow camera → Pick or create an exercise → Trace shapes while hand tracking responds → Ask Eva questions by voice → Receive a session report

**Prompt:** not public / not found
**Fit (implied):** Combines computer-vision hand tracking, a voice RAG assistant and LLM reporting; the page does not state a prize target.  *(targeted: Best AI/ML Hack)*
**AI:** MediaPipe hand and pose models for tracking; ElevenLabs conversational AI with RAG for the Eva assistant; Gemini generates session reports.
**Architecture:** React/Tailwind front end on Vercel with MediaPipe in the browser; Node/Express backend (Railway) with Firebase storing custom shapes; ElevenLabs and Gemini APIs.
**Novelty:** Targets an accessibility niche with gesture tracing exercises plus voice agent; custom shapes by pain region.
**Scope:** small · working: Live Vercel demo link listed; no repo, video or measured results. · polish: Accessibility-oriented UI described; page is short with no walkthrough.
**Claims:** Fully functional hand tracking exercise
**Gaps:** no repo; no video; no user flow on page; prize text not found
Sources: https://devpost.com/software/eas-e

---

