package com.example.voip.consumer

import java.io.File
import java.io.RandomAccessFile

/** Streams 16-bit PCM to a .wav file, patching the header sizes on close. */
class WavWriter(val file: File, private val sampleRate: Int, private val channels: Int) {
    private val raf = RandomAccessFile(file, "rw").apply { setLength(0) }
    private var dataBytes = 0L

    init { writeHeader() }

    fun write(pcm: ByteArray) {
        raf.write(pcm)
        dataBytes += pcm.size
    }

    fun close() {
        writeHeader()
        raf.close()
    }

    private fun writeHeader() {
        val byteRate = sampleRate * channels * 2
        raf.seek(0)
        raf.writeBytes("RIFF"); raf.writeIntLE((36 + dataBytes).toInt())
        raf.writeBytes("WAVE")
        raf.writeBytes("fmt "); raf.writeIntLE(16)
        raf.writeShortLE(1) // PCM
        raf.writeShortLE(channels)
        raf.writeIntLE(sampleRate)
        raf.writeIntLE(byteRate)
        raf.writeShortLE(channels * 2)
        raf.writeShortLE(16)
        raf.writeBytes("data"); raf.writeIntLE(dataBytes.toInt())
        raf.seek(raf.length())
    }

    private fun RandomAccessFile.writeIntLE(v: Int) =
        write(byteArrayOf(v.toByte(), (v shr 8).toByte(), (v shr 16).toByte(), (v shr 24).toByte()))

    private fun RandomAccessFile.writeShortLE(v: Int) =
        write(byteArrayOf(v.toByte(), (v shr 8).toByte()))
}
