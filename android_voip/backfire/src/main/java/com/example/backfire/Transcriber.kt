package com.example.backfire

import android.util.Log
import org.json.JSONObject
import org.vosk.Model
import org.vosk.Recognizer
import java.io.File
import java.util.concurrent.Executors

/**
 * Offline speech-to-text of the CALLER's audio (Vosk). Runs on its own thread; [onFinal] gets each finished utterance.
 * Audio comes in at any rate and is reduced to 16 kHz mono here.
 */
class Transcriber(
    private val model: Model,
    private val onPartial: (String) -> Unit = {},
    private val onFinal: (String) -> Unit,
) {
    private val exec = Executors.newSingleThreadExecutor { Thread(it, "transcriber") }
    private var rec: Recognizer? = null
    private val decimator = Decimator(RATE)
    @Volatile private var closed = false
    private var frames = 0

    fun start() = exec.execute {
        rec?.close()
        rec = Recognizer(model, RATE.toFloat())
        decimator.reset()
    }

    /** Called on a Binder thread for every ~10 ms frame. Never blocks it. */
    fun feed(pcm16: ByteArray, sampleRate: Int, channels: Int) {
        if (closed) return
        exec.execute {
            val r = rec ?: return@execute
            val pcm = decimator.process(pcm16, sampleRate, channels)
            if (pcm.isEmpty()) return@execute
            if (r.acceptWaveForm(pcm, pcm.size)) emit(r.result)
            else if (++frames % 15 == 0)  // partials (~every 150 ms) are only used to detect the caller talking over the decoy
                runCatching { JSONObject(r.partialResult).optString("partial") }.getOrNull()?.let { if (it.isNotBlank()) onPartial(it) }
        }
    }

    /** Flush the last words (e.g. when the caller stops talking at call end). */
    fun stop() = exec.execute {
        rec?.let { emit(it.finalResult); it.close() }
        rec = null
    }

    fun close() {
        closed = true
        stop()
        exec.execute { exec.shutdown() }
    }

    private fun emit(json: String) {
        val text = runCatching { JSONObject(json).optString("text") }.getOrDefault("").trim()
        if (text.isNotEmpty()) onFinal(text)
    }

    companion object {
        const val RATE = 16000
        @Volatile private var cached: Model? = null

        /** Loads once (~1 s). Null if the speech model isn't downloaded. */
        fun loadModel(dir: File): Model? {
            cached?.let { return it }
            if (!dir.isDirectory) return null
            return runCatching { Model(dir.absolutePath) }
                .onFailure { Log.e("Transcriber", "model load failed", it) }
                .getOrNull()?.also { cached = it }
        }

        fun unload() { cached?.close(); cached = null }
    }
}

/** Any-rate 16-bit PCM (mono or interleaved) -> 16-bit mono at [outRate], by box-averaging. Not thread-safe. */
class Decimator(private val outRate: Int) {
    private var acc = 0
    private var sum = 0L
    private var count = 0

    fun reset() { acc = 0; sum = 0; count = 0 }

    fun process(pcm: ByteArray, inRate: Int, channels: Int): ByteArray {
        val ch = channels.coerceAtLeast(1)
        if (inRate <= outRate && ch == 1) return pcm
        val frames = pcm.size / (2 * ch)
        val out = java.io.ByteArrayOutputStream(frames * outRate / inRate * 2 + 4)
        for (i in 0 until frames) {
            var s = 0
            for (c in 0 until ch) {
                val o = (i * ch + c) * 2
                s += (pcm[o].toInt() and 0xFF) or (pcm[o + 1].toInt() shl 8)
            }
            sum += s / ch
            count++
            acc += outRate
            if (acc >= inRate) {
                acc -= inRate
                val v = (sum / count).toInt().coerceIn(-32768, 32767)
                out.write(v and 0xFF); out.write((v shr 8) and 0xFF)
                sum = 0; count = 0
            }
        }
        return out.toByteArray()
    }
}
