package com.example.voip.call

import android.app.NotificationManager
import android.app.Service
import android.content.Context
import android.content.Intent
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.IBinder
import androidx.core.app.ServiceCompat
import androidx.core.content.ContextCompat
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.cancel
import kotlinx.coroutines.flow.distinctUntilChanged
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.launch

/**
 * Foreground service (type "microphone") that keeps the signaling socket open so calls
 * ring while the UI is closed, and keeps mic access while the screen is off.
 * Must be started while the activity is visible and RECORD_AUDIO is granted.
 */
class CallService : Service() {

    companion object {
        private const val EXTRA_SERVER = "server"
        private const val EXTRA_ID = "id"
        const val ACTION_STOP = "com.example.voip.STOP"
        const val ACTION_DECLINE = "com.example.voip.DECLINE"
        const val ACTION_HANGUP = "com.example.voip.HANGUP"

        fun start(context: Context, serverUrl: String, myId: String) {
            val intent = Intent(context, CallService::class.java)
                .putExtra(EXTRA_SERVER, serverUrl)
                .putExtra(EXTRA_ID, myId)
            ContextCompat.startForegroundService(context, intent)
        }

        fun stop(context: Context) {
            context.startService(Intent(context, CallService::class.java).setAction(ACTION_STOP))
        }
    }

    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main)
    private var collector: Job? = null

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onCreate() {
        super.onCreate()
        Notifications.createChannels(this)
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        when (intent?.action) {
            ACTION_STOP -> {
                collector?.cancel()
                collector = null
                CallManager.disconnect()
                ServiceCompat.stopForeground(this, ServiceCompat.STOP_FOREGROUND_REMOVE)
                stopSelf()
                return START_NOT_STICKY
            }
            ACTION_DECLINE -> { CallManager.decline(); return START_NOT_STICKY }
            ACTION_HANGUP -> { CallManager.hangUp(); return START_NOT_STICKY }
        }

        val server = intent?.getStringExtra(EXTRA_SERVER)
        val id = intent?.getStringExtra(EXTRA_ID)
        if (server == null || id == null) {
            stopSelf()
            return START_NOT_STICKY
        }

        val type = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) ServiceInfo.FOREGROUND_SERVICE_TYPE_MICROPHONE else 0
        val initial = CallManager.state.value.copy(myId = id, connection = Connection.CONNECTING)
        ServiceCompat.startForeground(this, Notifications.ONGOING_ID, Notifications.ongoing(this, initial), type)

        CallManager.connect(server, id)
        if (collector == null) {
            val nm = getSystemService(NotificationManager::class.java)
            collector = scope.launch {
                // Only rebuild the notification when something it shows changes (not on every user-list update).
                CallManager.state
                    .map { it.copy(users = emptyList(), message = null, muted = false, speaker = false) }
                    .distinctUntilChanged()
                    .collect { nm.notify(Notifications.ONGOING_ID, Notifications.ongoing(this@CallService, it)) }
            }
        }
        return START_NOT_STICKY
    }

    override fun onDestroy() {
        scope.cancel()
        Notifications.cancelIncoming(this)
        super.onDestroy()
    }
}
