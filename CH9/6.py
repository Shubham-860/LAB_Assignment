with open("log.txt") as f:
    data = f.read()
if data.lower().__contains__("python"):
    print("Log file contain python")
else:
    print("Log file does not contain python")
