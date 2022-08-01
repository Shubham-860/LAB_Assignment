with open("tables.txt", "a") as f:
    for j in range(2, 21):
        f.write(str(str(j) + " = "))
        for i in range(1, 11):
            f.write(str(i * j)+",")
        f.write("\n")
