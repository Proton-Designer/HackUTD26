# HackPrinceton: project cards (8 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackPrinceton Fall 2025

### doeve  (HackPrinceton Fall 2025)

- **Prizes:** Exploring Hybrid Intelligence by Photon [unknown]  (tier: sponsor_winner)
- **Pitch:** Personal agent you text or voice-message over iMessage to operate your computer remotely: fetch files, run scripts, push commits, with live progress and interruptible tasks.
- **Problem / user:** Users away from their computer sometimes need quick file access or commands and have no easy way to trigger them remotely. / developers and power users away from their computer
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; desktop / False / agent_or_tool_use; llm_chat; speech_or_voice; vision
- **Stack:** langs Python; TypeScript; frontend ; backend FastAPI; Node.js; Uvicorn; WebSocket; db ; hosting 
- **Tech/APIs:** Photon iMessage SDK (telecom, core, sponsor); Claude 3.5 Sonnet (Anthropic API) (ai_model, core); LangGraph / LangChain (framework, core); ElevenLabs (ai_model, supporting); PyAutoGUI / PyObjC (other, supporting); OpenCV (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** Photon iMessage SDK | fit: Targeted Photon's Hybrid Intelligence track by making iMessage (text or voice) the sole interface to a LangGraph/Claude agent that executes tasks on the user's computer and reports progress back.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims False
- **Notes:** Agent controls the host machine (PyAutoGUI, PyObjC, OpenCV) from an iMessage thread, accepts voice input, streams progress and lets the user change tasks mid-run.
- **Team size:** 3 | **Confidence:** high | unverified: writeup_sections; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/do-eve) | [GitHub](https://github.com/adhvaidhsunny/doeve)

### edgecart.  (HackPrinceton Fall 2025)

- **Prizes:** Winner Best Financial Hack by Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Predictive waste system for grocers that detects produce decay with computer vision and links it to purchasing behavior to cut spoilage.
- **Problem / user:** Grocers lose produce to spoilage without tools tying freshness to what customers actually buy. / grocery stores and retailers
- **Domain / idea type:** retail_consumer + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml; llm_chat
- **Stack:** langs Python; TypeScript; frontend React; backend Flask; WebSocket; db ; hosting 
- **Tech/APIs:** PyTorch ResNet18 (ai_model, core); YOLOv8 and OpenCV (ai_model, core); Knot (data_source, supporting); Google Gemini (ai_model, supporting); xAI Grok (ai_model, supporting)
- **Sponsor APIs:**  | fit: Won Capital One's Best Financial Hack for a grocery-waste analytics product that ties spoilage to purchase behavior; the page does not mention Capital One or Nessie.
- **Repo:** public, commits 148 (before/in/after event: 0/146/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup long, impact claims True (Projects a 19.5 percent waste reduction via Markov-chain analysis and cites 90 percent classifier accuracy.)
- **Notes:** Custom ResNet18 freshness classifier plus YOLOv8 tracking over live video, with a Markov-chain projection of waste reduction; own domain site and Knot transaction data.
- **Team size:** 3 | **Confidence:** high | unverified: event_end; sponsor_fit_note; Knot is_sponsor; ui_polish
- **Links:** [Devpost](https://devpost.com/software/edgecart) | [GitHub](https://github.com/AntoDono/edgecart)

### Messenger AI  (HackPrinceton Fall 2025)

- **Prizes:** Exploring Hybrid Intelligence by Photon [unknown]  (tier: sponsor_winner)
- **Pitch:** AI agent in iMessage group chats that reads texts, PDFs and images to give summaries, answers or memes to the group.
- **Problem / user:** Group conversations, such as study groups, lack an AI helper that works in the chat itself with shared context. / friends and study groups in group chats
- **Domain / idea type:** social_community + education / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; agent_or_tool_use; vision
- **Stack:** langs Python; TypeScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Photon iMessage Kit (telecom, core, sponsor); Dedalus Labs (ai_model, core)
- **Sponsor APIs:** Photon iMessage Kit | fit: Targeted Photon's Hybrid Intelligence track by building the agent on Photon's iMessage Kit with Dedalus Labs so it ingests chat texts, PDFs and images.
- **Repo:** None, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup short, impact claims False
- **Notes:** Short writeup; group-chat support was still a limitation and the team wanted Photon added like an extra contact.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/messenger-ai)

### PiggyBank  (HackPrinceton Fall 2025)

- **Prizes:** Exploring Hybrid Intelligence by Photon [unknown]  (tier: sponsor_winner)
- **Pitch:** Personal-finance assistant that tracks everyday spending from linked bank data and receipts, predicts purchases and nudges users through iMessage.
- **Problem / user:** Small invisible daily purchases quietly cause financial stress and people lack timely, low-friction guidance. / young adults managing everyday spending
- **Domain / idea type:** fintech_finance + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; recommendation; predictive_ml; vision
- **Stack:** langs Python; SQL; frontend Clerk; backend Flask; Node.js; db Snowflake; hosting DigitalOcean
- **Tech/APIs:** Photon (iMessage) (telecom, core, sponsor); Capital One Nessie (payments, core, sponsor); Dedalus (ai_model, supporting); Knot (payments, supporting); Snowflake (database, supporting); Gemini (ai_model, supporting); OpenAI (ai_model, supporting); Llama (ai_model, unclear); DigitalOcean (cloud, supporting); Clerk (auth, supporting); Flask (framework, supporting)
- **Sponsor APIs:** Photon; Capital One Nessie | fit: Targeted Photon's Hybrid Intelligence track with an iMessage agent that chats with the user about spending, sends spending nudges, and takes goals set via Nessie-linked accounts.
- **Repo:** public, commits 27 (before/in/after event: 0/24/3), README detailed
- **Demo/writeup:** video True, live none, screenshots 61, writeup long, impact claims False
- **Notes:** Combines Capital One Nessie bank linking, receipt processing, Snowflake storage, predicted-purchase scheduling and iMessage nudges; Photon pings were triggered manually for the demo.
- **Team size:** 4 | **Confidence:** medium | unverified: sponsor_apis_used depth; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/tbd-9clz1k) | [GitHub](https://github.com/HackPrincetonQANT/backend-frontned-agent-alltogether)

### TextFly  (HackPrinceton Fall 2025)

- **Prizes:** Exploring Hybrid Intelligence by Photon [unknown]  (tier: sponsor_winner)
- **Pitch:** Text-message travel agent that handles flight delay and cancellation rebooking, flight search and travel insights through a simple conversation, built on Photon.
- **Problem / user:** Travelers hit by widespread flight disruptions need fast rebooking help without navigating airline apps and sites. / air travelers facing delays or cancellations
- **Domain / idea type:** mobility_transport + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Photon SDK (telecom, core, sponsor); Anthropic (ai_model, core); OpenAI (ai_model, supporting); MCP servers (fast-flights, X, photon-imsg) (other, core)
- **Sponsor APIs:** Photon SDK | fit: Targeted Photon's Hybrid Intelligence track by using the Photon SDK for all inbound and outbound iMessage traffic to an orchestrator agent that books and searches flights, wrapped as an MCP server.
- **Repo:** public, commits 29 (before/in/after event: 0/29/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup short, impact claims False
- **Notes:** Orchestrator agent plus separate MCP servers (iMessage via Photon, flights search, X); multiple repos linked under a TextFly GitHub org.
- **Team size:** 4 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/textfly) | [GitHub](https://github.com/TextFly/flub-agent)

### Wings  (HackPrinceton Fall 2025)

- **Prizes:** Exploring Hybrid Intelligence by Photon [unknown]  (tier: sponsor_winner)
- **Pitch:** Dynamic credit-scoring system that combines bank-statement and spending data into a score and loan recommendation, delivered through an iMessage chatbot.
- **Problem / user:** Traditional credit systems exclude people with short credit histories such as new immigrants and young earners. / new immigrants and young earners with thin credit files
- **Domain / idea type:** fintech_finance + social_community / twist_on_known_app
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; predictive_ml
- **Stack:** langs JavaScript; Python; frontend React; backend Node.js; db Snowflake; hosting 
- **Tech/APIs:** Photon iMessage Kit (@photon-ai/imessage-kit) (telecom, core, sponsor); Capital One Nessie (payments, core, sponsor); Knot (payments, supporting); Dedalus (ai_model, supporting); OpenAI (ai_model, supporting); Snowflake (database, supporting); React (framework, supporting)
- **Sponsor APIs:** Photon iMessage Kit; Capital One Nessie | fit: Targeted Photon's Hybrid Intelligence track with a Node.js chatbot on @photon-ai/imessage-kit that watches incoming messages and returns credit score and loan guidance from Nessie and Knot data.
- **Repo:** public, commits 52 (before/in/after event: 0/52/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 43, writeup long, impact claims False
- **Notes:** Chatbot built with the Photon iMessage Kit monitors incoming messages; combines Nessie and Knot financial data with Snowflake scale datasets; mentions targeted engagement as a business angle.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/wingpay) | [GitHub](https://github.com/leowang2004/hackprinceton2025)


## HackPrinceton Spring 2025

### Roots  (HackPrinceton Spring 2025)

- **Prizes:** Winner Best Financial Hack [Sponsored by Capital One] [unknown]  (tier: sponsor_winner)
- **Pitch:** Finance education app that creates real Nessie accounts and transactions to teach financial independence, recommending the best credit card from a user's transaction history.
- **Problem / user:** Fragmented fintech apps overwhelm people trying to manage money; learners need one grounded place with real account data. / young adults learning personal finance
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend Flask; SQLAlchemy; db PostgreSQL; hosting 
- **Tech/APIs:** Capital One Nessie API (data_source, core, sponsor); Auth0 (auth, supporting); PostgreSQL (database, supporting); Flask (framework, core); Next.js (framework, core)
- **Sponsor APIs:** Capital One Nessie API | fit: Won Best Financial Hack by using the Nessie API to create a user's checking, savings and credit card accounts and drive transaction-based card recommendations and investment tracking.
- **Repo:** public, commits 8 (before/in/after event: 0/7/1), README solid
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Production-minded stack with Auth0 login, Postgres and Nessie-created checking, savings and credit card accounts; large writeup of about 1000 words and four authors.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; writeup_sections; ai_used; ui_polish
- **Links:** [Devpost](https://devpost.com/software/roots-xk19te) | [GitHub](https://github.com/Roots-Finance/parent-repo)


## Spring 2025

### SixthSense  (Spring 2025)

- **Prizes:** Best Overall Hack (Meta Quest + NordVPN products 1yr + 1GB data per member) [unknown]  (tier: overall_top3)
- **Pitch:** Wearable for blind users that turns objects seen through Meta glasses into unique vibration signatures on a glove and guides the hand toward them with servo motors.
- **Problem / user:** Assistive tools overload hearing or give only basic obstacle detection; blind users need a richer sense of what and where objects are. / blind and visually impaired people
- **Domain / idea type:** accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision
- **Stack:** langs Python; C++ (Arduino); frontend Next.js; backend Python; db ; hosting 
- **Tech/APIs:** YOLOv8 (ai_model, core); Meta smart glasses (hardware_part, core); Arduino + vibration and servo motors (hardware_part, core); Word embeddings + inverse Fourier transform (other, core)
- **Sponsor APIs:**  | fit: Won Best Overall Hack, whose prize bundle included NordVPN products; the project uses no Nord technology, so the sponsor link is only the prize item.
- **Repo:** public, commits 28 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims True (Cites 253 million people with visual impairment and reports 71.68% vs 10.23% pattern correlation.)
- **Notes:** YOLOv8 detections become word embeddings converted to vibration patterns with an inverse Fourier transform; separate 'what' glove and 'where' servo gauntlet on Arduinos; reports 71.68% vs 10.23% pattern correlation for similar vs different objects.
- **Team size:** 3 | **Confidence:** medium | unverified: ui_polish; event_start; event_end; placement
- **Links:** [Devpost](https://devpost.com/software/sixthsense-xuw41r) | [GitHub](https://github.com/k-kochhar/SixthSense)
