##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-08.py.py
##############################################################################
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


print(f"LCM of 10 and 5 -->  {lcm(10, 5)}")
print(f"LCM of 32 and 24 --> {lcm(32, 24)}")
print(f"LCM of 5 and 3 -->   {lcm(5, 3)}")
