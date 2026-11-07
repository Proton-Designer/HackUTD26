# HackIllinois — HackIllinois 2025 (1 projects)

### Recycle Tracker
*HackIllinois HackIllinois 2025 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 2nd Place Overall [2nd]

**What it is:** An Android (Kotlin) app plus Cloudflare Workers backend that rewards users with points for photographed recycling, using image hashing, EXIF/GPS metadata and device fingerprinting to block fraud, and offers hotspot data to NGOs and businesses.
**Problem / user:** People lacking incentive to recycle, plus organizations (NGOs, governments, brands) wanting trustworthy recycling data; fraud in reward programs is the stated obstacle.

**Features**
- Recycling photo submission and points — User uploads images; verified submissions earn points redeemable at local businesses. *[claimed]*
- Duplicate-image detection — Background Python server hashes images and compares against stored hashes table. *[claimed]*
- One device one account — FingerprintJS Pro visitor ID checked on signup and logged with OS, IP and location. *[claimed]*
- EXIF and GPS verification — Background task extracts metadata for location checks and hotspot mapping; README marks parts as in progress. *[planned]*
- Secure uploads to cloud storage — Signed URLs for Google Cloud Storage uploads. *[claimed]*
- Email notifications — SendGrid emails on submission results, points and reminders. *[claimed]*
- Insights for NGOs and brands — Hotspot maps and product-level analysis said to guide bin placement and ESG reporting. *[claimed]*
- Typed REST API with JWT auth — Hono on Cloudflare Workers, Zod validation, Better Auth, Drizzle over Neon Postgres, documented on Apidog. *[shown_working]*

**Flow:** Install Android APK → Sign up; device fingerprint is bound to account → Photograph and upload recycling → Backend stores image and runs hash/EXIF checks → Receive points and email → Redeem points at local vendors

**Prompt:** not public / not found
**Fit (none):** Overall prize with no specific prompt; project listed for GreenPioneers-style sustainability theme.  *(targeted: 2nd Place Overall)*
**AI:** Devpost claims AI image verification and AI product recognition, but no model is named; repo evidence shows hashing and EXIF processing in a Python worker (OpenCV/PIL, partly marked unfinished).
**Architecture:** Kotlin Android app calls Hono API on Cloudflare Workers (Neon via Drizzle), which signs GCS uploads and triggers a Leapcell Python task for hashing and metadata, then updates points and sends SendGrid email.
**Novelty:** Anti-fraud emphasis (device fingerprint plus image hashing) on a recycling reward app, and a second customer segment for aggregated recycling data.
**Scope:** medium · working: Deployed API URL, APK link and API docs; monorepo of apps and packages, small LOC (about 1.7k) and no tests. · polish: Detailed README architecture; no video; some items marked work in progress.
**Claims:** One device, one account enforced via visitor ID | Hash comparison blocks duplicate uploads | 30-day JWT sessions
**Gaps:** no overall-prize prompt text; AI model unspecified; no video
Sources: https://devpost.com/software/recycle-tracker, https://github.com/jacksonkasi0/Reward-Based-Recycling-Tracker

---

