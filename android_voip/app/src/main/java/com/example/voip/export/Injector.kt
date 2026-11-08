package com.example.voip.export

import android.util.Log
import org.webrtc.audio.JavaAudioDeviceModule

/**
 * Plays app-supplied audio into the call in place of the microphone (Backfire's decoy voice).
 *
 * How: with the mic muted, WebRTC's record thread sends its internal `emptyBytes` buffer every 10 ms instead of mic
 * data, and then calls the SamplesReadyCallback on the same thread. In that callback we write the NEXT 10 ms of decoy
 * audio into `emptyBytes`, so it goes out on the following tick, paced by WebRTC's own clock.
 * NOTE: `emptyBytes` is a private field of org.webrtc.audio.WebRtcAudioRecord (stream-webrtc-android 1.3.10);
 * re-check the name if the library is upgraded. If reflection fails, injection reports unavailable (silence, no crash).
 */
object Injector {
    private const val TAG = "Injector"
    private const val MAX_SECONDS = 30

    @Volatile var callId: String? = null
        private set
    private val lock = Any()
    private var queue = ShortArray(48000 * MAX_SECONDS)
    private var head = 0
    private var size = 0
    private var outRate = 48000
    private var adm: JavaAudioDeviceModule? = null
    private val emptyBytesField by lazy {
        runCatching { Class.forName("org.webrtc.audio.WebRtcAudioRecord").getDeclaredField("emptyBytes").apply { isAccessible = true } }
            .onFailure { Log.e(TAG, "WebRTC internals changed: injection unavailable", it) }.getOrNull()
    }

    val supported: Boolean get() = emptyBytesField != null

    fun attach(module: JavaAudioDeviceModule) { adm = module }

    fun start(id: String): Boolean {
        if (!supported || adm == null) return false
        synchronized(lock) { head = 0; size = 0 }
        callId = id
        adm?.setMicrophoneMute(true)
        Log.i(TAG, "injecting into $id")
        return true
    }

    fun stop() {
        if (callId == null) return
        callId = null
        adm?.setMicrophoneMute(false)
        synchronized(lock) { head = 0; size = 0 }
    }

    fun clear() = synchronized(lock) { head = 0; size = 0 }

    /** Queue mono 16-bit PCM at [rate]; resampled (linear) to the record rate. */
    fun push(pcm16: ByteArray, rate: Int) {
        val n = pcm16.size / 2
        if (n == 0) return
        val ratio = rate.toDouble() / outRate
        val outN = (n / ratio).toInt()
        synchronized(lock) {
            for (i in 0 until outN) {
                if (size >= queue.size) break   // more than 30 s queued: drop the excess
                val x = i * ratio
                val j = x.toInt().coerceAtMost(n - 1)
                val k = (j + 1).coerceAtMost(n - 1)
                val a = sample(pcm16, j); val b = sample(pcm16, k)
                queue[(head + size) % queue.size] = (a + (b - a) * (x - j)).toInt().toShort()
                size++
            }
        }
    }

    private fun sample(b: ByteArray, i: Int) = ((b[2 * i].toInt() and 0xFF) or (b[2 * i + 1].toInt() shl 8)).toShort().toInt()

    /** On WebRTC's record thread, right after a 10 ms frame went out: stage the next one. */
    fun onRecordTick(sampleRate: Int, channels: Int) {
        if (callId == null) return
        val dev = adm ?: return
        val buf = runCatching { emptyBytesField?.get(dev.audioInput) as? ByteArray }.getOrNull() ?: return
        outRate = sampleRate
        val ch = channels.coerceAtLeast(1)
        val frames = buf.size / (2 * ch)
        synchronized(lock) {
            for (f in 0 until frames) {
                val s = if (size > 0) { val v = queue[head]; head = (head + 1) % queue.size; size--; v.toInt() } else 0
                for (c in 0 until ch) {
                    val o = (f * ch + c) * 2
                    buf[o] = (s and 0xFF).toByte(); buf[o + 1] = ((s shr 8) and 0xFF).toByte()
                }
            }
        }
    }

    val speaking: Boolean get() = synchronized(lock) { size > 0 }
}
