# Test cases for Chesspiece valid moves

# Internal
import chess_board

# External
import pytest

row1 = 2
col1 = 2
king_result1 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
bishop_result1 = [
    (1, 1),
    (1, 3),
    (3, 1),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
]
queen_result1 = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (3, 1),
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
]


row2 = 2
col2 = 5
king_result2 = [(1, 4), (1, 5), (1, 6), (2, 4), (2, 6), (3, 4), (3, 5), (3, 6)]
bishop_result2 = [
    (1, 4),
    (1, 6),
    (3, 4),
    (4, 3),
    (5, 2),
    (6, 1),
    (3, 6),
    (4, 7),
    (5, 8),
]
queen_result2 = [
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 4),
    (2, 3),
    (2, 2),
    (2, 1),
    (2, 6),
    (2, 7),
    (2, 8),
    (3, 4),
    (4, 3),
    (5, 2),
    (6, 1),
    (3, 5),
    (4, 5),
    (5, 5),
    (6, 5),
    (7, 5),
    (8, 5),
    (3, 6),
    (4, 7),
    (5, 8),
]

row3 = 8
col3 = 1
king_result3 = [(7, 1), (7, 2), (8, 2)]
bishop_result3 = [(7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)]
queen_result3 = [
    (7, 1),
    (6, 1),
    (5, 1),
    (4, 1),
    (3, 1),
    (2, 1),
    (1, 1),
    (7, 2),
    (6, 3),
    (5, 4),
    (4, 5),
    (3, 6),
    (2, 7),
    (1, 8),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (8, 6),
    (8, 7),
    (8, 8),
]


row4 = 1
col4 = 8
king_result4 = [(1, 7), (2, 7), (2, 8)]
bishop_result4 = [(2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)]
queen_result4 = [
    (1, 7),
    (1, 6),
    (1, 5),
    (1, 4),
    (1, 3),
    (1, 2),
    (1, 1),
    (2, 7),
    (3, 6),
    (4, 5),
    (5, 4),
    (6, 3),
    (7, 2),
    (8, 1),
    (2, 8),
    (3, 8),
    (4, 8),
    (5, 8),
    (6, 8),
    (7, 8),
    (8, 8),
]


@pytest.mark.parametrize(
    "row, col, result",
    [
        (row1, col1, king_result1),
        (row2, col2, king_result2),
        (row3, col3, king_result3),
        (row4, col4, king_result4),
    ],
)
def test_king(row, col, result):
    king = chess_board.King(row, col)
    assert king.get_valid_moves() == result


# Bishop test
@pytest.mark.parametrize(
    "row, col, result",
    [
        (row1, col1, bishop_result1),
        (row2, col2, bishop_result2),
        (row3, col3, bishop_result3),
        (row4, col4, bishop_result4),
    ],
)
def test_bishop(row, col, result):
    bishop = chess_board.Bishop(row, col)
    assert bishop.get_valid_moves() == result


# Queen test
@pytest.mark.parametrize(
    "row, col, result",
    [
        (row1, col1, queen_result1),
        (row2, col2, queen_result2),
        (row3, col3, queen_result3),
        (row4, col4, queen_result4),
    ],
)
def test_queen(row, col, result):
    queen = chess_board.Queen(row, col)
    assert queen.get_valid_moves() == result
