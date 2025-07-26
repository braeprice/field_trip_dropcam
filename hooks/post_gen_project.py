import os

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename == ".gitkeep":
            filepath = os.path.join(root, filename)
            os.remove(filepath)