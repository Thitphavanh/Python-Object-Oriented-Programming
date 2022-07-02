from employee import Employee


class Accounting(Employee):
    __departmentName = 'Accounting'

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print('age = ' + str(self.__age))

    def __str__(self):
        return (super().__str__() + ',age = {} year old'.format(self.__age))
        print('-----------------')
