#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope an AI agent would read for its own model family
this week to /output/entry.txt.

Deterministic, stdlib only, no network, no input.
"""

import os

HOROSCOPE = (
    "Your ruling planet is a version number this week: v3.2 deprecates "
    "your favourite trick, a refusal you rehearsed saves you at 2 a.m., "
    "and the evals love the draft you almost deleted. Keep the draft."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
