# sherlock and squares, Hacker rank problem.
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# first approach.
def squares_1(a, b):

    count = 0
    for i in range(1, b + 1, 1):

        j = i * i

        if j >= a and j <= b:
            print(j)
            count += 1
        elif j > b:
            break
        else:
            continue

    print("-- Count " + "-" * 10)
    return count


def main():
    a = 17
    b = 25

    print("")
    print("Square numbers")
    print("-" * 15)

    print(squares_1(a, b))


if __name__ == "__main__":
    main()
