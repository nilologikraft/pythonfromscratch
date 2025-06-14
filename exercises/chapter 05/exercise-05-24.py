##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-24.py.py
##############################################################################
prime_count = int(input("Enter the number of prime numbers to generate: "))
if prime_count < 0:
    print("Invalid number. Please enter only positive values")
else:
    if prime_count >= 1:
        print("2")  # 2 is the only number that is both prime and even
    primes_generated = 1  # so it's the first prime number generated
    next_prime = 3  # the next prime starts with 3
    while primes_generated < prime_count:
        # Since all following primes are odd
        divisor = 3
        while divisor < next_prime:
            # If remainder is zero, the number is divisible
            if next_prime % divisor == 0:
                break
            # Increment the divisor
            divisor = divisor + 2
        # When the number is prime, it's only divisible by itself
        if divisor == next_prime:
            print(next_prime)
            primes_generated = primes_generated + 1
        # move to the next odd number,
        # since even numbers are not prime, except 2
        next_prime = next_prime + 2
