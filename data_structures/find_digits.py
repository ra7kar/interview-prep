# Find Digits, Hacker rank problem.
# https://www.hackerrank.com/challenges/find-digits/problem?h_r=internal-search&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def find_digits(n):

    n_str = str(n)
    count = 0

    for i in range(0, len(n_str), 1):
        val = int(n_str[i : i + 1])
        if val != 0 and n % val == 0:
            count += 1

    return count


def main():

    n = 10
    n = 124
    n = 1110
    print(find_digits(n))


if __name__ == "__main__":
    main()
