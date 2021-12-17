# Find if a number is even or odd,
# without using the mod, div or multiplication operators.


def is_even(n):

    # using Bit wise AND operation
    # if n & 1 == 1 :
    #     return False

    # return True

    # using bit wise OR operation
    # if n | 1 > n:
    #     return False
    # return True

    # using bit wise XOR operation
    if n ^ 1 < n:
        return False
    return True


if __name__ == "__main__":

    n = 11

    ret_val = is_even(n)
    print(ret_val)
    print("Selected number is {}, which is {} ".format(n, "even" if ret_val else "odd"))
