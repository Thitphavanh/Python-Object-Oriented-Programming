# Setter and Getter Method
class Employee:

    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

        # private method
    def _showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self.getName(), self.getSalary(), self.getDepartment()))

    # setter method
    def setName(self, newNmae):
        self.__name = newNmae

    def setSalary(self, newSalary):
        self.__salary = newSalary

    def setDepartment(self, newDepartment):
        self.__department = newDepartment

    # getter method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
# print('Greate employee in the 2022 years is', emp1.getName())
# print('He receip salary per month is', emp1.getSalary())
# print('He work at department of', emp1.getDepartment())
emp1._showData()
