# with respect to position, list valid chess piece moves

# External
from abc import ABCMeta, abstractmethod


def is_valid_position(row, col):
    """Validate if row/col are within limits of chess board

    Args:
        row (int): row position of the chess piece
        col (int): column position of the chess piece

    Returns:
        boolean: if valid return True, else False
    """

    if row > 8 or row < 1:
        return False

    if col > 8 or col < 1:
        return False

    return True


class ChessPiece(metaclass=ABCMeta):
    """Abstract base class of Chess piece

    Args:
        metaclass (ABC, optional): Defaults to ABCMeta.
    """

    def __init__(self, row, col):

        if row > 8 or row < 1:
            raise ValueError("Row is not in valid range")
        self.row = row

        if col > 8 or col < 1:
            raise ValueError("Col is not in valid range")
        self.col = col

    def get_position(self):
        return (self.row, self.col)

    def set_name(self):
        self.name = type(self).__name__

    def get_name(self):
        if not hasattr(self, "name"):
            self.set_name()
        return self.name

    @abstractmethod
    def get_valid_moves(self):
        raise NotImplementedError


class King(ChessPiece):
    """King chess piece

    Args:
        ChessPiece (ABC): ABC for chess piece
    """

    def get_valid_moves(self):
        row, col = self.get_position()
        valid_moves = []

        for r_shift in [-1, 0, 1]:
            for c_shift in [-1, 0, 1]:

                new_r = row + r_shift
                new_c = col + c_shift

                if is_valid_position(new_r, new_c):
                    if (new_r, new_c) != (row, col):
                        valid_moves.append((new_r, new_c))

        return valid_moves


class Bishop(ChessPiece):
    """Bishop chess piece

    Args:
        ChessPiece (ABC): ABC of chess piece
    """

    def get_valid_moves(self):
        row, col = self.get_position()
        valid_moves = []

        for r_shift in [-1, 1]:
            for c_shift in [-1, 1]:

                new_r = row
                new_c = col

                while is_valid_position(new_r, new_c):
                    if (new_r, new_c) != (row, col):
                        valid_moves.append((new_r, new_c))

                    new_r = new_r + r_shift
                    new_c = new_c + c_shift

        return valid_moves


class Queen(ChessPiece):
    """Queen chess piece"""

    def get_valid_moves(self):
        valid_moves = []
        row, col = self.get_position()

        for r_shift in [-1, 0, 1]:
            for c_shift in [-1, 0, 1]:
                if r_shift == 0 and c_shift == 0:
                    continue

                new_r, new_c = row, col

                while is_valid_position(new_r, new_c):
                    if (new_r, new_c) != (row, col):
                        valid_moves.append((new_r, new_c))

                    new_r = new_r + r_shift
                    new_c = new_c + c_shift

        return valid_moves


# ----------

row = 8
col = 8

print("-" * 75)
king = King(row, col)
print("")
print(
    "Initial Position of the " + king.get_name() + " is : " + str(king.get_position())
)
print("-" * 40)

print(king.get_valid_moves())
print("-" * 75)
print("")
# --------------------
print("")
bishop = Bishop(row, col)
print(
    "Initial Position of the "
    + bishop.get_name()
    + " is : "
    + str(bishop.get_position())
)
print("-" * 40)

print(bishop.get_valid_moves())
print("-" * 75)
print("")
# --------------------
print("")
queen = Queen(row, col)
print(
    "Initial Position of the " + queen.get_name() + " is : " + str(queen.get_position())
)
print("-" * 40)

print(queen.get_valid_moves())
print("-" * 75)
print("")
# ------------------------------
