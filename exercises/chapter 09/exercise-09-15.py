##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-15.py.py
##############################################################################
# Modified to read the word list from a file
# Reads a score.txt file with the number of hits per player
# Reads a words.txt file with the list of words
#
# Before running:
#
# Create an empty file named score.txt
# Create a words file named words.txt
# containing one word per line.
#
# The game randomly chooses a word from this file
import sys
import random

words = []
score = {}


def load_words():
    file = open("words.txt", "r", encoding="utf-8")
    for word in file.readlines():
        word = word.strip().lower()
        if word != "":
            words.append(word)
    file.close()


def load_score():
    file = open("score.txt", "r", encoding="utf-8")
    for line in file.readlines():
        line = line.strip()
        if line != "":
            user, counter = line.split(";")
            score[user] = int(counter)
    file.close()


def save_score():
    file = open("score.txt", "w", encoding="utf-8")
    for user in score.keys():
        file.write("{user};{score[user]}\n")
    file.close()


def update_score(name):
    if name in score:
        score[name] += 1
    else:
        score[name] = 1
    save_score()


def display_score():
    sorted_score = []
    for user, score_value in score.items():
        sorted_score.append([user, score_value])
    sorted_score.sort(key=lambda score_value: score_value[1])
    print("\n\nBest players by number of hits:")
    sorted_score.reverse()
    for up in sorted_score:
        print(f"{up[0]:30s} {up[1]:10d}")


load_words()
load_score()

word = words[random.randint(0, len(words) - 1)]

typed = []
hits = []
errors = 0
while True:
    password = ""
    for letter in word:
        password += letter if letter in hits else "."
    print(password)
    if password == word:
        print("You got it right!")
        name = input("Enter your name: ")
        update_score(name)
        break
    attempt = input("\nEnter a letter:").lower().strip()
    if attempt in typed:
        print("You already tried this letter!")
        continue
    else:
        typed += attempt
        if attempt in word:
            hits += attempt
        else:
            errors += 1
            print("You missed!")
    print("X==:==\nX  :   ")
    print("X  O   " if errors >= 1 else "X")
    line2 = ""
    if errors == 2:
        line2 = "  |   "
    elif errors == 3:
        line2 = r" \|   "
    elif errors >= 4:
        line2 = r" \|/ "
    print(f"X{line2}")
    line3 = ""
    if errors == 5:
        line3 += r" /     "
    elif errors >= 6:
        line3 += r" / \ "
    print(f"X{line3}")
    print("X\n===========")
    if errors == 6:
        print("Hanged!")
        break

display_score()
