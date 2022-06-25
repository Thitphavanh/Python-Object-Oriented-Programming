# Encapsulation
class Employee:

    def __init__(self, name, salary, department):
        # protected attribute
        self._name = name
        self._salary = salary
        self._department = department

        # protected method
    def _showData(self):
        print('Employee Infomartion : name = {}, salary = {}, department = {} '.format(
            self._name, self._salary, self._department))


# create object
emp1 = Employee('Noy', 4500000, 'Engineer')
emp1._name = 'James'
emp1._salary = 5000000
emp1._showData()
