import datetime as dt

class Transaction:

    def __init__(self, amount: float, kind: str, balance: float) -> None:
        self.__balance = balance
        self.amount = amount
        self.datetime = dt.datetime.now()
        self.type = kind
    
    def __str__(self):
        return "|{:>15.4f}|{:>6}|{:>28}|{:>15.4f}|".format(self.amount, self.type, str(self.datetime), self.__balance)
