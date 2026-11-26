#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun entry.

Writes the two-line warning to /output/entry.txt.
"""
import os

ENTRY = (
    "When Dad asks you to stay for dinner on your last night home in 2019, say yes.\n"
    "You will fly out at dawn, and for the next six years every takeoff will put that empty chair back beside you.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
