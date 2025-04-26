
# Bank Management System


> A simple console-based bank management project demonstrating core Object-Oriented Programming (OOP) concepts in Python.

---

## Table of Contents
- Project Overview
- Features
- Project Structure
- Installation
- How to Run
- Technologies Used


---

## Project Overview

This is a mini banking application where users can:
- Create **Savings** or **Current** accounts
- Perform **Deposits** and **Withdrawals**
- View **Transaction History**
- Maintain **Withdrawal Limits** (for Savings Accounts)
- Maintain **Minimum Balance** (for Current Accounts)
- **Save** and **Load** user data automatically with file handling (`pickle`)

---

## Features

- Create Savings and Current accounts  
- Deposit money  
- Withdraw money with proper validations  
- View transaction history  
- Persistent storage using **Pickle**  
- Error handling with custom exceptions  

---

## Project Structure

```
├── account.py          # Contains BankAccount, SavingAccount, CurrentAccount classes
├── bank_system.py      # Handles overall system functionalities
├── exceptions.py       # Custom exception (InsufficientBalanceError)
├── transactions.py     # Transaction recording class
├── main.py             # User interface (CLI menu)
├── bank_data.pkl       # Auto-saved data file (after running program)
└── README.md           # Project documentation
```

---

## Installation

1. **Clone the repository**:

    ```bash git clone https://github.com/your-username/bank-management-system.git cd bank-management-system```

2. **(Optional) Create a virtual environment**:

    ```bash python -m venv venv source venv/bin/activate  # For Linux/Mac venv\Scripts\activate   # For Windows```

3. **Install requirements** (not really needed, but good practice):

    ```bash pip install -r requirements.txt ```

---

## How to Run

Simply execute:

```bash python main.py```

Follow the menu to create accounts, deposit, withdraw, view transactions, and more!

---

## Technologies Used

- Python 3.x
- Pickle Module
- Object-Oriented Programming (OOP)


---

