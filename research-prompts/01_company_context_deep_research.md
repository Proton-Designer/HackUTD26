# Step 1: Company-context deep research (NVIDIA + T-Mobile)

Goal of this step: understand each sponsor as it is RIGHT NOW (Nov 2026): what it sells, who it serves, what it is pushing, what hurts, and what its judges will want to be associated with. No ideation yet; that comes after.

Already known (in HackUTD-2026-Research/06_hackutd_2026_sponsors/ and outputs/sponsor_cards.md), so the agent should NOT spend time on: HackUTD 2026 dates/format, the 2025 T-Mobile winners (InsighT, Beacon, HarmoniQ) and 2025 NVIDIA winners (Alchemetrics, DataDriver, Toyotron), the basic build.nvidia.com free endpoints, and the four DevEdge API names.

---------------------------------------------------------------------
## A. What to look for (checklist, same for both companies)

1. **Snapshot and current state**
   - What the company does in one paragraph, its business segments, and how revenue splits across them
   - Most recent quarterly earnings: headline numbers, what leadership stressed, guidance
   - Who is CEO and who else leads, plus any recent leadership changes
   - The 3-5 strategic priorities leadership repeats publicly (keynotes, earnings calls, shareholder letters)
2. **The last 12 months**
   - Major launches, acquisitions, partnerships, reorganizations, lawsuits, regulatory actions, outages or incidents
   - What the press and analysts say the company's biggest opportunity and biggest threat are right now
3. **Products and platforms**
   - A full product map with the flagship products marked
   - Which products are new or being pushed hardest in 2026
   - Developer-facing products we could use in 24 hours: how to get access, free tier, rate limits, sandbox, SDK languages, how good the docs are, and any quickstarts or sample apps
4. **Audiences and customers**
   - Every customer segment (consumer, SMB, enterprise, government, developers, partners)
   - 3-5 concrete personas per segment, covering their job, a typical day, and the tools they use
   - Internal users, meaning the employees whose work a hack could improve (PMs, network engineers, care reps, solutions architects, DevRel)
5. **Pain points and open problems** (evidence-backed)
   - Recurring customer complaints from Reddit, app-store reviews, the BBB, Downdetector, forums and review sites, quoted verbatim with dates
   - Problems the company itself says it is trying to fix
   - Workarounds people use today
6. **Competitive landscape**
   - Main competitors and where the company wins or loses against each
   - Recent moves by competitors that the company is responding to
7. **Their vocabulary and brand**
   - The terms they use themselves (product names, slogans, keynote phrases)
   - Brand values and anything they would NOT want their name attached to
8. **AI posture**
   - How they use AI internally and with customers
   - Their public AI partnerships and products
   - What "good AI" looks like in their messaging (safety, privacy, on-device, open models, and so on)
9. **Data we could use**
   - Public datasets, open models, coverage maps, status pages, public APIs, open-source repos
   - Anything they publish that a hack could build on
10. **Constraints and sensitivities**
    - Regulation (privacy rules, FCC, export controls), past breaches or scandals, and topics to avoid
11. **DFW, UTD and hackathon presence**
    - Their footprint in Dallas-Fort Worth, which teams sit there, ties to UTD, recruiting focus
    - Past hackathons they sponsored: challenge statements, what won, and anything judges said publicly about what they rewarded
    - Their developer and startup programs
12. **Judge lens**
    - Who from the company is likely judging (role, team) and what success looks like for them
    - Which kind of student project would make them look good if they rewarded it
13. **Overlap between NVIDIA and T-Mobile**
    - Joint initiatives (for example AI-RAN), shared customers, and shared themes
    - Because one project can enter both tracks, this matters.

---------------------------------------------------------------------
## B. Prompt 1: NVIDIA (paste as-is)

```
You are a research analyst preparing a 4-person student team for HackUTD 2026 (UT Dallas, Nov 7-8, 2026, 24 hours, expo-style judging). NVIDIA is one of our two target sponsor tracks. Today is November 7, 2026. Your job is to give us a deep, current understanding of NVIDIA as a company: its products, audiences, priorities and problems. Do NOT generate hackathon project ideas. That is a later step.

[OPTIONAL: If NVIDIA's official 2026 HackUTD challenge text has been announced, it is pasted here. Weight the research toward it, but still cover everything below:
<<PASTE CHALLENGE TEXT OR DELETE THIS BLOCK>>]

We already know these, so skip them: the HackUTD event format; the free inference endpoints on build.nvidia.com (Nemotron models, OpenAI-compatible API at integrate.api.nvidia.com/v1); and the HackUTD 2025 NVIDIA winners (Alchemetrics, DataDriver, Toyotron).

Research and report on:

1. COMPANY SNAPSHOT: business segments (Data Center, Gaming, Pro Visualization, Automotive/Robotics, OEM) and how revenue splits across them; the most recent quarterly earnings and what Jensen Huang and the CFO stressed; leadership; the 3-5 strategic themes NVIDIA repeats in 2026 keynotes (GTC 2026, Computex 2026, GTC DC/Paris and similar), e.g. agentic AI, physical AI, AI factories, sovereign AI, AI-RAN/6G, plus any newer ones.

2. LAST 12 MONTHS: major launches (GPU architectures such as Blackwell Ultra and Rubin, DGX Spark/Station, Jetson Thor and others), acquisitions, partnerships, investments, export-control and regulatory developments, antitrust issues, supply constraints. What analysts call NVIDIA's biggest opportunity and biggest risk right now.

3. SOFTWARE AND DEVELOPER PLATFORM (most important for us): map the current software stack: CUDA, NIM microservices, NeMo (including Guardrails, Agent Toolkit, Curator, Customizer), the Nemotron model family (every current model, size, modality, and what each is good at), Cosmos, Isaac/GR00T, Omniverse, Riva/speech, Dynamo, AI Blueprints, Brev, DGX Cloud, RTX AI PC tools, and whatever else is new in 2026. For each one: what it does, who it is for, and whether a student team can use it in 24 hours without its own GPUs (free tier, credits, rate limits, signup friction, docs and sample quality). Name the NVIDIA AI Blueprints or reference apps that could be forked quickly.

4. AUDIENCES: list NVIDIA's customer segments (hyperscalers, enterprises, startups, researchers, game developers and gamers, robotics/auto OEMs, telcos, governments, individual developers). For each, give 3 concrete personas with their job, current tools, and the pain NVIDIA addresses for them. Separately describe NVIDIA's own developer-relations and solutions-architect roles, since these are likely hackathon judges.

5. PAIN POINTS AND OPEN PROBLEMS: what developers complain about with NVIDIA's software (setup, CUDA/driver issues, NIM deployment, cost, rate limits, docs), quoted verbatim from forums, GitHub issues, Reddit and Hacker News with dates. Also the problems NVIDIA publicly says the industry still has to solve (inference cost, agent reliability, evaluation, energy, data for physical AI, and so on).

6. COMPETITIVE LANDSCAPE: AMD, Intel, custom silicon (TPU, Trainium, MTIA and others), open-model competitors to Nemotron, and inference providers. Where NVIDIA is winning, where it is under pressure, and how it responds (for example, open models and software lock-in).

7. VOCABULARY AND BRAND: the exact phrases NVIDIA uses for its own strategy and products, what NVIDIA wants to be known for, and anything it would not want associated with its name.

8. TELECOM AND T-MOBILE OVERLAP: NVIDIA's telecom work (Aerial, AI-RAN, the AI-RAN Alliance, any T-Mobile AI-RAN Innovation Center or joint trials, investments in network-equipment makers) and its current status in 2026. What a project spanning NVIDIA and a mobile carrier could credibly touch.

9. DFW, TEXAS AND UNIVERSITIES: NVIDIA's presence in Dallas-Fort Worth and Texas (offices, manufacturing partnerships, data centers), ties to UT Dallas, and its student and education programs (Deep Learning Institute, academic grants, Inception for startups).

10. HACKATHON HISTORY: hackathons NVIDIA sponsored or ran from 2024 to 2026 (TreeHacks, NeMo Agent Toolkit hackathon, GTC hackathons, DGX Spark hackathons, NemoClaw/"Hack-a-Claw" and others). Include challenge statements, judging criteria, winners, and anything NVIDIA staff said about what they rewarded.

11. JUDGE LENS: based on the above, what NVIDIA staff at a student hackathon would most want to see, and which kind of winning project would make NVIDIA look good publicly. Back this with evidence; do not invent project ideas.

OUTPUT FORMAT:
- Start with "Top 15 things a hackathon team must know about NVIDIA right now", one line each.
- Then one section per numbered item above, using tables where they help (the product map, the personas).
- Tag every factual claim [V] (verified, with source URL and publish date) or [U] (unverified or inferred). Prefer sources from the last 12 months, and flag anything older than 18 months as possibly stale.
- End with: (a) "Open questions to ask the NVIDIA booth/mentors", 8-12 of them; (b) "What changed since mid-2025" in one paragraph; (c) a full source list.
- Be concrete: names, numbers, dates and links. No generic filler.
```

---------------------------------------------------------------------
## C. Prompt 2: T-Mobile (paste as-is)

```
You are a research analyst preparing a 4-person student team for HackUTD 2026 (UT Dallas, Nov 7-8, 2026, 24 hours, expo-style judging). T-Mobile is the Title sponsor and one of our two target sponsor tracks. Today is November 7, 2026. Your job is to give us a deep, current understanding of T-Mobile as a company: its products, audiences, priorities and problems. Do NOT generate hackathon project ideas. That is a later step.

[OPTIONAL: If T-Mobile's official 2026 HackUTD challenge text has been announced, it is pasted here. Weight the research toward it, but still cover everything below:
<<PASTE CHALLENGE TEXT OR DELETE THIS BLOCK>>]

We already know these, so skip them: the HackUTD event format; the HackUTD 2025 T-Mobile winners (InsighT, Beacon, HarmoniQ, all customer-sentiment dashboards for PMs); and the names of the four DevEdge Network API families (Fraud Signals, Network Authentication, Call Protection, Quality on Demand).

Research and report on:

1. COMPANY SNAPSHOT: business lines (postpaid and prepaid wireless including Metro and Mint, 5G home internet, fiber, T-Mobile for Business/T-Priority, wholesale, advertising) and their revenue mix; the most recent quarterly earnings (subscriber adds, churn, ARPU/ARPA, guidance); leadership, including the CEO transition to Srini Gopalan and how strategy has shifted under him; the 3-5 priorities leadership repeats publicly in 2026.

2. LAST 12 MONTHS: major moves such as the UScellular integration, the fiber joint ventures (Lumos, Metronet), T-Satellite with Starlink, 5G Advanced and network slicing (T-Priority, SuperMobile and similar), plan and price changes, the T-Life app push, AI partnerships (OpenAI/IntentCX, Perplexity and others), layoffs or reorganizations, outages, security incidents, lawsuits and FCC actions. What analysts say T-Mobile's biggest opportunity and biggest threat are right now.

3. PRODUCTS AND DEVELOPER ACCESS: a full current product map (plans, perks/Magenta Status, T-Life app, home internet, fiber, satellite, business products, IoT, network slicing). Developer-facing assets: DevEdge (what is actually usable today, sandbox or simulator, self-serve versus sales-gated access, docs quality), GSMA Open Gateway/CAMARA and the Aduna joint venture, and any public APIs, SDKs or open data. State plainly what a student team could really access in 24 hours.

4. AUDIENCES: segments (consumer postpaid, prepaid/value, 55+, military, families, small business, enterprise, government/first responders, rural customers including former UScellular ones, home-internet switchers). For each, give 3 concrete personas with their situation, what they pay for, and their main friction with T-Mobile. Separately describe internal users: product managers, network engineers, Team of Experts/T-Force care reps, retail store staff, and the fraud and security teams.

5. PAIN POINTS AND OPEN PROBLEMS: recurring customer complaints in 2025-2026 (price increases on legacy plans, care experience, the switch to app-first service, coverage gaps, home-internet congestion, fraud and SIM-swap, data-breach fallout, satellite limits, and others), each quoted verbatim with date and source (Reddit r/tmobile and r/NoContract, app reviews, the BBB, Downdetector, news). Also the problems T-Mobile itself says it is solving, and the workarounds customers and employees use today.

6. COMPETITIVE LANDSCAPE: Verizon, AT&T (also a HackUTD sponsor), cable MVNOs (Spectrum, Xfinity), the EchoStar/Boost situation, fiber and fixed-wireless competitors, and satellite players. Where T-Mobile wins (network perception, value) and where it is losing.

7. VOCABULARY AND BRAND: the Un-carrier identity and whether it is still used, current slogans, how T-Mobile talks about AI, the network and customers, and topics or themes T-Mobile would not want its name on.

8. AI AND NETWORK INNOVATION: how T-Mobile uses AI internally (care, network operations, retail, marketing) and in products; the AI-RAN work with NVIDIA (AI-RAN Innovation Center, trials with Nokia or Ericsson, current status in 2026); 5G Advanced, network slicing and edge computing; any T-Mobile innovation labs or accelerators (T-Mobile Ventures, T Challenge and similar).

9. DFW AND UTD PRESENCE: T-Mobile's Frisco/Plano/North Texas footprint (headcount, which organizations sit there, e.g. engineering, product, care, the Ventures team), ties to UT Dallas, recruiting and internship focus, and local community programs.

10. HACKATHON HISTORY: hackathons and challenges T-Mobile sponsored from 2024 to 2026 (HackUTD 2024 and 2025, DubHacks, Hacktober, any T-Mobile internal or partner hackathons). Include challenge statements, winners, judging criteria, and anything T-Mobile staff said about what they rewarded.

11. JUDGE LENS: based on the above, which T-Mobile roles are likely to judge (product, network, engineering, recruiting), what each would value, and which kind of winning project would make T-Mobile look good publicly. Back this with evidence; do not invent project ideas.

OUTPUT FORMAT:
- Start with "Top 15 things a hackathon team must know about T-Mobile right now", one line each.
- Then one section per numbered item above, using tables where they help (the product map, the personas, the pain points).
- Tag every factual claim [V] (verified, with source URL and publish date) or [U] (unverified or inferred). Prefer sources from the last 12 months, and flag anything older than 18 months as possibly stale.
- End with: (a) "Open questions to ask the T-Mobile booth/mentors", 8-12 of them; (b) "What changed since mid-2025" in one paragraph; (c) a full source list.
- Be concrete: names, numbers, dates and links. No generic filler.
```

---------------------------------------------------------------------
## D. Optional Prompt 3: where NVIDIA and T-Mobile overlap (run only if both prompts above come back thin on it)

```
Today is November 7, 2026. Research every current point of contact between NVIDIA and T-Mobile US: the AI-RAN Innovation Center and any joint AI-RAN or Aerial trials, joint announcements from 2024-2026, NVIDIA's telecom/6G strategy as it applies to US carriers, T-Mobile's use of NVIDIA hardware or software (network operations, care, edge), and shared partners (Nokia, Ericsson, OpenAI and others). For each item give the status as of Nov 2026, what was actually delivered versus announced, and what is publicly documented enough for an outsider to build against or simulate. Tag claims [V] with URL and date, or [U]. Do not generate project ideas. End with a list of open questions and the sources.
```
