package com.example.backfire

import android.app.DownloadManager
import android.content.Context
import android.net.Uri
import android.os.Handler
import android.os.Looper
import android.util.Log
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import java.io.File
import java.util.concurrent.Executors
import java.util.zip.ZipInputStream

sealed interface ModelStatus {
    data object Missing : ModelStatus
    data class Downloading(val done: Long, val total: Long) : ModelStatus
    data object Preparing : ModelStatus
    data object Ready : ModelStatus
    data class Failed(val why: String) : ModelStatus
}

enum class ModelId(val title: String, val sizeLabel: String, val url: String) {
    SPEECH(
        "Speech-to-text (Vosk, English)", "40 MB",
        "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip",
    ),
    NEMOTRON(
        "Nemotron 3 Nano 4B (4-bit)", "2.5 GB",
        "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF/resolve/main/NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf",
    ),
}

/**
 * The two on-device models, each behind a Download button. Android's DownloadManager does the transfer, so a
 * 2.5 GB download survives the app going to the background. Files live in the app's external files dir
 * (also where `adb push` can drop them: /sdcard/Android/data/com.example.backfire/files/models/).
 */
object Models {
    private const val TAG = "Models"
    private lateinit var ctx: Context
    private lateinit var dm: DownloadManager
    private val io = Executors.newSingleThreadExecutor()
    private val main = Handler(Looper.getMainLooper())
    private val ids = mutableMapOf<ModelId, Long>()

    private val _status = MutableStateFlow(ModelId.entries.associateWith<ModelId, ModelStatus> { ModelStatus.Missing })
    val status: StateFlow<Map<ModelId, ModelStatus>> = _status.asStateFlow()

    val dir: File get() = File(ctx.getExternalFilesDir(null), "models").apply { mkdirs() }
    val nemotronFile: File get() = File(dir, "nemotron-3-nano-4b-q4_k_m.gguf")
    val speechDir: File get() = File(dir, "vosk-model-small-en-us-0.15")
    private fun downloadFile(id: ModelId) = if (id == ModelId.NEMOTRON) nemotronFile else File(dir, "vosk.zip")

    fun init(context: Context) {
        ctx = context.applicationContext
        dm = ctx.getSystemService(DownloadManager::class.java)
        val p = ctx.getSharedPreferences("models", Context.MODE_PRIVATE)
        refresh()
        // Resume watching downloads started before the app was restarted.
        ModelId.entries.forEach { id ->
            val dl = p.getLong(id.name, -1)
            if (dl >= 0 && !isReady(id)) { ids[id] = dl; poll(id) }
        }
    }

    fun isReady(id: ModelId) = when (id) {
        ModelId.SPEECH -> File(speechDir, "conf").isDirectory || File(speechDir, "am").isDirectory
        ModelId.NEMOTRON -> nemotronFile.length() > 1_000_000_000L
    }

    private fun refresh() = ModelId.entries.forEach { id -> if (isReady(id)) set(id, ModelStatus.Ready) }
    private fun set(id: ModelId, s: ModelStatus) = _status.update { it + (id to s) }

    fun download(id: ModelId) {
        if (isReady(id) || _status.value[id] is ModelStatus.Downloading) return
        downloadFile(id).delete()
        val req = DownloadManager.Request(Uri.parse(id.url))
            .setTitle("Backfire: ${id.title}")
            .setDescription(id.sizeLabel)
            .setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE)
            .setDestinationUri(Uri.fromFile(downloadFile(id)))
        val dl = dm.enqueue(req)
        ids[id] = dl
        ctx.getSharedPreferences("models", Context.MODE_PRIVATE).edit().putLong(id.name, dl).apply()
        set(id, ModelStatus.Downloading(0, -1))
        poll(id)
    }

    fun cancel(id: ModelId) {
        ids.remove(id)?.let { dm.remove(it) }
        set(id, ModelStatus.Missing)
    }

    fun delete(id: ModelId) {
        cancel(id)
        io.execute {
            if (id == ModelId.NEMOTRON) nemotronFile.delete() else speechDir.deleteRecursively()
            set(id, ModelStatus.Missing)
            Guard.onModelsChanged()
        }
    }

    private fun poll(id: ModelId) {
        val dl = ids[id] ?: return
        val c = dm.query(DownloadManager.Query().setFilterById(dl))
        var again = true
        c.use {
            if (!it.moveToFirst()) { set(id, ModelStatus.Failed("download disappeared")); return }
            val st = it.getInt(it.getColumnIndexOrThrow(DownloadManager.COLUMN_STATUS))
            val done = it.getLong(it.getColumnIndexOrThrow(DownloadManager.COLUMN_BYTES_DOWNLOADED_SO_FAR))
            val total = it.getLong(it.getColumnIndexOrThrow(DownloadManager.COLUMN_TOTAL_SIZE_BYTES))
            when (st) {
                DownloadManager.STATUS_SUCCESSFUL -> { again = false; finished(id) }
                DownloadManager.STATUS_FAILED -> {
                    again = false
                    set(id, ModelStatus.Failed("error ${it.getInt(it.getColumnIndexOrThrow(DownloadManager.COLUMN_REASON))}"))
                }
                else -> set(id, ModelStatus.Downloading(done, total))
            }
        }
        if (again) main.postDelayed({ poll(id) }, 700)
    }

    private fun finished(id: ModelId) {
        ids.remove(id)
        ctx.getSharedPreferences("models", Context.MODE_PRIVATE).edit().remove(id.name).apply()
        if (id == ModelId.NEMOTRON) {
            set(id, if (isReady(id)) ModelStatus.Ready else ModelStatus.Failed("file too small"))
            Guard.onModelsChanged()
            return
        }
        set(id, ModelStatus.Preparing)
        io.execute {
            val zip = downloadFile(id)
            runCatching { unzip(zip, dir) }
                .onSuccess { zip.delete(); set(id, if (isReady(id)) ModelStatus.Ready else ModelStatus.Failed("unexpected zip layout")) }
                .onFailure { Log.e(TAG, "unzip failed", it); set(id, ModelStatus.Failed("unzip failed")) }
            Guard.onModelsChanged()
        }
    }

    private fun unzip(zip: File, into: File) {
        val root = into.canonicalPath + File.separator
        ZipInputStream(zip.inputStream().buffered()).use { z ->
            while (true) {
                val e = z.nextEntry ?: break
                val out = File(into, e.name)
                require(out.canonicalPath.startsWith(root)) { "bad zip entry ${e.name}" }
                if (e.isDirectory) out.mkdirs() else { out.parentFile?.mkdirs(); out.outputStream().use { z.copyTo(it) } }
            }
        }
    }
}
