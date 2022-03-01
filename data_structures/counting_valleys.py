# Counting Valleys, hacker rank problem.
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def counting_valleys(steps, path):

    valleys = sea_level = 0

    for i in path:
        if sea_level == 0 and i == "D":
            valleys += 1
            sea_level -= 1
        elif i == "D":
            sea_level -= 1
        elif i == "U":
            sea_level += 1

    return valleys


# -------------------
def main():

    steps = 8
    path = "UDDDUDUU"

    steps = 12
    path = "DDUUDDUDUUUD"
    print(counting_valleys(steps, path))


if __name__ == "__main__":
    main()
