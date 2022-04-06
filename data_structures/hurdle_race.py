# Hurdle race, hacker rank problem.
# https://www.hackerrank.com/challenges/the-hurdle-race/problem?h_r=next-challenge&h_v=zen


def hurdle_race(k, height):

    max_hurdle = max(height)

    return max(max_hurdle - k, 0)


def main():
    k = 7
    height = [2, 5, 4, 5, 2]
    print(hurdle_race(k, height))


if __name__ == "__main__":
    main()
