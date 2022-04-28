# Sequence equation: Hacker rank problem.
# https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=internal-search


def permutation_equation(p):
    result = []
    len_p = len(p)

    for i in range(1, len_p + 1):
        result.append(p.index(p.index(i) + 1) + 1)

    return result


def main():

    p = [4, 3, 5, 1, 2]
    p = [5, 2, 1, 3, 4]
    p = [2, 3, 1]

    print(p)
    print(permutation_equation(p))


if __name__ == "__main__":
    main()
