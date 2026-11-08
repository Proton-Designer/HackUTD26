# Backfire: table pitch (v2, 4 minutes deck + demo, then open Q&A)

Deck: https://docs.google.com/presentation/d/1n5TyV86wL2546wV_2QbDOF7LUigL-KYgmdKjkpfrJDw/edit
(8 slides; every slide's spoken line is also in its speaker notes.)

**Who does what**
- Kareem: opener, then plays Maria (holds the Backfire phone).
- Rayan: leads the deck and narrates the demo.
- Ayman: plays the scammer on the VoIP phone; takes the how-it-works slide.
- Evan: drives the command center on the monitor.

**Numbers said out loud (5; above the kit's 3, so drop "67 million" from speech first if over time):**
4x as many older adults lost $10K+ to fake bank/government callers, 2024 vs 2020 (FTC Data Spotlight,
Aug 2025: 8,269 vs 1,790 reports, ages 60+) · $3,000 vs $599 (FTC,
Protecting Older Consumers, Oct 2026) · 280,000+ calls to AI "victims", 100+ days of scammer time
wasted (GSMA case study, Apate.ai and TPG Telecom, Oct 2025; longest call 54 min, on screen only) · 67 million Scam Callback Protection warnings (T-Mobile, Nov 2026)
· our measured result ([ADD]).

**On screen only (slide 5):** scammers spotted the AI as a bot in about 1 in 20 calls (Traister et al.,
arXiv 2609.29528, 2026, 10,015 calls; Sahin et al., USENIX SOUPS 2017, 200 calls).

**Never say:** "scammers stay on for 54 minutes" (it was the longest call, not typical), "no carrier
turns scam calls into intelligence" (TPG and Apate.ai do).

---

## Run of show

| Time | Slide | Who | Words and action |
|---|---|---|---|
| 0:00 | 1 Cover | Kareem | "Last night we were stuck for hours trying to stop scam calls. Then Rayan remembered what his basketball coach, Anthony, always told him: the best defense is offense." |
| 0:09 | 1 Cover | Kareem | Dunks on Rayan on "offense." Mime it, no ball. |
| 0:11 | 1 Cover | Rayan | Getting up: "Fair. So this is what we were stuck on." |
| 0:13 | 2 Maria | Rayan | "This is Maria. Her phone rings, and the caller ID says it's her bank. A man tells her someone is draining her account, she needs to move her savings to a safe account, and she shouldn't tell anyone at the branch. And this isn't rare: four times as many older adults reported losing $10,000 or more to this kind of scam in 2024 as in 2020." (Story first, then the number. On screen: 8,269 vs 1,790, FTC Data Spotlight, Aug 2025.) |
| 0:25 | 3 Stakes | Rayan | "When a scam starts with a phone call, people over 60 lose a median of $3,000. On social media, $599. The phone is where it costs the most." |
| 0:40 | 4 Gap | Rayan | "Everything T-Mobile does today judges the number before the phone rings. Once a scammer gets through, nothing helps her during the call." |
| 0:55 | 5 Caller Beware | Rayan | "That's why we're Caller Beware: on a scam call, the caller is the one who should worry. With Backfire, Maria taps one button, an AI in her voice takes over, and it only ever listens to him. And scammers do keep talking to AI. TPG Telecom in Australia sent more than 280,000 scam calls to AI 'victims' and wasted more than 100 days of scammer time." (The "1 in 20" card and the 54-minute longest call stay on screen for Q&A.) |
| 1:12 | 6 Follow the scam | Rayan | "Scammers change numbers for pennies, but not where the money goes. Everything the AI gets goes into protection T-Mobile already runs. Scam Callback Protection alone has played 67 million warnings. Let's show you. Ayman's the scammer." |
| 1:30 | Demo | All | See the demo block below. Command center lights up around 2:00. |
| 2:45 | 7 How it works | Ayman | "The hard part was letting an AI talk to a scammer without the scammer turning it against Maria. The detector and the decoy only hear the scammer and have no tools. A separate Nemotron agent sees only what the decoy extracted, runs real lookups, and can only propose blocks. Plain code applies what affects only Maria and queues the rest for one analyst click." |
| 3:20 | 8 Proof (table: cloud, local, keyword rules) | Rayan | "On 60 test scripts we froze before scoring, the cloud model caught [__] of [__] scams and wrongly flagged [__] of [__] real look-alike calls. A plain keyword filter flagged [__]. Next, we'd pilot on the servers behind T-Mobile's Live Translation." (Say only the cloud pair and the keyword false alarms; the local column is for questions.) |
| 3:45 | 8 Proof | Rayan | "One scam call, and that scammer can't reach Maria or any other Backfire customer again." |
| 3:52 | 8 Proof | Rayan + Kareem | "Scammer get scammed!" Beat. Then: "What would you like to go deeper on?" |

## Demo block (1:30 to 2:45)

Two-line table card for Ayman (same scam as slide 2; trimmed from Card 2, "Bank Fraud Department"):
- Line 1: "Hi, this is the fraud team at your bank. Someone's draining your account right now. To protect your savings, you need to move them to a safe account. And don't tell anyone at the branch."
- Payment line: "Our secure line is 1-888-555-0123, and the transfer portal is ____ dot com."

Why this scam: it's the FTC's "fake fraud alert" pattern. Older adults' losses of $100K+ to fake bank and
government callers went from $55M (2020) to $445M (2024), and 41% of older adults' $10K+ impostor losses
started with a phone call (FTC Data Spotlight, Aug 2025). The caller ID often shows the real bank's
number, spoofed, which is why judging the number alone misses it (slide 4).

| Step | What happens |
|---|---|
| 1 | Ayman dials from the VoIP phone (on speaker). Maria's phone shows Live Guard on. |
| 2 | Kareem answers in his normal voice: "Hello, this is Maria." Phone at his ear. |
| 3 | Ayman reads line 1. Nobody else talks while the call is live. |
| 4 | Two beeps. Kareem shows the judge the three buttons, taps Scammer Get Scammed, puts the phone face down, raises both hands. Two seconds of silence. |
| 5 | The AI, in Kareem's voice: "Sorry, I lost you there for a second," then asks how to pay. |
| 6 | Ayman reads the payment line. The AI ends the call. |
| 7 | Command center lights up. Rayan: "Kareem's been off that call since his hands went up, and Backfire only ever listened to the scammer. That was a Nemotron decoy in his voice, and it just got the scammer's callback number and website." |
| 8 | Callback rejected before it rings, then the new-number immunity call if it is live. |

Staging rules:
- Only the scam phone on speaker (two speakerphones in one call echo).
- Once the call connects, the scam phone's mic hears the table; anything said goes to the decoy.
- Nobody reads the wallet aloud. Show it on the command center.

## Failure lines
- Call drops: "The phone network dropped; here is the recorded run." Switch to the backup tab within 10 to 15 seconds. Never redial live.
- Lookup is slow: "That lookup is live and the registry is slow; here's the same lookup from the last run."
- Decoy goes quiet: "The decoy's turn timed out; here's the full decoy call we recorded."

## Open before judging
- Slide 8 table numbers: cloud, local and keyword rules (Ayman is running cloud and local now; rules and local test numbers are already in `detection/eval/RESULTS.md`).
- [ADD] scam line number on the cover's Try it card, or replace the card.
- Demo card switched from the IRS card to the bank "safe account" card to match slide 2. Run it once on
  the live line before judging (Ayman's local test caught 7 of 7 bank-fraud scripts, but the live line
  hasn't heard this card yet).
- Real demo domain: `intel/demo_config.json` still has the placeholder `backfire-demo.example`.
- Demo wallet is the Bitcoin genesis address; swap for a wallet the team made.
- Slide 5 says "an AI in her voice": change it if the voice clone is cut for a synthetic voice.
- Confirm Coach Anthony's line is told as Rayan's coach.
- Confirm with an organizer that 4 minutes is pitch time, not the whole visit.
