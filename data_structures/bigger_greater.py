# Bigger is Greater, hacker rank problem.
# https://www.hackerrank.com/challenges/bigger-is-greater/problem


def bigger_is_greater(w):

    n = len(w)
    w = list(w)
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        result = "no answer"
    else:
        j = n - 1
        while j >= i and w[j] <= w[i]:
            j -= 1

        # swap i and j
        w[i], w[j] = w[j], w[i]

        result = w[: i + 1] + w[i + 1 :][::-1]

    result = "".join(result)

    return result


def main():

    w = "ab"
    w = "abca"
    w = "dkhc"
    w = "bb"
    w = "dkhc"
    print("-" * 25)
    print(w)
    print(bigger_is_greater(w))
    print("-" * 25)

    pass


if __name__ == "__main__":
    main()
