# Taum and Bday, Hacker rank problem.
# https://www.hackerrank.com/challenges/taum-and-bday/problem?h_r=next-challenge&h_v=zen


def taum_bday(b, w, bc, wc, z):

    if wc > bc + z:  # replace wc to bc + Z
        wc = bc + z
    elif bc > wc + z:
        bc = wc + z

    return b * bc + w * wc


def main():
    b = 3  # Black gifts
    bc = 1  # Black gift cost
    w = 3  # White gifts
    wc = 9  # white gift cost
    z = 2  # the cost to convert one color gift to the other color

    b = 7
    w = 7
    bc = 4
    wc = 2
    z = 1

    print(taum_bday(b, w, bc, wc, z))


if __name__ == "__main__":
    main()
