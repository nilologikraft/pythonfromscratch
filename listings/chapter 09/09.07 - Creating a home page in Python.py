##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.07 - Creating a home page in Python.py
##############################################################################
with open("page.html", "w", encoding="utf-8") as page:
    page.write("<!DOCTYPE html>\n")
    page.write("<html lang=\"en-US\">\n")
    page.write("<head>\n")
    page.write("<meta charset=\"utf-8\">\n")
    page.write("<title>Page Title</title>\n")
    page.write("</head>\n")
    page.write("<body>\n")
    page.write("Hello!")
    for line in range(10):
        page.write(f"<p>{line}</p>\n")
    page.write("</body>\n")
    page.write("</html>\n")
