# find the absolute difference of the diagonal sum of an array.


def diagonal_sum(l_list):
    """Find the absolute difference value of the diagonal sum of an array.

    Args:
        l_list (list[int]): list of ints.
    """
    left_sum = right_sum = 0
    n = len(l_list)
    for i in range(n):
        left_sum += l_list[i][i]
        right_sum += l_list[i][n - i - 1]

    ret_val = abs(left_sum - right_sum)

    return ret_val


# ----------------------
def main():
    l_list = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    ret_val = diagonal_sum(l_list)
    print(ret_val)


if __name__ == "__main__":
    main()
