import os
from itertools import groupby


def sockMerchant(n, ar):
    socks_pair = 0
    ar.sort()
    grouped_socks = [{key: len(list(group))} for key, group in groupby(ar)]
    for color in grouped_socks:
        for key, value in color.items():
            if value % 2 == 0:
                socks_pair += value / 2
            else:
                socks_pair += (value - 1) / 2
    return int(socks_pair)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
