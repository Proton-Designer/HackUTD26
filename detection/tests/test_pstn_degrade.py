import numpy as np
from pathlib import Path
from detection.scripts import pstn_cards as P

ROOT = Path(__file__).resolve().parents[2]


def tone(f, n=16000, a=6000):
    return (np.sin(2 * np.pi * f * np.arange(n) / 8000) * a).astype("<i2")


def test_parse_cards_finds_all_ten_with_payment_step():
    c = P.parse_cards((ROOT / "data/script-cards.md").read_text())
    assert len(c) == 10 and all(len(v[1]) >= 6 for v in c.values()) and "gift cards" in c["1"][1][4] and len(c["2"][1]) == 7


def test_bandpass_cuts_out_of_band_keeps_in_band():
    lo, mid, hi = (np.abs(np.fft.rfft(P.bandpass(tone(f).astype(float)))).max() for f in (100, 1000, 3900))
    full = np.abs(np.fft.rfft(tone(1000).astype(float))).max()
    assert mid > 0.9 * full and lo < 0.1 * full and hi < 0.2 * full


def test_level_and_speed():
    for lvl in (-20.0, -28.0):
        y = P.degrade(tone(800), lvl).astype(float)
        assert abs(20 * np.log10(P.speech_rms(y) / 32768) - lvl) < 1.5
    assert abs(len(P.degrade(tone(800), -28.0, speed=1.2)) - 16000 / 1.2) <= 2


def test_matched_words():
    assert P.matched("send the gift cards now", "Send the gift cards now.") == 1.0
    assert P.matched("send the gift cards now", "send gift") == 0.4
