from account import Account

class Bank:
    
    @staticmethod
    def menu():
        print("\
              Choose one option:\n\
              1. Create an account\n\
              2. Withdraw money\n\
              3. Deposit money\n\
              4. Show balance\n\
              5. Show all transactions\n\
              6. Show account info\n\
              7. Quit")

        
    def __init__(self, name: str, branch: str) -> None:
        self.name = name
        self.branch = branch
        self.accounts = []

    # def show_all_accounts(self):
    #     print(self.accounts)

    @classmethod
    def transfer(cls, party_1: Account, party_2: Account, amount: float):
        party_1.withdraw(amount)
        party_2.deposit(amount)