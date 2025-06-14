##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-09.py.py
##############################################################################
# Here accounts.py and clients.py were copied into a single file.
# This change is only to facilitate the visualization
# of the answer to this exercise.


class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)

    def summary(self):
        print(f"AC N°{self.number} Balance: {self.balance:10.2f}\n")
        for client in self.clients:
            print(f"Name: {client.name}\nPhone: {client.phone}\n")

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(["WITHDRAW", value])
        else:
            print("Insufficient balance!")

    def deposit(self, value):
        self.balance += value
        self.operations.append(["DEPOSIT", value])

    def statement(self):
        print(f"Statement AC N° {self.number}\n")
        for o in self.operations:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n    Balance: {self.balance:10.2f}\n")


mary = Client("Mary", "1243-3321")
john = Client("John", "5554-3322")

account = Account([mary, john], 1234, 5000)
account.summary()
