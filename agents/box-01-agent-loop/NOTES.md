# Box 1 — The Agent Loop
 
## Core idea (in my own words)
 
> An LLM is a stateless function: `f(messages, tool_schemas) → text OR tool_call JSON`.
> The model decides; the harness executes.
> Agent = LLM + tools + loop + state (message list) + stop condition.
 
_Rewrite this after running the code, in my own words._
 
---
 
## Run log
 
**Repo explored:**
**Model:**
**Task given:**
 
```
(paste the trace here — the [step N] and -> lines)
```
 
**Steps taken:**     **Total prompt tokens:**
 
---
 
## Exercises
 
### 1. Watch the trace
What order did it explore in? Did it read anything unnecessary?
 
### 2. Token growth
| Step | prompt_tokens | cumulative |
|------|---------------|------------|
| 0 | | |
| 1 | | |
| 2 | | |
 
Observation:
 
### 3. Broken tool (ask it to read a missing file / `/etc/passwd`)
What did the model do after seeing `ERROR`?
 
### 4. Starved descriptions (set both descriptions to `"tool"`)
How did the trace change?
 
### 5. `max_steps=2`
What happened? What would a good fallback answer look like?
 
### Bonus: GitHub Models vs. Ollama
Differences in tool-call quality:
 
---
 
## Interview question
 
**Q: Why does an agent's token cost grow faster than linearly with the number of steps, and how do you mitigate it?**
 
My answer:
 
---
 
## Diagrams
 
- [ ] 1.1 The agent loop → `diagrams/1.1-agent-loop.png`
- [ ] 1.2 Responsibility boundary (LLM vs. harness) → `diagrams/1.2-boundary.png`
- [ ] 1.3 Quadratic context growth → `diagrams/1.3-context-growth.png`
---
 
## Open questions / things that surprised me
 
-
 