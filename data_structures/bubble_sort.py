# Program for bubble sort.


def bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ------------------------
def main():

    l_list = [4, 7, 1, 8, 3]
    print(l_list)
    print("-" * 20)
    print(bubble_sort(l_list))


if __name__ == "__main__":
    main()
