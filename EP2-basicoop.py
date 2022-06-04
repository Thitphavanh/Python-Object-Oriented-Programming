# create class
class Employee:

    # create method
    def detail(self):
        self.name = 'Hery Phenomenal'
        self.salary = 2000000
        print('My Employee Infomartion = {}, {}'.format(self.name,self.salary))


# create object
emp1 = Employee()
emp1.detail()
