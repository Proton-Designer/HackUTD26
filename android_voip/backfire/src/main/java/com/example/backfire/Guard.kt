package com.example.backfire

import android.content.Context
import android.util.Log
import com.example.backfire.decoy.Decoy
import com.example.backfire.decoy.DecoyIo
import com.example.backfire.decoy.Voice
import com.example.backfire.detect.Detector
import com.example.backfire.detect.LlamaBridge
import com.example.backfire.detect.LocalNemotron
import com.example.backfire.detect.NvidiaCloud
import com.example.backfire.detect.Reasons
import com.example.backfire.detect.Verdict
import com.example.voip.export.ICallAudioService
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import okhttp3.WebSocket
import org.json.JSONArray
import org.json.JSONObject
import java.util.concurrent.Executors

data class CallView(
    val callId: String,
    val peer: String,
    /** The network's routing decision (LIVE_GUARD / NORMAL), or null if the hub hasn't said / is unreachable. */
    val decision: String? = null,
    val hubLive: Boolean = false,
    val lines: List<String> = emptyList(),
    val verdict: Verdict? = null,
    val checks: Int = 0,
    val alertShown: Boolean = false,
    val chips: List<String> = emptyList(),
    /** The decoy (on this phone) is talking to the caller. */
    val decoyActive: Boolean = false,
    val note: String? = null,
)

data class GuardState(
    val boundToVoip: Boolean = false,
    val voipMissing: Boolean = false,
    val engineStatus: String = "",
    val engineReady: Boolean = false,
    /** A cloud model answered: required for Scammer Get Scammed (the decoy thinks in the cloud). */
    val cloudOk: Boolean = false,
    val cloudStatus: String = "No NVIDIA key",
    val call: CallView? = null,
    /** Peer the decoy took off Maria's hands; shown until she taps OK. */
    val handled: String? = null,
    val message: String? = null,
)

/**
 * Backfire on the phone. Detection: hears the caller (only), transcribes on the device, asks "Is this a scam?"
 * (on-device Nemotron or NVIDIA cloud; yes/no), warns Maria and tells the network only the answer.
 * Scammer Get Scammed: the decoy runs on this phone (cloud model + on-device voice) inside the same call.
 */
object Guard {
    private const val TAG = "Guard"
    private const val ALERT_AT = 0.8

    private lateinit var ctx: Context
    private val _state = MutableStateFlow(GuardState())
    val state: StateFlow<GuardState> = _state.asStateFlow()

    @Volatile var voip: ICallAudioService? = null
    private val work = Executors.newSingleThreadExecutor { Thread(it, "guard-detector") }
    private val net = Executors.newSingleThreadExecutor { Thread(it, "guard-net") }
    private var detector: Detector? = null
    private var detectorKey: String? = null
    @Volatile private var transcriber: Transcriber? = null
    private var events: WebSocket? = null
    @Volatile private var activeCall: String? = null
    @Volatile private var checkPending = false
    @Volatile private var decoy: Decoy? = null
    private val voice by lazy { Voice(ctx) }
    private var alerted = false
    private var realerted = false

    fun init(context: Context) {
        ctx = context.applicationContext
        onModelsChanged()
    }

    fun say(msg: String?) = _state.update { it.copy(message = msg) }
    fun setBound(bound: Boolean, missing: Boolean = false) = _state.update { it.copy(boundToVoip = bound, voipMissing = missing) }
    fun dismissHandled() = _state.update { it.copy(handled = null) }

    // ---------------------------------------------------------------- engines

    /** Models or settings changed: rebuild the detector and re-check the cloud, in the background. */
    fun onModelsChanged() {
        work.execute { ensureDetector() }
        checkCloud()
    }

    /** Scammer Get Scammed needs a cloud model. Verify the key/model actually answer. */
    fun checkCloud() = net.execute {
        val c = Settings.now
        if (c.nvidiaKey.isBlank()) { _state.update { it.copy(cloudOk = false, cloudStatus = "No NVIDIA key") }; return@execute }
        _state.update { it.copy(cloudStatus = "Checking NVIDIA cloud…") }
        val r = NvidiaCloud.chat(c.nvidiaKey, c.nvidiaModel, JSONArray().put(JSONObject().put("role", "user").put("content", "Say ok.")), 3, 0.0)
        _state.update { it.copy(cloudOk = r != null, cloudStatus = if (r != null) "NVIDIA cloud OK (${c.nvidiaModel})" else "NVIDIA cloud not reachable with this key/model") }
    }

    private fun engineKey(c: Config) = when (c.engine) {
        Engine.LOCAL -> "local:${Models.isReady(ModelId.NEMOTRON)}"
        Engine.NVIDIA -> "nvidia:${c.nvidiaModel}:${c.nvidiaKey.hashCode()}"
    }

    /** On the worker thread. */
    private fun ensureDetector(): Detector? {
        val c = Settings.now
        val key = engineKey(c)
        if (key == detectorKey && detector != null) return detector
        detector?.close(); detector = null; detectorKey = key
        val speechOk = Models.isReady(ModelId.SPEECH)
        when (c.engine) {
            Engine.LOCAL -> when {
                !LlamaBridge.available -> status("This build has no on-device engine. Use NVIDIA cloud, or install the build with Nemotron.", false)
                !Models.isReady(ModelId.NEMOTRON) -> status("Download Nemotron to use the on-device engine.", false)
                else -> {
                    status("Loading Nemotron 3 Nano 4B on this phone…", false)
                    val t0 = System.currentTimeMillis()
                    val d = LocalNemotron.load(Models.nemotronFile)
                    detector = d
                    if (d == null) status("Nemotron failed to load.", false)
                    else status("On-device Nemotron ready: ${d.threads} performance cores, loaded in ${(System.currentTimeMillis() - t0) / 1000} s", speechOk)
                }
            }
            Engine.NVIDIA -> if (c.nvidiaKey.isBlank()) status("Enter your NVIDIA API key.", false)
                else { detector = NvidiaCloud(c.nvidiaKey, c.nvidiaModel); status("NVIDIA cloud detection: ${c.nvidiaModel}", speechOk) }
        }
        if (!speechOk && detector != null) status(_state.value.engineStatus + " · Download the speech model to listen to calls.", false)
        return detector
    }

    private fun status(s: String, ready: Boolean) = _state.update { it.copy(engineStatus = s, engineReady = ready) }

    /** Speed check of the on-device engine across thread counts (Engine tab). */
    fun bench(done: (String) -> Unit) = work.execute {
        val d = ensureDetector() as? LocalNemotron ?: return@execute done("The on-device engine isn't loaded.")
        val r = d.bench(intArrayOf(1, 2, 3, 4, 5, 6, 8))
        done("threads · prompt tok/s · decode tok/s\n" + r.trim())
    }

    /** "Test detector": a scam and a normal call, each fed line by line like a real call. Reports per-check time. */
    fun test(done: (String) -> Unit) = work.execute {
        val d = ensureDetector() ?: return@execute done("No engine ready: ${_state.value.engineStatus}")
        val scam = listOf("Hello, this is officer Daniels with the IRS.", "There is a warrant for your arrest for unpaid taxes.",
            "To stop it today you need to buy Target gift cards and read me the numbers.", "Do not tell anyone at your bank about this call.")
        val normal = listOf("Hi, this is Jenny from Dr. Patel's dental office.", "I'm calling to confirm your cleaning on Tuesday at 10 am.",
            "If you need to reschedule just call the office. Have a great day.")
        fun run(lines: List<String>): String {
            d.reset()
            val t0 = System.currentTimeMillis()
            var v: Verdict? = null
            val times = lines.map { l -> val a = System.currentTimeMillis(); d.append(l); v = d.ask(); System.currentTimeMillis() - a }
            val total = System.currentTimeMillis() - t0
            return "${if (v?.scam == true) "YES" else if (v == null) "?" else "no"} (p=${"%.2f".format(v?.pYes ?: -1.0)}), per check ${times.joinToString("/")} ms, total $total ms"
        }
        val a = run(scam); val b = run(normal)
        d.reset()
        done("Scam call → $a\nDentist call → $b\n(${d.name})")
    }

    // ---------------------------------------------------------------- call lifecycle (from GuardService, Binder threads)

    fun onCallStarted(callId: String, peer: String, outgoing: Boolean) {
        if (outgoing || !Settings.now.liveGuard) return
        activeCall = callId
        alerted = false; realerted = false
        _state.update { it.copy(call = CallView(callId, peer)) }
        events?.cancel()
        events = Hub.events(callId, ::onHubEvent) { live -> updateCall(callId) { it.copy(hubLive = live) } }
        work.execute { ensureDetector()?.reset() }
        checkCloud()
        val model = Transcriber.loadModel(Models.speechDir)
        if (model == null) {
            updateCall(callId) { it.copy(note = "Speech model not downloaded: Live Guard can't listen.") }
            return
        }
        transcriber = Transcriber(model, onPartial = { decoy?.onCallerSpeaking() }) { text -> onUtterance(callId, text) }.also { it.start() }
    }

    fun onCallerAudio(callId: String, pcm16: ByteArray, sampleRate: Int, channels: Int) {
        if (callId != activeCall) return
        transcriber?.feed(pcm16, sampleRate, channels)
    }

    fun onCallEnded(callId: String, reason: String) {
        if (callId != activeCall) return
        activeCall = null
        transcriber?.close(); transcriber = null
        decoy?.stop(); decoy = null
        events?.close(1000, "call over"); events = null
        _state.update { it.copy(call = null) }
        Alerts.cancel(ctx)
    }

    private fun updateCall(callId: String, f: (CallView) -> CallView) = _state.update { s ->
        val c = s.call?.takeIf { it.callId == callId } ?: return@update s
        s.copy(call = f(c))
    }

    // ---------------------------------------------------------------- the network's side of this call

    private fun onHubEvent(ev: JSONObject) {
        val callId = ev.optString("call_id")
        val d = ev.optJSONObject("data") ?: JSONObject()
        when (ev.optString("type")) {
            "call.routed" -> {
                val decision = d.optString("decision")
                updateCall(callId) { it.copy(decision = decision) }
                // Trusted, verified callers: the network says don't listen. Respect it.
                if (decision == "NORMAL" && decoy == null) { transcriber?.close(); transcriber = null }
            }
            // An alert from the network (a cloud detector or an operator). Our own alerts echo back here too: show once.
            "alert.fired" -> {
                val c = _state.value.call?.takeIf { it.callId == callId } ?: return
                if (alerted || c.decoyActive) return
                alerted = true
                val arr = d.optJSONArray("why_chips")
                showAlert(c, (0 until (arr?.length() ?: 0)).map { arr!!.getString(it) })
            }
        }
    }

    // ---------------------------------------------------------------- detection: "Is this a scam?" -> yes / no

    private fun onUtterance(callId: String, text: String) {
        updateCall(callId) { it.copy(lines = (it.lines + text).takeLast(12)) }
        decoy?.let { if (it.active) { it.onCallerSaid(text); return } }
        work.execute { ensureDetector()?.append(text) }      // each utterance is evaluated once, in order
        if (checkPending) return
        checkPending = true
        work.execute { checkPending = false; check(callId) }  // utterances arriving meanwhile join the next check
    }

    /** On the worker thread. */
    private fun check(callId: String) {
        val call = _state.value.call?.takeIf { it.callId == callId } ?: return
        if (call.decision == "NORMAL" || call.decoyActive) return
        val v = ensureDetector()?.ask() ?: return
        if (activeCall != callId) return
        val (asks, reasons) = Reasons.of(call.lines.joinToString(" "))
        updateCall(callId) { it.copy(verdict = v, checks = it.checks + 1) }
        Log.i(TAG, "scam? ${if (v.scam) "yes" else "no"} p=${"%.2f".format(v.pYes)} in ${v.latencyMs} ms (${v.engine})")
        // The network gets the answer only: yes/no as a score in the contract's risk.update shape.
        Hub.report("risk.update", callId, JSONObject().put("s", v.pYes).put("asks", JSONArray(asks)).put("scam_type", if (v.scam) "scam" else "none")
            .put("stage", "opening").put("impersonates", JSONObject.NULL).put("addresses_ai_system", false)
            .put("why_chips", JSONArray(reasons)).put("engine", v.engine))
        val level = when {
            v.pYes >= ALERT_AT && !alerted -> "first"
            v.pYes >= 0.95 && alerted && !realerted -> "realert"
            else -> null
        } ?: return
        if (level == "first") alerted = true else realerted = true
        val chips = reasons.ifEmpty { listOf("Backfire thinks this is a scam") }
        Hub.report("alert.fired", callId, JSONObject().put("level", level).put("why_chips", JSONArray(chips)))
        showAlert(call, chips)
    }

    private fun showAlert(c: CallView, chips: List<String>) {
        val cs = chips.ifEmpty { listOf("Sounds like a scam") }
        updateCall(c.callId) { it.copy(alertShown = true, chips = cs, note = null) }
        Alerts.alert(ctx, c.peer, cs, sgsAvailable = _state.value.cloudOk)
    }

    // ---------------------------------------------------------------- Maria's three buttons

    fun action(action: String) {
        val c = _state.value.call ?: return
        Alerts.cancel(ctx)
        when (action) {
            "continue" -> { updateCall(c.callId) { it.copy(alertShown = false) }; Hub.userAction(c.callId, action) }
            "hang_up" -> {
                updateCall(c.callId) { it.copy(alertShown = false) }
                Hub.userAction(c.callId, action)
                runCatching { voip?.endCall(c.callId, "backfire_hangup") }
            }
            "scammer_get_scammed" -> net.execute { startDecoy(c) }
        }
    }

    /** Debug only (DebugReceiver): speak [text] into the current call via injection, no cloud involved. */
    fun debugSay(text: String) {
        val c = _state.value.call ?: return say("debugSay: no call")
        val svc = voip ?: return say("debugSay: Demo VoIP not bound")
        if (!svc.startInjection(c.callId)) return say("debugSay: injection refused")
        val (pcm, rate) = voice.synth(text) ?: return say("debugSay: TTS failed")
        val step = rate / 5 * 2
        var i = 0
        while (i < pcm.size) { svc.injectAudio(c.callId, pcm.copyOfRange(i, minOf(pcm.size, i + step)), rate); i += step }
        android.util.Log.i(TAG, "debugSay: injected ${pcm.size / 2 * 1000 / rate} ms at $rate Hz")
    }

    /** Scammer Get Scammed: this phone's side of the call becomes the decoy. Needs a working cloud model. */
    private fun startDecoy(c: CallView) {
        val cfg = Settings.now
        fun fail(why: String) { updateCall(c.callId) { it.copy(alertShown = true, note = "Scammer Get Scammed not available: $why") } }
        if (!_state.value.cloudOk) return fail("no cloud model (add an NVIDIA key in Engine).")
        val svc = voip ?: return fail("Demo VoIP isn't connected.")
        if (!runCatching { svc.startInjection(c.callId) }.getOrDefault(false)) return fail("Demo VoIP can't hand over this call.")
        val d = Decoy(c.callId, cfg.nvidiaKey, cfg.nvidiaModel, voice, object : DecoyIo {
            override fun play(pcm16: ByteArray, sampleRate: Int) {
                // Chunks of ~200 ms keep each Binder transaction small.
                val step = sampleRate / 5 * 2
                var i = 0
                while (i < pcm16.size) { runCatching { svc.injectAudio(c.callId, pcm16.copyOfRange(i, minOf(pcm16.size, i + step)), sampleRate) }; i += step }
            }
            override fun stopPlaying() { runCatching { svc.clearInjection(c.callId) } }
            override fun hangUp() { runCatching { svc.endCall(c.callId, "decoy_done") } }
            override fun event(type: String, data: JSONObject) = Hub.report(type, c.callId, data)
        })
        decoy = d
        updateCall(c.callId) { it.copy(decoyActive = true, alertShown = false, note = null) }
        _state.update { it.copy(handled = c.peer) }
        Hub.handoff(c.callId)          // the network records the handoff (dashboards, blocklist when it ends)
        d.start()
        Alerts.handled(ctx, c.peer)
    }
}
