##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-10.py.py
##############################################################################
points = 0
question = 1
while question <= 3:
    answer = input(f"Answer to question {question}: ")
    if question == 1 and (answer == "b" or answer == "B"):
        points = points + 1
    if question == 2 and (answer == "a" or answer == "A"):
        points = points + 1
    if question == 3 and (answer == "d" or answer == "D"):
        points = points + 1
    question += 1
print(f"The student scored {points} point(s)")
