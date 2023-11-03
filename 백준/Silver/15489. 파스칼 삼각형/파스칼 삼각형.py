r, c, w = map(int, input().split())
dp = [[1] * i for i in range(1, r + w)]
for i in range(1, r + w - 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
result = 0
for i in range(w):
    result += sum(dp[r + i - 1][c - 1:c + i])
print(result)
