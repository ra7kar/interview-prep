# designer pdf viewer, hacker rank problem
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def design_pdf_viewer(h, word):
    height = 0

    for letter in word:
        height = max(height, h[ord(letter) - ord("a")])

    return height * len(word)


def main():

    h = [1, 3, 5, 3, 5, 7, 8, 6, 4, 3, 3, 2, 4, 2, 3, 6, 7, 5, 9, 2, 3, 4, 6, 3, 6, 8]
    word = "bdef"
    print(design_pdf_viewer(h, word))


if __name__ == "__main__":
    main()
