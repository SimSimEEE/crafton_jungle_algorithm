n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if not dp[i][j]: continue
        if j - v[i] >= 0: dp[i+1][j-v[i]] = True
        if j + v[i] <= m: dp[i+1][j+v[i]] = True
ans = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        ans = i
        break
print(ans)