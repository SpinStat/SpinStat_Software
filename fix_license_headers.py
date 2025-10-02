#!/usr/bin/env python3

import pathlib
import sys

LICENSE = "Apache-2.0"
COPYRIGHT = "Copyright (c) 2025 Benedikt Zinn"

# File extensions and filenames we want to process
FILE_TYPES = {
    ".c": "c-style",
    ".h": "c-style",
    ".cpp": "c-style",
    ".hpp": "c-style",
    ".py": "hash",
    ".sh": "hash",
}
SPECIAL_FILES = {
    "Makefile": "hash",
    "CMakeLists.txt": "hash",
    "prj.conf": "hash",
    "west.yml": "hash",
    "Kconfig": "hash",
}

def make_header(style: str) -> str:
    if style == "c-style":
        return f"""/*
 * SPDX-License-Identifier: {LICENSE}
 *
 * {COPYRIGHT}
 */
"""
    elif style == "hash":
        return f"""# SPDX-License-Identifier: {LICENSE}
# {COPYRIGHT}
"""
    else:
        raise ValueError(f"Unknown style: {style}")

def needs_header(lines: list[str]) -> bool:
    return not any("SPDX-License-Identifier" in line for line in lines[:5])

def process_file(path: pathlib.Path, style: str):
    try:
        text = path.read_text(encoding="utf-8").splitlines(keepends=True)
    except Exception as e:
        print(f"Skipping {path} (could not read: {e})")
        return

    if needs_header(text):
        print(f"➕ Adding header to {path}")
        header = make_header(style).splitlines(keepends=True)
        new_text = header + ["\n"] + text
        path.write_text("".join(new_text), encoding="utf-8")
    else:
        print(f"-> {path} already has SPDX header")

def main():
    root = pathlib.Path(".")
    for path in root.rglob("*"):
        if not path.is_file():
            continue

        style = None
        if path.suffix in FILE_TYPES:
            style = FILE_TYPES[path.suffix]
        elif path.name in SPECIAL_FILES:
            style = SPECIAL_FILES[path.name]

        if style:
            process_file(path, style)

    print("\nrun: reuse lint")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

