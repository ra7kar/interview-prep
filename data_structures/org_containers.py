# Organize Containers. Hacker rank problem.
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem


def org_containers(container):

    len_container = len(container)

    row = [0] * len_container
    col = [0] * len_container

    for i in range(len_container):
        for j in range(len_container):
            row[i] += container[i][j]
            col[i] += container[j][i]

    row.sort()
    col.sort()

    for i in range(len(row)):
        if row[i] == col[i]:
            ret = "Possible"
        else:
            ret = "Impossible"

    return ret


def main():
    containers = [[1, 4], [2, 3]]
    containers = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
    containers = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]

    print(org_containers(containers))


if __name__ == "__main__":
    main()
