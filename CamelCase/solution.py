#!/bin/python3

import math
import os
import random
import re
import sys


def camelcase(s):
    counter_upper = 0
    for char in s:
        if char.isupper():
            counter_upper += 1
    return counter_upper + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
