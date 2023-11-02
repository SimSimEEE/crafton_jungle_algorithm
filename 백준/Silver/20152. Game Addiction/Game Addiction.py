h, n = map(int, input().split())
n = abs(h - n) + 1
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(i, n):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
print(dp[-1][-1])