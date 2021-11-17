# solve sudoku puzzle
import copy


def solve_board(input_board):
    """Solve a sudoku puzzle

    Args:
        input_board (list of list[int]): list of lists with integers
        representing the sudoku board

    Returns:
        tuple : status of solution and the sudoku board
    """
    board = copy.deepcopy(input_board)
    if solve_helper(board):
        return (True, board)

    return (False, board)


def find_empty_spot(board):
    """Find the empty spot in the board

    Args:
        board (list of list[int]): sudoku board, which is a list of lists

    Returns:
        Tuple and None: Tuple is returned when a empty spot is found
        else a None is returned
    """
    board_len = len(board)

    for row in range(board_len):
        for col in range(board_len):
            if board[row][col] == 0:
                return (row, col)

    return (None, None)  # no empty slots remaining in the board


def is_valid(board, guess, row, col):
    """Validated is the guess (int) is valid input to solve the sudoku
    puzzle

    Args:
        board (list of lists): sudoku board
        guess (int): number attempted to add to the sudoku board
        row (int): row possition where the Zero spot was found
        col (int): col possition where the Zero spot was found

    Returns:
        boolean: Return True if valid else return False"""

    # lets start checking for duplicates with the row
    row_val = board[row]
    if guess in row_val:
        return False

    # lets check the column values for duplicates
    col_val = [board[i][col] for i in range(len(board))]

    if guess in col_val:
        return False

    # check for duplicated in the box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False

    return True


def solve_helper(board):
    """A helper function to sudoku puzzle solver

    Args:
        board (list of lists[int]): helper function

    Returns:
        boolean: returns True if guessed number to be added is correct
        else will return a False
    """

    board_len = len(board)

    # Step 1 - check empyt spot in the board
    row, col = find_empty_spot(board)

    if row is None:
        return True  # puzzle is resolved

    # Step 2 - if there is a empty slot to put a number, we validate it
    for guess in range(1, board_len + 1):
        # step 3 - check if this is a valid guess
        if is_valid(board, guess, row, col):
            board[row][col] = guess

            if solve_helper(board):
                return True

        board[row][col] = 0

    return False


def print_board(board):
    """Print the sudoku board

    Args:
        board (list of lists): sudoku board, list of list[int]
    """
    board_len = len(board)

    for row in range(board_len):
        if row % 3 == 0 and row != 0:
            print("-" * 25)
        for col in range(board_len):
            val = board[row][col]
            if col % 3 == 0 and col != 0:
                print(" | ", end=" ")
            if col == 8:
                print(val)
            else:
                print(val, end=" ")


if __name__ == "__main__":

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 8, 5, 0, 0, 0, 0, 2],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 4, 0, 0],
        [8, 0, 4, 0, 0, 0, 9, 1, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    print_board(board)
    result = solve_board(board)
    print("-" * 5 + "Result" + "-" * 5)
    # print_board(result)
    print(result)
