# mini-max-sum of an array of 5 elements. HackerRank problem


def min_max_sum(py_list):
    s = 0
    min = max = py_list[0]
    for i in py_list:
        s += i
        if i > max:
            max = i
        if i < min:
            min = i

    print(s - max, end=" ")
    print(s - min)

    return (s - max, s - min)


# --------------
def main():
    py_list = [1, 3, 5, 7, 9, 10, 11]
    py_list = [7, 69, 2, 221, 8974]
    ret_val = min_max_sum(py_list)
    print(ret_val)


if __name__ == "__main__":
    main()
