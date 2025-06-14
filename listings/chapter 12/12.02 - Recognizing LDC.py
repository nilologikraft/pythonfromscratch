##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/12.02 - Recognizing LDC.py
##############################################################################
sentence = "Buy it for $50.72. Call (92) 5431-2201 now before 10/12/2033."
output = []
phone = []
def ldc(entry):
    state = 0
    ldc_code = []
    for position, character in enumerate(entry):
        if state == 0 and character == "(":
            state = 1
            ldc_code.append(character)
        elif state == 1 and character.isnumeric() and position <= 3:
            ldc_code.append(character)
        elif state == 1 and character == ")":
            state = 2
            ldc_code.append(character)
            return True, 0, position
        else:
            break
    return False, -1, -1
for position in range(len(sentence)):
    found, start, end = ldc(sentence[position:])
    if found:
        print(f"LDC found in positions: {position+start} to {position+end}")
        print(sentence[position + start: position + end + 1])
