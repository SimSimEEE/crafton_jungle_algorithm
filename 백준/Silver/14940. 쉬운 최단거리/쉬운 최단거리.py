n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            x, y = i, j
bfs(x, y)
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
for i in range(n):
    print(*visited[i])
