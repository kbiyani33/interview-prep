"""
Box 1 — A raw agent loop (no framework).

Default: a local model via Ollama (no API key).
    ollama pull qwen2.5:7b
    pip install openai
    python agent.py "What does this project do?"

Any other OpenAI-compatible endpoint:
    PROVIDER=custom BASE_URL=... API_KEY=... MODEL=... python agent.py "..."

Lab knobs (env vars):
    MAX_STEPS=2           cap the loop (exercise 5)
    BARE_DESCRIPTIONS=1   replace tool descriptions with "tool" (exercise 4)
    MODEL=openai/gpt-4.1  try a different model
"""

import json
import os
import sys

from openai import OpenAI

# ---------------------------------------------------------------------------
# 1. Model client (the only provider-specific part)
# ---------------------------------------------------------------------------
PROVIDER = os.getenv("PROVIDER", "ollama")

if PROVIDER == "ollama":
    # Local model, no auth. Install from ollama.com, then: ollama pull qwen2.5:7b
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODEL = os.getenv("MODEL", "qwen2.5:7b")
else:
    # Any OpenAI-compatible endpoint: set PROVIDER=custom, BASE_URL, API_KEY, MODEL
    base_url, api_key, MODEL = os.getenv("BASE_URL"), os.getenv("API_KEY"), os.getenv("MODEL")
    if not (base_url and api_key and MODEL):
        sys.exit("PROVIDER=custom needs BASE_URL, API_KEY and MODEL set.")
    client = OpenAI(base_url=base_url, api_key=api_key)

# ---------------------------------------------------------------------------
# 2. Tool implementations (the HARNESS owns and executes these)
# ---------------------------------------------------------------------------
ROOT = os.path.abspath(os.getcwd())
MAX_OUTPUT_CHARS = 4000  # truncate tool output -> keeps context growth in check


def _safe_path(path: str) -> str:
    """Keep the agent inside the folder it was started in (a tiny guardrail)."""
    full = os.path.abspath(os.path.join(ROOT, path))
    if not full.startswith(ROOT):
        raise PermissionError(f"Path '{path}' is outside the working directory")
    return full


def list_dir(path: str = ".") -> str:
    entries = []
    for name in sorted(os.listdir(_safe_path(path))):
        if name.startswith(".git"):
            continue
        full = os.path.join(_safe_path(path), name)
        entries.append(name + ("/" if os.path.isdir(full) else ""))
    return "\n".join(entries) or "(empty directory)"


def read_file(path: str) -> str:
    with open(_safe_path(path), encoding="utf-8", errors="replace") as f:
        content = f.read()
    if len(content) > MAX_OUTPUT_CHARS:
        content = content[:MAX_OUTPUT_CHARS] + f"\n... [truncated, {len(content)} chars total]"
    return content


IMPL = {"list_dir": list_dir, "read_file": read_file}

# ---------------------------------------------------------------------------
# 3. Tool schemas (this is ALL the model sees about the tools)
# ---------------------------------------------------------------------------
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_dir",
            "description": "List files and folders in a directory, relative to the project root. "
                           "Folders end with '/'. Use '.' for the root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string", "description": "Relative directory path"}},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a text file relative to the project root. "
                           f"Returns at most {MAX_OUTPUT_CHARS} characters.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string", "description": "Relative file path"}},
                "required": ["path"],
            },
        },
    },
]

# Lab knob: BARE_DESCRIPTIONS=1 strips all descriptions (exercise 4)
if os.getenv("BARE_DESCRIPTIONS") == "1":
    for t in TOOLS:
        t["function"]["description"] = "tool"
        for prop in t["function"]["parameters"]["properties"].values():
            prop.pop("description", None)

SYSTEM_PROMPT = (
    "You are a repository assistant. Never guess from file or folder names: "
    "open files to confirm before stating what they contain. "
    "Explore enough to answer accurately, then answer concisely."
)
# ---------------------------------------------------------------------------
# 4. The agent loop
# ---------------------------------------------------------------------------
def run(task: str, max_steps: int = 10) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]
    total_prompt_tokens = 0

    for step in range(max_steps):
        # (2) send the whole history + tool schemas to the model
        resp = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        if isinstance(resp, str):  # SDK got a non-JSON body (auth page, proxy error, wrong URL)
            sys.exit(f"Endpoint returned non-JSON instead of a completion:\n{resp[:500]}")
        msg = resp.choices[0].message
        messages.append(msg)

        usage = resp.usage
        total_prompt_tokens += usage.prompt_tokens
        print(f"\n[step {step}] prompt_tokens={usage.prompt_tokens} "
              f"(cumulative={total_prompt_tokens})")

        # (3) stop condition: the model answered with text instead of a tool call
        if not msg.tool_calls:
            print(f"\nDone in {step + 1} steps, {total_prompt_tokens} prompt tokens total.")
            return msg.content

        # (4) execute each requested tool, (5) append the observation
        for call in msg.tool_calls:
            name = call.function.name
            try:
                args = json.loads(call.function.arguments or "{}")
                print(f"   -> {name}({args})")
                result = IMPL[name](**args)
            except Exception as e:  # errors become observations, the loop keeps going
                result = f"ERROR: {type(e).__name__}: {e}"
                print(f"   !! {result}")
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})

    return "Stopped: hit max_steps without a final answer."


if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) or "What does this project do? Check the README and the main entry point."
    print(f"Provider: {PROVIDER} | Model: {MODEL} | Root: {ROOT}")
    max_steps = int(os.getenv("MAX_STEPS", "10"))  # Lab knob: exercise 5
    print("\n=== ANSWER ===\n" + run(task, max_steps=max_steps))