from employee import Employee


class Programer(Employee):
    __departmentName = 'Programer'

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print('experience = ' + str(self.__exp))
        print('skill = ' + self.__skill)

    def __str__(self):
        return (super().__str__() + ',experience = {} years, skill = {}'.format(self.__exp, self.__skill))
        print('-----------------')
