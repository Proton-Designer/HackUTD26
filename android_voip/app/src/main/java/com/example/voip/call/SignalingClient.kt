package com.example.voip.call

import android.os.Handler
import android.os.Looper
import android.util.Log
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.Response
import okhttp3.WebSocket
import okhttp3.WebSocketListener
import org.json.JSONObject
import java.util.concurrent.TimeUnit

/** WebSocket connection to the laptop signaling server, with automatic reconnect. */
class SignalingClient(
    private val url: String,
    private val myId: String,
    private val listener: Listener,
) {
    interface Listener {
        fun onConnected()
        fun onDisconnected(reason: String)
        fun onMessage(msg: JSONObject)
    }

    private val http = OkHttpClient.Builder()
        .pingInterval(15, TimeUnit.SECONDS)
        .build()
    private val handler = Handler(Looper.getMainLooper())
    private var socket: WebSocket? = null
    private var closed = false
    private var retryDelayMs = 1000L

    fun connect() {
        if (closed) return
        Log.i(TAG, "connecting to $url as $myId")
        socket = http.newWebSocket(Request.Builder().url(url).build(), object : WebSocketListener() {
            override fun onOpen(webSocket: WebSocket, response: Response) {
                retryDelayMs = 1000L
                webSocket.send(JSONObject().put("type", "register").put("id", myId).toString())
                listener.onConnected()
            }

            override fun onMessage(webSocket: WebSocket, text: String) {
                runCatching { JSONObject(text) }
                    .onSuccess { listener.onMessage(it) }
                    .onFailure { Log.w(TAG, "bad message: $text") }
            }

            override fun onClosed(webSocket: WebSocket, code: Int, reason: String) = lost(webSocket, "closed: $reason")

            override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) =
                lost(webSocket, t.message ?: t.javaClass.simpleName)
        })
    }

    private fun lost(ws: WebSocket, reason: String) {
        if (ws !== socket) return
        Log.w(TAG, "connection lost: $reason")
        listener.onDisconnected(reason)
        if (!closed) {
            handler.postDelayed({ connect() }, retryDelayMs)
            retryDelayMs = (retryDelayMs * 2).coerceAtMost(15_000L)
        }
    }

    fun send(msg: JSONObject) {
        val ok = socket?.send(msg.toString()) ?: false
        if (!ok) Log.w(TAG, "send failed: ${msg.optString("type")}")
    }

    fun close() {
        closed = true
        handler.removeCallbacksAndMessages(null)
        socket?.close(1000, "bye")
        socket = null
        http.dispatcher.executorService.shutdown()
    }

    private companion object { const val TAG = "Signaling" }
}
