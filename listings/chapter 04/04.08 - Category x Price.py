##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/04.08 - Category x Price.py
##############################################################################
1 category = int(input("Enter the product category:"))
2 if category == 1:
3      price = 10
4  else:
5      if category == 2:
6          price = 18
7      else:
8          if category == 3:
9              price = 23
10         else:
11             if category = 4:
12                 price = 26
13             else:
14                 if category == 5:
15                     price = 31
16                 else:
17                      print("Invalid category, enter a value between 1 and 5!")
18                     price = 0
19 print(f"Product price is: ${price:6.2f}")
