# Append delete , hacker rank problem
# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen


def append_delete(s, t, k):

    s_len = len(s)
    t_len = len(t)
    total_len = s_len + t_len
    count = 0

    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    # 2 Cases to solve the problem:
    # total_len <= 2*count + k and total_len %2 == k%2 YES
    # total_len <= k YES

    if total_len <= 2 * count + k and total_len % 2 == k % 2 or total_len <= k:
        return "Yes"
    else:
        return "No"


def main():
    s = "abcd"
    f = "defg"
    k = 7
    print(append_delete(s, f, k))


if __name__ == "__main__":
    main()
