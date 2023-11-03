n = int(input())
a = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][a[0]] = 1
for i in range(n - 1):
    for j in range(21):
        if dp[i][j]:
            if 0 <= j + a[i+1] <= 20:
                dp[i+1][j+a[i+1]] += dp[i][j]
            if 0 <= j - a[i+1] <= 20:
                dp[i+1][j-a[i+1]] += dp[i][j]
print(dp[-2][a[-1]])