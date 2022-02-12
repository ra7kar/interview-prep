# Quick sort (qs). qs is an example of O(n log(n)) complaxity.


def partition(arr, l_idx, r_idx):

    pivot = arr[r_idx]
    i = l_idx - 1
    # [3,-2,-1,0,2,4,1]
    for j in range(l_idx, r_idx):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    i += 1
    arr[i], arr[r_idx] = arr[r_idx], arr[i]

    return i


def quick_sort(arr, l_idx, r_idx):
    """Quick sort sorts a given array

    Args:
        arr (list[int]): list of integer to sort
        l (int): index of the starting element of the array
        r (int): index of the last element of the array

    Returns:
        list[int]: sorted array
    """

    if l_idx >= r_idx:
        return arr

    pivot = partition(arr, l_idx, r_idx)
    quick_sort(arr, l_idx, pivot - 1)
    quick_sort(arr, pivot + 1, r_idx)

    return arr


# ----------------------------------
def main():

    arr = [1, -2, -11, 10, 2, 14, 3]
    l_idx = 0
    r_idx = len(arr) - 1
    print(arr)
    print(quick_sort(arr, l_idx, r_idx))


if __name__ == "__main__":
    main()
