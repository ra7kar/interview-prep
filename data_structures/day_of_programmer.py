# Day of programmer, problem from Hacker rank
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=next-challenge&h_v=zen


def day_of_programmer(year):
    if year == 1918:
        return "26.09.1918"
    elif (year < 1917 and year % 4 == 0) or (
        year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
    ):
        return "12.09.%s" % year
    else:
        return "13.09.%s" % year


# -----------------------
def main():

    y = 2016

    print(day_of_programmer(y))


if __name__ == "__main__":
    main()
