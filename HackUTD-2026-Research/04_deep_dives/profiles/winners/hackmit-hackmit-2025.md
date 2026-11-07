# HackMIT — HackMIT 2025 (3 projects)

### EyeCraft
*HackMIT HackMIT 2025 · dataset: winners · tier: track_winner · evidence C · confidence low*
**Prizes:** First place, entertainment track [1st]

**What it is:** A Minecraft accessibility mod that maps face and head gestures to game controls for players with limited hand mobility, built by four university students at HackMIT 2025. Reported gestures include opening the mouth to move forward, looking up to tilt the view, and a right-eye wink to jump.
**Problem / user:** Players with limited hand movement or mobility who cannot use a standard keyboard and mouse for Minecraft.

**Features**
- Mouth-open to walk — Facial recognition maps mouth opening to forward movement *[claimed]*
- Look-up to tilt view — Head direction controls camera *[claimed]*
- Wink to jump — Right-eye wink triggers jump *[claimed]*
- Voice commands — Our earlier brief says voice commands are also mapped *[claimed]*

**Flow:** Player starts the mod with a webcam → Facial gestures drive character movement and camera

**Prompt:** not public / not found
**Fit (implied):** Makes a popular game playable hands-free for players with mobility limits.  *(targeted: Entertainment track (1st))*
**AI:** Webcam facial/gesture recognition (model not named in the source).
**Architecture:** 
**Novelty:** Accessibility-focused gesture control layered onto an existing game.
**Scope:** small · working: News article describes working gesture controls; no repo or demo found. · polish: Unknown.
**Gaps:** No project page or repo located; Tech stack unknown; Winks and voice detail from prior brief only
Sources: https://www.khoury.northeastern.edu/khoury-undergrads-win-three-categories-at-prestigious-mit-hackathon

---

### Griddy
*HackMIT HackMIT 2025 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** First place, sustainability track (novelty prize check) [1st]; First place, sustainability track [1st]

**What it is:** A power-grid orchestration demo: an ESP32 model grid with LED and motor loads, a 24 Hz mixed-integer routing algorithm with FFT demand prediction, a Cerebras-hosted fallback agent, and a Next.js metrics dashboard. The team also made iron-air batteries.
**Problem / user:** Grid operators and infrastructure developers who need more efficient routing and local storage independent of rare-earth supply chains.

**Features**
- Grid routing algorithm — Mixed-integer linear programming routes supply to consumers each tick *[claimed]*
- Demand prediction — FFT predicts each consumer's next-tick demand; runs at 24 Hz *[claimed]*
- Hardware grid model — ESP32 with LED and motor consumers fed modulated sine demand; WebSocket server streams JSON at 24 Hz *[shown_working]*
- Cerebras fallback agent — Agent takes over when algorithm confidence is low *[claimed]*
- Metrics dashboard — Next.js visualizations over a WebSocket backend *[claimed]*
- Iron-air battery — Home-built cell powering an LED for hours as local storage *[claimed]*

**Flow:** Dashboard connects to grid WebSocket → Nodes report demand → Algorithm assigns supply sources → Dashboard visualizes routing and metrics → Agent intervenes on low confidence

**Prompt:** not public / not found
**Fit (explicit):** Frames the project as energy-grid efficiency and independence; Cerebras agent used as emergency controller.  *(targeted: Sustainability track, Cerebras: Best Use of the Cerebras API, Infosys: Carbon-conscious intelligence)*
**Sponsor tools:** Cerebras API (Agent taking control in low-confidence situations, supporting)
**AI:** Mostly classical optimization (MILP, FFT); an LLM agent on Cerebras acts as fallback controller.
**Architecture:** ESP32 grid model serves readings over WebSocket; backend runs optimizer and sends supply commands; Next.js dashboard visualizes.
**Novelty:** Pairs software optimization with physical grid model and homemade iron-air batteries using fertilizer chemistry.
**Scope:** medium · working: Hardware circuit and WebSocket protocol documented in repo; battery ran an LED for hours per writeup. · polish: Dashboard with visualizations; 14k LOC repo, README covers only hardware API.
**Claims:** Outperforms US grid routing and known private solar grids | Algorithm sped from 2 Hz to 24 Hz | Battery powered an LED about 4 hours
**Gaps:** Sponsor/track challenge text not found; superiority claims unverified
Sources: https://plume.hackmit.org/project/kmips-kavlf-auvtc-ymtmn, https://github.com/Tetraslam/hackmit25 (evidence file)

---

### Kava
*HackMIT HackMIT 2025 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First place, EigenCloud Sponsor Prize Side Track [1st]; HackMIT EigenCloud Sponsor Prize Side Track (first place) [1st]

**What it is:** An AI claims agent for wildfire victims: users upload documents, an AI judge scores them against a 47-rule constitution, an enhancement loop fixes gaps and fetches missing receipts, and a claim packet PDF with signed proof card is produced.
**Problem / user:** Wildfire-affected renters and homeowners whose insurance claims get rejected for missing or messy documentation.

**Features**
- Document upload and OCR — Letters, receipts, photos are OCR'd, low-confidence scans reprocessed *[claimed]*
- AI Judge — Scores claim against 47 weighted rules with fraud and completeness checks, Claude-backed *[claimed]*
- Agentic improvement loop — Re-runs judge while adding docs and fixes; scores reported rising from 42% to 85%+ *[claimed]*
- Receipt fetching — Knot TransactionLink retrieves missing receipts *[claimed]*
- Claim packet PDF — Packet with proof card and trust badge, ECDSA-signed *[claimed]*
- TEE attestation — EigenCloud TEE service attests the evaluation *[claimed]*

**Flow:** Upload documents → Judge scores and lists missing items → Agent auto-fixes and fetches receipts → Re-score until threshold → Download claim packet with proof card

**Prompt:** not public / not found
**Fit (explicit):** Builds a domain-specific AI judge with a rule set, runs attestation in an EigenCloud TEE, uses Knot for receipts and Claude for evaluation.  *(targeted: EigenCloud Sponsor Prize Side Track (1st), EigenCloud Challenge #1: domain-specific AI judge, Knot, Anthropic: Best use of Claude, Fetch.ai)*
**Sponsor tools:** EigenCloud TEE (Tamper-proof attestation of judge result, core); Knot TransactionLink (Fetch missing receipts, supporting); Claude (AI judge reasoning, core)
**AI:** LLM judge applying a rules constitution plus OCR and vision; an enhancement agent loops on judge feedback without altering original user data.
**Architecture:** Next.js frontend, FastAPI backend with Claude and OCR, EigenCloud TEE service for signing, Docker setup.
**Novelty:** Judge-and-improve loop with cryptographic proof card, targeted at a concrete disaster-claims workflow.
**Scope:** medium · working: README with architecture, sample test claims, Docker; demo video linked on Plume. · polish: Step wizard UI, proof cards, packet PDF.
**Claims:** Scores improve from 42% to 85%+ through the loop | 47-rule constitution | Production-ready (README)
**Gaps:** Official sponsor challenge text not found
Sources: https://plume.hackmit.org/project/acarj-euukc-rblna-lfviq, https://github.com/arav06/kava-hackmit (evidence file)

---

