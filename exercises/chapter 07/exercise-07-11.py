##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-11.py.py
##############################################################################
words = [
    "house",
    "ball",
    "hose",
    "grape",
    "okra",
    "computer",
    "snake",
    "lentil",
    "rice",
]

index = int(input("Enter a number:"))
word = words[(index * 776) % len(words)]
for x in range(100):
    print()
typed = []
hits = []
errors = 0

lines_txt = """
X==:==
X  :
X
X
X
X
=======

"""

lines = []

for line in lines_txt.splitlines():
    # Padding spaces to each line
    # in case your text editor removed the
    # spaces at the end of each line
    lines.append(list(line.ljust(8, " ")))

while True:
    password = ""
    for letter in word:
        password += letter if letter in hits else "."
    print(password)
    if password == word:
        print("You got it right!")
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
            if errors == 1:
                lines[3][3] = "O"
            elif errors == 2:
                lines[4][3] = "|"
            elif errors == 3:
                lines[4][2] = "\\"
            elif errors == 4:
                lines[4][4] = "/"
            elif errors == 5:
                lines[5][2] = "/"
            elif errors == 6:
                lines[5][4] = "\\"

    for line in lines:
        print("".join(line))
    if errors == 6:
        print("Hanged!")
        print(f"The secret word was: {word}")
        break
