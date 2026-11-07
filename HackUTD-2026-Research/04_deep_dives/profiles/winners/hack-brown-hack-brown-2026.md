# Hack@Brown — Hack@Brown 2026 (1 projects)

### Emerald Path
*Hack@Brown Hack@Brown 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First-Time Hack

**What it is:** A React web app that draws Boston sidewalks on a Kepler.gl map from the city's Sidewalk Inventory data, lets users filter them by incline, surface, width and hazard, and routes between two points using only suitable sidewalks.
**Problem / user:** People with mobility disabilities lack sidewalk-quality data (surface, width, slope) in mainstream maps, making walking trips risky and anxiety-inducing; built by freshmen after a snowstorm.

**Features**
- Sidewalk map — Parses Analyze Boston Sidewalk Inventory GeoJSON and renders sidewalks on an embedded Kepler.gl map *[shown_working]*
- Accessibility filters — Users toggle incline, surface material, width and hazard level; the map updates to show matching sidewalks *[shown_working]*
- Accessible routing — Sidewalk graph with A* search finds the shortest route between two places using only acceptable sidewalks, limited to an area around endpoints *[shown_working]*
- Visual-cue UI — Drawn icons and custom filter controls styled with Tailwind, prototyped first in Figma *[shown_working]*
- Live snow/hazard reports — User-submitted sidewalk status updates that adjust sidewalk attributes and routing *[planned]*
- Multi-city expansion — Extend beyond Boston with more precise sidewalk geometry *[planned]*

**Flow:** Open the map with Boston sidewalks displayed → Select incline, surface, width and hazard filters → Map re-renders to show matching sidewalks → Enter two locations (example: Boston Common to Newbury St) → See the accessible route minimizing distance

**Prompt:** Best First-Time Hack goes to the highest-ranked team in which at least two thirds of members are at their first hackathon; criteria cover creativity, design, impact, growth and fit with the Metropolis theme.
**Fit (explicit):** Team of first-time hackers (stated on the page); the city sidewalk-accessibility navigation addresses the Metropolis theme and a societal problem.  *(targeted: Best First-Time Hack)*
**AI:** none
**Architecture:** React + Tailwind frontend embedding Kepler.gl; Boston GeoJSON sidewalk data parsed client-side into a node/edge graph; A* routing and filters run in the browser; no backend.
**Novelty:** Targets sidewalk-level accessibility data rather than road routing; the team pivoted from a snow-hazard idea when no dataset was found.
**Scope:** small · working: Repo of about 2k lines with working filtering and routing; demo video and screenshots on Devpost. · polish: Figma prototype, logo, branded UI; performance is laggy on the full dataset by their own account.
**Claims:** Cites 12.2% of US adults with mobility disability | Cites up to 48% of sidewalks inaccessible | Parsing the full dataset takes minutes
**Gaps:** README repeats the Devpost writeup; video not viewable; what's-next section in README cut off
Sources: https://devpost.com/software/elevator-path, evidence/hack-brown-hack-brown-2026-emerald-path.json (README), https://hack-brown-2026.devpost.com/

---

