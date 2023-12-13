import os
from itertools import product

def getMoneySpent(keyboards, drives, b):
    combinations = list(product(keyboards, drives))
    cost_of_products = list(filter(lambda x: x <= b, [sum(cost) for cost in combinations]))
    cost_of_products.sort()
    if cost_of_products:
        return cost_of_products[-1]
    else:
        return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
