##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-44.py.py
##############################################################################
import sys
import json

# Check if both filenames were provided as arguments
if len(sys.argv) != 4:
    print(
        "Usage: python exercise-09-44.py output_file.bmp drawing_file.txt color_table.json"
    )
    sys.exit(1)

output_file = sys.argv[1]
drawing_file = sys.argv[2]
color_file = sys.argv[3]

# Read the drawing from the file
try:
    with open(drawing_file, "r") as f:
        drawing = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Error: Drawing file '{drawing_file}' not found.")
    sys.exit(1)
except IOError:
    print(f"Error: Could not read drawing file '{drawing_file}'.")
    sys.exit(1)

# Load the color table from the JSON file
try:
    with open(color_file, "r") as f:
        letter_to_color = json.load(f)
except FileNotFoundError:
    print(f"Error: Color file '{color_file}' not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: File '{color_file}' does not contain valid JSON.")
    sys.exit(1)

# Verify and build the color table
for char in letter_to_color:
    color = letter_to_color[char]
    if len(color) != 3 or not all(isinstance(x, int) and 0 <= x <= 255 for x in color):
        print(f"Error: Invalid color for character '{char}'")
        sys.exit(1)


def bytes_little_endian(number, nbytes=4, signed=False):
    """Converts an integer to a sequence of bytes using little endian encoding.
    If signed is passed, reserves a bit to represent the sign."""
    return number.to_bytes(nbytes, "little", signed=signed)


def padding(value, size=4):
    """Calculates the next multiple for size"""
    if remainder := value % size:
        return value + size - remainder
    return value


# Point multiplier
# Each point will be copied multiplier times in the image
# If equal to 4, each point generates a 4x4 point block
multiplier = 32

# Check if all lines have the same size
drawing_width = len(drawing[0])

for line, z in enumerate(drawing):
    if len(z) != drawing_width:
        raise ValueError(
            f"Lines must have the same size. Line with different width: {line} instead of {len(z)}"
        )

# Calculate data based on multiplier
expanded_drawing = []
for line in drawing:
    new_line = []
    for letter in line:
        new_line.append(letter * multiplier)
    for _ in range(multiplier):
        expanded_drawing.append("".join(new_line))


width = len(expanded_drawing[0])  # Number of columns in the image
height = len(expanded_drawing)  # Number of lines in the image

# Check if letters represent colors
binary_data = []
for line in expanded_drawing:
    binary_line = []
    for char in line:
        # Invert byte order for BMP RGB format
        binary_line.append(bytes(letter_to_color[char][::-1]))
    binary_data.append(b"".join(binary_line))

# Add padding
width_bytes = width * 3
width_with_padding = padding(width_bytes)
if width_bytes != width_with_padding:
    for p, d in enumerate(binary_data):
        binary_data[p] = b"".join(
            [binary_data[p], bytes(width_with_padding - width_bytes)]
        )

# Calculate image size in bytes with padding
size = padding(width * 3) * height

bmp_header = [
    b"BM",  # Identifier
    bytes_little_endian(54 + size),  # Image size in bytes
    bytes(4),  # 4 bytes 0x00
    bytes_little_endian(54),  # Header size
]

dib_header = [
    bytes_little_endian(40),  # DIB header size
    bytes_little_endian(width),
    bytes_little_endian(
        -height, signed=True
    ),  # Negative height to build image top to bottom
    bytes_little_endian(1, 2),  # Color planes
    bytes_little_endian(24, 2),  # Bits per pixel
    bytes_little_endian(0),  # No compression
    bytes_little_endian(size),
    bytes_little_endian(2835),  # ceil(72 dpi x 39.3701 in/m) horizontal
    bytes_little_endian(2835),  # ceil(72 dpi x 39.3701 in/m) vertical
    bytes_little_endian(0),  # Number of colors in palette
    bytes_little_endian(0),  # Important colors
]

bmp_header_binary = b"".join(bmp_header)
dib_header_binary = b"".join(dib_header)
binary_data = b"".join(binary_data)

# Verify binary header sizes
assert len(bmp_header_binary) == 14
assert len(dib_header_binary) == 40
assert len(binary_data) == size


# Write the image
with open(output_file, "wb") as f:
    f.write(bmp_header_binary)
    f.write(dib_header_binary)
    f.write(binary_data)

print(f"File {output_file} generated. {width=} x {height=} {size=} bytes")
