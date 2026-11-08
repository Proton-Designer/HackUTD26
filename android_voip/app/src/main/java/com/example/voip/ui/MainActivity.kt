package com.example.voip.ui

import android.Manifest
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.SideEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.core.content.ContextCompat
import androidx.core.view.WindowCompat
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.voip.call.CallHistory
import com.example.voip.call.CallManager
import com.example.voip.call.CallService
import com.example.voip.call.CallState
import com.example.voip.call.Connection
import com.example.voip.call.Notifications

class MainActivity : ComponentActivity() {

    companion object {
        const val ACTION_ANSWER = "com.example.voip.ANSWER"
        const val ACTION_SHOW_RECENTS = "com.example.voip.SHOW_RECENTS"
        /** Your laptop's address on the Wi-Fi network (editable on the setup screen). */
        private const val DEFAULT_SERVER = "ws://10.162.176.86:8090"
    }

    private var tab by mutableStateOf(Tab.CONTACTS)
    private var fullScreenAllowed by mutableStateOf(true)
    private var pendingConnect: (() -> Unit)? = null

    private val permissionLauncher =
        registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { result ->
            if (result[Manifest.permission.RECORD_AUDIO] == true) pendingConnect?.invoke()
            else Toast.makeText(this, "Microphone permission is required to make calls", Toast.LENGTH_LONG).show()
            pendingConnect = null
        }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        handleIntent(intent)

        val prefs = getSharedPreferences("voip", Context.MODE_PRIVATE)
        setContent {
            MaterialTheme {
                Surface(Modifier.fillMaxSize()) {
                    val state by CallManager.state.collectAsStateWithLifecycle()
                    val recents by CallHistory.records.collectAsStateWithLifecycle()
                    // Light status-bar icons on the dark call screen, dark icons elsewhere.
                    val inCall = state.call != CallState.Idle
                    SideEffect {
                        WindowCompat.getInsetsController(window, window.decorView).isAppearanceLightStatusBars = !inCall
                    }
                    when {
                        state.call != CallState.Idle -> CallScreen(state)
                        state.connection == Connection.DISCONNECTED -> SetupScreen(
                            initialServer = prefs.getString("server", DEFAULT_SERVER)!!,
                            initialId = prefs.getString("id", Build.MODEL.replace(" ", "-").lowercase())!!,
                            onConnect = { server, id ->
                                prefs.edit().putString("server", server).putString("id", id).apply()
                                withPermissions { CallService.start(this, server, id) }
                            },
                        )
                        else -> HomeScreen(
                            state = state,
                            recents = recents,
                            tab = tab,
                            onTab = { tab = it },
                            showFullScreenPrompt = !fullScreenAllowed,
                            onFixFullScreen = ::openFullScreenSettings,
                            onGoOffline = { CallService.stop(this) },
                        )
                    }
                }
            }
        }
    }

    override fun onResume() {
        super.onResume()
        fullScreenAllowed = Notifications.canUseFullScreen(this)
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        handleIntent(intent)
    }

    private fun handleIntent(intent: Intent?) {
        when (intent?.action) {
            ACTION_ANSWER -> CallManager.accept()
            ACTION_SHOW_RECENTS -> tab = Tab.RECENTS
            else -> return
        }
        intent.action = Intent.ACTION_MAIN // don't repeat on rotation
    }

    private fun openFullScreenSettings() {
        if (Build.VERSION.SDK_INT >= 34) {
            startActivity(Intent(Settings.ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT, Uri.parse("package:$packageName")))
        }
    }

    private fun withPermissions(action: () -> Unit) {
        val needed = buildList {
            add(Manifest.permission.RECORD_AUDIO)
            if (Build.VERSION.SDK_INT >= 33) add(Manifest.permission.POST_NOTIFICATIONS)
            if (Build.VERSION.SDK_INT >= 31) add(Manifest.permission.BLUETOOTH_CONNECT)
        }.filter { ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED }

        if (needed.isEmpty()) action()
        else {
            pendingConnect = action
            permissionLauncher.launch(needed.toTypedArray())
        }
    }
}
