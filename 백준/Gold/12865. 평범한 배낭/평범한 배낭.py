N, K = map(int, input().split())
DP = [[0]*(K+1) for _ in range(N+1)]
stuff = [[0, 0]] + list(list(map(int, input().split())) for _ in range(N))

weight_sum = 0
for j in range(1, K+1):
    for i in range(1, N+1):
        weight, value = stuff[i]
        if j - weight >= 0:
            DP[i][j] = max(DP[i-1][j-weight] + value, DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][K])