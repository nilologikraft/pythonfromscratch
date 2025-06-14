##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-35.py.py
##############################################################################
import sys
import os
import os.path

# this module helps with converting filenames to valid HTML links
import urllib.request

style_mask = "'margin: 5px 0px 5px %dpx;'"


def generate_style(level):
    return style_mask % (level * 20)


def generate_listing(page, directory):
    root_count = os.path.abspath(directory).count(os.sep)
    for root, directories, files in os.walk(directory):
        level = root.count(os.sep) - root_count
        page.write(f"<p style={generate_style(level)}>{root}</p>")
        style = generate_style(level + 1)
        for f in files:
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            link = urllib.request.pathname2url(full_path)
            page.write(f"<p style={style}><a href='{link}'>{f}</a>  ({size} bytes)</p>")


if len(sys.argv) < 2:
    print("Enter the directory name to collect files!")
    sys.exit(1)

directory = sys.argv[1]

page = open("files.html", "w", encoding="utf-8")
page.write(
    """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Files</title>
</head>
<body>
"""
)
page.write(f"Files found starting from directory: {directory}")
generate_listing(page, directory)
page.write(
    """
</body>
</html>
"""
)
page.close()
