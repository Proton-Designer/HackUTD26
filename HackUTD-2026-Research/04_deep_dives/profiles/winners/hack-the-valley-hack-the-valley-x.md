# Hack the Valley — Hack the Valley X (3 projects)

### Dream House
*Hack the Valley Hack the Valley X · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 2nd Place Prize [2nd]

**What it is:** Tool that turns a rough 2D floor-plan sketch into a formal plan, detects furniture and walls, then builds a furnished 3D Unity scene from generated 3D assets.
**Problem / user:** Interior designers spending hours converting 2D plans into 3D visualizations that need CAD skills.

**Features**
- Sketch to floor plan — Gemini image model (Nano Banana) formalizes a sketch; endpoint returns a PNG. *[claimed]*
- Furniture detection — FastSAM segments objects and GPT-4o-mini Vision classifies types with positions, sizes and reasoning. *[shown_working]*
- Plan revision — Natural-language instructions revise an annotated floor plan. *[shown_working]*
- Photorealistic render — Endpoint generates a realistic image from the plan. *[shown_working]*
- Wall detection — CubiCasa5K-based walls mapped for the scene. *[claimed]*
- 3D asset matching — Trellis-generated model library matched to detected furniture. *[claimed]*
- Unity export — Scene endpoint exports furniture JSON for Unity. *[shown_working]*

**Flow:** Sketch a floor plan → System formalizes it → Edit the layout → Press render → Unity shows the furnished 3D space

**Prompt:** Hack the Valley X overall second place (Apple Watch SE plus Nord); no track text read for edition X.
**Fit (none):** No stated prize targeting; general-pool entry.  *(targeted: 2nd Place Prize [2nd])*
**AI:** Gemini image generation for sketches, FastSAM and SAM segmentation, GPT-4o-mini vision classification, Trellis 3D generation.
**Architecture:** Next.js frontend, FastAPI backend with floorplan, image and scene routers, Unity renders scenes from exported JSON and assets.
**Novelty:** Chains sketch cleanup, segmentation, text-to-3D assets and Unity assembly into one pipeline.
**Scope:** medium · working: Backend README with endpoint docs and tests folder; Devpost shows a screenshot but no video. · polish: Detailed API README; no demo link.
**Claims:** 3D interiors in seconds instead of hours (unmeasured)
**Gaps:** Edition X prize text not fetched; README mentions OpenAI while Devpost names Gemini and SAM; both recorded; Unity project not in README; No demo video
Sources: https://devpost.com/software/dreamhouse-vp4cfn, https://github.com/willzeng274/dreamhouse, evidence/hack-the-valley-hack-the-valley-x-dream-house.json

---

### NavSense
*Hack the Valley Hack the Valley X · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 3rd Place Prize [3rd]

**What it is:** A pair of ESP32-based smart gloves that receive turn-by-turn walking directions from an iOS app over Bluetooth Low Energy and play them back as distinct vibration patterns, with a voice agent for route setup and siren detection for safety.
**Problem / user:** Blind/low-vision and Deaf/hard-of-hearing pedestrians, plus runners and cyclists, who cannot safely rely on audio directions or watching a phone screen while moving.

**Features**
- Haptic turn cues in two gloves — App connects to both gloves over BLE and sends ASCII commands that trigger vibration motors with patterns for left, right, forward, pause and reroute. *[shown_working]*
- Route parsing from Google Maps — Node/Express server calls Google Maps Directions, returns legs and steps; each maneuver maps to a pattern, fired in advance and at execution. *[shown_working]*
- Voice agent for navigation — ElevenLabs speech with a Gemini model handles start, destination, travel mode, rerouting and quick questions via webhooks. *[claimed]*
- Siren and noise detection — On-device ML classifier (TensorFlow Lite / Core ML listed) detects sirens, alerts through the gloves and prompts the user to pause. *[claimed]*
- Glove power and status LEDs — USB-C rechargeable 18650 cell with BMS; LEDs show pairing, battery and error states mirroring haptic states. *[shown_working]*
- Manual route and BLE test screens — App has manual route entry, settings, active route and map views, Bluetooth pairing and a Bluetooth terminal for testing. *[shown_working]*
- 3D-printed enclosure — Custom printed box holds ESP32, battery and motor-LED circuitry on each glove. *[shown_working]*
- Trusted-contact live tracking — Friends view location and route on a web dashboard and check in if the user stops long. *[planned]*

**Flow:** Pair both gloves with the iOS app over Bluetooth → Give start, destination and mode by voice or enter the route manually → Server fetches the Google Maps route and splits it into steps → While walking, upcoming maneuvers trigger matching vibration patterns on the correct glove → LEDs show connection, battery and errors → A detected siren triggers a glove alert and a pause prompt → Ask the voice agent to reroute or answer questions

**Prompt:** not public / not found
**Fit (none):** Overall placement; no track text found. README frames accessibility and lists UN SDGs 3, 9, 10 and 11 as supported goals.  *(targeted: 3rd Place Prize)*
**AI:** ElevenLabs voice plus a Gemini model for intent, follow-ups and reroutes through webhooks; a TensorFlow/Core ML noise classifier for siren detection. No evaluation numbers given.
**Architecture:** Expo/React Native iOS app talks BLE to two ESP32 gloves (Arduino C++), and to a small Express server that wraps Google Maps Directions; voice agent runs on ElevenLabs with Gemini via webhooks.
**Novelty:** Full custom wearable hardware (two gloves, battery, BMS, printed enclosure) combined with a voice agent and siren detection; touch-only navigation aimed at both blind and Deaf users.
**Scope:** medium · working: Devpost says prototype tested on real devices; demo video exists; repo has app, server and TF folders (about 4.8k LOC). · polish: Custom printed enclosures, LEDs and charging circuit; no tests or CI.
**Claims:** Working haptic navigation gloves tested on real devices | First iOS and BLE project for the team | ML siren detection triggers glove alert
**Gaps:** No official Hack the Valley X prize text fetched (devpost slug failed); Devpost says React Native while built-with tags are generic; README says React Native iOS; No accuracy or latency numbers for siren detection
Sources: https://devpost.com/software/navsense-jp2e7z, evidence/hack-the-valley-hack-the-valley-x-navsense.json (README of Ibrahimkasiim1/HackthevalleyX)

---

### Plant Hopper
*Hack the Valley Hack the Valley X · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 1st Place Prize [1st]

**What it is:** A two-axis servo turret with a tunable water gun that finds individual plants through AprilTag markers on a camera feed, aims with PID and trigonometry, and waters each one. A Firebase-backed Next.js web app sends remote commands and shows soil moisture.
**Problem / user:** People who water plants and want to avoid the roughly half of watering water the page says is wasted by uniform sprinklers; hints at greenhouse and multi-plant use.

**Features**
- AprilTag plant localization — Camera detects a tag per plant and computes distance and offset; lens distortion corrected with a YAML calibration file. *[shown_working]*
- Two-axis turret aiming — CAD-designed pitch and base-rotation turret aligned by PID plus trigonometric shot-angle calculation on an Arduino. *[shown_working]*
- Servo-controlled water gun — Custom tunable water gun actuated by servos to water each plant individually. *[shown_working]*
- Remote web commands — Web app offers Water now, Run plant scan and Get moisture status; commands pass through Firebase to the robot. *[shown_working]*
- Soil moisture and image publishing — Robot pushes moisture sensor readings and CV snapshots to Firebase for display in the dashboard. *[shown_working]*
- Multithreaded Python controller — One Python process runs vision, Arduino serial, Firebase reads/writes and timing concurrently. *[shown_working]*
- Optimized watering schedules — Described as scheduling per plant using moisture data; details not given. *[claimed]*
- Analytics, reminders, plant profiles — Listed as future UI additions with DIY kits and wheeled turrets. *[planned]*

**Flow:** Open the web app from any device → Press Water now, Run plant scan or Get moisture status → Firebase relays the command to the Python controller → Camera finds AprilTag-marked plants and the turret aligns → Water gun fires at the chosen plant → Moisture data and snapshots appear back in the dashboard

**Prompt:** not public / not found
**Fit (none):** Overall prize; no track text found. Pitches water-waste reduction through per-plant targeting.  *(targeted: 1st Place Prize)*
**AI:** Classical computer vision (AprilTag detection with camera calibration) and PID control; no learned model mentioned.
**Architecture:** Camera and Arduino turret driven by a threaded Python controller that reads Firebase commands and writes moisture and images; Next.js app on Vercel reads and writes the same Firebase.
**Novelty:** Individual plant targeting via fiducial tags and a shooting turret, rather than zone sprinklers; hardware, firmware, vision and cloud dashboard all built in one weekend.
**Scope:** medium · working: Demo video in README and Devpost; repo has Arduino, CV, Main and frontend folders (about 9.4k LOC incl. frontend). · polish: Custom CAD turret, deployed web UI with charts; no tests.
**Claims:** Goal of 0% water waste | Cites 50% of plant watering water is wasted | Real-time remote control with no local setup
**Gaps:** No official Hack the Valley X prize text fetched; No measured water savings or accuracy figures; Scheduling logic not described in detail
Sources: https://devpost.com/software/plant-hopper, evidence/hack-the-valley-hack-the-valley-x-plant-hopper.json (README of jello-2/PlantHopper)

---

