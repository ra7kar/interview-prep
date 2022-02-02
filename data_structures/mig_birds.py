# Migratory birds: Hacker rank problem
# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen


def migratory_birds(bird_list):
    """for details of the program refer Hacker rank url above"""

    ln = max(bird_list) + 1

    l_list = [0] * ln

    for i in range(len(bird_list)):

        l_list[bird_list[i]] += 1

    return l_list.index(max(l_list))


# ---------------------------
def main():
    bird_list = [1, 1, 2, 20, 1, 3, 3, 3, 7]
    bird_list = [1, 2, 3, 6, 6, 7, 20, 4, 5, 4, 3, 2, 1, 3, 4]
    print(migratory_birds(bird_list))


if __name__ == "__main__":
    main()
