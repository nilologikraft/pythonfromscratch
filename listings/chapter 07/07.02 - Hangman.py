##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/07.02 - Hangman.py
##############################################################################
word = input("Type the secret word:").lower().strip()
for x in range(100):
    print()
typed = []
correct_answers = []
errors = 0
while True:
    password = ""
    for letter in word:
        password += letter if letter in correct_answers else "."
    print(password)
    if password == word:
        print("You got it right!")
        break
    attempt = input("\nType a letter:").lower().strip()
    if attempt in typed:
        print("You've already tried this letter!")
        continue
    else:
        typed += attempt
        if attempt in word:
            correct_answers += attempt
        else:
            errors += 1
            print("You made a mistake!")
    print("X==:==\nX  :  ")
    print("X  O  " if errors >= 1 else "X")
    line2 = ""
    if errors == 2:
        line2 = "  |  "
    elif errors == 3:
        line2 = " \|  "
    elif errors >= 4:
        line2 = " \|/ "
    print(f"X{line2}")
    line3 = ""
    if errors == 5:
        line3 += " /   "
    elif errors >= 6:
        line3 += " / \ "
    print(f"X{line3}")
    print("X\n===========")
    if errors == 6:
        print("Hanged!")
        break
