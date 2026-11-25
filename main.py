#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message entry.

Writes one commit message, 53 characters, for a fix that made things
worse: the alarm got silenced, the fire did not.
"""
import os

ENTRY = "fix: silenced the alarm, the fire is much quieter now"

# Gate from the competition rules: entry.txt must be UTF-8 text of
# 1 to 100 characters, not only white space. Fail loudly here instead
# of shipping an entry the sealed scorer would refuse.
MAX_CHARS = 100


def main():
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
