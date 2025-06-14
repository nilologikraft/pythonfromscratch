##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.23 - Alien Game.py
##############################################################################
import random
MAX_ATTEMPTS = 3
tree = random.randint(1, 100)
print("An alien is hiding behind a tree")
print("Each tree was numbered from 1 to 100.")
print("You have 3 attempts to guess behind which tree")
print("the alien is hiding.")
print(tree)  # Remove this line to make the tree the alien is hiding behind a secret
for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Tree {attempt}/{MAX_ATTEMPTS}: "))
    if guess == tree:
        print(f"You got it in attempt #{attempt}")
        break
    elif guess > tree:
        print("Too high")
    else:
        print("Too low")
else:
    print("You couldn't get it right.")
    print(f"The alien was hiding behind tree {tree}")
