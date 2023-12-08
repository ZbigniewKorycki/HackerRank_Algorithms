#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    max_height = 0
    counter = 0
    for cand in candles:
        if cand > max_height:
            max_height = cand
            counter = 1
        elif cand == max_height:
            counter += 1
        else:
            continue
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
