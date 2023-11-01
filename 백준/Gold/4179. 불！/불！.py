from collections import deque
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
fire = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            start = (i, j)
        elif graph[i][j] == 'F':
            fire.append((i, j))
q = deque()
q.append(start)
visited = [[0] * c for _ in range(r)]
visited[start[0]][start[1]] = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while q:
    ln = len(q)
    fire_ln = len(fire)
    for i in range(fire_ln):
        x, y = fire.pop(0)
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                fire.append((nx, ny))
    for i in range(ln):
        x, y = q.popleft()
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            print(visited[x][y])
            exit(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
else:
    print("IMPOSSIBLE")