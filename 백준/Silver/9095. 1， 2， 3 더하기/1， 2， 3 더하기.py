T=int(input())
dp=[1,1,2]
n = [int(input()) for _ in range(T)]
for _ in range(max(n)-2):
    dp.append(dp[-1]+dp[-2]+dp[-3])
[print(dp[i]) for i in n]