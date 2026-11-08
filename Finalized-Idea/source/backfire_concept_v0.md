The concept (working name: Backfire)
Protect first. The moment a scam is detected, the customer is out: their line drops or gets a safe-exit prompt. They are never part of the offense.
Decoy takes over. A Nemotron voice agent picks up the conversation as a believable victim. Your research found AI honeypot callers were spotted as non-human in only about 5% of calls. The scammer called you, so you’re just talking on their call.
Extract. The decoy plays along to the “how do I pay?” step, which is where scammers have to reveal their infrastructure:
callback numbers
the website they send you to
the crypto wallet, gift card or bank account the money goes to
the script they’re using
Burn. The Nemotron agent runs a fixed set of tools on what it extracted:
What it got
What the agent does
Real or simulated
Scammer’s number
Block it network-wide and label it “Scam” for every customer, then start a carrier traceback
Simulated (CAMARA format, labeled)
Phishing website
Look up the domain’s age (often days old), then draft takedown reports to the registrar and Google Safe Browsing
Domain lookup is real (public RDAP); reports drafted
Crypto wallet
Look it up on the public blockchain to show how much it has received, then draft a freeze request to the exchange
Blockchain lookup is real and legal (it’s public data)
Gift card
Send the card number to the issuer’s fraud team so the card is frozen before they cash out
Simulated request
Script
Add its fingerprint to detection, so the same script is caught on everyone else’s calls in seconds
Real (your own detector)
Everything
Pre-fill an FTC / FBI IC3 report packet with the evidence
Real forms, drafted (Kareem’s research says the FTC site showed a shutdown notice today, so keep a copy-paste fallback)

Tell the customer what happened: “You were targeted. We took it from here. Here’s what we shut down.” That’s the “after” T-Mobile asked for.
The demo (about 90 seconds)
The scam call. The judge plays the scammer, calls “Maria” and runs a gift-card or crypto script from a card.
The hidden switch. Partway through, detection fires. Maria’s screen says “You’re safe, hang up.” The judge keeps talking, unaware.
The reveal. A teammate tells the judge: “You’ve been talking to our AI for the last 40 seconds.”
The extraction. The judge hands over the wallet or card details from their script card.
The burn. On screen, the operation comes apart in seconds: number blocked, domain flagged as “registered 3 days ago”, wallet traced on the real blockchain, script fingerprinted.
Second wow: immunity. The judge tries the same script on a second “customer”. It’s caught instantly: “Known script. This number was burned 30 seconds ago.” One attempt made everyone immune.
Metric to show: time from detection to burned infrastructure, artifacts extracted per call, and scammer-minutes wasted. Measure them across N synthetic calls you write.
Where the legal line sits
Do
Don’t
Talk only on calls and threads the scammer started
Call, text or spam the scammer’s numbers (federal robocall rules)
Give fake details (fake names, fake gift card codes)
Hack, scan, crash or flood their websites or systems (“hack back” is a federal crime)
Look up public data (domain records, public blockchains)
Publish their personal information or shame them online
Report to the companies that can act (carriers, registrars, exchanges, card issuers, FTC, IC3)
Pretend to be police, the FBI or a bank
Use synthetic data only (it’s also T-Mobile’s rule)
Threaten them, or move or “steal back” money yourselves
Keep a human in the loop for anything that freezes accounts
Let the decoy engage before detection is confident

Two honest gaps to address in the pitch:
False positives. If detection is wrong, the decoy is talking to a real caller. Only hand off above a high confidence threshold, show that confidence on screen (T-Mobile asked for “honest confidence”), and never let the decoy commit to anything.
Recording. Store the transcript and extracted details, not audio. Recording laws vary by state.
This is general guidance, not legal advice. The T-Mobile reps at the booth deal with exactly this, so it’s worth asking one: “Is there anything in this flow you’d consider out of bounds?”
Why this fits both sponsors
T-Mobile: it protects customers before (immunity), during (the instant handoff) and after (the report). And only a carrier can block numbers network-wide.
NVIDIA: it’s clearly beyond a chatbot. A voice agent plans the conversation toward a goal (get the payment details), then a tool-calling agent runs the burn sequence. It’s multi-step, uses tools, and solves a real problem.
Backfire also works as an add-on to Live Wire, not just a replacement. Live Wire’s detection becomes the trigger and Backfire is what happens next: protect first, then take the attacker’s infrastructure apart.
