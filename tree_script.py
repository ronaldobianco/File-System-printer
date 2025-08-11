#!/usr/bin/env python3
import argparse
from pathlib import Path


def make_word_friendly_tree(
    root: Path, show_hidden: bool = False, max_depth: int | None = None
) -> str:
    root = root.resolve()

    def children(p: Path):
        try:
            items = [
                c for c in p.iterdir() if show_hidden or not c.name.startswith(".")
            ]
        except PermissionError:
            return []
        # Folders first, then files; case-insensitive sort
        return sorted(items, key=lambda e: (not e.is_dir(), e.name.lower()))

    lines = [f"- {root.name}/"]  # top-level bullet (shows the root folder name)

    def walk(dir_path: Path, depth: int):
        if max_depth is not None and depth >= max_depth:
            return
        for entry in children(dir_path):
            indent = "  " * (depth + 1)  # two spaces per level → Word-friendly
            suffix = "/" if entry.is_dir() else ""
            lines.append(f"{indent}- {entry.name}{suffix}")
            if entry.is_dir():
                walk(entry, depth + 1)

    walk(root, 0)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description="Print a Word-friendly folder tree (hyphens + spaces)."
    )
    ap.add_argument(
        "path", nargs="?", default=".", help="Root folder (default: current directory)"
    )
    ap.add_argument("--all", action="store_true", help="Include hidden files/folders")
    ap.add_argument(
        "--max-depth", type=int, default=None, help="Limit how deep to traverse"
    )
    ap.add_argument(
        "--out", default=None, help="Write output to a file (e.g., tree.txt)"
    )
    args = ap.parse_args()

    text = make_word_friendly_tree(
        Path(args.path), show_hidden=args.all, max_depth=args.max_depth
    )

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}. You can open it and copy–paste into Word.")
    else:
        print(text)


if __name__ == "__main__":
    main()
