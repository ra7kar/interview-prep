# ACM ICPC world finance meet, hacker rank problem.
# https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true


def acm_meet(topics):

    max_subjects = 0
    count = 0

    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            val1 = topics[i]
            val2 = topics[j]
            sub_max_subject = 0
            for x, y in zip(val1, val2):
                sub_max_subject += 1 if x == "1" or y == "1" else 0

            if sub_max_subject > max_subjects:
                max_subjects = sub_max_subject
                count = 1
            elif sub_max_subject == max_subjects:
                count += 1

    return [max_subjects, count]


def main():

    topics = ["10101", "11110", "00010"]
    topics = ["10101", "11100", "11010", "00101"]
    topics = ["11101", "10101", "11001", "10111", "10000", "01110"]

    print(acm_meet(topics))

    pass


if __name__ == "__main__":
    main()
