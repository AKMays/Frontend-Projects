"""
Purpose: This program is a simulation of an ATM that allows users to deposit, withdraw, transfer, and check the balance of their 
bank accounts. It uses object-oriented programming concepts to create an Account class and an ATM class, and includes features like 
generating account numbers and PINs randomly, and error handling for invalid user input. The program is designed to be realistic and 
secure, and to provide a convenient way for users to perform common banking transactions.
Author(s): Adonte Mays 
Date: 2022-03-11
Updated: 2023-28-04
"""

import random

class Account:
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.account_number = random.randint(100000, 999999)
        self.pin = random.randint(1000, 9999)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into {self.account_type} account. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds. {self.account_type} account balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.account_type} account. New balance: ${self.balance}")

    def transfer(self, amount, target_account):
        if self.balance < amount:
            print(f"Insufficient funds. {self.account_type} account balance: ${self.balance}")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount} from {self.account_type} account to {target_account.account_type} account. New {self.account_type} account balance: ${self.balance}. New {target_account.account_type} account balance: ${target_account.balance}")

    def check_balance(self):
        print(f"{self.account_type} account balance: ${self.balance}")

class ATM:
    def __init__(self):
        self.accounts = []

    def add_account(self, owner, balance, account_type):
        account = Account(owner, balance, account_type)
        self.accounts.append(account)
        print(f"Created {account_type} account for {owner}. Account number: {account.account_number}. Pin: {account.pin}")

    def get_account(self, account_number, pin):
        for account in self.accounts:
            if account.account_number == account_number and account.pin == pin:
                return account
        return None

    def run(self):
        while True:
            print("Welcome to the ATM. Please insert your card.")
            account_number = input("Enter your account number (Enter 1 to quit): ")
            if account_number == "1":
                    return 1
            pin = input("Enter your PIN: ")
            account = self.get_account(int(account_number), int(pin))
            if account is None:
                print("Invalid account number or PIN. Please try again.")
            else:
                while True:
                    print(f"Welcome, {account.owner}. What would you like to do?")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Check balance")
                    print("5. Quit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        amount = int(input("Enter deposit amount: "))
                        account.deposit(amount)
                    elif choice == "2":
                        amount = int(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    elif choice == "3":
                        target_account_number = int(input("Enter target account number: "))
                        target_account = None
                        for acct in self.accounts:
                            if acct.account_number == target_account_number:
                                target_account = acct
                                break
                        if target_account is None:
                            print(f"Target account number {target_account_number} not found.")
                        else:
                            amount = int(input("Enter transfer amount: "))
                            account.transfer(amount, target_account)
                    elif choice == "4":
                        account.check_balance()
                    else:
                        if choice == "5":
                            print("Thank you for using the ATM.")
                            break

atm = ATM()

atm.add_account("John Doe", 1000, "Checking")
atm.add_account("Jane Smith", 5000, "Savings")

atm.run()

