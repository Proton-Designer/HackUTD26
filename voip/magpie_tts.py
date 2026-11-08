"""One-shot NVIDIA Magpie TTS -> raw PCMU 8 kHz file. Run with decoy/.venv's python (riva client lives there):
  decoy/.venv/bin/python voip/magpie_tts.py OUT.ulaw "text"
Reuses decoy.voice.Voice (enrolled clone if present, else the labeled synthetic Magpie voice). Exit 2 = no audio. Never prints the key."""
import asyncio, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

def main():
    out, text = sys.argv[1], sys.argv[2]
    from decoy.voice import Voice
    frames = asyncio.run(Voice().frames(text))
    if not frames: sys.exit(2)
    pathlib.Path(out).write_bytes(b"".join(frames))

if __name__ == "__main__":
    main()
