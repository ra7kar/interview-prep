# Angry Professor, hacker rank problem
# https://www.hackerrank.com/challenges/angry-professor/problem?h_r=next-challenge&h_v=zen


def angry_professor(k, a):

    count = 0

    for i in a:
        count = count + 1 if i <= 0 else count

    return "NO" if count >= k else "YES"


def main():
    k = 2
    a = [-2, -1, 4, 2]
    print(angry_professor(k, a))


if __name__ == "__main__":
    main()
