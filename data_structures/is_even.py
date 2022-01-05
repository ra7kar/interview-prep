# Find if a number is even or odd,
# without using the mod, div or multiplication operators.

from enum import Enum


class Options(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


def is_even(n, option):

    # using Bit wise AND operation
    if option == "AND":
        if n & 1 == 1:
            return False  # ODD
        return True  # EVEN

    # using bit wise OR operation
    if option == "OR":
        if n | 1 > n:
            return True
        return False

    # using bit wise XOR operation
    if option == "XOR":
        if n ^ 1 < n:
            return False
        return True


if __name__ == "__main__":

    option = Options.AND.value  # AND

    n = 100

    ret_val = is_even(n, option)
    print("")
    print("Selected number is : {}".format(n))
    print("Number is          : {}".format("Even" if ret_val else "Odd"))
    print("Option used        : {}".format(option))
