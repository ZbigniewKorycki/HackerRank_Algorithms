import os


def breakingRecords(scores):
    max_break = 0
    min_break = 0
    max_record = scores[0]
    min_record = scores[0]
    for score in scores[1:]:
        if score > max_record:
            max_record = score
            max_break += 1
        elif score < min_record:
            min_record = score
            min_break += 1
    return max_break, min_break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
