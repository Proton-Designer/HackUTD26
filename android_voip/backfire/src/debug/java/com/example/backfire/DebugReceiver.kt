package com.example.backfire

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent

/** Debug builds only: speak a sentence into the current call through Demo VoIP's injection (tests the decoy's voice path). */
class DebugReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val text = intent.getStringExtra("text") ?: "Hello, this is a test of the Backfire decoy voice."
        val p = goAsync()
        Thread { try { Guard.debugSay(text) } finally { p.finish() } }.start()
    }
}
