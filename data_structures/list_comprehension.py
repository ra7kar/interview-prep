# list compression


def list_comp(x, y, z, n):
    """Usage of list comprehansion to improve readability and ease of code

    Args:
        x (int): x coordinate of a cuboid
        y (int): y coordinate of a cuboid
        z (int): z coordinate of a cuboid
        n (int): n is the number which acts as a filter, where sum of i+j+k
            should not equal to n. where i, j, k are number range for x,y,z

    Returns:
        [list]: returns the list of numbers without the items in the filter.
    """
    l_list = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    return l_list


if __name__ == "__main__":

    l_list = list_comp(1, 1, 1, 2)
    print(l_list)
