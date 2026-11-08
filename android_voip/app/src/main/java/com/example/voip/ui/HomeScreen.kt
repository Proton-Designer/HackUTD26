package com.example.voip.ui

import android.text.format.DateUtils
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Call
import androidx.compose.material.icons.automirrored.filled.CallMade
import androidx.compose.material.icons.automirrored.filled.CallMissed
import androidx.compose.material.icons.automirrored.filled.CallMissedOutgoing
import androidx.compose.material.icons.automirrored.filled.CallReceived
import androidx.compose.material.icons.filled.History
import androidx.compose.material.icons.filled.MoreVert
import androidx.compose.material.icons.filled.People
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.voip.call.CallHistory
import com.example.voip.call.CallManager
import com.example.voip.call.CallOutcome
import com.example.voip.call.CallRecord
import com.example.voip.call.Connection
import com.example.voip.call.UiState

enum class Tab { CONTACTS, RECENTS }

private val OnlineGreen = Color(0xFF2E7D32)
private val MissedRed = Color(0xFFD32F2F)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(
    state: UiState,
    recents: List<CallRecord>,
    tab: Tab,
    onTab: (Tab) -> Unit,
    showFullScreenPrompt: Boolean,
    onFixFullScreen: () -> Unit,
    onGoOffline: () -> Unit,
) {
    val snackbar = remember { SnackbarHostState() }
    LaunchedEffect(state.message) {
        state.message?.let {
            snackbar.showSnackbar(it)
            CallManager.clearMessage()
        }
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text("Phone")
                        val online = state.connection == Connection.CONNECTED
                        Text(
                            if (online) "● ${state.myId}" else "○ Connecting as ${state.myId}…",
                            style = MaterialTheme.typography.bodySmall,
                            color = if (online) OnlineGreen else Color.Gray,
                        )
                    }
                },
                actions = {
                    var menu by remember { mutableStateOf(false) }
                    IconButton(onClick = { menu = true }) { Icon(Icons.Filled.MoreVert, "Menu") }
                    DropdownMenu(menu, onDismissRequest = { menu = false }) {
                        DropdownMenuItem(text = { Text("Clear call history") }, onClick = { menu = false; CallHistory.clear() })
                        DropdownMenuItem(text = { Text("Go offline") }, onClick = { menu = false; onGoOffline() })
                    }
                },
            )
        },
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    selected = tab == Tab.CONTACTS, onClick = { onTab(Tab.CONTACTS) },
                    icon = { Icon(Icons.Filled.People, null) }, label = { Text("Contacts") },
                )
                NavigationBarItem(
                    selected = tab == Tab.RECENTS, onClick = { onTab(Tab.RECENTS) },
                    icon = { Icon(Icons.Filled.History, null) }, label = { Text("Recents") },
                )
            }
        },
        snackbarHost = { SnackbarHost(snackbar) },
    ) { padding ->
        Column(Modifier.padding(padding).fillMaxSize()) {
            if (showFullScreenPrompt) {
                Card(
                    Modifier.fillMaxWidth().padding(12.dp),
                    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.tertiaryContainer),
                ) {
                    Row(Modifier.padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
                        Text("Allow incoming calls to show full screen on the lock screen.", Modifier.weight(1f))
                        TextButton(onClick = onFixFullScreen) { Text("Allow") }
                    }
                }
            }
            when (tab) {
                Tab.CONTACTS -> Contacts(state, recents)
                Tab.RECENTS -> Recents(recents)
            }
        }
    }
}

@Composable
private fun Contacts(state: UiState, recents: List<CallRecord>) {
    var name by remember { mutableStateOf("") }
    // People you've talked to before who aren't online right now.
    val offline = recents.map { it.peer }.distinct().filter { it !in state.users && it != state.myId }

    LazyColumn(Modifier.fillMaxSize()) {
        item {
            Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
                OutlinedTextField(
                    name, { name = it.trim() },
                    label = { Text("Call by name") }, singleLine = true, modifier = Modifier.weight(1f),
                )
                Spacer(Modifier.width(8.dp))
                CallButton(enabled = name.isNotEmpty()) { CallManager.call(name); name = "" }
            }
        }
        item { SectionHeader("Online now (${state.users.size})") }
        if (state.users.isEmpty()) {
            item {
                Text(
                    "Nobody else is online. Open the app on another phone.",
                    Modifier.padding(horizontal = 16.dp, vertical = 8.dp), color = Color.Gray,
                )
            }
        }
        items(state.users, key = { "on-$it" }) { user ->
            ContactRow(user, online = true, subtitle = "Available")
        }
        if (offline.isNotEmpty()) {
            item { SectionHeader("Offline") }
            items(offline, key = { "off-$it" }) { user -> ContactRow(user, online = false, subtitle = "Offline") }
        }
    }
}

@Composable
private fun ContactRow(name: String, online: Boolean, subtitle: String) {
    Row(
        Modifier.fillMaxWidth().clickable(enabled = online) { CallManager.call(name) }.padding(horizontal = 16.dp, vertical = 10.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Box {
            Avatar(name)
            if (online) Box(
                Modifier.align(Alignment.BottomEnd).size(12.dp)
                    .background(Color.White, CircleShape).padding(2.dp).background(OnlineGreen, CircleShape)
            )
        }
        Column(Modifier.weight(1f).padding(start = 16.dp)) {
            Text(name, style = MaterialTheme.typography.titleMedium, color = if (online) Color.Unspecified else Color.Gray)
            Text(subtitle, style = MaterialTheme.typography.bodySmall, color = Color.Gray)
        }
        CallButton(enabled = online) { CallManager.call(name) }
    }
}

@Composable
private fun Recents(recents: List<CallRecord>) {
    if (recents.isEmpty()) {
        Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) { Text("No recent calls", color = Color.Gray) }
        return
    }
    LazyColumn(Modifier.fillMaxSize()) {
        items(recents, key = { it.callId + it.startedAtMs }) { r ->
            val missed = r.outcome == CallOutcome.MISSED
            Row(
                Modifier.fillMaxWidth().clickable { CallManager.call(r.peer) }.padding(horizontal = 16.dp, vertical = 10.dp),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Avatar(r.peer)
                Column(Modifier.weight(1f).padding(start = 16.dp)) {
                    Text(
                        r.peer,
                        style = MaterialTheme.typography.titleMedium,
                        color = if (missed) MissedRed else Color.Unspecified,
                        fontWeight = if (missed) FontWeight.SemiBold else null,
                    )
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        val (icon, tint) = when {
                            missed -> Icons.AutoMirrored.Filled.CallMissed to MissedRed
                            r.outcome == CallOutcome.DECLINED -> Icons.AutoMirrored.Filled.CallMissed to Color.Gray
                            !r.outgoing -> Icons.AutoMirrored.Filled.CallReceived to Color(0xFF1E88E5)
                            r.outcome == CallOutcome.ANSWERED -> Icons.AutoMirrored.Filled.CallMade to OnlineGreen
                            else -> Icons.AutoMirrored.Filled.CallMissedOutgoing to Color.Gray
                        }
                        Icon(icon, null, tint = tint, modifier = Modifier.size(16.dp))
                        Spacer(Modifier.width(4.dp))
                        Text(
                            "${describe(r)} · ${whenText(r.startedAtMs)}",
                            style = MaterialTheme.typography.bodySmall, color = Color.Gray,
                        )
                    }
                }
                CallButton(enabled = true) { CallManager.call(r.peer) }
            }
            HorizontalDivider(Modifier.padding(start = 76.dp))
        }
    }
}

private fun whenText(ms: Long): CharSequence =
    if (System.currentTimeMillis() - ms < 60_000) "Just now" else DateUtils.getRelativeTimeSpanString(ms)

private fun describe(r: CallRecord): String = when (r.outcome) {
    CallOutcome.ANSWERED -> "%d:%02d".format(r.durationSec / 60, r.durationSec % 60)
    CallOutcome.MISSED -> "Missed"
    CallOutcome.DECLINED -> "Declined"
    CallOutcome.NO_ANSWER -> "No answer"
    CallOutcome.REJECTED -> "Declined by them"
    CallOutcome.CANCELLED -> "Cancelled"
    CallOutcome.FAILED -> "Failed"
}

@Composable
private fun SectionHeader(text: String) {
    Text(
        text, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary,
        modifier = Modifier.padding(start = 16.dp, top = 12.dp, bottom = 4.dp),
    )
}

@Composable
private fun CallButton(enabled: Boolean, onClick: () -> Unit) {
    IconButton(onClick = onClick, enabled = enabled) {
        Icon(Icons.Filled.Call, "Call", tint = if (enabled) OnlineGreen else Color.LightGray)
    }
}

@Composable
fun SetupScreen(initialServer: String, initialId: String, onConnect: (String, String) -> Unit) {
    var server by remember { mutableStateOf(initialServer) }
    var myId by remember { mutableStateOf(initialId) }
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Icon(Icons.Filled.Call, null, tint = OnlineGreen, modifier = Modifier.size(64.dp))
        Text("Demo VoIP", style = MaterialTheme.typography.headlineMedium)
        OutlinedTextField(myId, { myId = it.trim() }, label = { Text("Your name") }, singleLine = true, modifier = Modifier.fillMaxWidth())
        OutlinedTextField(server, { server = it }, label = { Text("Server") }, singleLine = true, modifier = Modifier.fillMaxWidth())
        androidx.compose.material3.Button(
            onClick = { onConnect(server.trim(), myId) },
            enabled = myId.isNotBlank() && server.isNotBlank(),
            modifier = Modifier.fillMaxWidth(),
        ) { Text("Go online") }
    }
}
