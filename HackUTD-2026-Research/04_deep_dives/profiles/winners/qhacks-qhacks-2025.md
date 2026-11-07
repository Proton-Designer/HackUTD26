# QHacks — QHacks 2025 (3 projects)

### LUNA
*QHacks QHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place: PS5 Slim Digital [1st]; Nord Security Bundle

**What it is:** Wearable assistive device: a camera on an ESP32-S3 clipped to glasses photographs the scene, a backend asks Claude to describe it, converts text to speech and plays it on the device for blind users.
**Problem / user:** Blind and low-vision people who need real-time spoken descriptions of their surroundings.

**Features**
- Scene narration — ESP32-S3 camera posts an image to the backend, Claude 3.5 Sonnet describes it, audio plays on the device. *[claimed]*
- OCR of text in scene — Uses Claude's vision for reading text, chosen for strong OCR. *[claimed]*
- Cloud text-to-speech — Google Cloud TTS returns audio fetched by the device and played through a speaker via I2S DAC. *[claimed]*
- Clip-on 3D-printed enclosure — CAD-designed compact housing mounts to eyewear. *[claimed]*
- Haptic feedback — Multi-threaded embedded software drives haptics; role not detailed. *[claimed]*
- Deep-sleep mode — Firmware sleeps between uses for longer runtime. *[claimed]*
- Descriptions only, no navigation — Deliberately limits scope to description, not safety or route advice, to avoid harm from model errors. *[claimed]*

**Flow:** Wear device on glasses → Camera captures a frame → Image is POSTed to Express server → Claude describes the scene, TTS makes audio → Device fetches and plays the audio

**Prompt:** QHacks 2025 top three (PS5 Slim for first) plus a Nord Security bundle for the top three; no sponsor challenge text. Criteria: implementation, design, pitch, innovation and social impact, optional AI theme.
**Fit (none):** No stated prize targeting; accessibility hardware with a working embedded-to-AI pipeline entered in the general top-three pool.  *(targeted: First Place: PS5 Slim Digital [1st], Nord Security Bundle)*
**AI:** Claude 3.5 Sonnet vision for scene description and OCR; Google Cloud Text-to-Speech for speech.
**Architecture:** Seeed Xiao ESP32-S3 Sense (C++/PlatformIO) sends images by HTTP to a Node/Express backend that calls Claude and Google TTS, then serves audio back to the device speaker.
**Novelty:** Complete hardware build (custom firmware, CAD enclosure, DAC audio) around off-the-shelf vision LLM, rare among web-heavy projects; later pursued as a startup.
**Scope:** medium · working: Hardware prototype photos on Devpost; repo with large skibidi folder and tests; README says later prototypes and Hult Prize pitch. · polish: Four photos, project website and README storyline; no demo video.
**Claims:** Won 1st place overall at QHacks 2025 (README) | Team selected for Hult Prize regional round after the hackathon (README) | Cites 1.1 billion people with vision loss
**Gaps:** README is startup-oriented and has no technical docs; No latency or accuracy measured; Repo includes later work beyond the hackathon prototype (React Native/BLE mentioned)
Sources: https://devpost.com/software/luna-nblywg, https://github.com/Valagit12/Qhacks2025, evidence/qhacks-qhacks-2025-luna.json, https://qhacks-2025.devpost.com/

---

### NextBid
*QHacks QHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Third Place: Keychron V1 Keyboard [3rd]; Nord Security Bundle

**What it is:** Auction marketplace web app with a Tinder-style swipe interface for buyers and photo-based listing for sellers, where GPT-4o names the item, rates condition and suggests a starting price.
**Problem / user:** Buyers and sellers who find conventional auction sites cluttered and slow.

**Features**
- Swipe-to-bid feed — Buyers swipe right to bid and left to skip items. *[claimed]*
- Photo-based listing — Seller photographs an item; OpenAI identifies and names it and fills condition and ideal price. *[claimed]*
- Recommendations — Swipe and favorite interactions are recorded to curate the next item shown. *[claimed]*
- Real-time bidding and notifications — Live updates and alerts when a seller's item sells. *[claimed]*
- Favorites and auction management — Users favorite, track and manage items. *[claimed]*
- Authentication — Clerk handles sign-in. *[claimed]*
- AI tag generation — OpenAI generates tags for items. *[claimed]*

**Flow:** Seller photographs an item → AI generates title, condition and price → Buyer swipes through listings → Right swipe places a bid → Seller gets a sale notification

**Prompt:** QHacks 2025 top three (Keychron V1 for third) plus Nord Security bundle for the top three; the NBC challenge offered a silent-auction website option but this page does not claim it.
**Fit (implied):** Page does not name a prize; the README thanks National Bank, and a silent auction site was one NBC challenge option, so a fit is implied but not stated.  *(targeted: Third Place: Keychron V1 Keyboard [3rd], Nord Security Bundle)*
**AI:** GPT-4o vision turns a photo into title, condition and price suggestion; README also mentions ML recommendation models from swipe data (implementation unconfirmed).
**Architecture:** Next.js/React/Tailwind app with Node server routes, Prisma over SQLite, Clerk auth, AWS S3 uploads and OpenAI calls.
**Novelty:** Applies swipe-card dating-app mechanics to auctions and automates seller listing from a photo.
**Scope:** small · working: Repo of about 1.2k lines with Prisma schema and upload code; screenshots show buyer and seller views; no live demo. · polish: Responsive UI with animation libraries, thumbnail and README screenshots.
**Claims:** Built in two days by four first-year students | Database moved from MySQL to SQLite to save time
**Gaps:** README says ML recommenders exist but code evidence not inspected; No setup instructions in README; Auction timer described as limited
Sources: https://devpost.com/software/next-bid, https://github.com/ela202/QHacksAuction, evidence/qhacks-qhacks-2025-nextbid.json, https://qhacks-2025.devpost.com/

---

### TLDR.AI
*QHacks QHacks 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place: Meta Quest 3S [2nd]; Nord Security Bundle

**What it is:** Chrome extension that detects terms-of-service links on sign-up pages, sends the text to a FastAPI backend where a Cohere model lists risky clauses with quotes, and shows them in a sidebar.
**Problem / user:** Anyone creating accounts who never reads privacy policies or user agreements.

**Features**
- Sign-up and TOS page detection — Extension checks URL and body text to spot account-creation pages and legal links. *[claimed]*
- TOS scraping — Fetches the legal agreement text and posts it to a REST API. *[claimed]*
- Risk summary — Model returns 3 to 5 dangers in plain language, each with a quoted passage. *[shown_working]*
- Fine-tuned Cohere model — Command R+ tuned on a synthetic fault dataset generated by Cohere and GPT-4o to cut hallucination. *[claimed]*
- RAG and structured output — Grounds answers in the document text and constrains replies to a JSON schema. *[claimed]*
- Sidebar UI with fire loading animation — Results appear in a sidebar; examples shown for AliExpress and Minecraft TOS. *[shown_working]*
- Caching database — Stores results for previously analysed documents. *[claimed]*

**Flow:** User opens a sign-up page → Extension finds the TOS link → TOS text sent to backend → Cohere analyses it → Sidebar lists risks with citations

**Prompt:** QHacks 2025 top three (Meta Quest 3S for second) plus Nord Security bundle for the top three; no separate track text. A privacy-themed bundle but no stated challenge.
**Fit (none):** No stated targeting; a consumer privacy/safety tool pairing naturally with the Nord bundle, but nothing explicit.  *(targeted: Second Place: Meta Quest 3S [2nd], Nord Security Bundle)*
**AI:** Cohere Command R+ fine-tuned on synthetic data from Cohere and GPT-4o, with a grounding system prompt, RAG and JSON structured output.
**Architecture:** Chrome extension front end (HTML/CSS/JS) posts scraped TOS to a FastAPI service that calls Cohere and a cache database, returning structured risks.
**Novelty:** Fine-tunes a model on synthetic data specifically for TOS red flags and quotes sources, beyond a plain summarizer prompt.
**Scope:** small · working: Devpost screenshots of AliExpress and Minecraft analyses and demo video; repo about 850 lines. · polish: Figma design, custom logo and loading animation; README short with no setup.
**Claims:** Uses 'every feature Cohere offers' | Fine-tuned model reduces hallucination (not measured)
**Gaps:** README says model is prompted (no mention of fine-tune); Devpost says fine-tuned; No metrics; Not published to Chrome Web Store
Sources: https://devpost.com/software/tldr-ai-amuh73, https://github.com/pooriaahmadi/qhacks2025, evidence/qhacks-qhacks-2025-tldr-ai.json, https://qhacks-2025.devpost.com/

---

