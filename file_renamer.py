import os

folder = "."  # current folder
for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)
    new_name = "new_" + filename
    print(f"Would rename: {filename} -> {new_name}")

