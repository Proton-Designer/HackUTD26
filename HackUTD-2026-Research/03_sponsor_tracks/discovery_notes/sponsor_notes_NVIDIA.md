# NVIDIA sponsor discovery notes

## Approaches
- Devpost hackathon site per event: prize list on main page, /project-gallery?winners=true, then each winner project page for prize badges (in-page fetch from a Chrome tab).
- Devpost JSON hackathon API (devpost.com/api/hackathons?search=...): found NVIDIA-hosted/co-hosted events (nemoclaw, nvidia-aws, hpaistudio, comfyui-nvidia-hackathon-25, arangodbhackathon, nebiusglobalaihackathon).
- Scanned ~680 ended Devpost hackathons (>=250 registrants, 2025-2026 dates; API listing stopped near page 101 of recently-added order, so coverage is partial) for "NVIDIA/Brev/Nemotron" on the main page: 38 hits, most only judge bios. Real NVIDIA prizes: TreeHacks 2025/2026, HackUTD 2025, SteelHacks XIII, Knight Hacks IX, DataHacks 2026, ShellHacks 2025.
- Devpost software search JSON (query=nvidia..., winner=true): 85 projects, none carried NVIDIA-named prize badges.
- WebSearch/WebFetch: NVIDIA forum/blog recaps (NeMo Agent Toolkit, Cosmos Cookoff), Nota AI blog (Nemotron Seoul), UCSC news (Hack-a-Claw), GTC hackathon page.

## Notes
- HackUTD 2025 NVIDIA page has no challenge text, only prizes (Rules/Resources/Updates checked). 3 winners (Alchemetrics, DataDriver, Toyotron) all already analyzed; no placement stated.
- HackUTD 2024 (hackutd-ripple), HackUTD IX/X, Cal Hacks 11/12, HackMIT, HackGT 11/12, Hack the North 2024/25, PennApps XXV/XXVI, HackPrinceton 2025, HackHarvard 2025, TAMUhack 2025, HackTX 2025, HackIllinois 2025/26, LA Hacks 2025, UofTHacks 13: main pages show no NVIDIA prize (only partial check of main page text).
- Low-confidence rows (NVIDIA hardware is only the prize item, no NVIDIA challenge): SBU Hacks 2026 A.U.R.A., HackTX 2026 ARcher. Also seen but not scanned for winners: UB Hacking Fall 2025 (Best AI/ML Hack prize = Jetson), HackPrinceton Fall 2025 (Best Hardware Hack = Jetson), MHacks 2025 (Overdrive = Jetson), DeveloperWeek 2026 (Linode prize = Jetson), DevNetwork AI/ML Hack 2026 (Crusoe challenge uses Nemotron, DGX Spark 1st).
- Winners not Devpost-listed: ComfyUI x NVIDIA RTX Hackathon (winners gallery empty), GTC San Jose 2026 hackathons (no winners published), Hack@URI (no NVIDIA challenge), Nebius x NVIDIA Global AI Hackathon (results due ~Jan 2027), Brunel/Lboro NVIDIA hackathon (UK, project not named), NVIDIA-India Agentic AI Hackathon 2026 (only a LinkedIn lead), HackAI Dell+NVIDIA (ended Oct 2 2024, out of window).
- event dates for Agentic AI Unleashed from Devpost API: Oct 13 - Nov 4 2025. TreeHacks 2026 and DubHacks etc dates left null if not seen.

## Leads left
- Rescan with lower registration threshold and the remaining API pages (page 101+); scan winners for DevNetwork AI/ML 2026, UB Hacking 2025, MHacks 2025, HackPrinceton Fall 2025, DeveloperWeek 2026.
- Full NeMo Agent Toolkit hackathon Devpost/GitHub links for 3 named winners; NVIDIA Cosmos Cookoff Devpost page; Santa Clara "Agents for Impact" (luma.com/813gzkjk); Hack-a-Claw at other universities; Vercel x NVIDIA world's shortest hackathon; Dell/NVIDIA HackAI 2025; NVIDIA-India Agentic AI Hackathon 2026; Brunel/Lboro NVIDIA hackathon.
- NVIDIA prizes at hackathons hosted off Devpost (HackMIT, Hack the North, Cal Hacks sites).

## Follow-up pass (added)
- Checked: TAMUhack 2026 (th26) prizes page: no NVIDIA prize. HackUTD 2024 news (Dallas Innovates): no NVIDIA challenge mentioned. HackMIT 2025 plume project pages show no prizes/tracks (prizes not on plume; login needed for teams) -> unresolved. Hack the North: hackthenorth.com now shows only 2026, no NVIDIA info.
- DevNetwork AI/ML 2026 (May 11-28 2026): scanned all 24 winners; Crusoe 'Nemotron agent' challenge winners Argus and Leavitt added (sponsor of prize is Crusoe; NVIDIA DGX Spark is 1st prize; Overall Winner crusoe-nemotron-harness did not carry the Crusoe badge, not added).
- UB Hacking Fall 2025 (Nov 8-9): scanned winners; Best AI/ML Hack = EAS&E (Jetson Nano prize, low confidence row). Other UB winners carried no NVIDIA badge (first 16 viewed; list truncated in tool output).
- NeMo Agent Toolkit hackathon winner recap (NVIDIA blog 2025-07-17): winners are unnamed with no Devpost/GitHub/YouTube links in the post, so no winner rows possible. Brunel hackathon article names a team (Aman Sah, Sahid Mujavar, Zohaib Estesham, Eshita Agarwal) but no project, date or links.
- New prompts: Spark Hack Seattle, NVFP4 Kernel Hackathon, NVIDIA x Vercel, AI Summit NY Dell+NVIDIA, Crusoe Nemotron, NeMo toolkit judging criteria.
## Leads still left
- HackMIT 2024/2025 prizes (hackmit.org/other sources), Hack the North 2025 sponsors, Cal Hacks 11/12/13 slugs, HackUTD 2024 winner badges, MHacks 2025, HackPrinceton Fall 2025, DeveloperWeek 2026, HackTX 2025/26, Hacklanta winners scan; UB Hacking winners beyond first 16; Santa Clara Agents for Impact recap; Hack-a-Claw other campuses; NVIDIA-India Agentic AI Hackathon; HackAI Dell+NVIDIA 2025; Spark Hack Seattle winners.
