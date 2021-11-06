
# Validate sudoku board

from math import sqrt
from pprint import pprint

def validate_sudoko_board(board):
    """ 
    Return True if board is correct
    Return False if board is incorrect
    """ 

    board_len = len(board)

    # # check for duplicate numbers in ROW
    for row in board:
        seen = set()
        for col in row:
            if col in seen:
                return False
            seen.add(col)
    
    # check for duplicates numbers in COLUMNS
    for col_idx in range(board_len):
        seen = set()
        for row in board:
            if row[col_idx] in seen:
                return False
            seen.add(row[col_idx])

    # check the 3x3 box for duplicates in a 9x9 board
    box_size = int(sqrt(board_len))   # box size is 3 x 3
    for row_box in range(box_size):
        for col_box in range(box_size):
            seen = set() 
            for row in range(row_box*box_size, (row_box+1)*box_size):
                for col in range(col_box*box_size, (col_box+1)*box_size):
                    val = board[row][col]
                    if val in seen:
                        return False
                    seen.add(val)

    return True

def print_board(board):
    board_len = len(board)
    for row in range(board_len):
        if row % 3 == 0 and row != 0:
            print("-"*25)
        for col in range(board_len):

            if col % 3 == 0 and col !=0 :
                print(" | ", end=" ")
          
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" ")
            


board = [[  7,  8,  5, 4,  3,  9, 1,  2,  6],
         [  6,  1,  2, 8,  7,  5, 3,  4,  9],
         [  4,  9,  3, 6,  2,  1, 5,  7,  8],
         [  8,  5,  7, 9,  4,  3, 2,  6,  1],
         [  2,  6,  1, 7,  5,  8, 9,  3,  4],
         [  9,  3,  4, 1,  6,  2, 7,  8,  5],
         [  5,  7,  8, 3,  9,  4, 6,  1,  2],
         [  1,  2,  6, 5,  8,  7, 4,  9,  3],
         [  3,  4,  9, 2,  1,  6, 8,  5,  7]]

result = validate_sudoko_board(board)

print(""*2)
print("-"*32)
print("Sudoku board FAILED test" if not result else "Sudoku Board PASSED the test")
print("-"*32)
print("")
print( "Pritty print the board")
print( "-"*30)

print( "Test print the Board with grids")
pprint(board)
print("")
print( "Test print the Board with grids")
print( "-"*32)
print_board(board)




