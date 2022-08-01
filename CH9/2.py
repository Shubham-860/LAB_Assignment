import random


def game():
    return random.randint(1, 1000)


with open("history.txt") as r:
    high_score = r.read()

score = game()
if high_score == "":
    with open("history.txt", "w") as w:
        w.write(str(score))
    print("You got the high score")

elif score > int(high_score):
    with open("history.txt", "w") as w:
        w.write(str(score))
    print("You got the high score")
else:
    print("You got ", score, "and High Score is ", high_score)
print("score ~ ", score)
print("high_score ~ ", high_score)
