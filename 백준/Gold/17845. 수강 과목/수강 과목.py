n, k = map(int, input().split())
dp = [[0]*(n + 1) for _ in range(k + 1)]
stuff = [[0, 0]] + list(list(map(int, input().split())) for _ in range(k))
for j in range(1, n+1):
    for i in range(1, k+1):
        v, w = stuff[i]
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[k][n])
