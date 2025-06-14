##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/10.01 - Account with transaction log and statement (accounts.py).py
##############################################################################
class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)
    def summary(self):
        print(f"Account #{self.number} Balance: {self.balance:10.2f}")
    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(["WITHDRAW", value])
    def deposit(self, value):
        self.balance += value
        self.operations.append(["DEPOSIT", value])
    def statement(self):
        print(f"Account Statement #{self.number}\n")
        for operation in self.operations:
            print(f"{operation[0]:10s} {operation[1]:10.2f}")
        print(f"\n    Balance: {self.balance:10.2f}\n")
