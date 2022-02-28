# Socks merchant, problem from hacker rank
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def sock_merchant(n, ar):

    count = 0

    dic = {}

    for i in ar:
        dic[i] = dic.get(i, 0) + 1

    for i in dic:
        count += dic[i] // 2

    return count


# ----------------------------------------
def main():

    n = 3
    ar = [1, 2, 1]
    n = 10
    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    print(sock_merchant(n, ar))


if __name__ == "__main__":
    main()
