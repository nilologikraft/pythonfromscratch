##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-12.py.py
##############################################################################
#
# Tic Tac Toe
#

# The board
board = """               Positions
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""
# A list of positions (row and column) for each valid game position
# An extra element was added to facilitate index manipulation
# and so that they have the same value as the position
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3

positions = [
    None,  # Element added to facilitate indices
    (5, 1),  # 1
    (5, 5),  # 2
    (5, 9),  # 3
    (3, 1),  # 4
    (3, 5),  # 5
    (3, 9),  # 6
    (1, 1),  # 7
    (1, 5),  # 8
    (1, 9),  # 9
]

# Positions that lead to winning the game
# Moves making a row, column or diagonals win
# The numbers represent the winning positions
winning = [
    [1, 2, 3],  # Rows
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],  # Columns
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],  # Diagonals
    [1, 5, 9],
]

# Build the board from strings
# generating a list of lists that can be modified
board_grid = []
for line in board.splitlines():
    board_grid.append(list(line))

player = "X"  # Start playing with X
playing = True
moves = 0  # Move counter - used to know if it's a draw
while True:
    for t in board_grid:  # Print the board
        print("".join(t))
    if not playing:  # End after printing the last board
        break
    if moves == 9:  # If 9 moves were made, all positions have been filled
        print("It's a draw! No one won.")
        break
    move = int(input(f"Enter position to play 1-9 (player {player}):"))
    if move < 1 or move > 9:
        print("Invalid position")
        continue
    # Check if the position is free
    if board_grid[positions[move][0]][positions[move][1]] != " ":
        print("Position occupied.")
        continue
    # Mark the move for the player
    board_grid[positions[move][0]][positions[move][1]] = player
    # Check if won
    for p in winning:
        for x in p:
            if board_grid[positions[x][0]][positions[x][1]] != player:
                break
        else:  # If the for loop ends without break, all positions in p belong to the same player
            print(f"Player {player} won ({p}): ")
            playing = False
            break
    player = "X" if player == "O" else "O"  # Switch player
    moves += 1  # Move counter

# About coordinate conversion:
# board_grid[positions[x][0]][positions[x][1]]
#
# Since board_grid is a list of lists, we can access each character
# by specifying a row and column. To get the row and column based on
# the played position, we use the positions list which returns a tuple with 2 elements:
# row and column. Where row is element [0] and column is element [1].
# What these lines do is convert a game position (1-9)
# into board rows and columns. Note that in this example we use the board as
# move memory, in addition to displaying the current game state.
