from detection import schema

def test_normalize_valid_and_clamped():
    o = schema.normalize({"s": 7, "asks": ["gift_card", "bogus"], "stage": "x", "impersonates": "IRS", "addresses_ai_system": "true"})
    assert o["s"] == 1.0 and o["band"] == "critical" and o["asks"] == ["gift_card"]
    assert o["stage"] == "opening" and o["addresses_ai_system"] is True
    assert "Claims to be IRS" in o["why_chips"] and "Talks to the AI" in o["why_chips"]

def test_normalize_garbage_never_raises():
    for g in (None, [], "x", {"s": "nan"}, {"asks": "otp"}):
        assert schema.normalize(g)["band"] == "low"

def test_bands():
    assert [schema.band(x) for x in (0.39, 0.4, 0.79, 0.8, 0.949, 0.95)] == ["low", "watch", "watch", "high", "high", "critical"]


def test_negative_chips_filtered():
    out = schema.normalize({"s": 0.1, "why_chips": ["No pin ask", "Not urgent", "Never asks for codes", "Urgent threat", "No"]})
    assert out["why_chips"] == ["Urgent threat"]
