package com.example.backfire

import android.app.PendingIntent
import android.app.Service
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.util.Log
import androidx.core.app.NotificationCompat
import androidx.core.app.ServiceCompat
import androidx.core.content.ContextCompat
import com.example.backfire.ui.MainActivity
import com.example.voip.export.ICallAudioListener
import com.example.voip.export.ICallAudioService
import com.example.voip.export.VoipExport

/**
 * Background half of Backfire: stays bound to Demo VoIP's call-audio export and feeds the CALLER's side to [Guard].
 * A foreground service, because Android freezes background apps and a frozen app receiving audio gets killed.
 */
class GuardService : Service() {
    companion object {
        private const val TAG = "GuardService"
        fun start(context: Context) =
            ContextCompat.startForegroundService(context, Intent(context, GuardService::class.java))
    }

    private var bound = false
    private var service: ICallAudioService? = null
    private val main = Handler(Looper.getMainLooper())

    private val listener = object : ICallAudioListener.Stub() {
        override fun onCallStarted(callId: String, peerId: String, outgoing: Boolean) = Guard.onCallStarted(callId, peerId, outgoing)

        override fun onAudioFrame(callId: String, source: Int, pcm16: ByteArray, sampleRate: Int, channels: Int, timestampMs: Long) {
            // The caller only. Maria's own microphone (SOURCE_LOCAL) is dropped here and never processed.
            if (source == VoipExport.SOURCE_REMOTE) Guard.onCallerAudio(callId, pcm16, sampleRate, channels)
        }

        override fun onCallEnded(callId: String, reason: String) = Guard.onCallEnded(callId, reason)
    }

    private val connection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName, binder: IBinder) {
            service = ICallAudioService.Stub.asInterface(binder).also { it.registerListener(listener) }
            Guard.voip = service
            Guard.setBound(true)
            Log.i(TAG, "bound to Demo VoIP")
        }

        override fun onServiceDisconnected(name: ComponentName) {
            service = null
            Guard.voip = null
            Guard.setBound(false)
        }
    }

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        Alerts.channels(this)
        val open = PendingIntent.getActivity(this, 0, Intent(this, MainActivity::class.java), PendingIntent.FLAG_IMMUTABLE)
        val n = NotificationCompat.Builder(this, Alerts.CH_STATUS)
            .setSmallIcon(android.R.drawable.ic_lock_lock)
            .setContentTitle("Backfire Live Guard is on")
            .setContentText("Listens to unknown callers only, never to you")
            .setOngoing(true)
            .setContentIntent(open)
            .build()
        val type = if (Build.VERSION.SDK_INT >= 34) ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE else 0
        ServiceCompat.startForeground(this, 1, n, type)
        bind()
        return START_STICKY
    }

    private fun bind() {
        if (bound) return
        bound = runCatching { bindService(VoipExport.bindIntent(), connection, Context.BIND_AUTO_CREATE) }.getOrDefault(false)
        if (!bound) {
            Guard.setBound(false, missing = true)
            main.postDelayed({ bind() }, 5000)  // Demo VoIP may be installed later
        }
    }

    override fun onDestroy() {
        runCatching { service?.unregisterListener(listener) }
        if (bound) runCatching { unbindService(connection) }
        bound = false
        Guard.setBound(false)
        super.onDestroy()
    }
}
