

class Programar:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f"company Name is {self.company}, employee Name is {self.name}and he/she worked with {self.product}")


shubham = Programar("Shubham", "GitHub")
Shree = Programar("Shree", "abcd")

shubham.getinfo()
Shree.getinfo()