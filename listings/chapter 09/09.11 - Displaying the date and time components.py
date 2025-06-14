##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.11 - Displaying the date and time components.py
##############################################################################
import time
now = time.localtime()
print(f"Year: {now.tm_year}")
print(f"Month: {now.tm_mon}")
print("Day: {now.tm_mday}")
print("Hour: {now.tm_hour}")
print("Minute: {now.tm_min}")
print(f"Second: {now.tm_sec}")
print(f"Day of the week: {now.tm_wday}")
print(f"Day of the year: {now.tm_yday}")
print(f"Daylight saving time: {now.tm_isdst}")
