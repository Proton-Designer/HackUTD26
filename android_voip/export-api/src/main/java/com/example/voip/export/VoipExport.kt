package com.example.voip.export

import android.content.Intent

/** Contract shared between the VoIP app and apps that consume its call audio. */
object VoipExport {
    const val VOIP_PACKAGE = "com.example.voip"
    const val ACTION_BIND_AUDIO = "com.example.voip.export.BIND_AUDIO"

    /** Signature-level permission: only apps signed with the same key can bind. */
    const val PERMISSION_CALL_AUDIO = "com.example.voip.permission.CALL_AUDIO"

    const val SOURCE_LOCAL = 0
    const val SOURCE_REMOTE = 1

    fun bindIntent(): Intent = Intent(ACTION_BIND_AUDIO).setPackage(VOIP_PACKAGE)
}
