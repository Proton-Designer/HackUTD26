package com.example.backfire.decoy

import android.util.Log
import io.grpc.CallOptions
import io.grpc.ManagedChannel
import io.grpc.Metadata
import io.grpc.MethodDescriptor
import io.grpc.okhttp.OkHttpChannelBuilder
import io.grpc.stub.ClientCalls
import io.grpc.stub.MetadataUtils
import java.io.ByteArrayOutputStream
import java.io.InputStream
import java.util.concurrent.TimeUnit

/**
 * NVIDIA Magpie TTS Zero-shot, called straight from the phone (no laptop): speaks text in the voice of a 3-10 s prompt.
 * gRPC service nvidia.riva.tts.RivaSpeechSynthesis/Synthesize on grpc.nvcf.nvidia.com (NVCF function id).
 * Request/response are hand-encoded protobuf (field numbers from NVIDIA's riva_tts.proto):
 *   SynthesizeSpeechRequest { 1 text, 2 language_code, 3 encoding (LINEAR_PCM=1), 4 sample_rate_hz, 6 zero_shot_data }
 *   ZeroShotData { 1 audio_prompt (a whole WAV file, like NVIDIA's client sends), 3 encoding (UNSPECIFIED=0), 4 quality }
 *   SynthesizeSpeechResponse { 1 audio (PCM16 mono) }
 */
class MagpieClone(private val apiKey: String, private val functionId: String = ZEROSHOT_FN) {
    private val channel: ManagedChannel = OkHttpChannelBuilder.forAddress("grpc.nvcf.nvidia.com", 443)
        .useTransportSecurity()
        .build()

    /** Blocking. Returns PCM16 mono at [RATE] Hz, or null on any failure (caller falls back to the on-device voice). */
    fun synth(text: String, promptWav: ByteArray, quality: Int = 20): ByteArray? {
        val zeroShot = Proto().bytes(1, promptWav).varint(3, 0).varint(4, quality.toLong()).toByteArray()
        val req = Proto().string(1, text).string(2, "en-US").varint(3, 1).varint(4, RATE.toLong()).bytes(6, zeroShot).toByteArray()
        val md = Metadata().apply {
            put(Metadata.Key.of("function-id", Metadata.ASCII_STRING_MARSHALLER), functionId)
            put(Metadata.Key.of("authorization", Metadata.ASCII_STRING_MARSHALLER), "Bearer $apiKey")
        }
        return runCatching {
            val ch = io.grpc.ClientInterceptors.intercept(channel, MetadataUtils.newAttachHeadersInterceptor(md))
            val resp = ClientCalls.blockingUnaryCall(ch, SYNTHESIZE, CallOptions.DEFAULT.withDeadlineAfter(12, TimeUnit.SECONDS), req)
            Log.i(TAG, "response ${resp.size} bytes")
            Proto.field(resp, 1)
        }.onFailure { Log.w(TAG, "Magpie failed: ${it.message}") }.getOrNull()
    }

    fun close() { channel.shutdownNow() }

    companion object {
        private const val TAG = "MagpieClone"
        const val RATE = 22050
        const val ZEROSHOT_FN = "55cf67bf-600f-4b04-8eac-12ed39537a08"   // ai-magpie-tts-zeroshot (NVCF)

        private object Raw : MethodDescriptor.Marshaller<ByteArray> {
            override fun stream(value: ByteArray): InputStream = value.inputStream()
            override fun parse(stream: InputStream): ByteArray = stream.readBytes()
        }

        private val SYNTHESIZE: MethodDescriptor<ByteArray, ByteArray> = MethodDescriptor.newBuilder<ByteArray, ByteArray>()
            .setType(MethodDescriptor.MethodType.UNARY)
            .setFullMethodName("nvidia.riva.tts.RivaSpeechSynthesis/Synthesize")
            .setRequestMarshaller(Raw).setResponseMarshaller(Raw)
            .build()
    }
}

/** Minimal protobuf writer/reader: just varints and length-delimited fields. */
class Proto {
    private val out = ByteArrayOutputStream()
    private fun raw(v: Long) { var x = v; while (x and 0x7F.inv().toLong() != 0L) { out.write(((x and 0x7F) or 0x80).toInt()); x = x ushr 7 }; out.write(x.toInt()) }
    fun varint(field: Int, v: Long) = apply { raw((field shl 3).toLong()); raw(v) }
    fun bytes(field: Int, b: ByteArray) = apply { raw(((field shl 3) or 2).toLong()); raw(b.size.toLong()); out.write(b) }
    fun string(field: Int, s: String) = bytes(field, s.toByteArray())
    fun toByteArray(): ByteArray = out.toByteArray()

    companion object {
        /** First length-delimited value of [field] in a message, or null. */
        fun field(msg: ByteArray, field: Int): ByteArray? {
            var i = 0
            fun rd(): Long { var r = 0L; var s = 0; while (true) { val b = msg[i++].toInt() and 0xFF; r = r or ((b and 0x7F).toLong() shl s); if (b < 0x80) return r; s += 7 } }
            while (i < msg.size) {
                val tag = rd(); val f = (tag ushr 3).toInt()
                when ((tag and 7).toInt()) {
                    0 -> rd()
                    1 -> i += 8
                    2 -> { val n = rd().toInt(); if (f == field) return msg.copyOfRange(i, i + n); i += n }
                    5 -> i += 4
                    else -> return null
                }
            }
            return null
        }
    }
}
