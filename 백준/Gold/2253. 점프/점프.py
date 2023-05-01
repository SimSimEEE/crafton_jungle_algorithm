N, M = map(int, input().split())
max_speed = int((2*N+1/4)**0.5)+1
INF = float("INF")
dp = list([INF]*(max_speed+1) for _ in range(N+1))
small_stone = list(int(input()) for _ in range(M))
dp[1][0] = 0
for step in range(2, N+1):
    if step in small_stone:
        continue
    for speed in range(1, max_speed):
        dp[step][speed] = min(dp[step-speed][speed-1],
                              dp[step-speed][speed], dp[step-speed][speed+1])+1
result = min(dp[N])
print(result if result != INF else -1)