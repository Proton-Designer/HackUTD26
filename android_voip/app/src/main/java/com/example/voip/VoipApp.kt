package com.example.voip

import android.app.Application
import com.example.voip.call.CallManager
import com.example.voip.call.Notifications

class VoipApp : Application() {
    override fun onCreate() {
        super.onCreate()
        Notifications.createChannels(this)
        CallManager.init(this)
    }
}
