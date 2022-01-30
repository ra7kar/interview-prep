# Breaking the record: Hacker rank problem.


def breaking_record(py_list):
    """Breaking the record, hacker rank problem
        https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem

    Args:
        py_list (list[int]): list of scores for the season.

    Returns:
        [list[int]]:
    """

    min_count = max_count = 0
    min_value = max_value = py_list[0]

    for i in py_list:
        if i < min_value:
            min_count += 1
            min_value = i
        if i > max_value:
            max_count += 1
            max_value = i

    return [max_count, min_count]


# ------------
def main():
    py_list = [12, 24, 10, 24]  # [1, 1]
    py_list = [10, 5, 20, 20, 4, 5, 2, 25, 1]  # [2, 4]
    py_list = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]  # [4, 0]

    print(breaking_record(py_list))


if __name__ == "__main__":
    main()
