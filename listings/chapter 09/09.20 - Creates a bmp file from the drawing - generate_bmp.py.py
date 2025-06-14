##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.20 - Creates a bmp file from the drawing - generate_bmp.py.py
##############################################################################
FILE = "image_python.bmp"
def bytes_little_endian(number, nbytes=4, signal=False):
    """Converts an integer into a sequence of bytes using the little-endian encoding.
    If signal is passed, reserve one bit to represent the signal. """
    return number.to_bytes(nbytes, "little", signed=signal)
def padding(value, size=4):
    """Calculate the next multiple for size"""
    if rest := value % size:
        return value + size - rest
    return value
# Letter to color conversion table
# in RGB format (red, green, blue)
# Each color component can vary from 0 to 255.
letter_to_color = {
    " ": (0, 0, 0),  # black
    "r": (255, 0, 0),  # red
    "g": (0, 255, 0),  # green
    "b": (0, 0, 255),  # blue
}
# Drawing that we will transform into an image
drawing = [
    "  rrrr r r bbbbb b    b   ggggg   g    g  r",
    "  r  r r r   b   b    b  g     g  gg   g  r",
    "  r  r r r   b   b    b  g r r g  g g  g  r",
    "  rrr   r    b   bbbbbb  g     g  g  g g  r",
    "  r     r    b   b    b  gr b rg  g  g g   ",
    "  r     r    b   b    b  g rrr g  g   gg  r",
    "  r     r    b   b    b   ggggg   g    g  r",
]
# Point multiplier
# Each dot will be copied multiple times (multiplier) in the image
# If equal to 4, each point generates a block of 4 x 4 points
multiplier = 32
# Check if all the lines are the same size
drawing_width = len(drawing[0])
for line, z in enumerate(drawing):
    if len(z) != drawing_width:
        raise ValueError(
            "Lines must be the same size. Line with different width: {line + 1} instead of {len(z)}"
        )
# Calculate the data based on the multiplier
expand_drawing = []
for line in drawing:
    new_line = []
    for letter in line:
        new_line.append(letter * multiplier)
    for _ in range(multiplier):
        expand_drawing.append("".join(new_line))
width = len(expand_drawing[0])  # Number of columns in the image
height = len(expand_drawing)  # Number of lines in the image
# Check if the letters represent the colors
binary_data = []
for line in expand_drawing:
    binary_line = []
    for character in line:
        # We use [::-1] to reverse the order of the colors to match the BMP format
        binary_line.append(bytes(letter_to_color[character] [::-1]))
    binary_data.append(b"".join(binary_line))
# Add padding
width_bytes = width * 3
width_with_padding = padding(width_bytes)
if width_bytes != width_with_padding:
    for p, d in enumerate(binary_data):
        binary_data[p] = b"".join(
            [binary_data[p], bytes(width_with_padding - width_bytes)]
        )
# Calculate the size in bytes of the image with padding
size = padding(width * 3) * height
bmp_header = [
    b"BM",  # Identifier
    bytes_little_endian(54 + size),  # Image size in bytes
    bytes(4),  # 4 bytes 0x00
    bytes_little_endian(54),  # Headers size
]
dib_header = [
    bytes_little_endian(40),  # DIB header size
    bytes_little_endian(width),
    bytes_little_endian(-height,
                        signal=True),  # Negative height to mount the image from top to bottom
    bytes_little_endian(1, 2),  # Color planes
    bytes_little_endian(24, 2),  # Bits per point
    bytes_little_endian(0),  # Uncompressed
    bytes_little_endian(size),
    bytes_little_endian(2835),  # text(72 dpi x 39.3701 in/m) horizontal
    bytes_little_endian(2835),  # ceiling(72 dpi x 39.3701 in/m) vertical
    bytes_little_endian(0),  # Number of colors in the palette
    bytes_little_endian(0),  # Important colors
]
binary_bmp_header = b"".join(bmp_header)
binary_dib_header = b"".join(dib_header)
binary_data = b"".join(binary_data)
# Check the size of each binary header
assert len(binary_bmp_header) == 14
assert len(binary_dib_header) == 40
assert len(binary_data) == size
# Save the image
with open(FILE, "wb") as f:
    f.write(binary_bmp_header)
    f.write(binary_dib_header)
    f.write(binary_data)

print(f"File {FILE} generated. {width=} x {height=} {size=} bytes")
