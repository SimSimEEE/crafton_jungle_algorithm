N = int(input())
matrix = list(list(map(int, input().split())) for _ in range(N))

DP = list([0]*N for _ in range(N))

for length in range(1, N):
    for start in range(N - length):
        end = start + length
        if start != end:
            DP[start][end] = float("inf")
            for mid in range(start, end):
                DP[start][end] = min(DP[start][end], DP[start][mid] + DP[mid+1][end] + matrix[start][0] * matrix[mid][1] * matrix[end][1])
print(DP[0][-1])