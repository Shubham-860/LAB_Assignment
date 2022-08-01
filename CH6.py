# 1

# a = []
# for i in range(4):
#     a.append(int(input("inter a number")))
# if (a[0] >= a[1]) and (a[0] >= a[2]) and (a[0] >= a[3]):
#     print(a[0], "~ is the greater")
# elif(a[1] >= a[2]) and (a[1] >= a[3]):
#     print(a[1], "~ is the greater")
# elif a[2] >= a[3]:
#     print(a[2], "~ is the greater")
# else:
#     print(a[3], "~ is the greater")

# 2

# a = []
# for i in range(3):
#     a.append(int(input("Enter marks\n")))
#
# avg = (a[0] + a[1] + a[2]) / 3
# if a[0] < 33 or a[1] < 33 or a[2] < 33 or avg < 40:
#     print("fail")
# else:
#     print("pass")

# 3

# text1 = input("Enter text\n")
# text = text1.lower()
# if "buy now" in text:
#     span = True
# elif "click this" in text:
#     span = True
# elif "subscribe this" in text:
#     span = True
# else:
#     span = False
#
# if span:
#     print("Its a spam")
# else:
#     print("Its not a spam")

# 4

# username = input("Enter username\n")
# if len(username)<11:
#     print("username contains less then 10 or 10 characters.")
# else:
#     print("username contains more then 11 characters.")

# 5

# list = [11,223,435,576,768,908]
#
# no = int(input("Enter the number\n"))
# if no in list:
#     print("list contains given number")
# else:
#     print("List does not contain given number")

# 6

# marks = int(input("Enter the percentage\n"))
#
# if marks > 90:
#     print("you got EX")
# elif marks > 80:
#     print("you got A")
# elif marks > 70:
#     print("you got B")
# elif marks > 60:
#     print("you got C")
# elif marks > 50:
#     print("you got D")
# else:
#     print("you got F")

# 7

post = input("Enter the post")
postL = post.lower()
if postL.__contains__("harry"):
    print("post is talking about harry")
else:
    print("post is not talking about harry")
