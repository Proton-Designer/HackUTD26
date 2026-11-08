package com.example.voip.call

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

enum class CallOutcome {
    ANSWERED,   // talked
    MISSED,     // incoming, caller gave up before we answered
    DECLINED,   // incoming, we declined
    NO_ANSWER,  // outgoing, nobody picked up
    REJECTED,   // outgoing, they declined or were busy
    CANCELLED,  // outgoing, we hung up before they answered
    FAILED,     // network/offline
}

data class CallRecord(
    val callId: String,
    val peer: String,
    val outgoing: Boolean,
    val startedAtMs: Long,
    val durationSec: Long,
    val outcome: CallOutcome,
)

/** Recents list, persisted as a small JSON file in app storage. */
object CallHistory {
    private const val MAX = 200
    private lateinit var file: File
    private val _records = MutableStateFlow<List<CallRecord>>(emptyList())
    val records: StateFlow<List<CallRecord>> = _records.asStateFlow()

    fun init(context: Context) {
        if (::file.isInitialized) return
        file = File(context.filesDir, "call_history.json")
        _records.value = runCatching { parse(file.readText()) }.getOrDefault(emptyList())
    }

    @Synchronized
    fun add(record: CallRecord) {
        val list = (listOf(record) + _records.value).take(MAX)
        _records.value = list
        runCatching { file.writeText(serialize(list)) }
    }

    @Synchronized
    fun clear() {
        _records.value = emptyList()
        file.delete()
    }

    private fun serialize(list: List<CallRecord>) = JSONArray().apply {
        list.forEach {
            put(
                JSONObject()
                    .put("callId", it.callId).put("peer", it.peer).put("outgoing", it.outgoing)
                    .put("startedAtMs", it.startedAtMs).put("durationSec", it.durationSec)
                    .put("outcome", it.outcome.name)
            )
        }
    }.toString()

    private fun parse(text: String): List<CallRecord> {
        val arr = JSONArray(text)
        return (0 until arr.length()).map { i ->
            val o = arr.getJSONObject(i)
            CallRecord(
                callId = o.getString("callId"),
                peer = o.getString("peer"),
                outgoing = o.getBoolean("outgoing"),
                startedAtMs = o.getLong("startedAtMs"),
                durationSec = o.getLong("durationSec"),
                outcome = runCatching { CallOutcome.valueOf(o.getString("outcome")) }.getOrDefault(CallOutcome.FAILED),
            )
        }
    }
}
