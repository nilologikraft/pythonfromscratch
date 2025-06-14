##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/04.10 - Bye Plans with elif.py
##############################################################################
valid = True
plan = input("What's your cell phone plan? ")
if plan == "LittleTalk":
    minutes_on_plan = 100
    extra = 0.20
    price = 50
elif plan == "TalkMore":
    minutes_on_plan = 500
    extra = 0.15
    price = 99
else:
    valid = False
if not valid:
    print(f"Error: I don't know this plan {plan}")
else:
    minutes_consumed = int(input("How many minutes did you consume? "))
    print("You will pay:")
    print(f"Plan price ${price:10.2f}")
    supplement = 0
    if minutes_consumed > minutes_on_plan:
        supplement = extra * (minutes_consumed - minutes_on_plan)
    print(f"Supplement ${supplement:10.2f}")
    print(f"Total      ${price + supplement:10.2f}")
