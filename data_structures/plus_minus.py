# hacker rank problem Plus Minus

"""Given an array of integers, calculate the ratios of its elements that
    are positive, negative, and zero. Print the decimal value of each
    fraction on a new line with  places after the decimal.
"""


def plus_minus(py_list):

    # declare a set
    ret_val = []
    py_list_len = len(py_list)

    # get count of +ve, -ve and 0's
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
