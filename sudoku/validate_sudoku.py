# Validate sudoku board

from math import sqrt
from pprint import pprint


def validate_sudoku_board(board):
    """Check if a sudoku board is valid.

    Args:
        board (list[list[int]]): Board specified as a 2d array.

    Returns:
        boolean: Return True if board is valid, else return False.
    """

    board_len = len(board)

    # # check for duplicate numbers in ROW
    for row in board:
        seen = set()
        for val in row:
            if val in seen and val != 0:
                return False
            seen.add(val)

    # check for duplicates numbers in COLUMNS
    for col_idx in range(board_len):
        seen = set()
        for row in board:
            val = row[col_idx]
            if val in seen and val != 0:
                return False
            seen.add(val)

    # check the 3x3 box for duplicates in a 9x9 board
    box_size = int(sqrt(board_len))  # box size is 3 x 3
    for row_box in range(box_size):
        for col_box in range(box_size):
            seen = set()
            for row in range(row_box * box_size, (row_box + 1) * box_size):
                for col in range(col_box * box_size, (col_box + 1) * box_size):
                    val = board[row][col]
                    if val in seen and val != 0:
                        return False
                    seen.add(val)

    return True


if __name__ == "__main__":

    board = [
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7],
    ]

    result = validate_sudoku_board(board)

    print("" * 2)
    print("-" * 32)
    print("Sudoku board FAILED test" if not result else "Sudoku Board PASSED the test")
    print("-" * 32)
    print("")
    print("Pretty print the board")
    print("-" * 30)

    pprint(board)
