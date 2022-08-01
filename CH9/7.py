data = True
i = 1
with open("log.txt") as f:
    while data:
        data = f.readline()
        if data.lower().__contains__("python"):
            print(f"on page no {i} Log file contain python")
        i += 1
print("finished")