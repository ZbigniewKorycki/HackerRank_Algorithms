def staircase(n):
    for x in range(1, n + 1):
        print(str("#" * x).rjust(n))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
