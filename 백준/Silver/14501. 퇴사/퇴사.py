import sys
input = sys.stdin.readline
n = int(input())
consult = [0] + list(list(map(int,input().split())) for _ in range(n))
dp = [0] * 20
for i in range(1,n+1):
    dp[i] = max(dp[i],dp[i-1])
    dp[i + consult[i][0] - 1] = max(dp[i + consult[i][0] - 1], dp[i-1] + consult[i][1])
    
print(dp[n])