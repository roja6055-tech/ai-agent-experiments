"""A tiny deterministic tool-using agent built with the Python standard library.

Run: python src/agent.py
This illustrates an agent/tool loop without an LLM or API key.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Tool:
    name: str
    description: str
    run: Callable[..., str]


PROJECT_NOTES = {
    "sample model review": (
        "The fictional sample model review is in progress. "
        "Next step: validate required fields and summarize exceptions."
    )
}


def add_numbers(a: float, b: float) -> str:
    return f"The sum is {a + b:g}."


def lookup_project_note(topic: str) -> str:
    normalized = topic.strip().lower()
    if normalized not in PROJECT_NOTES:
        return "No matching note was found in the demo knowledge base."
    return PROJECT_NOTES[normalized]


TOOLS: dict[str, Tool] = {
    "add_numbers": Tool("add_numbers", "Add two numbers.", add_numbers),
    "lookup_project_note": Tool(
        "lookup_project_note", "Look up a fictional project note.", lookup_project_note
    ),
}


def choose_tool(user_request: str) -> tuple[str, dict[str, Any]] | None:
    """Simple intent router; an LLM planner could replace this function later."""
    addition = re.search(
        r"add\s+(-?\d+(?:\.\d+)?)\s+and\s+(-?\d+(?:\.\d+)?)",
        user_request,
        flags=re.IGNORECASE,
    )
    if addition:
        return "add_numbers", {
            "a": float(addition.group(1)),
            "b": float(addition.group(2)),
        }

    if "status" in user_request.lower() or "review" in user_request.lower():
        return "lookup_project_note", {"topic": "sample model review"}

    return None


def run_agent(user_request: str) -> str:
    """Select one registered tool, execute it, and return its observation."""
    selection = choose_tool(user_request)
    if selection is None:
        return (
            "I couldn't map that request to an available demo tool. "
            "Try 'Add 18 and 24' or ask for the sample model review status."
        )

    tool_name, arguments = selection
    tool = TOOLS[tool_name]
    observation = tool.run(**arguments)
    return f"Tool used: {tool.name}\nObservation: {observation}"


def main() -> None:
    print("Tiny Tool-Using Agent")
    print("Try: Add 18 and 24")
    print("Try: What is the status of the sample model review?")
    request = input("\nYour request: ").strip()
    print("\n" + run_agent(request))


if __name__ == "__main__":
    main()
