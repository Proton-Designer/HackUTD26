# SwampHacks: project cards (4 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## SwampHacks - XI

### OffTrails  (SwampHacks - XI)

- **Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place) [unknown]  (tier: overall_top3)
- **Pitch:** Off-trail route planner that runs a modified A* search over USGS terrain and Sentinel-2 water and vegetation data between user-chosen start and end points.
- **Problem / user:** Hikers heading off marked trails lack route guidance that accounts for terrain, water and vegetation. / Outdoor hikers
- **Domain / idea type:** mobility_transport + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend Leaflet.js; backend ; db ; hosting 
- **Tech/APIs:** USGS elevation data (data_source, core); Sentinel-2 L2A (data_source, core); Rasterio (framework, supporting); Leaflet.js (maps_geo, supporting); OpenStreetMap (maps_geo, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 40 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Uses satellite and elevation datasets rather than trail maps for pathfinding; map shown with Leaflet.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ai_used
- **Links:** [Devpost](https://devpost.com/software/offtrails) | [GitHub](https://github.com/blohse8/OffTrails)

### ReStory  (SwampHacks - XI)

- **Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place) [unknown]  (tier: overall_top3)
- **Pitch:** Wearable AI device that identifies people by face and voice embeddings and isolates the wearer's own speech to help recall conversations.
- **Problem / user:** People struggle to remember who they met and what was said in conversations. / Wearers who want conversation recall, e.g. memory-impaired users
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; speech_or_voice; rag_or_search; llm_chat
- **Stack:** langs Python; frontend ; backend FastAPI; WebSockets; db ChromaDB; hosting 
- **Tech/APIs:** Raspberry Pi 5 (hardware_part, core); ArcFace / ECAPA-TDNN embeddings (ai_model, core); WhisperX (ai_model, core); SpeechBrain (framework, supporting); Gemini (ai_model, supporting); OpenRouter (ai_model, supporting); ChromaDB (database, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 130 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 28, writeup long, impact claims False
- **Notes:** Fuses ArcFace face and ECAPA-TDNN voice embeddings on a Raspberry Pi 5 with a wearer-anchoring step to separate the user's voice.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; target_user
- **Links:** [Devpost](https://devpost.com/software/restory) | [GitHub](https://github.com/retromonos/SwampHacks11FIH)

### SignHero  (SwampHacks - XI)

- **Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place); Best Game Design Project [unknown]  (tier: overall_top3)
- **Pitch:** Guitar Hero-style rhythm game that teaches ASL fingerspelling using webcam hand tracking, with song, training and testing modes.
- **Problem / user:** Learning sign language fingerspelling is dull and gives little real-time feedback. / ASL learners
- **Domain / idea type:** accessibility + education / entertainment_or_game
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs TypeScript; frontend Next.js; Tailwind CSS; backend T3 stack; db MongoDB; hosting 
- **Tech/APIs:** MediaPipe (framework, core); OpenCV (framework, supporting); MongoDB (database, supporting); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 183 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 31, writeup long, impact claims False
- **Notes:** Webcam hand-pose recognition drives beatmap-synced gameplay; writeup covers latency optimization and timing sync challenges.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; stack_languages; stack_backend
- **Links:** [Devpost](https://devpost.com/software/signhero) | [GitHub](https://github.com/MsMarion/ASL-Fun-Training)


## SwampHacks - XII

### Spotle.ink  (SwampHacks - XII)

- **Prizes:** Best First Timers [unknown]  (tier: track_winner)
- **Pitch:** Multiplayer webcam scavenger-hunt game where Gemini generates a findable household item each round and players race in a WebRTC video room.
- **Problem / user:** Remote players want a quick, active party game that works over video with friends. / Casual friend groups playing online
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; vision
- **Stack:** langs JavaScript; frontend React; Tailwind CSS; Vite; backend Node.js; Socket.IO; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core); PeerJS / WebRTC (other, core); Socket.IO (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 124 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 49, writeup long, impact claims False
- **Notes:** Four-letter room codes, peer-to-peer WebRTC video grid and Gemini-generated round challenges; 49 screenshots.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; writeup_sections; vision
- **Links:** [Devpost](https://devpost.com/software/spotle-ink) | [GitHub](https://github.com/MasonRLevy/Spotle.ink)
