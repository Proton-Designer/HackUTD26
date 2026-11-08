package com.example.backfire.decoy

import android.content.Context
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice as TtsVoice
import android.util.Log
import java.io.File
import java.io.RandomAccessFile
import java.util.Locale
import java.util.UUID
import java.util.concurrent.CountDownLatch
import java.util.concurrent.TimeUnit

/**
 * The decoy's voice: Android's on-device text-to-speech, slowed down and pitched like an older woman.
 * Labeled synthetic. (A consented clone of Maria's voice would plug in here later.)
 */
class Voice(context: Context) {
    private val ctx = context.applicationContext
    private val ready = CountDownLatch(1)
    @Volatile private var ok = false
    private val tts: TextToSpeech = TextToSpeech(ctx) { status ->
        ok = status == TextToSpeech.SUCCESS
        ready.countDown()
    }

    init {
        Thread {
            if (!ready.await(5, TimeUnit.SECONDS) || !ok) { Log.e(TAG, "TTS unavailable"); return@Thread }
            tts.language = Locale.US
            pickVoice()?.let { tts.voice = it; Log.i(TAG, "voice: ${it.name}") }
            tts.setSpeechRate(0.88f)
            tts.setPitch(0.92f)
        }.start()
    }

    /** A local (offline) US English voice, preferring female-sounding ones. */
    private fun pickVoice(): TtsVoice? = runCatching {
        val us = tts.voices.filter { it.locale.language == "en" && it.locale.country == "US" && !it.isNetworkConnectionRequired }
        us.firstOrNull { "female" in it.name.lowercase() || it.name.lowercase().contains("sfg") || it.name.contains("-f-") }
            ?: us.firstOrNull()
    }.getOrNull()

    /** Text -> 16-bit mono PCM and its sample rate. Blocking (~100-400 ms for a sentence). */
    fun synth(text: String): Pair<ByteArray, Int>? {
        if (!ready.await(5, TimeUnit.SECONDS) || !ok) return null
        val f = File(ctx.cacheDir, "tts-${UUID.randomUUID()}.wav")
        val done = CountDownLatch(1)
        val id = f.name
        tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {}
            override fun onDone(utteranceId: String?) { if (utteranceId == id) done.countDown() }
            @Deprecated("Deprecated in Java") override fun onError(utteranceId: String?) { if (utteranceId == id) done.countDown() }
        })
        if (tts.synthesizeToFile(text, null, f, id) != TextToSpeech.SUCCESS) return null
        done.await(8, TimeUnit.SECONDS)
        return try { readWav(f) } catch (e: Exception) { Log.e(TAG, "bad wav", e); null } finally { f.delete() }
    }

    fun close() = tts.shutdown()

    /** Minimal RIFF reader: finds fmt + data chunks; returns mono PCM16 (first channel). */
    private fun readWav(f: File): Pair<ByteArray, Int>? {
        RandomAccessFile(f, "r").use { r ->
            val head = ByteArray(12); r.readFully(head)
            var rate = 0; var ch = 1; var bits = 16
            while (r.filePointer < r.length()) {
                val id = ByteArray(4); r.readFully(id)
                val size = Integer.reverseBytes(r.readInt())
                val tag = String(id)
                if (tag == "fmt ") {
                    val fmt = ByteArray(size); r.readFully(fmt)
                    ch = (fmt[2].toInt() and 0xFF) or (fmt[3].toInt() shl 8)
                    rate = (fmt[4].toInt() and 0xFF) or ((fmt[5].toInt() and 0xFF) shl 8) or ((fmt[6].toInt() and 0xFF) shl 16)
                    bits = (fmt[14].toInt() and 0xFF)
                } else if (tag == "data") {
                    val n = if (size <= 0 || size > r.length() - r.filePointer) (r.length() - r.filePointer).toInt() else size
                    val data = ByteArray(n); r.readFully(data)
                    if (bits != 16 || rate == 0) return null
                    if (ch == 1) return data to rate
                    val frames = n / (2 * ch)
                    val mono = ByteArray(frames * 2)
                    for (i in 0 until frames) { mono[2 * i] = data[2 * i * ch]; mono[2 * i + 1] = data[2 * i * ch + 1] }
                    return mono to rate
                } else r.skipBytes(size + (size and 1))
            }
        }
        return null
    }

    companion object { private const val TAG = "DecoyVoice" }
}
