# repeated string, hacker rank problem.
# https://www.hackerrank.com/challenges/repeated-string/problem?h_r=next-challenge&h_v=zen


def rep_string(s, n):

    s_len = len(s)
    total = 0

    if s_len < n:
        for i in s:
            if i == "a":
                total += 1

        total = (n // s_len) * total

    for i in s[: n % s_len]:
        if i == "a":
            total += 1

    return total


def main():
    s = "aba"
    n = 10
    print(rep_string(s, n))


if __name__ == "__main__":
    main()
