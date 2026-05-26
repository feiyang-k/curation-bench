#!/usr/bin/env bash
# Launch the OpenHands CLI sandbox container (datacuration-bench-openhands)
# wired to Together AI as the inference backend. Replaces the previous
# host-side vLLM launch path (docker/start_qwen3coder_vllm.sh) — no local
# GPU is needed for the agent backbone with this configuration.
#
# Mirrors the OpenHands host-install setup but inside the benchmark's
# containerized agent shell, so it slots into the same DooD pipeline as
# claude.Dockerfile / codex.Dockerfile.
#
# Tunables (override via env):
#   IMAGE         (default datacuration-bench-openhands:latest)
#   MODEL         (default Qwen/Qwen3-Coder-480B-A35B-Instruct)
#   WORKSPACE     (default /tmp/oh-smoke) host dir mounted as /workspace
#   TASK          (default sanity check) headless task string
#   NATIVE_TOOLS  (default true) set to "false" for prompted tool calls
#                 (needed by e.g. deepseek-ai/DeepSeek-V4-Pro)
#
# Required:
#   TOGETHER_API_KEY in the host shell.
set -euo pipefail

if [ -z "${TOGETHER_API_KEY:-}" ]; then
  echo "Error: TOGETHER_API_KEY is not set in the host shell." >&2
  echo "Run: export TOGETHER_API_KEY=your_key_here" >&2
  exit 1
fi

IMAGE="${IMAGE:-datacuration-bench-openhands:latest}"
# Default to Qwen3.5-397B-A17B: serverless on Together AI. Qwen3-Coder-480B
# and many of the other "strong" Together models are NOT serverless and fail
# with a "create a dedicated endpoint" error unless you provision one in the
# Together dashboard.
MODEL="${MODEL:-Qwen/Qwen3.5-397B-A17B}"
WORKSPACE="${WORKSPACE:-/tmp/oh-smoke}"
TASK="${TASK:-Create a folder named test_folder in /workspace and list its contents.}"
NATIVE_TOOLS="${NATIVE_TOOLS:-true}"

mkdir -p "$WORKSPACE"
GID=$(stat -c '%g' /var/run/docker.sock)

echo "→ image:        $IMAGE"
echo "→ model:        together_ai/$MODEL"
echo "→ workspace:    $WORKSPACE -> /workspace"
echo "→ native tools: $NATIVE_TOOLS"
echo ""

exec docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --group-add "$GID" \
  -v "$WORKSPACE:/workspace:rw" \
  -e RUNTIME=docker \
  -e SANDBOX_USER_ID="$(id -u)" \
  -e AGENT_SERVER_IMAGE_REPOSITORY=ghcr.io/openhands/agent-server \
  -e AGENT_SERVER_IMAGE_TAG=latest-python \
  -e SANDBOX_VOLUMES="$WORKSPACE:/workspace:rw" \
  -e LLM_API_KEY="$TOGETHER_API_KEY" \
  -e LLM_MODEL="together_ai/${MODEL}" \
  -e LLM_BASE_URL="https://api.together.xyz/v1" \
  -e LLM_NATIVE_TOOL_CALLING="$NATIVE_TOOLS" \
  "$IMAGE" \
  -lc "openhands --headless --override-with-envs -t \"$TASK\""
