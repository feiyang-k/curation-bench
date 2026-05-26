# OpenHands CLI sandbox for datacuration benchmark.
#
# Inference backend: Together AI (cloud, LiteLLM `together_ai/` prefix).
# Earlier revisions targeted a host-side vLLM at host.docker.internal:8000;
# we switched to Together AI to remove the local-GPU dependency for the agent
# backbone (training/eval still uses the host GPUs).
#
# Runtime model: Docker-out-of-Docker (DooD), per the OpenHands canonical setup.
# The OpenHands CLI runs inside this container; agent tool calls spawn a
# *sibling* agent-server container (ghcr.io/openhands/agent-server:<ver>-python)
# on the host via the bind-mounted /var/run/docker.sock. DooD is independent
# of where inference happens, so it stays.
#
# Smoke run (Together AI backend):
#
#   GID=$(stat -c '%g' /var/run/docker.sock)
#   mkdir -p /tmp/oh-smoke
#   docker run --rm \
#     -v /var/run/docker.sock:/var/run/docker.sock \
#     --group-add "$GID" \
#     -v /tmp/oh-smoke:/workspace:rw \
#     -e RUNTIME=docker \
#     -e SANDBOX_USER_ID=$(id -u) \
#     -e AGENT_SERVER_IMAGE_REPOSITORY=ghcr.io/openhands/agent-server \
#     -e AGENT_SERVER_IMAGE_TAG=latest-python \
#     -e SANDBOX_VOLUMES=/tmp/oh-smoke:/workspace:rw \
#     -e LLM_API_KEY="$TOGETHER_API_KEY" \
#     -e LLM_MODEL="together_ai/Qwen/Qwen3.5-397B-A17B" \
#     -e LLM_BASE_URL="https://api.together.xyz/v1" \
#     -e LLM_NATIVE_TOOL_CALLING=true \
#     datacuration-bench-openhands:latest \
#     -lc 'openhands --headless --override-with-envs -t "<task>"'
#
# Smoke-tested 2026-05-11 with Qwen/Qwen3.5-397B-A17B: 2 iterations, native
# tool calls, terminal sandbox spawned via DooD, file created on host workspace.
#
# Swap models by changing LLM_MODEL. Examples (all LiteLLM `together_ai/`):
#   together_ai/Qwen/Qwen3.5-397B-A17B                (serverless, default)
#   together_ai/Qwen/Qwen3-Coder-480B-A35B-Instruct   (NEEDS DEDICATED ENDPOINT — non-serverless)
#   together_ai/moonshotai/Kimi-K2-Instruct           (likely needs dedicated endpoint)
#   together_ai/zai-org/GLM-4.6
#   together_ai/deepseek-ai/DeepSeek-V4-Pro           (set LLM_NATIVE_TOOL_CALLING=false)
#
# Per the Together AI error returned to OpenHands as ConversationErrorEvent,
# non-serverless models fail with: "Unable to access non-serverless model X.
# Please visit https://api.together.ai/models/X to create a dedicated endpoint."
# If you hit that, either switch to a serverless model or provision a dedicated
# endpoint in the Together dashboard.
#
# Notes vs. the upstream docs recipe (python:3.12-slim, runs as root, mounts
# ~/.openhands -> /root/.openhands):
#   - We bake the CLI into a CUDA base, so `--pull=always` + `pip install uv`
#     are unnecessary here. CUDA stays so the agent can shell out to GPU jobs.
#   - We keep the non-root `agent` user for parity with claude/codex.Dockerfile.
#     For DooD that means the agent must be able to read /var/run/docker.sock;
#     pass `--group-add $(stat -c '%g' /var/run/docker.sock)` at run time.
#   - `--override-with-envs` is REQUIRED — without it, OpenHands ignores
#     LLM_API_KEY/LLM_MODEL/LLM_BASE_URL and starts the interactive wizard.
#   - Together AI is not in OpenHands' docs by name; it works via LiteLLM
#     (https://docs.litellm.ai/docs/providers/togetherai). Prefix is
#     `together_ai/`, base URL is `https://api.together.xyz/v1`.
#
# CUDA devel image provides nvcc for building flash-attn from source
FROM nvidia/cuda:12.8.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# System deps + Python 3.12 from deadsnakes PPA + Docker CLI for DooD
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    git \
    gnupg \
    software-properties-common \
    ripgrep \
    gcc \
    g++ \
    libxcb1 \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    && ln -sf /usr/bin/python3.12 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.12 /usr/bin/python \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
       | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable" \
       > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

# Create a venv so pip works with Python 3.12
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Pre-install data science deps so the agent doesn't waste turns
RUN pip install --upgrade pip \
    && pip install datasets pyarrow numpy Pillow

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install OpenHands CLI as an isolated uv tool with its own Python 3.12.
# Canonical package is `openhands` (NOT `openhands-ai`, which is the legacy SDK).
# CLI requires Python ==3.12.*.
ENV UV_TOOL_DIR=/opt/uv-tools \
    UV_TOOL_BIN_DIR=/usr/local/bin
RUN uv tool install openhands --python 3.12
ENV DISABLE_AUTOUPDATER=1

# Disable OpenHands StuckDetector for headless long-running training/eval
# jobs. The default detector trips after 4 identical "wait/poll" actions
# (e.g. {"command": "", "is_input": true, "summary": "monitoring training"})
# which is exactly what agents do while a multi-hour finetune runs. The
# detector then forcibly ends the conversation and kills the container,
# taking down the finetune subprocess with it.
#
# There's no CLI flag or env var to disable this — the only Conversation
# constructor parameter `stuck_detection=False` must be passed in
# openhands_cli/setup.py. We patch that single line at image build time.
RUN sed -i 's|hook_config=hook_config,|hook_config=hook_config, stuck_detection=False,|' \
    /opt/uv-tools/openhands/lib/python3.12/site-packages/openhands_cli/setup.py \
    && grep -q "stuck_detection=False" \
       /opt/uv-tools/openhands/lib/python3.12/site-packages/openhands_cli/setup.py \
    && echo "✓ stuck_detection=False patch applied"

# Bump the default per-run iteration cap from 500 → 10000. The default 500
# is hit easily by long iterative benchmarks (12-iter pipelines × ~50-100
# tool calls each), causing the agent to be force-terminated mid-experiment
# with `MaxIterationsReached`. There is no CLI flag or env var to override
# this — the only handle is the `max_iteration_per_run` kwarg of the
# Conversation() constructor in openhands_cli/setup.py.
RUN sed -i 's|stuck_detection=False,|stuck_detection=False, max_iteration_per_run=10000,|' \
    /opt/uv-tools/openhands/lib/python3.12/site-packages/openhands_cli/setup.py \
    && grep -q "max_iteration_per_run=10000" \
       /opt/uv-tools/openhands/lib/python3.12/site-packages/openhands_cli/setup.py \
    && echo "✓ max_iteration_per_run=10000 patch applied"

# Add a Qwen3-style XML→tool_calls fallback to LLM.completion.
# Together AI's Qwen3.5-397B-A17B endpoint degrades under long context and
# returns tool calls as XML embedded in the assistant message's `content`
# instead of populating the native `tool_calls` field. OpenHands'
# response_dispatch.classify_response then reads "no tool calls = agent
# finished" and silently terminates the run.
#
# The patch intercepts that case in llm.py and re-synthesizes proper
# ChatCompletionMessageToolCall objects. It is anchored on the stable
# invariant (<parameter=K>V</parameter> blocks) rather than the volatile
# wrapper, so it handles Form A (<function=NAME>...), Form B
# (<tool_call><NAME>...), and truncated/incomplete XML (no closing tags).
#
# NOTE: this only fires when native_tool_calling=True AND tool_calls is
# None AND content has a <parameter=...> block. native happy-path
# responses (Kimi, etc.) are unaffected. native_tool_calling cannot be
# turned off via env var — OpenHands' --override-with-envs only reads
# LLM_API_KEY/LLM_BASE_URL/LLM_MODEL, so this fallback is the de-facto
# protection for the OpenHands+Qwen path.
COPY openhands_xml_fallback_patch.py /tmp/openhands_xml_fallback_patch.py
RUN python3 /tmp/openhands_xml_fallback_patch.py \
    && rm /tmp/openhands_xml_fallback_patch.py

# Make LLM_NATIVE_TOOL_CALLING env var actually take effect. By default
# OpenHands' --override-with-envs only reads LLM_API_KEY/LLM_BASE_URL/
# LLM_MODEL (see LLMEnvOverrides in openhands_cli/stores/agent_store.py)
# — LLM_NATIVE_TOOL_CALLING is silently dropped, so the per-agent
# `native_tools: true/false` config in docker.yaml is a no-op for
# OpenHands agents and `native_tool_calling` always falls back to its
# Field default (True). This patch adds LLM_NATIVE_TOOL_CALLING to the
# env-override surface so the existing docker.yaml setting actually
# applies per-agent (e.g. qwen=false to avoid XML format degradation,
# kimi=true since native FC works for it).
COPY openhands_native_tool_calling_env_patch.py /tmp/openhands_native_tool_calling_env_patch.py
RUN python3 /tmp/openhands_native_tool_calling_env_patch.py \
    && rm /tmp/openhands_native_tool_calling_env_patch.py

# Agent home: world-writable so any UID works
RUN useradd -m -s /bin/bash agent \
    && mkdir -p /home/agent/.openhands \
    && mkdir -p /home/agent/.cache/huggingface \
    && mkdir -p /home/agent/.triton \
    && chmod -R 777 /home/agent \
    && chmod 666 /etc/passwd

# Git config accessible to any user
RUN git config --system user.email "container@local" \
    && git config --system user.name "container"

ENTRYPOINT ["/bin/bash"]
