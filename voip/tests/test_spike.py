from voip.spike.app import lin2ulaw, tone_frames
def test_ulaw_known():
    assert lin2ulaw(0) == 0xFF and lin2ulaw(32635) == 0x80 and lin2ulaw(-32635) == 0x00
def test_tone_frames_20ms():
    fs = tone_frames(secs=1); assert len(fs) == 50 and all(len(f) == 160 for f in fs)
