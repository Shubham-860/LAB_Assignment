# def hello():
#     print("Hello", name, "Have a nice day!")
#
#
# name = input("Enter your name : ")
# hello()

def rec(n):
    if n <= 1:
        return 1
    n = n * (rec(n - 1))
    return n


a = rec(int(input("Enter a number : ")))
print(a)
