# is multiple of a number.
# numbers n and m, where n = mi.
# return true if n is a multiple of m else return false.


def is_multiple(n, m):

    for i in range(1, n + 1):
        if n / i == m:
            ret_val = i

    return ret_val if ret_val else None


if __name__ == "__main__":

    print(is_multiple(100, 9))
