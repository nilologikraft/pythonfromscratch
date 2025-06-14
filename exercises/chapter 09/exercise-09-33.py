##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-33.py.py
##############################################################################
# This exercise can also be done using the glob module
# Check Python documentation for more information
import sys
import os
import os.path

# this module helps with converting filenames to valid HTML links
import urllib.request

if len(sys.argv) < 2:
    print("Enter the directory name to collect jpg and png files!")
    sys.exit(1)

directory = sys.argv[1]

page = open("images.html", "w", encoding="utf-8")
page.write(
    """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>PNG and JPG Images</title>
</head>
<body>
"""
)
page.write(f"Images found in directory: {directory}")
for entry in os.listdir(directory):
    name, extension = os.path.splitext(entry)
    if extension in [".jpg", ".png"]:
        full_path = os.path.join(directory, entry)
        link = urllib.request.pathname2url(full_path)
        page.write(f"<p><a href='{link}'>{entry}</a></p>")

page.write(
    """
</body>
</html>
"""
)
page.close()
