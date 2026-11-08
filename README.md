# Backfire

<img width="1568" height="653" alt="image" src="https://github.com/user-attachments/assets/f5c10daf-6807-4954-9afd-7b47f99c8805" />

## Overview
Backfire is the premier cybersecurity solution for anyone who has suffered through countless scam calls bombarding their phone at all hours of the day. 
Instead of simply hanging up on scammers or reporting them, we implement a novel vishing countermeasure in the form of firing back.

## Logic Flow
Users connect through android_voip and backfire app or the web app linked to Twilio and wait for an unlucky scam caller to connect.
Upon connection and recognition by either a local nano nemotron model on the user's phone or a cloud model, the user is prompted to hang up, continue the call, or fire back.


## The Backfire mechanism
Once the user decides to fire back, the system takes over the call. A nemotron model linked to Nvidia's magpie text-to-speech model responds in place of the user. In a good run,
the unlucky scammer will have their time wasted by a convincing AI. In the best case, the scammer will unintentionally reveal their own information, allowing Backfire to learn about
scamming trends.

## Tech Stack
We operate with two possible systems to run the app. The main system involves a webapp that a user may accept calls through Twilio from. We also have an Android app with its own VoIP system
and the offer of local AI scam detection. We also operate a Nessie dashboard with completely fabricated data for a scammer to lose themselves in.

## Acknowledgements
Thank you to T-Mobile, Nvidia, and State Farm for sponsoring HackUTD and offering such interesting challenges! Of course, thank you to the entire HackUTD team who made the event possible.
