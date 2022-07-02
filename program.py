from accounting import Accounting
from programmer import Programer
from sale import Sale

account = Accounting('Noy', 1800000, 26)
print('Accountant employees department are get income per year', str(account._getIncome(1200000)))
programer = Programer('Tom', 4500000, 2, 'Architecture engineer')
print('Programer employees department are get income per year', str(programer._getIncome(1500000, 150000)))
sale = Sale('Tum', 3000000, 'Vientaine')
print('Sale employee departments are get income per year', str(sale._getIncome()))
