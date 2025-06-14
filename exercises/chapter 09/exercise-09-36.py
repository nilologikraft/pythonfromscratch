##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-36.py.py
##############################################################################
import sys
import os
import os.path
import math


# This function converts the size
# into more readable units, avoiding
# returning and printing very large values.
def size_to_human_readable(size):
    if size == 0:
        return "0 byte"
    magnitude = math.log(size, 10)
    if magnitude < 3:
        return f"{size} bytes"
    elif magnitude < 6:
        return f"{size / 1024.0:7.3f} KB"
    elif magnitude < 9:
        return f"{size / pow(1024, 2)} MB"
    elif magnitude < 12:
        return f"{size / pow(1024, 3)} GB"


style_mask = "'margin: 5px 0px 5px %dpx;'"


def generate_style(level):
    return style_mask % (level * 30)


# Returns a function where the nroot parameter is used
# to calculate the indentation level
def generate_level_and_style(root):
    def level(path):
        xlevel = path.count(os.sep) - nroot
        return generate_style(xlevel)

    nroot = root.count(os.sep)
    return level


# Uses os.walk to traverse directories
# And a stack to store the size of each directory
def generate_listing(page, directory):
    directory = os.path.abspath(directory)
    # indenter is a function that calculates how many levels
    # from the directory level a path should have.
    indenter = generate_level_and_style(directory)
    stack = [[directory, 0]]  # Guard element, to avoid empty stack
    for root, directories, files in os.walk(directory):
        # If the current directory: root
        # Is not a subdirectory of the last traversed
        # Pop until finding a common parent
        while not root.startswith(stack[-1][0]):
            last = stack.pop()
            page.write(
                f"<p style={indenter(last[0])}>Size: (size_to_human_readable(last[1]))</p>"
            )
            stack[-1][1] += last[1]
        page.write(f"<p style={indenter(root)}>{root}</p>")
        d_size = 0
        for f in files:
            full_path = os.path.join(root, f)
            d_size += os.path.getsize(full_path)
        stack.append([root, d_size])
    # If the stack has more than one element
    # pop them
    while len(stack) > 1:
        last = stack.pop()
        page.write(
            f"<p style={indenter(last[0])}>Size: ({size_to_human_readable(last[1])})</p>"
        )
        stack[-1][1] += last[1]


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
