"""Tests for Docker runner agent configuration."""

from pathlib import Path

from benchmark.core.profile import Profile
from benchmark.runner.docker_runner import _AGENTS, _build_volumes


def test_codex_agent_uses_dedicated_image_and_json_exec():
    spec = _AGENTS["codex"]

    assert spec["dockerfile"] == "codex.Dockerfile"
    assert spec["tag"] == "datacuration-bench-codex:latest"
    assert "codex exec" in spec["cmd"]
    assert "--full-auto" in spec["cmd"]
    assert "--json" in spec["cmd"]
    assert spec["creds_dst"] == "/home/agent/.codex/auth.json"


def test_build_volumes_mounts_codex_credentials(tmp_path, monkeypatch):
    home = tmp_path / "home"
    auth = home / ".codex" / "auth.json"
    auth.parent.mkdir(parents=True)
    auth.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(Path, "home", lambda: home)

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    volumes = _build_volumes(Profile(), {}, output_dir, _AGENTS["codex"])

    assert str(auth) in volumes
    assert volumes[str(auth)] == {
        "bind": "/home/agent/.codex/auth.json",
        "mode": "ro",
    }


def test_build_volumes_mounts_claude_credentials(tmp_path, monkeypatch):
    home = tmp_path / "home"
    creds = home / ".claude" / ".credentials.json"
    creds.parent.mkdir(parents=True)
    creds.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(Path, "home", lambda: home)

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    volumes = _build_volumes(Profile(), {}, output_dir, _AGENTS["claude"])

    assert str(creds) in volumes
    assert volumes[str(creds)] == {
        "bind": "/home/agent/.claude/.credentials.json",
        "mode": "ro",
    }
