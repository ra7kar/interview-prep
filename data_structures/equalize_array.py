# Equalize array, hacker rank problem.
# https://www.hackerrank.com/challenges/equality-in-a-array/problem?h_r=next-challenge&h_v=zen

from collections import Counter


def equalize_arr(arr):
    arr_len = len(arr)
    arr_counter = Counter(arr)

    max_val = max(arr_counter.values())

    return arr_len - max_val


def main():
    arr = [3, 3, 2, 1, 3]
    arr = [1, 2, 3, 1, 2, 3, 3, 3, 9]
    arr = [1, 2, 3, 1, 2, 3, 3, 3]
    print(equalize_arr(arr))


if __name__ == "__main__":
    main()
