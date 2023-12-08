import os

def diagonalDifference(arr):
    from_left_up = 0
    from_right_up = 0
    index_to_take_right_up = len(arr) - 1
    index_to_take_left_up = 0
    for line in arr:
        from_left_up += line[index_to_take_left_up]
        from_right_up += line[index_to_take_right_up]
        index_to_take_left_up += 1
        index_to_take_right_up -= 1
    return abs(from_left_up - from_right_up)


# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
