##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-12.py.py
##############################################################################
distance = float(input("Enter the distance in km:"))
average_speed = float(input("Enter the average speed in km/h:"))
time = distance / average_speed
print("The estimated time is %5.2f hours" % time)
# Optional: print the time in hours, minutes and seconds
time_s = int(time * 3600)  # convert from hours to seconds
hours = int(time_s / 3600)  # integer part
time_s = int(time_s % 3600)  # remainder
minutes = int(time_s / 60)
seconds = int(time_s % 60)
print("%05d:%02d:%02d" % (hours, minutes, seconds))
