# Given two arrays and a target,
# return a tuple of the pair which sums equal or first closest to the target
# length of both arrays are equal
# e.g. [1,4,8], [2,6,8] target=11
# return value will be a tuple (4,6)
# e.g. [2,6,5], [2,3,7] target=8
# return value will be a tuple (5,3)


def two_arrays(arr1, arr2, target):
    arr1_sorted = sorted(arr1)
    arr2_sorted = sorted(arr2)

    n = len(arr1_sorted)
    i = 0
    j = n - 1
    smallest_diff = abs(arr1_sorted[0] + arr2_sorted[0] - target)
    closest_val = (arr1_sorted[0], arr2_sorted[0])
    if smallest_diff == target:
        return closest_val

    while i < n and j >= 0:
        v1 = arr1_sorted[i]
        v2 = arr2_sorted[j]
        x = abs(v1 + v2 - target)
        if x < smallest_diff:
            smallest_diff = x
            closest_val = (v1, v2)

        if smallest_diff == 0:
            return closest_val
        elif (v1 + v2) < target:
            i += 1
        elif (v1 + v2) > target:
            j -= 1

    return closest_val


# ---------------------
def main():
    arr1 = [7, 4, 1, 10]
    arr2 = [4, 5, 8, 7]
    arr1 = [2, 5, 7, 8]
    arr2 = [8, 5, 7, 1]
    target = 11
    arr1 = [2, 5, 7, 8]
    arr2 = [8, 5, 7, 1]
    target = 13
    print(two_arrays(arr1, arr2, target))


if __name__ == "__main__":
    main()
