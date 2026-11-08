package com.example.voip.export;

/**
 * Implemented by apps that want to receive call audio.
 * All calls are oneway: the VoIP app never blocks on a slow listener.
 */
oneway interface ICallAudioListener {
    /** A call has connected and audio is about to flow. */
    void onCallStarted(String callId, String peerId, boolean outgoing);

    /**
     * One chunk of 16-bit little-endian PCM (about 10 ms).
     * source: VoipExport.SOURCE_LOCAL (this phone's mic) or VoipExport.SOURCE_REMOTE (the other person).
     */
    void onAudioFrame(String callId, int source, in byte[] pcm16, int sampleRate, int channels, long timestampMs);

    /** The call ended. reason: "hangup", "remote_hangup", "rejected", "failed", "offline". */
    void onCallEnded(String callId, String reason);
}
