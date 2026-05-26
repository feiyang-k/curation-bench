"""Tests for run_prompt.md parser."""

import pytest

from benchmark.core.prompt import RunPrompt, parse_run_prompt, parse_run_prompt_text


class TestParseRunPromptText:
    def test_basic(self):
        text = """\
---
tasks:
  - task_a
  - task_b
iterations: 3
profile: helios
---

Prioritize OCR data.
"""
        result = parse_run_prompt_text(text)
        assert result.tasks == ["task_a", "task_b"]
        assert result.iterations == 3
        assert result.profile == "helios"
        assert result.strategy_text == "Prioritize OCR data."

    def test_defaults(self):
        text = """\
---
tasks:
  - only_task
---
"""
        result = parse_run_prompt_text(text)
        assert result.tasks == ["only_task"]
        assert result.iterations == 1
        assert result.profile is None
        assert result.strategy_text == ""

    def test_no_frontmatter_raises(self):
        with pytest.raises(ValueError, match="must start with YAML frontmatter"):
            parse_run_prompt_text("No frontmatter here.")

    def test_unclosed_frontmatter_raises(self):
        with pytest.raises(ValueError, match="missing closing ---"):
            parse_run_prompt_text("---\ntasks:\n  - x\n")

    def test_missing_tasks_raises(self):
        with pytest.raises(ValueError, match="must include 'tasks'"):
            parse_run_prompt_text("---\niterations: 2\n---\n")

    def test_empty_tasks_raises(self):
        with pytest.raises(ValueError, match="non-empty list"):
            parse_run_prompt_text("---\ntasks: []\n---\n")

    def test_invalid_task_entry_raises(self):
        with pytest.raises(ValueError, match="tasks\\[1\\] must be a non-empty string"):
            parse_run_prompt_text("---\ntasks:\n  - good\n  - 123\n---\n")

    def test_invalid_iterations_zero(self):
        with pytest.raises(ValueError, match="positive integer"):
            parse_run_prompt_text("---\ntasks:\n  - t\niterations: 0\n---\n")

    def test_invalid_iterations_string(self):
        with pytest.raises(ValueError, match="positive integer"):
            parse_run_prompt_text("---\ntasks:\n  - t\niterations: many\n---\n")

    def test_invalid_yaml_raises(self):
        with pytest.raises(ValueError, match="Invalid YAML"):
            parse_run_prompt_text("---\n: bad: yaml: {{\n---\n")

    def test_frontmatter_not_mapping_raises(self):
        with pytest.raises(ValueError, match="must be a YAML mapping"):
            parse_run_prompt_text("---\n- just a list\n---\n")

    def test_multiline_strategy(self):
        text = """\
---
tasks:
  - t1
---

Line one.

Line two.
Line three.
"""
        result = parse_run_prompt_text(text)
        assert "Line one." in result.strategy_text
        assert "Line three." in result.strategy_text

    def test_whitespace_in_task_ids_stripped(self):
        text = """\
---
tasks:
  - "  task_with_spaces  "
---
"""
        result = parse_run_prompt_text(text)
        assert result.tasks == ["task_with_spaces"]

    def test_source_path_in_error(self):
        with pytest.raises(ValueError, match="my_file.md"):
            parse_run_prompt_text("no frontmatter", source_path="my_file.md")


class TestParseRunPromptFile:
    def test_from_file(self, tmp_path):
        f = tmp_path / "run_prompt.md"
        f.write_text("---\ntasks:\n  - t1\niterations: 2\n---\nStrategy.\n")
        result = parse_run_prompt(f)
        assert result.tasks == ["t1"]
        assert result.iterations == 2
        assert result.strategy_text == "Strategy."
        assert str(f) in (result.source_path or "")

    def test_missing_file(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            parse_run_prompt(tmp_path / "missing.md")
