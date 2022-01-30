# subarray division: Hacker rank problem
# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen


def birthday(s, d, m):
    """This is a Hacker rank problem, pls refer url above for details

    Args:
        s (list[int]): chocolate squares
        d (int): day of the birthday
        m (int): month of the birthday

    return: int
    """
    count = 0
    total = sum(s[:m])
    if total == d:
        count += 1

    for i in range(m, len(s)):
        total += s[i]
        total -= s[i - m]
        if total == d:
            count += 1

    return count


# ---------------
def main():

    s = [1, 2, 1, 3, 2]
    d = 3  # birthday
    m = 2  # month

    print(birthday(s, d, m))


if __name__ == "__main__":
    main()
