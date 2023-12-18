import math
import os
import random
import re
import sys


def pickingNumbers(a):
    a.sort()
    longest_array = 0
    counter = 1
    counter_compared = 0
    lower_num_array = a[0]
    for num in a[1:]:
        if num == lower_num_array:
            counter += 1
        else:
            if num - lower_num_array == 1:
                counter += 1
                counter_compared += 1
            elif num - lower_num_array == 2:
                lower_num_array = num - 1
                counter = counter_compared + 1
                counter_compared = 1
            else:
                lower_num_array = num
                counter = 1
                counter_compared = 0
        if counter > longest_array or counter_compared > longest_array:
            longest_array = max(counter, counter_compared)
    return longest_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
