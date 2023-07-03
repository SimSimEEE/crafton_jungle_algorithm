from collections import deque
n, m = map(int, input().split())
graph = list(list(input()) for _ in range(m))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

white = 0
black = 0

def bfs(x, y, a):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = -1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == a:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                cnt += 1
    return cnt * cnt
                

for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            white += bfs(i, j, "W")
        if graph[i][j] == "B":
            black += bfs(i, j, "B")
print(white, black)