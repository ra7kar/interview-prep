# Beautiful says at the movies
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#


def reverse(i):
    str_i = str(i)
    reverse_i = "".join(reversed(str_i))

    return int(reverse_i)


def beautiful_days(i, j, k):
    count = 0

    for x in range(i, j + 1):
        xx = reverse(x)
        if abs(x - xx) % k == 0:
            count += 1

    return count


def main():
    i = 20
    j = 23
    k = 6
    print(beautiful_days(i, j, k))


if __name__ == "__main__":
    main()
