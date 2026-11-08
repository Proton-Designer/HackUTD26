"""#127: playbook classifier, targets, bail signals (no network)."""
import sys
sys.path.insert(0, ".")
from decoy import playbooks as PB


def test_classify_cards():
    assert PB.classify(["Hi, this is the fraud team at your bank.", "Someone's draining your account right now."]) == "bank"
    assert PB.classify(["This is Officer Daniel Brooks with the IRS Enforcement Division.", "There is a warrant for your arrest."]) == "irs_gov"
    assert PB.classify(["Good evening! I'm Michael with Apex Digital Assets.", "Our crypto platform gets 30 percent returns."]) == "crypto"
    assert PB.classify(["Hi, this is Kevin from Microsoft Windows support.", "Your computer has a virus."]) == "tech_support"
    assert PB.classify(["Grandma, it's me, I'm in jail.", "Please don't tell mom, I need bail."]) == "grandparent"
    assert PB.classify(["Hello, how are you today?"]) == "generic"


def test_reclassify_needs_clear_lead():
    lines = ["Hi, this is the fraud team at your bank.", "Someone's draining your account right now."]
    assert PB.classify(lines + ["A police officer will call you."], "bank") == "bank"       # one stray word: stay
    # card 8 'bank plus police' is still a bank cash-out: stays bank
    assert PB.classify(lines + ["This is Detective Ray Daniels, police. Don't tell the branch."], "bank") == "bank"
    # a real change of story switches
    assert PB.classify(lines + ["Actually your computer is hacked, I'm with Microsoft support.",
                                "Install AnyDesk so our technician can remove the virus and malware."], "bank") == "tech_support"


def test_missing_and_note():
    arts = [{"kind": "callback_phone", "value": "+18885550123"}, {"kind": "domain", "value": "backfire-demo.example"}]
    assert PB.missing("bank", arts)[0] == "payment_handle"
    n = PB.note("bank", arts, 4, "Wait, send it to who exactly?")
    assert "callback_phone" in n and "payment app" in n and "Turns left: 4" in n
    assert PB.missing("bank", arts + [{"kind": "payment_handle", "rail": "zelle", "id": "x@y.z"}]) == ["impersonated_org"]


def test_bail_signals():
    assert PB.SUSPICION.search("Wait, are you a robot? Who is this really?")
    assert PB.SUSPICION.search("Is this a recording?")
    assert not PB.SUSPICION.search("Open your banking app and send the money by Zelle.")
    assert PB.HOSTILE.search("Listen you idiot, just do it")
    assert PB.REFUSAL.search("Why do you need to know that?") and PB.REFUSAL.search("Just do what I tell you.")
    assert not PB.REFUSAL.search("Our secure line is 1-888-555-0123.")
    assert set(PB.GOODBYES) >= {"got_payment_details", "time_cap", "no_progress", "suspicion", "hostile", "refused", "silence"}
