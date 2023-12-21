import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    arrivals_on_time = [arrival_time for arrival_time in a if arrival_time <= 0]
    return "YES" if len(arrivals_on_time) < k else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
