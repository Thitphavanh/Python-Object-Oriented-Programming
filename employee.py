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