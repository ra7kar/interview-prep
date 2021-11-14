# Sudoku Solver

# find empy cell
def find_empty(board):
    """This function returns row col position if that cell is 0
    else will return True

    Args:
        board (list of lists): sudoku board values

    Return:
        returns a tuple if empyt cell is found, else
        will return True as the not found.
    """

    board_len = len(board)

    for row in range(board_len):
        for col in range(board_len):
            if board[row][col] == 0:
                return (row, col)

    return False


def print_board(board):
    """This function print the sudoku board in a readable format
    from the list of lists input

    Args:
        board (list of lists): sudoku board input
    """
    board_len = len(board)
    print("")
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

    print("")


def validate(board, num, pos):
    """Check the board for duplicates if the input num is entered in pos
    Args:
        board (list of lists): sudoku board
        num (int): number to be entered in the board
        pos (tuple): row and column of the position where the new
        number has to be added
    Return:
        False if duplicate number is found
        True if the num can be entered as a new number in the board
    """

    board_len = len(board)
    row, col = pos

    # check duplicate numbers in rows
    for i in range(board_len):
        val = board[row][i]
        if val == num and col != i:
            return False

    # check duplicate numbers in columns
    for i in range(board_len):
        val = board[i][col]
        if val == num and row != i:
            return False

    # check duplicate numbers in the box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):  # i refers to rows
        for j in range(box_col * 3, box_col * 3 + 3):  # j refers to columns
            val = board[i][j]
            if val == num and (i, j) != (row, pos):
                return False

    return True


def solve(board):

    if solve_helper(board):
        return board


def solve_helper(board):
    """Solve sudoku puzzle.

    Args:
        board (list[list[int]]): sudoku board
    """
    board_len = len(board)
    find = find_empty(board)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, board_len + 1):
        if validate(board, i, find):
            board[row][col] = i

            if solve_helper(board):
                return True

            board[row][col] = 0

    return False


if __name__ == "__main__":

    board = [
        [0, 7, 4, 0, 6, 0, 0, 0, 1],
        [0, 0, 1, 3, 0, 2, 8, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 7, 0, 1, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    print_board(board)
    a = solve(board)
    print("----Result---" * 2)
    print_board(board)
    print(a)
