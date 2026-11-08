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


async def main():
    seen, n = set(), 0
    for w in list(card_windows()) + list(mock_windows()):
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
