import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transactions = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transactions.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transactions.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and no more than your account balance. :)")
        self.show_balance()

    def show_balance(self):
        print("Balance is Rs.{}".format(self.__balance))     # == print(f"Balance is Rs.{self.balance}")

    def show_transactions(self):
        for date, amount in self._transactions:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type =  "withdrawn"
                amount *= -1
            print("{:>6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    rohit = Account("Rohit", 0)
    rohit.show_balance()
    rohit.deposit(1000)
    rohit.withdraw(190)
    rohit.show_transactions()


    ameya = Account("Ameya", 800)
    ameya.deposit(100)
    ameya.withdraw(200)
    ameya.show_transactions()