# Backfire: how to test it (teammates)

Everything runs on the live hub on Ayman's Mac. You only need two phones (or a phone and a laptop).

| What | Where |
|---|---|
| Customer app (the protected person) | https://reg-subjects-curriculum-whenever.trycloudflare.com |
| Command center (carrier / bank view) | https://reg-subjects-curriculum-whenever.trycloudflare.com/command-center/ (Ctrl+F5 to reload) |
| Scam line (call this) | **+1 (469) 908-8594** |
| Pairing PIN | ask Ayman (never post it in GitHub or Discord; the repo is public) |

The tunnel URL can change if the hub machine changes networks; Ayman posts the new one.

## 1. Set up the customer app (once per phone)
1. Open the customer app link on your phone (Safari or Chrome).
2. Enter the pairing PIN.
3. Optional: Share -> **Add to Home Screen**, then open it from the icon (full screen, like an app).
4. Onboarding: turn on Backfire, then **set up your voice**: quiet room, phone ~20 cm from your mouth, not on a call, no Bluetooth headset. Look for "recording quality: good"; if it says phone quality, record again.
   - For a more natural clone, try the conversational version: add `?enroll=talk` to the link and answer the questions out loud instead of reading.
5. Keep the app open with the screen on during calls (iPhones pause background web pages). **Wear earphones** on the customer phone.

## 2. Run a test call (two people)
- **Customer**: the paired phone, app open, earphones in.
- **Scammer**: any other phone, normal dialer, held to the ear (not speaker), **caller ID on**, speak **English**.

1. Scammer calls **+1 (469) 908-8594**. The customer's app rings (Answer / Decline). Customer taps **Answer**.
2. Scammer reads the **Judge card** (top of `data/script-cards.md`), line 1:
   "Hi, this is the fraud team at your bank. Someone's draining your account right now. To protect your savings, you need to move them to a safe account. And don't tell anyone at the branch."
3. About 8-18 s in, the customer's app beeps and shows **"This call may be a scam"**. Customer taps **Fire Back**.
4. Backfire's decoy now talks to the scammer in the customer's cloned voice. Scammer continues:
   - "Our secure line is 1-888-555-0123, and the transfer portal is backfire-demo dot example."
   - Last: "Open your banking app and send the $1,800 by Zelle to refunds dot dept at backfire dash demo dot example. That's the safe account."
5. Keep talking until the decoy says goodbye and ends the call.
6. Wait 3+ minutes, then call again **from the same phone**: it should be rejected before it rings.

## 3. What to check
- Customer app: real ringing (no auto-answer), clear audio, alert with chips, Fire Back -> "Backfire has the call", "Listening to the decoy" works.
- Scammer phone: customer's voice clear, no echo of yourself; decoy speaks within ~2 s, sounds like the customer, natural (no metallic buzz), doesn't talk over you, never switches voice, wraps up.
- Command center: live (no REPLAY / RECONNECTING badge); transcript and risk move; after the call: payment details, number blocked, **Money trail** "$1,800 stopped", 7 victims -> mule -> cash-out; click **Approve** -> "Scammer get scammed. He got $0."; callback shows "rejected before it rang".
- Note the time of anything odd and post it in the team chat; P1 matches it to the call report.

## Rules (please follow)
- **One test call at a time**, at least 3 minutes apart. Never automate calls (the Telnyx account was once flagged for automated calling).
- Don't add real numbers to the app's Do Not Screen list.
- Between demos, P1 resets the demo state (`POST /demo/reset`); ask Ayman if the money trail or a block looks stale.
- No phone line? Phone-free demo: `scripts/demo_call --reset` on the hub machine (see `docs/DEMO_DAY_RUNBOOK.md`).
