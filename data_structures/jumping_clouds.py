# Jumping on clouds, Hacker rank problem.
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?h_r=internal-search&h_r=next-challenge&h_v=zen


def jumping_clouds(c, k):

    result = 100
    i = 0
    n = len(c)

    while True:
        result = result - 1 - 2 * c[i]
        i = (i + k) % n
        if i == 0:
            break

    return result


def main():

    c = [0, 0, 1, 0, 0, 1, 1, 0]
    k = 2
    c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    k = 3
    print(jumping_clouds(c, k))


if __name__ == "__main__":
    main()
