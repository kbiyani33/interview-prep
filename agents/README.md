AI Agents & MCP — Learning Lab

Learning AI agents and the Model Context Protocol (MCP) one box at a time, the same way I worked through system design patterns. Each box has runnable code, hand-drawn Excalidraw diagrams, and an interview question I can answer out loud.

Goal: be confident in applied AI interviews on both theory ("why does X work this way?") and practice ("build / debug it").

Roadmap
#	Box	Build / Understand	Status
1	The agent loop	Raw agent in ~100 lines of Python, no framework	⬜
2	Tool design	Schemas, descriptions, errors as observations, idempotency, tool count vs. accuracy	⬜
3	Context & memory	Context window as RAM, compaction, session vs. long-term memory	⬜
4	Workflows vs. agents	Chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer	⬜
5	MCP fundamentals	N×M problem, host/client/server, tools/resources/prompts, JSON-RPC, stdio vs. streamable HTTP	⬜
6	MCP in production	Remote servers, OAuth, gateways, tool poisoning, prompt injection, confused deputy	⬜
7	Multi-agent	Subagents, context isolation, handoffs, A2A	⬜
8	Evals & observability	Traces, trajectory evals, LLM-as-judge, regression suites	⬜
9	Guardrails	Input/output filters, permission tiers, human-in-the-loop	⬜
10	Capstone	Box 1 agent whose tools come from my own MCP server	⬜

Status: ⬜ not started · 🟨 in progress · ✅ done (code run + diagrams drawn + interview Q answered)

Folder layout
agents/
├── README.md                  ← this file
├── box-01-agent-loop/
│   ├── agent.py               ← runnable code
│   ├── NOTES.md               ← my notes, trace observations, interview answer
│   └── diagrams/              ← Excalidraw exports (.excalidraw + .png)
├── box-02-tool-design/
└── ...

Every box folder follows the same structure: code → NOTES.md → diagrams/.

Setup (GitHub Codespaces — no API key needed)

Codespaces sets GITHUB_TOKEN automatically, and it works with GitHub Models (OpenAI-compatible API).

bash
# open this repo in a Codespace, then:
pip install openai
# run from the repo root — the agent explores whatever folder you start it in
python agents/box-01-agent-loop/agent.py "What does this repo contain and how is it organised?"
Default model: openai/gpt-4o-mini via https://models.github.ai/inference
Local alternative: PROVIDER=ollama python agents/box-01-agent-loop/agent.py "..." (needs Ollama + qwen2.5:7b)
Stop the Codespace when done — free hours are monthly.
Excalidraw conventions

Same legend in every diagram so they read as one series.

Element	Shape / colour	Meaning
LLM	Purple rounded rectangle	The model — stateless, only produces text or JSON
Harness / runtime	Blue rectangle	My code: the loop, parsing, executing
Tools / external systems	Green rectangle	Filesystem, APIs, DBs, MCP servers
State / context	Yellow stacked rectangles	Message list, memory, caches
User	Grey circle / stick figure	The human
Trust boundary	Red dashed rectangle	Where untrusted data enters
Solid arrow	—	Call / request
Dashed arrow	—	Result / observation / response
①②③ on arrows	—	Order of execution

Rule: if I can't explain a diagram out loud in 60 seconds, it has too much on it — split it.

Per-box checklist
[ ] Code runs and I've read the trace
[ ] Exercises done, observations written in NOTES.md
[ ] Diagrams drawn and exported to diagrams/
[ ] Interview question answered out loud (and written in NOTES.md)
Interview questions bank

Collected as I go — one per box, answer lives in that box's NOTES.md.

Box 1: Why does an agent's token cost grow faster than linearly with the number of steps, and how do you mitigate it?