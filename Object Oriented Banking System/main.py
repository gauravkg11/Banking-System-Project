from bank_system import BankSystem
from exceptions import InsufficientBalanceError


def get_int_input(prompt):
    # validated input
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    bank = BankSystem()

    while True:
        print("Welcome to XYZ Bank")
        print("Select your options")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show all account")
        print("5. Delete an account")
        print("6. Transaction History")
        print("7. Exit")

        choice = get_int_input("Enter your choice: ")

        if choice == 1:
            name = input("Enter full name of customer: ")
            account_number = get_int_input("Enter new account number: ")
            account_type = input("Enter account type Savings/Current: ").strip().lower()
            if account_type in ("savings", "current"):
                bank.create_account(name, account_number, account_type)
            else:
                print("Invalid account type. Please enter 'Savings' or 'Current'.")
        elif choice == 2:
            account_number = get_int_input("Enter the account number: ")
            amount = get_int_input("Enter the amount to deposit: ")
            if bank.find_account(account_number):
                account = bank.find_account(account_number)
                account.deposit(amount)
            else:
                print("Invalid account number.")
        elif choice == 3:
            account_number = get_int_input("Enter the account number: ")
            amount = get_int_input("Enter the amount to withdraw: ")
            if bank.find_account(account_number):
                account = bank.find_account(account_number)
                try:
                    account.withdraw(amount)
                except InsufficientBalanceError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid account number.")
        elif choice == 4:
            bank.show_all_accounts()
        elif choice == 5:
            account_number = get_int_input("Enter the account number: ")
            if bank.find_account(account_number):
                bank.delete_account(account_number)
            else:
                print("Invalid account number.")
        elif choice == 6:
            account_number = get_int_input("Enter the account number: ")
            bank.show_transaction_history(account_number)
        elif choice == 7:
            bank.save_data()
            print("Data saved successfully. Exiting... Thank you.")
            break
        else:
            print("Invalid input. Please enter a valid input.")
            continue


if __name__ == "__main__":
    main()
