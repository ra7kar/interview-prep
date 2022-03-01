# electronic_shop, hacker rank problem
# https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def get_money_spent(keyboards, drives, b):

    ret_val = -1

    for k in keyboards:
        for d in drives:
            if (k + d) <= b and (k + d) > ret_val:
                ret_val = k + d

    return ret_val


# ------------------
def main():
    keyboards = [40, 50, 60]
    drives = [5, 8, 12]
    b = 60
    keyboards = [3, 1]
    drives = [5, 2, 8]
    b = 10
    keyboards = [4]
    drives = [5]
    b = 5
    print(get_money_spent(keyboards, drives, b))


if __name__ == "__main__":
    main()
