n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]
ln_list = []
before_vip = 0
for cnt_vip in vip:
    ln_list.append(cnt_vip - before_vip - 1)
    before_vip = cnt_vip
ln_list.append(n - before_vip)
dp = [0] * (max(ln_list) + 1)
dp[0] = 1
for i in range(1, max(ln_list) + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
ans = 1
for i in ln_list:
    ans *= dp[i]
print(ans)