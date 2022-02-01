# divisible sum pair: Hacker rank problem.
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


def divisible_sum_pairs(n, k, ar):
    """for details pls refer the url above

    Args:
        n (int): int
        k (int): int
        ar (list[int]): array

    Returns:
        [type]: [description]
    """

    count = 0

    for i in range(n):
        for j in range(n):
            if (ar[i] + ar[j]) % k == 0 and i < j:
                count += 1

    return count


# ----------------
def main():

    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    print(divisible_sum_pairs(n, k, ar))


if __name__ == "__main__":
    main()
