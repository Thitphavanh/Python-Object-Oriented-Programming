# Setter Method 
class Employee:

    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

        # private method
    def _showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self.__name, self.__salary, self.__department))

    # setter method
    def setName(self, newNmae):
        self.__name = newNmae

    def setSalary(self, newSalary):
        self.__salary = newSalary

    def setDepartment(self, newDepartment):
        self.__department = newDepartment
        
# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
emp1.setName('James')
emp1.setSalary(6000000)
emp1.setDepartment('Innovator')
emp1._showData()
