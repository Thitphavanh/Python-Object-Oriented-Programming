# Auxiliary function
class Employee:

    def __init__(self, name, salary, department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department
        
        # public method
    def showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self.name, self.salary, self.department))


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
emp2 = Employee('Jo', 4500000, 'Manager')

