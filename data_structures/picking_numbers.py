# Picking numbers, Hacker rank problem.
# https://www.hackerrank.com/challenges/picking-numbers/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import Counter


def picking_numbers(a):

    arr = Counter(a)

    maxnum = 0

    for i in range(100):

        maxnum = max(maxnum, arr[i] + arr[i + 1])

    return maxnum


# -------------
def main():

    arr = [1, 2, 4, 4, 4, 5]
    print(picking_numbers(arr))


if __name__ == "__main__":
    main()
