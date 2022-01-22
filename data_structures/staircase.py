# Staircase - Hackerrank problem


def staircase(n):
    """Print a staircase with # character right justified

    Args:
        n (int): print # n times

    Returns:
        list: list of #
    """

    l_list = []
    for i in range(n):

        s = "#" * (i + 1)
        print(s.rjust(n))
        l_list.append(s.rjust(n))

    return l_list


# ----------------------
def main():
    n = 6
    print(staircase(n))


if __name__ == "__main__":
    main()
