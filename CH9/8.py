with open("sample.txt") as f:
    with open("copy.txt", "w") as w:
        w.write(f.read())

print()
