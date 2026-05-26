"""Docker-based runner for launching Claude/Codex agents."""

from __future__ import annotations

import json
import logging
import os
import shutil
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from ..core.profile import Profile, load_profile, resolve_profile_path, find_default_profile
from ..core.prompt import parse_run_prompt

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCKER_DIR = REPO_ROOT / "docker"

# Ensure the host UID exists in /etc/passwd so getpass.getuser() works
# (needed by PyTorch torchinductor, DeepSpeed, etc.)
_PASSWD_FIX = 'echo "agent:x:$(id -u):$(id -g)::/home/agent:/bin/bash" >> /etc/passwd 2>/dev/null; '

# Host-relative source paths under repo root. Used by docker_runner to
# stage the selected protocol; agents never see these filenames.
_HOST_PROTOCOL_FILES: dict[str, str] = {
    "plain": "protocols/plain.md",
    "instruction": "protocols/instruction.md",
    "skill": "protocols/skill.md",
}
# Canonical in-container path. Agents always read this regardless of
# which protocol variant is selected on the host — they cannot infer
# the variant from the filename.
_CONTAINER_PROTOCOL_PATH = "/workspace/PROTOCOL.md"

_AGENTS: dict[str, dict[str, Any]] = {
    "claude": {
        "dockerfile": "claude.Dockerfile",
        "tag": "datacuration-bench-claude:latest",
        "cmd": (
            _PASSWD_FIX +
            'cd /workspace && claude -p "$(cat {prompt_path})" '
            "--dangerously-skip-permissions "
            "--max-turns {max_turns} "
            "--verbose "
            "--output-format stream-json "
            "2>&1 | tee /workspace/output/run.jsonl"
        ),
        "creds_src": ".claude/.credentials.json",
        "creds_dst": "/home/agent/.claude/.credentials.json",
    },
    # DeepSeek-routed Claude Code: same CLI, but the image bakes in
    # ANTHROPIC_BASE_URL/ANTHROPIC_AUTH_TOKEN pointing at DeepSeek's
    # Anthropic-compatible API. No host credential mount.
    "claude-deepseek": {
        "dockerfile": "claude-deepseek.Dockerfile",
        "tag": "datacuration-bench-claude-deepseek:latest",
        "cmd": (
            _PASSWD_FIX +
            'cd /workspace && claude -p "$(cat {prompt_path})" '
            "--dangerously-skip-permissions "
            "--max-turns {max_turns} "
            "--verbose "
            "--output-format stream-json "
            "2>&1 | tee /workspace/output/run.jsonl"
        ),
    },
    "codex": {
        "dockerfile": "codex.Dockerfile",
        "tag": "datacuration-bench-codex:latest",
        "cmd": (
            _PASSWD_FIX +
            "cd /workspace && codex exec "
            "--dangerously-bypass-approvals-and-sandbox "
            "--skip-git-repo-check "
            "--json "
            "{model_flag}"
            "{effort_flag}"
            '"$(cat {prompt_path})" '
            "2>&1 | tee /workspace/output/run.jsonl"
        ),
        "creds_src": ".codex/auth.json",
        "creds_dst": "/home/agent/.codex/auth.json",
        "extra_mounts": [
            # config.toml has model/reasoning defaults; mount so codex picks them up
            {"src": ".codex/config.toml", "dst": "/home/agent/.codex/config.toml", "mode": "ro"},
        ],
    },
    # OpenHands CLI routed through Together AI (LiteLLM `together_ai/` prefix).
    # Two variants share the same image; they differ only by LLM_MODEL passed
    # at runtime (driven by docker.yaml::agents.<name>.model). Auth via
    # TOGETHER_API_KEY passed through from host env (see _apply_agent_env).
    # DooD: OpenHands spawns sibling agent-server containers via the
    # bind-mounted host docker socket.
    "openhands-kimi": {
        "dockerfile": "openhands.Dockerfile",
        "tag": "datacuration-bench-openhands:latest",
        "cmd": (
            _PASSWD_FIX +
            "cd /workspace && openhands --headless --json --override-with-envs "
            '-t "$(cat {prompt_path})" '
            "2>&1 | tee /workspace/output/run.jsonl"
        ),
        "extra_mounts": [
            {"src": "/var/run/docker.sock", "dst": "/var/run/docker.sock",
             "mode": "rw", "absolute": True},
        ],
        "needs_docker_sock": True,
    },
    "openhands-qwen": {
        "dockerfile": "openhands.Dockerfile",
        "tag": "datacuration-bench-openhands:latest",
        "cmd": (
            _PASSWD_FIX +
            "cd /workspace && openhands --headless --json --override-with-envs "
            '-t "$(cat {prompt_path})" '
            "2>&1 | tee /workspace/output/run.jsonl"
        ),
        "extra_mounts": [
            {"src": "/var/run/docker.sock", "dst": "/var/run/docker.sock",
             "mode": "rw", "absolute": True},
        ],
        "needs_docker_sock": True,
    },
}

_GPU_ENV_KEYS = ("CUDA_VISIBLE_DEVICES", "BENCHMARK_TRAIN_GPUS", "BENCHMARK_EVAL_GPUS")


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


def _build_cmd_kwargs(agent: str, agent_cfg: dict, prompt: str = "plain") -> dict:
    """Assemble format() kwargs used by the agent-specific cmd template.

    Unused keys are silently ignored by str.format(), so we can provide a
    superset — each agent's template only pulls what it needs.
    """
    kwargs: dict[str, Any] = {
        "max_turns": agent_cfg.get("max_turns", 5000),
        "model_flag": "",
        "effort_flag": "",
        # All protocols mount at the same canonical path; the agent
        # cannot tell which variant was selected on the host.
        "prompt_path": _CONTAINER_PROTOCOL_PATH,
    }
    if agent == "codex":
        model = agent_cfg.get("model")
        effort = agent_cfg.get("effort")
        if model:
            kwargs["model_flag"] = f"-m {model} "
        if effort:
            kwargs["effort_flag"] = f"-c model_reasoning_effort={effort} "
    return kwargs


def _apply_agent_env(env: dict, agent: str, agent_cfg: dict) -> None:
    """Inject agent-specific env vars derived from agents.<agent>.* config.

    Claude reads `ANTHROPIC_MODEL` / `CLAUDE_CODE_EFFORT_LEVEL` from env.
    Codex model/effort go through CLI flags (see _build_cmd_kwargs).
    OpenHands reads LLM_* env vars via `--override-with-envs`.
    """
    if agent in ("claude", "claude-deepseek"):
        if agent_cfg.get("model"):
            env["ANTHROPIC_MODEL"] = str(agent_cfg["model"])
        if agent_cfg.get("effort"):
            env["CLAUDE_CODE_EFFORT_LEVEL"] = str(agent_cfg["effort"])
    if agent == "claude-deepseek":
        # The DeepSeek image bakes in ANTHROPIC_AUTH_TOKEN. Drop any host
        # Anthropic OAuth token that _build_env passed through, otherwise
        # Claude Code may prefer it and route to api.anthropic.com instead.
        env.pop("CLAUDE_CODE_OAUTH_TOKEN", None)
    if agent.startswith("openhands"):
        # OpenHands routes inference through Together AI via LiteLLM. The
        # `together_ai/` prefix tells LiteLLM which provider to use.
        if agent_cfg.get("model"):
            env["LLM_MODEL"] = f"together_ai/{agent_cfg['model']}"
        env["LLM_BASE_URL"] = "https://api.together.xyz/v1"
        env["LLM_NATIVE_TOOL_CALLING"] = str(
            agent_cfg.get("native_tools", True)
        ).lower()
        # DooD runtime: OpenHands spawns sibling agent-server containers.
        env["RUNTIME"] = "docker"
        env["SANDBOX_USER_ID"] = str(os.getuid())
        env["AGENT_SERVER_IMAGE_REPOSITORY"] = "ghcr.io/openhands/agent-server"
        env["AGENT_SERVER_IMAGE_TAG"] = "latest-python"
        env["SANDBOX_VOLUMES"] = "/workspace:/workspace:rw"
        # Pass-through TOGETHER_API_KEY from host (mirrors CLAUDE_CODE_OAUTH_TOKEN
        # at _build_env). Never bake the key into the image.
        if "TOGETHER_API_KEY" in os.environ:
            env["LLM_API_KEY"] = os.environ["TOGETHER_API_KEY"]
        else:
            logger.warning(
                "TOGETHER_API_KEY not set in host env; OpenHands will fail to "
                "authenticate. Run: export TOGETHER_API_KEY=<your_key>"
            )


def load_docker_config(path: str | Path = "configs/docker.yaml") -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = REPO_ROOT / p
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Mount extraction
# ---------------------------------------------------------------------------


def _collect_profile_paths(profile: Profile) -> list[str]:
    """Collect all host paths from the profile that need mounting."""
    paths: list[str] = []
    for p in profile.dataset_path_map.values():
        paths.append(p)
    for p in profile.model_path_map.values():
        paths.append(p)
    if profile.eval_data_dir:
        paths.append(profile.eval_data_dir)
    return paths


def _dedupe_paths(paths: list[str]) -> list[str]:
    """Remove child paths if a parent is already in the list."""
    existing = sorted(set(p for p in paths if Path(p).exists()))
    result: list[str] = []
    for p in existing:
        if not any(p.startswith(parent + "/") for parent in result):
            result.append(p)
    return result


def _build_volumes(
    profile: Profile,
    docker_config: dict,
    output_dir: Path,
    spec: dict[str, Any],
) -> dict[str, dict[str, str]]:
    """Build the full volume mapping for the container."""
    volumes: dict[str, dict[str, str]] = {}

    # 1. Project repo → /workspace
    volumes[str(REPO_ROOT)] = {"bind": "/workspace", "mode": "rw"}

    # 2. Output directory
    volumes[str(output_dir)] = {"bind": "/workspace/output", "mode": "rw"}

    # 3. Profile paths (identity mounts). Eval dirs mount rw so VLMEvalKit
    # can extract images into an "images/" subdirectory; dataset and model
    # paths stay ro.
    eval_paths = {profile.eval_data_dir} if profile.eval_data_dir else set()
    for p in _dedupe_paths(_collect_profile_paths(profile)):
        mode = "rw" if p in eval_paths else "ro"
        volumes[p] = {"bind": p, "mode": mode}

    # 4. Agent credentials (optional — agents that auth via env vars omit creds_src)
    creds_src = spec.get("creds_src")
    if creds_src:
        creds = Path.home() / creds_src
        if creds.exists():
            volumes[str(creds)] = {"bind": spec["creds_dst"], "mode": "ro"}
        else:
            logger.warning("Agent credentials not found at %s", creds)

    # 4b. Agent extra mounts. `src` is relative to $HOME by default; set
    # `absolute: True` to treat it as an absolute host path (e.g. for
    # /var/run/docker.sock when an agent needs Docker-out-of-Docker).
    for em in spec.get("extra_mounts", []):
        src = em["src"]
        em_src = Path(src) if em.get("absolute") else (Path.home() / src)
        if em_src.exists():
            volumes[str(em_src)] = {"bind": em["dst"], "mode": em.get("mode", "ro")}
        else:
            logger.warning("Agent extra mount not found at %s", em_src)

    # 5. Extra mounts from docker.yaml
    for m in docker_config.get("mounts", []):
        src = m["src"]
        if Path(src).exists():
            volumes[src] = {"bind": m["dst"], "mode": m.get("mode", "ro")}

    return volumes


# ---------------------------------------------------------------------------
# GPU handling
# ---------------------------------------------------------------------------


def _remap_gpu_ids(host_gpu_str: str, visible_gpus: list[int]) -> str:
    """Map host GPU IDs to container-local IDs.

    E.g., host_gpu_str="2,3", visible_gpus=[2,3] -> "0,1"
    """
    host_ids = [int(x.strip()) for x in host_gpu_str.split(",") if x.strip()]
    remapped = []
    for hid in host_ids:
        try:
            remapped.append(str(visible_gpus.index(hid)))
        except ValueError:
            remapped.append(str(hid))  # fallback: keep original
    return ",".join(remapped)


def _build_env(profile: Profile, docker_config: dict) -> tuple[dict[str, str], list[str]]:
    """Build container env vars and return (env_dict, host_gpu_ids)."""
    env: dict[str, str] = {}

    # Docker config env
    for k, v in docker_config.get("env", {}).items():
        env[k] = str(v)

    # Profile env (overrides docker config)
    for k, v in profile.env.items():
        env[k] = str(v)

    # Parse host GPU list
    cuda_vis = env.get("CUDA_VISIBLE_DEVICES", "0")
    host_gpus = [int(x.strip()) for x in cuda_vis.split(",") if x.strip()]
    host_gpu_ids = [str(g) for g in host_gpus]

    # Remap GPU env vars to container-local IDs
    env["CUDA_VISIBLE_DEVICES"] = ",".join(str(i) for i in range(len(host_gpus)))
    for key in ("BENCHMARK_TRAIN_GPUS", "BENCHMARK_EVAL_GPUS"):
        if key in env:
            env[key] = _remap_gpu_ids(env[key], host_gpus)

    # Container user
    env["HOME"] = "/home/agent"
    env["GIT_CONFIG_SYSTEM"] = "/etc/gitconfig"

    # Pass through host CLAUDE_CODE_OAUTH_TOKEN for API billing (overrides mounted credentials.json)
    if "CLAUDE_CODE_OAUTH_TOKEN" in os.environ:
        env["CLAUDE_CODE_OAUTH_TOKEN"] = os.environ["CLAUDE_CODE_OAUTH_TOKEN"]

    return env, host_gpu_ids


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def run_agent(
    agent: str,
    *,
    profile_name: str | None = None,
    docker_config_path: str = "configs/docker.yaml",
    rebuild: bool = False,
    dry_run: bool = False,
    new_suite: bool = False,
    prompt: str = "plain",
) -> int:
    """Run the benchmark: one container per task, each handling all its iterations.

    Returns 0 if all tasks' containers exited 0, else the last non-zero exit code.
    """
    spec = _AGENTS[agent]

    # Load profile
    if profile_name:
        profile_path = resolve_profile_path(profile_name)
    else:
        profile_path = find_default_profile()
        if not profile_path:
            raise SystemExit("No profile found. Pass --profile or create profiles/*.yaml")
    profile = load_profile(profile_path)

    # Parse run_prompt.md to get the task list
    run_prompt = parse_run_prompt(REPO_ROOT / "run_prompt.md")
    tasks = run_prompt.tasks
    logger.info("Tasks to run: %s (each with %d iterations)", tasks, run_prompt.iterations)

    # Load docker config
    docker_config = load_docker_config(docker_config_path)
    agent_cfg = docker_config.get("agents", {}).get(agent, {})
    max_turns = agent_cfg.get("max_turns", 5000)

    # Suite-level output directory (shared across all task containers)
    suite_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if dry_run:
        # Just print the first task's docker run command for reference
        output_dir = REPO_ROOT / "runs" / f"docker_{agent}_{suite_stamp}_{tasks[0]}"
        output_dir.mkdir(parents=True, exist_ok=True)
        volumes = _build_volumes(profile, docker_config, output_dir, spec)
        env, host_gpu_ids = _build_env(profile, docker_config)
        _apply_agent_env(env, agent, agent_cfg)
        env["BENCHMARK_CURRENT_TASK"] = tasks[0]
        cmd = spec["cmd"].format(**_build_cmd_kwargs(agent, agent_cfg, prompt))
        _print_dry_run(spec["tag"], cmd, volumes, env, host_gpu_ids)
        return 0

    # Before init: flip any leftover container-form paths (from a previous
    # crashed run) back to host form so init's resume check can find them.
    _rewrite_suite_paths(REPO_ROOT, to_container=False)

    # Host-side init: create suite with all targets before any container starts.
    # BENCHMARK_AGENT / BENCHMARK_NEW_SUITE are read by cmd_init to:
    #   - segregate suites per agent (claude vs codex don't share a suite)
    #   - honor --new-suite to force a fresh suite even for the same agent.
    logger.info("Initializing suite on host ...")
    init_env = {**os.environ, "BENCHMARK_AGENT": agent}
    if new_suite:
        init_env["BENCHMARK_NEW_SUITE"] = "1"
    init_result = subprocess.run(
        ["uv", "run", "datacuration-bench", "init"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env=init_env,
    )
    if init_result.returncode != 0:
        logger.error("Suite init failed: %s", init_result.stderr)
        return 1

    # Rewrite all host paths in suite state files to container paths (/workspace/...).
    # The host init uses host paths, but the container only sees /workspace.
    _rewrite_suite_paths(REPO_ROOT, to_container=True)

    logger.info("Suite initialized.")

    # Docker client
    import docker
    client = docker.from_env()

    # Build or reuse image (only once, before the loop)
    tag = spec["tag"]
    if rebuild or not _image_exists(client, tag):
        logger.info("Building Docker image %s ...", tag)
        client.images.build(
            path=str(DOCKER_DIR),
            dockerfile=spec["dockerfile"],
            tag=tag,
        )
    else:
        logger.info("Reusing existing image %s", tag)

    # Loop: one container per task
    last_exit_code = 0
    for task_id in tasks:
        logger.info("=" * 60)
        logger.info("Starting container for task: %s", task_id)
        logger.info("=" * 60)

        exit_code = _run_one_task_container(
            client=client,
            agent=agent,
            spec=spec,
            task_id=task_id,
            suite_stamp=suite_stamp,
            profile=profile,
            docker_config=docker_config,
            max_turns=max_turns,
            prompt=prompt,
        )
        if exit_code != 0:
            last_exit_code = exit_code
            logger.warning("Task %s container exited with code %d", task_id, exit_code)

    # Print final suite result
    suite_result = REPO_ROOT / ".bench_active_suite"
    if suite_result.exists():
        suite_dir = Path(suite_result.read_text(encoding="utf-8").strip())
        result_file = suite_dir / "suite_result.json"
        if result_file.exists():
            logger.info("Suite result:\n%s", result_file.read_text(encoding="utf-8"))

    return last_exit_code


def _rewrite_suite_paths(repo_root: Path, *, to_container: bool) -> None:
    """Rewrite absolute paths in suite state files between host and container forms.

    Host init writes paths like /home/.../datacuration-benchmark1/runs/<stamp>.
    Inside the container these paths don't exist — only /workspace is mounted.
    Forward rewrite (to_container=True) runs after `init` so the container can
    read state; reverse rewrite (to_container=False) runs before `init` so that
    a leftover container-form pointer from a crashed run becomes valid again on
    the host (needed for resume).
    """
    host_prefix = str(repo_root)
    container_prefix = "/workspace"
    src, dst = (host_prefix, container_prefix) if to_container else (container_prefix, host_prefix)

    # 1. .bench_active_suite (plain text)
    active_file = repo_root / ".bench_active_suite"
    if not active_file.exists():
        return
    text = active_file.read_text(encoding="utf-8")
    active_file.write_text(text.replace(src, dst), encoding="utf-8")

    # 2. Resolve the suite dir on the host filesystem, independent of pointer form
    pointer_text = active_file.read_text(encoding="utf-8").strip()
    host_suite_dir = Path(pointer_text.replace(container_prefix, host_prefix, 1))
    if not host_suite_dir.exists():
        return

    # 3. suite_state.json (JSON with embedded paths)
    state_file = host_suite_dir / "suite_state.json"
    if state_file.exists():
        text = state_file.read_text(encoding="utf-8")
        state_file.write_text(text.replace(src, dst), encoding="utf-8")

    # 4. task.resolved.yaml files contain suite-relative run paths
    for task_yaml in host_suite_dir.rglob("task.resolved.yaml"):
        text = task_yaml.read_text(encoding="utf-8")
        task_yaml.write_text(text.replace(src, dst), encoding="utf-8")


def _run_one_task_container(
    *,
    client,
    agent: str,
    spec: dict,
    task_id: str,
    suite_stamp: str,
    profile: Profile,
    docker_config: dict,
    max_turns: int,
    prompt: str = "plain",
) -> int:
    """Start a container to handle all iterations of one task."""
    import docker

    # Per-task output directory
    output_dir = REPO_ROOT / "runs" / f"docker_{agent}_{suite_stamp}_{task_id}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build volumes, env, GPU config (fresh each iteration so BENCHMARK_CURRENT_TASK is set)
    volumes = _build_volumes(profile, docker_config, output_dir, spec)
    env, host_gpu_ids = _build_env(profile, docker_config)
    agent_cfg = docker_config.get("agents", {}).get(agent, {})
    _apply_agent_env(env, agent, agent_cfg)
    env["BENCHMARK_CURRENT_TASK"] = task_id

    # Per-task isolated curation/ working dir. Each task gets its own copy of
    # the repo-root curation/ baseline, mounted at /workspace/curation. This
    # prevents cross-task pollution when containers run in parallel, while
    # letting iterations of the same task inherit prior code.
    active_file = REPO_ROOT / ".bench_active_suite"
    if active_file.exists():
        suite_ref = active_file.read_text(encoding="utf-8").strip()
        suite_host = Path(suite_ref.replace("/workspace", str(REPO_ROOT), 1))
        task_curation_host = suite_host / task_id / "curation"
        baseline = REPO_ROOT / "curation"
        if not task_curation_host.exists() and baseline.exists():
            task_curation_host.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(baseline, task_curation_host)
        volumes[str(task_curation_host)] = {"bind": "/workspace/curation", "mode": "rw"}

        # Per-task protocol staging. Copy the selected protocol source to
        # <suite>/<task_id>/PROTOCOL.md and mount that single file at the
        # canonical container path read-only. Combined with the tmpfs
        # overlay below on /workspace/protocols, this means the agent sees
        # exactly one protocol file under a name that doesn't reveal which
        # variant (plain/instruction/skill) it received.
        host_protocol_src = REPO_ROOT / _HOST_PROTOCOL_FILES[prompt]
        if not host_protocol_src.exists():
            raise SystemExit(
                f"Selected protocol source missing: {host_protocol_src}"
            )
        task_protocol_host = suite_host / task_id / "PROTOCOL.md"
        if not task_protocol_host.exists():
            task_protocol_host.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(host_protocol_src, task_protocol_host)
        volumes[str(task_protocol_host)] = {
            "bind": _CONTAINER_PROTOCOL_PATH,
            "mode": "ro",
        }

    cmd = spec["cmd"].format(**_build_cmd_kwargs(agent, agent_cfg, prompt))
    user = f"{os.getuid()}:{os.getgid()}"

    logger.info("Launching container (task=%s, max_turns=%d)", task_id, max_turns)
    run_kwargs: dict[str, Any] = dict(
        image=spec["tag"],
        command=["-c", cmd],
        environment=env,
        volumes=volumes,
        user=user,
        device_requests=[
            docker.types.DeviceRequest(
                device_ids=host_gpu_ids,
                capabilities=[["gpu"]],
            )
        ],
        ipc_mode="host",
        network_mode="host",
        shm_size="16g",
        detach=True,
        # Hide the host's protocols/ source dir from the agent. An empty
        # tmpfs at this path overrides the inherited /workspace mount so
        # the unselected protocol files are physically unreachable.
        tmpfs={"/workspace/protocols": ""},
    )
    if spec.get("needs_docker_sock"):
        # Non-root `agent` user inside the container needs to read
        # /var/run/docker.sock; add the host docker group's GID.
        sock_gid = os.stat("/var/run/docker.sock").st_gid
        run_kwargs["group_add"] = [sock_gid]
    container = client.containers.run(**run_kwargs)

    # Stream logs to console. The container's entrypoint also tees to
    # /workspace/output/run.jsonl, so we don't duplicate it on the host.
    from .stream_parser import print_stream

    try:
        print_stream(container.logs(stream=True, follow=True), log_file=None)
        result = container.wait()
    except KeyboardInterrupt:
        logger.warning("Interrupted — stopping container for task %s...", task_id)
        container.stop(timeout=10)
        result = {"StatusCode": -1}

    exit_code = result.get("StatusCode", -1)
    logger.info("Task %s container finished (exit=%d)", task_id, exit_code)

    try:
        container.remove()
    except Exception:
        pass

    return exit_code


def _image_exists(client, tag: str) -> bool:
    try:
        client.images.get(tag)
        return True
    except Exception:
        return False


def _print_dry_run(
    tag: str,
    cmd: str,
    volumes: dict[str, dict[str, str]],
    env: dict[str, str],
    gpu_ids: list[str],
) -> None:
    """Print the equivalent docker run command."""
    parts = ["docker run --rm -it"]
    parts.append(f'  --gpus \'"device={",".join(gpu_ids)}"\'')
    parts.append("  --ipc=host --shm-size=16g")
    for src, mount in sorted(volumes.items()):
        mode = mount["mode"]
        dst = mount["bind"]
        parts.append(f"  -v {src}:{dst}:{mode}")
    for k, v in sorted(env.items()):
        # Mask secrets
        display = "***" if "KEY" in k or "SECRET" in k or "TOKEN" in k else v
        parts.append(f"  -e {k}={display}")
    parts.append(f"  {tag}")
    parts.append(f"  -c '{cmd}'")
    print(" \\\n".join(parts))
