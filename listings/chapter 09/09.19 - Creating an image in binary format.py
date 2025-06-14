##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.19 - Creating an image in binary format.py
##############################################################################
image_in_hex = """
42 4d
46 00 00 00
00 00
00 00
36 00 00 00
28 00 00 00
02 00 00 00
02 00 00 00
01 00
18 00
00 00 00 00
10 00 00 00
13 0b 00 00
13 0b 00 00
00 00 00 00
00 00 00 00
00 00 FF
FF FF FF
00 00
FF 00 00
00 FF 00
00 00"""

image_bytes = bytes.fromhex(image_in_hex)

with open("imagem.bmp", "wb") as f:
    f.write(image_bytes)
