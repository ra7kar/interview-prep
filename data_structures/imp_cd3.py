# Simulate CD functionality

from collections import deque


def cd(cur_path, commands):
    """Simulate cd for command line.

    Current path is given as input, and a list of commands
    is provided, based on the current path execute each command
    in the command list and return the final path, assume the
    command has valide sub directory paths/names.

    Args:
        cur_path (str): current path
        commands (list(str)): list of commands

    Returns:
        path (str): final path after command are executed.
    """
    stack = deque(cur_path.split("/"))

    for cmd in commands:
        parts = cmd.split("/")

        for i in parts:
            if i == "..":
                stack.pop()
            elif i != "":
                stack.append(i)

    return "/".join(stack)


def main():
    cur_path = "/Users/rct/src/interview-prep/data_structures"
    commands = ["..", "../..", "test", "../", "test2"]

    print("Current path is :" + cur_path)
    print(cd(cur_path, commands))


if __name__ == "__main__":
    main()
