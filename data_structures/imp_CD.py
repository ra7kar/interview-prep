# Simulate cd command and display results after series of input commands.

from collections import deque


def imp_cd(cur_path, commands):

    stack = deque(cur_path.split("/"))

    def check_slash(i):
        """Replace '../' commands with '..'."""
        if "../" in i:

            for n in range(len(i)):
                if i[n] == "../":
                    i[n] = ".."

        return i

    for i in commands:
        i = check_slash(i)  # check and replace '../' with '..'
        parts = i.split("/")

        for c in parts:
            if c == "/" or c == "":
                stack = deque("/")
            elif c == "..":
                stack.pop()
                if len(stack) == 0:
                    stack.append("/")
            else:
                stack.append(c)

    path = ""
    for i in stack:
        if i == "/":
            path += "/"
        else:
            path += i + "/"

    return path


def main():

    cur_path = "/Users/rct/src/interview-prep/data_structures"

    commands = ["../.."]
    commands = ["../..", "data_structure"]
    # commands = ['../..', 'data_structure', '/']
    # commands = ['../..', 'data_structure', '/User/rct', '..', '/', \
    #               '/User/src/test', 'abc']
    commands = ["../..", "data_structure", "/User/rct", "..", "/", "test", "abc"]
    # commands = ['../..', 'data_structure', '/User/rct', '../', '/', \
    #               'test', '../', 'abc']

    print("")
    print("-" * 20)
    print(cur_path)
    print(imp_cd(cur_path, commands))


if __name__ == "__main__":
    main()
