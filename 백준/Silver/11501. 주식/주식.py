import sys
input = sys.stdin.readline
for _ in range(int(input())):
    day_n = int(input())
    stocks = list(map(int,input().split()))
    max_stock = 0
    result = 0
    for stock in stocks[::-1]:
        max_stock = max(max_stock, stock)
        if max_stock > stock:
            result += max_stock-stock
    print(result)