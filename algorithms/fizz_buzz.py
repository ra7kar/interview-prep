# fizz_buff
# For numbers 1 to 100 for every multiple of 3 print Fizz
# for every multiple of 5 print Buzz
# for every multiple of 3 x 5 pring FizzBuss


def fizz_buzz(n):

    for i in range(n):

        if i % 3 == 0:
            print("Buzz " + str(i))
        if i % 5 == 0:
            print("Fizz " + str(i))
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz " + str(i))


fizz_buzz(25)
