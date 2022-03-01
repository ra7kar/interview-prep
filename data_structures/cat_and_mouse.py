# Cat and Mouse, hacker rank problem
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def cat_and_mouse(x, y, z):

    pos1 = abs(x - z)
    pos2 = abs(y - z)

    if pos1 == pos2:
        ret_val = "Mouse C"
    elif pos1 > pos2:
        ret_val = "Cat B"
    else:
        ret_val = "Cat A"

    return ret_val


# ----------------------------
def main():

    x = 5
    y = 2
    z = 4

    print(cat_and_mouse(x, y, z))


if __name__ == "__main__":
    main()
