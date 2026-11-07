# HackSheffield — hackSheffield 9 (4 projects)

### A Helping Hand
*HackSheffield hackSheffield 9 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place Hack [1st]

**What it is:** A camera-based physiotherapy game for children recovering from hand and wrist injuries: MediaPipe tracks the hand and the user earns points for performing set hand positions in a space-themed game with music.
**Problem / user:** Children with hand or wrist injuries for whom physiotherapy is dull and frequent appointments cost families time and money.

**Features**
- Gesture recognition — MediaPipe pre-trained hand tracking via a laptop or phone camera detects exercise poses. *[shown_working]*
- Beginner mode — Low-range-of-motion exercise such as opening and closing the palm. *[claimed]*
- Random mode — Shows one of seven set hand positions for users with more movement. *[claimed]*
- Points for correct movement — Points awarded only once an exercise is performed correctly. *[claimed]*
- Game presentation — On-screen next-exercise prompt, background music and space-themed astronaut visuals in an OpenCV UI. *[claimed]*
- Family minigame — Competitive family play is mentioned as a possible expansion. *[planned]*

**Flow:** Launch the program with the camera on → Choose Beginner or Random mode → Read the on-screen exercise prompt → Perform the gesture → Earn points and move to next exercise

**Prompt:** First Place Hack at hackSheffield 9: the event's top overall prize (Nintendo Switch Lite); no explicit theme listed, though one project cites Growth.
**Fit (none):** Overall prize with no specific brief; the project fits a growth/recovery reading but states no link.  *(targeted: First Place Hack)*
**AI:** Pre-trained MediaPipe hand-landmark model for gesture detection; no custom training.
**Architecture:** Single Python app: OpenCV capture and UI, MediaPipe gesture logic, playsound for music; model file and images bundled.
**Novelty:** Turns a rehabilitation routine into a camera game; fell back from a MotionLeap sensor and Streamlit to OpenCV.
**Scope:** tiny · working: Small repo of 17 files, about 290 LOC; Devpost says a working two-mode game with scoring; one screenshot. · polish: Themed visuals and music; no clinical validation, tests or video.
**Claims:** Reduces cost and effort for families without compromising impact (unsupported)
**Gaps:** Repo requirements list streamlit packages though UI moved to OpenCV; No video or demo
Sources: https://devpost.com/software/a-helping-hand-7v9h46, https://github.com/technologeve/a_helping_hand (evidence README), https://hs9.devpost.com/

---

### Explainatron - 3000
*HackSheffield hackSheffield 9 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Place Hack [3rd]; [MLH] Best Use of Streamlit

**What it is:** A mobile-friendly Streamlit learning tool: the user names a topic, the AI asks clarifying questions and builds clickable diagrams of its parts, and a second path converts a photo of handwritten maths into LaTeX and a PDF with a short explanation.
**Problem / user:** Students left confused by lecture slides or whiteboard maths who want an interactive explainer.

**Features**
- Clarifying-question topic flow — The AI asks the user what they want to learn before explaining. *[claimed]*
- Interactive component diagrams — Diagrams show key parts of a topic; clicking a part gives a deeper breakdown such as TCP/IP layers. *[shown_working]*
- Q and A assistant — Chat helps clarify a topic or diagram. *[claimed]*
- Handwritten maths to LaTeX and PDF — Vision model reads whiteboard or handwritten maths and outputs typeset LaTeX, a PDF and a short explanation. *[claimed]*
- Maths topic diagrams — Recognised maths topics (e.g. calculus) can be broken into interactive diagrams. *[claimed]*
- Mobile-compatible uploads — Full Streamlit site works on mobile with file upload. *[claimed]*

**Flow:** Enter a topic or upload a maths photo → Answer clarifying questions → View the interactive diagram → Click components for detail → Ask follow-up questions or download the PDF

**Prompt:** MLH Best Use of Streamlit: hack with Streamlit for a chance to win an Arduino Tiny ML Kit per team member; Streamlit is an open-source Python web-app library. Also Third Place Hack (Echo Dot).
**Fit (explicit):** The whole app is built in Streamlit for UI, diagrams and uploads; team chose it to simplify full-stack and mobile integration.  *(targeted: Third Place Hack, MLH Best Use of Streamlit)*
**Sponsor tools:** Streamlit (MLH) (Entire front end and app hosting on streamlit.app, core)
**AI:** OpenAI GPT-4 and GPT-4o for explanations and vision, DALL-E for images, chain-of-thought and one-shot prompting for LaTeX/PDF; Llama and Databricks prototypes dropped.
**Architecture:** Streamlit Python app with OpenAI calls, streamlit-agraph and d3-dagre diagram components, plus a separate React homepage folder.
**Novelty:** Combines concept-to-diagram exploration and handwritten-maths-to-LaTeX in one tool.
**Scope:** small · working: Deployed streamlit.app demo and slide deck linked; 67 files with tests present. · polish: Has a separate React homepage; no usage metrics; open-source goal not met since it needs OpenAI.
**Claims:** Aims to be an open-source classroom learning tool (still depends on OpenAI)
**Gaps:** README only shows setup commands; Live demo and slides not opened; Screenshot count not captured
Sources: https://devpost.com/software/storyboard-es0q7p, https://github.com/shahar-dagan/HackSheffield2024 (evidence README), https://hs9.devpost.com/

---

### GrowthPath
*HackSheffield hackSheffield 9 · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [CompSoc] First Time Hack

**What it is:** A Flask web app of AI helpers for students with learning differences: speech-to-text for dysgraphia, a read-aloud and simplifying tool for dyslexia, a handwriting-to-text tool for dyspraxia, and an idiom translator for autism, plus a general AI chat.
**Problem / user:** Students with dysgraphia, dyslexia, dyspraxia or autism facing barriers in education; offered to all students.

**Features**
- Thoughts into Words — Speech-to-text turns spoken ideas into written text with simplified prompts. *[claimed]*
- Reading Buddy — Text-to-speech reads text aloud and offers simplified text versions. *[claimed]*
- Handwriting Interpreter — Converts handwritten notes into digital text. *[claimed]*
- Literal Lens — Rewrites idioms and slang into literal language. *[claimed]*
- General AI Chat — General assistant for information and ideas. *[claimed]*
- Disability-based home page — Home page lets users pick a disability and see each tool's description. *[shown_working]*
- Parent and child accounts — Accounts, progress tracking and history are future work. *[planned]*

**Flow:** Open the home page → Select a learning disability → Read the matching tool description → Use the tool (speak, upload, read or chat) → Receive converted or simplified output

**Prompt:** [CompSoc] First Time Hack at hackSheffield 9: a prize for first-time hackers; the Devpost prize list gives no further description.
**Fit (implied):** Team was new to front-end development and built a working multi-tool app in the event; no further stated link.  *(targeted: [CompSoc] First Time Hack)*
**AI:** Gemini LLM via google-generativeai for simplification, idiom translation and chat; Whisper and Google Web Speech for speech input; pyttsx3 text-to-speech.
**Architecture:** Flask backend with controllers and Jinja templates, MongoDB via PyMongo, ffmpeg audio handling, HTML/CSS/JS front end.
**Novelty:** Maps each tool to a specific learning difference and offers them in one app.
**Scope:** small · working: 26 files, about 1.6k LOC, six screenshots of tool pages; no live demo. · polish: Kid-friendly interface claimed; no testing with users; README is setup only.
**Claims:** Fast LLM responses so users do not wait
**Gaps:** README is setup-only; Which tools actually work end to end not shown
Sources: https://devpost.com/software/growthpath, https://github.com/Shawarm0/HackSheffield9-Project (evidence README), https://hs9.devpost.com/

---

### Where is the SOIL
*HackSheffield hackSheffield 9 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Place Hack [2nd]

**What it is:** A browser simulation in HTML, CSS and JavaScript of potato sprouts growing roots toward moisture in a randomly generated Perlin-noise soil map, inspired by a Portal 2 easter egg, with a sandbox mode to tweak parameters.
**Problem / user:** No explicit user or problem; viewers who enjoy a growth simulation, with future ideas for growers choosing breeds and planting placement.

**Features**
- Hydrotropic root growth — Sprouts and roots grow toward higher moisture in the environment. *[shown_working]*
- Random moisture map — Perlin noise forms a topographic moisture map where peaks are 100 percent and troughs 0 percent. *[claimed]*
- Sandbox mode — Users change logic, parameters or scenarios. *[claimed]*
- Runs in browser — Hosted demo on GitHub Pages needs no download. *[shown_working]*

**Flow:** Open the demo link → Watch roots search the soil for moisture → Adjust sandbox parameters

**Prompt:** Second Place Hack at hackSheffield 9 (NordVPN package); the team says its entry fits the event's Growth theme, which the Devpost page itself does not state.
**Fit (implied):** Team ties potato growth to a Growth theme; no official prompt text confirmed.  *(targeted: Second Place Hack)*
**AI:** none
**Architecture:** Client-side JavaScript simulation with Perlin-noise environment on a canvas, served statically from GitHub Pages.
**Novelty:** Playful biological simulation with no AI yet; rapid algorithm prototyping chose the most realistic root behaviour.
**Scope:** tiny · working: Live GitHub Pages demo linked; repo not linked on page. · polish: Described as satisfying to watch; no metrics, screenshots or video.
**Gaps:** No repo linked; Demo page not opened; Theme not on the official page
Sources: https://devpost.com/software/where-is-the-soil, https://hs9.devpost.com/

---

