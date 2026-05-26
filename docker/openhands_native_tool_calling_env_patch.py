"""Patch openhands_cli/stores/agent_store.py so LLMEnvOverrides reads
LLM_NATIVE_TOOL_CALLING from the environment.

Background: docker.yaml exposes a per-agent `native_tools: true/false`
key which docker_runner.py translates into the LLM_NATIVE_TOOL_CALLING
env var. But OpenHands' --override-with-envs path only reads
LLM_API_KEY / LLM_BASE_URL / LLM_MODEL — LLM_NATIVE_TOOL_CALLING is
silently dropped, and `native_tool_calling` falls back to its Field
default (True). So the per-agent config has been a no-op.

This patch adds LLM_NATIVE_TOOL_CALLING to the env-override surface so
the existing docker.yaml setting actually takes effect per-agent
(qwen=false, kimi=true, etc.).

Run at image build time:
    python3 openhands_native_tool_calling_env_patch.py
"""

from __future__ import annotations

import pathlib
import py_compile
import sys

AGENT_STORE = pathlib.Path(
    "/opt/uv-tools/openhands/lib/python3.12/site-packages/openhands_cli/stores/agent_store.py"
)

# --- Anchor 1: env-var constant declarations ---------------------------------
ANCHOR_1_OLD = '''ENV_LLM_API_KEY = "LLM_API_KEY"
ENV_LLM_BASE_URL = "LLM_BASE_URL"
ENV_LLM_MODEL = "LLM_MODEL"
'''
ANCHOR_1_NEW = '''ENV_LLM_API_KEY = "LLM_API_KEY"
ENV_LLM_BASE_URL = "LLM_BASE_URL"
ENV_LLM_MODEL = "LLM_MODEL"
ENV_LLM_NATIVE_TOOL_CALLING = "LLM_NATIVE_TOOL_CALLING"
'''

# --- Anchor 2: LLMEnvOverrides field declarations ----------------------------
ANCHOR_2_OLD = '''    api_key: SecretStr | None = None
    base_url: str | None = None
    model: str | None = None
'''
ANCHOR_2_NEW = '''    api_key: SecretStr | None = None
    base_url: str | None = None
    model: str | None = None
    native_tool_calling: bool | None = None
'''

# --- Anchor 3: from_env logic (read env, parse to bool) ----------------------
ANCHOR_3_OLD = '''        model = os.environ.get(ENV_LLM_MODEL) or None
        if model:
            result["model"] = model

        return cls(**result)
'''
ANCHOR_3_NEW = '''        model = os.environ.get(ENV_LLM_MODEL) or None
        if model:
            result["model"] = model

        ntc_str = os.environ.get(ENV_LLM_NATIVE_TOOL_CALLING)
        if ntc_str is not None and ntc_str != "":
            result["native_tool_calling"] = (
                ntc_str.strip().lower() in ("true", "1", "yes", "on")
            )

        return cls(**result)
'''

# --- Anchor 4: has_overrides() should include the new field ------------------
ANCHOR_4_OLD = '''    def has_overrides(self) -> bool:
        """Check if any overrides are set."""
        return any([self.api_key, self.base_url, self.model])
'''
ANCHOR_4_NEW = '''    def has_overrides(self) -> bool:
        """Check if any overrides are set."""
        return any(
            [self.api_key, self.base_url, self.model, self.native_tool_calling is not None]
        )
'''


def main() -> int:
    src = AGENT_STORE.read_text()
    if "ENV_LLM_NATIVE_TOOL_CALLING" in src:
        print("✓ native_tool_calling env patch already applied; skipping.")
        return 0

    for name, old, new in [
        ("env-var constant", ANCHOR_1_OLD, ANCHOR_1_NEW),
        ("LLMEnvOverrides field", ANCHOR_2_OLD, ANCHOR_2_NEW),
        ("from_env logic", ANCHOR_3_OLD, ANCHOR_3_NEW),
        ("has_overrides", ANCHOR_4_OLD, ANCHOR_4_NEW),
    ]:
        if old not in src:
            print(
                f"✗ anchor not found: {name} -- upstream layout changed.",
                file=sys.stderr,
            )
            return 1
        src = src.replace(old, new, 1)

    AGENT_STORE.write_text(src)
    try:
        py_compile.compile(str(AGENT_STORE), doraise=True)
    except py_compile.PyCompileError as e:
        print(f"✗ patched agent_store.py failed to compile: {e}", file=sys.stderr)
        return 2

    print("✓ native_tool_calling env patch applied to agent_store.py and compiles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
