package com.example.voip.consumer

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.Service
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.IBinder
import android.util.Log
import androidx.core.app.NotificationCompat
import androidx.core.app.ServiceCompat
import androidx.core.content.ContextCompat
import com.example.voip.export.ICallAudioService
import com.example.voip.export.VoipExport
import kotlinx.coroutines.flow.update
import java.io.File

/**
 * Foreground service that binds to the VoIP app and records call audio.
 * Keeping this in a foreground service stops Android from freezing (and then killing)
 * the app while audio frames are streaming in.
 */
class RecorderService : Service() {

    companion object {
        private const val CHANNEL = "listening"
        private const val ACTION_STOP = "com.example.voip.consumer.STOP"

        fun start(context: Context) =
            ContextCompat.startForegroundService(context, Intent(context, RecorderService::class.java))

        fun stop(context: Context) =
            context.startService(Intent(context, RecorderService::class.java).setAction(ACTION_STOP))
    }

    private var service: ICallAudioService? = null
    private var bound = false

    private val connection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName, binder: IBinder) {
            service = ICallAudioService.Stub.asInterface(binder).also { it.registerListener(CallAudioReceiver) }
            CallAudioReceiver.state.update { it.copy(bound = true, lastEvent = "Waiting for a call…") }
            Log.i(TAG, "bound to VoIP app, active call=${service?.activeCallId}")
        }

        override fun onServiceDisconnected(name: ComponentName) {
            service = null
            CallAudioReceiver.state.update { it.copy(bound = false, lastEvent = "VoIP app went away; reconnecting…") }
        }
    }

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onCreate() {
        super.onCreate()
        CallAudioReceiver.dir = File(getExternalFilesDir(null), "calls").apply { mkdirs() }
        getSystemService(NotificationManager::class.java).createNotificationChannel(
            NotificationChannel(CHANNEL, "Listening for calls", NotificationManager.IMPORTANCE_LOW)
        )
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        if (intent?.action == ACTION_STOP) {
            ServiceCompat.stopForeground(this, ServiceCompat.STOP_FOREGROUND_REMOVE)
            stopSelf()
            return START_NOT_STICKY
        }

        val open = PendingIntent.getActivity(
            this, 0, Intent(this, ReceiverActivity::class.java), PendingIntent.FLAG_IMMUTABLE
        )
        val notification = NotificationCompat.Builder(this, CHANNEL)
            .setSmallIcon(android.R.drawable.ic_btn_speak_now)
            .setContentTitle("Call Audio Receiver")
            .setContentText("Recording calls from Demo VoIP")
            .setOngoing(true)
            .setContentIntent(open)
            .build()
        val type = if (Build.VERSION.SDK_INT >= 34) ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE else 0
        ServiceCompat.startForeground(this, 1, notification, type)

        if (!bound) {
            bound = runCatching { bindService(VoipExport.bindIntent(), connection, Context.BIND_AUTO_CREATE) }
                .onFailure { Log.e(TAG, "bind failed", it) }
                .getOrDefault(false)
            if (!bound) CallAudioReceiver.state.update {
                it.copy(lastEvent = "Can't bind. Install the VoIP app first, then reinstall this app (same signing key).")
            }
        }
        return START_STICKY
    }

    override fun onDestroy() {
        runCatching { service?.unregisterListener(CallAudioReceiver) }
        if (bound) runCatching { unbindService(connection) }
        bound = false
        CallAudioReceiver.state.update { it.copy(bound = false, lastEvent = "Stopped") }
        super.onDestroy()
    }

    private val TAG = "RecorderService"
}
