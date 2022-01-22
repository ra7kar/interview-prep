# Grading students - hacker rank problem


def students_grades(py_list):
    """Program performs rounding of grades as per hacker rank problem

    Args:
        py_list (list[int]): each entry is a student grade from 0-100

    Returns:
        list[int]: rounded off grades as per rules in hacker rank problem
    """

    ret_val = []
    for i in py_list:
        # condition 1
        if i < 38:
            ret_val.append(i)
            continue
        # condition 2
        n = i % 5
        if n >= 3:
            ret_val.append(i + (5 - n))
            continue
        # condition 3
        if n < 3:
            ret_val.append(i)

    return ret_val


# ------------------
def main():
    py_list = [37, 38, 39, 40, 81, 82, 83, 84, 85, 100]
    py_list = [39, 40, 81, 82, 83, 84, 85]
    print(py_list)
    ret_val = students_grades(py_list)
    print(ret_val)


if __name__ == "__main__":
    main()
