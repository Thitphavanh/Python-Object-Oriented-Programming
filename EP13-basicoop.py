# Super
class Employee:
    # class variable
    minSalary = 1200000
    maxSalary = 5000000
    companyName = 'ANITOCORN INC.'

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

        # private method
    def _showData(self):
        print('name = ' + self.__name)
        print('salary = ', format(self.__salary))
        print('department = ' + self._department)

    # employee get income per year
    def _getIncome(self):
        return self.__salary*12

    def __str__(self):
        return ('name = {}, department = {}, salary = {}, income per year = {} '.format(self.__name, self._department, self.__salary, self._getIncome()))


class Accounting(Employee):
    __departmentName = 'Accounting'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


class Programer(Employee):
    __departmentName = 'Programer'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


class Sale(Employee):
    __departmentName = 'Sale'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


account = Accounting('Noy', 1800000)
print(account.__str__())
programer = Programer('Tom', 4500000)
print(programer.__str__())
sale = Sale('Tum', 3000000)
print(sale.__str__())

