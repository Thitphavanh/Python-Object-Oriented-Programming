# Overloading
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
    def _getIncome(self, bonus=0, overtime=0):
        return (self.__salary*12) + bonus + overtime

    def __str__(self):
        return ('name = {}, department = {}, salary = {}, income per year = {} '.format(self.__name, self._department, self.__salary, self._getIncome()))


class Accounting(Employee):
    __departmentName = 'Accounting'

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print('age = ' + str(self.__age))

    def __str__(self):
        return (super().__str__() + ',age = {} year old'.format(self.__age))
        print('-----------------')


class Programer(Employee):
    __departmentName = 'Programer'

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print('experience = ' + str(self.__exp))
        print('skill = ' + self.__skill)

    def __str__(self):
        return (super().__str__() + ',experience = {} years, skill = {}'.format(self.__exp, self.__skill))
        print('-----------------')


class Sale(Employee):
    __departmentName = 'Sale'

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print('area = ' + self.__area)

    def __str__(self):
        return (super().__str__() + ',area = {}'.format(self.__area))
        print('-----------------')


account = Accounting('Noy', 1800000, 26)
print('Accountant employees department are get income per year', str(account._getIncome(1200000)))
programer = Programer('Tom', 4500000, 2, 'Architecture engineer')
print('Programer employees department are get income per year', str(programer._getIncome(1500000,150000)))
sale = Sale('Tum', 3000000, 'Vientaine')
print('Sale employee departments are get income per year', str(sale._getIncome()))
