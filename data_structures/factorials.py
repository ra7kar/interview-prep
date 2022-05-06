# Extra long factorials, HackerRank problem.
# https://www.hackerrank.com/challenges/extra-long-factorials/problem?h_r=internal-search


def factorial(n):

    if n == 1:
        return 1
    else:
        retval = n * factorial(n - 1)
    return retval


def main():
    n = 4
    print(factorial(n))


if __name__ == "__main__":
    main()
