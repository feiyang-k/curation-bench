# Codex sandbox for datacuration benchmark
# CUDA devel image provides nvcc for building flash-attn from source
FROM nvidia/cuda:12.8.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# System deps + Python 3.12 from deadsnakes PPA
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
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    && ln -sf /usr/bin/python3.12 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.12 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Create a venv so pip works with Python 3.12
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Pre-install data science deps so the agent doesn't waste turns
RUN pip install --upgrade pip \
    && pip install datasets pyarrow numpy Pillow

# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN npm install -g @openai/codex@0.123.0
ENV DISABLE_AUTOUPDATER=1

# Agent home: world-writable so any UID works
RUN useradd -m -s /bin/bash agent \
    && mkdir -p /home/agent/.codex \
    && mkdir -p /home/agent/.cache/huggingface \
    && mkdir -p /home/agent/.triton \
    && chmod -R 777 /home/agent \
    && chmod 666 /etc/passwd

# Git config accessible to any user
RUN git config --system user.email "container@local" \
    && git config --system user.name "container"

ENTRYPOINT ["/bin/bash"]
