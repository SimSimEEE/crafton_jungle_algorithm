N, M = map(int, input().split())

maxsize = float('inf')
dist = [[maxsize] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

input()  

C = list(map(int, input().split()))
cities = [0] * (N+1)

for X in range(1, N+1):
    maxValue = 0
    for c in C:
        if c == X or dist[c][X] == maxsize or dist[X][c] == maxsize:
            continue
        maxValue = max(maxValue, dist[X][c] + dist[c][X])
    cities[X] = maxValue

target = min(cities[1:])
answer = []

for X in range(1, N+1):
    if cities[X] == target:
        answer.append(X)

print(*answer)
