# Apples and oranges: Hacker rank problem.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """For the details of the problem pls refer Hackerrank site.

    Args:
        s (int): Starting boundary of the house on left side of x axis
        t (int): Ending boundary of the house on the right side of x axis
        a (int): location of apple tree on x axis
        b (int): location of the orange tree on x axis
        apples (list[int]): distance from the tree where the apple fell
        oranges (list[int]): distance from the tree where the orange fell
    """

    apple_count = orange_count = 0

    for i in apples:
        apple_fell_at = a + i
        if apple_fell_at >= s and apple_fell_at <= t:
            apple_count += 1

    for i in oranges:
        orange_fell_at = b + i
        if orange_fell_at >= s and orange_fell_at <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)
    return (apple_count, orange_count)


# ----------------------
def main():
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6]
    print(countApplesAndOranges(s, t, a, b, apples, oranges))


if __name__ == "__main__":
    main()
