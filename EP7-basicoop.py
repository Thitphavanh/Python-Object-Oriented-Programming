# Encapsulation
class Employee:

    def __init__(self, name, salary, department):
        # private attribute
        self._name = name
        self.__salary = salary
        self.__department = department

        # private method
    def __showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self._name, self.__salary, self.__department))


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
emp1._name = 'James'
emp1.__salary = 5000000
emp1.__department = 'Inovator'

