# Inheritance
class Employee:
    # class variable
    minSalary = 1200000
    maxSalary = 5000000
    companyName = 'ANITOCORN INC.'

    def __init__(self, name, salary, department):
        # instance variable
        self.name = name
        self.salary = salary
        self.department = department

        # private method
    def _showData(self):
        print('Employee Infomartion : name = ' + self.name)
        print('salary = ', format(self.salary))
        print('department = ' + self.department)


class Accounting(Employee):
    def __init__(self):
        pass


class Programer(Employee):
    def __init__(self):
        pass


class Sale(Employee):
    def __init__(self):
        pass


account = Accounting()
print(account.companyName)

programer = Programer()
print(programer.minSalary)

sale = Sale()
# print(sale.minSalary)
