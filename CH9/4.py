with open("sample.txt") as f:
    data = f.read()
while True:
    if "donkey" in data:
        data = data.replace("donkey", "####")
    else:
        break
with open("sample.txt", "w") as w:
    w.write(data)
