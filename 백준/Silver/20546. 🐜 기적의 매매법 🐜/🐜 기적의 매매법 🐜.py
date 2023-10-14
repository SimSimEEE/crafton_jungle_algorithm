money = int(input())
stocks = list(map(int, input().split()))
timing = 0
bnp = 0
money2 = money
for stock in stocks:
    if stock <= money:
        buy = money // stock
        timing += buy
        money -= stock * buy
timing = money + stock * timing
stock_price = []
for i in range(1, len(stocks)):
    if stocks[i - 1] < stocks[i]:
        stock_price.append(1)
    elif stocks[i - 1] > stocks[i]:
        stock_price.append(-1)
    else:
        stock_price.append(0)
    if len(stock_price) == 3:
        if stock_price == [1, 1, 1]:
            money2 += stock * bnp
            bnp = 0
        elif stock_price == [-1, -1, -1]:
            buy = money2 // stocks[i]
            bnp += buy
            money2 -= stocks[i] * buy
        stock_price.pop(0)
bnp = money2 + stock * bnp
if timing < bnp:
    print('TIMING')
elif timing > bnp:
    print('BNP')
else:
    print('SAMESAME')