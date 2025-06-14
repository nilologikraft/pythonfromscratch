##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-37.py.py
##############################################################################
import json


# Function to read student grades
def read_grades():
    grades = []
    for i in range(4):
        grade = float(input(f"Enter the {i+1}th grade: "))
        grades.append(grade)
    return grades


# Reading student data
name = input("Enter student name: ")
grades = read_grades()

# Creating dictionary with student data
student = {"name": name, "grades": grades}

# Saving data to a JSON file
with open("student_grades.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data successfully saved to 'student_grades.json' file.")
