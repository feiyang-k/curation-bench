"""Patch openhands SDK's llm.py to add a Qwen3-style XML->tool_calls
fallback when a native-FC response comes back with empty tool_calls but
the message content embeds the tool call as XML.

Together AI's Qwen3.5-397B-A17B endpoint degrades under long context and
emits tool calls as XML inside `content` instead of the native
`tool_calls` field. OpenHands' response_dispatch then reads "no tool
calls = agent finished" and silently terminates the run.

Observed malformed shapes:
    Form A: <function=NAME><parameter=K>V</parameter>...</function>
    Form B: <tool_call><NAME><parameter=K>V</parameter>...</function></tool_call>
            (bare tag, no `function=` prefix, wrapped in <tool_call>)
    Form D: any of the above TRUNCATED mid-output (oversized tool call hits
            the provider's max output tokens) -> no closing </function>,
            last <parameter= has no </parameter>.

Parser strategy (not whack-a-mole):
  * tool name = the tag immediately before the first <parameter= block
    (lookahead anchor). The `function=` prefix and the <tool_call>
    wrapper are both volatile and tolerated.
  * </function> is OPTIONAL (`(?:</function>|$)`) so a truncated tool call
    is still recovered -- the agent then gets a normal tool error to
    retry on, instead of a silent run-ending "Agent finished".
  * </parameter> is likewise optional, so the last (truncated) parameter
    is still captured.

Run at image build time:
    python3 openhands_xml_fallback_patch.py
"""

from __future__ import annotations

import pathlib
import py_compile
import sys

LLM_PY = pathlib.Path(
    "/opt/uv-tools/openhands/lib/python3.12/site-packages/openhands/sdk/llm/llm.py"
)

ANCHOR = """            raw_resp: ModelResponse | None = None
            if use_mock_tools:
                raw_resp = copy.deepcopy(resp)
                resp = self.post_response_prompt_mock(
                    resp,
                    nonfncall_msgs=formatted_messages,
                    tools=cc_tools,
                    include_security_params=add_security_risk_prediction,
                )
"""

ADDITION = """            elif (
                cc_tools
                and resp.choices
                and getattr(resp.choices[0].message, "tool_calls", None) is None
                and getattr(resp.choices[0].message, "content", None)
            ):
                # XML-in-content fallback for native-FC providers that return
                # Qwen3-style tool calls as XML embedded in message content
                # instead of populating the native tool_calls field.
                #
                #   Form A: <function=NAME><parameter=K>V</parameter>...</function>
                #   Form B: <tool_call><NAME>...<parameter=K>V</parameter>...</function></tool_call>
                #   Form D: any of the above truncated mid-output (no closing tags)
                #
                # Tool name is position-anchored: the tag immediately before
                # the first <parameter= block. </function> and </parameter>
                # are optional so truncated tool calls are still recovered
                # (agent gets a tool error to retry on, not a silent finish).
                import re as _re_xfb
                import json as _json_xfb
                import uuid as _uuid_xfb
                _c_xfb = resp.choices[0].message.content
                _cs_xfb = _re_xfb.sub(r"</?tool_call>\\s*", "", _c_xfb)
                _matches_xfb = list(
                    _re_xfb.finditer(
                        r"<(?:function=)?([a-zA-Z_][\\w-]*)>\\s*"
                        r"(?=<parameter=)(.*?)(?:</function>|$)",
                        _cs_xfb,
                        _re_xfb.DOTALL,
                    )
                )
                if not _matches_xfb:
                    # no-parameter fallback: strict, requires </function>
                    _matches_xfb = list(
                        _re_xfb.finditer(
                            r"<function=([a-zA-Z_][\\w-]*)>\\n?(.*?)</function>",
                            _cs_xfb,
                            _re_xfb.DOTALL,
                        )
                    )
                if _matches_xfb:
                    from litellm.types.utils import (
                        ChatCompletionMessageToolCall as _TC_xfb,
                        Function as _Fn_xfb,
                    )
                    _tcs_xfb = []
                    for _m_xfb in _matches_xfb:
                        _params_xfb: dict[str, str] = {}
                        for _pm_xfb in _re_xfb.finditer(
                            r"<parameter=([^>]+)>(.*?)"
                            r"(?:</parameter>|(?=<parameter=)|$)",
                            _m_xfb.group(2),
                            _re_xfb.DOTALL,
                        ):
                            _params_xfb[_pm_xfb.group(1).strip()] = (
                                _pm_xfb.group(2).strip()
                            )
                        _tcs_xfb.append(
                            _TC_xfb(
                                id=f"call_{_uuid_xfb.uuid4().hex[:8]}",
                                type="function",
                                function=_Fn_xfb(
                                    name=_m_xfb.group(1).strip(),
                                    arguments=_json_xfb.dumps(_params_xfb),
                                ),
                            )
                        )
                    raw_resp = copy.deepcopy(resp)
                    resp.choices[0].message.tool_calls = _tcs_xfb
                    _mark_xfb = _re_xfb.search(
                        r"<tool_call>|<function=|<[a-zA-Z_][\\w-]*>\\s*<parameter=",
                        _c_xfb,
                    )
                    _prefix_xfb = (
                        _c_xfb[: _mark_xfb.start()].strip() if _mark_xfb else ""
                    )
                    resp.choices[0].message.content = _prefix_xfb or None
                    logger.info(
                        "LLM.completion: XML-fallback recovered %d tool call(s) "
                        "from Qwen3-style XML in content "
                        "(native_tool_calling=True)",
                        len(_tcs_xfb),
                    )
"""


def main() -> int:
    src = LLM_PY.read_text()
    if "XML-fallback recovered" in src:
        print("✓ XML-fallback patch already applied; skipping.")
        return 0
    if ANCHOR not in src:
        print(
            "✗ XML-fallback anchor not found in llm.py - upstream layout changed.",
            file=sys.stderr,
        )
        return 1
    patched = src.replace(ANCHOR, ANCHOR + ADDITION, 1)
    LLM_PY.write_text(patched)
    try:
        py_compile.compile(str(LLM_PY), doraise=True)
    except py_compile.PyCompileError as e:
        LLM_PY.write_text(src)
        print(
            f"✗ Patched llm.py failed to compile; reverted. Error: {e}",
            file=sys.stderr,
        )
        return 2
    print("✓ XML-fallback patch applied to llm.py and compiles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
