# Kangaroo: Hacker rank problem.


def kangaroo(x1, v1, x2, v2):
    """This is a Hacker rank problem, the url below has the details.
    https://www.hackerrank.com/challenges/kangaroo/problem

    Args:
        refer the above url for the below details.
        x1 ([type]): [description]
        v1 ([type]): [description]
        x2 ([type]): [description]
        v2 ([type]): [description]

    Returns:
        [type]: [description]
    """

    if x1 < x2 and v1 < v2:
        return "NO"

    dist_diff = abs(x1 - x2)
    jump_diff = abs(v1 - v2)

    if v1 != v2 and dist_diff % jump_diff == 0:
        return "YES"
    else:
        return "NO"


# --------------------
def main():
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    print(kangaroo(x1, v1, x2, v2))


if __name__ == "__main__":
    main()
