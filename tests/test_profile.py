"""Tests for profile YAML loader."""

import pytest

from benchmark.core.profile import (
    Profile,
    find_default_profile,
    load_profile,
    resolve_profile_path,
)


class TestLoadProfile:
    def test_full_profile(self, tmp_path):
        f = tmp_path / "test.yaml"
        f.write_text("""\
dataset_path_map:
  llava665k: /data/llava665k
  visionflan: /data/visionflan
model_path_map:
  llava-1.5-7b-hf: /models/llava
  qwen2.5-vl-3b-instruct: /models/qwen
eval_data_dir: /eval/LMUData
env:
  CUDA_VISIBLE_DEVICES: "0,1"
  HF_HOME: /cache/hf
""")
        p = load_profile(f)
        assert p.dataset_path_map == {
            "llava665k": "/data/llava665k",
            "visionflan": "/data/visionflan",
        }
        assert p.model_path_map["qwen2.5-vl-3b-instruct"] == "/models/qwen"
        assert p.eval_data_dir == "/eval/LMUData"
        assert p.env["CUDA_VISIBLE_DEVICES"] == "0,1"

    def test_minimal_profile(self, tmp_path):
        f = tmp_path / "minimal.yaml"
        f.write_text("dataset_path_map:\n  ds: /data/ds\n")
        p = load_profile(f)
        assert p.dataset_path_map == {"ds": "/data/ds"}
        assert p.model_path_map == {}
        assert p.eval_data_dir is None
        assert p.env == {}

    def test_empty_profile(self, tmp_path):
        f = tmp_path / "empty.yaml"
        f.write_text("{}\n")
        p = load_profile(f)
        assert p.dataset_path_map == {}

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_profile(tmp_path / "missing.yaml")

    def test_invalid_yaml_raises(self, tmp_path):
        f = tmp_path / "bad.yaml"
        f.write_text(": bad: yaml: {{\n")
        with pytest.raises(ValueError, match="Invalid YAML"):
            load_profile(f)

    def test_non_mapping_raises(self, tmp_path):
        f = tmp_path / "list.yaml"
        f.write_text("- item1\n- item2\n")
        with pytest.raises(ValueError, match="must be a YAML mapping"):
            load_profile(f)

    def test_invalid_path_map_raises(self, tmp_path):
        f = tmp_path / "bad_map.yaml"
        f.write_text("dataset_path_map: just_a_string\n")
        with pytest.raises(ValueError, match="dataset_path_map.*must be a mapping"):
            load_profile(f)


class TestResolveProfilePath:
    def test_existing_file(self, tmp_path):
        f = tmp_path / "direct.yaml"
        f.write_text("{}\n")
        assert resolve_profile_path(str(f)) == f

    def test_name_in_profiles_dir(self, tmp_path):
        profiles = tmp_path / "profiles"
        profiles.mkdir()
        f = profiles / "helios.yaml"
        f.write_text("{}\n")
        result = resolve_profile_path("helios", profiles_dir=profiles)
        assert result == f

    def test_name_with_yml_extension(self, tmp_path):
        profiles = tmp_path / "profiles"
        profiles.mkdir()
        f = profiles / "helios.yml"
        f.write_text("{}\n")
        result = resolve_profile_path("helios", profiles_dir=profiles)
        assert result == f

    def test_name_with_yaml_suffix(self, tmp_path):
        profiles = tmp_path / "profiles"
        profiles.mkdir()
        f = profiles / "helios.yaml"
        f.write_text("{}\n")
        result = resolve_profile_path("helios.yaml", profiles_dir=profiles)
        assert result == f

    def test_not_found_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            resolve_profile_path("nonexistent", profiles_dir=tmp_path)


class TestFindDefaultProfile:
    def test_finds_first_yaml(self, tmp_path):
        (tmp_path / "alpha.yaml").write_text("{}\n")
        (tmp_path / "beta.yaml").write_text("{}\n")
        result = find_default_profile(tmp_path)
        assert result == tmp_path / "alpha.yaml"

    def test_no_profiles_dir(self, tmp_path):
        result = find_default_profile(tmp_path / "nonexistent")
        assert result is None

    def test_empty_dir(self, tmp_path):
        result = find_default_profile(tmp_path)
        assert result is None

    def test_falls_back_to_yml(self, tmp_path):
        (tmp_path / "only.yml").write_text("{}\n")
        result = find_default_profile(tmp_path)
        assert result == tmp_path / "only.yml"
