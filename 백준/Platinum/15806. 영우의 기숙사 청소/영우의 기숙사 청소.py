from collections import deque

N, M, K, t = map(int, input().split())
directions = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2), (2, -1), (2, 1)]
q = deque()
check = []
visited = [[[False] * 2 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    q.append((a - 1, b - 1, 0))
    visited[a - 1][b - 1][0] = True

for _ in range(K):
    c, d = map(int, input().split())
    check.append((c - 1, d - 1))

while q:
    x, y, day = q.popleft()
    if day >= t:
        continue

    spread_flag = False
    for d in range(8):
        nx, ny = x + directions[d][0], y + directions[d][1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny][(day + 1) % 2]:
            visited[nx][ny][(day + 1) % 2] = True
            q.append((nx, ny, day + 1))
            spread_flag = True

    if not spread_flag:
        visited[x][y][day % 2] = False

c = t % 2
for cx, cy in check:
    if visited[cx][cy][c]:
        print("YES")
        exit(0)

print("NO")
