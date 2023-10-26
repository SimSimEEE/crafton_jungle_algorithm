r, c, k = map(int, input().split())
maps = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
result = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(x, y, cnt):
    global result
    if (x, y) == (0, c - 1) and cnt == k:
        result += 1
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] == '.':
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = 0


visited[r - 1][0] = 1
dfs(r - 1, 0, 1)
print(result)