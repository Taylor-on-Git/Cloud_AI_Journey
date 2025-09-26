from pathlib import Path  # pathlib makes file/folder handling clean and safe

# Work in the current folder (".")
folder = Path(".")

# Ask the user what prefix to add (e.g., "new_", "final_", etc.)
prefix = input("Enter a prefix to add: ")

# Loop through every item in the folder
for p in folder.iterdir():
    if not p.is_file():
        continue  # skip directories (e.g., .git folder)

    if p.suffix != ".txt":
        continue  # only rename .txt files for safety

    if p.name.startswith(prefix):
        continue  # skip files already renamed with this prefix (avoid double-renaming)

    # Build the new filename by adding the prefix
    new_name = prefix + p.name

    # Show what is happening
    print(f"Renaming: {p.name} -> {new_name}")

    # Actually rename the file
    p.rename(p.with_name(new_name))