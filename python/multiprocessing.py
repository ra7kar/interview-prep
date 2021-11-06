# Multiprocessing
import time
import concurrent.futures


start = time.perf_counter()


def sum_list(ll):
    total = sum(ll)
    return total


if __name__ == "__main__":
    seconds = [5, 4, 3, 2, 1]
    nlist = 100000
    parallel_processes = 10
    split_into = (
        int(nlist / parallel_processes)
        if not nlist % parallel_processes
        else int((nlist / parallel_processes)) + 1
    )

    ll = [n for n in range(1, nlist)]
    new_ll = [ll[x : x + split_into] for x in range(0, len(ll), split_into)]
    # print [data[x:x+10] for x in xrange(0, len(data), 10)]
    f_total = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:

        results = [executor.submit(sum_list, new_ll[n]) for n in range(len(new_ll))]
        # results = [executor.map(sum_list, new_ll[n]) for n in range(len(new_ll))]

        for f in concurrent.futures.as_completed(results):
            f_total += f.result()
            print(f.result())

    # processes = []
    # n=1.5
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[n])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f"Function completed in ->  {round(finish-start, 2)} Sec's")
    print("List :")
    print(ll)
    print("Split count : " + str(split_into))
    print("List total :" + str(f_total))
