# Demo VoIP

Phone-to-phone voice calls over Wi-Fi (WebRTC), with **live call audio exported to your other apps**.

```
server/       Node signaling server (runs on your laptop)
app/          The calling app            (com.example.voip)
export-api/   Shared AIDL contract for apps that want call audio
consumer/     Sample receiver app        (com.example.voip.consumer) – records both sides to WAV
bridge/       Backfire hub routes        (carrier events, caller audio, decoy handoff) – see BACKFIRE.md
```

**Backfire:** this app can stand in for Telnyx in the Backfire demo (Live Guard, Scammer Get Scammed, decoy handoff,
callback blocking). See [BACKFIRE.md](BACKFIRE.md).

## Run it

1. **Start the server on the laptop**
   ```
   cd server && npm install && npm start
   ```
   It prints the `ws://<laptop-ip>:8090` URLs. Phones must be on the same Wi-Fi (or the same Tailscale network).
   If your firewall blocks it: `sudo ufw allow 8090/tcp` (or the equivalent).

2. **Build and install.** JDK 21 is in `~/.jdks/jdk-21.0.13+9` and the SDK is in `~/Android/Sdk`
   (`local.properties` points at it). Plug in a phone with USB debugging on, then:
   ```
   export JAVA_HOME=~/.jdks/jdk-21.0.13+9
   ./gradlew :app:installDebug          # on both phones
   ./gradlew :consumer:installDebug     # on the phone(s) where you want audio exported
   ```
   With two phones plugged in at once, add `-Pandroid.injected.device.serial=<serial>` or install the APKs
   with `~/Android/Sdk/platform-tools/adb -s <serial> install -r app/build/outputs/apk/debug/app-debug.apk`.
   Install `app` **before** `consumer`. The audio permission is signature-level, so it is only granted
   if the defining app is already installed and both are signed with the same key (debug builds on one machine are).

3. On each phone, open **Demo VoIP**, pick a name, check the server URL, and tap **Go online**.
   Either phone can call the other from **Contacts** (or **Recents**). On Android 14+, tap **Allow** on the
   banner so incoming calls can take over the lock screen.

   Phone-style behaviour: ringtone and vibration on the callee, ringback and busy tones on the caller,
   full-screen incoming and in-call screens, mute, speaker, automatic Bluetooth/wired headset routing,
   screen-off at the ear, a 45 s no-answer timeout, "Reconnecting…" on network blips, call history,
   missed-call notifications, and "busy" if you're already on a call.

4. Open **Call Audio Receiver** on either phone. During a call it shows live levels for both sides
   and writes `…_local.wav` (your mic) and `…_remote.wav` (the other person). To copy them off:
   ```
   adb pull /sdcard/Android/data/com.example.voip.consumer/files/calls/
   ```

## iPhone (or any browser): the web phone

`server/web/index.html` is Demo VoIP as a web page, speaking the same signaling protocol, so an iPhone can call an
Android phone (and the other way round). No App Store, no Mac, no Xcode. The server serves it on the same port as
signaling. It supports the Backfire carrier role as the **caller** (it follows `transfer` to the decoy silently), so
the judge can play the scammer on an iPhone. Backfire itself (Live Guard, the decoy) still runs only on Android.

iOS only allows the microphone on **https**, so expose the server through a tunnel:
```
sudo pacman -S cloudflared                     # once (macOS: brew install cloudflared)
cd server && npm start                         # signaling + web phone on :8090
cloudflared tunnel --url http://localhost:8090 # prints https://<random>.trycloudflare.com
```
On the iPhone: open that https URL in **Safari** → pick a name → **Go online** → allow the microphone → tap
**Call** next to the Android phone's name. For an app icon: Share → **Add to Home Screen**.
The Android phones keep using `ws://<laptop-ip>:8090` (or `wss://<random>.trycloudflare.com`).

Limits (web, not native): iOS pauses the page when it is in the background or the screen locks, so keep it open
with the screen on (it requests a screen wake lock); there's no ringing while closed and no earpiece/speaker toggle.
The call audio itself is peer to peer (STUN only, like the Android app), so both phones should be on the same Wi-Fi.

## Receiving call audio in your own app

Add the `:export-api` module as a dependency, request the permission, and bind:

```xml
<uses-permission android:name="com.example.voip.permission.CALL_AUDIO" />
<queries><package android:name="com.example.voip" /></queries>
```

```kotlin
val listener = object : ICallAudioListener.Stub() {
    override fun onCallStarted(callId: String, peerId: String, outgoing: Boolean) {}
    override fun onAudioFrame(callId: String, source: Int, pcm16: ByteArray,
                              sampleRate: Int, channels: Int, timestampMs: Long) {
        // source == VoipExport.SOURCE_LOCAL (my mic) or SOURCE_REMOTE (other person)
        // pcm16 = ~10 ms of 16-bit little-endian PCM
    }
    override fun onCallEnded(callId: String, reason: String) {}
}
bindService(VoipExport.bindIntent(), object : ServiceConnection {
    override fun onServiceConnected(n: ComponentName, b: IBinder) =
        ICallAudioService.Stub.asInterface(b).registerListener(listener)
    override fun onServiceDisconnected(n: ComponentName) {}
}, Context.BIND_AUTO_CREATE)
```

Callbacks are `oneway` and arrive on a Binder thread, so hand heavy work (encoding, network upload) to your own thread.

**Bind from a foreground service, not an activity.** Android freezes apps in the background. If a frozen app keeps
receiving ~200 audio frames a second, Android kills it ("Async binder space running out while frozen").
`consumer/RecorderService.kt` shows the pattern.

## How it works

- **Signaling:** WebSocket JSON messages (`register`, `offer`, `answer`, `ice`, `bye`, `reject`) relayed by `server/server.js`.
- **Media:** WebRTC/Opus, peer-to-peer on the LAN. There is no TURN server, so calls across different restrictive networks may fail.
- **Audio tap:** the local mic comes from `JavaAudioDeviceModule.setSamplesReadyCallback`, and remote audio comes from
  an `AudioTrackSink` on the received track. Both go to `AudioBus`, and `AudioExportService` forwards them over Binder.
- **Staying reachable:** `CallService` is a microphone foreground service that holds the WebSocket open, so calls
  ring with the app closed. It's started from the UI because Android only allows mic foreground services to start from the foreground.

## Demo limitations

- No push notifications (FCM): a phone is only reachable while "online" (the foreground service is running).
- No authentication: anyone who can reach the server can register any name.
- Signaling is unencrypted `ws://`. The media itself is encrypted (DTLS-SRTP).

## Testing without a second phone

`tools/testpeer.py` is a laptop-side peer that speaks the same protocol, sends a 440 Hz tone and records what it receives:

```
python -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/testpeer.py --server ws://127.0.0.1:8090 --mode answer            # phone calls it
.venv/bin/python tools/testpeer.py --server ws://127.0.0.1:8090 --mode call --target emu # it calls the phone
```
Options: `--decline`, `--cancel N` (hang up after N s of ringing), `--talk N`, `--ring N`.
The tone shows up in the receiver app's `…_remote.wav`.
