# HackUNT — HackUNT 2024 (3 projects)

### Meet+
*HackUNT HackUNT 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner CBRE

**What it is:** A small FastAPI web tool where a user pastes a meeting transcript and gets back a summary, a list of action items and calendar-style event details generated with Gemini.
**Problem / user:** People running or attending virtual meetings, such as teams, who want automatic notes and task assignment; creator cites internship and TA experience.

**Features**
- Transcript submission via web page — HTML front end accepts a pasted meeting transcript. *[unclear]*
- Action item extraction — Gemini-based analysis lists specific tasks discussed. *[claimed]*
- Meeting summary — Generates a concise summary of key points from the transcript. *[claimed]*
- Event detail generation — Produces summary, location such as Google Meet, purpose, start and end with time zone, and attendees. *[claimed]*

**Flow:** Open the web page → Paste a meeting transcript → Receive action items, summary and event details

**Prompt:** CBRE challenge at HackUNT 2024: build an AI/ML solution making workplaces and buildings more efficient, adaptable and user-friendly, covering space use, tenant satisfaction and operations.
**Fit (implied):** Positions meeting transcripts to workflows as workplace efficiency; no explicit tie to buildings or tenants stated.  *(targeted: CBRE)*
**AI:** Gemini processes the transcript to extract action items, summary and event fields; usage details not described on the page.
**Architecture:** Python FastAPI backend with an HTML/CSS front end template; Google APIs mentioned; creator says front end and back end were not connected in time.
**Novelty:** Solo-built meeting-notes generator; generic idea with weak link to the building-focused sponsor prompt.
**Scope:** tiny · working: 9 files, about 700 LOC; screenshots labeled front end and testing; author says front/back end were not connected. · polish: No README, demo, video or tests.
**Claims:** Turns virtual meetings into organized, efficient workflows | Saves time through automated note-taking and task assignment
**Gaps:** no README in repo; Gemini usage not described; front-end/back-end link incomplete
Sources: https://devpost.com/software/meet-gqybo1, https://github.com/SameerK73/Meet-

---

### Propertunity
*HackUNT HackUNT 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner CBRE

**What it is:** A property-management web app with separate manager and tenant portals: tenants file maintenance tickets via a Gemini chatbot or SMS, and managers see ML-based maintenance forecasts and opportunity-cost analysis to prioritize repairs.
**Problem / user:** Property managers lacking data to prioritize maintenance and cost of delays, and tenants frustrated by after-hours ticket delays; built for the CBRE challenge.

**Features**
- Role-based dashboard routing — Email domain decides manager versus tenant dashboard; any @CBRE.com email gets the manager portal. *[shown_working]*
- Maintenance prediction — ML forecasts needs using location factors such as weather and natural disaster risk from WeatherAPI. *[claimed]*
- Opportunity cost analysis — Quarterly cost forecasts help rank maintenance categories. *[claimed]*
- Tenant ticket interface — Tenants submit and track maintenance requests stored in MongoDB. *[shown_working]*
- Gemini chatbot ticketing — 24/7 bot creates, categorizes and prioritizes tickets in real time. *[claimed]*
- Twilio SMS messaging — Tenants send messages from their phone through Twilio. *[claimed]*
- Smart notifications — Alerts for urgent issues and ticket updates. *[claimed]*

**Flow:** Log in (Firebase or Auth0) → Land on manager or tenant dashboard by email domain → Tenant chats with bot to open a ticket → Manager reviews suggestions and cost forecasts

**Prompt:** CBRE challenge at HackUNT 2024: build an AI/ML solution making workplaces and buildings more efficient, adaptable and user-friendly, addressing space use, tenant satisfaction, operations.
**Fit (explicit):** Directly targets tenant and property-manager problems with predictive maintenance, cost prioritization and 24/7 tenant ticketing, using CBRE branding.  *(targeted: CBRE)*
**AI:** Gemini chatbot creates and classifies tickets; unspecified ML models forecast maintenance and opportunity cost from weather and disaster-risk inputs.
**Architecture:** Next.js and React/TypeScript app on Vercel with MongoDB ticket store, Gemini API, Twilio SMS, WeatherAPI; auth moved from Auth0 to Firebase per page.
**Novelty:** Combines tenant chatbot, SMS and predictive cost analysis in one two-sided portal styled to the sponsor's branding.
**Scope:** small · working: Deployed on Vercel with demo logins; about 1.4k LOC, 30 files. · polish: README with setup and login notes; CBRE-branded UI; no tests or video.
**Claims:** Microservices design expected to save server costs | Accurate opportunity cost predictions from multiple data points
**Gaps:** ML models not described, likely mocked; no video
Sources: https://devpost.com/software/propertunity, https://github.com/UsmanS2/realhackUNT24

---

### UtiliTrack
*HackUNT HackUNT 2024 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner CBRE

**What it is:** A concept dashboard for businesses to monitor energy use, detect waste and automatically schedule HVAC and maintenance using sensor feedback and machine learning; repo is a small React app.
**Problem / user:** Business owners and facilities teams losing money on inefficient energy use; cites $370 billion annual US energy waste and a restaurant losing $3,000-5,000 monthly on air conditioning.

**Features**
- Real-time energy consumption tracking — Reads usage data from sensors and displays patterns. *[claimed]*
- Waste pattern detection — Algorithms flag inefficiencies in consumption. *[claimed]*
- Automated HVAC scheduling — Runs systems only when needed using sensor feedback and dynamic power adjustment. *[claimed]*
- Automated maintenance scheduling — Predictive algorithms schedule upkeep before breakdowns. *[claimed]*
- ML setting optimization — Learns from usage data to tune settings. *[claimed]*
- Owner dashboard with feedback tracking — Single React dashboard for efficiency and customer feedback. *[unclear]*

**Flow:** Owner opens dashboard → Reviews energy consumption and waste patterns → Lets automation adjust schedules or overrides it

**Prompt:** CBRE challenge at HackUNT 2024: build an AI/ML solution making workplaces and buildings more efficient, adaptable and user-friendly, addressing space use, tenant satisfaction, operations.
**Fit (implied):** Addresses building operational efficiency through energy monitoring and predictive maintenance.  *(targeted: CBRE, HackUNT third place)*
**AI:** Machine learning claimed to optimize equipment settings and predict maintenance from usage data; no model details given.
**Architecture:** React front end with Firebase and Python back end; sensor data feed unspecified. Repo contains a single React app of about 600 LOC.
**Novelty:** Energy-waste framing with a quantified problem statement; implementation is a thin front end with most capabilities described rather than demonstrated.
**Scope:** tiny · working: 32 files, about 589 LOC, React scaffold with test setup; no demo or video. · polish: Four uncaptioned screenshots; README is only a title.
**Claims:** Potentially saving $111 billion in the US | Detected and prevented unnecessary energy use in real-scenario tests
**Gaps:** backend/ML code not visible in evidence; claims unverified
Sources: https://devpost.com/software/utilitrack, https://github.com/Sid-Myla/HackUNT2024

---

