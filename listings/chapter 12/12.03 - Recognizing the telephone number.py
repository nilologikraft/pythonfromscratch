##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/12.03 - Recognizing the telephone number.py
##############################################################################
sentence = "Buy it for $50.72. Call (92) 5431-2201 now before 10/12/2033."
output = []
phone = []
def number(entry, qmin, qmax):
    num = 0
    for character in entry:
        if character.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return True, 0, num - 1
    return False, -1, -1
def ldc(entry):
    state = position = 0
    ldc_code = []
    while position < len(entry):
        character = entry[position]
        if state == 0 and character == "(":
            state = 1
            ldc_code.append(character)
        elif state == 1:
            found, start, end = number(entry[position:], 2, 3)
            if found:
                lcd_code.append(entry[position + start: position + end + 1])
                state = 2
                position += end
            else:
                break
        elif state == 2:
            if character == ")":
                return True, 0, position
            break
        else:
            break
        position += 1
    return False, -1, -1
for position in range(len(sentence)):
    found, start, end = ldc(sentence[position:])
    if found:
        print(f"LDC found in positions: {position+start} to {position+end}")
        print(sentence[position + start: position + end + 1])
