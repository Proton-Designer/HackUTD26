package com.example.backfire

import android.app.Application

class BackfireApp : Application() {
    override fun onCreate() {
        super.onCreate()
        Settings.init(this)
        Alerts.channels(this)
        Models.init(this)
        Guard.init(this)
    }
}
