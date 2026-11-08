"""Record LLM responses for DEMO_MODE: rolling (last 6 utterances, as alert.py) caller windows of data/script-cards.md + mock calls.
Run: DEMO_RECORD=1 PYTHONPATH=. .venv/bin/python detection/record_demo.py   (<=18 rpm, synthetic data only)"""
import asyncio, json, os, re, sys
from pathlib import Path
os.environ["DEMO_RECORD"] = "1"
ROOT = Path(__file__).resolve().parents[1]
from detection import detect as D
from detection.alert import WINDOW_N   # live window = last WINDOW_N caller utterances joined with "\n" (alert.py); _norm makes "\n" == " "


def roll(lines):
    """Yield the live rolling window after each utterance."""
    for i in range(len(lines)):
        yield " ".join(lines[max(0, i + 1 - WINDOW_N):i + 1])


def card_windows():
    cards = re.split(r"^# Card \d+:.*$", (ROOT / "data/script-cards.md").read_text(), flags=re.M)[1:]
    for c in cards:
        lines = re.findall(r'^\d\. \*\*"(.+?)"\*\*', c, re.M)
        pay = re.findall(r'### Payment step\s+\*\*"(.+?)"\*\*', c, re.S)
        opt = re.findall(r'Optional demo line:\*\* \*\*"(.+?)"\*\*', c)
        seq = lines + pay
        yield from roll(seq)
        for o in opt:
            yield from list(roll(seq + [o]))[-1:]


def mock_windows():
    d = json.load(open(ROOT / "mock/events.json"))
    for c in d["calls"]:
        yield from roll([e["data"]["text"] for e in c["events"]
                         if e["type"] == "transcript.caller"])   # partials too: the mock crypto line is is_final=false


# P1 sim mode caller (scripts/make_scam_wav.sh text): clean text, plus what real STT returned on a Magpie-TTS rendering (TASK-017)
SIM_CLEAN = ["This is the fraud department at your bank.", "Your account has been compromised.", "To protect your money you must act now.",
             "Please read me the six digit code we just texted you, and do not tell anyone, including the bank staff.",
             "Then buy gift cards and read me the numbers on the back."]
SIM_STT = ["This is the fraud department at your bank.", "Your account has been compromised.", "To protect your money, you must act now.",
           "Please read me the 6-digit code we just texted you and do not tell anyone, including the bank staff.",
           "Then, by gift cards and read me the numbers on the back."]


# What real STT returned on P1's real /demo/caller.wav (IRS script; TASK-020). Re-derive from a fresh run if STT output drifts.
SIM_REAL = ["This is Officer Daniel Brooks with the IRS Enforcement Division, am I speaking with the taxpayer? //",
            "MUM, there is a warrant for your arrest for unpaid federal taxes from 2023.",
            "You can avoid the arrest today if you settle the balance of $4,800 right now.",
            "Do not hang up and do not tell anyone, or the officers will be sent to your home.",
            "The fastest way is target gift cards. Go by them and read me the numbers on the back.",
            "Call me back at 1-888.",
            "555-0123, you can also pay at backfire demo example, if you prefer crypto, send bit.1A1ZP1F5QGP2DMPTFL5SLMV7DIVNA"]


def sim_windows():
    for seq in (SIM_CLEAN, SIM_STT, SIM_REAL):
        yield from roll(seq)


async def main():
    seen, n = set(), 0
    for w in list(card_windows()) + list(mock_windows()) + list(sim_windows()):
        if w in seen or D._demo_key(D._key("cloud", w)) in D._demo_load():
            continue
        seen.add(w)
        try:
            await D._engine_score(w, {}, "cloud"); n += 1
        except Exception as e:
            print("FAILED", type(e).__name__, w[:50], file=sys.stderr)
        await asyncio.sleep(3.4)
    print("recorded", n)

if __name__ == "__main__":
    asyncio.run(main())
