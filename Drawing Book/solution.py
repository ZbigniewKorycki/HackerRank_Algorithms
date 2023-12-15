import os
import math


def pageCount(n, p):
    is_n_even = False
    if n % 2 == 0:
        is_n_even = True
    if is_n_even:
        if p <= n / 2:
            return math.ceil((p-1)/2)
        else:
            return math.ceil((n-p)/2)
    else:
        if p < n / 2:
            return math.ceil((p-1)/2)
        else:
            return math.floor((n-p)/2)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
