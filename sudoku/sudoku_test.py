# Std
import random

# External
import pytest

# Internal
import sudoku
from validate_sudoku import validate_sudoku_board


NUM_BOARDS = 10
SQUARE_SIZE = 9


def generate_board():
    num_init_cells = random.randint(1, 3 * SQUARE_SIZE)
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
    solution = sudoku.solve(board)
    assert validate_sudoku_board(solution), "Invalid solution: {}".format(solution)
