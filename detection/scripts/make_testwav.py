"""Generate the SYNTHETIC test call WAV (NVIDIA Magpie TTS, 8 kHz mono) -> detection/testdata/scam_call_synth.wav.
Needs NVIDIA_API_KEY in env or .env. Synthetic voice, fictional scam script, no real person or number."""
import os, sys, wave, riva.client
from pathlib import Path
LINES = ["Hello, this is Agent Collins from the Internal Revenue Service.",
         "There is a warrant in your name for unpaid taxes.",
         "You must pay today with gift cards, and do not tell anyone, or you will be arrested.",
         "Read me the numbers on the back of the cards now."]
def main(out):
    key = os.environ.get("NVIDIA_API_KEY")
    if not key:
        from dotenv import dotenv_values
        key = dotenv_values(Path(__file__).resolve().parents[2] / ".env").get("NVIDIA_API_KEY")
    auth = riva.client.Auth(None, True, "grpc.nvcf.nvidia.com:443", [["function-id", "877104f7-e885-42b9-8de8-f6e4c6303969"], ["authorization", "Bearer " + key]])
    tts = riva.client.SpeechSynthesisService(auth)
    sil = b"\x00\x00" * 8000 * 1
    pcm = b"\x00\x00" * 4000
    for l in LINES:
        r = tts.synthesize(l, language_code="en-US", sample_rate_hz=8000, voice_name="Magpie-Multilingual.EN-US.Mia")
        pcm += r.audio + sil
    w = wave.open(out, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(pcm); w.close()
    print("wrote", out, len(pcm) / 16000, "s")
if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "detection/testdata/scam_call_synth.wav")
