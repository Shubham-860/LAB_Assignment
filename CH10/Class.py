# class Employee:
#     company = "Google Inc"
#     salary = 12345
#
#     def getSalary(self):
#         print(f"Hello {self.name} Your salary is {self.salary}")
#
#     @staticmethod
#     def greet():
#         print("Good morning!")
#
#
# Shubham = Employee()
# Shree = Employee()
# # print(Shubham.company)
# # print(Shree.company)
# Shree.company = "SHow the bound is strong"
#
# print(Shubham.company)
# print(Shree.company)
# Shubham.name = "Shubham"
# print(Shubham.getSalary())
#
#

class computer:
    display = 15.6
    random = 0

    def __init__(self, cpu, ram, gpu):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.games = self.games()

    def config(self, battery=5):
        print(
            f"Config is cpu = {self.cpu}, ram = {self.ram}, gpu = {self.gpu}, battery = {battery} hours and display = {self.display} inches")

    def compare(self, other):
        if self.gpu == other.gpu:
            return True
        else:
            return False

    class games:
        def __init__(self):
            self.action = 4
            self.race = 3
            self.adventure = 3

        def show(self):
            print(f"we have {self.action} action games, {self.race} racesing games, {self.adventure} adventure games")


nitro = computer("i5 8th gen", 8, "1550 Ti")
s550 = computer("i5 8th gen", 8, "MX 330")
nitro.config(2)
nitro.games.show()
computer.display = 17.0
s550.config()
s550.cpu = "i5 12th gen"
print(nitro.random)
nitro.random = 10
print(nitro.random)
if nitro.compare(s550):
    print("Its the same")
else:
    print("its different")
