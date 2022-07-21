# Beautiful triplets, hacker rank problem.
# https://www.hackerrank.com/challenges/beautiful-triplets/problem

from collections import Counter


def beautiful_triplets(d, arr):
    arr_counter = Counter(arr)
    count = 0

    print(arr_counter)

    for num in arr:
        if arr_counter[num + d] and arr_counter[num + d + d]:
            count += 1

    return count


def main():
    arr = [1, 2, 4, 4, 5, 7, 8, 10]
    d = 3
    print("-" * 5 + " Array ----")
    print(arr)
    print("-" * 5 + " ----")
    print(beautiful_triplets(d, arr))
    pass


if __name__ == "__main__":
    main()
