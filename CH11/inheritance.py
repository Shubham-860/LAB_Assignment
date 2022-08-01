class VIIT:
    address = "Baramati"


class MCA(VIIT):
    flor = 5


class Shubham(MCA):
    subject = "Python"


student = Shubham()


# print(student.address, student.flor, student.subject)

class Employee:
    def __init__(self):
        self.name = "employee"
        self.salary = 15000
        self.bonus = 12000

    # def changeSalary(self):
    #     self.salary = 47474

    @property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.bonus = val - self.salary


shub = Employee()
shub.name = "Shubham"
print(shub.totalSalary, "=", shub.salary, "+", shub.bonus)
shub.totalSalary = 30000
print(shub.totalSalary, "=", shub.salary, "+", shub.bonus)
