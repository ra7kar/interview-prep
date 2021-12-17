# Find if a number is even or odd,
# without using the mod, div or multiplication operators.


def is_even(n, option="AND"):

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

    option = "AND"  # AND
    option = "OR"  # OR
    #    option = "XOR"    # XOR

    n = 101

    ret_val = is_even(n, option)
    print("")
    print("Selected number is : {}".format(n))
    print("Number is          : {}".format("Even" if ret_val else "Odd"))
    print("Option used        : {}".format(option))
