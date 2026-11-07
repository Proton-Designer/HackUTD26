# LA Hacks (AI Hackathon 2026): project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## LA Hacks AI Hackathon 2026

### BetterBill  (LA Hacks AI Hackathon 2026)

- **Prizes:** Photon: Best Voice Agent (also Visa prize) [unknown]  (tier: sponsor_winner)
- **Pitch:** Medical-bill dispute assistant that reads bill photos, checks charges against price files and policies, drafts appeal letters and phones billing offices with a voice agent.
- **Problem / user:** Patients facing large hospital bills must learn billing codes, price files and charity-care rules and lose hours on hold to dispute them. / patients disputing hospital bills
- **Domain / idea type:** health_wellness + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; llm_chat; speech_or_voice; agent_or_tool_use
- **Stack:** langs TypeScript; Python; frontend React; React Native; Expo; TanStack Start; Tailwind CSS; shadcn/ui; backend Bun; oRPC; Better Auth; Drizzle ORM; db PostgreSQL (Tiger Data); hosting Vercel
- **Tech/APIs:** Photon (phone line) (telecom, core, sponsor); ElevenLabs agent (ai_model, core, sponsor); Google Gemini (ai_model, core, sponsor); StepFun (ai_model, supporting, sponsor); Browser Use (other, supporting, sponsor); Tiger Data (database, supporting, sponsor); Sentry (other, supporting, sponsor); LiveKit (telecom, supporting); Playwright (framework, supporting)
- **Sponsor APIs:** Photon; ElevenLabs; Gemini; StepFun; Browser Use; Tiger Data; Sentry | fit: Won Photon's Best Voice Agent: an ElevenLabs agent places calls to billing offices over a Photon line while Gemini drafts letters and Browser Use gathers price files.
- **Repo:** public, commits 205 (before/in/after event: 0/205/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 10, writeup medium, impact claims True (Reports results on 5 recreated KFF Health News Bill of the Month cases, including misses.)
- **Notes:** Splits work so AI transcribes and drafts while a TypeScript rules engine decides facts; self-reports misses on five recreated KFF Bill of the Month cases; lists seven sponsor tools.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections; sponsor_apis_used
- **Links:** [Devpost](https://devpost.com/software/betterbill) | [GitHub](https://github.com/matmanna/betterbill)

### Henomaly  (LA Hacks AI Hackathon 2026)

- **Prizes:** Photon: iMessage Track Winner (also QNX prize) [unknown]  (tier: sponsor_winner)
- **Pitch:** Edge computer-vision system watching poultry flocks for early signs of disease, sending farmers an iMessage alert with evidence image and explanation.
- **Problem / user:** Diseases like avian influenza spread fast through commercial flocks and are caught late without continuous monitoring. / poultry farmers
- **Domain / idea type:** other + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web; bot_or_chat / True / vision; predictive_ml; agent_or_tool_use
- **Stack:** langs Python; C; TypeScript; frontend Next.js; React; backend ; db ; hosting Vercel; AWS
- **Tech/APIs:** Photon (iMessage) (telecom, core, sponsor); QNX (other, core, sponsor); YOLO / Ultralytics (ai_model, core); ONNX Runtime (framework, core); PyTorch (framework, supporting); OpenCV (framework, supporting); Raspberry Pi (hardware_part, supporting); ESP32 (hardware_part, supporting); AWS (cloud, supporting)
- **Sponsor APIs:** Photon; QNX | fit: Won Photon's iMessage track: Photon and iMessage deliver alerts with evidence image to the farmer, who can chat, request the image and decide whether to share it with a vet; also targeted the QNX prize.
- **Repo:** public, commits 178 (before/in/after event: 0/178/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 28, writeup long, impact claims False
- **Notes:** Runs detection on QNX-based edge hardware (Raspberry Pi/ESP32 mentioned) with ONNX Runtime; farmer chooses what is shared with a vet; team drafted a fix for QNX's ONNX Runtime packaging.
- **Team size:** 3 | **Confidence:** high | unverified: writeup_sections; has_hardware depth
- **Links:** [Devpost](https://devpost.com/software/holy-crap) | [GitHub](https://github.com/RishitRai/Henomaly)

### SproutPass  (LA Hacks AI Hackathon 2026)

- **Prizes:** Photon: iMessage Runner-Up (also Visa prize) [unknown]  (tier: sponsor_winner)
- **Pitch:** Parents' companion that lists outgrown baby clothes from photos or iMessage, extracts needs, and suggests nearby trades between parents when their paths cross.
- **Problem / user:** Babies outgrow clothes quickly, and listing items, finding buyers and coordinating exchanges takes effort for parents. / parents of young children
- **Domain / idea type:** retail_consumer + social_community / twist_on_known_app
- **Platforms / hardware / AI:** web; bot_or_chat / False / vision; llm_chat; recommendation
- **Stack:** langs TypeScript; frontend React; Vite; React-Leaflet; Zustand; Base44; backend ; db ; hosting 
- **Tech/APIs:** Photon (iMessage) (telecom, core, sponsor); Claude (ai_model, core); Codex (ai_model, supporting); Base44 (framework, supporting); Leaflet (maps_geo, supporting); React (framework, supporting)
- **Sponsor APIs:** Photon | fit: Runner-up in Photon's iMessage track: Photon connects a private iMessage conversation where parents send clothing photos and receive marketplace offers and payment receipts; also targeted the Visa prize.
- **Repo:** public, commits 73 (before/in/after event: 0/73/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Game-like nearby 'encounter' matching (inspired by Pikmin); AI asks for confirmation before saving details; real iMessage demo of an offer and a simulated-payment receipt; location is simulated offline.
- **Team size:** 3 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/sproutpass) | [GitHub](https://github.com/96528025/SproutPass)
