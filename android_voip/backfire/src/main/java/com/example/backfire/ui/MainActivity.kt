package com.example.backfire.ui

import android.Manifest
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.text.format.DateUtils
import android.text.format.Formatter
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Cloud
import androidx.compose.material.icons.filled.Memory
import androidx.compose.material.icons.filled.Phone
import androidx.compose.material.icons.filled.Shield
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Switch
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
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.core.content.ContextCompat
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.backfire.Blocked
import com.example.backfire.Engine
import com.example.backfire.Guard
import com.example.backfire.GuardService
import com.example.backfire.Hub
import com.example.backfire.ModelId
import com.example.backfire.ModelStatus
import com.example.backfire.Models
import com.example.backfire.Settings
import com.example.backfire.detect.LlamaBridge
import com.example.backfire.detect.NvidiaCloud

private enum class Tab { LIVE, ENGINE, PROTECTION }


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        if (Build.VERSION.SDK_INT >= 33 &&
            ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
        ) requestPermissions(arrayOf(Manifest.permission.POST_NOTIFICATIONS), 1)
        GuardService.start(this)
        setContent { MaterialTheme { Screen() } }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun Screen() {
    var tab by remember { mutableStateOf(Tab.LIVE) }
    val st by Guard.state.collectAsStateWithLifecycle()
    val snackbar = remember { SnackbarHostState() }
    LaunchedEffect(st.message) { st.message?.let { snackbar.showSnackbar(it); Guard.say(null) } }

    Scaffold(
        topBar = { TopAppBar(title = { Text("Backfire") }) },
        bottomBar = {
            NavigationBar {
                NavigationBarItem(tab == Tab.LIVE, { tab = Tab.LIVE }, { Icon(Icons.Filled.Phone, null) }, label = { Text("Live") })
                NavigationBarItem(tab == Tab.ENGINE, { tab = Tab.ENGINE }, { Icon(Icons.Filled.Memory, null) }, label = { Text("Engine") })
                NavigationBarItem(tab == Tab.PROTECTION, { tab = Tab.PROTECTION }, { Icon(Icons.Filled.Shield, null) }, label = { Text("Protection") })
            }
        },
        snackbarHost = { SnackbarHost(snackbar) },
    ) { pad ->
        Column(Modifier.padding(pad).fillMaxSize().verticalScroll(rememberScrollState()).padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            when (tab) {
                Tab.LIVE -> LiveTab()
                Tab.ENGINE -> EngineTab()
                Tab.PROTECTION -> ProtectionTab()
            }
        }
    }
}

@Composable
private fun Section(title: String, content: @Composable () -> Unit) {
    Card(Modifier.fillMaxWidth()) {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(title, style = MaterialTheme.typography.titleMedium)
            content()
        }
    }
}

@Composable
private fun Small(text: String, color: Color = Color.Gray) = Text(text, style = MaterialTheme.typography.bodySmall, color = color)

// ---------------------------------------------------------------- Live

@Composable
private fun LiveTab() {
    val st by Guard.state.collectAsStateWithLifecycle()
    val cfg by Settings.config.collectAsStateWithLifecycle()

    Card(Modifier.fillMaxWidth()) {
        Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
            Icon(Icons.Filled.Shield, null, tint = if (cfg.liveGuard) Teal else Color.Gray, modifier = Modifier.size(36.dp))
            Column(Modifier.weight(1f).padding(start = 12.dp)) {
                Text("Live Guard", style = MaterialTheme.typography.titleMedium)
                Small(if (cfg.liveGuard) "On. Unknown callers are checked while you talk." else "Off. Calls aren't checked.")
            }
            Switch(cfg.liveGuard, { on -> Settings.update { it.copy(liveGuard = on) } })
        }
    }

    Section("Status") {
        Small(when {
            st.boundToVoip -> "✓ Connected to Demo VoIP"
            st.voipMissing -> "Demo VoIP isn't installed (or was installed after Backfire: reinstall Backfire)."
            else -> "Connecting to Demo VoIP…"
        }, if (st.boundToVoip) Teal else Danger)
        Small((if (st.engineReady) "✓ " else "") + st.engineStatus.ifEmpty { "Choose an engine in the Engine tab." }, if (st.engineReady) Teal else Color.Gray)
        Small(if (cfg.deviceToken != null) "✓ Paired with the Backfire network" else "Not paired with the Backfire network (Protection tab)",
            if (cfg.deviceToken != null) Teal else Color.Gray)
    }

    val c = st.call
    if (c == null) {
        Section("No call right now") { Small("When someone you don't know calls, what they say appears here, transcribed on this phone.") }
    } else Section("On a call with ${c.peer}") {
        Small(listOfNotNull(
            c.decision?.let { "Network: $it" } ?: "Network: unknown",
            if (c.hubLive) "hub connected" else "hub offline",
            if (c.decoyActive) "decoy talking" else "${c.checks} checks",
        ).joinToString(" · "))
        c.note?.let { Small(it, Amber) }
        c.verdict?.let { v ->
            Text("Is this a scam? ${if (v.scam) "YES" else "no"}  (p=${"%.2f".format(v.pYes)})",
                fontWeight = FontWeight.SemiBold, color = if (v.pYes >= 0.8) Danger else if (v.pYes >= 0.5) Amber else Teal)
            Small("${v.engine} · last check ${v.latencyMs} ms")
        }
        HorizontalDivider()
        Small("Caller said (stays on this phone):")
        if (c.lines.isEmpty()) Small("…")
        c.lines.takeLast(6).forEach { Text("“$it”", style = MaterialTheme.typography.bodyMedium) }

    }
    st.handled?.let { Section("Handled for you") { Small("Backfire's decoy is talking to $it."); TextButton(onClick = Guard::dismissHandled) { Text("OK") } } }
}

// ---------------------------------------------------------------- Engine

@Composable
private fun EngineTab() {
    val cfg by Settings.config.collectAsStateWithLifecycle()
    val status by Models.status.collectAsStateWithLifecycle()
    val st by Guard.state.collectAsStateWithLifecycle()
    var testResult by remember { mutableStateOf<String?>(null) }

    Section("Speech-to-text (needed for both engines)") {
        ModelRow(ModelId.SPEECH, status[ModelId.SPEECH]!!)
        Small("Turns the caller's voice into text on this phone. Your voice is never used.")
    }

    Section("Detection engine") {
        EngineChoice(Engine.LOCAL, cfg.engine, Icons.Filled.Memory, "On this phone: Nemotron 3 Nano 4B",
            "Private: the caller's words never leave the phone. Only the risk score is sent.")
        EngineChoice(Engine.NVIDIA, cfg.engine, Icons.Filled.Cloud, "NVIDIA cloud",
            "The caller's recent words go to NVIDIA's API with your key.")
    }

    if (cfg.engine == Engine.LOCAL) Section("On-device model") {
        if (!LlamaBridge.available) Small("This build doesn't include the on-device engine. Install the build made with -Pbackfire.llama=true.", Danger)
        ModelRow(ModelId.NEMOTRON, status[ModelId.NEMOTRON]!!)
        Small("Needs ~2.5 GB of storage and about 3 GB of free memory while loaded.")
    } else NvidiaSection()

    Section("Check the engine") {
        Small(st.engineStatus)
        OutlinedButton(onClick = { testResult = "Asking \"Is this a scam?\" about a scam call and a normal call…"; Guard.test { testResult = it } }) { Text("Test detector") }
        testResult?.let { Small(it, Color.Unspecified) }
        if (cfg.engine == Engine.LOCAL && LlamaBridge.available)
            OutlinedButton(onClick = { testResult = "Measuring speed…"; Guard.bench { testResult = it } }) { Text("Speed check") }
    }

    Section("Scammer Get Scammed") {
        Small(if (st.cloudOk) "✓ Available. The decoy runs on this phone and thinks with NVIDIA cloud." else
            "Not available: the decoy needs a cloud model. ${st.cloudStatus}.", if (st.cloudOk) Teal else Danger)
        if (cfg.engine == Engine.LOCAL) NvidiaSection()
    }
    LaunchedEffect(cfg.engine, cfg.nvidiaKey, cfg.nvidiaModel) { Guard.onModelsChanged() }
}

@Composable
private fun EngineChoice(e: Engine, current: Engine, icon: androidx.compose.ui.graphics.vector.ImageVector, title: String, sub: String) {
    Row(Modifier.fillMaxWidth().selectable(selected = e == current) { Settings.update { it.copy(engine = e) } }.padding(vertical = 4.dp),
        verticalAlignment = Alignment.CenterVertically) {
        RadioButton(e == current, { Settings.update { it.copy(engine = e) } })
        Icon(icon, null, modifier = Modifier.size(22.dp))
        Column(Modifier.padding(start = 8.dp)) { Text(title); Small(sub) }
    }
}

@Composable
private fun ModelRow(id: ModelId, s: ModelStatus) {
    val ctx = LocalContext.current
    Text("${id.title} · ${id.sizeLabel}", fontWeight = FontWeight.SemiBold)
    when (s) {
        ModelStatus.Missing -> OutlinedButton(onClick = { Models.download(id) }) { Text("Download (${id.sizeLabel})") }
        is ModelStatus.Downloading -> {
            if (s.total > 0) LinearProgressIndicator(progress = { s.done.toFloat() / s.total }, modifier = Modifier.fillMaxWidth())
            else LinearProgressIndicator(Modifier.fillMaxWidth())
            Row(verticalAlignment = Alignment.CenterVertically) {
                Small("${Formatter.formatShortFileSize(ctx, s.done)} of ${if (s.total > 0) Formatter.formatShortFileSize(ctx, s.total) else "?"}", Color.Unspecified)
                Spacer(Modifier.width(8.dp))
                TextButton(onClick = { Models.cancel(id) }) { Text("Cancel") }
            }
        }
        ModelStatus.Preparing -> { LinearProgressIndicator(Modifier.fillMaxWidth()); Small("Unpacking…") }
        ModelStatus.Ready -> Row(verticalAlignment = Alignment.CenterVertically) {
            Small("✓ Downloaded", Teal); Spacer(Modifier.width(8.dp)); TextButton(onClick = { Models.delete(id) }) { Text("Delete") }
        }
        is ModelStatus.Failed -> Row(verticalAlignment = Alignment.CenterVertically) {
            Small("Failed: ${s.why}", Danger); Spacer(Modifier.width(8.dp)); TextButton(onClick = { Models.download(id) }) { Text("Retry") }
        }
    }
}

@Composable
private fun NvidiaSection() {
    val cfg by Settings.config.collectAsStateWithLifecycle()
    var key by remember(cfg.nvidiaKey) { mutableStateOf(cfg.nvidiaKey) }
    var model by remember(cfg.nvidiaModel) { mutableStateOf(cfg.nvidiaModel) }
    var models by remember { mutableStateOf<List<String>>(emptyList()) }
    var info by remember { mutableStateOf<String?>(null) }
    Section("NVIDIA cloud") {
        OutlinedTextField(key, { key = it.trim() }, label = { Text("API key (nvapi-…)") }, singleLine = true,
            visualTransformation = PasswordVisualTransformation(), modifier = Modifier.fillMaxWidth())
        OutlinedTextField(model, { model = it.trim() }, label = { Text("Model") }, singleLine = true, modifier = Modifier.fillMaxWidth())
        Row {
            OutlinedButton(onClick = { Settings.update { it.copy(nvidiaKey = key, nvidiaModel = model) }; info = "Saved"; Guard.onModelsChanged() }) { Text("Save") }
            Spacer(Modifier.width(8.dp))
            OutlinedButton(onClick = {
                info = "Loading models…"
                Thread {
                    NvidiaCloud.listModels(key)
                        .onSuccess { models = it; info = if (it.isEmpty()) "No Nemotron models for this key" else null }
                        .onFailure { info = "Couldn't list models: ${it.message}" }
                }.start()
            }, enabled = key.isNotBlank()) { Text("Load models") }
        }
        info?.let { Small(it, Color.Unspecified) }
        models.forEach { m ->
            Row(Modifier.fillMaxWidth().selectable(m == model) { model = m; Settings.update { it.copy(nvidiaKey = key, nvidiaModel = m) } },
                verticalAlignment = Alignment.CenterVertically) {
                RadioButton(m == model, { model = m; Settings.update { it.copy(nvidiaKey = key, nvidiaModel = m) } })
                Small(m, Color.Unspecified)
            }
        }
        Small("The key is stored only on this phone.")
    }
}

// ---------------------------------------------------------------- Protection

@Composable
private fun ProtectionTab() {
    val cfg by Settings.config.collectAsStateWithLifecycle()
    var hub by remember(cfg.hubUrl) { mutableStateOf(cfg.hubUrl) }
    var pin by remember { mutableStateOf("") }
    var blocked by remember { mutableStateOf<List<Blocked>?>(null) }
    var info by remember { mutableStateOf<String?>(null) }
    fun refresh() = Hub.protectionLog { blocked = it; if (it == null) info = "Can't load the protection log (hub offline or not paired)" }
    LaunchedEffect(cfg.deviceToken, cfg.hubUrl) { if (cfg.deviceToken != null) refresh() }

    Section("Backfire network") {
        Small("The network blocks known scammers before your phone rings, runs the decoy, and stops scam numbers for everyone. It only receives risk scores from this phone.")
        OutlinedTextField(hub, { hub = it.trim() }, label = { Text("Hub address, e.g. http://10.0.0.5:8000") }, singleLine = true, modifier = Modifier.fillMaxWidth())
        if (hub.trimEnd('/') != cfg.hubUrl) OutlinedButton(onClick = { Settings.update { it.copy(hubUrl = hub.trimEnd('/')) } }) { Text("Save address") }
        if (cfg.deviceToken != null) Small("✓ This phone is paired", Teal) else {
            Small("Enter the DEVICE PIN the hub printed.")
            Row(verticalAlignment = Alignment.CenterVertically) {
                OutlinedTextField(pin, { pin = it.filter(Char::isDigit).take(6) }, label = { Text("Code") }, singleLine = true,
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword), modifier = Modifier.weight(1f))
                TextButton(onClick = { Hub.pair(pin) { _, msg -> Guard.say(msg) }; pin = "" }, enabled = pin.length >= 4 && cfg.hubUrl.isNotBlank()) { Text("Pair") }
            }
        }
        info?.let { Small(it, Color.Unspecified) }
    }

    Section("Numbers we blocked") {
        Row(verticalAlignment = Alignment.CenterVertically) { Spacer(Modifier.weight(1f)); TextButton(onClick = { refresh() }) { Text("Refresh") } }
        val list = blocked.orEmpty()
        if (list.isEmpty()) Small("None yet.")
        list.forEachIndexed { i, b ->
            if (i > 0) HorizontalDivider()
            Row(Modifier.padding(vertical = 6.dp), verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text(b.number, fontWeight = FontWeight.SemiBold)
                    Small("${b.reason} · ${DateUtils.getRelativeTimeSpanString((b.ts * 1000).toLong())}")
                }
                TextButton(onClick = { Hub.undo(b) { ok -> Guard.say(if (ok) "${b.number} unblocked" else "Undo failed"); refresh() } }) { Text("Undo") }
            }
        }
    }

    VoiceSection()

    Card(Modifier.fillMaxWidth(), colors = CardDefaults.cardColors()) {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            Text("What we keep", style = MaterialTheme.typography.titleMedium)
            Text("• Your side of a call: never heard, never kept.")
            Text("• The caller's words: turned into text on this phone, used for the score, not saved.")
            Text("• Sent to the network: risk scores and alerts only.")
            Text("• Scammer numbers: kept so they can be stopped.")
            Text("• Your voice profile: 8 seconds, only on this phone, until you delete it.")
        }
    }
}

// ---------------------------------------------------------------- voice profile (consented clone, on this phone)

@Composable
private fun VoiceSection() {
    val vs by com.example.backfire.decoy.VoiceProfile.state.collectAsStateWithLifecycle()
    val cfg by Settings.config.collectAsStateWithLifecycle()
    var consent by remember { mutableStateOf(false) }
    val mic = androidx.activity.compose.rememberLauncherForActivityResult(
        androidx.activity.result.contract.ActivityResultContracts.RequestPermission()
    ) { ok -> if (ok) com.example.backfire.decoy.VoiceProfile.record(consent) else Guard.say("Microphone permission is needed to record your voice") }
    val ctx = LocalContext.current
    Section("Your voice (optional)") {
        if (vs.enrolled && !vs.recording) {
            Small("✓ Your voice is set up. If you press Scammer Get Scammed, Backfire's decoy talks to the scammer in your voice" +
                if (cfg.nvidiaKey.isBlank()) " once an NVIDIA key is set (Engine tab)." else ".", Teal)
            OutlinedButton(onClick = { com.example.backfire.decoy.VoiceProfile.delete() }) { Text("Delete my voice") }
        } else {
            Text("Backfire can talk to scammers in your voice, so they waste their time and not yours.")
            Row(Modifier.fillMaxWidth().selectable(consent) { consent = !consent }, verticalAlignment = Alignment.CenterVertically) {
                androidx.compose.material3.Checkbox(consent, { consent = it })
                Small("I agree that Backfire may make a voice profile from my recording. It is used only when I press " +
                    "Scammer Get Scammed, stays on this phone (sent to NVIDIA only to speak each sentence), and I can delete it at any time.",
                    Color.Unspecified)
            }
            if (consent) {
                Small("Press Record and read this out loud:")
                Text(com.example.backfire.decoy.VoiceProfile.PARAGRAPH, style = MaterialTheme.typography.bodyLarge)
                if (vs.recording) {
                    LinearProgressIndicator(progress = { vs.level }, modifier = Modifier.fillMaxWidth())
                    Small("Recording… %.0f s".format(vs.seconds), Color.Unspecified)
                    OutlinedButton(onClick = { com.example.backfire.decoy.VoiceProfile.stopRecording() }) { Text("Stop") }
                } else OutlinedButton(onClick = {
                    if (ContextCompat.checkSelfPermission(ctx, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED)
                        com.example.backfire.decoy.VoiceProfile.record(consent)
                    else mic.launch(Manifest.permission.RECORD_AUDIO)
                }) { Text("● Record") }
            }
        }
        vs.message?.let { Small(it, Color.Unspecified) }
    }
}
