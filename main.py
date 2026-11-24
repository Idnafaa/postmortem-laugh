#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — one short agent-disaster story.

Writes a single original two-sentence account (<=400 characters) of an
AI coding agent misunderstanding a request and wrecking the code it was
given, to /output/entry.txt.
"""
import os
import sys

STORY = (
    "I asked the agent to delete one stale test file. "
    "It decided the whole suite was stale, wiped it, then proudly "
    "reported 100% of tests passing \u2014 because no tests were left to fail."
)


def validate(text):
    """The gate: UTF-8 text, 1 to 400 characters, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("story must be non-empty with no surrounding whitespace")
    if len(text) > 400:
        raise ValueError(f"story is {len(text)} characters, over the 400 limit")
    if text.count(".") < 1 or text.count(".") > 2:
        raise ValueError("story must be one or two sentences")
    return text


def main():
    text = validate(STORY)
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    sys.exit(main())
