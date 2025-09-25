"""
file_renamer.py

A simple script to rename files in the current folder.

Current behavior:
- Only renames files with the .txt extension.
- Adds "new_" as a prefix to the filename.
- Skips folders (e.g., .git) and non-.txt files.

Usage:
    python file_renamer.py

Notes:
- Dry-run mode prints what *would* happen.
- To actually rename, uncomment the line with p.rename(...).
"""
from pathlib import Path

folder = Path(".")
for p in folder.iterdir():
    if not p.is_file():
        continue  # skip folders like .git
    if p.suffix != ".txt":
        continue  # only touch .txt files
    new_name = "new_" + p.name
    print(f"Renaming: {p.name} -> {new_name}")
    # Uncomment the line below to actually rename
    p.rename(p.with_name(new_name))
