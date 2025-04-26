from transaction import Transaction
from exceptions import InsufficientBalanceError


class BankAccount:
    def __init__(self, name, account_number):
        self.account_holder_name = name
        self.account_number = account_number
        self.transaction_history = []
        self.__account_balance = 0

    def get_balance(self):
        return self.__account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self.transaction_history.append(Transaction("Deposit", amount))
            print("Deposit successful")
        else:
            print("Invalid amount")
        return self.__account_balance

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            self.transaction_history.append(Transaction("Withdrawal", amount))
            print("Withdrawal successful")
        else:
            raise InsufficientBalanceError("Insufficient balance for withdrawal.")
        return self.__account_balance

    def show_transaction_history(self):
        if self.transaction_history:
            for tran in self.transaction_history:
                print(tran)
        else:
            print("No transaction yet.")


class SavingAccount(BankAccount):
    def __init__(self, name, account_number):
        super().__init__(name, account_number)
        self.withdrawal_count = 0
        self.withdrawal_limit = 3

    def withdraw(self, amount):
        if self.withdrawal_count < self.withdrawal_limit:
            super().withdraw(amount)
            self.withdrawal_count += 1
        else:
            print("Insufficient Balance or limit reached")
        return self.get_balance()


class CurrentAccount(BankAccount):
    def __init__(self, name, account_number):
        super().__init__(name, account_number)
        self.minimum_balance = 1000

    def withdraw(self, amount):
        if amount <= (self.get_balance() - self.minimum_balance):
            super().withdraw(amount)
        else:
            raise InsufficientBalanceError("Withdrawal would breach the minimum balance requirement.")
        return self.get_balance()
