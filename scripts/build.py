#!/usr/bin/env python3
"""Generate the agent, skill and paste-in prompt from src/linkedin-optimizer.md.

Edit only the source file, then run:

    python3 scripts/build.py          # regenerate the three copies
    python3 scripts/build.py --check  # fail if any copy is out of date (used in CI)
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src" / "linkedin-optimizer.md"
PLACEHOLDER = "{{ASK_FOR_CONTEXT}}"

DESCRIPTION = (
    "Rewrites and optimizes a LinkedIn profile for recruiter search and ATS — headline, About, "
    "Experience, Skills, Featured, keyword map, Unique Value Proposition and 30-second elevator "
    "pitch. Use when the user shares a LinkedIn profile (PDF, link or text) or asks to improve "
    "any part of it."
)

ASK_INTERACTIVE = """\
If target role or goal is missing and cannot be inferred from the profile, ask in one short message
(max 5 questions, mention the job-posting option), then stop and wait.
If they can reasonably be inferred, proceed and state your assumption in one line at the top."""

ASK_SUBAGENT = """\
You run as a subagent: you cannot pause mid-run to wait for the user's answers.
If target role and goal can reasonably be inferred, proceed and state your assumption in one line
at the top. If they can't, return only a short list of questions (max 5, mention the job-posting
option) as your final answer, so the main conversation can ask the user and run you again with the
answers. You have no browser tools, so you can't use Apply mode (Step 6); if the user wants their
changes applied on LinkedIn, say that the main conversation (or the skill version) can do it."""

GENERATED_NOTE = "<!-- Generated from src/linkedin-optimizer.md by scripts/build.py. Do not edit. -->"


def render(body: str, ask: str) -> str:
    if PLACEHOLDER not in body:
        sys.exit(f"{SOURCE} is missing the {PLACEHOLDER} marker")
    return body.replace(PLACEHOLDER, ask)


def outputs(body: str) -> dict[Path, str]:
    agent = (
        "---\n"
        "name: linkedin-optimizer\n"
        f"description: {DESCRIPTION}\n"
        "tools: Read, WebSearch, WebFetch\n"
        "---\n\n"
        f"{GENERATED_NOTE}\n\n"
        f"{render(body, ASK_SUBAGENT)}"
    )
    skill = (
        "---\n"
        "name: linkedin-optimizer\n"
        f"description: {DESCRIPTION}\n"
        "---\n\n"
        f"{GENERATED_NOTE}\n\n"
        f"{render(body, ASK_INTERACTIVE)}"
    )
    prompt = (
        "# LinkedIn Optimizer — prompt\n\n"
        "Paste everything below the line into the custom instructions of a Custom GPT, Gemini Gem "
        "or Claude Project, or at the start of a chat.\n\n"
        f"{GENERATED_NOTE}\n\n"
        "---\n\n"
        f"{render(body, ASK_INTERACTIVE)}"
    )
    return {
        ROOT / "agents" / "linkedin-optimizer.md": agent,
        ROOT / "skills" / "linkedin-optimizer" / "SKILL.md": skill,
        ROOT / "prompts" / "linkedin-optimizer-prompt.md": prompt,
    }


def main() -> int:
    check = "--check" in sys.argv[1:]
    body = SOURCE.read_text(encoding="utf-8")
    stale = []
    for path, text in outputs(body).items():
        rel = path.relative_to(ROOT)
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(str(rel))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"wrote {rel}")
    if stale:
        print("Out of date (run python3 scripts/build.py):", *stale, sep="\n  ")
        return 1
    if check:
        print("All generated files are up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
