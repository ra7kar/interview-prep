# generator example

# first we will implement a regular function to generated Factors. The we will
# implement the a generator of Factors.


def factors(k):
    ret_list = []
    for i in range(1, k + 1):
        if k % i == 0:
            ret_list.append(i)

    return ret_list


k = 100
py_list = factors(k)
print("List generated from a regular function")
print(py_list)


def factors_gen(k):
    for i in range(1, k + 1):
        if k % i == 0:
            yield i


print("number which is a factor")
for factor in factors_gen(k):
    print(factor, end=", ")
