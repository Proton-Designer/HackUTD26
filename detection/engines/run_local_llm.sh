#!/usr/bin/env bash
# Start the local detector model (Nemotron 3 Nano 4B Q4_K_M) on the GPU for engine=local.
# WSL2 + NVIDIA driver 546: Ollama/llama.cpp CUDA-12.8 Linux builds fail ("kernel image invalid"), so we run the
# Windows llama.cpp CUDA-12.4 build through WSL interop. One-time setup is documented in detection/README.md.
# Then: export LOCAL_LLM_URL=http://$(ip route | awk '/default/{print $3}'):8101
set -euo pipefail
DIR=${LLAMA_WIN_DIR:-/mnt/c/backfire-llama}
GW=$(ip route | awk '/default/{print $3}')
cd "$DIR"
exec ./llama-server.exe -m NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf -ngl 99 -c 2048 -np 1 --port 8101 --host "$GW" --reasoning off
