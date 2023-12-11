#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    num_between_sets = set()
    min_multiple_b = sorted(b)[0]
    for num_b in b:
        for num_a in a:
            pot_num_between = num_b / num_a
            if num_b % num_a == 0 and pot_num_between <= min_multiple_b:
                num_between_sets.add(pot_num_between)
    num_between_sets_final = set()
    for num_b in b:
        for num in num_between_sets:
            if num_b % num == 0:
                num_between_sets_final.add(num)
    return len(num_between_sets_final)





# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
