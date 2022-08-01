with open("twinkle.txt") as f:
    text = f.read()
text = text.lower()
if text.__contains__("twinkle"):
    print("File contains twinkle")
else:
    print("file dont contains twinkle")
