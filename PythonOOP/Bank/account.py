from transaction import Transaction

class Account:

    def __init__(self, name: str, num: str, balance: float) -> None:
        self.name = name
        self.num = num
        self.__balance = balance
        self.__transactions = [Transaction(self.balance, "Cr", self.balance)]

    def withdraw(self, amount):
        self.balance = -amount
        transaction = Transaction(amount, "Dr", self.balance)
        self.__transactions.append(transaction)
        
    def deposit(self, amount):
        self.balance = amount
        transaction = Transaction(amount, "Cr", self.balance)
        self.__transactions.append(transaction)

    def show_transactions(self):
        print("=====================================================================")
        print(self)
        print("|{:^15}|{:^6}|{:^28}|{:^15}|".format("Amount", "Type", "Date", "Balance"))
        for transaction in self.get_transactions:
            print(transaction)
    
    @property
    def get_transactions(self):
        return self.__transactions

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance += amount
    
    def __str__(self) -> str:
        return "Name.: {}\nAcc No.: {}".format(self.name, self.num)
