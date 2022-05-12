# Non divisible subset, hacker rank problem.
# https://www.hackerrank.com/challenges/non-divisible-subset/problem?h_r=next-challenge&h_v=zen


def non_div_subset(k, s):

    f = [0] * k

    for i in s:
        f[i % k] += 1

    result = min(f[0], 1)
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            result += max(f[i], f[k - i])
        else:
            result += min(f[i], 1)

    return result


def main():

    s = [
        2375782,
        21836421,
        2139842193,
        2138723,
        23816,
        21836219,
        2948784,
        43864923,
        283648327,
        23874673,
    ]
    s = [1, 3, 4, 5, 6]
    k = 4

    s = [1, 7, 2, 4]
    k = 3

    # s= [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575,
    #  436]
    # k = 7

    print(non_div_subset(k, s))


if __name__ == "__main__":
    main()
