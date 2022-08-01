# 1
# def greater():
#     if a >= b and a >= c:
#         print(a, " is greater number")
#     elif b >= a and b >= c:
#         print(b, " is greater number")
#     else:
#         print(c, " is greater number")
#
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# greater()

# 2

# (°C × 9/5) + 32 = °F
# def far(c):
#     f = (c * (9 / 5)) + 32
#     print(c, "Celsius = ", f, "Fahrenheit")
#
#
# c = float(input("Enter temperature in celsius: "))
# far(c)


# 3

# print("Hello", end="")
# print(" Shubham")

# 4

# def natural(n):
#     if n <= 1:
#         return 1
#     n = n + natural(n - 1)
#     return n
#
#
# no = int(input("Enter a number: "))
# print("Sum ~ ", natural(no))


# 5

# def pattern(n):
#     for i in range( n + 1):
#         print("*" * (n - i), end="")
#         print(" ")
#
#
# line = int(input("Enter number of lines"))
# pattern(line)

# 6

# def cm(inch):
#     print(f"{inch} inch = {inch * 2.54} cm")
#
#
# cm(int(input("Enter inch : ")))


# 7

def removeAdnStrip(st, word):
    sta = st.replace(word, "")
    return sta.strip()


st = "  Hello, my name is Shubham"
word = "Shubham"

a = removeAdnStrip(st, word)
print(a)

# 8

# def table(n):
#     for i in range(1, 11):
#         print(f"{n}X{i}={i * n}")
#
#
# table(int(input("Enter number")))


# def multiple(n):
#     mul = 1
#     for i in n:
#         mul *= i
#     return mul
#
#
# a = int(input("Enter amount of numbers : "))
# n = []
# for i in range(a):
#     n.append(int(input("Enter number : ")))
#
# print("multiplication = ", multiple(n))
