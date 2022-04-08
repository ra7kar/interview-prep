# Utopian tree, Hacker rank program.
# https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=next-challenge&h_v=zen


def utopian_tree(n):

    s = 0

    for i in range(n + 1):
        s = s + 1 if i % 2 == 0 else s * 2

    return s


def main():

    n = 3
    print(utopian_tree(n))


if __name__ == "__main__":
    main()
