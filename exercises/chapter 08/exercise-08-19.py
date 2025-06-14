##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-19.py.py
##############################################################################
def primes(n):
    p = 1  # Position in sequence
    yield 2  # 2 is the only even prime number
    d = 3  # divisor starts with 3
    b = 3  # dividend starts with 3, is the number we'll test if it's prime
    while p < n:
        # print(d, b, d % b, p, n)
        if b % d == 0:  # If b is divisible by d, the remainder will be 0
            if b == d:  # If b equals d, all d values have been tested
                yield b  # b is prime
                p += 1  # increment the sequence
            b += 2  # Move to the next odd number
            d = 3  # Start dividing by 3 again
        elif d < b:  # Continue trying?
            d += 2  # Increment the divisor to the next odd number
        else:
            b += 2  # Try another odd number


for prime in primes(10):
    print(prime)
