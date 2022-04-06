# Climbing the leader board, Hacker rank problem.
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


def climbing_leaderboard(ranked, player):

    scores = list(set(ranked))
    scores.sort()
    n = len(scores)
    i = 0
    result = []

    for player_score in player:
        while i < n and scores[i] <= player_score:
            i += 1
        result.append(n - i + 1)

    print(result)


def main():

    ranked = [130, 90, 90, 80]
    player = [70, 80, 105]

    climbing_leaderboard(ranked, player)


if __name__ == "__main__":
    main()
