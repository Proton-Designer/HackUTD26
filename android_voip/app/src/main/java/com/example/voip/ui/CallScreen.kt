package com.example.voip.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.BluetoothAudio
import androidx.compose.material.icons.filled.Call
import androidx.compose.material.icons.filled.CallEnd
import androidx.compose.material.icons.filled.Headset
import androidx.compose.material.icons.filled.Mic
import androidx.compose.material.icons.filled.MicOff
import androidx.compose.material.icons.filled.PhoneInTalk
import androidx.compose.material.icons.automirrored.filled.VolumeUp
import androidx.compose.material3.FilledIconButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableLongStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.voip.call.AudioRoute
import com.example.voip.call.CallManager
import com.example.voip.call.CallState
import com.example.voip.call.UiState
import com.example.voip.call.peerName
import kotlinx.coroutines.delay

private val Green = Color(0xFF2E7D32)
private val Red = Color(0xFFD32F2F)

/** Full-screen incoming / in-call UI, like the system dialer's. */
@Composable
fun CallScreen(state: UiState) {
    val call = state.call
    val peer = call.peerName ?: return

    // One column: header on top, controls at the bottom, flexible space between.
    Column(
        Modifier
            .fillMaxSize()
            .background(Brush.verticalGradient(listOf(Color(0xFF0D1B2A), Color(0xFF1B263B))))
            .safeDrawingPadding()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Column(Modifier.fillMaxWidth().padding(top = 48.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Avatar(peer, size = 112.dp)
            Spacer(Modifier.height(20.dp))
            Text(peer, color = Color.White, fontSize = 34.sp, fontWeight = FontWeight.Light)
            Spacer(Modifier.height(8.dp))
            when (call) {
                is CallState.Incoming -> StatusText("Incoming call")
                is CallState.Outgoing -> StatusText("Calling…")
                is CallState.Connecting -> StatusText("Connecting…")
                is CallState.Active -> when {
                    state.reconnecting -> StatusText("Reconnecting…", Color(0xFFFFB74D))
                    else -> CallTimer(call.startedAtMs)
                }
                CallState.Idle -> Unit
            }
        }

        if (state.decoy) {
            Spacer(Modifier.height(24.dp))
            Text("🛡 Backfire is talking to this caller for you.\nYou can put the phone down.", color = Color(0xFFB39DDB),
                fontSize = 18.sp, textAlign = androidx.compose.ui.text.style.TextAlign.Center)
        }
        Spacer(Modifier.weight(1f))
        Column(Modifier.fillMaxWidth().padding(bottom = 24.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            if (call is CallState.Incoming) {
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly) {
                    RoundAction(Icons.Filled.CallEnd, "Decline", Red) { CallManager.decline() }
                    RoundAction(Icons.Filled.Call, "Answer", Green) { CallManager.accept() }
                }
            } else {
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceEvenly) {
                    ToggleAction(
                        icon = if (state.muted) Icons.Filled.MicOff else Icons.Filled.Mic,
                        label = if (state.muted) "Unmute" else "Mute",
                        on = state.muted,
                    ) { CallManager.setMuted(!state.muted) }
                    ToggleAction(
                        icon = when (state.route) {
                            AudioRoute.SPEAKER -> Icons.AutoMirrored.Filled.VolumeUp
                            AudioRoute.BLUETOOTH -> Icons.Filled.BluetoothAudio
                            AudioRoute.HEADSET -> Icons.Filled.Headset
                            AudioRoute.EARPIECE -> Icons.Filled.PhoneInTalk
                        },
                        label = when (state.route) {
                            AudioRoute.SPEAKER -> "Speaker"
                            AudioRoute.BLUETOOTH -> "Bluetooth"
                            AudioRoute.HEADSET -> "Headset"
                            AudioRoute.EARPIECE -> "Speaker"
                        },
                        on = state.route == AudioRoute.SPEAKER,
                    ) { CallManager.setSpeaker(!state.speaker) }
                }
                Spacer(Modifier.height(40.dp))
                RoundAction(Icons.Filled.CallEnd, "End", Red) { CallManager.hangUp() }
            }
        }
    }
}

@Composable
private fun StatusText(text: String, color: Color = Color(0xFFB0BEC5)) {
    Text(text, color = color, fontSize = 18.sp)
}

@Composable
private fun CallTimer(startedAtMs: Long) {
    var now by remember { mutableLongStateOf(System.currentTimeMillis()) }
    LaunchedEffect(startedAtMs) {
        while (true) {
            now = System.currentTimeMillis()
            delay(500)
        }
    }
    val secs = ((now - startedAtMs) / 1000).coerceAtLeast(0)
    StatusText(if (secs >= 3600) "%d:%02d:%02d".format(secs / 3600, secs / 60 % 60, secs % 60) else "%d:%02d".format(secs / 60, secs % 60))
}

@Composable
private fun RoundAction(icon: ImageVector, label: String, color: Color, onClick: () -> Unit) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        FilledIconButton(
            onClick = onClick,
            modifier = Modifier.size(76.dp),
            shape = CircleShape,
            colors = IconButtonDefaults.filledIconButtonColors(containerColor = color, contentColor = Color.White),
        ) { Icon(icon, contentDescription = label, modifier = Modifier.size(34.dp)) }
        Spacer(Modifier.height(8.dp))
        Text(label, color = Color.White)
    }
}

@Composable
private fun ToggleAction(icon: ImageVector, label: String, on: Boolean, onClick: () -> Unit) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        FilledIconButton(
            onClick = onClick,
            modifier = Modifier.size(64.dp),
            shape = CircleShape,
            colors = IconButtonDefaults.filledIconButtonColors(
                containerColor = if (on) Color.White else Color.White.copy(alpha = 0.15f),
                contentColor = if (on) Color(0xFF0D1B2A) else Color.White,
            ),
        ) { Icon(icon, contentDescription = label, modifier = Modifier.size(28.dp)) }
        Spacer(Modifier.height(8.dp))
        Text(label, color = Color.White)
    }
}
