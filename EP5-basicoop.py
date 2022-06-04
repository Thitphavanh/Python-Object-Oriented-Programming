# Auxiliary function
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
emp2 = Employee('Jo', 4500000, 'Manager')

# print(isinstance(emp1,Employee))
print(emp1.__class__)