# Backfire: table pitch (v3, 4 minutes deck + live demo, then open Q&A)

Deck: https://docs.google.com/presentation/d/1n5TyV86wL2546wV_2QbDOF7LUigL-KYgmdKjkpfrJDw/edit
(8 slides; each slide's spoken line is also in its speaker notes.)

What changed from v2: no persona name (say "the customer" / "someone you love", never "Maria" or "her");
the customer uses the Backfire mobile web app on a real phone and the scammer calls the real number;
the demo ends on the money (Capital One Nessie) with one Approve click; slide 8 has the measured numbers.

**Who does what**
- Kareem: opener, then plays the customer (holds the phone with the Backfire web app open, earphones in).
- Rayan: leads the deck and narrates the demo.
- Ayman: plays the scammer on a real phone (caller ID on); takes the how-it-works slide.
- Evan: drives the command center on the monitor and clicks Approve.

**Numbers said out loud (6; drop "67 million" first if over time):**
4x older adults losing $10K+ to fake bank/government callers, 2024 vs 2020 (FTC Data Spotlight, Aug 2025:
8,269 vs 1,790, ages 60+) · $3,000 vs $599 median loss, phone vs social media (FTC, Protecting Older
Consumers, Oct 2026) · 280,000+ scam calls TPG Telecom sent to AI "victims" (GSMA case study, Oct 2025) ·
67 million Scam Callback Protection warnings (T-Mobile, Nov 2026) · our test: 33 of 33 scams caught, 2 of 27
look-alike legit calls wrongly flagged (our rules-only fallback, no AI: 26 of 33 and 1 of 27) · on real phone calls the alert fired 12 to 18 s in.

**If asked "why 12 seconds?" (P2, 5 real phone calls, team actors):** "Backfire alerts 12 to 18 seconds into the call, and 0.3 to 3 seconds after the scammer says the key words. Most of that time is the scammer working up to the ask." Real-call tally: 5 of 6 scam calls alerted (the miss had the caller's audio muted upstream), 7 of 7 harmless calls stayed quiet.

**On screen only:** scammers spotted the AI as a bot in about 1 in 20 calls (slide 5); "Tricks aimed at
the AI: 13 of 13 vs 9 of 13" (slide 8 table).

**Never say:** "Scammer get scammed" before the Approve click (it's the payoff line; the button is called Fire Back); "Maria", "her voice" (say "their voice"); "instant" or "real-time" (say "about 12 to 18 seconds
in"); "100%"; "on device" or "nothing leaves the phone" (on this path detection runs on our server, and
speech-to-text uses NVIDIA-hosted Riva); "we held the money" (Nessie cancels the pending transfer: say
"stopped"); "real bank" (it is Capital One's Nessie sandbox with mock data); "scammers stay on for 54
minutes" (longest call, not typical); "no carrier turns scam calls into intelligence" (TPG and Apate.ai do).

---

## Run of show

| Time | Slide | Who | Words and action |
|---|---|---|---|
| 0:00 | 1 Cover | Kareem | "Last night we were stuck for hours trying to stop scam calls. Then Rayan remembered what his basketball coach, Anthony, always told him: the best defense is offense." |
| 0:09 | 1 Cover | Kareem | Dunks on Rayan on "offense." Mime it, no ball. |
| 0:11 | 1 Cover | Rayan | Getting up: "Fair. So this is what we were stuck on." |
| 0:13 | 2 Persona | Rayan | "Picture someone you love, 78. The phone rings, and caller ID says it's their bank. A man says someone is draining the account, they need to move their savings to a safe account, and they shouldn't tell anyone at the branch. Four times as many older adults lost $10,000 or more to this kind of call in 2024 as in 2020." |
| 0:28 | 3 Stakes | Rayan | "When a scam starts with a phone call, people over 60 lose a median of $3,000. On social media, $599. The phone is where it costs the most." |
| 0:40 | 4 Gap | Rayan | "Everything T-Mobile does today judges the number before the phone rings. Once a scammer gets through, nothing helps during the call." |
| 0:52 | 5 Caller Beware | Rayan | "So we flipped it: Caller Beware. With Backfire, the customer taps Fire Back and an AI in their own voice takes over. It only ever listens to the caller. And scammers do keep talking to AI: TPG Telecom in Australia sent more than 280,000 scam calls to AI 'victims'." |
| 1:10 | 6 Follow the money | Rayan | "Scammers change numbers for pennies, but not where the money goes. The decoy's job is to get his payout account. Capital One stops the transfer and flags that account; T-Mobile warns anyone who dials his callback number. Let's show you. Ayman's the scammer." |
| 1:30 | Demo | All | See the demo block below. The command center does the talking from about 2:30. |
| 3:00 | 7 How it works | Ayman | "The hard part was letting an AI talk to a scammer without the scammer turning it against the customer. The detector and the decoy only hear the caller and have no tools. A separate Nemotron agent sees only what the decoy extracted, runs real lookups, and only proposes actions. Plain code applies what affects only the customer, like stopping their own transfer, and queues anything bank-wide or network-wide for one human click." |
| 3:25 | 8 Proof | Rayan | "On 60 test scripts, the Nemotron model on our laptop caught 33 of 33 scams and wrongly flagged 2 of 27 real look-alike calls. Our rules-only fallback, with no AI, caught 26 and wrongly flagged 1, which is why it's a floor, not the detector. On real phone calls, the alert fired 12 to 18 seconds in. Next, we'd pilot on T-Mobile's call servers with a Capital One payee-risk feed." |
| 3:45 | 8 Proof | Rayan | "One scam call. The customer kept their $1,800, his account is flagged for every customer, and he can't reach a Backfire customer again." |
| 3:52 | 8 Proof | Rayan + Kareem | "Scammer get scammed!" Beat. Then: "What would you like to go deeper on?" |

## Demo block (1:30 to 3:00)

Demo card for Ayman (same "safe account" scam as slide 2, trimmed to three lines; P1 lists it first in data/script-cards.md as the Judge card). Judges who call on their own pull from the bucket in data/script-cards-v3-bank.md (10 bank-fraud cards, all ending in the same Zelle payout):
- Line 1: "Hi, this is the fraud team at your bank. Someone's draining your account right now. To protect your savings, you need to move them to a safe account. And don't tell anyone at the branch."
- Payment line: "Our secure line is 1-888-555-0123, and the transfer portal is backfire-demo dot example."
- **Zelle line (say it last, it triggers the bank ending):** "Open your banking app and send the $1,800 by Zelle to refunds dot dept at backfire dash demo dot example. That's the safe account."

| Step | What happens | Command center (Evan) |
|---|---|---|
| 1 | Ayman dials (469) 908-8594 from his phone, caller ID on, on speaker. The customer's phone rings full screen. | Live call view: "Ringing the customer with Live Guard on" |
| 2 | Kareem taps **Answer** (do not let it ring out: no answer rejects the call) and says, in his normal voice: "Hello?" | |
| 3 | Ayman reads line 1. Nobody else talks while the call is live. | Caller-only transcript scrolls; risk gauge climbs |
| 4 | Two beeps, about 12 to 18 seconds in. Kareem shows the judge the three buttons, taps **Fire Back**, puts the phone face down, raises both hands. | "The customer tapped Fire Back" |
| 5 | The AI, in Kareem's voice: "Sorry, I lost you there for a second," then asks how to pay. | Banner: "The scammer is talking to the decoy in the customer's voice" |
| 6 | Ayman reads the payment line, then the Zelle line. The decoy repeats it back slowly, then says goodbye and hangs up by itself. | |
| 7 | Rayan, while intel runs (5 to 15 s): "Kareem's been off that call since his hands went up. Backfire only ever listened to the caller. That was a Nemotron decoy in his voice, and it just got the scammer's payout account." | Screen moves to **Money trail** by itself; Capital One lockup appears |
| 8 | Rayan points: "$1,800 stopped before it reached the scammer. That 'safe account' already took $18,100 from seven other people." | Banner: "$1,800 stopped before it reached the scammer"; map: customer's line cut, 7 victims into the mule account |
| 9 | Rayan: "One click and every customer who tries to pay it gets warned first." **Evan clicks "Approve · flag this account"** (right column). As the banner changes, Rayan + Kareem: "Scammer get scammed." (First time anyone says it.) | Banner: **"Scammer get scammed. He got $0."**; mule account tagged Flagged |
| 10 | T-Mobile beat, if time: Ayman calls back from the same phone. It never rings. | Checklist: "He called back: rejected before it rang" |

Staging rules:
- Only the scammer's phone on speaker. The customer wears earphones (open speaker echoes into the call).
- Caller ID on for every call (the callback rejection needs the number).
- Once connected, the scammer's phone hears the table; anything said there goes to the decoy.
- Nobody reads the wallet aloud; show it on the command center.
- One judged call at a time. Reset between judges: `POST /demo/reset` (also starts the customer's pending $1,800 in the Nessie sandbox), then Clear for next judge (C) on the command center.

## Capital One judge (20 seconds, at or after the money trail)
"Backfire turns a scam call into the payout account the scammer wanted. In Capital One's Nessie sandbox,
that stops the customer's own pending Zelle to him, finds the seven other customers who already paid the
same account, and queues one analyst click to flag it for everyone. Nessie calls are real; the bank data
is mock, and the bank-wide flag is a simulated payload."

## 60-second version (tired or late judges)
1. "Backfire: T-Mobile customers hand a scam call to an AI decoy that stops the payout and blocks the scammer."
2. Live: answer, two beeps, tap Fire Back, hands up.
3. Decoy in the customer's voice gets the Zelle address. Pause two seconds on the Money trail.
4. "$1,800 stopped, the mule account flagged with one click. Scammer get scammed. What would you like to see?"

## Failure lines
- Call drops: "The phone network dropped; here is the recorded run." Switch to the replay (command center `?src=fixture`) within 10 to 15 seconds. Never redial live.
- Money trail is slow: "Intel is running real lookups; here's the same ending from the last run." (Replay, press 2, click Approve.)
- Decoy goes quiet: "The decoy's turn timed out; here's the full decoy call we recorded."

## Open before judging
- Ayman re-enrolls his voice with the fixed web recorder (quality check must say "ok"), so the clone sounds like him.
- Settled: every card in data/script-cards-v3-bank.md ends in Zelle to refunds.dept@backfire-demo.example for $1,800, so the bank ending fires on any card. Run /demo/reset between judges (one pending transfer per reset). Judges should read the whole card, at least through the code or payment ask.
- Hub has the latest command center (reload `/command-center/` with Ctrl+F5) and `NESSIE_API_KEY` set (acceptance 12/12).
- Confirm with an organizer that 4 minutes is pitch time, not the whole visit.
