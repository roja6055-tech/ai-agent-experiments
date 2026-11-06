# AI Agent Experiments

Small, explainable experiments exploring AI-agent patterns, automation, tool use, and evaluation.

The first experiment is a **minimal tool-using agent** written with Python's standard library. It demonstrates a basic control loop: interpret a request, select an allowed tool, execute it, and return an observation. It uses deterministic routing rather than an LLM so the mechanics are transparent and it runs without API keys.

> **Status:** Learning starter project, not a production agent framework.

## First experiment: a tiny tool-using agent

Available tools:
- `add_numbers`: adds two numeric inputs.
- `lookup_project_note`: retrieves a fictional note from an in-memory knowledge base.

Run it:

```bash
python src/agent.py
```

Try:
- `Add 18 and 24`
- `What is the status of the sample model review?`

## What this demonstrates
- An explicit tool registry.
- Simple request routing.
- Tool input validation.
- Separation of routing logic and tool implementation.
- Why bounded permissions and human oversight matter.

## Roadmap
- Add an LLM-backed planner behind a defined interface.
- Add structured schemas for tool arguments.
- Add human approval for consequential actions.
- Add tracing, latency and success-rate evaluation.
- Explore retrieval-augmented generation (RAG).
- Explore an agent that calls a privacy-preserving compute service without access to secret keys.

## Safety principles
- Give agents the minimum tool permissions they need.
- Validate tool inputs and outputs.
- Require human approval before external or irreversible actions.
- Keep secrets in environment variables or a secrets manager; never commit API keys.
- Use synthetic data in public examples.

Independent experiments in AI-assisted software development, practical automation, data workflows, and agent evaluation.
