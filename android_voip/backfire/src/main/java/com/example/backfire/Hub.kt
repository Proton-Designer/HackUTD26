package com.example.backfire

import android.util.Log
import okhttp3.Call
import okhttp3.Callback
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.Response
import okhttp3.WebSocket
import okhttp3.WebSocketListener
import org.json.JSONArray
import org.json.JSONObject
import java.io.IOException
import java.util.concurrent.TimeUnit

data class Blocked(val number: String, val reason: String, val ts: Double, val undoToken: String)

/**
 * The phone's link to the Backfire network (the hub). What crosses it:
 *  in:  this call's routing decision and handoff events
 *  out: risk scores and alerts only (never audio, never transcripts), and Maria's button presses
 */
object Hub {
    private const val TAG = "Hub"
    private val JSON = "application/json".toMediaType()
    val http: OkHttpClient = OkHttpClient.Builder()
        .connectTimeout(3, TimeUnit.SECONDS)
        .readTimeout(20, TimeUnit.SECONDS)
        .pingInterval(15, TimeUnit.SECONDS)
        .build()

    private fun base(): String? = Settings.now.hubUrl.trim().trimEnd('/').ifBlank { null }

    private fun req(path: String): Request.Builder? {
        val b = base() ?: return null
        val r = Request.Builder().url(b + path)
        Settings.now.deviceToken?.let { r.header("x-device-token", it) }
        return r
    }

    private fun post(path: String, body: JSONObject, done: (Int, JSONObject?) -> Unit = { _, _ -> }) {
        val r = req(path)?.post(body.toString().toRequestBody(JSON))?.build() ?: return done(-1, null)
        http.newCall(r).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) { Log.w(TAG, "POST $path: ${e.message}"); done(-1, null) }
            override fun onResponse(call: Call, response: Response) = response.use {
                done(it.code, runCatching { JSONObject(it.body!!.string()) }.getOrNull())
            }
        })
    }

    fun pair(pin: String, done: (Boolean, String) -> Unit) =
        post("/pair", JSONObject().put("pin", pin.trim())) { code, body ->
            val tok = body?.optString("device_token").orEmpty()
            if (code == 200 && tok.isNotEmpty()) {
                Settings.update { it.copy(deviceToken = tok) }
                done(true, "Paired with Backfire")
            } else done(false, if (code == 401) "Wrong code" else if (code == -1) "Can't reach the hub" else "Pairing failed ($code)")
        }

    /** This call's events (history first). The hub closes it when the call ends. */
    fun events(callId: String, onEvent: (JSONObject) -> Unit, onState: (Boolean) -> Unit): WebSocket? {
        val b = base() ?: return null
        val url = b.replaceFirst("http", "ws") + "/android/events/$callId" + (Settings.now.deviceToken?.let { "?d=$it" } ?: "")
        return http.newWebSocket(Request.Builder().url(url).build(), object : WebSocketListener() {
            override fun onOpen(webSocket: WebSocket, response: Response) = onState(true)
            override fun onMessage(webSocket: WebSocket, text: String) { runCatching { onEvent(JSONObject(text)) } }
            override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {
                Log.w(TAG, "events: ${t.message} (${response?.code})"); onState(false)
            }
            override fun onClosed(webSocket: WebSocket, code: Int, reason: String) = onState(false)
        })
    }

    /** Contract events this phone produces: risk.update / alert.fired (detection) and decoy.* / guardrail.tripped /
     *  artifacts.extracted (the decoy). Never audio; never Maria's words. */
    fun report(type: String, callId: String, data: JSONObject) =
        post("/android/report", JSONObject().put("type", type).put("call_id", callId).put("data", data)) { code, _ ->
            if (code != 200) Log.w(TAG, "report $type -> $code")
        }

    /** Scammer Get Scammed handled on this phone: the network records the handoff (no transfer needed). */
    fun handoff(callId: String) = post("/android/handoff", JSONObject().put("call_id", callId)) { code, _ ->
        if (code != 200) Log.w(TAG, "handoff -> $code")
    }

    fun userAction(callId: String, action: String, done: (Int) -> Unit = {}) =
        post("/user/action", JSONObject().put("call_id", callId).put("action", action)) { code, _ -> done(code) }

    fun protectionLog(done: (List<Blocked>?) -> Unit) {
        val r = req("/protection-log")?.get()?.build() ?: return done(null)
        http.newCall(r).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) = done(null)
            override fun onResponse(call: Call, response: Response) = response.use {
                if (!it.isSuccessful) return done(null)
                val arr = runCatching { JSONObject(it.body!!.string()).optJSONArray("blocked") }.getOrNull() ?: JSONArray()
                done((0 until arr.length()).map { i ->
                    val o = arr.getJSONObject(i)
                    Blocked(o.optString("number"), o.optString("reason"), o.optDouble("ts"), o.optString("undo_token"))
                })
            }
        })
    }

    fun undo(b: Blocked, done: (Boolean) -> Unit) =
        post("/protection-log/undo", JSONObject().put("undo_token", b.undoToken)) { code, _ -> done(code == 200) }
}
