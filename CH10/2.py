class calculater:
    def square(self, a):
        return a ** 2

    def squareRoot(self, a):
        return a ** 0.5

    def cube(self, a):
        return a ** 3


a = int(input("Enter a number: "))
c = calculater()
print(f"the square of {a} is : {c.square(a)}, squareRoot is {c.squareRoot(a)} and cube is {c.cube(a)}")
