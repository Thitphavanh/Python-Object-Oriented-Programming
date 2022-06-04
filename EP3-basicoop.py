# create class
class Employee:

    # create method
    def detail(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self.name, self.salary, self.department))


# create object
emp1 = Employee()
emp1.detail('Noy', 4500000, 'Engineer')

emp2 = Employee()
emp2.detail('Tick', 2500000, 'Programmer')

emp1.showData()
emp2.showData()
