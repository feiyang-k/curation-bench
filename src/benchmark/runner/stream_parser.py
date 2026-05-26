"""Pretty-print parser for Claude Code stream-json output."""

from __future__ import annotations

import json
import sys
from typing import Iterator


def print_stream(log_stream: Iterator[bytes], *, log_file=None) -> None:
    """Parse stream-json lines from Claude Code and pretty-print them.

    docker-py emits byte-level chunks (sometimes 1 byte each), so buffer until
    we see a newline before splitting into lines. Without this, each byte gets
    treated as a separate line and output is one character per row.
    """
    buffer = b''
    for chunk in log_stream:
        buffer += chunk
        while b"\n" in buffer:
            raw, buffer = buffer.split(b"\n", 1)
            line = raw.decode('utf-8', errors='replace').strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                _emit(line, log_file)
                continue
            _handle_json(obj, log_file)
    tail = buffer.decode('utf-8', errors='replace').strip()
    if tail:
        try:
            obj = json.loads(tail)
            _handle_json(obj, log_file)
        except json.JSONDecodeError:
            _emit(tail, log_file)


def _emit(text: str, log_file=None) -> None:
    print(text, flush=True)
    if log_file:
        log_file.write(text + "\n")
        log_file.flush()


def _handle_json(obj, log_file) -> None:
    # Codex occasionally emits bare ints/strings/lists in its JSON stream;
    # only dicts have meaningful type/message structure. Skip non-dicts safely.
    if not isinstance(obj, dict):
        return

    # OpenHands events use `kind` (not Claude's `type` field). Detect early
    # and route to the OpenHands handler before the Claude/Codex branches.
    if obj.get("kind") and not obj.get("type"):
        _handle_openhands(obj, log_file)
        return

    msg_type = obj.get("type", "")

    if msg_type == "assistant":
        msg = obj.get("message", {})
        for block in msg.get("content", []):
            if block.get("type") == "text" and block.get("text"):
                _emit(f"\n[assistant] {block['text']}", log_file)
            elif block.get("type") == "tool_use":
                name = block.get("name", "?")
                inp = block.get("input", {})
                if name == "Bash":
                    _emit(f"\n[tool] {name}: {inp.get('command', '')}", log_file)
                elif name in ("Read", "Glob", "Grep"):
                    _emit(
                        f"\n[tool] {name}: "
                        f"{inp.get('file_path', inp.get('pattern', inp.get('path', '')))}",
                        log_file,
                    )
                elif name == "Write":
                    _emit(f"\n[tool] {name}: {inp.get('file_path', '')}", log_file)
                else:
                    _emit(f"\n[tool] {name}: {str(inp)[:200]}", log_file)

    elif msg_type == "user":
        msg = obj.get("message", {})
        for block in msg.get("content", []):
            if block.get("type") == "tool_result":
                content = block.get("content", "")
                if isinstance(content, str) and len(content) > 300:
                    content = content[:300] + "..."
                _emit(f"  => {content}", log_file)

    elif msg_type == "result":
        cost = obj.get("total_cost_usd", 0)
        turns = obj.get("num_turns", 0)
        dur = obj.get("duration_ms", 0) / 1000
        _emit(f"\n--- Done: {turns} turns, {dur:.1f}s, ${cost:.4f} ---", log_file)

    # Codex 0.123 event format
    elif msg_type == "turn.started":
        _emit("\n--- TURN START ---", log_file)
    elif msg_type == "turn.completed":
        usage = obj.get("usage", {}) or {}
        _emit(
            f"\n--- TURN END  input={usage.get('input_tokens', '?')} "
            f"output={usage.get('output_tokens', '?')} ---",
            log_file,
        )
    elif msg_type == "thread.started":
        _emit("\n[thread started]", log_file)
    elif msg_type == "item.completed":
        item = obj.get("item", {}) or {}
        it = item.get("type", "")
        if it == "agent_message":
            text = (item.get("text") or "").replace("\n", " ")[:300]
            _emit(f"\n[say] {text}", log_file)
        elif it == "command_execution":
            cmd = (item.get("command") or "").replace("\n", " | ")[:200]
            ec = item.get("exit_code", 0)
            tag = "" if ec == 0 else f" exit={ec}"
            _emit(f"\n[cmd{tag}] {cmd}", log_file)
        elif it == "collab_tool_call":
            tool = item.get("tool", "?")
            prompt_text = (item.get("prompt") or "").replace("\n", " ")[:200]
            _emit(f"\n[sub:{tool}] {prompt_text}", log_file)
        elif it == "reasoning":
            text = (item.get("text") or "").replace("\n", " ")[:200]
            _emit(f"\n[think] {text}", log_file)
        else:
            # Unknown item.type — surface raw so we don't go dark
            raw = json.dumps(item, ensure_ascii=False)[:200]
            _emit(f"\n[item:{it}] {raw}", log_file)

    elif msg_type:
        # Unknown top-level type — surface raw so we don't go dark
        raw = json.dumps(obj, ensure_ascii=False)[:200]
        _emit(f"\n[?{msg_type}] {raw}", log_file)


# ---------------------------------------------------------------------------
# OpenHands event handler
# ---------------------------------------------------------------------------
# OpenHands emits one JSON line per event when invoked with `--json`. Each
# event has a `kind` field (vs Claude/Codex `type`). Schema reference:
# https://github.com/All-Hands-AI/OpenHands (sdk events module)


_ANSI_SCRUB = ("\x1b[?2004l", "\x1b[?2004h", "\x1b[?25l", "\x1b[?25h")


def _scrub_ansi(text) -> str:
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    for esc in _ANSI_SCRUB:
        text = text.replace(esc, "")
    return text


def _extract_text_blocks(value) -> str:
    """Pull readable text from OpenHands content/observation fields.

    These fields can be a plain string, a list of {type, text} blocks
    (vision-language content style), or a dict whose `text`/`output`/
    `content` field is itself one of those — recurse to flatten."""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for block in value:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                inner = block.get("text")
                if inner is not None:
                    parts.append(_extract_text_blocks(inner))
        return "\n".join(parts)
    if isinstance(value, dict):
        for key in ("text", "output", "content"):
            if key in value and value[key] is not None:
                return _extract_text_blocks(value[key])
        return ""
    return ""


def _handle_openhands(obj, log_file) -> None:
    kind = obj.get("kind", "")
    source = obj.get("source", "")

    if kind == "SystemPromptEvent":
        # System prompt is large and not interesting per-event; skip.
        return

    if kind == "MessageEvent":
        text = _extract_text_blocks(obj.get("content") or obj.get("message", ""))
        text = _scrub_ansi(text).strip()
        if text:
            _emit(f"\n[{source or 'msg'}] {text[:400]}", log_file)
        return

    if kind == "ActionEvent":
        tool = obj.get("tool_name", "?")
        tool_call = obj.get("tool_call") or {}
        args_raw = tool_call.get("arguments", "")
        # `arguments` is a JSON string per OpenAI function-call convention.
        try:
            args = json.loads(args_raw) if isinstance(args_raw, str) else args_raw
        except (json.JSONDecodeError, TypeError):
            args = args_raw
        if isinstance(args, dict):
            shown = (
                args.get("command")
                or args.get("file_text")
                or args.get("path")
                or args.get("query")
                or json.dumps(args, ensure_ascii=False)
            )
        else:
            shown = str(args)
        shown = _scrub_ansi(str(shown)).replace("\n", " | ")[:300]
        _emit(f"\n[tool:{tool}] {shown}", log_file)
        return

    if kind == "ObservationEvent":
        out = _extract_text_blocks(obj.get("observation", ""))
        out = _scrub_ansi(out).strip()
        if len(out) > 400:
            out = out[:400] + "..."
        _emit(f"  => {out}", log_file)
        return

    if kind == "AgentErrorEvent":
        err = str(obj.get("error", ""))[:400]
        _emit(f"\n[!error] {err}", log_file)
        return

    # Unknown OpenHands kind — surface raw so we don't go dark
    raw = json.dumps(obj, ensure_ascii=False)[:200]
    _emit(f"\n[?oh:{kind}] {raw}", log_file)
