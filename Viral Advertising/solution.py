import math
import os
import math


def viralAdvertising(n):
    cumulative = 0
    current_likes = math.floor(5 / 2)
    for day in range(n):
        cumulative += current_likes
        current_likes = math.floor(current_likes * 3 / 2)
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
