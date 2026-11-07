# Hack the Valley: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Hack the Valley 11

### Premiere  (Hack the Valley 11)

- **Prizes:** 3rd Place Prize [3rd]; Hack the Valley x School of Cities [unknown]  (tier: overall_top3)
- **Pitch:** Raspberry Pi robot car carrying an iPhone scans abandoned properties and builds a browsable 3D reconstruction for redevelopment assessment.
- **Problem / user:** Assessing abandoned or deteriorating buildings for redevelopment is unsafe and hard without understanding their structure. / engineers, developers and municipalities
- **Domain / idea type:** housing_real_estate + civic_legal / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_ios; web / True / False
- **Stack:** langs Python; Swift; HTML; CSS; frontend Three.js; Spark.js; Vite; SwiftUI; backend FastAPI; db ; hosting 
- **Tech/APIs:** Raspberry Pi (hardware_part, core); ARKit (framework, core); COLMAP (other, core); Brush (other, core); Three.js (framework, core); Spark.js (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:**  | fit: Also won Hack the Valley x School of Cities; page frames project around urban redevelopment of abandoned properties.
- **Repo:** public, commits 18 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Robot car streams iPhone ARKit capture; COLMAP/Brush Gaussian-splat reconstruction viewed in browser with Three.js and Spark.js; queue lists a different repo name than the page link.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_used; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/estate-o-bot) | [GitHub](https://github.com/Vedthakar/HTV11.git)

### Pyrosense  (Hack the Valley 11)

- **Prizes:** 1st Place Prize [1st]  (tier: overall_top3)
- **Pitch:** Helmet-mounted sensing system giving firefighters a live map of building layout, teammate positions and predicted gas hazards.
- **Problem / user:** Firefighters in smoke-filled unfamiliar buildings lack situational awareness of structure and hazardous gas spread. / firefighters
- **Domain / idea type:** safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / predictive_ml
- **Stack:** langs Python; frontend ; backend FastAPI; ROS2; db TimescaleDB; hosting Vultr; Tailscale
- **Tech/APIs:** Raspberry Pi (hardware_part, core); LiDAR (hardware_part, core); ROS2 (framework, core); SLAM (other, core); TimescaleDB (Tiger Data) (database, core); Vultr (cloud, supporting); Tailscale (other, supporting); Foxbridge (other, unclear)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims False
- **Notes:** Combines helmet sensor unit with LiDAR SLAM on ROS2/Raspberry Pi, time-series gas data in TimescaleDB, and past/present/predicted hazard view.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_used; ai_types; sponsor_apis_used; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/pyrosafe)

### Soundscape  (Hack the Valley 11)

- **Prizes:** 2nd Place Prize [2nd]  (tier: overall_top3)
- **Pitch:** Captioning tool that adds environmental sound descriptions to videos, via a dashboard upload or a YouTube extension.
- **Problem / user:** Standard captions omit non-speech sounds like alarms or glass breaking, leaving hard-of-hearing viewers without context. / deaf and hard-of-hearing viewers
- **Domain / idea type:** accessibility + creative_media / creative_tool
- **Platforms / hardware / AI:** web; browser_extension / False / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Python; db ; hosting 
- **Tech/APIs:** CLAP (ai_model, core); PANNs (ai_model, core); SigLIP (ai_model, core); Gemini (ai_model, supporting); Claude (ai_model, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 145 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Multi-step pipeline: SigLIP scene recognition, CLAP/PANNs sound detection, LLM caption writing, plus an evaluation step; delivered as dashboard and browser extension.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; tech_items.depth; writeup_length
- **Links:** [Devpost](https://devpost.com/software/sound-thing) | [GitHub](https://github.com/soundthing/Soundscape)


## Hack the Valley X

### Dream House  (Hack the Valley X)

- **Prizes:** 2nd Place Prize [2nd]  (tier: overall_top3)
- **Pitch:** Turns a rough 2D floor-plan sketch into a cleaned-up layout and then an editable 3D furnished space.
- **Problem / user:** Designers spend hours converting 2D floor plans into 3D visuals, which normally needs CAD skills. / interior designers and home planners
- **Domain / idea type:** housing_real_estate + creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / vision; generative_media
- **Stack:** langs Python; TypeScript; CSS; frontend Next.js; Unity; backend FastAPI; db ; hosting 
- **Tech/APIs:** Gemini (Nano Banana) (ai_model, core); Segment Anything (SAM) (ai_model, core); CUDI casa 5K (ai_model, unclear); Unity (framework, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 30 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Pipeline chains Nano Banana image generation, SAM furniture segmentation, CUDI casa 5K and Unity rendering behind Next.js and FastAPI.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; platforms; tech_items.depth
- **Links:** [Devpost](https://devpost.com/software/dreamhouse-vp4cfn) | [GitHub](https://github.com/willzeng274/dreamhouse)

### NavSense  (Hack the Valley X)

- **Prizes:** 3rd Place Prize [3rd]  (tier: overall_top3)
- **Pitch:** Pair of smart gloves that give turn-by-turn walking directions through vibration patterns, paired with a phone navigation app.
- **Problem / user:** Audio and screen directions occupy hearing and sight, which is risky for blind, low-vision or deaf pedestrians. / blind, low-vision and deaf or hard-of-hearing pedestrians
- **Domain / idea type:** accessibility + mobility_transport / hardware_gadget
- **Platforms / hardware / AI:** hardware; mobile_cross / True / None
- **Stack:** langs TypeScript; JavaScript; C++; frontend React Native; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Bluetooth Low Energy (other, core); Google Maps (maps_geo, core); ElevenLabs (ai_model, unclear); TensorFlow Lite (framework, unclear); React Native (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 41 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots None, writeup long, impact claims False
- **Notes:** Each glove has an ESP32 talking BLE to a React Native app; distinct vibration patterns encode left, right, forward, pause and recalculate; Google Maps routing.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_used; n_screenshots; tech_items.depth
- **Links:** [Devpost](https://devpost.com/software/navsense-jp2e7z) | [GitHub](https://github.com/Ibrahimkasiim1/HackthevalleyX)

### Plant Hopper  (Hack the Valley X)

- **Prizes:** 1st Place Prize [1st]  (tier: overall_top3)
- **Pitch:** Servo turret with a water gun that locates each plant via AprilTags and waters it individually, controlled from a web dashboard.
- **Problem / user:** Sprinklers waste much water and treat all plants the same regardless of their needs or schedules. / gardeners and plant growers
- **Domain / idea type:** sustainability_climate + retail_consumer / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / False
- **Stack:** langs Python; C++; frontend Next.js; React; Tailwind; backend ; db Firebase; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); AprilTag (other, core); Servos (hardware_part, core); Firebase (database, supporting); Next.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 130 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 3, writeup medium, impact claims True (States sprinklers waste up to 50% of water used.)
- **Notes:** Custom CAD 2-axis turret using AprilTag detection, PID alignment and trigonometry to aim; Arduino serial link plus Firebase-synced web app.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; writeup_length
- **Links:** [Devpost](https://devpost.com/software/plant-hopper) | [GitHub](https://github.com/jello-2/PlantHopper)
