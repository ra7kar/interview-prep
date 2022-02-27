# Bill division - Problem from hacker rank.
# details of the problem can be got from the below url.
# https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def bon_appetit(bill, k, b):
    """program details are in the url supplied above

    Args:
        bill (list[int]): cost of individual items eaten at the restaurant
        k (int): index of item not eaten by Anna
        b (int): amount charged by Brian to Anna as a split amount of the bill
    return:
        (int): amount that Brian has to refund to Anna if changed more, else
        print Bon Appetit
    """

    bill_total = sum(bill)
    actual_amount = (bill_total - bill[k]) / 2

    if actual_amount == b:
        return "Bon Appetit"

    else:
        return int(b - actual_amount)


# ----------------
def main():
    bill = [10, 20, 30, 40]
    k = 1
    b = 40
    print(bon_appetit(bill, k, b))


if __name__ == "__main__":
    main()
