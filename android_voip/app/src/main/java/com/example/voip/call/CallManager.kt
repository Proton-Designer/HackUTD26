package com.example.voip.call

import android.content.Context
import android.util.Log
import com.example.voip.export.AudioBus
import com.example.voip.export.Injector
import com.example.voip.export.VoipExport
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import org.json.JSONObject
import org.webrtc.AudioSource
import org.webrtc.AudioTrack
import org.webrtc.AudioTrackSink
import org.webrtc.DataChannel
import org.webrtc.IceCandidate
import org.webrtc.MediaConstraints
import org.webrtc.MediaStream
import org.webrtc.PeerConnection
import org.webrtc.PeerConnectionFactory
import org.webrtc.RtpTransceiver
import org.webrtc.SdpObserver
import org.webrtc.SessionDescription
import org.webrtc.audio.JavaAudioDeviceModule
import java.util.UUID
import java.util.concurrent.Executors
import java.util.concurrent.ScheduledFuture
import java.util.concurrent.TimeUnit

enum class Connection { DISCONNECTED, CONNECTING, CONNECTED }

sealed interface CallState {
    data object Idle : CallState
    /** We sent an offer and the other phone is ringing. */
    data class Outgoing(val callId: String, val peer: String) : CallState
    /** Someone is calling us. */
    data class Incoming(val callId: String, val peer: String, val offerSdp: String) : CallState
    /** Answered; media still connecting. */
    data class Connecting(val callId: String, val peer: String, val outgoing: Boolean) : CallState
    data class Active(val callId: String, val peer: String, val outgoing: Boolean, val startedAtMs: Long) : CallState
}

val CallState.callId: String?
    get() = when (this) {
        CallState.Idle -> null
        is CallState.Outgoing -> callId
        is CallState.Incoming -> callId
        is CallState.Connecting -> callId
        is CallState.Active -> callId
    }

val CallState.peerName: String?
    get() = when (this) {
        CallState.Idle -> null
        is CallState.Outgoing -> peer
        is CallState.Incoming -> peer
        is CallState.Connecting -> peer
        is CallState.Active -> peer
    }

data class UiState(
    val connection: Connection = Connection.DISCONNECTED,
    val myId: String = "",
    val users: List<String> = emptyList(),
    val call: CallState = CallState.Idle,
    val muted: Boolean = false,
    val speaker: Boolean = false,
    val route: AudioRoute = AudioRoute.EARPIECE,
    /** Media dropped (e.g. Wi-Fi blip) and WebRTC is trying to recover. */
    val reconnecting: Boolean = false,
    /** Backfire's decoy is talking for this phone. */
    val decoy: Boolean = false,
    val message: String? = null,
)

/**
 * Owns the signaling connection and the WebRTC call.
 * All mutable state is touched only on [exec] so callbacks from OkHttp/WebRTC threads can't race.
 */
object CallManager {
    private const val TAG = "CallManager"
    private const val RING_TIMEOUT_SEC = 45L
    private const val RECONNECT_TIMEOUT_SEC = 15L

    private lateinit var appContext: Context
    private lateinit var effects: CallEffects
    private val exec = Executors.newSingleThreadScheduledExecutor { r -> Thread(r, "call-manager") }

    private val _state = MutableStateFlow(UiState())
    val state: StateFlow<UiState> = _state.asStateFlow()

    private var signaling: SignalingClient? = null

    private var factory: PeerConnectionFactory? = null
    private var pc: PeerConnection? = null
    private var localSource: AudioSource? = null
    private var localTrack: AudioTrack? = null
    private var remoteTrack: AudioTrack? = null
    private val pendingIce = mutableListOf<IceCandidate>()
    private var remoteDescriptionSet = false

    // Per-call bookkeeping for the Recents list.
    private var callOutgoing = false
    private var callStartedAtMs = 0L
    private var callConnectedAtMs = 0L
    private var ringTimeout: ScheduledFuture<*>? = null
    private var reconnectTimeout: ScheduledFuture<*>? = null

    /** Non-null only while media is connected; read from audio threads. */
    @Volatile private var exportCallId: String? = null
    @Volatile private var muted = false

    /**
     * Backfire handoff, caller side: the carrier moved this call to another peer (the decoy). The UI keeps showing the
     * original name; signaling for the call now goes to [signalPeer]. [pcGen] lets callbacks from the replaced
     * PeerConnection be ignored.
     */
    private var signalPeer: String? = null
    private var pcGen = 0

    fun init(context: Context) {
        if (::appContext.isInitialized) return
        appContext = context.applicationContext
        effects = CallEffects(appContext)
        CallHistory.init(appContext)
    }

    // ---------------------------------------------------------------- public API (any thread)

    fun connect(serverUrl: String, myId: String) = exec.execute {
        signaling?.close()
        _state.update { it.copy(connection = Connection.CONNECTING, myId = myId, message = null) }
        signaling = SignalingClient(serverUrl, myId, object : SignalingClient.Listener {
            override fun onConnected() = exec.execute {
                _state.update { it.copy(connection = Connection.CONNECTED, message = null) }
            }

            override fun onDisconnected(reason: String) = exec.execute {
                _state.update { it.copy(connection = Connection.CONNECTING, users = emptyList(), message = "Can't reach server ($reason)") }
            }

            override fun onMessage(msg: JSONObject) = exec.execute { handleSignal(msg) }
        }).also { it.connect() }
    }

    fun disconnect() = exec.execute {
        hangUpInternal()
        signaling?.close()
        signaling = null
        _state.update { UiState(myId = it.myId) }
    }

    fun call(peer: String) = exec.execute {
        val s = _state.value
        if (s.call != CallState.Idle || peer.isBlank() || peer == s.myId) return@execute
        if (s.connection != Connection.CONNECTED) {
            _state.update { it.copy(message = "Not connected to the server") }
            return@execute
        }
        val callId = UUID.randomUUID().toString()
        beginCall(outgoing = true)
        setCall(CallState.Outgoing(callId, peer))
        effects.enterCallAudio()
        applyRoute()
        effects.startRingback()
        ringTimeout = exec.schedule({
            if (_state.value.call is CallState.Outgoing && currentCallId() == callId) endCall("no_answer", notifyPeer = true)
        }, RING_TIMEOUT_SEC, TimeUnit.SECONDS)

        val conn = createPeerConnection(callId, peer) ?: return@execute endCall("failed", notifyPeer = false)
        conn.createOffer(object : SdpAdapter("createOffer") {
            override fun onCreateSuccess(sdp: SessionDescription) {
                conn.setLocalDescription(object : SdpAdapter("setLocal(offer)") {
                    override fun onSetSuccess() = exec.execute {
                        if (currentCallId() != callId) return@execute
                        send("offer", peer, callId) { put("sdp", sdp.description) }
                    }
                }, sdp)
            }
        }, MediaConstraints())
    }

    fun accept() = exec.execute {
        val incoming = _state.value.call as? CallState.Incoming ?: return@execute
        val (callId, peer, offerSdp) = incoming
        cancelRingTimeout()
        effects.stopRinging()
        Notifications.cancelIncoming(appContext)
        setCall(CallState.Connecting(callId, peer, outgoing = false))
        effects.enterCallAudio()
        applyRoute()
        val conn = createPeerConnection(callId, peer) ?: return@execute endCall("failed", notifyPeer = true)

        conn.setRemoteDescription(object : SdpAdapter("setRemote(offer)") {
            override fun onSetSuccess() = exec.execute {
                if (currentCallId() != callId) return@execute
                onRemoteDescriptionSet()
                conn.createAnswer(object : SdpAdapter("createAnswer") {
                    override fun onCreateSuccess(sdp: SessionDescription) {
                        conn.setLocalDescription(object : SdpAdapter("setLocal(answer)") {
                            override fun onSetSuccess() = exec.execute {
                                if (currentCallId() != callId) return@execute
                                send("answer", peer, callId) { put("sdp", sdp.description) }
                            }
                        }, sdp)
                    }
                }, MediaConstraints())
            }
        }, SessionDescription(SessionDescription.Type.OFFER, offerSdp))
    }

    fun decline() = exec.execute {
        val incoming = _state.value.call as? CallState.Incoming ?: return@execute
        send("reject", incoming.peer, incoming.callId)
        endCall("declined", notifyPeer = false)
    }

    fun hangUp() = exec.execute { hangUpInternal() }

    fun setMuted(value: Boolean) = exec.execute {
        if (_state.value.decoy) return@execute   // disabling the track would also silence the decoy's voice
        muted = value
        localTrack?.setEnabled(!value)
        _state.update { it.copy(muted = value) }
    }

    fun setSpeaker(on: Boolean) = exec.execute {
        _state.update { it.copy(speaker = on) }
        applyRoute()
    }

    fun clearMessage() = _state.update { it.copy(message = null) }

    /**
     * Backfire's decoy takes over this phone's side of the call: the caller hears the decoy voice instead of the mic.
     * Synchronous (called over Binder); returns false if the call isn't active.
     */
    fun startDecoyMode(callId: String): Boolean {
        val f = java.util.concurrent.FutureTask {
            val c = _state.value.call as? CallState.Active ?: return@FutureTask false
            if (c.callId != callId || !Injector.start(callId)) return@FutureTask false
            muted = false
            localTrack?.setEnabled(true)
            _state.update { it.copy(muted = false, decoy = true) }
            updateProximity()   // phone is silent and can be put down or used: no screen-off at the ear
            true
        }
        exec.execute(f)
        return runCatching { f.get(2, TimeUnit.SECONDS) }.getOrDefault(false)
    }

    fun stopDecoyMode() = exec.execute {
        Injector.stop()
        _state.update { it.copy(decoy = false) }
        updateProximity()
    }

    /** Another app (Backfire) ends the call, e.g. when the decoy is done. */
    fun endFromApp(callId: String, reason: String) = exec.execute {
        if (currentCallId() == callId) endCall(reason, notifyPeer = true)
    }

    // ---------------------------------------------------------------- signaling

    private fun handleSignal(msg: JSONObject) {
        val type = msg.optString("type")
        val from = msg.optString("from")
        val callId = msg.optString("callId")
        val current = _state.value.call

        when (type) {
            "users" -> {
                val arr = msg.optJSONArray("ids")
                val ids = (0 until (arr?.length() ?: 0)).map { arr!!.getString(it) }
                _state.update { s -> s.copy(users = ids.filter { it != s.myId }.sorted()) }
            }

            "error" -> _state.update { it.copy(message = "Server error: ${msg.optString("message")}") }

            "offer" -> {
                if (current != CallState.Idle) {
                    // Already on a call: tell the caller we're busy and log it as missed, like a phone would.
                    send("reject", from, callId) { put("reason", "busy") }
                    val now = System.currentTimeMillis()
                    CallHistory.add(CallRecord(callId, from, outgoing = false, startedAtMs = now, durationSec = 0, outcome = CallOutcome.MISSED))
                    Notifications.showMissed(appContext, from, now)
                    return
                }
                resetPerCallState()
                beginCall(outgoing = false)
                setCall(CallState.Incoming(callId, from, msg.getString("sdp")))
                effects.startRinging()
                Notifications.showIncoming(appContext, from)
                // Safety net in case the caller vanishes without sending "bye".
                ringTimeout = exec.schedule({
                    if (_state.value.call is CallState.Incoming && currentCallId() == callId) endCall("no_answer", notifyPeer = false)
                }, RING_TIMEOUT_SEC + 15, TimeUnit.SECONDS)
            }

            "answer" -> {
                if (signalPeer != null && from == signalPeer && current.callId == callId) {
                    // The decoy answered our re-offer: finish the handoff quietly, the call screen never changes.
                    pc?.setRemoteDescription(object : SdpAdapter("setRemote(transfer answer)") {
                        override fun onSetSuccess() = exec.execute {
                            if (currentCallId() == callId) onRemoteDescriptionSet()
                        }
                    }, SessionDescription(SessionDescription.Type.ANSWER, msg.getString("sdp")))
                    return
                }
                if (current !is CallState.Outgoing || current.callId != callId) return
                cancelRingTimeout()
                effects.stopTones()
                setCall(CallState.Connecting(callId, current.peer, outgoing = true))
                pc?.setRemoteDescription(object : SdpAdapter("setRemote(answer)") {
                    override fun onSetSuccess() = exec.execute {
                        if (currentCallId() == callId) onRemoteDescriptionSet()
                    }
                }, SessionDescription(SessionDescription.Type.ANSWER, msg.getString("sdp")))
            }

            "ice" -> {
                if (current.callId != callId) return
                val candidate = IceCandidate(msg.optString("sdpMid"), msg.optInt("sdpMLineIndex"), msg.getString("candidate"))
                val conn = pc
                if (conn != null && remoteDescriptionSet) conn.addIceCandidate(candidate) else pendingIce.add(candidate)
            }

            "reject" -> if (current.callId == callId) {
                endCall(
                    when (msg.optString("reason")) {
                        "busy" -> "busy"
                        "blocked" -> "blocked"
                        else -> "rejected"
                    },
                    notifyPeer = false,
                )
            }

            // Backfire carrier: move this (outgoing) call to another peer without telling the user.
            "transfer" -> if (current.callId == callId && callOutgoing &&
                (current is CallState.Active || current is CallState.Connecting)
            ) {
                startTransfer(callId, msg.getString("to"))
            }

            // The carrier couldn't hand off (no decoy online). The call simply continues.
            "backfire" -> if (current.callId == callId && msg.optString("status") == "decoy_offline") {
                _state.update { it.copy(message = "Backfire's decoy is offline") }
            }

            "bye" -> if (current.callId == callId) {
                endCall(msg.optString("reason").ifEmpty { "remote_hangup" }, notifyPeer = false)
            }
        }
    }

    private fun send(type: String, to: String, callId: String, extra: JSONObject.() -> Unit = {}) {
        signaling?.send(JSONObject().put("type", type).put("to", to).put("callId", callId).apply(extra))
    }

    // ---------------------------------------------------------------- WebRTC

    private fun ensureFactory(): PeerConnectionFactory {
        factory?.let { return it }
        PeerConnectionFactory.initialize(
            PeerConnectionFactory.InitializationOptions.builder(appContext).createInitializationOptions()
        )
        val adm = JavaAudioDeviceModule.builder(appContext)
            .setUseHardwareAcousticEchoCanceler(true)
            .setUseHardwareNoiseSuppressor(true)
            // Raw microphone PCM from this phone, ~10 ms per callback.
            .setSamplesReadyCallback { samples ->
                Injector.onRecordTick(samples.sampleRate, samples.channelCount)  // decoy voice for the next 10 ms
                val id = exportCallId ?: return@setSamplesReadyCallback
                if (Injector.callId == id) return@setSamplesReadyCallback        // never export the decoy as "my mic"
                if (muted) return@setSamplesReadyCallback
                AudioBus.frame(id, VoipExport.SOURCE_LOCAL, samples.data, samples.sampleRate, samples.channelCount)
            }
            .createAudioDeviceModule()
            .also { Injector.attach(it) }
        return PeerConnectionFactory.builder()
            .setAudioDeviceModule(adm)
            .createPeerConnectionFactory()
            .also { factory = it }
    }

    /** Decoded audio from the other phone, ~10 ms per callback. */
    private val remoteSink = AudioTrackSink { data, bitsPerSample, sampleRate, channels, frames, _ ->
        val id = exportCallId ?: return@AudioTrackSink
        if (bitsPerSample != 16) return@AudioTrackSink
        val buf = data.duplicate()
        val bytes = ByteArray(minOf(buf.remaining(), frames * channels * 2))
        buf.get(bytes)
        AudioBus.frame(id, VoipExport.SOURCE_REMOTE, bytes, sampleRate, channels)
    }

    private fun createPeerConnection(callId: String, peer: String): PeerConnection? {
        val f = ensureFactory()
        val gen = ++pcGen
        val iceServers = listOf(
            // Phones on the same Wi-Fi connect via host candidates; STUN helps across NATs.
            PeerConnection.IceServer.builder("stun:stun.l.google.com:19302").createIceServer()
        )
        val config = PeerConnection.RTCConfiguration(iceServers).apply {
            sdpSemantics = PeerConnection.SdpSemantics.UNIFIED_PLAN
            continualGatheringPolicy = PeerConnection.ContinualGatheringPolicy.GATHER_CONTINUALLY
        }

        val conn = f.createPeerConnection(config, object : PeerConnection.Observer {
            override fun onIceCandidate(candidate: IceCandidate) = exec.execute {
                if (currentCallId() != callId || gen != pcGen) return@execute
                send("ice", peer, callId) {
                    put("sdpMid", candidate.sdpMid)
                    put("sdpMLineIndex", candidate.sdpMLineIndex)
                    put("candidate", candidate.sdp)
                }
            }

            override fun onConnectionChange(newState: PeerConnection.PeerConnectionState) = exec.execute {
                Log.i(TAG, "peer connection: $newState")
                if (currentCallId() != callId || gen != pcGen) return@execute
                when (newState) {
                    PeerConnection.PeerConnectionState.CONNECTED -> onMediaConnected()
                    PeerConnection.PeerConnectionState.DISCONNECTED -> onMediaInterrupted(callId)
                    PeerConnection.PeerConnectionState.FAILED -> endCall("failed", notifyPeer = true)
                    else -> Unit
                }
            }

            override fun onTrack(transceiver: RtpTransceiver) {
                val track = transceiver.receiver.track() as? AudioTrack ?: return
                exec.execute {
                    if (currentCallId() != callId || gen != pcGen) return@execute
                    remoteTrack = track
                    track.addSink(remoteSink)
                }
            }

            override fun onSignalingChange(s: PeerConnection.SignalingState) {}
            override fun onIceConnectionChange(s: PeerConnection.IceConnectionState) {}
            override fun onIceConnectionReceivingChange(receiving: Boolean) {}
            override fun onIceGatheringChange(s: PeerConnection.IceGatheringState) {}
            override fun onIceCandidatesRemoved(candidates: Array<out IceCandidate>) {}
            override fun onAddStream(stream: MediaStream) {}
            override fun onRemoveStream(stream: MediaStream) {}
            override fun onDataChannel(channel: DataChannel) {}
            override fun onRenegotiationNeeded() {}
        }) ?: return null

        val source = f.createAudioSource(MediaConstraints())
        val track = f.createAudioTrack("mic-$callId", source)
        track.setEnabled(!muted)
        conn.addTrack(track, listOf("voip"))

        pc = conn
        localSource = source
        localTrack = track
        return conn
    }

    private fun onRemoteDescriptionSet() {
        remoteDescriptionSet = true
        pendingIce.forEach { pc?.addIceCandidate(it) }
        pendingIce.clear()
    }

    private fun onMediaConnected() {
        reconnectTimeout?.cancel(false)
        reconnectTimeout = null
        _state.update { it.copy(reconnecting = false) }

        val c = _state.value.call as? CallState.Connecting ?: return // already active: this was a reconnect
        callConnectedAtMs = System.currentTimeMillis()
        setCall(CallState.Active(c.callId, c.peer, c.outgoing, callConnectedAtMs))
        updateProximity()
        AudioBus.callStarted(c.callId, c.peer, c.outgoing)
        exportCallId = c.callId
    }

    /** Caller side of a Backfire handoff: drop the media with Maria and re-offer the same call to [to]. */
    private fun startTransfer(callId: String, to: String) {
        Log.i(TAG, "transfer $callId -> $to")
        remoteTrack?.let { runCatching { it.removeSink(remoteSink) } }
        pc?.dispose()
        localTrack?.let { runCatching { it.dispose() } }
        localSource?.dispose()
        resetPerCallState()
        signalPeer = to
        val conn = createPeerConnection(callId, to) ?: return endCall("failed", notifyPeer = true)
        conn.createOffer(object : SdpAdapter("createOffer(transfer)") {
            override fun onCreateSuccess(sdp: SessionDescription) {
                conn.setLocalDescription(object : SdpAdapter("setLocal(transfer offer)") {
                    override fun onSetSuccess() = exec.execute {
                        if (currentCallId() != callId) return@execute
                        send("offer", to, callId) { put("sdp", sdp.description) }
                    }
                }, sdp)
            }
        }, MediaConstraints())
    }

    /** Wi-Fi blip etc. WebRTC often recovers by itself; give it a while before giving up. */
    private fun onMediaInterrupted(callId: String) {
        if (_state.value.call !is CallState.Active) return
        _state.update { it.copy(reconnecting = true) }
        reconnectTimeout?.cancel(false)
        reconnectTimeout = exec.schedule({
            if (currentCallId() == callId && _state.value.reconnecting) endCall("failed", notifyPeer = true)
        }, RECONNECT_TIMEOUT_SEC, TimeUnit.SECONDS)
    }

    // ---------------------------------------------------------------- call lifecycle

    private fun beginCall(outgoing: Boolean) {
        callOutgoing = outgoing
        callStartedAtMs = System.currentTimeMillis()
        callConnectedAtMs = 0L
    }

    private fun hangUpInternal() {
        val call = _state.value.call
        if (call is CallState.Incoming) {
            send("reject", call.peer, call.callId)
            endCall("declined", notifyPeer = false)
        } else {
            endCall("hangup", notifyPeer = true)
        }
    }

    /**
     * reason: hangup (we ended), remote_hangup, declined (we declined), rejected (they declined),
     * busy, no_answer, offline, failed.
     */
    private fun endCall(reason: String, notifyPeer: Boolean) {
        val call = _state.value.call
        val callId = call.callId ?: return
        val peer = call.peerName!!
        if (Injector.callId == callId) Injector.stop()
        if (notifyPeer) send("bye", signalPeer ?: peer, callId) { put("reason", if (reason == "hangup") "remote_hangup" else reason) }
        signalPeer = null

        cancelRingTimeout()
        reconnectTimeout?.cancel(false)
        reconnectTimeout = null
        Notifications.cancelIncoming(appContext)

        if (exportCallId == callId) {
            exportCallId = null
            AudioBus.callEnded(callId, reason)
        }

        remoteTrack?.let { runCatching { it.removeSink(remoteSink) } }
        pc?.dispose()
        localTrack?.let { runCatching { it.dispose() } } // may already be released with the PeerConnection
        localSource?.dispose()
        resetPerCallState()

        // Phone-style feedback, then release audio once the tone has played.
        effects.stopRinging()
        effects.setProximity(false)
        val wasRingingOut = call is CallState.Outgoing
        when {
            wasRingingOut && (reason == "rejected" || reason == "busy") -> effects.playBusy()
            call is CallState.Active -> effects.playEnded()
            else -> effects.stopTones()
        }
        exec.schedule({ if (_state.value.call == CallState.Idle) effects.exitCallAudio() }, 2600, TimeUnit.MILLISECONDS)

        val outcome = when {
            callConnectedAtMs > 0 -> CallOutcome.ANSWERED
            callOutgoing -> when (reason) {
                "hangup" -> CallOutcome.CANCELLED
                "no_answer" -> CallOutcome.NO_ANSWER
                "rejected", "busy", "blocked" -> CallOutcome.REJECTED
                else -> CallOutcome.FAILED
            }
            reason == "declined" -> CallOutcome.DECLINED
            else -> CallOutcome.MISSED
        }
        val duration = if (callConnectedAtMs > 0) (System.currentTimeMillis() - callConnectedAtMs) / 1000 else 0
        CallHistory.add(CallRecord(callId, peer, callOutgoing, callStartedAtMs, duration, outcome))
        if (outcome == CallOutcome.MISSED) Notifications.showMissed(appContext, peer, callStartedAtMs)

        val text = when (outcome) {
            CallOutcome.ANSWERED -> when (reason) {
                "handoff" -> "Backfire took this call for you"
                "backfire_hangup" -> "Backfire hung up for you"
                "decoy_done" -> "Backfire's decoy finished the call"
                else -> "Call ended · %d:%02d".format(duration / 60, duration % 60)
            }
            CallOutcome.NO_ANSWER -> "$peer didn't answer"
            CallOutcome.REJECTED -> when (reason) {
                "busy" -> "$peer is busy"
                "blocked" -> "Your call can't be completed as dialed"
                else -> "$peer declined"
            }
            CallOutcome.FAILED -> if (reason == "offline") "$peer is offline" else "Call failed"
            CallOutcome.MISSED -> "Missed call from $peer"
            CallOutcome.CANCELLED, CallOutcome.DECLINED -> null
        }
        setCall(CallState.Idle, text)
    }

    private fun cancelRingTimeout() {
        ringTimeout?.cancel(false)
        ringTimeout = null
    }

    private fun resetPerCallState() {
        pc = null
        localSource = null
        localTrack = null
        remoteTrack = null
        pendingIce.clear()
        remoteDescriptionSet = false
    }

    private fun currentCallId(): String? = _state.value.call.callId

    private fun setCall(call: CallState, message: String? = null) {
        val idle = call == CallState.Idle
        _state.update {
            it.copy(
                call = call,
                message = message ?: it.message.takeIf { !idle },
                muted = if (idle) false else it.muted,
                speaker = if (idle) false else it.speaker,
                reconnecting = if (idle) false else it.reconnecting,
                decoy = if (idle) false else it.decoy,
            )
        }
        if (idle) muted = false
    }

    private fun applyRoute() {
        val route = effects.route(_state.value.speaker)
        _state.update { it.copy(route = route) }
        updateProximity()
    }

    /** Screen goes dark at the ear only when the earpiece is in use. */
    private fun updateProximity() {
        val inCall = when (_state.value.call) {
            is CallState.Outgoing, is CallState.Connecting, is CallState.Active -> true
            else -> false
        }
        effects.setProximity(inCall && !_state.value.decoy && _state.value.route == AudioRoute.EARPIECE)
    }

    /** Logs failures and tears the call down; subclasses override the success callbacks they need. */
    private open class SdpAdapter(private val what: String) : SdpObserver {
        override fun onCreateSuccess(sdp: SessionDescription) {}
        override fun onSetSuccess() {}
        override fun onCreateFailure(error: String?) = fail(error)
        override fun onSetFailure(error: String?) = fail(error)
        private fun fail(error: String?) {
            Log.e(TAG, "$what failed: $error")
            exec.execute { endCall("failed", notifyPeer = true) }
        }
    }
}
