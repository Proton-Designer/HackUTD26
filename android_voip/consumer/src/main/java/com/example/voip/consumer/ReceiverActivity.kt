package com.example.voip.consumer

import android.Manifest
import android.content.pm.PackageManager
import android.media.MediaPlayer
import android.os.Build
import androidx.activity.result.contract.ActivityResultContracts
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Card
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.voip.export.ICallAudioListener
import com.example.voip.export.VoipExport
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.update
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import kotlin.math.sqrt

data class ReceiverState(
    val bound: Boolean = false,
    val callId: String? = null,
    val peer: String? = null,
    val localLevel: Float = 0f,
    val remoteLevel: Float = 0f,
    val localFormat: String = "",
    val remoteFormat: String = "",
    val recordings: List<File> = emptyList(),
    val lastEvent: String = "Waiting for a call…",
)

/**
 * Receives live call audio from the VoIP app and writes each side to its own WAV file
 * under Android/data/com.example.voip.consumer/files/calls/.
 */
object CallAudioReceiver : ICallAudioListener.Stub() {
    val state = MutableStateFlow(ReceiverState())
    lateinit var dir: File

    private val lock = Any()
    private var currentCall: String? = null
    private var currentPeer: String = "unknown"
    private val writers = HashMap<Int, WavWriter>()

    fun refreshRecordings() {
        val files = dir.listFiles { f -> f.extension == "wav" }?.sortedByDescending { it.lastModified() } ?: emptyList()
        state.update { it.copy(recordings = files) }
    }

    override fun onCallStarted(callId: String, peerId: String, outgoing: Boolean) {
        synchronized(lock) {
            closeWriters()
            currentCall = callId
            currentPeer = peerId
        }
        state.update { it.copy(callId = callId, peer = peerId, lastEvent = "Call ${if (outgoing) "to" else "from"} $peerId started") }
    }

    override fun onAudioFrame(callId: String, source: Int, pcm16: ByteArray, sampleRate: Int, channels: Int, timestampMs: Long) {
        synchronized(lock) {
            if (callId != currentCall) { // we bound mid-call and missed onCallStarted
                closeWriters()
                currentCall = callId
                currentPeer = "unknown"
                state.update { it.copy(callId = callId, peer = currentPeer) }
            }
            val writer = writers.getOrPut(source) {
                val stamp = SimpleDateFormat("yyyyMMdd-HHmmss", Locale.US).format(Date())
                val side = if (source == VoipExport.SOURCE_LOCAL) "local" else "remote"
                WavWriter(File(dir, "${stamp}_${currentPeer}_$side.wav"), sampleRate, channels)
            }
            writer.write(pcm16)
        }

        val level = rms(pcm16)
        val fmt = "$sampleRate Hz, $channels ch"
        state.update {
            if (source == VoipExport.SOURCE_LOCAL) it.copy(localLevel = level, localFormat = fmt)
            else it.copy(remoteLevel = level, remoteFormat = fmt)
        }
    }

    override fun onCallEnded(callId: String, reason: String) {
        synchronized(lock) {
            if (callId == currentCall) {
                closeWriters()
                currentCall = null
            }
        }
        state.update { it.copy(callId = null, peer = null, localLevel = 0f, remoteLevel = 0f, lastEvent = "Call ended ($reason)") }
        refreshRecordings()
    }

    private fun closeWriters() {
        writers.values.forEach { runCatching { it.close() } }
        writers.clear()
    }

    /** RMS of 16-bit LE PCM, scaled to 0..1 for the level meter. */
    private fun rms(pcm: ByteArray): Float {
        var sum = 0.0
        val n = pcm.size / 2
        if (n == 0) return 0f
        for (i in 0 until n) {
            val s = ((pcm[2 * i + 1].toInt() shl 8) or (pcm[2 * i].toInt() and 0xFF)).toShort().toDouble()
            sum += s * s
        }
        return (sqrt(sum / n) / 8000.0).coerceIn(0.0, 1.0).toFloat()
    }
}

class ReceiverActivity : ComponentActivity() {
    private var player: MediaPlayer? = null

    private val notificationPermission =
        registerForActivityResult(ActivityResultContracts.RequestPermission()) { }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        CallAudioReceiver.dir = File(getExternalFilesDir(null), "calls").apply { mkdirs() }
        CallAudioReceiver.refreshRecordings()

        if (Build.VERSION.SDK_INT >= 33 &&
            checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
        ) notificationPermission.launch(Manifest.permission.POST_NOTIFICATIONS)

        // Recording lives in a foreground service so it keeps working when this screen is closed.
        RecorderService.start(this)

        setContent {
            MaterialTheme {
                Surface(Modifier.fillMaxSize()) {
                    val s by CallAudioReceiver.state.collectAsStateWithLifecycle()
                    ReceiverScreen(
                        s,
                        onPlay = ::play,
                        onToggle = { if (s.bound) RecorderService.stop(this) else RecorderService.start(this) },
                    )
                }
            }
        }
    }

    private fun play(file: File) {
        player?.release()
        player = MediaPlayer().apply {
            setDataSource(file.path)
            prepare()
            start()
        }
    }

    override fun onDestroy() {
        player?.release()
        super.onDestroy()
    }
}

@Composable
private fun ReceiverScreen(s: ReceiverState, onPlay: (File) -> Unit, onToggle: () -> Unit) {
    Column(
        Modifier.fillMaxSize().safeDrawingPadding().padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp),
    ) {
        Text("Call Audio Receiver", style = MaterialTheme.typography.headlineMedium)
        Row(verticalAlignment = Alignment.CenterVertically) {
            Text(
                if (s.bound) "● Connected to VoIP app" else "○ Not connected",
                color = if (s.bound) Color(0xFF2E7D32) else Color.Gray,
                modifier = Modifier.weight(1f),
            )
            TextButton(onClick = onToggle) { Text(if (s.bound) "Stop" else "Start") }
        }
        Text(s.lastEvent)

        if (s.callId != null) {
            Card(Modifier.fillMaxWidth()) {
                Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Text("Live: ${s.peer}", style = MaterialTheme.typography.titleMedium)
                    Meter("Me (mic)", s.localLevel, s.localFormat)
                    Meter("Them", s.remoteLevel, s.remoteFormat)
                }
            }
        }

        Text("Recordings", style = MaterialTheme.typography.titleMedium)
        LazyColumn {
            items(s.recordings, key = { it.path }) { f ->
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text("${f.name}  (${f.length() / 1024} KB)", Modifier.weight(1f), style = MaterialTheme.typography.bodySmall)
                    TextButton(onClick = { onPlay(f) }) { Text("Play") }
                }
            }
        }
    }
}

@Composable
private fun Meter(label: String, level: Float, format: String) {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Text(label, Modifier.width(90.dp))
        LinearProgressIndicator(progress = { level }, modifier = Modifier.weight(1f))
    }
    if (format.isNotEmpty()) Text(format, style = MaterialTheme.typography.bodySmall, color = Color.Gray)
}
