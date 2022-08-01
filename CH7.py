# no = [0]
# for i in range(5):
#     no.append(int(input("Enter a number: ")))
#
# print(no)

##

# no = 1
# a = None
# for i in range(5):
#     a = int(input("Enter a number:"))
#     while a == 0:
#         print("you can't enter zero")
#         a = int(input("Enter a number:"))
#     no = no*a
# print(no)
#

##

# 1

# no = int(input("Enter a number:"))
# for i in range(1, 11):
#     # print(no, " * ", i, " = ", no * i)
#     print(f"{no} X {i} = {i*no}")


# 2

# l1 = ["harry", "sohan", "sachin", "rahul", "Shubham"]
# for a in l1:
#     if a.lower().startswith("s"):
#         print(f"Hello {a}")

# 3

# i = 1
# no = int(input("Enter a number:"))
# while i <= 10:
#     print(f"{no} X {i} = {i * no}")
#     i += 11


# 4

#
# no = int(input("Enter a number:"))
# prime = True
# for i in range(2, no):
#     if no % i == 0:
#         prime = False
# if prime:
#     print("Given number is prime number")
# else:
#     print("Given number is not prime number")


# 5

# no = int(input("Enter a number:"))
# Sum = i = 0
# while i <= no:
#     Sum = i + Sum
#     i += 1
# print(Sum)

# 6

# no = int(input("Enter a number:"))
# fac = 1
# for a in range(1, no+1):
#     fac = fac * a
# print(fac)

# 7
# n = 3
# for i in range(4):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i + 1), end="")
#     print()

# 8

# for a in range(4):
#     print("*"*(a+1))

# 8

# for i in range(3):
#     print("*", end="")
#     if i == 1:
#         print(" ", end="")
#     else:
#         print("*", end="")
#     print("*")

# 9
a = input("Enter a number: ")
while True:

    try:
        a = int(a)
        mu = []
        for i in range(1, 11):
            mu.append(f"{a}X{i}={a * i}")
        for m in mu:
            print(m)
        break
    except:
        a = input("Enter number: ")
