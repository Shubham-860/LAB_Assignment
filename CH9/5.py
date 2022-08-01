with open("sample.txt") as f:
    data = f.read()
words = ["monkey", "donkey"]

for word in words:
    while True:
        if word in data:
            data = data.replace(word, "####")
        else:
            break
with open("sample.txt", "w") as w:
    w.write(data)
print(data)