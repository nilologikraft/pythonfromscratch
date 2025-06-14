##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-07.py.py
##############################################################################
# Uma boa fonte de textos para teste é o projeto Gutemberg
# http://www.gutenberg.org/
# Não esqueça de configurar o encoding do arquivo.
#
# Este programa foi testado com Moby Dick
# http://www.gutenberg.org/cache/epub/2701/pg2701.txt
# Gravado com o nome de mobydick.txt
#
WIDTH = 76
LINES = 60
FILENAME = "mobydick.txt"


def check_page(file, line, page):
    if line == LINES:
        footer = f"= {FILENAME} - Page: {page} ="
        file.write(footer.center(WIDTH - 1) + "\n")
        page += 1
        line = 1
    return line, page


def write(file, line, nlines, page):
    file.write(line + "\n")
    return check_page(file, nlines + 1, page)


input_file = open(FILENAME, encoding="utf-8")
output = open("paginated_output.txt", "w", encoding="utf-8")

page = 1
lines = 1

for line in input_file.readlines():
    words = line.rstrip().split(" ")
    line = ""
    for word in words:
        word = word.strip()
        if len(line) + len(word) + 1 > WIDTH:
            lines, page = write(output, line, lines, page)
            line = ""
        line += word + " "
    if line != "":
        lines, page = write(output, line, lines, page)

# To print the number on the last page
while lines != 1:
    lines, page = write(output, "", lines, page)

input_file.close()
output.close()
