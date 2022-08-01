import random


def userinput():
    inp = input("Enter snake(s) water(w) or gun(g) : ")
    while True:
        if inp == "s":
            return 1
            break
        elif inp == "w":
            return 2
            break
        elif inp == "g":
            return 3
            break
        else:
            inp = input("Enter between s , w & g : ")


def game(ui):
    ci = random.randint(1, 3)
    if ui == ci:
        print("Its a tie")
        return None
    elif (ui == 1 and ci == 2) or (ui == 2 and ci == 3) or (ui == 3 and ci == 1):
        print("You wins")
        return True
    else:
        print("You lose")
        return False
    # print(ui)
    # print(ci)


print("Welcome to Snake water and gun")
turns = input("type y for best of three or no for single match : ")
cs = 0
us = 0
if turns == 'y':

    while True:
        uii = userinput()
        score = game(uii)

        if score:
            us += 1
        elif score:
            cs += 1
        print(score)
        if cs == 3 or us == 3:
            break

    if us == 3:
        print("congrats you win")
    elif cs == 3:
        print("You lose, better luck next time")
    else:
        print("something went wrong")
    print(cs, us)
else:
    uii = userinput()
    game(uii)
