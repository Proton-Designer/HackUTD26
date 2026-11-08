package com.example.backfire.ui

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.VerifiedUser
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.backfire.Guard

val Amber = Color(0xFFFFB300)
val Teal = Color(0xFF26A69A)
val Purple = Color(0xFF7E57C2)
val Danger = Color(0xFFD32F2F)
val Navy = Color(0xFF1B263B)

/** Over the call: the alert with Maria's three choices, then "Handled for you". Closes itself when there's nothing to show. */
class AlertActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                val st by Guard.state.collectAsStateWithLifecycle()
                val call = st.call
                when {
                    call != null && !call.decoyActive && (call.alertShown || call.note != null) -> AlertPanel(
                        peer = call.peer, chips = call.chips, sgsAvailable = st.cloudOk, note = call.note,
                    ) { a -> Guard.action(a); if (a != "scammer_get_scammed") finish() }
                    st.handled != null -> Handled(st.handled!!) {
                        Guard.dismissHandled(); finish()
                        // The decoy keeps the call going on its own: send Maria home rather than back to the call screen.
                        startActivity(android.content.Intent(android.content.Intent.ACTION_MAIN)
                            .addCategory(android.content.Intent.CATEGORY_HOME).addFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK))
                    }
                    else -> LaunchedEffect(Unit) { finish() }
                }
            }
        }
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun AlertPanel(peer: String, chips: List<String>, sgsAvailable: Boolean, note: String?, onAction: (String) -> Unit) {
    Column(
        Modifier.fillMaxSize().background(Color(0xFF3E2723)).safeDrawingPadding().padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(14.dp, Alignment.CenterVertically),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Icon(Icons.Filled.Warning, null, tint = Amber, modifier = Modifier.size(72.dp))
        Text("Be careful. This may be a scam.",
            color = Color.White, fontSize = 26.sp, fontWeight = FontWeight.Bold)
        Text(peer, color = Color(0xFFCFD8DC), fontSize = 18.sp)
        if (chips.isNotEmpty()) FlowRow(horizontalArrangement = Arrangement.spacedBy(6.dp, Alignment.CenterHorizontally), verticalArrangement = Arrangement.spacedBy(6.dp)) {
            chips.forEach {
                Text(it, color = Color.White, fontSize = 14.sp,
                    modifier = Modifier.background(Amber.copy(alpha = 0.35f), RoundedCornerShape(50)).padding(horizontal = 12.dp, vertical = 5.dp))
            }
        }
        note?.let { Text(it, color = Amber, fontSize = 15.sp) }
        Spacer(Modifier.height(8.dp))
        if (sgsAvailable) Big("Scammer Get Scammed", Purple) { onAction("scammer_get_scammed") }
        else Button(onClick = {}, enabled = false, modifier = Modifier.fillMaxWidth().height(56.dp)) {
            Text("Scammer Get Scammed not available", fontSize = 16.sp)
        }
        Big("Hang up", Danger) { onAction("hang_up") }
        Big("Continue", Color(0xFF546E7A)) { onAction("continue") }
        Text("Backfire listens to the caller only, never to you.", color = Color(0xFFB0BEC5), fontSize = 13.sp)
    }
}

@Composable
fun Handled(peer: String, onOk: () -> Unit) {
    Column(
        Modifier.fillMaxSize().background(Navy).safeDrawingPadding().padding(28.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Icon(Icons.Filled.VerifiedUser, null, tint = Purple, modifier = Modifier.size(96.dp))
        Text("Handled for you", color = Color.White, fontSize = 30.sp, fontWeight = FontWeight.Bold)
        Text("Backfire's decoy is talking to $peer on this phone, so they waste their time and not yours. Nothing about you is shared. " +
            "Calls from this number will be blocked when it's over.", color = Color(0xFFCFD8DC), fontSize = 17.sp)
        Text("Your phone stays silent: you won't hear them and they won't hear you. You can put it away.",
            color = Color(0xFFCFD8DC), fontSize = 17.sp)
        Big("OK, close", Purple, onOk)
    }
}

@Composable
fun Big(label: String, color: Color, onClick: () -> Unit) {
    Button(onClick = onClick, colors = ButtonDefaults.buttonColors(containerColor = color, contentColor = Color.White),
        modifier = Modifier.fillMaxWidth().height(56.dp)) { Text(label, fontSize = 18.sp, fontWeight = FontWeight.SemiBold) }
}
