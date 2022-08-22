n = input("Enter a number: ")
while True:
    try:
        n = int(n)
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
        print("factorial = ", factorial)
        break
    except:
        n = input(print("Enter a number"))
# a = [8, 2, 3, -1, 7]
# mult = 1
# for i in a:
#     mult = mult * i
#
# print(mult)
