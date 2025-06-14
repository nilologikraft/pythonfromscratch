##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-16.py.py
##############################################################################
import random

player_health = 100
tree = random.randint(1, 100)
print("An alien is hiding behind a tree")
print("Each tree has been numbered from 1 to 100.")
print("You have 3 attempts to guess which tree")
print("the alien is hiding behind.")

while player_health > 0:
    print(f"Health points: {player_health}")
    guess = int(input("Choose a tree [1-100]: "))
    if guess == tree:
        print("You got it right! The alien was found!")
        break
    elif guess > tree:
        print("Too high")
    else:
        print("Too low")
    damage = random.randint(5, 20)
    player_health -= damage

if player_health <= 0:
    print("You didn't survive. The alien won.")
    print(f"The alien was behind tree {tree}.")
