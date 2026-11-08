#!/usr/bin/env bash
# Fetch llama.cpp (pinned) for Backfire's on-device Nemotron engine, then build with:
#   cd android_voip && ./gradlew :backfire:installDebug -Pbackfire.llama=true
# Needs the Android NDK 28.2.13676358 and CMake 3.31.6 (Android Studio SDK Manager, or sdkmanager).
set -euo pipefail
cd "$(dirname "$0")/.."
PIN=a2b301831d05b07860de508d229d430207127802
if [ ! -d third_party/llama.cpp/.git ]; then
  git clone --filter=blob:none https://github.com/ggml-org/llama.cpp.git third_party/llama.cpp
fi
git -C third_party/llama.cpp fetch --depth 1 origin "$PIN" 2>/dev/null || true
git -C third_party/llama.cpp checkout -q "$PIN"
echo "llama.cpp at $PIN"
