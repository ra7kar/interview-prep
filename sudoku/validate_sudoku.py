""" validate sudoku board
    input is a board
    Return True if board is correct
    Return False if board is incorrect
"""


def validate_sudoko_board(board):

    board_len = len(board)

    # # check row numbers for duplicates
    seen = {}
    for row in board:
        for col in row:
            if col not in seen:
                seen[col] = 1
            else:
                return False
            
        seen={}
    
    # check columns for duplicates
    seen = {}
    for col in range(board_len):
        for row in board:
            if row[col] not in seen:
                seen[row[col]] = 1
            else:
                return False
 
        seen = {}

    # check the box for duplicates
    for row in range(board_len):
        first_box = {}
        second_box = {}
        third_box = {}
        for col in range(board_len):
            val = board[row][col]
            square = col // 3
            if square == 0 :
                if val in first_box:
                    return False
                else:
                    first_box[val]=1

            if square == 1 :
                if val in second_box:
                    return False
                else:
                    second_box[val]=1

            if square == 2 :
                if val in third_box:
                    return False
                else:
                    third_box[val]=1

    return True
        

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



