# generator example

# first we will implement a regular function to generated Factors. The we will
# implement the a generator of Factors.

"""regular function to generate factors.
def factors(k):
    ret_list = []
    for i in range(1, k + 1):
        if k % i == 0:
            ret_list.append(i)

    return ret_list



py_list = factors(k)
print("List generated from a regular function")
print(py_list)
"""


def factors_gen(k):
    for i in range(1, k + 1):
        if k % i == 0:
            yield i


def factor(k):
    ret_val = []
    for i in factors_gen(k):
        ret_val.append(i)

    return ret_val


if __name__ == "__main__":

    k = 100
    print("number which is a factor")
    ret_val = factor(k)
    print(ret_val)
