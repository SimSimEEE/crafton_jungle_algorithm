n, m = map(int, input().split())
d = [0] + list(int(input()) for _ in range(n))
dp = [[0] * (m + 1) for _ in range(n+1)]
for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j - 1] + d[i]
        dp[i][0] = max(dp[i][0], dp[i - j][j])
    # for j in range(1, m + 1):
print(dp[-1][0])
