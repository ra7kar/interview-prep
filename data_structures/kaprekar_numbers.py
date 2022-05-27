# Kaprekar numbers, Hacker rank problem.
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem


def kaprekar_numbers(p, q):

    ret_val = []

    for i in range(p, q + 1):

        d = len(str(i))

        sqr = str(i * i)

        if len(sqr) < 2:
            right = int(sqr)
            left = 0
        else:
            r_len = d
            right = int(sqr[-r_len:])
            l_len = len(sqr) - d
            left = int(sqr[:l_len])

        if left + right == i:
            ret_val.append(str(i))

    if ret_val:
        return ret_val
    else:
        return "INVALID RANGE"


def main():

    p = 1
    q = 700

    print(kaprekar_numbers(p, q))


if __name__ == "__main__":
    main()
