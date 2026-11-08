package com.example.voip.export

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.os.RemoteCallbackList
import android.os.RemoteException
import android.util.Log
import java.util.concurrent.Executors

/**
 * Bound service that streams call audio to other apps signed with the same key.
 * Clients bind with [VoipExport.bindIntent] and call registerListener().
 */
class AudioExportService : Service(), AudioBus.Sink {

    private val listeners = RemoteCallbackList<ICallAudioListener>()

    // RemoteCallbackList broadcasts must not overlap, and audio threads must not block,
    // so every outgoing call goes through this single thread.
    private val dispatcher = Executors.newSingleThreadExecutor { r -> Thread(r, "audio-export") }

    private val binder = object : ICallAudioService.Stub() {
        override fun registerListener(listener: ICallAudioListener?) {
            if (listener != null) listeners.register(listener)
            Log.i(TAG, "listener registered (uid=${android.os.Binder.getCallingUid()}), total=${listeners.registeredCallbackCount}")
        }

        override fun unregisterListener(listener: ICallAudioListener?) {
            if (listener != null) listeners.unregister(listener)
        }

        override fun getActiveCallId(): String? = AudioBus.activeCallId

        override fun startInjection(callId: String): Boolean =
            callId == AudioBus.activeCallId && com.example.voip.call.CallManager.startDecoyMode(callId)

        override fun injectAudio(callId: String, pcm16: ByteArray, sampleRate: Int) {
            if (callId == Injector.callId) Injector.push(pcm16, sampleRate)
        }

        override fun clearInjection(callId: String) { if (callId == Injector.callId) Injector.clear() }

        override fun stopInjection(callId: String) { if (callId == Injector.callId) com.example.voip.call.CallManager.stopDecoyMode() }

        override fun endCall(callId: String, reason: String) {
            if (callId == AudioBus.activeCallId) com.example.voip.call.CallManager.endFromApp(callId, reason)
        }
    }

    override fun onCreate() {
        super.onCreate()
        AudioBus.add(this)
    }

    override fun onBind(intent: Intent?): IBinder = binder

    override fun onDestroy() {
        AudioBus.remove(this)
        dispatcher.shutdown()
        listeners.kill()
        super.onDestroy()
    }

    override fun onCallStarted(callId: String, peerId: String, outgoing: Boolean) =
        broadcast { it.onCallStarted(callId, peerId, outgoing) }

    override fun onFrame(callId: String, source: Int, pcm16: ByteArray, sampleRate: Int, channels: Int, timestampMs: Long) {
        if (listeners.registeredCallbackCount == 0) return
        broadcast { it.onAudioFrame(callId, source, pcm16, sampleRate, channels, timestampMs) }
    }

    override fun onCallEnded(callId: String, reason: String) =
        broadcast { it.onCallEnded(callId, reason) }

    private fun broadcast(block: (ICallAudioListener) -> Unit) {
        if (dispatcher.isShutdown) return
        dispatcher.execute {
            val n = listeners.beginBroadcast()
            try {
                for (i in 0 until n) {
                    try {
                        block(listeners.getBroadcastItem(i))
                    } catch (e: RemoteException) {
                        // Client died; RemoteCallbackList drops it automatically.
                    }
                }
            } finally {
                listeners.finishBroadcast()
            }
        }
    }

    private companion object { const val TAG = "AudioExport" }
}
