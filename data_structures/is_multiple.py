# is multiple of a number.
# numbers n and m, where n = mi.
# return true if n is a multiple of m else return false.


def is_multiple(n, m):
    ret_val = False
    for i in range(1, n + 1):
        if n / i == m:
            ret_val = True

    return ret_val


if __name__ == "__main__":

    n = 100
    m = 5

    print("The number is {}, which is divided by {}".format(n, m))
    print("Multiple is {}".format(int(n / m) if is_multiple(n, m) else "None"))
