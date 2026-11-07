# HackPrinceton — HackPrinceton Fall 2025 (6 projects)

### doeve
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Exploring Hybrid Intelligence by Photon

**What it is:** A system that lets you control your Mac by texting or voice-noting it over iMessage. A bridge forwards messages to a backend where a vision-based agent operates the desktop, sending progress updates and screenshots back to the thread.
**Problem / user:** People away from their computer who want to open files, run scripts or push git commits hands-free by message.

**Features**
- iMessage text and voice command intake — Node bridge using the Photon iMessage SDK reads new messages and attachments and forwards them to a FastAPI backend. *[claimed]*
- Voice note transcription — ElevenLabs Scribe transcribes audio and the transcript replaces the message body; failures ask for text. *[claimed]*
- Vision-based computer use — Claude computer use sees screenshots, clicks, types and navigates apps and files. *[claimed]*
- Live progress and screenshots in chat — Updates and screenshots return to the iMessage thread; the user can add, change tasks or text stop. *[claimed]*
- Two orchestration modes — Native lightweight path or LangChain/LangGraph workflows with routing, retries and memory. *[claimed]*
- Job queue and sessions — Backend queues tasks, tracks sessions and streams WebSocket updates with structured logs. *[claimed]*

**Flow:** Send a text or voice note in iMessage → Bridge forwards message with sender and attachments → Audio is transcribed if present → Backend queues the task → Agent acts on the computer and posts updates and screenshots → User interrupts or sends stop → Result reported in the thread

**Prompt:** Photon-sponsored track on hybrid-intelligence agents; full text not retrieved. Photon's general challenge is agents reachable over iMessage and other messaging channels.
**Fit (explicit):** Page says it won this track; iMessage is the sole interface to an AI agent that acts on a computer, built on Photon's iMessage kit.  *(targeted: Exploring Hybrid Intelligence by Photon)*
**Sponsor tools:** Photon iMessage Kit (Reading Messages database events and delivering iMessage input to the backend, core); ElevenLabs Scribe (Voice note transcription, supporting)
**AI:** Claude vision computer use for screen understanding and control; LangChain/LangGraph for routing and retries; Gemini and OpenAI as alternatives; ElevenLabs Scribe for speech. pyautogui dropped for accuracy.
**Architecture:** Node/Express iMessage bridge calls a FastAPI backend with job queue and WebSockets; LangGraph agent drives Claude computer use on the host Mac and returns screenshots through the bridge.
**Novelty:** Chat-thread remote control of a full desktop with mid-task interruption, using voice notes as input.
**Scope:** medium · working: Devpost describes a working agent built in under 36 hours; repo could not be cloned for inspection; no video. · polish: Dataflow diagram and iMessage screenshot; no demo link.
**Claims:** Prototype built in under 36 hours
**Gaps:** Repo clone failed so no README; No video or demo; Claude model version as stated on page
Sources: https://devpost.com/software/do-eve

---

### edgecart.
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best Financial Hack by Capital One

**What it is:** A grocery waste system where shelf cameras score produce freshness, then discounts are pushed only to shoppers whose bank-linked purchase history shows they buy that item. Stores get a dashboard with reorder insights and food-bank donation scheduling.
**Problem / user:** Grocery stores losing money on expiring produce and shoppers missing relevant deals; random discounts come too late or too broad.

**Features**
- Camera freshness detection — YOLOv8 finds produce, ResNet18 scores freshness 0-100, Gemini Robotics counts blemishes. *[claimed]*
- Dynamic discounting — Discount is set from freshness drop with a 20 percent floor. *[claimed]*
- Purchase history via Knot — Customers connect accounts through Knot API to reveal what, how often and at what price they buy groceries. *[claimed]*
- Grok match scoring and notifications — xAI Grok scores timing, value perception and urgency; push sent only to matches scoring 80 or higher. *[claimed]*
- Store analytics and natural-language queries — Dashboard suggests reorder cuts and diagnoses weak offers; Grok answers questions for stores and customers. *[claimed]*
- Zero-waste fallback — Auto-schedules food bank donation 12 hours before critical decay and awards waste-warrior points. *[claimed]*
- Admin dashboard and customer portal — React apps with WebSocket real-time updates and AI reasoning panel. *[shown_working]*

**Flow:** Camera spots produce and freshness drops → Discount calculated → System finds customers who buy the item → Grok scores match and sends push notification → Customer buys the discounted item → Unsold items go to a food bank donation

**Prompt:** Best Financial Hack by Capital One, a prize inside the Business & Enterprise track, with no separate brief on the page.
**Fit (implied):** Page lists three prizes won; the finance link is recovered store revenue and shopper savings using Knot transaction data. No Capital One API is used.  *(targeted: Best Financial Hack by Capital One, YC x HackPrinceton Challenge, Build on the Knot TransactionLink API)*
**Sponsor tools:** Knot TransactionLink API (Customer purchase history across merchants, core)
**AI:** YOLOv8 detection, fine-tuned ResNet18 freshness classifier, Gemini Robotics blemish detection, and xAI Grok for matching, reasoning and natural-language queries with rate limiting.
**Architecture:** Cameras feed a Flask REST and WebSocket backend with SQLite; vision pipeline then Knot data then Grok scoring; React admin dashboard and customer portal receive live updates.
**Novelty:** Joins in-store computer vision with bank-linked shopper behavior to target markdowns per customer.
**Scope:** large · working: About 27k LOC repo with tests, live site edgecart.tech, and claimed 90 percent classifier accuracy on its own dataset. · polish: Detailed README with mermaid diagrams and 3D styled UI; no video.
**Claims:** 90 percent accuracy on the fresh/rotten dataset | Under 3 seconds from detection to notification | Projected 19.5 percent emissions reduction from a Markov model | 15 at-risk items matched to 8 customers in testing
**Gaps:** No video; Impact figures are projections; No privacy or consent discussion
Sources: https://devpost.com/software/edgecart, https://github.com/AntoDono/edgecart

---

### Messenger AI
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Exploring Hybrid Intelligence by Photon

**What it is:** An AI agent that reads a group chat's texts, PDFs and images through Photon's iMessage kit and answers questions or produces summaries and memes using that context. Sending replies into group chats was not yet supported by the kit.
**Problem / user:** Groups of friends, especially students cramming together, who want conversation-aware answers and summaries in their chat.

**Features**
- Conversation ingestion — Parses texts, PDFs and images from iMessage via Photon's iMessage kit into a context window. *[claimed]*
- Context-aware Q&A — Agent answers questions using what it has seen in the conversation. *[claimed]*
- Summaries and memes — Generates summaries, answers and memes for the chat. *[claimed]*
- Web-surfing agent — Dedalus Labs powered agent can browse the web. *[claimed]*
- Group-chat sending — Posting back into group threads depends on future kit support. *[planned]*

**Flow:** Start the agent → Agent reads the conversation and attachments → User asks a question → Agent answers from conversation context

**Prompt:** Photon-sponsored track on hybrid-intelligence agents; full text not retrieved. Photon's general challenge is agents reachable over iMessage and other messaging channels.
**Fit (implied):** Uses Photon's iMessage kit to put an agent into messaging context; page says it won this prize.  *(targeted: Exploring Hybrid Intelligence by Photon)*
**Sponsor tools:** Photon iMessage Kit (Reading texts and attachments and integrating the agent into chats, core); Dedalus Labs (Agent platform powering the AI, core)
**AI:** Dedalus Labs-hosted agent with a conversation-built context window and web browsing; no model named.
**Architecture:** Python/TypeScript service reads iMessage via Photon's kit, builds context, and calls a Dedalus agent; website at messengerai.tech.
**Novelty:** Group chat treated as agent context rather than a one-on-one bot; outbound group messaging unsolved at the time.
**Scope:** small · working: Demo video embedded and a demo website listed; no repo. · polish: Short Devpost writeup with video; implementation details sparse.
**Gaps:** No repo; Video not viewed; Model and architecture details absent
Sources: https://devpost.com/software/messenger-ai

---

### PiggyBank
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Exploring Hybrid Intelligence by Photon

**What it is:** PiggyBank (Piggy) is a spending coach that pulls item-level purchases into Snowflake, labels each as need or want, predicts when the user will next buy something habitual, and texts a nudge over iMessage beforehand. Users can also text receipt photos or chat about their spending.
**Problem / user:** Everyday spenders, especially younger consumers, whose small impulse purchases (coffee, delivery) add up without them noticing.

**Features**
- Item-level transaction ingestion and need/want classification — Knot TransactionLink data lands in Snowflake; Dedalus labels each purchase with a confidence score. *[claimed]*
- Predictive nudges before habitual purchases — Repeat-purchase intervals give a next-purchase time; Piggy iMessages a cheaper-alternative suggestion ahead of it (demo-mode scheduling). *[claimed]*
- Receipt scanning over iMessage — User texts a receipt photo; Gemini 2.5 Flash extracts structured data and Piggy confirms the saved total. *[shown_working]*
- Chat with spending history — GPT-4 agent with function calling queries Snowflake and answers questions like monthly coffee spend or how to save $50. *[shown_working]*
- Reaction-aware, multilingual coaching — Agent reads emoji reactions and replies in the user's language to refine later coaching. *[claimed]*
- React web dashboard — Clerk-authenticated pages for activity, insights, predicted purchases, deals, goals and a growing 'piggy' graph. *[shown_working]*

**Flow:** Sign up and link accounts through Knot; set a savings goal and connect a bank via Nessie → Transactions appear on the activity page → Piggy learns recurring purchases such as a daily coffee → An iMessage nudge arrives before the predicted purchase, tied to the savings goal → User replies or texts a receipt photo → User opens the dashboard or chats to ask about spending

**Prompt:** Photon-sponsored HackPrinceton Fall 2025 track on hybrid-intelligence agents; the public page lists only prize amounts (winner plus runner-up, Photon credits, interview fast-track) and no build brief.
**Fit (explicit):** The coach lives in iMessage via Photon's SDK, mixing LLM chat, receipt vision and a prediction model with live transaction data; the page claims nine targeted tracks.  *(targeted: Exploring Hybrid Intelligence by Photon, Knot TransactionLink API, MLH Best Use of DigitalOcean Gradient AI)*
**Sponsor tools:** Photon iMessage Kit (Delivers nudges, chat and receipt intake over iMessage, core); Capital One Nessie (Bank connection and goal setup, supporting)
**AI:** Dedalus classifies purchases; Gemini 2.5 Flash does receipt OCR; GPT-4 agent with function calling answers Snowflake-backed questions; Llama 3.1 on DigitalOcean Gradient plus a Snowflake time-series step predicts next purchase.
**Architecture:** React/Clerk dashboard, iMessage bot and terminal chat call a Node GPT-4 agent service, which calls a FastAPI backend (predictions, coaching, receipts); all data sits in Snowflake.
**Novelty:** Combines predictive pre-purchase nudging with receipt OCR and chat in one iMessage agent, and uses real production Knot item-level data rather than mock data alone.
**Scope:** medium · working: README gives setup, API endpoints and test data; page calls it a functional MVP; nudges run in demo mode only. · polish: Detailed README with architecture diagram, 19 screenshots, Clerk auth and multilingual support.
**Claims:** Won three HackPrinceton Fall 2025 tracks including Photon | Forecasts described as 'high accuracy' with no metrics | Cites 65% of Americans live paycheck to paycheck
**Gaps:** No demo video; Photon track brief text not published
Sources: https://devpost.com/software/tbd-9clz1k, https://github.com/HackPrincetonQANT/backend-frontned-agent-alltogether, https://hackprinceton-fall-2025.devpost.com/

---

### TextFly
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Exploring Hybrid Intelligence by Photon

**What it is:** TextFly (Flub) is a travel assistant reached by text message that answers flight and weather questions, and claims to predict delays from live X/Twitter signals. A Claude agent with Python flight-search tools sits behind an iMessage watcher.
**Problem / user:** Travelers facing flight disruptions who want answers by plain text without installing an app.

**Features**
- Text-message travel assistant — Photon iMessage watcher forwards texts to an HTTP agent server and returns the reply. *[claimed]*
- Flight search — Python tool function queries flight data (cheapest EWR to LAX style questions) via Claude function calling. *[shown_working]*
- Multi-turn conversation context — Agent keeps history so follow-ups like 'cheapest option?' work. *[shown_working]*
- Delay prediction from X/Twitter signals — Page says a social-media MCP feeds delay and cancellation prediction; not in the repo README. *[claimed]*
- Weather checks across cities — Sub-agents fetch weather to steer users away from risky plans. *[claimed]*
- Orchestrator with parallel sub-agents — Page describes an orchestrator delegating to MCP-equipped sub-agents; final repo moved to a single agent. *[unclear]*

**Flow:** User texts the Flub number → Message reaches the agent server through the Photon watcher → Claude agent picks flight or weather tools → Reply is texted back

**Prompt:** Photon-sponsored HackPrinceton Fall 2025 track on hybrid-intelligence agents; the public page lists only prize amounts (winner plus runner-up, Photon credits, interview fast-track) and no build brief.
**Fit (implied):** An AI agent that users reach through native text messaging via Photon SDK, with tool-using sub-agents behind it.  *(targeted: Exploring Hybrid Intelligence by Photon, Best Use of Vibe Kanban)*
**Sponsor tools:** Photon SDK (Receive and send user texts, core); Dedalus MCP hosting (Attempted to deploy MCP tools; stayed local, token)
**AI:** Claude API with native function calling over Python tools; page also tags OpenAI and describes an orchestrator-plus-sub-agent design using MCP servers.
**Architecture:** iMessage watcher (TypeScript) posts to a Python agent server; a single Claude agent calls local tool functions such as flight search; separate repos hold web site and MCP servers.
**Novelty:** Targets disruption prediction through social-media signals over SMS; the repo README notes a deliberate move away from MCP to simple direct tools.
**Scope:** small · working: Repo has a runnable agent with flight search and an iMessage bridge; delay prediction not evidenced. · polish: Landing site at textfly.tech and setup docs; no video or tests.
**Claims:** 'Instant, accurate responses' stated without metrics | Predicts delays from real-time X data
**Gaps:** No video; Devpost design differs from repo (MCP vs single agent)
Sources: https://devpost.com/software/textfly, https://github.com/TextFly/flub-agent, https://hackprinceton-fall-2025.devpost.com/

---

### Wings
*HackPrinceton HackPrinceton Fall 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Exploring Hybrid Intelligence by Photon

**What it is:** Wings pairs an iMessage financial coach with a WingsPay BNPL demo web app. Knot and Nessie transaction data in Snowflake feed a credit-scoring model and LLM answers, so users get dynamic credit offers or spending advice.
**Problem / user:** People with thin credit files, such as new immigrants and young earners, plus lenders wanting behavior-based credit decisions.

**Features**
- iMessage financial coach — Node bot using Photon iMessage Kit fetches Snowflake transactions and replies via Cortex, OpenAI or Dedalus, chunked like human texts. *[shown_working]*
- Dynamic credit score and loan recommendation — Weighting model on bank and merchant data yields a score and suggested amount. *[claimed]*
- Advice mode on risky spending — Overspending signals switch the bot from offering credit to nudging. *[claimed]*
- Data ingestion from Knot and Nessie — Scripts pull merchant transactions, bills, deposits and loans and standardize them in Snowflake. *[shown_working]*
- WingsPay BNPL checkout web app — React/Vite storefronts, checkout flow and credit dashboard backed by an Express server. *[shown_working]*

**Flow:** User authorizes data access in the frontend → Backend pulls Knot transactions and Nessie account data into Snowflake → Model scores credit health → User texts the iMessage bot for insights → Bot offers credit or switches to advice mode

**Prompt:** Photon-sponsored HackPrinceton Fall 2025 track on hybrid-intelligence agents; the public page lists only prize amounts (winner plus runner-up, Photon credits, interview fast-track) and no build brief.
**Fit (implied):** Financial coaching delivered as a conversational iMessage agent via Photon's kit, combining LLM reasoning, Snowflake Cortex SQL and structured credit scoring.  *(targeted: Exploring Hybrid Intelligence by Photon)*
**Sponsor tools:** Photon iMessage Kit (Monitor and reply to iMessages, core); Capital One Nessie (Identity, bills, loans, deposits, supporting)
**AI:** OpenAI models (default gpt-4o-mini) and optional Dedalus models answer questions and generate SQL; Snowflake Cortex adds SQL/NLP insights; credit model is a weighted scoring approach with unspecified training data.
**Architecture:** Knot and Nessie scripts populate Snowflake; Node chatbot with iMessage bridge queries it, optionally via a FastAPI Dedalus bridge; React/Vite web app and Express server host the BNPL demo.
**Novelty:** Reframes credit as behavior-based and ties it to BNPL, offering both a chat coach and a checkout demo from the same data pipeline.
**Scope:** large · working: Repo has about 24.6k LOC, datasets, bot phone number in README, and tests. · polish: Layout and env docs are clear; 14 screenshots; no video.
**Claims:** Credit model trained on 'large-scale datasets' (no detail) | Winner of Photon track
**Gaps:** No video; Model details absent
Sources: https://devpost.com/software/wingpay, https://github.com/leowang2004/hackprinceton2025

---

