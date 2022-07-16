# magic square, hacker rank problem.
# https://www.hackerrank.com/challenges/magic-square-forming/problem

import sys


def magic_square(s):

    s = sum(s, [])  # convert 2d list to 1d list

    magic_l = [
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
    ]
    minimum_cost = sys.maxsize
    for mag in magic_l:
        diff = 0
        for i, j in zip(s, mag):
            diff += abs(i - j)
        minimum_cost = min(minimum_cost, diff)

    return minimum_cost


def main():

    s = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

    print(magic_square(s))


if __name__ == "__main__":
    main()
