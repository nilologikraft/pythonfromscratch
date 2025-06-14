##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.14 - Shows the current date in different time zones.py
##############################################################################
from zoneinfo import ZoneInfo
from datetime import datetime
brussels = ZoneInfo("Europe/Brussels")
new_york = ZoneInfo("America/New_York")
tokyo = ZoneInfo("Japan")
manaus = ZoneInfo("America/Manaus")
brasilia = ZoneInfo("Brazil/East")
rio_branco = ZoneInfo("America/Rio_Branco")
now = datetime.now()
print("Now in:")
print("Brussels    ", now.astimezone(brussels))
print("New York    ", now.astimezone(new_york))
print("Tokyo       ", now.astimezone(tokyo))
print("\nNow in Brazil:")
print("Rio Branco  ", now.astimezone(rio_branco))
print("Manaus      ", now.astimezone(manaus))
print("Brasilia    ", now.astimezone(brasilia))
