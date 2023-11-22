n = int(input())
dp = list([1] * 10 for _ in range(n))
    
for i in range(1, 10):
    for j in range(1, n):
        dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

print(sum(dp[n - 1]) % 10007)