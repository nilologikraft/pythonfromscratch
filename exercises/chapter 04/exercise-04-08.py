##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-08.py.py
##############################################################################
plan = input("What is your cell phone plan? ")
if plan != "littletalk" and plan != "talkmore":
    print("I don't know this plan")
else:
    if plan == "littletalk":
        minutes_in_plan = 100
        extra = 0.20
        price = 50
    else:
        minutes_in_plan = 500
        extra = 0.15
        price = 99

    minutes_used = int(input("How many minutes did you use? "))
    print("You will pay:")
    print(f"Plan price      ${price:10.2f}")
    supplement = 0
    if minutes_used > minutes_in_plan:
        supplement = extra * (minutes_used - minutes_in_plan)
    print(f"Supplement      ${supplement:10.2f}")
    print(f"Total           ${price + supplement:10.2f}")
