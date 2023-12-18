import math
import os
import random
import re
import sys


def utopianTree(n):
    current_height = 1
    for cyc_num in range(n):
        if cyc_num % 2 == 0:
            current_height *= 2
        else:
            current_height += 1
    return current_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
