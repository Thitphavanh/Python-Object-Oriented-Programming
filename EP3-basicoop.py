# create class
class Employee:

    # create method
    def detail(self, name, salary):
        self.name = name
        self.salary = salary
        print('My Employee Infomartion = {}, {}'.format(self.name, self.salary))


# create object
emp1 = Employee()
emp1.detail('Noy', 1500000)

emp2 = Employee()
emp2.detail('Tick', 1200000)
