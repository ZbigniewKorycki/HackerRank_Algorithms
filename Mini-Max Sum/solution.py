def miniMaxSum(arr):
    arr.sort()
    mini_sum = sum(arr[0:4])
    max_sum = sum(arr[1:])
    print(mini_sum, max_sum)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
