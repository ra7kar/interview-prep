# drawing_book problem from hacker rank
# https://www.hackerrank.com/challenges/drawing-book/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#
#


def drawing_book(n, p):
    front = p // 2

    if n % 2 == 1:
        back = (n - p) // 2
    else:
        back = (n - p + 1) // 2

    return min(front, back)


# --------------------------------
def main():

    n = 7
    p = 4
    print(drawing_book(n, p))


if __name__ == "__main__":
    main()
