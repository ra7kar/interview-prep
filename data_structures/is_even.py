# Find if a number is even or odd,
# without using the mod, div or multiplication operators.

from enum import Enum


class Operations(Enum):
    AND = 0
    OR = 1
    XOR = 2


def is_even(n, option):

    # using Bit wise AND operation
    if option == Operations.AND:

        return not (n & 1 == 1)
        # if n & 1 == 1:
        #     return False  # ODD
        # return True  # EVEN

    # using bit wise OR operation
    if option == Operations.OR:

        return n | 1 > n
        # if n | 1 > n:
        #     return True
        # return False

    # using bit wise XOR operation
    if option == Operations.XOR:

        return not (n ^ 1 < n)

        # if n ^ 1 < n:
        #     return False
        # return True


if __name__ == "__main__":

    option = Operations.XOR  # AND

    n = 99

    ret_val = is_even(n, option)
    print("")
    print("Selected number is : {}".format(n))
    print("Number is          : {}".format("Even" if ret_val else "Odd"))
    print("Option used        : {}".format(option.name))
