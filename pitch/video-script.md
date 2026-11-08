# Backfire: Devpost video (2:00), script and shot list

Record after the 08:00 code freeze, on the frozen build, from one real run (judge-style call on the Telnyx
line, customer on the Backfire web app). Every simulated part is labelled on screen. No persona name:
say "the customer". Same claims as the deck and `pitch/script.md`; nothing here that the deck doesn't say.

**What to capture (raw clips):**
- A. Customer's phone screen recording (iPhone or Android, web app): ringing, Answer, Live Guard, two beeps, the three buttons, tap Fire Back.
- B. Scammer's side: Ayman on speaker reading Card 2 (line 1, payment line, Zelle line). Audio matters more than video.
- C. Command center screen recording (1920x1080, browser full screen, no bookmarks bar): the whole call from ring to "Scammer get scammed. He got $0.", including the Approve click.
- D. The callback: Ayman calls again and it never rings (phone screen stays idle; command center shows "rejected before it rang").
- E. Deck slides 6, 7 and 8 as stills.
- F. 3 to 5 seconds of the team at the table (optional, for the end).

Voiceover: Rayan, one take per section, quiet room, phone ~20 cm away.

| Time | On screen | Voiceover (Rayan) |
|---|---|---|
| 0:00 to 0:08 | Black, then the phone ringing (A). Caption: "Caller ID: Their bank" | "Your phone rings. Caller ID says it's your bank. It isn't." |
| 0:08 to 0:20 | Deck slide 3 still ($3,000 vs $599), then slide 4 (the gap) | "When a scam starts with a phone call, people over 60 lose a median of $3,000. And once a scam call gets through, nothing on the phone helps during the call." |
| 0:20 to 0:30 | Title card: "Backfire. Caller Beware." Small line: "T-Mobile Safe Signal · NVIDIA Nemotron · Capital One Nessie" | "So we built Backfire. On a scam call, the caller is the one who should worry." |
| 0:30 to 0:50 | Split: phone (A) left, command center Live call view (C) right. Caller transcript scrolls, risk gauge climbs, two beeps. | "This is a real call on a real phone line. Backfire hears only the caller's side. A Nemotron model scores what he says, and about twelve to eighteen seconds in, the customer hears two quiet beeps." |
| 0:50 to 1:02 | Close on the phone: thumb taps Fire Back, phone goes face down. | "One tap on Fire Back. An AI decoy takes over the call in the customer's own voice, with their consent. The customer is off the line." |
| 1:02 to 1:15 | Command center: decoy turns in purple; audio of the decoy asking how to pay and Ayman reading the Zelle line (B). | "The decoy stalls, plays along, and does one job: get his payout account. Here, a Zelle address he calls the 'safe account'." |
| 1:15 to 1:35 | Command center switches to the Money trail by itself (Capital One lockup). Hold 2 s on "$1,800 stopped before it reached the scammer", then the map: 7 victims into one mule account. | "In Capital One's Nessie sandbox, that stops the customer's pending $1,800 transfer. And that 'safe account' already took $18,100 from seven other people." |
| 1:35 to 1:45 | Cursor clicks "Approve · flag this account". Banner: "Scammer get scammed. He got $0." Mule tagged Flagged. | "One analyst click flags it for every customer. He got nothing." |
| 1:45 to 1:52 | Clip D: Ayman calls back, the phone stays dark, checklist ticks "rejected before it rang". | "And when he calls back, it never rings." |
| 1:52 to 2:00 | Deck slide 8 still (33 of 33), then end card: "Backfire · github.com/Proton-Designer/HackUTD26" | "On our 60 synthetic test scripts it caught 33 of 33 scams and wrongly flagged 2 of 27 look-alike legit calls. Small sample. Scammer get scammed." |

**On-screen labels (must be visible when the thing is on screen):**
- "Simulated T-Mobile network (Telnyx stands in)" during the call shots.
- "Capital One Nessie sandbox · mock bank data" during the Money trail (already in the map header).
- "Bank-wide flag: simulated payload" on the Approve shot.
- "Synthetic test set: 33 scam, 27 legit scripts" and "Test set re-scored after fixes; held-out 40: 20 of 20, 1 of 20" under the 33 of 33 still.

**Never in the video:** "Maria"; "instant" or "real-time" (say "about twelve to eighteen seconds"); "on device"
(on this path detection runs on our server); "we held the money" (say "stopped"); "real bank";
"100%". No real phone numbers other than the demo line, no wallet read aloud.

**Fallback if the live run fails at recording time:** record the command center replay
(`/command-center/?src=fixture`, press R, click Approve at the end) and label it "Recorded replay of a
test call" for its whole length. Never present the replay as live.

**Export:** 1080p, under 2:00, captions burned in (judges often watch muted), upload unlisted on
YouTube and paste the link into Devpost.
