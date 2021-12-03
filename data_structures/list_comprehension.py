# list compression


# def list_comp(x,y,z,n):
#     l_list = []
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if i+j+k != n:
#                     l_list.append([i,j,k])

#     return l_list


def list_comp(x, y, z, n):

    l_list = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    return l_list


l_list = list_comp(1, 1, 1, 2)
print(l_list)
