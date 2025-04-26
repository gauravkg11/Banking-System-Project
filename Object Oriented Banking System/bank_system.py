from account import SavingAccount, CurrentAccount
import pickle, os


class BankSystem:
    def __init__(self):
        self.name = None
        self.account_type = None
        self.account_number = None
        self.account_details = {}  # Contains complete customer details such as name, account number, account type
        self.filename = "bank_data.pkl"
        self.load_data()

    def create_account(self, name, account_number, account_type):
        self.account_type = account_type

        if self.account_type == "savings":
            account = SavingAccount(name, account_number)  # Creating an object and assigning it to a variable
            self.account_details.update({account_number: account})  # assigning the object variable as key's value
        elif self.account_type == "current":
            account = CurrentAccount(name, account_number)
            self.account_details.update({account_number: account})
        print(f"Account created with account number {account_number} {account_type} for {name}")

    def find_account(self, account_number):
        if account_number in self.account_details:
            details = self.account_details[account_number]
            return details
        else:
            print("Invalid account number.")
            return None

    def show_all_accounts(self):
        for key, value in self.account_details.items():
            print(
                f"Account number: {key} | Customer Name: {value.account_holder_name} | Balance: {value.get_balance()}")
        return

    def delete_account(self, account_number):
        if account_number in self.account_details:
            details = self.account_details.pop(account_number)
            print(
                f"Account number: {account_number} | Customer Name: {details.account_holder_name} have been closed")
            return details
        else:
            print("Details not found")
            return None

    def show_transaction_history(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.show_transaction_history()
        else:
            print("Account not found.")

    def save_data(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.account_details, f)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.account_details = pickle.load(f)
        else:
            self.account_details = {}
