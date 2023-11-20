n = int(input())
boj = input()
dp = [float("inf")] * (n + 1)
dp[0] = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        k = j - i
        if boj[i] == 'B' and boj[j] == 'O':
            dp[j] = min(dp[i] + k*k, dp[j])
        elif boj[i] == 'O' and boj[j] == 'J':
            dp[j] = min(dp[i] + k*k, dp[j])
        elif boj[i] == 'J' and boj[j] == 'B':
            dp[j] = min(dp[i] + k*k, dp[j])
print(dp[n - 1] if dp[n - 1] != float("inf") else -1)