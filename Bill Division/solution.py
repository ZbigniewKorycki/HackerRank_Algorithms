def bonAppetit(bill, k, b):
    cost_of_products_without_k = sum(bill) - bill[k]
    if cost_of_products_without_k / 2 == b:
        print("Bon Appetit")
    else:
        print(int(b - cost_of_products_without_k/2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
