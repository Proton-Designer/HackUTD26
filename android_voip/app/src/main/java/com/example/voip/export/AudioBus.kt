package com.example.voip.export

import java.util.concurrent.CopyOnWriteArrayList

/**
 * In-process fan-out of call audio. CallManager publishes here and
 * AudioExportService forwards everything to bound apps over Binder.
 * Kept separate so other in-app consumers (e.g. a recorder) can subscribe too.
 */
object AudioBus {
    interface Sink {
        fun onCallStarted(callId: String, peerId: String, outgoing: Boolean)
        fun onFrame(callId: String, source: Int, pcm16: ByteArray, sampleRate: Int, channels: Int, timestampMs: Long)
        fun onCallEnded(callId: String, reason: String)
    }

    private val sinks = CopyOnWriteArrayList<Sink>()

    @Volatile
    var activeCallId: String? = null
        private set

    fun add(sink: Sink) { sinks.add(sink) }
    fun remove(sink: Sink) { sinks.remove(sink) }

    fun callStarted(callId: String, peerId: String, outgoing: Boolean) {
        activeCallId = callId
        sinks.forEach { it.onCallStarted(callId, peerId, outgoing) }
    }

    /** Called on WebRTC audio threads: sinks must not block. */
    fun frame(callId: String, source: Int, pcm16: ByteArray, sampleRate: Int, channels: Int) {
        if (sinks.isEmpty()) return
        val ts = System.currentTimeMillis()
        sinks.forEach { it.onFrame(callId, source, pcm16, sampleRate, channels, ts) }
    }

    fun callEnded(callId: String, reason: String) {
        if (activeCallId == callId) activeCallId = null
        sinks.forEach { it.onCallEnded(callId, reason) }
    }
}
