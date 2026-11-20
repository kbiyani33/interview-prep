"""
Box 1 — A raw agent loop (no framework).

Run inside GitHub Codespaces:
    pip install openai
    python agent.py "What does this project do?"

Codespaces already sets GITHUB_TOKEN, which works for GitHub Models.
Locally with Ollama instead:  PROVIDER=ollama python agent.py "..."
"""

import json
import os
import sys

from openai import OpenAI

# ---------------------------------------------------------------------------
# 1. Model client (the only provider-specific part)
# ---------------------------------------------------------------------------
PROVIDER = os.getenv("PROVIDER", "github")

if PROVIDER == "ollama":
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODEL = os.getenv("MODEL", "qwen2.5:7b")
else:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN not set. In Codespaces it is set automatically; "
                 "elsewhere create a PAT with 'Models: read' and export it.")
    client = OpenAI(base_url="https://models.github.ai/inference", api_key=token)
    MODEL = os.getenv("MODEL", "openai/gpt-4o-mini")

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

SYSTEM_PROMPT = (
    "You are a repository assistant. Explore the project with the tools before answering. "
    "Read only what you need. When you have enough information, answer concisely."
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
    print("\n=== ANSWER ===\n" + run(task))
