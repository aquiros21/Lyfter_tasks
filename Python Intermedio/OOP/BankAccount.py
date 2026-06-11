
class BankAccount:

    def __init__(self):
        self.balance = 0

    def add_funds(self, funds):
        self.balance += funds

    def withdraw_funds(self, funds):
        self.balance -= funds


class SavingsAccount(BankAccount):

    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw_funds(self, funds):
        if (self.balance - funds) <= self.minimum_balance:
            print("Invalid transaction, minimum balance was exceeded")
            return
        else:
            self.balance -= funds


minimum_balance = SavingsAccount(600)
minimum_balance.add_funds(1000)
minimum_balance.withdraw_funds(500)