package com.example.backfire

import android.content.Context
import android.content.SharedPreferences
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

enum class Engine { LOCAL, NVIDIA }

data class Config(
    val liveGuard: Boolean = true,
    val engine: Engine = Engine.LOCAL,
    val hubUrl: String = "",
    val deviceToken: String? = null,
    val nvidiaKey: String = "",
    val nvidiaModel: String = Settings.DEFAULT_NVIDIA_MODEL,
)

/** Everything the user sets in the Backfire app. Stored only on this phone. */
object Settings {
    const val DEFAULT_NVIDIA_MODEL = "nvidia/nemotron-3.5-lightning-30b-a3b"  // contracts/models.md (P2 primary)
    private lateinit var prefs: SharedPreferences
    private val _config = MutableStateFlow(Config())
    val config: StateFlow<Config> = _config.asStateFlow()
    val now: Config get() = _config.value

    fun init(context: Context) {
        prefs = context.getSharedPreferences("backfire", Context.MODE_PRIVATE)
        _config.value = Config(
            liveGuard = prefs.getBoolean("liveGuard", true),
            engine = runCatching { Engine.valueOf(prefs.getString("engine", "LOCAL")!!) }.getOrDefault(Engine.LOCAL),
            hubUrl = prefs.getString("hub", "")!!,
            deviceToken = prefs.getString("token", null),
            nvidiaKey = prefs.getString("nvidiaKey", "")!!,
            nvidiaModel = prefs.getString("nvidiaModel", DEFAULT_NVIDIA_MODEL)!!,
        )
    }

    fun update(f: (Config) -> Config) {
        val old = _config.value
        val c = f(old).let { if (it.hubUrl != old.hubUrl) it.copy(deviceToken = null) else it }  // new hub: pair again
        _config.value = c
        prefs.edit()
            .putBoolean("liveGuard", c.liveGuard)
            .putString("engine", c.engine.name)
            .putString("hub", c.hubUrl)
            .putString("token", c.deviceToken)
            .putString("nvidiaKey", c.nvidiaKey)
            .putString("nvidiaModel", c.nvidiaModel)
            .apply()
    }
}
