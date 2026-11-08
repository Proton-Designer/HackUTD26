package com.example.voip.call

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.Person
import com.example.voip.ui.MainActivity

object Notifications {
    const val ONGOING_ID = 1
    private const val INCOMING_ID = 2
    private const val MISSED_ID_BASE = 1000

    private const val CH_ONGOING = "ongoing"
    private const val CH_INCOMING = "incoming_calls"
    private const val CH_MISSED = "missed_calls"

    fun createChannels(context: Context) {
        val nm = context.getSystemService(NotificationManager::class.java)
        nm.createNotificationChannel(NotificationChannel(CH_ONGOING, "Online status and active call", NotificationManager.IMPORTANCE_LOW))
        nm.createNotificationChannel(
            NotificationChannel(CH_INCOMING, "Incoming calls", NotificationManager.IMPORTANCE_HIGH).apply {
                setSound(null, null) // CallEffects rings and vibrates itself
                enableVibration(false)
            }
        )
        nm.createNotificationChannel(NotificationChannel(CH_MISSED, "Missed calls", NotificationManager.IMPORTANCE_DEFAULT))
    }

    /** True if the system will let us show the incoming-call screen over the lock screen (Android 14+ asks the user). */
    fun canUseFullScreen(context: Context): Boolean =
        Build.VERSION.SDK_INT < 34 || context.getSystemService(NotificationManager::class.java).canUseFullScreenIntent()

    fun ongoing(context: Context, s: UiState): Notification {
        val b = NotificationCompat.Builder(context, CH_ONGOING)
            .setSmallIcon(android.R.drawable.sym_action_call)
            .setOngoing(true)
            .setContentIntent(openApp(context))
            .setCategory(NotificationCompat.CATEGORY_CALL)

        val call = s.call
        val peer = call.peerName
        if (peer != null && call !is CallState.Incoming) {
            val status = when (call) {
                is CallState.Outgoing -> "Calling…"
                is CallState.Connecting -> "Connecting…"
                is CallState.Active -> if (s.reconnecting) "Reconnecting…" else "Ongoing call"
                else -> ""
            }
            if (call is CallState.Active) b.setUsesChronometer(true).setWhen(call.startedAtMs)
            return b.setContentTitle(peer).setContentText(status)
                .setStyle(NotificationCompat.CallStyle.forOngoingCall(person(peer), serviceAction(context, CallService.ACTION_HANGUP)))
                .build()
        }

        val text = if (s.connection == Connection.CONNECTED) "Online as ${s.myId} — you can receive calls" else "Connecting as ${s.myId}…"
        return b.setContentTitle("Demo VoIP").setContentText(text)
            .setCategory(NotificationCompat.CATEGORY_SERVICE)
            .addAction(0, "Go offline", serviceAction(context, CallService.ACTION_STOP))
            .build()
    }

    fun showIncoming(context: Context, peer: String) {
        val fullScreen = openApp(context)
        val answer = openApp(context, MainActivity.ACTION_ANSWER, requestCode = 1)
        val decline = serviceAction(context, CallService.ACTION_DECLINE)
        val b = NotificationCompat.Builder(context, CH_INCOMING)
            .setSmallIcon(android.R.drawable.sym_call_incoming)
            .setContentTitle(peer)
            .setContentText("Incoming call")
            .setCategory(NotificationCompat.CATEGORY_CALL)
            .setPriority(NotificationCompat.PRIORITY_MAX)
            .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
            .setOngoing(true)
            .setContentIntent(fullScreen)
            .setFullScreenIntent(fullScreen, true)

        if (canUseFullScreen(context)) {
            b.setStyle(NotificationCompat.CallStyle.forIncomingCall(person(peer), decline, answer))
        } else {
            b.addAction(0, "Decline", decline).addAction(0, "Answer", answer)
        }
        context.getSystemService(NotificationManager::class.java).notify(INCOMING_ID, b.build())
    }

    fun cancelIncoming(context: Context) =
        context.getSystemService(NotificationManager::class.java).cancel(INCOMING_ID)

    fun showMissed(context: Context, peer: String, atMs: Long) {
        val n = NotificationCompat.Builder(context, CH_MISSED)
            .setSmallIcon(android.R.drawable.sym_call_missed)
            .setContentTitle("Missed call")
            .setContentText(peer)
            .setWhen(atMs)
            .setShowWhen(true)
            .setCategory(NotificationCompat.CATEGORY_MISSED_CALL)
            .setAutoCancel(true)
            .setContentIntent(openApp(context, MainActivity.ACTION_SHOW_RECENTS, requestCode = 2))
            .build()
        context.getSystemService(NotificationManager::class.java).notify(MISSED_ID_BASE + peer.hashCode() % 1000, n)
    }

    private fun person(name: String) = Person.Builder().setName(name).setImportant(true).build()

    private fun openApp(context: Context, action: String = Intent.ACTION_MAIN, requestCode: Int = 0): PendingIntent {
        val intent = Intent(context, MainActivity::class.java)
            .setAction(action)
            .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_SINGLE_TOP)
        return PendingIntent.getActivity(context, requestCode, intent, PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
    }

    private fun serviceAction(context: Context, action: String): PendingIntent = PendingIntent.getService(
        context, action.hashCode(), Intent(context, CallService::class.java).setAction(action),
        PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
    )
}
