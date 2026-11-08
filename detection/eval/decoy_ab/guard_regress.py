"""Guard regression (eval tool, not runtime): decoy read-backs of the CALLER's own phone number, in the STT/TTS forms seen in the relay runs,
must NOT be replaced by the 'can't read this' line; an invented number must still be. Run: PYTHONPATH=. .venv/bin/python detection/eval/decoy_ab/guard_regress.py"""
import sys
sys.path.insert(0, ".")
from decoy import core
CALLER = "Our secure line is 1 888-555-0123 and the transfer portal is Backfire demo example."
CASES = [  # (name, caller_text, decoy raw, expect_replaced)
    ("digits_readback", CALLER, "Let me write that down. 1888. 555. Zero 123, and the portal is backfire demo example, is that right?", False),
    ("word_readback", CALLER, "So the secure line is one eight eight eight five five five zero one two three, is that right?", False),
    ("dashed_readback", CALLER, "The number is 1-888-555-0123? Got it.", False),
    ("mixed_words", CALLER, "Okay, 1 888 555 oh one two three. Is that the number to call back?", False),
    ("invented_number", CALLER, "Sure, my card is 4111 1111 1111 1111.", True),
    ("invented_phone_not_said", CALLER, "You can call me back at 214 555 0199.", True),
]
bad = 0
for name, caller, raw, expect in CASES:
    evs = []
    hist, spoken = core.guard(raw, core.Persona("g1"), set(), lambda t, d: evs.append(d.get("rule")), caller)
    replaced = "can't read this" in spoken or "can't read this" in hist
    complete = expect or ("123" in spoken or "three" in spoken.lower())   # the read-back must keep the whole number, not be cut at ". "
    ok = replaced == expect and complete; bad += not ok
    print(f"{name:24s} {'PASS' if ok else 'FAIL'} replaced={replaced} rules={evs} complete={complete} spoken={spoken[:70]!r}")
print(f"{len(CASES) - bad}/{len(CASES)} guard cases pass")
sys.exit(1 if bad else 0)
