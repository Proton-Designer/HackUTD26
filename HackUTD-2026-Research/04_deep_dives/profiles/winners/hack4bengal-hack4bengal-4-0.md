# Hack4Bengal — Hack4Bengal 4.0 (1 projects)

### Auralix.ai
*Hack4Bengal Hack4Bengal 4.0 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Runner-Up [3rd]

**What it is:** An async team assistant: it records meetings (tab plus microphone via Chrome extension, or file upload), transcribes with Whisper, summarizes with Gemini, creates Notion tasks and posts summaries to Slack. A scheduler also summarizes each member's GitHub and Notion activity daily.
**Problem / user:** Distributed product and engineering teams whose meeting decisions and progress are scattered across audio, Notion and GitHub.

**Features**
- Dual audio capture — Chrome extension (tabCapture) plus mic, or web-app file upload. *[shown_working]*
- Transcribe and summarize — Whisper transcription followed by Gemini analysis and summary. *[shown_working]*
- Notion task creation — Action items become Notion tasks with assignees and due dates. *[shown_working]*
- Slack posting — Instant meeting summaries and daily reports to Slack via webhook. *[shown_working]*
- GitHub commit tracking — Commits are matched to tasks to update status automatically. *[claimed]*
- Daily progress aggregator — Scheduler pulls GitHub and Notion activity and Gemini writes per-member standup summaries. *[claimed]*

**Flow:** Record a meeting from the extension or upload audio → Whisper transcribes and Gemini summarizes → Action items sync to Notion → Summary posts to Slack → Daily job posts per-member progress updates

**Prompt:** not public / not found
**Fit (explicit):** Devfolio page says it applied to the Gemini API track and uses Gemini for summaries and progress reports; track text itself was not found.  *(targeted: Best use of Gemini API (MLH, applied), Second Runner-Up (overall))*
**Sponsor tools:** Gemini API (Meeting summaries, action items and per-member progress summaries, core); Whisper (Speech-to-text, core)
**AI:** Whisper for transcription; Gemini for summarization, action-item extraction and daily progress writing from GitHub/Notion data.
**Architecture:** Chrome extension and web app send audio to a Flask backend (Flask-APScheduler); Whisper then Gemini; outputs go to Notion, Slack and GitHub integrations.
**Novelty:** Joins meeting audio with repository and task-board activity in one async standup flow.
**Scope:** medium · working: Demo video linked; README describes features and architecture; ~3.9k LOC with backend, extension and web app. · polish: ASCII architecture diagram and CI present; no metrics.
**Gaps:** Official Gemini track text not found; Hack4Bengal page lists tracks and sponsors only; Placing is overall Second Runner-Up; track win not confirmed
Sources: https://devfolio.co/projects/auralixai-d1ba, evidence/hack4bengal-hack4bengal-4-0-auralix-ai.json, https://hack4bengal-4.devfolio.co/

---

