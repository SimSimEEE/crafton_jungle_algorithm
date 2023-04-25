from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]
ripe_tomatoes = deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            ripe_tomatoes.append([i, j])

while ripe_tomatoes:
    x, y = ripe_tomatoes.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
            ripe_tomatoes.append([nx, ny])
            tomato_box[nx][ny] = tomato_box[x][y] + 1

min_day = 0
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 0:
            print(-1)
            exit()
        min_day = max(min_day,tomato_box[i][j])
else:
    print(min_day-1)