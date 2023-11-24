
def plusMinus(arr):
    positive_int = []
    negative_int = []
    for x in arr:
        if x > 0:
            positive_int.append(x)
        elif x < 0:
            negative_int.append(x)
    print(round(len(positive_int)/len(arr), 6))
    print(round(len(negative_int)/len(arr), 6))
    print(round(1-(len(positive_int)/len(arr) + len(negative_int)/len(arr)), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)