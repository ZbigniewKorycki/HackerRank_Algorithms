import os

def compareTriplets(a, b):
    result_a = 0
    result_b = 0
    for category_index in range(3):
        if a[category_index] > b[category_index]:
            result_a += 1
        elif a[category_index] < b[category_index]:
            result_b += 1
    return [result_a, result_b]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
