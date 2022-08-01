import math
import os


# print("Hello again!")

# print(os.listdir())

# no = int(input("Enter a number"))
# print("Square ~ ", no * no)
# print("Square root ~ ", math.sqrt(no))

# a = int(input("Enter no 1\n"))
# b = int(input("Enter no b\n"))
# print("Average is ", (a + b) / 2)

# sentence = "Hello    Ny name   is              Shubham"
# while sentence.__contains__("  "):
#     sentence = sentence.replace("  ", " ")
# print(sentence)


# a = [1, 3, 5, 7]
# Sum = 0
# for i in a:
#     Sum += i
# print(Sum)

# b = [23, 54, 76, 98, 0, 0, 65, 0]
# print(b.count(0))
# b.sort()
# print(b)


# s = {}
# print(type(s))

# s = [1, {23, 54, 76, 98}]
# s.append(34)
# print(s.__len__())

# a = []
# for i in range(4):
#     a.append(int(input("enter number: ")))
#
# if (a[0] >= a[1]) and (a[0] >= a[2]) and (a[0] >= a[3]):
#     print(a[0], " is Greater")
# elif (a[1] >= a[2]) and (a[1] >= a[3]):
#     print(a[1], " is Greater")
# elif a[2] >= a[3]:
#     print(a[2], " is Greater")
# else:
#     print(a[3], " is Greater")


# post = "asklfbkuydfl b habfckbaf harry "
#
# if post.lower().__contains__("harry"):
#     print("Post is contains name harry")
# else:
#     print("no post does not contain name harry")

# no = int(input("enter number for table : "))
# for i in range(10):
#     print(f"{no} X {i + 1} = {no * i}")

# n = 4
# for i in range(4):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i + 1))

# def MT(no):
#     for i in range(1, 11):
#         print(f"{no}X{i}={i * no}")
#
#
# MT(int(input("Enter a number : ")))


# with open("Try.txt", "w") as f:
#     f.write("")

class Employee:
    def __init__(self, name, age, workExp, post, gender):
        self.name = name
        self.age = age
        self.workExp = workExp
        self.post = post
        self.gender = gender
        if gender == "male":
            self.t1 = "He"
            self.t2 = "His"
        if gender == "female":
            self.t1 = "She"
            self.t2 = "Her"
        company = "Microsoft"

    def Show(self):
        print(f"The name of employee is {self.name}, and {self.t2.lower()} age is {self.age} Years.\n"
              f"{self.t2} work experience is {self.workExp}, Now {self.t1.lower()} is in {self.post}'s post")


name = "Shubham"
age = 22
workExp = "1 year"
post = "manager"
gender = "male"

Shub = Employee(name, age, workExp, post, gender)
Shub.Show()
