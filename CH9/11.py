import os

with open("copy.txt") as f:
    data = f.read()
with open("rename.txt", "w") as n:
    n.write(data)
os.remove("copy.txt")

# os.renames("rename.txt", "renameWithOS.txt")
