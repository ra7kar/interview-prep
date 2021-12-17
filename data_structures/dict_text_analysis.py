# dictionaries for text analysis in a file.

import argparse

parser = argparse.ArgumentParser(description="Find word count in a file")
parser.add_argument(
    "-f",
    "--file_name",
    default="test2.txt",
    type=str,
    help="File name with path if not in local dir",
)
args = parser.parse_args()


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
    # file_name = "test2.txt"
    count = text_analysis(args.file_name)
    filtered = {key: value for key, value in count.items() if value < 20}
    print(filtered)
