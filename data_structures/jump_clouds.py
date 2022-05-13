# Jumping the Clouds, hacker rank challenge.
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


def jump_clouds(c):

    count = 0
    c_len = len(c)
    i = 0
    while i != c_len:
        if i + 2 < c_len and c[i + 2] == 0:
            count += 1
            i += 2
        elif i + 1 < c_len and c[i + 1] == 0:
            count += 1
            i += 1
        else:
            i += 1

    return count

    pass


def main():

    c = [0, 0, 1, 0, 0, 1, 0]

    print(jump_clouds(c))

    pass


if __name__ == "__main__":
    main()
