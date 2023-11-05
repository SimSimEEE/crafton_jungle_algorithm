n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * n 
dp[0] = 1
for i in range(n - 1):
    for j in range(i + 1, n):
        if (j - i) * (1 + abs(a[i] - a[j])) <= k and dp[i] != 0:
            dp[j] = 1
print("YES" if dp[-1] else "NO")