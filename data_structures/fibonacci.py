# Fibonacci sequence.


def fib_seq(n):
    py_list = []
    a, b = 0, 1

    for i in range(1, n + 1):
        py_list.append(a)
        a, b = b, a + b

    return py_list


# --------------------
def main():
    n = 5
    print(fib_seq(n))


if __name__ == "__main__":
    main()
