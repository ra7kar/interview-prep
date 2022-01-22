# mini-max-sum of an array of 5 elements. HackerRank problem


def min_max_sum(py_list):
    """program finds the min of the array, max of the array and returns
    the (sum - min) and (sum - max) valuse of the array.
    Standart max, min and sum functions are not use to optimize the program and
    generate the result in one loop i.e O(n)

    Args:
        py_list (list[int]): list of intigers

    Returns:
        [type]: [description]
    """
    s = 0
    min = max = py_list[0]
    for i in py_list:  # Sum of valuses in the list.
        s += i
        if i > max:  # Find max value in the py_list.
            max = i
        if i < min:  # Find min value in the py_list.
            min = i

    print(s - max, end=" ")
    print(s - min)

    return (s - max, s - min)


# --------------
def main():
    py_list = [1, 3, 5, 6]
    py_list = [7, 69, 2, 221, 8974]
    print(min_max_sum(py_list))


if __name__ == "__main__":
    main()
