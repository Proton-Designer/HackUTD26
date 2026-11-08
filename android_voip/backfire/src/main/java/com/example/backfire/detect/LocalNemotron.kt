package com.example.backfire.detect

import android.util.Log
import com.example.backfire.BuildConfig
import java.io.File

/** JNI surface of src/main/cpp/backfire_llama.cpp. */
object LlamaBridge {
    /** False when this APK was built without -Pbackfire.llama=true, or the .so failed to load. */
    val available: Boolean = BuildConfig.HAS_LLAMA && runCatching { System.loadLibrary("backfire_llama") }
        .onFailure { Log.e("LlamaBridge", "native library missing", it) }.isSuccess

    external fun nativeLoad(path: String, threads: Int, nCtx: Int): Long
    external fun nativeSetPrefix(handle: Long, prefix: String): Boolean
    external fun nativeReset(handle: Long)
    external fun nativeAppend(handle: Long, text: String): Int
    external fun nativeAsk(handle: Long, question: String): Float
    external fun nativeBench(handle: Long, threads: IntArray, nTok: Int, keep: Int): String
    external fun nativeFree(handle: Long)
}

/**
 * Nemotron 3 Nano 4B (Q4_K_M) running on this phone, answering only "yes"/"no". Nothing leaves the device.
 * Speed: big cores only, system prompt cached at load, transcript appended incrementally, one logits read per check.
 */
class LocalNemotron private constructor(private val handle: Long, val threads: Int) : Detector {
    override val name = "On-device Nemotron 3 Nano 4B"
    private val lines = ArrayDeque<String>()

    override fun reset() { lines.clear(); LlamaBridge.nativeReset(handle) }

    override fun append(utterance: String) {
        lines.addLast(utterance)
        while (lines.size > 12) lines.removeFirst()
        var pos = LlamaBridge.nativeAppend(handle, Prompt.line(utterance))
        if (pos < 0 || pos > N_CTX - 200) {
            // Context nearly full (long call): restart from the prompt with the most recent lines.
            LlamaBridge.nativeReset(handle)
            lines.takeLast(8).forEach { pos = LlamaBridge.nativeAppend(handle, Prompt.line(it)) }
        }
    }

    override fun ask(): Verdict? {
        val t0 = System.nanoTime()
        val p = LlamaBridge.nativeAsk(handle, Prompt.ASK)
        val ms = (System.nanoTime() - t0) / 1_000_000
        if (p < 0f) return null
        Log.i(TAG, "P(yes)=%.3f in %d ms".format(p, ms))
        return Verdict(p >= 0.5f, p.toDouble(), ms, "local")
    }

    /** Times prompt processing and decoding at several thread counts; logs and returns "threads pp tg" lines. */
    fun bench(threads: IntArray, nTok: Int = 64): String = LlamaBridge.nativeBench(handle, threads, nTok, this.threads)

    override fun close() = LlamaBridge.nativeFree(handle)

    companion object {
        private const val TAG = "LocalNemotron"
        private const val N_CTX = 2048

        /** Performance cores only: on big.LITTLE phones the little cores slow every matmul down to their pace. */
        fun bigCores(): Int {
            val freqs = (0 until Runtime.getRuntime().availableProcessors()).mapNotNull { i ->
                runCatching { File("/sys/devices/system/cpu/cpu$i/cpufreq/cpuinfo_max_freq").readText().trim().toLong() }.getOrNull()
            }
            if (freqs.isEmpty()) return 4
            val top = freqs.max()
            return freqs.count { it >= top * 0.6 }.coerceIn(2, 8)
        }

        /** Slow (maps ~2.5 GB and evaluates the system prompt): call once, off the main thread. */
        fun load(model: File, threads: Int = bigCores()): LocalNemotron? {
            if (!LlamaBridge.available || !model.exists()) return null
            val h = LlamaBridge.nativeLoad(model.absolutePath, threads, N_CTX)
            if (h == 0L) return null
            if (!LlamaBridge.nativeSetPrefix(h, Prompt.PREFIX)) { LlamaBridge.nativeFree(h); return null }
            Log.i(TAG, "ready with $threads threads")
            return LocalNemotron(h, threads)
        }
    }
}
