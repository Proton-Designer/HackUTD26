# Hacklanta — Hacklanta 2026 (2 projects)

### Ingineer
*Hacklanta Hacklanta 2026 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [Photon] Agents in iMessage - Winner

**What it is:** An iMessage coordinator agent (Ing) that plans events among friends: each person's agent shares calendar availability, finds a common slot, creates events, and calls specialist agents for food, rides, venues and research.
**Problem / user:** Friends whose plans die in long group chats before anyone settles time, place, ride or food; each friend gets a personal agent.

**Features**
- Natural-language planning by text — User texts a goal such as finding dinner time; Ing starts a group chat with friends' agents. *[shown_working]*
- Calendar availability matching — Each Ing reads Google Calendar free/busy only, finds a shared 30-minute slot and proposes it; details stay private. *[shown_working]*
- Event creation and invitations — After group confirmation each agent adds the event to its owner's calendar and invitations go out. *[shown_working]*
- Specialist agents — Narrow agents for food delivery, rides, venues, tickets, gifts and itinerary reply only when relevant, else PASS. *[claimed]*
- Cloud browser research — E2B Desktop sandbox with OpenAI computer use browses and returns screenshots and short answers via iMessage. *[claimed]*
- Voting, preferences, Venmo splits — Tapback voting, private order rounds, saved preferences and bill splitting per creator bio. *[claimed]*
- Encrypted memory and private tool scope — Group data and memory encrypted; personal tools only available in a user's private chat. *[claimed]*

**Flow:** Text Ing a planning goal → Ing adds friends' agents to a group chat → Agents report availability and a slot is proposed → Group confirms; calendar events and invites created → Specialists offer food, ride and venue options → Ing merges choices into a final itinerary

**Prompt:** Photon track at Hacklanta: build an agent that lives in iMessage and integrates the Spectrum SDK.
**Fit (explicit):** Multi-agent coordinator living in iMessage group chats, built on Photon, handling group logistics through each friend's agent.  *(targeted: [Photon] Agents in iMessage)*
**Sponsor tools:** Photon (iMessage agent platform) (coordinator agent in iMessage group chats, core)
**AI:** Coordinator agent routes requests to eight narrow specialist agents with strict reply rules; OpenAI computer use drives a cloud browser for research.
**Architecture:** Photon iMessage coordinator, specialist agent layer, Google Calendar integration, E2B cloud desktop, encrypted memory and agent proxy over websockets, Neon Postgres; landing page on Vercel; runs on teammates' laptops with failover.
**Novelty:** Agent-per-person design where agents negotiate on behalf of friends, with a strict PASS rule to stop agent chatter, plus sandboxed browser research.
**Scope:** large · working: Page says a working iMessage flow exists; live landing page; repo not cloned in evidence. · polish: Landing page on Vercel with demo link; no video.
**Claims:** Working iMessage flow where one text brings multiple agents into the group chat | Calendar matching without revealing private events
**Gaps:** repo clone failed so no README or code stats; no video
Sources: https://devpost.com/software/ingineer

---

### Safeword
*Hacklanta Hacklanta 2026 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** [Photon] Agents in iMessage - Runner Up

**What it is:** A personal-safety agent reachable by iMessage and phone call: a user walking alone at night can ask it to stay with them or request help, and a spoken duress phrase silently triggers calls and WhatsApp alerts to a human emergency contact with a 911 script.
**Problem / user:** People, especially students, walking home alone at night; existing tools need a free hand, a watcher or speaking aloud and alert only one person.

**Features**
- Stay With Me mode — Agent checks in by text and escalates if the user is silent for 15 seconds, then 15 more. *[shown_working]*
- Help Me Now mode — Immediate escalation with no conversation. *[shown_working]*
- Voice companion with duress phrase — ElevenLabs agent answers calls; a trigger phrase calls an escalate webhook while its spoken reply stays ordinary; also works in text. *[shown_working]*
- Automated call to emergency contact — Twilio places a call stating who needs help and where, identifying itself as an AI. *[shown_working]*
- WhatsApp alert with 911 script — Twilio message carries name, address, map link, time and a word-for-word script; the contact, not software, calls 911. *[shown_working]*
- Multi-channel agent loop — Same logic runs on iMessage via Photon Spectrum and in terminal. *[shown_working]*

**Flow:** Text walk me home to the iMessage agent → Choose 1 Stay With Me or 2 Help Me Now → Optionally call and talk to the voice companion → Say the duress phrase if threatened → Emergency contact gets an automated call → Contact receives WhatsApp location and 911 script and calls 911

**Prompt:** Photon track at Hacklanta: build an agent that lives in iMessage and integrates the Spectrum SDK.
**Fit (explicit):** Safety agent delivered through iMessage using Spectrum, with voice and escalation channels added.  *(targeted: [Photon] Agents in iMessage, Cox Social Good, MLH ElevenLabs)*
**Sponsor tools:** Photon Spectrum (iMessage agent loop across providers, core)
**AI:** ElevenLabs Agents provide the voice companion with a custom escalate webhook tool; the escalation logic is rule-based timers; Claude is listed as built with but its role is unstated.
**Architecture:** Photon Spectrum message and voice entry points feed a Node/Express agent holding session state and timers, which fires Twilio call and WhatsApp alerts; Cloudflare tunnel exposes the webhook to ElevenLabs.
**Novelty:** Covert voice duress trigger paired with a human-in-the-loop 911 script; deliberately never calls emergency services itself.
**Scope:** small · working: Page describes end-to-end Twilio call and WhatsApp alert working with debugging notes; no repo, demo or video. · polish: Four screenshots, cited statistics and a clear architecture description.
**Claims:** Cites Gallup: 4 in 10 Americans afraid to walk alone at night near home | Cites AAU 2019 survey of 181,752 students, 13% reporting nonconsensual contact
**Gaps:** no repository; no video or demo link; next steps cut off
Sources: https://devpost.com/software/safeword-3ef01z

---

