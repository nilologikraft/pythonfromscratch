##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-29.py.py
##############################################################################
movies = {
    "drama": ["Citizen Kane", "The Godfather"],
    "comedy": ["Modern Times", "American Pie", "Dr. Dolittle"],
    "crime": ["Black Rain", "Death Wish", "Hard to Kill"],
    "war": ["Rambo", "Platoon", "Tora!Tora!Tora!"],
}

page = open("movies.html", "w", encoding="utf-8")
page.write(
    """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Movies</title>
</head>
<body>
"""
)
for category, values in movies.items():
    page.write(f"<h1>{category}</h1>")
    for entry in values:
        page.write(f"<p>{entry}</p>")
page.write(
    """
</body>
</html>
"""
)
page.close()
