import os
from itertools import groupby
def migratoryBirds(arr):
    sorted_num = sorted(arr)
    grouped_num = {key: list(group) for key, group in groupby(sorted_num)}
    max_bird_id = 0
    counter_occur_bird_id = 0
    for key, group in grouped_num.items():
        if len(group) > counter_occur_bird_id:
            counter_occur_bird_id = len(group)
            max_bird_id = key
        elif len(group) == counter_occur_bird_id:
            if key < max_bird_id:
                max_bird_id = key
        else:
            continue
    return max_bird_id



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
