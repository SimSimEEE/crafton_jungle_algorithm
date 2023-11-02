def factorial(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp
dp = factorial(30)
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[m] // (dp[n] * dp[m - n]))