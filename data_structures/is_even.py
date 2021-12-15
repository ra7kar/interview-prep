# Find if a number is even or odd,
# without using the mod, div or multiplication operators.


def is_even(n):

    is_even = True
    for _ in range(1, n + 1):
        if is_even:
            is_even = False
        else:
            is_even = True

    return is_even


if __name__ == "__main__":

    n = 11

    ret_val = is_even(n)
    print(ret_val)
    print("Selected number is {} which is {}".format(n, "even" if ret_val else "odd"))
