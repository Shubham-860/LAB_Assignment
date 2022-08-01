with open("sample.txt") as f:
    with open("copy.txt") as c:
        if f.read() == c.read():
            print("The data is identical")
        else:
            print("The data is not identical")
