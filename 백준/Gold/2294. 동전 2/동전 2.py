import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted(list(set(int(input()) for _ in range(n))))

dp = [float("inf")]*(k+1)

dp[0] = 0

for i in range(k+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] == float("inf"):
    print(-1)
else:
    print(dp[k])