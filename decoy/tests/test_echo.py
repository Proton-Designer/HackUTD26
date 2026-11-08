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
