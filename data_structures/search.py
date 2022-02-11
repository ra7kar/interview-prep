# Program explaining linear search and binary search

from enum import Enum


class Search_Type(Enum):
    BINARY = "B"
    LINEAR = "L"


def search(search_type, search_number, py_list):
    """This program displays Linear search and Binary search for the same
    input array, to steady the BigO(N) and BigO(logN)
    O(N) is for linear search of an array
    O(LogN) is for Binary search of an array

    Args:
        search_type (string): Valuse indicates if search is Linear or Binary
        L = Linear, B = Binary
        search_number (int): Number to search
        py_list (list[int]): list of intigers to search in

    Returns:
        Boolean : True if search number id found else False.
    """

    n = len(py_list)

    if search_type == Search_Type.LINEAR:
        for i in range(n):
            if py_list[i] == search_number:
                return True
        return False

    else:
        # [1,2,3,4,5,6]
        start = 0
        end = n - 1

        def binary_search(start, end, search_number, py_list):
            mid_idx = (start + end) // 2
            # Base case
            if start > end:
                return False

            if py_list[mid_idx] == search_number:
                return True

            if py_list[mid_idx] > search_number:
                end = mid_idx - 1
                ret_val = binary_search(start, end, search_number, py_list)
            elif py_list[mid_idx] < search_number:
                start = mid_idx + 1
                ret_val = binary_search(start, end, search_number, py_list)

            return ret_val

        return binary_search(start, end, search_number, py_list)


# ---------------------
def main():

    search_type = Search_Type.BINARY  # L = linear search, B = Binary search
    search_number = -1
    py_list = [1, 2, 3, 4, 5, 6]
    print(search(search_type, search_number, py_list))


if __name__ == "__main__":
    main()
