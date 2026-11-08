package com.example.backfire

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent

/** Debug builds only: speak a sentence into the current call through Demo VoIP's injection (tests the decoy's voice path). */
class DebugReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.getStringExtra("voice_wav") != null) {   // --es voice_wav name.wav (pushed to the app's external files dir)
            val f = java.io.File(context.getExternalFilesDir(null), intent.getStringExtra("voice_wav")!!)
            if (f.exists()) com.example.backfire.decoy.VoiceProfile.importWav(f.readBytes())
            return
        }
        val text = intent.getStringExtra("text") ?: "Hello, this is a test of the Backfire decoy voice."
        if (intent.getBooleanExtra("clone_test", false)) {   // --ez clone_test true: synthesize only (no call needed), log the result
            val p = goAsync()
            Thread {
                try {
                    val v = com.example.backfire.decoy.Voice(context)
                    val t0 = System.currentTimeMillis()
                    val r = v.synth(text)
                    android.util.Log.i("DebugReceiver", "clone_test: kind=${v.kind} audio=${r?.let { it.first.size / 2 * 1000 / it.second }} ms rate=${r?.second} in ${System.currentTimeMillis() - t0} ms")
                    r?.let { java.io.File(context.getExternalFilesDir(null), "clone_test.wav").writeBytes(com.example.backfire.decoy.VoiceProfile.wav(
                        ShortArray(it.first.size / 2).also { s -> java.nio.ByteBuffer.wrap(it.first).order(java.nio.ByteOrder.LITTLE_ENDIAN).asShortBuffer().get(s) }, it.second)) }
                    v.close()
                } finally { p.finish() }
            }.start()
            return
        }
        val p = goAsync()
        Thread { try { Guard.debugSay(text) } finally { p.finish() } }.start()
    }
}
