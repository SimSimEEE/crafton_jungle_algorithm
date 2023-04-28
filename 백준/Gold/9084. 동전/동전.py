import sys
input = sys.stdin.readline

for _ in range(int(input())):
    coin_cnt = int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    DP = [1] + [0]*M
    for coin in coins:
        for i in range(coin,M+1):
            DP[i] += DP[i-coin]
    print(DP[M])