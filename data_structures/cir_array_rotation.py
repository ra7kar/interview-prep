# Circular Array Rotation. Hacker rank problem.
# https://www.hackerrank.com/challenges/circular-array-rotation/problem


def circular_array_rotation(a, k, queries):
    ret = []
    n = len(a)
    k = k % n
    a = a[-k:] + a[:-k]

    for i in queries:
        ret.append(a[i])

    print(a)
    return ret


def main():

    a = [3, 4, 5, 6, 7]
    k = 3
    queries = [1, 2]

    print(" original list - ")
    print(a)
    print(" Rotate right by : " + str(k))
    print(circular_array_rotation(a, k, queries))


if __name__ == "__main__":
    main()
