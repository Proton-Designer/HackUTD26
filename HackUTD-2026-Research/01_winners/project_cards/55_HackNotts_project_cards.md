# HackNotts: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackNotts '25

### Chronomancer  (HackNotts '25)

- **Prizes:** First Place [1st]  (tier: overall_top3)
- **Pitch:** Strategy game where players command events across non-linear time over UK cities as medieval kingdoms, with Z3 SMT proofs of timeline consistency.
- **Problem / user:** Prevent time paradoxes while ruling across past and future. / strategy game players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop; hardware / True / llm_chat
- **Stack:** langs Rust; GML; frontend GameMaker; backend Rust; db ; hosting 
- **Tech/APIs:** Z3 theorem prover (framework, core); GameMaker (framework, core); Google Directions/Routes/Places APIs (maps_geo, core); OpenAI API (ai_model, supporting); k-means clustering (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 77 (before/in/after event: 0/76/1), README detailed
- **Demo/writeup:** video False, live none, screenshots 11, writeup long, impact claims False
- **Notes:** Rust controller with GameMaker frontend; SMT solver verifies win/loss; Google Maps APIs turn real cities into game worlds; played on a touch-controlled hand-made fabric lectern.
- **Team size:** 3 | **Confidence:** high | unverified: has_hardware; team_size
- **Links:** [Devpost](https://devpost.com/software/chronomancer) | [GitHub](https://github.com/tobybenjaminclark/chrono)

### Functional Fantisay Minecraft TEAM 44  (HackNotts '25)

- **Prizes:** Second Place [2nd]; Best use of Haskell Prize [unknown]  (tier: overall_top3)
- **Pitch:** Minecraft-style 3D voxel clone written in Haskell with OpenGL bindings.
- **Problem / user:** Solo attempt to build a Minecraft clone in 24 hours in Haskell. / self / game developers
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Haskell; frontend ; backend ; db ; hosting 
- **Tech/APIs:** OpenGL (framework, core); Haskell (framework, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 3, writeup short, impact claims False
- **Notes:** Own 3D rendering engine in Haskell; author's writeup is terse and informal; also won Best use of Haskell prize; no GitHub linked.
- **Team size:** 1 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/functional-fantisay-minecraft)

### Medieval Roguelike  (HackNotts '25)

- **Prizes:** First Time Hackers [unknown]  (tier: track_winner)
- **Pitch:** Basic pygame roguelike where you grind gold for boosts and defeat a boss.
- **Problem / user:** Two first-time hackers building a small game in a day. / first-time hackers / casual players
- **Domain / idea type:** entertainment_games / entertainment_or_game
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** pygame (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 104 (before/in/after event: 0/104/0), README none
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Pivoted from Unity (blocked on school devices) to pygame; all art is open-licensed and not the team's own.
- **Team size:** 2 | **Confidence:** medium | unverified: n_screenshots
- **Links:** [Devpost](https://devpost.com/software/medieval-roguelike) | [GitHub](https://github.com/Huskslay/Hacknotts)


## HackNotts '26

### Holy XP  (HackNotts '26)

- **Prizes:** First Time Hacker [unknown]  (tier: track_winner)
- **Pitch:** Windows XP-themed hedge fund game with a simulated stock market, Bloomberg-style ticker and local-LLM-written news and emails, set in the dot-com crash.
- **Problem / user:** First-time hackers building a retro OS-style game around the Y2K theme. / first-time hackers and game players
- **Domain / idea type:** entertainment_games + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend Python; db ; hosting 
- **Tech/APIs:** Local LLM (ai_model, core); React (framework, core); Cloudflared (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 35 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Team stresses hand-coded work; stock simulator translated from Tkinter to React; a local LLM writes emails and news that may be tips or lies.
- **Team size:** 4 | **Confidence:** high | unverified: tech_items depth
- **Links:** [Devpost](https://devpost.com/software/y2k_os) | [GitHub](https://github.com/JamesBoyl3/HackNotts2026)

### Kitkat  (HackNotts '26)

- **Prizes:** First Place [1st]; Whimsy Prize [unknown]  (tier: overall_top3)
- **Pitch:** ESP32 flip-phone-style handheld with custom C++ OS, Snake, a drawing app and music playback, in a 3D-printed Hello Kitty case.
- **Problem / user:** Explore the origins of the cyberdeck trend by building a retro flip handheld. / hobbyists and makers
- **Domain / idea type:** entertainment_games + creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C++; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Arduino IDE (framework, core); Fusion 360 (other, supporting); Blender (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 14 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video False, live none, screenshots 4, writeup medium, impact claims False
- **Notes:** ESP32 had too few buses to run touchscreen, display and SD card together; code outgrew flash so partition scheme changed; printed case designed in Fusion 360 and Blender.
- **Team size:** 3 | **Confidence:** high
- **Links:** [Devpost](https://devpost.com/software/kitkat) | [GitHub](https://github.com/Nox-afg/Hacknotts26)

### Logicverse  (HackNotts '26)

- **Prizes:** Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Deterministic simulation of hackathon attendees: scraped data forms a ~90,000-fact SPARQL knowledge base that drives scripted conversations between on-screen avatars.
- **Problem / user:** Simulate online-era human conversation using logic rather than generative AI. / hackathon attendees
- **Domain / idea type:** entertainment_games + social_community / creative_tool
- **Platforms / hardware / AI:** desktop / False / vision
- **Stack:** langs Rust; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Bevy (framework, core); SPARQL / RDF Turtle (database, core); web scrapers (data_source, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Scraped Discord (via browser automation), GitHub, LinkedIn and Devpost for attendee facts; Rust/Bevy renderer with custom stage-direction DSL; webcam face matching puts people on screen.
- **Team size:** 4 | **Confidence:** high | unverified: team_size; ai_types
- **Links:** [Devpost](https://devpost.com/software/logicverse)
