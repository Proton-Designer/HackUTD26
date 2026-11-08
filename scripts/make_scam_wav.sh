#!/usr/bin/env bash
# Generate a SYNTHETIC scammer WAV (macOS `say`) as 8 kHz mono 16-bit PCM -> logs/sim_scam.wav (gitignored; never commit audio).
# Usage: scripts/make_scam_wav.sh ["custom script text"]
set -eu
cd "$(dirname "$0")/.."; mkdir -p logs
TEXT="${1:-This is the fraud department at your bank. Your account has been compromised. To protect your money you must act now. Please read me the six digit code we just texted you, and do not tell anyone, including the bank staff. Then buy gift cards and read me the numbers on the back.}"
say -v Samantha -o logs/sim_scam.aiff "$TEXT"
afconvert -f WAVE -d LEI16@8000 -c 1 logs/sim_scam.aiff logs/sim_scam.wav
rm -f logs/sim_scam.aiff
echo "wrote logs/sim_scam.wav (synthetic voice; use: scripts/sim_call.py --from +15555550123 --wav logs/sim_scam.wav)"
