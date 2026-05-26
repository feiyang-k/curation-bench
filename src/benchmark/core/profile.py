"""Loader for machine-local profile YAML files.

A profile contains dataset/model path mappings, eval data directories,
and environment variables.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Profile:
    """Parsed machine-local profile."""

    dataset_path_map: dict[str, str] = field(default_factory=dict)
    model_path_map: dict[str, str] = field(default_factory=dict)
    eval_data_dir: str | None = None
    env: dict[str, str] = field(default_factory=dict)

    # Original path for error messages
    source_path: str | None = None


def load_profile(path: str | Path) -> Profile:
    """Load a profile from a YAML file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Profile not found: {path}")
    text = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in profile {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(
            f"Profile must be a YAML mapping, got {type(data).__name__} (in {path})"
        )

    return _parse_profile(data, source_path=str(path))


def resolve_profile_path(
    name_or_path: str,
    profiles_dir: str | Path | None = None,
) -> Path:
    """Resolve a profile name or path to an actual file.

    - If name_or_path is an existing file path, return it directly.
    - Otherwise treat it as a profile name and look in profiles_dir
      (default: ./profiles/) for {name}.yaml.
    """
    p = Path(name_or_path)
    if p.exists() and p.is_file():
        return p

    base = Path(profiles_dir) if profiles_dir else Path.cwd() / "profiles"
    # Try with .yaml extension
    candidate = base / f"{name_or_path}.yaml"
    if candidate.exists():
        return candidate
    # Try with .yml extension
    candidate_yml = base / f"{name_or_path}.yml"
    if candidate_yml.exists():
        return candidate_yml
    # Try as-is (maybe user passed "helios.yaml")
    candidate_as_is = base / name_or_path
    if candidate_as_is.exists():
        return candidate_as_is

    raise FileNotFoundError(
        f"Profile not found: tried {p}, {candidate}, {candidate_yml}, {candidate_as_is}"
    )


def find_default_profile(profiles_dir: str | Path | None = None) -> Path | None:
    """Find the first .yaml file in the profiles directory, or None."""
    base = Path(profiles_dir) if profiles_dir else Path.cwd() / "profiles"
    if not base.is_dir():
        return None
    yamls = sorted(base.glob("*.yaml"))
    if not yamls:
        yamls = sorted(base.glob("*.yml"))
    return yamls[0] if yamls else None


def _parse_profile(data: dict, *, source_path: str | None = None) -> Profile:
    """Construct a Profile from a parsed YAML dict."""
    dataset_path_map = _extract_str_map(data, "dataset_path_map", source_path)
    model_path_map = _extract_str_map(data, "model_path_map", source_path)
    env = _extract_str_map(data, "env", source_path)

    eval_data_dir = data.get("eval_data_dir")

    return Profile(
        dataset_path_map=dataset_path_map,
        model_path_map=model_path_map,
        eval_data_dir=str(eval_data_dir) if eval_data_dir else None,
        env=env,
        source_path=source_path,
    )


def _extract_str_map(
    data: dict, key: str, source_path: str | None
) -> dict[str, str]:
    """Extract an optional string→string mapping from the data dict."""
    raw = data.get(key)
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ValueError(
            f"'{key}' must be a mapping, got {type(raw).__name__} (in {source_path})"
        )
    return {str(k): str(v) for k, v in raw.items()}
