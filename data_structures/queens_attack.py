# Queens attack, hacker rank problem.
# https://www.hackerrank.com/challenges/queens-attack-2/problem?h_r=next-challenge&h_v=zen


def queens_attack(n, k, r_q, c_q, obstacles):

    total_moves = 0

    obs = {}

    for i, j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j: 1}

    def limit(r, c):
        return True if 1 <= r <= n and 1 <= c <= n else False

    def check(r_q, c_q, r, c):
        count = 0
        r_q += r
        c_q += c
        while limit(r_q, c_q) and obs.get(r_q, {}).get(c_q, 0) == 0:
            count += 1
            r_q += r
            c_q += c

        return count

    r = [1, -1, 0, 0, 1, -1, 1, -1]
    c = [0, 0, -1, 1, -1, -1, 1, 1]

    for i, j in zip(r, c):
        total_moves += check(r_q, c_q, i, j)

    return total_moves


def main():
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [(5, 5), (4, 2), (2, 3)]

    print(queens_attack(n, k, r_q, c_q, obstacles))


if __name__ == "__main__":
    main()
