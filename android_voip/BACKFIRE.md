# Backfire on Demo VoIP (alternative to Telnyx)

Two phones and a laptop run the whole Backfire story with no Telnyx. **Maria's phone detects and runs the decoy; the
network routes, records and blocks.**

| Where | What | Code |
|---|---|---|
| **Maria's phone: Backfire app** (`com.example.backfire`) | Hears the **caller's** side of Demo VoIP calls (audio export), transcribes on the phone (Vosk), asks **"Is this a scam?" → yes/no** (on-device **Nemotron 3 Nano 4B** or NVIDIA cloud), shows the alert. On **Scammer Get Scammed** it runs the **decoy on the phone**: cloud Nemotron decides what to say, on-device TTS speaks it into the call | `backfire/` |
| **Both phones: Demo VoIP** (`com.example.voip`) | A dialer. Exports call audio, and lets Backfire **inject the decoy voice** in place of the mic (`ICallAudioService.startInjection` / `injectAudio`) | `app/`, `export-api/` |
| **Laptop: signaling server = the carrier** | Asks the hub before ringing (a blocked caller never rings), reports answer/hangup, ends calls on `hang_up` | `server/server.js` |
| **Laptop: hub** (P1's hub + `/android/*`) | Routing, blocklist, bus. Takes the phone's answers (`/android/report`) and records the phone-run handoff (`/android/handoff`) | `bridge/` |
| *(fallback)* **decoy peer** | Only for the old transfer path (`/decoy` on the network); not used when the phone runs the decoy | `tools/decoy_peer.py` |

```
caller ──WebRTC──► Demo VoIP (Maria) ──caller audio (AIDL)──► Backfire: Vosk STT ─► "Is this a scam?" yes/no
                         ▲                                        │   (Nemotron 4B on the phone, or NVIDIA cloud)
                         │ decoy voice injected                   ├─► alert + buttons over the call
                         │ (mic muted)                            └─► hub: risk.update / alert.fired (the answer only)
Scammer Get Scammed ─► Backfire decoy: Vosk STT ─► NVIDIA cloud Nemotron (persona, placeholders) ─► code guardrails
                       ─► fake values from code ─► Android TTS ─► Demo VoIP injection ─► caller
                       ─► hub: handoff.started, decoy.turn, decoy.fake_value, guardrail.tripped, artifacts.extracted
caller hangs up ─► call.ended ─► number blocked ─► the callback never rings
```

**Scammer Get Scammed needs a cloud model.** Backfire checks that the NVIDIA key and model answer. Without that, the
alert shows **"Scammer Get Scammed not available"** (and the notification leaves the button out). Detection still works
on the device.

## Backfire app

- **Engine tab:** **Download** buttons for the speech model (40 MB) and Nemotron 3 Nano 4B Q4_K_M (2.5 GB), a choice of
  detection engine, the NVIDIA key and model for the decoy (default: P2's pin `nvidia/nemotron-3.5-lightning-30b-a3b`),
  **Test detector** (a scam call and a dentist call, line by line, with timings) and **Speed check** (tokens/s per thread count).
- **On-device detector:** one yes/no answer. The question and system prompt are evaluated once at load; each caller
  utterance is decoded once and appended in place; a check copies the live sequence inside llama.cpp, adds ~8 end-of-turn
  tokens and reads P(yes) from one set of logits (no generation). Runs on the performance cores only.
  Measured on a Galaxy S22 (thermally throttled): ~11 tok/s prompt, ~5 tok/s decode, best at 4 threads; a check takes
  ~0.8-1.8 s plus ~1-3 s to read a new utterance; scam call p=0.97, dentist call p=0.09. Weights stay memory-mapped:
  loading them into RAM (which enables q4_K repacking) needed ~3.2 GB and got the app swapped and killed.
- **Decoy (on the phone):** persona "Margaret"; the model writes placeholders ([CARD], [SSN], [GIFTCODE]...) and code
  fills them with per-call fake values (card fails Luhn, SSN in the never-issued 9xx range) and reports `decoy.fake_value`;
  guardrails in code (no invented numbers, no authority claims, no threats, stays in persona) report `guardrail.tripped`;
  fillers mask cloud latency; the caller talking over it stops the voice (barge-in); 20-minute cap; at the end the
  extractor reports validated `artifacts.extracted` (incl. `instruction_to_ai`, #16).
- **Build with the on-device engine:**
  ```bash
  android_voip/tools/fetch_llama.sh
  cd android_voip && ./gradlew :backfire:installDebug -Pbackfire.llama=true   # NDK 28.2 + CMake 3.31.6
  ```
- Skip the 2.5 GB phone download: `adb push NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf /sdcard/Android/data/com.example.backfire/files/models/nemotron-3-nano-4b-q4_k_m.gguf`
- Install Demo VoIP **before** Backfire (signature permission), and **open Backfire once after every install** (that
  starts its background service).
- Debug builds: `adb shell am broadcast -a com.example.backfire.DEBUG_SAY -n com.example.backfire/.DebugReceiver --es text "Hello"`
  speaks a sentence into the current call (tests the injection path without the cloud).

## Run it

From the repo root on the laptop (one-time setup: `python3 -m venv .venv-hub && .venv-hub/bin/pip install -r server/requirements.txt websockets aiortc numpy`, then `cd android_voip/server && npm install`):

```bash
# 1. hub + Android routes, reachable from the phones (prints DEVICE PIN)
HUB_PORT=8000 .venv-hub/bin/python -m uvicorn android_voip.bridge.hub_app:app --host 0.0.0.0 --port 8000
#    add P3_DECOY_URL=ws://<decoy host> to use the real decoy; unset = the hub's echo decoy
#    add P2_STT_URL=ws://<p2 host> to stream the caller's audio to detection

# 2. signaling server in carrier mode
cd android_voip/server && BACKFIRE_HUB=http://127.0.0.1:8000 npm start

# 3. (only for the old transfer path) decoy peer
.venv-hub/bin/python android_voip/tools/decoy_peer.py --server ws://127.0.0.1:8090 --hub http://127.0.0.1:8000
```

Phones: install Demo VoIP on both, and Backfire on Maria's (see above). In Backfire's **Protection** tab, enter the hub
address (`http://<laptop-ip>:8000`) and the DEVICE PIN the hub printed. In **Engine**, download the models and pick an engine.
Name the scammer phone with a number-like id (e.g. `214-555-0147`). The id is its "caller ID" for routing and the blocklist.

Demo:
1. The scammer phone calls Maria. Her screen shows **🛡 Live Guard on · Caller ID not verified**.
2. Backfire transcribes and scores the caller on the phone, and alerts when the score reaches 0.8. To force an alert without a scammy caller, run:
   `curl -X POST localhost:8000/events -H 'Content-Type: application/json' -d '{"type":"alert.fired","call_id":"<id>","data":{"level":"first","why_chips":["Asks for gift cards","Claims to be IRS"]}}'`
   The call id is in the signaling server log (`[route] ... (<id>)`).
3. Maria taps **Scammer Get Scammed** (on the alert or its notification). Backfire shows **Handled for you**, and her
   phone's call screen says Backfire is talking; the scammer now hears the decoy. The scammer's call carries on with the decoy.
4. The scammer hangs up and calls again. It is rejected before ringing ("Your call can't be completed as dialed").

## Test without phones

With the three processes above running (the hub can stay on 127.0.0.1):

```bash
.venv-hub/bin/python android_voip/tools/e2e_backfire.py      # ends with RESULT: ALL PASS
```

## Env

| Var | Where | Meaning |
|---|---|---|
| `BACKFIRE_HUB` | signaling server, decoy peer | Hub base URL. Unset = plain VoIP, Backfire off. |
| `HUB_TOKEN` | all three | If the hub uses one. The carrier and decoy peer send it; the phone uses its device token. |
| `DECOY_ID`, `DECOY_SECRET` | signaling server, decoy peer | The decoy's id (default `decoy`, hidden from contacts). The secret stops a phone from registering as the decoy. |
| `P3_DECOY_URL`, `P2_STT_URL` | hub | Same as the Telnyx path (`server/relay.py`). |

## Limits (demo)
- Restore (bringing Maria back) is not implemented. The handoff is one-way, as on the Telnyx path.
- No TURN server: the phones and the laptop must share a network (the same Wi-Fi or Tailscale). Use `--stun` on the decoy peer otherwise.
- There is about a second of silence while the scammer's phone re-connects to the decoy. The decoy's opener ("Sorry, I lost you there for a second") covers it.
