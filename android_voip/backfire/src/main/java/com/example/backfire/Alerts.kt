package com.example.backfire

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.media.AudioManager
import android.media.ToneGenerator
import android.os.Build
import android.os.VibrationEffect
import android.os.Vibrator
import android.os.VibratorManager
import androidx.core.app.NotificationCompat
import com.example.backfire.ui.AlertActivity

/**
 * The scam alert, shown over Demo VoIP's call screen: two beeps, a vibration, a heads-up notification with the three
 * buttons, and a full-screen alert where Android allows it.
 */
object Alerts {
    const val CH_STATUS = "status"
    const val CH_ALERT = "alert"
    private const val ID_ALERT = 7
    const val EXTRA_ACTION = "action"

    fun channels(ctx: Context) {
        val nm = ctx.getSystemService(NotificationManager::class.java)
        nm.createNotificationChannel(NotificationChannel(CH_STATUS, "Live Guard status", NotificationManager.IMPORTANCE_LOW))
        nm.createNotificationChannel(NotificationChannel(CH_ALERT, "Scam alerts", NotificationManager.IMPORTANCE_HIGH).apply {
            setSound(null, null)  // we play our own two beeps into the call audio
            enableVibration(false)
        })
    }

    private fun actionIntent(ctx: Context, action: String, code: Int) = PendingIntent.getBroadcast(
        ctx, code, Intent(ctx, ActionReceiver::class.java).putExtra(EXTRA_ACTION, action),
        PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
    )

    fun alert(ctx: Context, peer: String, chips: List<String>, sgsAvailable: Boolean) {
        channels(ctx)
        val full = PendingIntent.getActivity(
            ctx, 1, Intent(ctx, AlertActivity::class.java).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
        )
        val n = NotificationCompat.Builder(ctx, CH_ALERT)
            .setSmallIcon(android.R.drawable.stat_sys_warning)
            .setContentTitle("⚠ Be careful. This may be a scam.")
            .setContentText(chips.joinToString(" · "))
            .setSubText(peer)
            .setPriority(NotificationCompat.PRIORITY_MAX)
            .setCategory(NotificationCompat.CATEGORY_CALL)
            .setOngoing(true)
            .setContentIntent(full)
            .setFullScreenIntent(full, true)
            .apply { if (sgsAvailable) addAction(0, "Scammer Get Scammed", actionIntent(ctx, "scammer_get_scammed", 10)) }
            .addAction(0, "Hang up", actionIntent(ctx, "hang_up", 11))
            .addAction(0, "Continue", actionIntent(ctx, "continue", 12))
            .build()
        ctx.getSystemService(NotificationManager::class.java).notify(ID_ALERT, n)
        // Best effort: Android may block activity starts from the background; the notification covers that case.
        runCatching { ctx.startActivity(Intent(ctx, AlertActivity::class.java).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)) }
        beep(ctx)
    }

    fun handled(ctx: Context, peer: String) {
        channels(ctx)
        val open = PendingIntent.getActivity(
            ctx, 2, Intent(ctx, AlertActivity::class.java).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK), PendingIntent.FLAG_IMMUTABLE,
        )
        val n = NotificationCompat.Builder(ctx, CH_ALERT)
            .setSmallIcon(android.R.drawable.ic_lock_lock)
            .setContentTitle("✓ Handled for you")
            .setContentText("Backfire's decoy is talking to $peer on this phone. You can put the phone down.")
            .setContentIntent(open)
            .setAutoCancel(true)
            .build()
        ctx.getSystemService(NotificationManager::class.java).notify(ID_ALERT, n)
        runCatching { ctx.startActivity(Intent(ctx, AlertActivity::class.java).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)) }
    }

    fun cancel(ctx: Context) = ctx.getSystemService(NotificationManager::class.java).cancel(ID_ALERT)

    private fun beep(ctx: Context) {
        runCatching {
            val t = ToneGenerator(AudioManager.STREAM_VOICE_CALL, 90)
            t.startTone(ToneGenerator.TONE_PROP_BEEP2, 400)
        }
        runCatching {
            val v = if (Build.VERSION.SDK_INT >= 31) ctx.getSystemService(VibratorManager::class.java).defaultVibrator
            else @Suppress("DEPRECATION") ctx.getSystemService(Vibrator::class.java)
            v.vibrate(VibrationEffect.createWaveform(longArrayOf(0, 150, 100, 150), -1))
        }
    }
}

/** The notification's three buttons. */
class ActionReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        intent.getStringExtra(Alerts.EXTRA_ACTION)?.let { Guard.action(it) }
    }
}
