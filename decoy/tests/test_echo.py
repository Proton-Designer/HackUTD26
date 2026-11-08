"""#131: our own words echoing into a caller line are stripped, the caller's words kept."""
import sys
sys.path.insert(0, ".")
from decoy.app import Session


class _S:
    said = ["I can't find my phone right now.", "Who did you say was calling?"]


def test_strip_echo():
    f = Session.strip_echo
    assert f(_S(), "I can't find my phone right now. Are you talking about the Zelle transfer?") == "Are you talking about the Zelle transfer?"
    assert f(_S(), "Send it by Zelle to refunds dot dept at backfire dash demo dot example.") == \
        "Send it by Zelle to refunds dot dept at backfire dash demo dot example."
    assert f(_S(), "who did you say was calling") == ""
    assert f(_S(), "Who did I say? Your bank.") == "Who did I say? Your bank."   # 2-word overlap is not echo


def test_strip_note_echo():
    from decoy.app import strip_note_echo
    assert strip_note_echo("What should I do next?\nprivate steering note: have callback_phone.") == "What should I do next?"
    assert strip_note_echo("Okay. (Hidden context for your next reply: Already got: x)") == "Okay."
    assert strip_note_echo("Okay, which app?\n\nAlready got: callback_phone. About 5 turns left.") == "Okay, which app?"
    assert strip_note_echo("Hidden context for your next reply (never say it): react") is None
    assert strip_note_echo("I've got a note right here, go ahead.") == "I've got a note right here, go ahead."


def test_strip_note_echo_live_shapes():   # #135 shapes P2 saw on the bolt fallback
    from decoy.app import strip_note_echo
    assert strip_note_echo("Okay, what's next? [private] Have: None.") == "Okay, what's next?"
    assert strip_note_echo("Sure. [Private] Have: nothing yet. Need: handle") == "Sure."
    assert strip_note_echo("Right. (private) Got: payment app.") == "Right."
    assert strip_note_echo("Okay, I'm listening. Have: None.") == "Okay, I'm listening."
    assert strip_note_echo("I have a pen, go ahead.") == "I have a pen, go ahead."
    assert strip_note_echo("I've got my card here. What do I need to type?") == "I've got my card here. What do I need to type?"
