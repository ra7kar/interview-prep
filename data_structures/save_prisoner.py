# Save prisoner. Hacker rank problem.
# https://www.hackerrank.com/challenges/save-the-prisoner/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def save_prisoner(n, m, s):
    """Hacker rank problem
    Args:
        n (int): Number of prisoners
        m (int): Number of candies
        s (int): starting chair number
    """
    res = s + m - 1
    res %= n
    if res == 0:
        return n
    else:
        return res


def main():

    n = 5
    m = 3
    s = 3

    print(save_prisoner(n, m, s))


if __name__ == "__main__":
    main()
