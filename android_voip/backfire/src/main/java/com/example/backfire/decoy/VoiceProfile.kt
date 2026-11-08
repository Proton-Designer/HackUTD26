package com.example.backfire.decoy

import android.annotation.SuppressLint
import android.content.Context
import android.media.AudioFormat
import android.media.AudioRecord
import android.media.MediaRecorder
import android.util.Log
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import java.io.ByteArrayOutputStream
import java.io.File
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.sqrt

data class VoiceState(
    val enrolled: Boolean = false,
    val recording: Boolean = false,
    val seconds: Float = 0f,
    val level: Float = 0f,
    val consentVersion: String? = null,
    val message: String? = null,
)

/**
 * Maria's consented voice profile, entirely on this phone: she reads a paragraph once; we keep only the clearest 8 s
 * as the Magpie zero-shot prompt (app-private storage), never the rest. Delete removes it.
 * The microphone is used ONLY here, while she presses Record; never during calls.
 */
object VoiceProfile {
    private const val TAG = "VoiceProfile"
    const val RATE = 22050
    const val CONSENT_VERSION = "v1"
    private const val MIN_S = 3f
    private const val PROMPT_S = 8f
    private const val MAX_S = 60f

    val PARAGRAPH = "My grandmother kept a garden behind the little yellow house. Every spring we planted tomatoes, beans " +
        "and sunflowers taller than the fence. She said the secret was patience, good soil, and talking to the plants " +
        "on quiet mornings. I still think of her whenever I smell fresh basil."

    private lateinit var dir: File
    private val _state = MutableStateFlow(VoiceState())
    val state: StateFlow<VoiceState> = _state.asStateFlow()
    @Volatile private var stop = false

    private val prompt get() = File(dir, "prompt.wav")
    private val meta get() = File(dir, "consent.txt")

    fun init(context: Context) {
        dir = File(context.filesDir, "voice").apply { mkdirs() }
        _state.update { it.copy(enrolled = prompt.exists(), consentVersion = meta.takeIf { f -> f.exists() }?.readText()) }
    }

    /** The prompt WAV for Magpie, or null if Maria hasn't enrolled. */
    fun promptWav(): ByteArray? = prompt.takeIf { it.exists() }?.readBytes()

    fun delete() {
        prompt.delete(); meta.delete()
        _state.update { VoiceState(message = "Your voice profile was deleted.") }
    }

    fun stopRecording() { stop = true }

    /** Needs RECORD_AUDIO (asked by the screen). Records until [stopRecording] or 60 s, then builds the prompt. */
    @SuppressLint("MissingPermission")
    fun record(consented: Boolean) {
        if (!consented) { _state.update { it.copy(message = "Please agree first.") }; return }
        if (_state.value.recording) return
        stop = false
        Thread {
            val minBuf = AudioRecord.getMinBufferSize(RATE, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_16BIT)
            val rec = runCatching {
                AudioRecord(MediaRecorder.AudioSource.VOICE_RECOGNITION, RATE, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_16BIT, minBuf * 4)
            }.getOrNull()
            if (rec == null || rec.state != AudioRecord.STATE_INITIALIZED) {
                _state.update { it.copy(message = "Can't use the microphone.") }; return@Thread
            }
            val all = ByteArrayOutputStream()
            val buf = ShortArray(RATE / 10)
            _state.update { it.copy(recording = true, seconds = 0f, message = null) }
            rec.startRecording()
            try {
                while (!stop && all.size() < MAX_S * RATE * 2) {
                    val n = rec.read(buf, 0, buf.size)
                    if (n <= 0) continue
                    val bb = ByteBuffer.allocate(n * 2).order(ByteOrder.LITTLE_ENDIAN)
                    var sum = 0.0
                    for (i in 0 until n) { bb.putShort(buf[i]); sum += buf[i] * buf[i].toDouble() }
                    all.write(bb.array())
                    val level = (sqrt(sum / n) / 6000.0).toFloat().coerceIn(0f, 1f)
                    _state.update { it.copy(seconds = all.size() / 2f / RATE, level = level) }
                }
            } finally {
                runCatching { rec.stop() }; rec.release()
            }
            finish(all.toByteArray())
        }.start()
    }

    private fun finish(pcm: ByteArray) {
        val samples = ShortArray(pcm.size / 2).also { ByteBuffer.wrap(pcm).order(ByteOrder.LITTLE_ENDIAN).asShortBuffer().get(it) }
        val win = (PROMPT_S * RATE).toInt()
        if (samples.size < MIN_S * RATE) {
            _state.update { it.copy(recording = false, message = "Too short. Please read the whole paragraph.") }; return
        }
        // Loudest 8 s window = the most speech (Magpie prompts work best as a few clean seconds, 3-10 s).
        var best = 0; var bestE = -1.0
        if (samples.size > win) {
            val hop = RATE / 4
            var start = 0
            while (start + win <= samples.size) {
                var e = 0.0
                for (i in start until start + win step 4) e += samples[i] * samples[i].toDouble()
                if (e > bestE) { bestE = e; best = start }
                start += hop
            }
        }
        val cut = samples.copyOfRange(best, minOf(samples.size, best + win))
        val rms = sqrt(cut.sumOf { it * it.toDouble() } / cut.size)
        if (rms < 300) {
            _state.update { it.copy(recording = false, message = "We couldn't hear you. Please try again a bit closer to the phone.") }; return
        }
        prompt.writeBytes(wav(cut, RATE))
        meta.writeText(CONSENT_VERSION)
        Log.i(TAG, "voice prompt saved: %.1f s of %.1f s".format(cut.size / RATE.toFloat(), samples.size / RATE.toFloat()))
        _state.update { VoiceState(enrolled = true, consentVersion = CONSENT_VERSION, message = "Your voice is set up.") }
    }

    /** Debug/test only: use an existing mono 16-bit WAV as the prompt (DebugReceiver). */
    fun importWav(bytes: ByteArray) {
        prompt.writeBytes(bytes); meta.writeText(CONSENT_VERSION)
        _state.update { VoiceState(enrolled = true, consentVersion = CONSENT_VERSION, message = "Voice imported (debug).") }
    }

    fun wav(s: ShortArray, rate: Int): ByteArray {
        val data = ByteBuffer.allocate(s.size * 2).order(ByteOrder.LITTLE_ENDIAN).apply { s.forEach { putShort(it) } }.array()
        val h = ByteBuffer.allocate(44).order(ByteOrder.LITTLE_ENDIAN)
        h.put("RIFF".toByteArray()).putInt(36 + data.size).put("WAVE".toByteArray()).put("fmt ".toByteArray())
            .putInt(16).putShort(1).putShort(1).putInt(rate).putInt(rate * 2).putShort(2).putShort(16)
            .put("data".toByteArray()).putInt(data.size)
        return h.array() + data
    }
}
