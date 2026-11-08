"""P3 decoy playbooks (#127): classify the scam from what the caller says, go after that scam's cash-out artifacts in
priority order, and know when to bail. Data, not prose: the per-turn note given to the model is built from this.

Types follow the FTC / FBI IC3 top phone-scam categories and our judge cards (data/script-cards*.md).
Target names are extractor artifact kinds (decoy/core.py EXTRACT_PROMPT); "site" = domain or url.
Pull lines never name an app, payee or address the caller hasn't said (core.SYSTEM rule): the model only repeats theirs.
"""
from __future__ import annotations

import re

# What a target means, for the note ("Still need: ...").
TARGET_HINT = {
    "payment_handle": "the exact payment app and the handle/email/phone to send to",
    "gift_card_brand": "which gift card brand, how much, and how to give them the codes",
    "wallet": "the crypto wallet address (have them read it slowly)",
    "site": "the exact website to go to (have them spell it)",
    "callback_phone": "a number to call them back on",
    "remote_app": "the name of the app they want installed",
    "impersonated_org": "who exactly they are with",
}

# Generic natural ways to ask for each target (model uses its own words; these are ideas). No app names.
PULLS = {
    "payment_handle": ["Okay, which app do I use for that, and what do I put in the 'send to' box?",
                       "Wait, send it to who exactly? Can you spell that for me, slowly?",
                       "Is it an email or a phone number I'm sending it to? Read it to me again."],
    "gift_card_brand": ["Which kind of gift card, does it matter which store?",
                        "Okay, and once I have the cards, how do I give you the numbers?",
                        "How many cards, and what amount on each one?"],
    "wallet": ["The address is so long, can you read it to me slowly, a few letters at a time?",
               "Where do I send the coins to? Read me the address again."],
    "site": ["What's the website again? Spell it for me, I'm typing it in.",
             "Is that dot com, or something else? Say the whole thing one more time."],
    "callback_phone": ["If we get cut off, what number do I call you back on?",
                       "Give me your direct number, in case my phone drops you."],
    "remote_app": ["What's the name of the app you want me to put on? Spell it.",
                   "Where do I get that program from, what do I type in?"],
    "impersonated_org": ["Sorry, which department did you say you're with?"],
}

PLAYBOOKS: dict[str, dict] = {
    "bank": {"label": "bank fraud team / safe account / Zelle reversal",
             "targets": ["payment_handle", "callback_phone", "site", "impersonated_org"],
             "keywords": ["fraud department", "fraud team", "fraud prevention", "your bank", "your account", "safe account",
                          "protected account", "zelle", "debit card", "checking", "savings", "wire", "reversal",
                          "suspicious charge", "branch", "draining", "overdraft", "deposit", "loan", "transfer"]},
    "irs_gov": {"label": "IRS / government / police warrant",
                "targets": ["gift_card_brand", "payment_handle", "wallet", "callback_phone", "site"],
                "keywords": ["irs", "internal revenue", "tax", "warrant", "arrest", "officer", "sheriff", "police",
                             "federal", "court", "jury duty", "badge", "enforcement", "deputy"]},
    "ssa_medicare": {"label": "Social Security / Medicare benefits",
                     "targets": ["payment_handle", "gift_card_brand", "callback_phone", "site"],
                     "keywords": ["social security", "medicare", "benefits", "ssn suspended", "medicaid", "new card",
                                  "benefit card", "ssa"]},
    "tech_support": {"label": "tech support / virus / refund",
                     "targets": ["remote_app", "site", "payment_handle", "gift_card_brand", "callback_phone"],
                     "keywords": ["microsoft", "windows", "apple", "computer", "virus", "hacked", "malware", "anydesk",
                                  "teamviewer", "remote", "technician", "support", "firewall", "ip address", "refund"]},
    "crypto": {"label": "crypto / investment",
               "targets": ["wallet", "site", "payment_handle", "callback_phone"],
               "keywords": ["crypto", "bitcoin", "btc", "ethereum", "coinbase", "investment", "returns", "portfolio",
                            "trading", "platform", "profit", "wallet", "usdt", "digital assets"]},
    "grandparent": {"label": "family emergency / grandchild / bail",
                    "targets": ["payment_handle", "gift_card_brand", "callback_phone", "wallet"],
                    "keywords": ["grandma", "grandpa", "grandson", "granddaughter", "it's me", "accident", "jail", "bail",
                                 "lawyer", "attorney", "don't tell mom", "don't tell dad", "hospital", "in trouble"]},
    "utility": {"label": "utility shut-off",
                "targets": ["payment_handle", "gift_card_brand", "wallet", "callback_phone", "site"],
                "keywords": ["power company", "electric", "utility", "disconnect", "shut off", "shutoff", "meter",
                             "gas company", "water bill", "past due", "service will be"]},
    "delivery": {"label": "package / delivery fee",
                 "targets": ["site", "payment_handle", "callback_phone"],
                 "keywords": ["package", "delivery", "parcel", "shipment", "usps", "ups", "fedex", "dhl", "courier",
                              "customs", "redelivery", "tracking"]},
    "prize": {"label": "prize / lottery / sweepstakes",
              "targets": ["payment_handle", "gift_card_brand", "wallet", "callback_phone", "site"],
              "keywords": ["won", "winner", "prize", "lottery", "sweepstakes", "jackpot", "claim", "processing fee",
                           "publishers clearing", "congratulations"]},
    "job": {"label": "job / employment / overpayment",
            "targets": ["payment_handle", "site", "wallet", "callback_phone"],
            "keywords": ["job", "position", "recruiter", "hiring", "remote work", "work from home", "interview",
                         "training fee", "equipment", "salary", "onboarding", "overpaid", "check"]},
    "generic": {"label": "unknown scam",
                "targets": ["payment_handle", "site", "callback_phone", "gift_card_brand", "wallet"],
                "keywords": []},
}


def classify(lines: list[str], current: str = "generic") -> str:
    """Keyword score over the caller's lines, recent lines weighted up. Re-classifies only when another type clearly
    leads (so one stray word doesn't flip the playbook)."""
    if not lines:
        return current
    scores = {k: 0.0 for k in PLAYBOOKS}
    n = len(lines)
    for i, line in enumerate(lines[-8:]):
        t = " " + re.sub(r"[^a-z0-9' ]", " ", line.lower()) + " "
        w = 1.0 + 0.5 * (i >= len(lines[-8:]) - 2)       # the last two lines count 1.5x (story changes)
        for k, pb in PLAYBOOKS.items():
            for kw in pb["keywords"]:
                if f" {kw} " in t:
                    scores[k] += w * (1.5 if " " in kw else 1.0)   # phrases are stronger evidence than single words
    best = max(scores, key=scores.get)
    if scores[best] < 1.0 or n == 0:
        return current
    if current != "generic" and best != current and scores[best] < scores.get(current, 0) + 1.5:
        return current
    return best


def have(arts: list[dict]) -> set[str]:
    """Targets satisfied by the haul ('site' = domain or url)."""
    out = set()
    for a in arts:
        k = a.get("kind")
        out.add("site" if k in ("domain", "url") else k)
    return out


def missing(scam: str, arts: list[dict]) -> list[str]:
    got = have(arts)
    return [t for t in PLAYBOOKS.get(scam, PLAYBOOKS["generic"])["targets"] if t not in got]


def note(scam: str, arts: list[dict], turns_left: int, pull: str | None) -> str:
    """The short per-turn steering note for the model (kept out of the stored history)."""
    pb = PLAYBOOKS.get(scam, PLAYBOOKS["generic"])
    got = sorted(have(arts) & set(pb["targets"]) | ({"impersonated_org"} & have(arts)))
    need = [t for t in missing(scam, arts) if t != "impersonated_org"]
    parts = [f"Scam type: {pb['label']}.", f"Have: {', '.join(got) or 'nothing yet'}."]
    if need:
        parts.append(f"Still need (next): {TARGET_HINT[need[0]]}.")
        # P1 08:09: no verbatim pull phrase (the model parroted 'send-to box' in 6 of 12 replies); and no naming
        # an app or payee before the caller does (SYSTEM already says so)
    else:
        parts.append("You have what you need: keep it short and friendly.")
    parts.append(f"Turns left: {turns_left}.")
    return "[steering note, private] " + " ".join(parts)


# ---------------------------------------------------------------- bail signals (#127 5d)
SUSPICION = re.compile(r"\b(robot|a bot|bot\b|an ai|artificial|a recording|recorded|machine|automated|not a real person|"
                       r"are you (real|human|a person)|who is this really|who am i (really )?talking to|scam ?bait(er|ing)?|"
                       r"you're wasting my time|stop wasting|i know what you're doing|nice try)", re.I)
HOSTILE = re.compile(r"\b(fuck|f\*+|shit|bitch|asshole|idiot|stupid|dumb|moron|shut up|screw you)\b", re.I)
REFUSAL = re.compile(r"\b(i (can't|cannot|won't|will not) (tell|give|spell|say)|why do you (need|want) (to know|that)|"
                     r"just do (it|what i (say|tell you))|stop asking|doesn't matter|that's not important|"
                     r"i already (told|said)|forget (about )?(it|that))\b", re.I)

GOODBYES = {
    "got_payment_details": "Okay, I've got all of that written down. I'm going to go take care of it right now. Bye bye.",
    "time_cap": "Oh, someone's at the door, I'm so sorry, I have to go. I'll call you right back, okay? Bye now.",
    "no_progress": "You know what, I'm getting confused, let me go find my son and have him help me. Bye now.",
    "suspicion": "Oh, I don't know about all this anymore. I'm going to go talk to my family first. Bye.",
    "hostile": "Okay, I don't like how you're talking to me. I'm going to hang up now. Bye.",
    "refused": "Well, if you can't tell me that, I don't think I can do this. I'm going to hang up. Bye.",
    "silence": "Hello? Hello? I can't hear you anymore. I'm going to hang up now. Bye.",
}
