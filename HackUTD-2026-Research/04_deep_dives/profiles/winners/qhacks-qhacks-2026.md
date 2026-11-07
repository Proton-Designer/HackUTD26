# QHacks — QHacks 2026 (3 projects)

### Atlas
*QHacks QHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place [2nd]

**What it is:** Voice-driven time-travel explorer: pick a place and year on a 3D globe or by talking to an AI guide, then arrive in a World Labs generated 3D scene rendered as Gaussian splats while the guide explains the history.
**Problem / user:** People who read about history but cannot feel what a place and era were like.

**Features**
- Interactive globe with infinite zoom — Select country, city or coordinates and a year. *[shown_working]*
- Interruptible voice conversation — Gradium speech-to-text and text-to-speech with barge-in, driving Gemini replies. *[claimed]*
- Gemini tool calling — Tools suggest globe locations, pick era-aware music and trigger world creation. *[claimed]*
- Hyperspace transition — Starfield warp with music matched to time and culture while the world generates. *[claimed]*
- Generated 3D world — World Labs API produces a scene for the coordinates and year, rendered with Spark.js and Three.js splats. *[claimed]*
- In-world guide — Guide interprets what the user sees and gives historical context. *[claimed]*
- Context-aware loading narration — Messages during generation depend on the chosen time and place. *[claimed]*

**Flow:** Landing page with starfield and globe → Choose place and year by clicking or speaking → Hyperspace warp with era music and narration → Arrive in generated 3D world → Explore while the guide narrates

**Prompt:** QHacks 2026 main placements (second place MSI monitor); Gradium sponsor track offered cash and credits; criteria include theme alignment beyond basic LLM use.
**Fit (implied):** No stated prize targeting; Gradium voice API is core to the experience, but the page does not claim the Gradium track.  *(targeted: Second Place [2nd])*
**Sponsor tools:** Gradium (speech-to-text and text-to-speech for the voice guide, core); Gemini API (guide behavior and tool calling, core); World Labs API (3D world generation, core)
**AI:** Gemini drives the guide with tool calls (globe, music, generation); World Labs generates splat worlds from location/year/interest prompts; Gradium handles voice.
**Architecture:** React/Vite/Three.js/Spark.js frontend with react-globe.gl; FastAPI WebSocket backend relays Gradium audio and Gemini responses and calls World Labs.
**Novelty:** Combines conversational agent, globe selection and generative Gaussian-splat worlds in one flow with interruptible voice.
**Scope:** medium · working: Demo video, about 8k-line repo with backend tests and docs folder; splat artifacts still being fixed. · polish: Hyperspace transition, tailored music and narration; env example and docs present.
**Claims:** Interruptible low-latency voice with no redirect out of app
**Gaps:** README is only a video link and placement line; docs/ folder not read; No metrics; Whether Gradium track was entered is unstated
Sources: https://devpost.com/software/atlas-m8yot1, https://github.com/MatthewLones/QHacks-2026, evidence/qhacks-qhacks-2026-atlas.json, https://qhacks-2026.devpost.com/

---

### Orca
*QHacks QHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** First Place [1st]

**What it is:** Voice-to-MIDI composer: record humming, singing or beatboxing (optionally with spoken instructions), a multi-stage pipeline converts it to multi-track MIDI shown in a piano-roll editor, and further voice instructions edit the result through tool calls.
**Problem / user:** Musically inclined people without instruments or production skills who want to turn a hummed idea into real music.

**Features**
- Voice recording or upload — Accepts MP3/WebM of singing, humming or beatboxing in the browser. *[shown_working]*
- Five-stage audio-to-MIDI pipeline — BasicPitch notes, Gemini segment classification and chords, score builder, instrument mapper, MIDI merger. *[shown_working]*
- Piano-roll editor — Next.js UI with per-track mute/visibility and soundfont playback via Tone.js. *[shown_working]*
- Spoken-instruction editing — Voice commands trigger tool calls such as change_pitch and change_scale on a track. *[shown_working]*
- Segment classification — Separates speech from humming, singing, beatboxing and silence so each routes to a different MIDI strategy. *[shown_working]*
- Instrument assignment — Singing and humming go to piano/flute, beatboxing to drums. *[shown_working]*
- Agentic rhythm editor — Devpost says a Gemini agent picks tools such as instrument assignment from the instructions. *[claimed]*
- Marketplace and collaboration — Community marketplace and real-time collaborative editing are future work. *[planned]*

**Flow:** Record or upload a voice clip → Backend job runs the pipeline and the page polls status → Piano roll loads the MIDI → Toggle tracks and play back → Record a voice instruction to change pitch or scale

**Prompt:** QHacks 2026 main placements (first place Sony headphones); criteria include Theme Alignment, going beyond basic LLM use and showing understanding of AI concepts.
**Fit (implied):** No stated prize targeting; multi-stage audio pipeline plus a tool-calling agent fits the theme criterion of going beyond a basic LLM wrapper, but this is an inference.  *(targeted: First Place [1st])*
**Sponsor tools:** Gemini API (audio segmentation/classification, chord generation, tool-calling agent, core); ElevenLabs (speech-to-text of spoken instructions (per Devpost), supporting)
**AI:** Gemini classifies audio segments, writes chords and acts as a tool-calling agent; BasicPitch extracts notes; MusicLang generates sparse parts; Devpost also cites a custom segmentation model.
**Architecture:** Next.js/Zustand/Tone.js frontend polls a FastAPI backend; upload router starts a job running the five pipeline stages and exposes MIDI and instruction endpoints.
**Novelty:** Mixes spoken commands and music in one recording and edits MIDI through deterministic tool calls instead of letting an LLM edit audio.
**Scope:** medium · working: Detailed README with pipeline and API; backend tests exist; Vimeo demo on Devpost. · polish: Piano-roll UI and structured README; no screenshots counted.
**Claims:** Agentic tool approach 'eliminates most hallucinations' (qualitative) | Backtrack output is usable
**Gaps:** README uses MusicLang for sparse/percussive parts; Devpost says MusicLang backtracks were dropped; README names Gemini for segmentation; Devpost describes a custom ML segmenter and ElevenLabs transcription; Screenshot count not captured
Sources: https://devpost.com/software/orca-4po0nm, https://github.com/Beebdoles/qhacks-2026, evidence/qhacks-qhacks-2026-orca.json, https://qhacks-2026.devpost.com/

---

### Willow
*QHacks QHacks 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Place [3rd]

**What it is:** Voice-controlled assistant for disabled and elderly users that lets them operate the web by speaking commands, delivered as a Windows app launched from a LILYGO ESP32 USB stick that installs it.
**Problem / user:** Seniors and people with arthritis, cerebral palsy or low vision who struggle with keyboards and mice when browsing, shopping, searching or getting directions.

**Features**
- Conversational voice commands — Spoken requests such as playing jazz or looking up a recipe are interpreted by a custom agent. *[shown_working]*
- Browser automation — Dynamic Playwright tools carry out the request (Devpost shows it operating Google Maps). *[shown_working]*
- ElevenLabs voice in and out — Speech transcription and a calm George-voice narration. *[claimed]*
- USB-stick installer — LILYGO stick types a command that builds and runs the project, then can be removed. *[claimed]*
- Picture-in-picture window — Small always-visible window across tabs with a mute button, startup muted. *[claimed]*
- Accessible desktop GUI — Vanilla HTML/CSS/JS hosted via Eel with large readable theme. *[shown_working]*
- Local-first privacy stance — README says it runs locally, collects nothing and can be muted. *[claimed]*
- High-contrast UI and screen-reader integration — Listed as next steps. *[planned]*

**Flow:** Plug in the USB stick → Stick installs and launches Willow → Mini window appears with mic muted → Unmute and speak a request → Agent drives the browser to do it

**Prompt:** QHacks 2026 main placements (third place JBL Go 4 speaker); criteria include design and UX plus innovation and social impact.
**Fit (implied):** No stated prize targeting; accessibility-focused voice assistant with hardware installer meets the social impact criterion, by inference.  *(targeted: Third Place [3rd])*
**Sponsor tools:** ElevenLabs (speech-to-text and narration voice, core)
**AI:** Custom Python agent using OpenAI plus ElevenLabs transcription turns speech into tool calls; Playwright executes browser actions.
**Architecture:** LILYGO ESP32 stick with C++ script bootstraps a PyInstaller-built Python app; Eel serves a vanilla web GUI; agent calls Playwright tools.
**Novelty:** Hardware USB stick as zero-setup installer for non-technical users, paired with an agent that drives the real browser.
**Scope:** medium · working: Demo video and Google Maps screenshots; repo of about 3k lines with Arduino code and web UI. · polish: Themed GUI, packaged exe, README with ethics section; README breaks off before limitations.
**Claims:** Went from no ESP32 experience to a working program | Runs a 0.5 GB script past Windows antivirus (self-reported)
**Gaps:** README says no data leaves the computer while Devpost lists OpenAI and ElevenLabs cloud calls; Devpost mentions pywebview but README and challenges say Eel; README text truncated at limitations section
Sources: https://devpost.com/software/willow-8f5wqn, https://github.com/regularpooria/willow_qhacks2026, evidence/qhacks-qhacks-2026-willow.json, https://qhacks-2026.devpost.com/

---

