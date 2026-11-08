package com.example.voip.export;

import com.example.voip.export.ICallAudioListener;

interface ICallAudioService {
    void registerListener(ICallAudioListener listener);
    void unregisterListener(ICallAudioListener listener);
    /** Current call id, or null when idle. */
    String getActiveCallId();

    /**
     * Backfire decoy: from now on the other party hears injected audio instead of this phone's microphone.
     * Returns false if callId isn't the active, connected call.
     */
    boolean startInjection(String callId);
    /** Queue 16-bit mono PCM (any sample rate) to play into the call. */
    oneway void injectAudio(String callId, in byte[] pcm16, int sampleRate);
    /** Drop queued audio (barge-in: the other party started talking). */
    oneway void clearInjection(String callId);
    /** Back to the microphone. */
    oneway void stopInjection(String callId);
    /** Hang up the call. reason "decoy_done" tells the carrier the decoy ended it. */
    oneway void endCall(String callId, String reason);
}
