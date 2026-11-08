package com.example.backfire.detect

import android.util.Log
import com.example.backfire.Hub
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONArray
import org.json.JSONObject
import java.util.concurrent.TimeUnit

/**
 * NVIDIA's hosted Nemotron (OpenAI-compatible, integrate.api.nvidia.com), called from the phone with the user's key.
 * Used for detection when chosen, and always for the decoy's replies.
 */
class NvidiaCloud(private val apiKey: String, private val model: String) : Detector {
    override val name = "NVIDIA cloud ($model)"
    private val lines = ArrayDeque<String>()

    override fun reset() = lines.clear()
    override fun append(utterance: String) { lines.addLast(Prompt.clean(utterance)); while (lines.size > 12) lines.removeFirst() }

    override fun ask(): Verdict? {
        val user = "What the caller has said so far:" + lines.joinToString("") { "\n- $it" } + "\n\n" + Prompt.QUESTION
        val t0 = System.currentTimeMillis()
        val out = chat(apiKey, model, JSONArray()
            .put(JSONObject().put("role", "system").put("content", Prompt.SYSTEM))
            .put(JSONObject().put("role", "user").put("content", user)), maxTokens = 3, temperature = 0.0) ?: return null
        val a = out.trim().lowercase()
        val scam = when {
            a.startsWith("yes") -> true
            a.startsWith("no") -> false
            else -> return null
        }
        return Verdict(scam, if (scam) 0.9 else 0.1, System.currentTimeMillis() - t0, "cloud")
    }

    companion object {
        private const val TAG = "NvidiaCloud"
        const val BASE = "https://integrate.api.nvidia.com/v1"
        private val http by lazy { Hub.http.newBuilder().readTimeout(8, TimeUnit.SECONDS).build() }

        /** One chat completion; thinking off (contracts/models.md). Blocking. Null on any failure. */
        fun chat(apiKey: String, model: String, messages: JSONArray, maxTokens: Int, temperature: Double): String? {
            val body = JSONObject().put("model", model).put("messages", messages)
                .put("max_tokens", maxTokens).put("temperature", temperature)
                .put("chat_template_kwargs", JSONObject().put("enable_thinking", false))
            val req = Request.Builder().url("$BASE/chat/completions").header("Authorization", "Bearer $apiKey")
                .post(body.toString().toRequestBody("application/json".toMediaType())).build()
            return runCatching {
                http.newCall(req).execute().use { r ->
                    val txt = r.body!!.string()
                    if (!r.isSuccessful) { Log.w(TAG, "HTTP ${r.code}: ${txt.take(200)}"); return null }
                    JSONObject(txt).getJSONArray("choices").getJSONObject(0).getJSONObject("message")
                        .optString("content").substringAfterLast("</think>").trim()
                }
            }.onFailure { Log.w(TAG, "request failed: ${it.message}") }.getOrNull()
        }

        /** Nemotron model ids this key can use (for the picker, and as the availability check). Blocking. */
        fun listModels(apiKey: String): Result<List<String>> = runCatching {
            val req = Request.Builder().url("$BASE/models").header("Authorization", "Bearer $apiKey").build()
            http.newCall(req).execute().use { r ->
                check(r.isSuccessful) { "HTTP ${r.code}" }
                val arr = JSONObject(r.body!!.string()).getJSONArray("data")
                (0 until arr.length()).map { arr.getJSONObject(it).getString("id") }.filter { "nemotron" in it.lowercase() }.sorted()
            }
        }
    }
}
