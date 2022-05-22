# Encryption, hacker rank problem.
# https://www.hackerrank.com/challenges/encryption/problem

from math import ceil, floor, sqrt


def encryption(s):
    # generate a new string without spaces
    s1 = s.replace(" ", "")
    s1_len = len(s1)
    s1_sqrt = sqrt(s1_len)
    s1_floor = floor(s1_sqrt)
    s1_ceil = ceil(s1_sqrt)
    result = []

    # arrive at the rows and columns of the matrix.
    if s1_floor * s1_ceil < s1_len:
        m = max(s1_floor, s1_ceil)
        cols = m
    else:
        cols = s1_ceil

    # get character from string at every cols valuse and transport is to to rows
    for i in range(cols):
        temp = []
        j = 0

        while i + j < s1_len:
            temp.append(s1[i + j])
            j += cols

        result.append("".join(temp))

    # convert it to required output format.
    ret_val = ""
    for i in result:
        ret_val += i + " "

    return ret_val


def main():
    s = "feed the dog"
    s = "chill out"
    s = "if man was meant to stay on the ground god would have given us roots"
    s = "have a nice day"
    print("-" * 25)
    print("Input string : " + s)
    print("-" * 2)
    print("Encrypted string : ", end="")
    print(encryption(s))

    print("-" * 25)


if __name__ == "__main__":
    main()
