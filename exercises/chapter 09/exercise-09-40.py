##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-40.py.py
##############################################################################
import sys
import itertools


def print_bytes(image, bytes_per_line=16):
    for b in itertools.batched(image, bytes_per_line):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {" " * 3 * (bytes_per_line - len(b))}{tview}")


if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        image = f.read(512)  # Doesn't read the entire file, only the first 512 bytes
    print_bytes(image)
