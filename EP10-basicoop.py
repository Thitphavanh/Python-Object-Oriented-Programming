# Class Variable
class Employee:
    # class variable
    _minSalary = 1200000
    _maxSalary = 5000000
    _companyName = 'ANITOCORN INC.'

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

        # private method
    def _showData(self):
        print('Employee Infomartion : name = ' + self.__name)
        print('Employee Infomartion : salary = ', format(self.__salary))
        print('Employee Infomartion : department = ' + self._department)


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
print('This company the less salary is', str(Employee._minSalary))
print(Employee._companyName)