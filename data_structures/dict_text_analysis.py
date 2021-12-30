# dictionaries for text analysis in a file.

import os


def text_analysis(file_name):

    file1 = open(file_name, "r")
    d = dict()
    for line in file1:
        words = line.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d


if __name__ == "__main__":
    file_name = os.path.dirname(__file__) + "/test1.txt"
    count = text_analysis(file_name)
    filtered = {key: value for key, value in count.items() if value < 20}
    print(filtered)
