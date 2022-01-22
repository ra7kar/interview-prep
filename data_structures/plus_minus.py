# Plus Minus: Hacker rank problem

"""Given an array of integers, calculate the ratios of its elements that
    are positive, negative, and zero. Print the decimal value of each
    fraction on a new line with 6 places after the decimal.
"""


def plus_minus(py_list):
    """Given a list, get the +ve, -ve and Zeors count, and find the ratio with
    the length of the list. print 3 ration outputs for each, +ve, -ve and Zero
    in a new line

    Args:
        py_list (list[int]): list of ints

    Returns:
        list[int]: ratio valuse of +ve, -ve and zeros count, with the len
        of the list
    """

    # Initialize output list.
    ret_val = []
    py_list_len = len(py_list)

    # Get count of +ve, -ve and 0's.
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    for i in py_list:
        if i > 0:
            positive_numbers += 1
        if i < 0:
            negative_numbers += 1
        if i == 0:
            zeros += 1

    ret_val.append("{:6f}".format(positive_numbers / py_list_len))
    ret_val.append("{:6f}".format(negative_numbers / py_list_len))
    ret_val.append("{:6f}".format(zeros / py_list_len))

    for i in ret_val:
        print(i)

    return ret_val


# -------------
def main():
    py_list = [-4, 3, -9, 0, 4, 1]
    ret_val = plus_minus(py_list)
    print(ret_val)


if __name__ == "__main__":
    main()
