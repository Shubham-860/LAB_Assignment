n = int(input("Enter amount number :"))
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
num = []
for i in range(n):
    c = a + b
    a = b
    b = c
    num.append(c)
print(num)
exit()

