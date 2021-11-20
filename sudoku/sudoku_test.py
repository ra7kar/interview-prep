# Std
import pprint
import random

# External
import pytest

# Internal
import sudoku
from validate_sudoku import validate_sudoku_board


NUM_BOARDS = 9
SQUARE_SIZE = 9


def generate_board():
    # TODO: #14 - Add support for randomly generating valid sudoku boards to solve
    num_init_cells = 1
    cords = {
        (random.randint(0, SQUARE_SIZE - 1), random.randint(0, SQUARE_SIZE - 1))
        for _ in range(num_init_cells)
    }

    grid = [[0 for _ in range(9)] for _ in range(9)]

    for cord in cords:
        r, c = cord
        choices = {i for i in range(1, SQUARE_SIZE + 1)}
        while True:
            assert len(choices) > 0
            pick = random.choice(tuple(choices))
            choices.remove(pick)
            grid[r][c] = pick
            if validate_sudoku_board(grid):
                break
    return grid


@pytest.mark.parametrize("board", [generate_board() for _ in range(NUM_BOARDS)])
def test_random_sudoku(board):
    pprint.pprint(board)
    status, solution = sudoku.solve_board(board)
    pprint.pprint(solution)
    assert status and validate_sudoku_board(solution), "Invalid solution:\n{}".format(
        pprint.pformat(solution)
    )
