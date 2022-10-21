# cut sticks, hacker rank problem.
# https://www.hackerrank.com/challenges/cut-the-sticks/problem

from collections import Counter


def cut_the_stick(arr):

    ret_val = []
    arr_counter = Counter(arr)
    len_arr = len(arr)

    for i in sorted(arr_counter.keys()):

        ret_val.append(len_arr)
        len_arr -= arr_counter[i]

    return ret_val


def main():

    arr = [5, 4, 4, 2, 2, 8]
    arr = [5, 4, 4, 2, 2, 8]
    arr = [1, 2, 3, 4, 3, 3, 2, 1]
    print(cut_the_stick(arr))


if __name__ == "__main__":
    main()
