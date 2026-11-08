package com.example.voip.call

import android.content.Context
import android.media.AudioDeviceInfo
import android.media.AudioManager
import android.media.Ringtone
import android.media.RingtoneManager
import android.media.ToneGenerator
import android.os.Build
import android.os.PowerManager
import android.os.VibrationEffect
import android.os.Vibrator
import android.os.VibratorManager

enum class AudioRoute { EARPIECE, SPEAKER, BLUETOOTH, HEADSET }

/** The "phone-like" side effects of a call: ringing, tones, vibration, proximity screen-off, audio routing. */
class CallEffects(private val context: Context) {
    private val audioManager = context.getSystemService(AudioManager::class.java)
    private val powerManager = context.getSystemService(PowerManager::class.java)
    private val vibrator: Vibrator =
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) context.getSystemService(VibratorManager::class.java).defaultVibrator
        else @Suppress("DEPRECATION") context.getSystemService(Vibrator::class.java)

    private var ringtone: Ringtone? = null
    private var toneGenerator: ToneGenerator? = null
    private var proximityLock: PowerManager.WakeLock? = null

    // ------------------------------------------------------------ incoming ring

    fun startRinging() {
        stopRinging()
        val mode = audioManager.ringerMode
        if (mode == AudioManager.RINGER_MODE_NORMAL) {
            ringtone = RingtoneManager.getRingtone(context, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE))?.apply {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) isLooping = true
                play()
            }
        }
        if (mode != AudioManager.RINGER_MODE_SILENT && vibrator.hasVibrator()) {
            vibrator.vibrate(VibrationEffect.createWaveform(longArrayOf(0, 800, 1200), 0))
        }
    }

    fun stopRinging() {
        ringtone?.stop()
        ringtone = null
        vibrator.cancel()
    }

    // ------------------------------------------------------------ tones the caller hears

    /** "Ring… ring…" while the other phone is ringing. */
    fun startRingback() = tone(ToneGenerator.TONE_SUP_RINGTONE, durationMs = -1)

    /** Busy signal after a decline. */
    fun playBusy() = tone(ToneGenerator.TONE_SUP_BUSY, durationMs = 2500)

    /** Short beep when a call ends. */
    fun playEnded() = tone(ToneGenerator.TONE_PROP_PROMPT, durationMs = 300)

    fun stopTones() {
        toneGenerator?.stopTone()
    }

    private fun tone(type: Int, durationMs: Int) {
        val gen = toneGenerator ?: runCatching { ToneGenerator(AudioManager.STREAM_VOICE_CALL, 80) }.getOrNull()
            ?.also { toneGenerator = it } ?: return
        gen.stopTone()
        gen.startTone(type, durationMs)
    }

    // ------------------------------------------------------------ in-call audio

    fun enterCallAudio() {
        audioManager.mode = AudioManager.MODE_IN_COMMUNICATION
    }

    fun exitCallAudio() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) audioManager.clearCommunicationDevice()
        else @Suppress("DEPRECATION") run { audioManager.isSpeakerphoneOn = false }
        audioManager.mode = AudioManager.MODE_NORMAL
    }

    /**
     * Speaker if requested; otherwise a connected Bluetooth/wired headset if there is one; otherwise the earpiece.
     * Returns the route actually chosen.
     */
    fun route(speaker: Boolean): AudioRoute {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            val devices = audioManager.availableCommunicationDevices
            val target = if (speaker) {
                devices.firstOrNull { it.type == AudioDeviceInfo.TYPE_BUILTIN_SPEAKER }
            } else {
                devices.firstOrNull { it.type in BLUETOOTH_TYPES } ?: devices.firstOrNull { it.type in WIRED_TYPES }
            }
            if (target == null) {
                audioManager.clearCommunicationDevice()
                return AudioRoute.EARPIECE
            }
            audioManager.setCommunicationDevice(target)
            return when (target.type) {
                AudioDeviceInfo.TYPE_BUILTIN_SPEAKER -> AudioRoute.SPEAKER
                in BLUETOOTH_TYPES -> AudioRoute.BLUETOOTH
                else -> AudioRoute.HEADSET
            }
        }
        @Suppress("DEPRECATION")
        audioManager.isSpeakerphoneOn = speaker
        return if (speaker) AudioRoute.SPEAKER else AudioRoute.EARPIECE
    }

    // ------------------------------------------------------------ proximity (screen off at the ear)

    fun setProximity(enabled: Boolean) {
        if (enabled) {
            if (proximityLock?.isHeld == true) return
            if (!powerManager.isWakeLockLevelSupported(PowerManager.PROXIMITY_SCREEN_OFF_WAKE_LOCK)) return
            proximityLock = powerManager.newWakeLock(PowerManager.PROXIMITY_SCREEN_OFF_WAKE_LOCK, "voip:proximity").apply {
                setReferenceCounted(false)
                acquire(3 * 60 * 60 * 1000L)
            }
        } else {
            proximityLock?.let { if (it.isHeld) it.release(PowerManager.RELEASE_FLAG_WAIT_FOR_NO_PROXIMITY) }
            proximityLock = null
        }
    }

    fun releaseAll() {
        stopRinging()
        stopTones()
        setProximity(false)
        exitCallAudio()
    }

    private companion object {
        val BLUETOOTH_TYPES = setOf(AudioDeviceInfo.TYPE_BLUETOOTH_SCO, AudioDeviceInfo.TYPE_BLE_HEADSET)
        val WIRED_TYPES = setOf(AudioDeviceInfo.TYPE_WIRED_HEADSET, AudioDeviceInfo.TYPE_USB_HEADSET)
    }
}
