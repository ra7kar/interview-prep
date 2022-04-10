# viral advertising, hacker rank problem.
# https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def viral_adv(days):

    cumulative = 0
    advertized = 5
    liked = 0

    for i in range(1, days + 1):
        liked = advertized // 2
        cumulative += liked
        advertized = liked * 3

    return cumulative


def main():
    n = 4
    print(viral_adv(n))


if __name__ == "__main__":
    main()
