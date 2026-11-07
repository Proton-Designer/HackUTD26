# UofTHacks — UofTHacks (2 projects)

### FurMe
*UofTHacks UofTHacks · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Overall UofTHacks First Place [1st]

**What it is:** A Furby-inspired animatronic desk companion whose servos track the user's face, which talks with speech-to-text and text-to-speech, tells jokes, detects mood from facial expression to play matching Spotify songs, and is managed from a web dashboard with a chatbot and camera view.
**Problem / user:** No explicit problem: built around 2000s nostalgia for Furby toys as a desk assistant for someone wanting a companion with music, chat and home monitoring.

**Features**
- Face-following animatronic body — Servos driven by microcontroller track the user's face using a camera *[claimed]*
- Emotion-based music — Facial expression detection chooses mood-appropriate songs such as childhood favorites via Spotify *[claimed]*
- Voice conversation and jokes — Google speech-to-text and text-to-speech with ChatGPT-generated replies *[claimed]*
- Web dashboard — Login page and dashboard to control and monitor the Furby *[shown_working]*
- Dashboard chatbot — Cohere-powered assistant handles tasks from the dashboard *[claimed]*
- Surveillance camera view — Live camera feed shown on the dashboard for home security *[shown_working]*
- Calendar, daily overview, Pomodoro and phone detection — Listed as next steps *[planned]*

**Flow:** Log in to the dashboard → Control and monitor the Furby → View the camera feed → Talk to the Furby and watch it track the face → Music plays matched to detected mood

**Prompt:** UofTHacks 11 overall prizes ranked by the criteria Theme, Technology, Design, Completion and Learning; the event had sponsor challenges with their own themes and a Cohere prize, with no single overall theme on the main page.
**Fit (implied):** Devpost frames the project around Furby nostalgia and highlights hardware plus software integration; Cohere is used for the dashboard chatbot.  *(targeted: Overall UofTHacks First Place)*
**Sponsor tools:** Cohere (dashboard chatbot (cohere-ai in client dependencies), supporting); Agora RTC (listed in tags and client deps, likely video streaming of the camera view; role not explained, unclear)
**AI:** Facial emotion detection (model unnamed), ChatGPT for jokes and conversation, Cohere for the dashboard chatbot, Google speech-to-text and text-to-speech.
**Architecture:** Physical Furby with Arduino/microcontroller, servos, camera and speaker; Python server (large) and React client with Google OAuth, Agora RTC and Cohere SDK; Spotify API.
**Novelty:** A physical animatronic toy rebuilt as an AI desk assistant spanning mechanics, vision, voice, music and security camera in one weekend project.
**Scope:** large · working: Repo has client and server folders with tests, but the file count is inflated by a bundled environment; no demo link or video on Devpost. · polish: Screenshots show hardware internals and dashboard; repo has no README.
**Claims:** Won first place overall at UofTHacks 11 | No quantitative metrics
**Gaps:** repo has no README (evidence is tree and manifests only); no video; screenshot count not captured; Devpost lists Python server while 'Cohere' vs 'ChatGPT' roles from page only
Sources: https://devpost.com/software/furme, evidence/uofthacks-uofthacks-furme.json, https://uofthacks-11.devpost.com/

---

### wayback
*UofTHacks UofTHacks · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Overall UofTHacks Third Place [3rd]

**What it is:** A Figma plugin that parses a frame containing a rough component sketch and emits matching UI code, with a Next.js demo site that renders the output in Windows XP, Windows 7 and modern themes.
**Problem / user:** Building retro-styled UI components is slow; implied users are developers turning Figma prototypes into code.

**Features**
- Figma frame to code — Plugin walks the node tree from the root like a compiler and outputs JSX/HTML for the frame *[shown_working]*
- Element detection — Recognizes buttons, text inputs, text elements and pictures *[claimed]*
- Cohere Classify label semantics — Node properties turned into English sentences and fine-tuned on examples such as destructive buttons *[claimed]*
- Spacing-based grouping — Greedy algorithm groups children into containers by spacing within a tolerance *[claimed]*
- Alignment inference — Computes main-axis and cross-axis alignment for grouped children *[claimed]*
- Themed demo site — Next.js app shows generated components as Windows XP, Windows 7 or modern web *[shown_working]*
- Forms and auto state hooks — Listed as next steps *[planned]*

**Flow:** Sketch a rough component in a Figma frame → Run the plugin → Plugin parses nodes and outputs code → View the component in the demo site themes

**Prompt:** UofTHacks 11 overall prizes ranked on Theme, Technology, Design, Completion and Learning; sponsor challenges (including Cohere) had their own themes; no single overall theme on the main page.
**Fit (implied):** Devpost says the original idea was a themed time-travel through internet history, narrowed to retro-styled components; Cohere Classify is used for semantics.  *(targeted: Overall UofTHacks Third Place, Best Build with Cohere)*
**Sponsor tools:** Cohere Classify (semantic classification of element labels from node properties, core)
**AI:** Fine-tuned Cohere Classify model on node properties rendered as sentences for label semantics; geometry handled by deterministic algorithms.
**Architecture:** Figma plugin (TypeScript) traverses the design tree, classifies nodes, groups by spacing and generates code; separate Next.js frontend demonstrates themed components.
**Novelty:** Compiler-style tree conversion from design to code with a hybrid of ML for semantics and deterministic layout logic.
**Scope:** small · working: 83-file repo with plugin and demo frontend, about 3.3k LOC; no video or live demo listed. · polish: README is two lines; Devpost explains algorithms; no tests.
**Claims:** No quantitative metrics | Team says it is useful in their own daily work
**Gaps:** Devpost lists placement as both 'Winner Overall' and 'Third Place'; Devpost says JSX and html both for output; repo is named uofthacks-2023 while page says UofTHacks 11
Sources: https://devpost.com/software/wayback-7g1x2s, evidence/uofthacks-uofthacks-wayback.json, https://uofthacks-11.devpost.com/

---

