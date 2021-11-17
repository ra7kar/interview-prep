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
        [8, 7, 4, 5, 6, 9, 2, 3, 1],
        [5, 6, 1, 3, 4, 2, 8, 7, 9],
        [2, 9, 3, 8, 1, 7, 4, 5, 6],
        [3, 2, 9, 6, 7, 5, 1, 4, 8],
        [4, 5, 6, 1, 2, 8, 3, 9, 7],
        [1, 8, 7, 4, 9, 3, 5, 6, 2],
        [6, 1, 2, 9, 5, 4, 7, 8, 3],
        [7, 4, 8, 2, 3, 6, 9, 1, 5],
        [9, 3, 5, 7, 8, 1, 6, 2, 4],
    ]

    # board 2
    board2 = [
        [1, 2, 3, 4, 5, 7, 6, 8, 9],
        [4, 7, 5, 8, 6, 9, 1, 2, 3],
        [6, 8, 9, 1, 2, 3, 5, 4, 7],
        [3, 1, 2, 7, 9, 6, 8, 5, 4],
        [9, 4, 8, 5, 3, 1, 7, 6, 2],
        [5, 6, 7, 2, 4, 8, 3, 9, 1],
        [2, 9, 6, 3, 1, 5, 4, 7, 8],
        [8, 3, 4, 6, 7, 2, 9, 1, 5],
        [7, 5, 1, 9, 8, 4, 2, 3, 6],
    ]

    # board 3
    board = [
        [7, 5, 8, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [5, 8, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [8, 7, 5, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7],
    ]

    result = validate_sudoku_board(board)

    print("" * 2)
    print("-" * 32)
    print(
        "Sudoku board FAILED the test" if not result else "Sudoku Board PASSED the test"
    )
    print("-" * 32)
    print("")
    print("Pretty print the board")
    print("-" * 30)

    pprint(board)
    pprint(result)
