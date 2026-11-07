# HackNotts — HackNotts '25 (3 projects)

### Chronomancer
*HackNotts HackNotts '25 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place [1st]

**What it is:** A toy strategy game where the player rules medieval kingdoms generated from real UK cities and issues decisions that reshape past, present or future events. An SMT solver checks that the resulting timeline is consistent; a paradox ends the game. Played on a touch-controlled fabric lectern.
**Problem / user:** No stated problem; a game for strategy and time-puzzle fans, inspired by the card game Reigns, built as a 24-hour hackathon entry.

**Features**
- Non-linear acyclic time — Events held as a directed acyclic graph in a Rust controller, converted to interval order for display on a circular clock-like interface. *[shown_working]*
- Real UK cities as medieval kingdoms — Google Directions, Routes and Places data mapped onto a unit circle; notable locations become faction outposts (York, Southampton, Brighton screens). *[shown_working]*
- Three factions via k-means — Locations clustered into Gnomes, Centaurs and Trolls, each with custom emblems rendered in the game. *[claimed]*
- Symbolic ledger decisions — Decisions are generated from their effects, then reworded into natural-language descriptions by the OpenAI API. *[claimed]*
- SMT timeline verification — Accepting a ledger encodes the map-time state as first-order constraints; Z3 must find a valid timeline or the player loses. *[shown_working]*
- Win, loss and unsatisfiable screens — Devpost gallery shows menu, gameplay, ledger, unsatisfiable-decision, loss and win screens. *[shown_working]*
- Narrative from constraints — Story arcs derived from symbolic constraints and acted out by AI. *[claimed]*
- Touch-only lectern hardware — A purple fabric lectern from a craft shop serves as a mystic touch play surface; touch control worked 15 minutes before hand-in. *[claimed]*

**Flow:** Start from the main menu → See real-city kingdoms grouped into factions → Open the ledger of decisions with natural-language text → Pick a decision that alters past, present or future events → Accepting triggers Z3 satisfiability check → Valid timeline: play continues; paradox: game over

**Prompt:** Open brief: build anything that works (site, game, program) in 25 hours; judged on Creativity, Completeness and Technical Achievement. First Place has no separate description.
**Fit (none):** Game combining a formal-logic solver, real map data and AI text in a playable loop; no prize is named on the page.  *(targeted: First Place)*
**AI:** OpenAI API rewrites symbolically generated decision text into readable ledgers; k-means clusters locations; Z3 SMT solver (not ML) proves timeline consistency.
**Architecture:** Rust controller (events DAG, Z3, petgraph, reqwest to Google/OpenAI) feeding a GameMaker frontend; Google location data to unit-circle kingdoms; touch lectern as input.
**Novelty:** Uses a formal SMT solver as the game rule engine to prove or refute timeline paradoxes; physical lectern built the night before.
**Scope:** medium · working: Devpost shows gameplay, win and loss screens and an embedded video; README admits bugs and no install guidance. · polish: Custom emblems, logo gif, themed interface and lectern prop; no tests or CI.
**Claims:** Largest hackathon undertaking in Rust for the team | Touch control working 15 minutes before hand-in | First Place at HackNotts 25
**Gaps:** YouTube video not watchable; No install steps; Devpost has no challenges section; roles of Gamemaker vs Rust parts not detailed
Sources: https://devpost.com/software/chronomancer, evidence/hacknotts-hacknotts-25-chronomancer.json (README, tobybenjaminclark/chrono), https://hacknotts-25.devpost.com/

---

### Functional Fantisay Minecraft TEAM 44
*HackNotts HackNotts '25 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Place [2nd]; Best use of Haskell Prize

**What it is:** A Minecraft-style 3D voxel game written in Haskell on OpenGL bindings, with a self-built rendering engine, block placing, and lighting. Built by one author in 24 hours.
**Problem / user:** No problem stated; personal project for someone who wanted a Minecraft clone and likes Haskell.

**Features**
- Fully 3D voxel world — A Minecraft-like block world rendered in 3D in Haskell. *[shown_working]*
- Custom 3D rendering engine — Rendering built from scratch over OpenGL bindings using custom shader code. *[claimed]*
- Block building — Screenshot captioned "Building a House" shows placed blocks forming a structure. *[shown_working]*
- Lighting — Screenshot captioned "Lights" shows lit scenes. *[shown_working]*

**Flow:** Launch the Haskell executable → Move through the 3D voxel world → Place blocks to build structures such as a house

**Prompt:** Open brief and judging criteria for the event; "Best use of Haskell" is listed as a prize name without any description.
**Fit (implied):** Entire game and renderer are written in Haskell with OpenGL bindings; author says the aim was a Minecraft clone in Haskell.  *(targeted: Best use of Haskell)*
**AI:** none
**Architecture:** Single Haskell program using OpenGL bindings and custom shaders to render a block world; no server or external services mentioned.
**Novelty:** Pure functional-language implementation of a graphics-heavy voxel engine; author notes they dislike monads afterwards.
**Scope:** small · working: Three screenshots show rendered world, building and lighting; no demo video or repo. · polish: Rough: empty "What it does" and "What next" sections, typos, no repo link.
**Claims:** A fully 3D Minecraft clone in Haskell | Built a 3D rendering engine in Haskell
**Gaps:** No repo or video; What it does section empty; Whether name "Fantisay" targets the Fantasy theme prize is not stated
Sources: https://devpost.com/software/functional-fantisay-minecraft, https://hacknotts-25.devpost.com/

---

### Medieval Roguelike
*HackNotts HackNotts '25 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** First Time Hackers

**What it is:** A small pygame roguelike by a two-person team: grind gold, buy a few power boosters, then find and defeat a boss. Built in about a day after Unity was blocked on school devices; art comes from open-licensed itch.io packs.
**Problem / user:** No problem statement; a quick first-hackathon game for players of simple roguelikes.

**Features**
- Roguelike combat loop — Player explores generated levels and fights enemies in pygame; repo has generation and object modules *[claimed]*
- Gold grinding and boosters — Earn gold and buy a small set of power boosters *[claimed]*
- Boss fight — Find and defeat the boss as the end goal *[claimed]*
- Level generation — Repo contains a generation folder with procedural-level code (not described on page) *[unclear]*

**Flow:** Launch the pygame window → Fight enemies to collect gold → Buy boosters → Locate and defeat the boss

**Prompt:** not public / not found
**Fit (none):** Prize listed by name only on the hackathon page; the Devpost page does not state first-time status explicitly, though the team calls itself new to this style of project.  *(targeted: First Time Hackers)*
**AI:** none
**Architecture:** Single Python/pygame program with asset, object and level-generation modules; art from third-party open-licensed packs.
**Novelty:** Plain, self-described scuffed small game; notable only as a quick pivot from Unity to pygame.
**Scope:** small · working: Repo of about 2.9k lines and 127 files; page calls it playable with a full loop. · polish: Explicitly deprioritized art; no README, video or demo link.
**Claims:** Playable progression loop from gold to boss
**Gaps:** no README; no video, so gameplay not seen; Devpost description very short
Sources: https://devpost.com/software/medieval-roguelike, evidence/hacknotts-hacknotts-25-medieval-roguelike.json (no README, tree only), prompts_cache/hacknotts-25.md

---

