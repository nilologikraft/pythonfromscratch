##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-38.py.py
##############################################################################
import json
import os


def read_grades():
    grades = []
    for i in range(4):
        grade = float(input(f"Enter the {i+1}th grade: "))
        grades.append(grade)
    return grades


def load_data():
    # If the file doesn't exist, returns an empty list
    if not os.path.exists("student_grades.json"):
        return []

    try:
        with open("student_grades.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# Reading existing data
students = load_data()

# Reading new data
name = input("Enter student name: ")
grades = read_grades()

# Creating dictionary with new data
new_student = {"name": name, "grades": grades}

# Checks if student already exists and updates, or adds new student
student_exists = False
for i, student in enumerate(students):
    if student["name"] == name:
        students[i] = new_student
        student_exists = True
        break

if not student_exists:
    students.append(new_student)

# Saving all data to JSON file
with open("student_grades.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student data successfully saved to 'student_grades.json' file.")
