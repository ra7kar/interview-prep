# Library fine, hacker rank problem.
# https://www.hackerrank.com/challenges/library-fine/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def library_fine(d1, m1, y1, d2, m2, y2):

    # fine over a year = 10_000 Hacko
    # fine over a month = 500 Hackos
    # fine over a day = 15 Hackos

    # fine for days
    delay_days = d1 - d2
    delay_months = m1 - m2
    delay_years = y1 - y2
    late_fee = 0

    print("Days :" + str(delay_days))
    print("Months :" + str(delay_months))
    print("year :" + str(delay_years))

    if y1 - y2 > 0:
        late_fee += delay_years * 10_000
    elif y1 == y2 and m1 - m2 > 0:
        late_fee += delay_months * 500
    elif y1 == y2 and m1 == m2 and d1 - d2 > 0:
        late_fee = delay_days * 15

    return late_fee


def main():

    d1 = 9
    m1 = 7
    y1 = 2016

    d2 = 6
    m2 = 6
    y2 = 2015

    print("-" * 25)
    fine = library_fine(d1, m1, y1, d2, m2, y2)
    print("-" * 25)
    print("Fine :" + str(fine))


if __name__ == "__main__":
    main()
