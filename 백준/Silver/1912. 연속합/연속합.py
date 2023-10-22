n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] * n
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print(max(dp))