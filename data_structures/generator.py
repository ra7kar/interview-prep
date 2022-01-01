# Implement the a generator of Factors.


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
    print("")
    print("Numbers listed below are factors of : " + str(k))
    ret_val = factor(k)
    print(ret_val)
    print("")
