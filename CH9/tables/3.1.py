for i in range(2, 21):
    with open(f"table of {i}", "w") as f:
        for j in range(1, 11):
            f.write(f"{i}X{j} = {i*j}\n")
    with open(f"table of {i}", "r") as d:
        print(d.read())