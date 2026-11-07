# Niantic Spatial (HackUTD 2026 - Bronze sponsor)

Entity assumed: Niantic Spatial, Inc. (San Francisco; spun out of Niantic in May 2025), NOT Niantic Inc. (Scopely now owns the games). Reason: the sponsor name is "Niantic Spatial" and it is the only entity by that name. [verified, Wikipedia]

## 1. Who they are / what they build now
- AI + spatial computing company building geospatial "world models" (Large Geospatial Model, trained on 30B+ posed images) for robotics, defense, utilities, AR, construction, inspection. [verified: https://en.wikipedia.org/wiki/Niantic_Spatial]
- Products: Scaniverse (phone/360/drone capture -> Gaussian splats, meshes, VPS maps; USDZ export added Jul 2026), VPS / VPS2 (centimeter-level localization, works in GPS-denied areas), semantic understanding (200+ object types; GeekWire said "later this year"), Niantic Spatial SDK (NSDK). Also keeps Ingress and Peridot. [verified, Wikipedia + GeekWire]
- 8th Wall is being shut down (hosted services end early 2027; code mostly open-sourced). Don't build on it. [verified, Wikipedia]
- CEO Inhi Cho Suh since Mar 2026; John Hanke exec chairman. [verified]

## 2. HackUTD 2026 prize/challenge
- Event: Nov 7-8, 2026, UT Dallas ECSW. Niantic Spatial listed as Bronze sponsor on https://zeroday.hackutd.co. [verified, fetched]
- Challenge text: NOT PUBLIC. Site says "This year's challenge tracks will be announced once hacking starts." Prize details also not public. No Devpost/MLH listing found. [verified absence on the site; Devpost not located]

## 3. Tooling for 36 hours
- NSDK (release 4.1.0): VPS localization, anchors (persistent), VPS coverage API, mesh download API, location drift mitigation. Platforms: Unity (6000.0.74f1), Swift (iOS), Kotlin (Android). Web not listed in release notes. Meta Quest 3 support restored (pin OpenXR 1.15.1). [verified: https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/ and /docs/nsdk/release_notes/]
- Signup: Scaniverse Web (scaniverse.nianticspatial.com) -> "New" experience (NSDK doesn't work with Classic) -> sign up w/ email or Google -> create Organization. Lightship.dev is decommissioned. [verified: https://www.nianticspatial.com/docs/nsdk/create_account] Access token step is on the "Set up the SDK" page, not confirmed by me. [unverified]
- Free tier: GeekWire says a free tier covers basic scanning and positioning; paid plans add 360 camera support etc. Quotas are per org, monthly credits, top-ups $10/$20/$50. [verified: GeekWire, https://www.nianticspatial.com/docs/scaniverse/quickstart]. Exact free limits: not found.
- Scaniverse app: free iOS/Android. Android scan/upload/localization testing added in 4.1.0.
- Public VPS locations only cover mapped places; for a hackathon, scan a private location at UTD with Scaniverse and test localization (needs time to process). [inference from docs]
- Docs root: https://www.nianticspatial.com/docs/nsdk/

## 4. Prior hackathon sponsorships
- MOLTEN spatial hackathon (Inglewood, CA; Roboflow, Auki, Niantic Spatial): Niantic gave one month Scaniverse Pro per participant; no Niantic-specific prize listed. https://luma.com/5jo47m0d [verified]
- Niantic Studio Real-World Challenge (online, $15k pool; judges cited creativity, innovation, technical excellence). Winners: Puzzle AR, Point Drifters (multiplayer VPS racing), Toy Trek and Gaussian Splat Drive (splat games), Dresden Mystery (location escape room), Lucky Fountain (VPS coin toss). https://info.nianticspatial.com/blog/meet-the-winners-niantic-studio-real-world-challenge [verified]
- Scaniverse #SplatYourWorld (Jul 2026): categories Industrial, Natural (incl. GPS-denied), Urban; paid subscribers only. https://radiancefields.com/niantic-spatial-opens-the-scaniverse-splatyourworld-challenge [verified]
- Past Niantic Spatial prompts at HackUTD or Devpost hackathons: none found. [unverified]
- Dev Program partners exist (e.g., Sugar Creative). [verified listing only]

## 5. What they likely value (inference)
Evidence: their own contest judging (creativity, innovation, technical excellence); marketing emphasis on robotics/industrial/utilities and GPS-denied use. Inference: real use of VPS/Scaniverse (not generic AR gimmick), a working live demo at a real place, and an enterprise/physical-AI story.
Project directions [all inference]:
1. Scan a UTD building with Scaniverse, localize with VPS, build indoor wayfinding / accessibility navigation app (Kotlin wayfinding guide exists in 4.1.0).
2. Persistent AR anchors for facility inspection or maintenance notes (industrial/utilities framing), possibly with an LLM summarizing reports tied to anchors.
3. Gaussian-splat digital twin of a space plus an AI agent that answers questions about it (semantics + splat viewer), e.g., campus tour or emergency-prep walkthrough.

## 6. Questions for the booth
- What is the actual challenge and prize? Which APIs must be used to qualify?
- Is there a hackathon org/credit code for NSDK and Scaniverse Pro? Free-tier quotas and processing latency for new scans?
- Is the access token flow ready for new orgs today? Any UTD locations already VPS-mapped?
- Web (WebXR/three.js) support for VPS2 or only Unity/Swift/Kotlin? Is the semantics API available now?
- Loaner devices? Judging criteria and who judges?

## Sources
- https://zeroday.hackutd.co (verified)
- https://hackutd.co (verified; past sponsors list only)
- https://en.wikipedia.org/wiki/Niantic_Spatial (verified)
- https://www.geekwire.com/2026/from-pokemon-go-to-physical-ai-niantic-spatial-unveils-its-global-3d-mapping-platform/ (verified)
- https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/ (verified)
- https://www.nianticspatial.com/docs/nsdk/release_notes/ (verified)
- https://www.nianticspatial.com/docs/nsdk/create_account (verified)
- https://www.nianticspatial.com/docs/scaniverse/quickstart (verified)
- https://www.nianticspatial.com/university-partner-with-us (verified; no credits info)
- https://luma.com/5jo47m0d ; https://info.nianticspatial.com/blog/meet-the-winners-niantic-studio-real-world-challenge ; https://radiancefields.com/niantic-spatial-opens-the-scaniverse-splatyourworld-challenge (verified)
