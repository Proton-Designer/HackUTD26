# HackEurope — HackEurope 2026 (1 projects)

### ZeroStrike
*HackEurope HackEurope 2026 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Overall winner / top prize (per TCD article; which city not stated); HackEurope: Grand Winner (hackeurope.com testimonial; Julian Lewandowski's site: Overall winner, HackEurope 2026)

**What it is:** Wildfire prevention platform that predicts dry-lightning ignition risk, tracks storm cells, and uses Claude agents to pick and dispatch a DJI drone. The drone carries an ESP32-triggered servo to release cloud-seeding payload over threatened terrain.
**Problem / user:** Dry lightning ignites wildfires before rain falls and response is slow; the page cites large EU wildfire damage and budget cuts. Implied users are wildfire response agencies.

**Features**
- Dry-lightning risk model — XGBoost trained on 28,000 California 2020 ignitions with ERA5 features (CAPE, dewpoint depression, humidity, slope, NDVI) *[claimed]*
- Severity grid and storm tracking — 0.05 degree composite grid; storm cells projected 6 hours ahead to detect collisions with red zones *[shown_working]*
- Claude dispatch agent — chooses fastest drone and builds intercept route from map, trajectory, fleet and imagery data *[claimed]*
- Mission-control dashboard — React and Mapbox with risk zones, storm cells, trajectories, drone positions *[shown_working]*
- GeoJSON threat API — Flask on Firebase Cloud Functions serves prioritized zones *[shown_working]*
- Android DJI mission injector — custom MSDK v5 app injects waypoints and virtual-stick commands into a DJI Mini 4 Pro *[shown_working]*
- ESP32 seeding release — servo drops payload at computed points; ESP32 polls Cloud Function each second via Firestore bus *[claimed]*
- Mock-data fallback — silent deterministic synthetic data if live polling fails *[shown_working]*

**Flow:** Hourly data layers refresh → Model scores risk and storm tracks run → Trajectory intersects a red zone → Agent selects drone and route → Dashboard writes mission to Firestore → Android app flies waypoints → Servo releases seeding payload

**Prompt:** Grand Winner: best project across all three HackEurope locations (EUR 10,000 plus Gemini credits); judged on startup potential, technical complexity and execution.
**Fit (implied):** Page does not name a prize; it presents a startup-style climate product combining ML, agents and custom drone hardware, which maps to the stated criteria of technical complexity and execution.  *(targeted: HackEurope: Grand Winner)*
**Sponsor tools:** Anthropic Claude API (autonomous dispatch decision loop over map, telemetry and imagery, core); Firebase / Firestore (message bus between dashboard, Android app and ESP32, core)
**AI:** XGBoost classifier for ignition risk on ERA5 features; Claude agent with tool access to threat map, storm trajectories, fleet telemetry and satellite imagery makes dispatch decisions.
**Architecture:** Python/Flask scoring engine on Cloud Functions -> GeoJSON; React/Mapbox dashboard; Firestore bus to Android DJI app and ESP32 servo; synthetic data provider to be swapped for NOAA, FIRMS, Sentinel.
**Novelty:** Combines weather ML, LLM dispatch agent and bespoke physical payload release on a consumer drone in one 30-hour build.
**Scope:** large · working: Live site zerostrike.live, YouTube demo, five screenshots; page says drone integrated, though current feeds are synthetic. · polish: Multi-layer Mapbox dashboard and hardware integration; no field test of seeding reported.
**Claims:** 78% precision on held-out data | Dispatch route generated in under three seconds | Built in 30 hours | Real ERA5 features roughly doubled fire-weather signal importance
**Gaps:** repo julianlewandowski/zerostrike not read; no evidence file
Sources: https://devpost.com/software/zerostrike, https://hackeurope.devpost.com/

---

