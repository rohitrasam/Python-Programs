from bank import Bank
from account import Account
import time

rohit = Account("Rohit", "1029194123", 1000)
ameya = Account("Ameya", "1238912934", 900)
rohit.deposit(101)
time.sleep(10)
rohit.withdraw(580)
rohit.show_transactions()

Bank.transfer(rohit, ameya, 100)
time.sleep(10)
Bank.transfer(rohit, ameya, 59)
rohit.show_transactions()
ameya.show_transactions()