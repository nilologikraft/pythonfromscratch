##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.08 - Generating a web page from a dictionary.py
##############################################################################
movies = {
    "drama": ["Citizen Kane", "The Godfather"],
    "comedy": ["Modern Times", "American Pie", "Dr. Dolittle"],
    "police": ["Black Rain", "Desire to Kill", "Hard to Kill"],
    "war": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("movies.html", "w", encoding="utf-8") as page:
    page.write("""
<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<title>Movies</title>
</head>
<body>
""")
    for category, m in movies.items():
        page.write(f"<h1>{category.title()}</h1>\n")
        for movie in m:
            page.write(f"<h2>{movie}</h2>\n")
    page.write("</body></html>")
