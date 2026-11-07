# HackNYU: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2025

### Dristhi  (2025)

- **Prizes:** Track: Security and Privacy (sponsored by Nord Security) [unknown]  (tier: sponsor_winner)
- **Pitch:** Smart bag for visually impaired users with an emergency-alert button, posture and temperature sensing, webcam plus ultrasonic obstacle detection and spoken guidance via a web app.
- **Problem / user:** Visually impaired people face obstacles and safety risks while moving around and need hands-free alerts and guidance. / visually impaired individuals
- **Domain / idea type:** accessibility + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; speech_or_voice
- **Stack:** langs Python; C++; frontend ; backend Python; db ; hosting 
- **Tech/APIs:** OpenCV (framework, core); MediaPipe (ai_model, core); HC-SR04 ultrasonic sensor (hardware_part, core); pyttsx3 (other, supporting); geopy (other, supporting)
- **Sponsor APIs:**  | fit: Won the Security and Privacy track sponsored by Nord Security; the writeup uses no Nord product and frames the work as personal-safety hardware (emergency alerts and obstacle warnings).
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims True (Cites about 245 million people with visual impairments as the motivating population.)
- **Notes:** Combines OpenCV/MediaPipe person and object detection with an HC-SR04 ultrasonic sensor for distance validation and pyttsx3 voice output; team reported intermittent ultrasonic sensor failures and noisy analog data.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/dristhi)

### FirstWave  (2025)

- **Prizes:** Track: Security and Privacy (sponsored by Nord Security) [unknown]  (tier: sponsor_winner)
- **Pitch:** Spear-phishing simulation platform where GPT-based agents build fake LinkedIn personas from public data, engage employees, and report vulnerabilities in a dashboard.
- **Problem / user:** Standard phishing training does not replicate modern targeted social engineering, leaving the human firewall untested. / corporate security and training teams
- **Domain / idea type:** safety_security + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs JavaScript; frontend Next.js; React; backend Node.js; Puppeteer; db MongoDB; hosting 
- **Tech/APIs:** OpenAI GPT-4o (ai_model, core); Puppeteer (framework, core); MongoDB (database, supporting); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Won the Security and Privacy track sponsored by Nord Security with a phishing-awareness simulator; the writeup uses no Nord product and targets the track theme (social-engineering defense).
- **Repo:** public, commits 29 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live none, screenshots 19, writeup medium, impact claims False
- **Notes:** Puppeteer-driven agents run LinkedIn-style engagement with campaign setup and post-campaign analysis reports; the writeup stresses consent protocols but gives no detail on enforcement.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/firstwave-5wbld1) | [GitHub](https://github.com/Laphatize/firstwave)
