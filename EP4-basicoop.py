# create Constructor
class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self.name, self.salary, self.department))


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
emp1.department = 'Head of Engineer'
emp1.salary = 5000000

emp1.showData()
emp2 = Employee('Jo', 4500000, 'Manager')
emp2.showData()
