package com.example.voip.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.absoluteValue

private val avatarColors = listOf(
    Color(0xFF1E88E5), Color(0xFF43A047), Color(0xFFE53935), Color(0xFF8E24AA),
    Color(0xFFFB8C00), Color(0xFF00897B), Color(0xFF3949AB), Color(0xFFD81B60),
)

@Composable
fun Avatar(name: String, size: Dp = 44.dp, modifier: Modifier = Modifier) {
    val color = avatarColors[name.hashCode().absoluteValue % avatarColors.size]
    Box(modifier.size(size).background(color, CircleShape), contentAlignment = Alignment.Center) {
        Text(
            name.firstOrNull()?.uppercase() ?: "?",
            color = Color.White,
            fontSize = (size.value * 0.42f).sp,
        )
    }
}
