plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

// On-device Nemotron needs llama.cpp compiled in: ./gradlew :backfire:installDebug -Pbackfire.llama=true
// (after tools/fetch_llama.sh). Without it the app still works with the NVIDIA cloud engine.
val withLlama = (findProperty("backfire.llama") as String?)?.toBoolean() ?: false

android {
    namespace = "com.example.backfire"
    compileSdk = 36
    if (withLlama) ndkVersion = "28.2.13676358"

    defaultConfig {
        applicationId = "com.example.backfire"
        minSdk = 27
        targetSdk = 36
        versionCode = 1
        versionName = "0.1"
        buildConfigField("boolean", "HAS_LLAMA", withLlama.toString())
        ndk { abiFilters += listOf("arm64-v8a") }
        if (withLlama) externalNativeBuild { cmake { arguments += listOf("-DCMAKE_BUILD_TYPE=Release") } }
    }
    if (withLlama) externalNativeBuild { cmake { path = file("src/main/cpp/CMakeLists.txt"); version = "3.31.6" } }
    buildTypes {
        // Debug builds of llama.cpp are ~10x slower; always compile the native side optimized.
        getByName("debug") { if (withLlama) externalNativeBuild { cmake { arguments += "-DCMAKE_BUILD_TYPE=Release" } } }
    }
    buildFeatures { compose = true; buildConfig = true }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

kotlin {
    compilerOptions { jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17) }
}

dependencies {
    implementation(project(":export-api"))
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    // Offline speech-to-text (model downloaded in the app).
    implementation("com.alphacephei:vosk-android:0.3.47@aar")
    implementation("net.java.dev.jna:jna:5.13.0@aar")
    // Maria's voice clone: NVIDIA Magpie TTS Zero-shot is gRPC-only (grpc.nvcf.nvidia.com). Messages are hand-encoded
    // (MagpieClone.kt), so no protobuf code generation is needed.
    implementation("io.grpc:grpc-okhttp:1.68.1")
    implementation("io.grpc:grpc-stub:1.68.1")

    implementation("androidx.core:core-ktx:1.16.0")
    implementation("androidx.activity:activity-compose:1.10.1")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.9.1")
    implementation(platform("androidx.compose:compose-bom:2025.06.01"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.material:material-icons-extended")

    testImplementation("junit:junit:4.13.2")
    testImplementation("org.json:json:20240303")   // real org.json on the JVM (android.jar's is a stub)
}
