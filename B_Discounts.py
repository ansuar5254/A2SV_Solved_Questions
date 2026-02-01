t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    vouchers = list(map(int, input().split()))

    prices.sort()
    vouchers.sort()

    total = sum(prices)
    idx = n - 1  

    for x in vouchers:
        if idx < 0:
            break
        free_index = idx - (x - 1)
        if free_index >= 0:
            total -= prices[free_index]
        idx -= x

    print(total)
